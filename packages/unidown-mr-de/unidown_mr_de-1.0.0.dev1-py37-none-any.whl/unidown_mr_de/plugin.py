import re
import traceback
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path
from typing import Dict, List

import certifi
import urllib3
import urllib3.util
from tqdm import tqdm
from unidown import dynamic_data, tools
from unidown.plugin import APlugin, LinkItem, PluginException, PluginInfo

from unidown_mr_de.exceptions import GetEbookLinksException, NothingFoundInThread
from unidown_mr_de.html_parser.last_update_html_parser import LastUpdateHTMLParser
from unidown_mr_de.html_parser.list_html_parser import ListHTMLParser
from unidown_mr_de.html_parser.thread_html_parser import ThreadHTMLParser


class Plugin(APlugin):
    """
    Plugin class, derived from APlugin.
    """
    _info = PluginInfo('mr_de', '1.0.0', 'www.mobileread.com')

    def __init__(self, options: List[str] = None):
        super().__init__(options)
        self._unit = 'eBook'
        if 'format' in self._options:
            self._options['format'] = self._options['format'].split(',')
        else:
            self._options['format'] = []

        self.threads_path = self.temp_path.joinpath('threads/')
        tools.create_dir_rec(self.threads_path)
        self._unit = 'eBook'

    def _create_download_links(self) -> Dict[str, LinkItem]:
        wiki_thread_dic = self.get_thread_links()  # link: name
        self.log.info('Threads found: ' + str(len(wiki_thread_dic)))

        # DEV, just use five wiki threads
        wiki_thread_dic = {k: wiki_thread_dic[k] for k in wiki_thread_dic.keys()}

        self.download(wiki_thread_dic, self.threads_path, 'Downloading threads', 'thread')
        wiki_thread_dic, lost_dic = self.check_download(wiki_thread_dic, self.threads_path)
        if not wiki_thread_dic:
            raise PluginException("No thread was downloaded successful.")

        link_item_dict = self.get_ebook_links(wiki_thread_dic)
        return link_item_dict

    def _create_last_update_time(self) -> datetime:
        self.log.info('Download thread overview list')
        self.download_wiki_list()
        parser = LastUpdateHTMLParser()
        with self.temp_path.joinpath('main_list.html').open(mode='r', encoding="utf8") as reader:
            parser.feed(reader.read())
        if parser.wiki_list_date == datetime(1970, 1, 1):
            raise PluginException("Something wents wrong with wikilist time.")
        return parser.wiki_list_date

    # -------------------------------------- #

    def get_thread_links(self):
        """
        Extract thread links from the wiki list.

        :rtype: Dict[link, LinkItem]
        """
        thread_dic = {}
        for thread in self.extract_ebook_threads():  # add a download file name for every thread
            thread_dic[thread] = LinkItem(self.link_to_thread(thread), datetime(1970, 1, 1))
        return thread_dic

    @staticmethod
    def link_to_thread(link):
        """
        Convert link of a thread to a name which can be used as file name.

        :param link: link with special character
        :return: new link without special characters
        """
        return link.replace('?', '_').replace('/', '%') + '.html'

    def download_wiki_list(self):
        """
        Download the wiki list.
        """
        with urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where()) as https:
            with https.request('GET', 'https://wiki.mobileread.com/wiki/Free_eBooks-de/de', preload_content=False,
                               retries=urllib3.util.retry.Retry(3)) as load:
                with self.temp_path.joinpath('main_list.html').open(mode='wb') as out_file:
                    out_file.write(load.data)

    def extract_ebook_threads(self):
        """
        Extract the ebook threads from the wiki list.

        :return list with thread links
        """
        parser = ListHTMLParser(self._options['format'])
        with self.temp_path.joinpath('main_list.html').open(mode='r', encoding="utf8") as reader:
            parser.feed(reader.read())
        parser.close()

        return parser.thread_list

    @staticmethod
    def get_ebook_links_from_file(path: Path):
        """
        Extract the ebook attachment links from given file.

        :return dict
        """
        try:
            parser = ThreadHTMLParser()
            with path.open(mode='r', encoding="utf-8", errors='ignore') as reader:
                parser.feed(reader.read())
            parser.close()
            link_item_dict = {}
            for item in parser.link_data_list:
                valid_name = re.sub(r'[^\w\-_. ]', '_', item[1])
                link_item_dict['/forums/attachment.php?attachmentid=' + item[0]] = LinkItem(valid_name, parser.time)
        except Exception:
            raise GetEbookLinksException(path, traceback.format_exc())
        if not link_item_dict:
            raise NothingFoundInThread(path)

        return link_item_dict

    def get_ebook_links(self, link_item_dict: dict):
        """
        Get all ebook links from the threads html with multi processing.

        :return dict[link, LinkItem]
        """
        job_list = []

        with ProcessPoolExecutor(max_workers=self.simul_downloads) as executor:
            for link, item in link_item_dict.items():  # all thread htmls
                path = self.threads_path.joinpath(item.name)
                job = executor.submit(self.get_ebook_links_from_file, path)
                job_list.append(job)

        pbar = tqdm(as_completed(job_list), total=len(job_list), desc='Extract ebook links', unit='thread', leave=True,
                    mininterval=1, ncols=100, disable=dynamic_data.DISABLE_TQDM)
        for _ in pbar:
            pass

        ebook_links = {}
        for job in job_list:  # merge all results into one dict
            try:
                result = job.result()
                for link in result.keys():  # no check if logging at warn level is chosen
                    if link in ebook_links:
                        self.log.warning("Doubled link found: " + self.host + link)
                ebook_links.update(result)
            except NothingFoundInThread as ex:
                self.log.info("Nothing found in " + str(ex.path))
            except GetEbookLinksException as ex:
                self.log.error("Something went wrong in: " + str(ex.path) + ' | ' + ex.orig_ex)
                pbar.write('[Error] Something wents wrong. Please check the log file.')

        return ebook_links

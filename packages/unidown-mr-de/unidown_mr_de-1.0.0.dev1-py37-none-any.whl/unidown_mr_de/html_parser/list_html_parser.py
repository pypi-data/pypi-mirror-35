from html.parser import HTMLParser
from typing import List


class ListHTMLParser(HTMLParser):
    """
    Extractor for the forum threads of the wiki list.

    :param format_list: which formats will be collected
    :type format_list: List[str]

    :ivar format_list: which formats will be collected
    :vartype format_list: List[str]
    :ivar last_link: last detected link
    :vartype last_link: str
    :ivar thread_list: thread list
    :vartype thread_list: List[str]
    """

    def __init__(self, format_list: List[str]):
        HTMLParser.__init__(self)
        self.format_list = format_list
        self.last_link = ''
        self.thread_list = []

    def error(self, message):
        raise Exception(message)

    def handle_starttag(self, tag, attrs):
        """
        Gets the last updated date of the wiki list and last possible thread link.
        """
        # a valid link must be inside of an 'a' tag
        if (tag != 'a') and (tag != 'span'):
            return
        for sub_tag, value in attrs:
            # if href is defined, set last_link
            if (sub_tag == "href") and (tag == 'a'):
                self.last_link = value

    def handle_endtag(self, tag):
        """
        Reset the last possible thread link if leaving the a tag.
        """
        # last_link is empty if outside of an 'a' tag
        if tag == 'a':
            self.last_link = ''

    def handle_data(self, data):
        """
        Check for legal thread link and append them.
        """
        # a valid link must be inside an 'a' tag and data must be a valid format
        # last_link is empty if outside of an 'a' tag
        if not (data.lower() in self.format_list or len(self.format_list) == 0) or (self.last_link == ''):
            return
        # cut the link, only the part after the hostname is needed
        self.last_link = self.last_link[25:]
        # only add unique links
        if self.last_link not in self.thread_list:
            self.thread_list.append(self.last_link)

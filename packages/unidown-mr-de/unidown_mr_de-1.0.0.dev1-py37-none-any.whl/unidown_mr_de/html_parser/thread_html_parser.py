import re
from datetime import datetime, timedelta
from html.parser import HTMLParser


class ThreadHTMLParser(HTMLParser):
    """
    Extractor for the ebook links from the forum threads.
    Checks only the first post for an possible ebook link. (self.in_container > 1)

    :ivar last_link: latest found link
    :vartype last_link: str
    :ivar link_data_list: attachment id and link of the collected resources
    :vartype link_data_list: List[Tuple[str, str]]
    :ivar in_posts: if in post sector
    :vartype in_posts: bool
    :ivar in_continer: if in container sector
    :vartype in_continer: bool
    :ivar in_edit_note_part: if in edit sector
    :vartype in_edit_note_part: bool
    :ivar in_em_tag: if in edit date/ time tag
    :vartype in_em_tag: bool
    :ivar time: time of last editing
    :vartype time: upload time of the resource
    """

    def __init__(self):
        HTMLParser.__init__(self)
        self.last_link = ''
        self.link_data_list = []
        self.in_posts = False  # if in post sector
        self.in_container = 0  # if in container sector
        self.in_edit_note_part = False  # if in edit sector
        self.in_em_tag = False  # if in edit date/ time tag
        self.time = datetime(1970, 1, 1)

    def error(self, message):
        raise Exception(message)

    def handle_comment(self, data):
        """
        Check if in an edit sector and counts the post.
        """
        if not self.in_posts:
            return
        # set if in edit sector
        if data == ' edit note ':
            self.in_edit_note_part = True
        if data == ' / edit note ':
            self.in_edit_note_part = False
        # set if in a post
        if data == ' open content container ':
            self.in_container += 1
        if data == ' / close content container ':
            self.in_container += 1

    def handle_starttag(self, tag, attrs):
        """
        Check if in edit part or post sector and get the last possible ebook link too.
        """
        # set if in post sector
        if tag == 'div':
            for sub_tag, value in attrs:
                if (sub_tag == 'id') and (value == 'posts'):
                    self.in_posts = True
                if (sub_tag == 'id') and (value == 'lastpost'):
                    self.in_posts = False  # stop parser?

        if (self.in_container > 1) or (not self.in_posts):  # if not in post sector and if not in a post
            return

        # a valid link must be inside of an 'a' tag
        if tag == 'a':
            for sub_tag, value in attrs:
                # if href is defined, set last_link
                if sub_tag == 'href':
                    self.last_link = value

        if tag == 'em':
            self.in_em_tag = True

    def handle_endtag(self, tag):
        """
        Check if in edit part or post sector or if outside of an a tag, reset the last possible ebook link.
        """
        if (self.in_container > 1) or (not self.in_posts):  # if not in post sector and if not in a post
            return

        # a valid link must be inside of an 'a' tag
        if tag == 'a':
            self.last_link = ''

        if tag == 'em':
            self.in_em_tag = False

    def handle_data(self, data):
        """
        Check for legal ebook links and gets a possible edit time.
        """
        if (self.in_container > 1) or (not self.in_posts):  # if not in post sector and if not in a post
            return

        # a valid link must be inside an 'a' tag and data must be a valid format
        # last_link is empty if outside of an 'a' tag
        if (self.last_link != '') and ('attachment' in self.last_link):
            self.last_link = re.search(r"attachmentid=(\d)*", self.last_link).group()[13:]
            self.link_data_list.append((self.last_link, data))

        if self.in_em_tag:  # test for possible edit tag
            cur_date_str = re.search(r"(\d\d)-(\d\d)-(\d\d\d\d)", data)
            cur_time_str = re.search(r"(\d\d):(\d\d)", data)
            if cur_date_str is not None:
                cur_date_str = cur_date_str.group().replace('-', '')
                self.time = datetime(int(cur_date_str[-4:]), int(cur_date_str[:2]), int(cur_date_str[2:4]))
                if cur_time_str is not None:
                    cur_time_str = cur_time_str.group().replace(':', '')
                    self.time += timedelta(hours=int(cur_time_str[:2]), minutes=int(cur_time_str[-2:]))

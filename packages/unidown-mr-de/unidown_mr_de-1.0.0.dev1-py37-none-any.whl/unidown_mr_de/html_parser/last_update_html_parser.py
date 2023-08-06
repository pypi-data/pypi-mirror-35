import re
from datetime import datetime
from html.parser import HTMLParser


class LastUpdateHTMLParser(HTMLParser):
    """
    Extractor for the forum threads from the wiki list.

    :ivar wiki_list_date: update time of the wiki list
    :vartype wiki_list_date: ~datetime.datetime
    """

    def __init__(self):
        HTMLParser.__init__(self)
        self.wiki_list_date = datetime(1970, 1, 1)

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
            if (sub_tag == "id") and (tag == 'span'):
                date = re.search(r"(\d\d).(\d\d).(\d\d\d\d)", value)
                if date is not None:
                    date = date.group()
                    self.wiki_list_date = datetime(int(date[-4:]), int(date[3:5]), int(date[:2]))

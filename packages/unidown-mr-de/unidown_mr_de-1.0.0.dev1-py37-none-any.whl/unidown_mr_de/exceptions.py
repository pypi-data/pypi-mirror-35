"""
mr_de specific module exceptions.
"""

from unidown.plugin.exceptions import PluginException


class GetEbookLinksException(PluginException):
    """
    Something wents wrong while parsing an wiki thread.
    """

    def __init__(self, path, orig_ex):
        super().__init__()
        self.path = path
        self.orig_ex = orig_ex


class NothingFoundInThread(PluginException):
    """
    If no ebook in a wiki thread was found.
    """

    def __init__(self, path):
        super().__init__()
        self.path = path

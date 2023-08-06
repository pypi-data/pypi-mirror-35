"""
Updates older savestate version to the newest one.
TODO
"""

import json
import re
from pathlib import Path


def update_savestat(path: Path, version: int):  # TODO: finish
    with path.open(mode='r', encoding="utf8") as data_file:
        ebook_link_dict_old = json.loads(data_file.read())

    if 'wikilist_date' not in ebook_link_dict_old:
        ebook_link_dict_old['wikilist_date'] = 0

    for item in ebook_link_dict_old:
        if not item.isdigit() and (item is not None):
            attach_id = re.search(r"attachmentid=(\d)*", item)
            if attach_id is not None:
                attach_id = attach_id.group()[13:]
                ebook_link_dict_old[attach_id] = ebook_link_dict_old.pop(item)

                # wikilist_date -> update_date
                # attachmentid=(<id>) -> id
                # add version

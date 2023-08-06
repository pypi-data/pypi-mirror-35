# -*- coding: utf-8; -*-
# This file is part of Superdesk.
# For the full copyright and license information, please see the
# AUTHORS and LICENSE files distributed with this source code, or
# at https://www.sourcefabric.org/superdesk/license
#
# Author  : Jérôme
# Creation: 2018-05-21 16:51

from superdesk.commands.data_updates import DataUpdate


class DataUpdate(DataUpdate):

    resource = 'vocabularies'

    def forwards(self, collection, mongodb_database):
        # some qcode were stored as integer, we fix it by converting them to string
        for item in collection.find({"items.qcode": {"$exists": "", "$not": {"$type": 2}}}):
            items = item["items"]
            for i in items:
                try:
                    i["qcode"] = str(i["qcode"])
                except KeyError:
                    pass
            collection.update({'_id': item['_id']}, {
                '$set': {
                    'items': items
                }})

    def backwards(self, mongodb_collection, mongodb_database):
        pass

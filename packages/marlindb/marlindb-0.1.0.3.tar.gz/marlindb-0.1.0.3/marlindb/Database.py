# Copyright (C) DataInz Technologies Pte. Ltd. - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited.
# Proprietary and confidential.

import json
import urllib.request
import urllib.error
from .Table import Table

# Class representing a database object in MarlinDB
class Database:

    # Constructor
    def __init__(self, dbname, id, session):

        # Name of the database.
        self.dbname = dbname

        # Unique id of the database.
        self.id = id

        # The session to which the database object belongs.
        self.session = session


    # Function to query the database. This function is only for testing and will
    # be removed later.
    def getRecords(self, query, encoding = 'json'):
        query_data = {}
        query_data['session_id'] = self.id
        query_data['query'] = query
        query_json = json.dumps(query_data)
        post_data = query_json.encode(encoding='utf-8')
        headers = {}
        headers['Content-Type'] = 'application/json'

        try:
            request = urllib.request.Request(url="http://" + self.session.hostname + ":" + self.session.port + "/test/query",
                                             data=post_data,
                                             headers=headers)
            urllib.request.urlopen(request, timeout=self.session.timeout).read()
        except urllib.error.HTTPError as err:
            return False
        except urllib.error.URLError as err:
            return False
        return True

    # Function to join 2 tables in the database.
    def join(self, tables, columns):

        # Join currently only supports join of a maximum of 2 tables.
        if len(tables) > 2 or len(columns) > 2:
            return None

        #returning the joined table.
        new_table = Table(tableName=tables[0].tableName, id=0, session=self.session, is_view=True)
        self.session.temp_views.append(new_table)
        return new_table

    # Function to get a table from the database.
    def getTable(self, tableName):
        return Table(tableName=tableName, id=0, session=self.session, is_view=False)
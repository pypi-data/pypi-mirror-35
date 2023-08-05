# Copyright (C) DataInz Technologies Pte. Ltd. - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited.
# Proprietary and confidential.

# Class representing a table object in MarlinDB
class Table:

    # Constructor
    def __init__(self, tableName, id, session, is_view=False):

        # Name of the table.
        self.tableName = tableName

        # The unique identifier of the Table.
        self.id = id

        # Boolean denoting whether its a table or a view.
        self.is_view = is_view

        # The session to which the table or view belongs.
        self.session = session

    # Function to get records from the table
    def getRecords(self, columns, offset, limit, encoding='json'):
        return True

    # Function to execute aggregate operation on the table.
    # The function returns a new table with the aggregate results.
    def aggregate(self, columns, options, encoding='json'):
        new_table = Table(tableName='', id=-1, session=self.session, is_view=True)
        self.session.temp_views.append(new_table)
        return new_table

    # Function to execute filter operation on the table.
    # The function returns a new table with filtered results
    def filter(self, columns, conditions, encoding='json'):
        new_table = Table(tableName='', id=-1, session=self.session, is_view=True)
        self.session.temp_views.append(new_table)
        return new_table

    # Function to generate a sub view from the given table using the specified offset and limit.
    # The function returns a new table with the filtered results
    def subView(self, columns, offset, limit, encoding='json'):
        new_table = Table(tableName='', id=-1, session=self.session, is_view=True)
        self.session.temp_views.append(new_table)
        return new_table

    # Function to delete a table and its associated components from MarlinDB
    def delete(self):
        return True
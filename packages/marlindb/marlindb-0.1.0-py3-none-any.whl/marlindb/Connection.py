# Copyright (C) DataInz Technologies Pte. Ltd. - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited.
# Proprietary and confidential.

import urllib.request
import urllib.error
import json
from .Database import Database

# The class that is responsible for managing a session for sending and receiving
# requests from MarlinDB server.
class MarlindbSession:

    # Constructor
    def __init__(self, hostname, port, username, password, timeout = 30):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.id = -1
        self.timeout = timeout

    # Function to select a database
    def getDatabase(self, dbname):
        return Database(dbname)

    # Function to query the database
    def query(self, database, query):
        query_data = {}
        query_data['session_id'] = self.id
        query_data['query'] = query
        query_json = json.dumps(query_data)
        post_data = query_json.encode('utf-8')
        headers = {}
        headers['Content-Type'] = 'application/json'

        try:
            request = urllib.request.Request("http://" + self.hostname + ":" + self.port + "/query", post_data, headers)
            urllib.request.urlopen(request, timeout=self.timeout).read()
        except urllib.error.HTTPError as err:
            return False
        except urllib.error.URLError as err:
            return False
        return True

# Function to connect to MarlinDB server.
def connect(hostname, port, connection, username, password, timeout = 30):
    session = MarlindbSession(hostname, port, username, password, timeout=timeout)
    try:
        urllib.request.urlopen("http://" + hostname + ":" + port + "/test/alive").read()
    except urllib.error.HTTPError as err:
        return session

    session.id = 0
    return session
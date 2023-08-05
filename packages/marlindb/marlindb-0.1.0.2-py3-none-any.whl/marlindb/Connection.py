# Copyright (C) DataInz Technologies Pte. Ltd. - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited.
# Proprietary and confidential.

import urllib.request
import urllib.error
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
        self.temp_views = []

    # Function to select a database
    def getDatabase(self, dbname):
        return Database(dbname, 0, self)

    # Function to close the session
    def close(self):
        for table in range(0, len(self.temp_views)):
            table.delete()
        self.id = -1

# Function to connect to MarlinDB server.
def initSession(hostname, port, connection, username, password, timeout=30):
    session = MarlindbSession(hostname=hostname, port=port, username=username, password=password, timeout=timeout)
    try:
        urllib.request.urlopen(url="http://" + hostname + ":" + port + "/test/alive").read()
    except urllib.error.HTTPError as err:
        return session

    session.id = 0
    return session
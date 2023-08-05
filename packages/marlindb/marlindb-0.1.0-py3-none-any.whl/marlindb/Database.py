# Copyright (C) DataInz Technologies Pte. Ltd. - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited.
# Proprietary and confidential.

import json
import urllib.request
import urllib.error

# Class that represents a database.
class Database:

    # Constructor
    def __init__(self, dbname):
        self.dbname = dbname
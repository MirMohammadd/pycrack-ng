import os
import sys
sys.path.append(os.getcwd())
try:
    import bcrypt
except:
    import thirdparty.bcrypt as bcrypt

import lib.core.settings as settings

class Phash:
    def __init__(self):
        pass

    

    def hash(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def check(self, password, hash):
        return bcrypt.checkpw(password.encode('utf-8'), hash)
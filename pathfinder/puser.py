import sqlite3

def get_user(uid):
    pass

def get_user_list(page):
    pass

def get_online_users(page):
    pass

def set_online(user):
    pass

def set_offline(user):
    pass

class PathfinderUser:

    def __init__(self, uid):
        try:
            pass
        except:
            pass
    
    def __store(self):
        pass

    def __retrieve(self):
        pass

    def fetch_data(self, indicator):
        if indicator == 0:
            return self.stats['uid']
        elif indicator == 1:
            return self.stats['uname']
        elif indicator == 2:
            return self.stats['utag']
        elif indicator == 3:
            return self.stats['channels']
        
    def add_channel(self, channel_id):
        self.stats['channels'].append(channel_id)

    def __channel_string(self, channels):
        channel_str = ""
        return channel_str
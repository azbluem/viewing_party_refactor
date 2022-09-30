from viewing_party.movie import WatchFunctions

class Person:
    def __init__(self,name,watched,friends,subscriptions):
        self.name=name
        self.watched=watched
        self.friends=friends
        self.subscriptions=subscriptions
    
    def add_watched_movie(self,movie):
        self.watched.append(movie)
        return self.watched
    
    def get_num_watched(self):
        list_len=len(self.watched)
        return list_len

    def get_watched_dict(self):
        return WatchFunctions.get_dict_titles(self.watched)
    
    def get_favorites_dict(self):
        return WatchFunctions.get_dict_titles(self.favorites)
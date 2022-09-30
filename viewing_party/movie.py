class Movie:
    def __init__(self,title,genre,rating,host):
        self.title=title
        self.genre=genre
        self.rating=rating
        self.host=host

    def update_rating(self,new_rating):
        self.rating=new_rating

class WatchFunctions:
    def get_dict_titles(movie_list):
        return_dict={}
        for movie in movie_list:
            return_dict[movie["title"]]=movie
        return return_dict
    
    def get_title_set(movie_dicts):
        return set(key for key in movie_dicts.keys())

    def get_set_diff_as_list(set1,set2):
        return [set1-set2]

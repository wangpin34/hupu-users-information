class User ():
    def __init__(self, name, level, following, followers, homepage, profile):
        self.__name = name
        self.__level = level
        self.__following = following
        self.__followers = followers
        self.__homepage = homepage
        self.__profile = profile
    def getProfile(self):
        return self.__profile

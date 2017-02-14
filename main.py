from fetchUserData import fetchDoc, parseProfile

__author__ = 'Remind Wang'

homePage = 'https://my.hupu.com/212432398485366/profile'
doc = fetchDoc(homePage)
if doc is not None:
    parseProfile(doc)

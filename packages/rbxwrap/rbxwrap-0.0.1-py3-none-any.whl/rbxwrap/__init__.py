"""
    RBLXWrap.py
    a simple roblox api wrapper that
    is easy to write in

    by <@623612991568478239>
"""
import requests, json, random


# Wraper Source #
'''
Basic Commands a Deauthenticated user can use
'''
class roblox: 
    def getuser_byid(id):
        userinfo = requests.get("https://users.roblox.com/v1/users/{}".format(id)).json()
        return userinfo
    def getuser_byuser(user):
        userinfo = requests.get("https://api.roblox.com/users/get-by-username", json={
            "username": user
        }).json()
        return userinfo

    '''
    Commands only an authenticated user can use
    '''
    class Client:
        def __init__(self, token):
            self.token = token
        
        def getcurrentuser(self):
            curauth = requests.get("https://users.roblox.com/v1/users/authenticated", headers={"cookie": self.token}).json()
            return curauth
        def join_game(self, id):
            print("This function is still in development")
        def getcountrycode(self):
            requests.get("https://users.roblox.com/v1/users/authenticated/country-code", headers={"cookie": self.token}).json()['countryCode']
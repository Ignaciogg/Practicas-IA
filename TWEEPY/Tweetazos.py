# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 16:06:01 2020

@author: gabriel.marin
"""

import tweepy

from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler

class MyListener (StreamListener):
    
    def on_data(self, data):
        try:
            with open ("C:/Users/nacho/IA/elBicho.json", 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error en el dato: %s" % str(e))
            return True
    def on_error(self, status):
        print(status)
        return True
    
#Credenciales del Twitter API
consumer_key = "S8HBEm4evnbfxLBryV44Qz1po"
consumer_secret = "iZUWayc5dn2IY0LtAZYh2lGyZcCcDAqYDoBkJlvlJxWLXRC8hH"
access_token = "1441480563169312771-kYQajbkkxxV612VQGafNsgr3OxPulv"
access_secret = "k87QEfgMmklo1RODhLskKTuORjQubowvDC4A1QVi18unO"

auth=OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

twitter_stream = Stream (auth, MyListener())
twitter_stream.filter(track=['el bicho'])

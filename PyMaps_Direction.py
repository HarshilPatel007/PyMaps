#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os, sys, googlemaps, json, readline, rlcompleter, atexit
from HTMLParser import HTMLParser

api_key = ' <Enter Your Google Maps Direction API Key Here> '

gmap = googlemaps.Client(key=api_key)

print ("\n\t\t\t PyMaps Direction \n\t PyMaps - A Google Maps Implementation In Python \n\n\t\t\t    Developed By : Harshil Patel \n")

start_point = raw_input("\t[*] Please Enter a Start Point    : ")
end_point = raw_input("\t[*] Please Enter a End Point      : ")

# Thanks To 'Eloff' for this strip_tags class and function
# Link : https://stackoverflow.com/questions/753052/strip-html-from-strings-in-python
class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

directions = gmap.directions(start_point, end_point)[0]

leg = directions['legs']
step = leg[0]['steps']
#hi = step[0]['html_instructions']

#If You Want to Print Output On Screen
#print strip_tags((json.dumps(lg1, indent=2)))

#If You Want to Save The Output In File
prt = strip_tags((json.dumps(step, indent=2)))
print("\n\t[*] Supported File Types [ .json, .txt, .pdf ]")
filename = raw_input("\t[*] Enter Filename to Store the Data : ")
with open(filename,'a') as f:
    f.write('\n' + start_point + '\t <==> \t' + end_point + '\n' + "----------------------------------------------" + '\n' + prt)








#################################################################
#								#
#DON'T LOOK AT THIS ;)						#
#THIS IS NOTES THAT I WRITE DURING CODING OF THIS PROGRAM ;)	#
#								#
#print(json.dumps(directions, indent=2))			#
#print strip_tags((json.dumps(lg, indent=2)))			#
#								#
# for step in lg[0]:						#
#     print step						#
#								#
#								#
# overview_polyline						#
# warnings							#
# bounds							#
# waypoint_order						#
# summary							#
# copyrights							#
# legs								#
#								#
# distance							#
# traffic_speed_entry						#
# end_address							#
# via_waypoint							#
# start_address							#
# start_location						#
# steps								#
# duration							#
# end_location							#
#								#
#################################################################
#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os, sys, googlemaps, json, readline, rlcompleter, atexit

api_key = ' <Enter Your Google Maps GeoLocation API Key Here> '
gmap = googlemaps.Client(key=api_key)

def banner():
	print ("\n\t\t\t PyMaps GeoLocation \n\t PyMaps - A Google Maps Implementation In Python \n\n\t\t\t    Developed By : Harshil Patel \n")

def main():
    name = raw_input("\t [*] Please Enter Any City/Stret OR Country Name : ")

    geocode_result = gmap.geocode(name)[0]
    geometry = geocode_result['geometry']
    place_id = geocode_result['place_id']
    addr_compnt = geocode_result['address_components']
    frmtd_addr = geocode_result['formatted_address']
    typs = geocode_result['types']

    #print(json.dumps(geocode_result, indent=2))

    print("\n [*] Place ID : \n")
    print(json.dumps(place_id, indent=2))

    print("\n [*] Types : \n")
    print(json.dumps(typs, indent=2))

    print("\n [*] Geometry Inforamation : \n")
    print(json.dumps(geometry, indent=2))

    print("\n [*] Address Components : \n")
    print(json.dumps(addr_compnt, indent=2))

    print("\n [*] Formatted Address : \n")
    print(json.dumps(frmtd_addr, indent=2))

    # key = geocode_result.keys()
    # print key


if __name__ == '__main__':
    try:
	banner()
        main()
    except:
        sys.exit("\n\t [*] Something Goes Wrong")

#!/usr/bin/env python
"""Script that fetches the latest xkcd.com comic, stores it temporarily on disk and makes it
the default background picture using feh"""

# Import modules
import urllib,json,os

# Set global variables
debug = 1
xkcdJsonUrl="http://www.xkcd.com/info.0.json"

# Use the XKCD Json to get todays comic URL
info = json.load(urllib.urlopen(xkcdJsonUrl))

if(debug):
    print "xkcd.com JSON information: "
    print info

# Get the XKCD comic URL/image
url = info['img'] 
urllib.urlretrieve(url)

# Run feh to put the fetched comic as background wallpaper
arguments=" --bg-center "+info['img']                                            
os.system("feh" + arguments)

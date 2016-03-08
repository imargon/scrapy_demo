=========
Tinfoleak v1.5 
Vicente Aguilera Diaz
@VAguileraDiaz
vaguilera@isecauditors.com
Internet Security Auditors
03/20/2015
=========
Tinfoleak: "Get detailed information about a Twitter user"

TABLE OF CONTENTS

1. DESCRIPTION
2. REQUIREMENTS
3. CONFIGURATION
4. EXECUTION
5. LICENSE


=== 1. DESCRIPTION

tinfoleak is a simple Python script that allow to obtain:

    basic information about a Twitter user (name, picture, location, followers, etc.)
    devices and operating systems used by the Twitter user
    applications and social networks used by the Twitter user
    place and geolocation coordinates to generate a tracking map of locations visited
    show user tweets in Google Earth!
    user route and days in each location
    top visited locations and coordinates (to predict home location, work location, etc.)
    hashtags used by the Twitter user and related info (RTs, FAVs, date, time, etc.)
    user mentions by the the Twitter and related info (RTs, FAVs, date, time, etc.)
    topics used by the Twitter user
    ... and a lot of more features!

You can filter all the information by:

    start date / time
    end date / time
    keywords


=== 2. REQUIREMENTS

You need to have installed Tweepy (Twitter API library for Python) in your system.

Download and installation intructions:
https://github.com/tweepy/tweepy


=== 3. CONFIGURATION

The first time you runs this script, you need to assign the OAuth settings.

    1. Edit "tinfoleak.py"
    Use your favorite editor ;-)

    2. Give value to these variables:
    CONSUMER_KEY
    CONSUMER_SECRET
    ACCESS_TOKEN
    ACCESS_TOKEN_SECRET

    How to obtain these values:
    https://dev.twitter.com/discussions/631

    3. Save "tinfoleak.py"


=== 4. EXECUTION 

Execute "tinfoleak.py -h" to show Tinfoleak help.

Usage Example:

./tinfoleak.py stevewoz -is --hashtags --mentions --find ok --media --meta --geo stevewoz.kml --top 10 -t 400 -o stevewoz.html


=== 5. LICENSE

This work is licensed under a Creative Commons Attribution Share-Alike v4.0 License.
https://creativecommons.org/licenses/by-sa/4.0/












#!/usr/bin/env python
# -*- coding: utf-8 -*-

# License:
# This work is licensed under a Creative Commons Attribution Share-Alike v4.0 License.
# https://creativecommons.org/licenses/by-sa/4.0/

"""
Tinfoleak - Get detailed info about a Twitter user 
	:author: 	Vicente Aguilera Diaz
	:version: 	1.5
"""
#argparse是python用于解析命令行参数和选项的标准模块
import argparse
#
import tweepy
import sys
import ConfigParser
import datetime
import errno
import os
import urllib2
from PIL import Image, ExifTags, ImageCms
import exifread
import struct
import time
import pyexiv2
from collections import OrderedDict
from operator import itemgetter
import urllib2
from OpenSSL import SSL
from jinja2 import Template, Environment, FileSystemLoader


# ----------------------------------------------------------------------
def credits(parameters):
	"""Show program credits"""

	print "+++ " 
	print "+++ " + parameters.program_name + " " + parameters.program_version + " - \"Get detailed information about a Twitter user\""
	print "+++ " + parameters.program_author_name + ". " + parameters.program_author_twitter
	print "+++ " + parameters.program_author_companyname
	print "+++ " + parameters.program_date
	print "+++ " 
	print


class Configuration():
	"""Configuration information"""
	# ----------------------------------------------------------------------
	def __init__(self):
		try:
			# Read tinfoleak configuration file ("tinfoleak.conf")
			config = ConfigParser.RawConfigParser()
			config.read('tinfoleak.conf')
			self.color = config.get('colors', 'INFO')
			self.color_hdr = config.get('colors', 'HEADER')
			self.color_fun = config.get('colors', 'FUNCTION')

			CONSUMER_KEY = config.get('Twitter OAuth', 'CONSUMER_KEY')
			CONSUMER_SECRET = config.get('Twitter OAuth', 'CONSUMER_SECRET')
			ACCESS_TOKEN = config.get('Twitter OAuth', 'ACCESS_TOKEN')
			ACCESS_TOKEN_SECRET = config.get('Twitter OAuth', 'ACCESS_TOKEN_SECRET') 
			
			# User authentication
			auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
			auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
		
			# Tweepy (a Python library for accessing the Twitter API)
			#self.api = tweepy.API(auth, secure=True)
			self.api = tweepy.API(auth)
			
		except Exception, e:
			show_error(e)
			sys.exit(1)



# --------------------------------------------------------------------------
class User:
	"""Information about a Twitter user"""
	screen_name = ""
	name = ""
	id = ""
	created_at = ""
	followers_count = ""
	statuses_count = ""
	location = ""
	geo_enabled = ""
	description = ""
	expanded_description = ""
	url = ""
	expanded_url = ""
	profile_image_url = ""
	profile_banner_url = ""
	tweets_average = ""
	meta = ""
	friend_source = ""
	friend_target = ""
	friend_source_followed_by_target = ""
	friend_target_followed_by_source = ""
	friend_source_following_target = ""
	friend_target_following_source = ""
	friend_source_can_dm_target = ""
	friend_target_can_dm_source = ""

	
	

	# ----------------------------------------------------------------------
	def set_user_information(self, api):
		try:
			self.screen_name = api.screen_name
			self.name = api.name
			self.id = api.id
			self.created_at = api.created_at
			self.followers_count = api.followers_count
			self.friends_count = api.friends_count
			self.statuses_count = api.statuses_count
			self.location = api.location
			self.geo_enabled = api.geo_enabled
			self.time_zone = api.time_zone

			td = datetime.datetime.today() - self.created_at
			self.tweets_average = round(float(self.statuses_count / (td.days * 1.0)),2) 

			self.url = api.url
			 
			if len(api.entities) > 1:
				if api.entities['url']['urls']:
					self.expanded_url = api.entities['url']['urls'][0]['expanded_url']
				else:
					self.expanded_url = ""
			else:
				self.expanded_url = ""
				
			try:
				self.description = api.description 
				if api.entities['description']['urls']:
					tmp_expanded_description = api.description
					url = api.entities['description']['urls'][0]['url']
					expanded_url = api.entities['description']['urls'][0]['expanded_url']
					self.expanded_description = tmp_expanded_description.replace(url, expanded_url)
				else:
					self.expanded_description= ""
			except:
				self.expanded_description= ""		
			
			self.profile_image_url = str(api.profile_image_url).replace("_normal","")
			
			try:
				if api.profile_banner_url:
					self.profile_banner_url = str(api.profile_banner_url).replace("_normal","")
				else:
					self.profile_banner_url = ""
			except:
				self.profile_banner_url = ""
				
		except Exception, e:
			show_error(e)
			sys.exit(1)

	# ----------------------------------------------------------------------
	def show_user_information(self,info_color, header_color, fun_color):
		try:
			string = "USER INFORMATION "
			print "\n\n\t" + chr(27) + fun_color + "\t" + string + chr(27) + "[0m"
						
			print_header(header_color, "General Information")
			print_info(info_color, "Screen Name:\t\t\t" + self.screen_name)
			print_info(info_color, "User Name:\t\t\t" + self.name)
			print_info(info_color, "Twitter Unique ID:\t\t" + str(self.id))
			print_info(info_color, "Account created at:\t\t" + self.created_at.strftime('%m/%d/%Y'))
			print_info(info_color, "Followers:\t\t\t" + '{:,}'.format(self.followers_count))
			print_info(info_color, "Friends:\t\t\t" + '{:,}'.format(self.friends_count))
			print_info(info_color, "Tweets:\t\t\t\t" + '{:,}'.format(self.statuses_count))
			try:
				print_info(info_color, "Location:\t\t\t" + str(self.location))
			except:
				print_info(info_color, "Location:")
			print_info(info_color, "Time zone:\t\t\t" + str(self.time_zone))
			print_info(info_color, "Geo enabled:\t\t\t" + str(self.geo_enabled))
			
			print_info(info_color, "URL:\t\t\t\t" + str(self.url))
			if self.expanded_url:
				print_info(info_color, "Expanded URL:\t\t\t" + str(self.expanded_url))
			
			print_info(info_color, "Description:\t\t\t" + str(self.description.encode('utf-8')).replace("\n"," "))
			if self.expanded_description:
				print_info(info_color, "Expanded Description:\t\t" + str(self.expanded_description.encode('utf-8')).replace("\n"," "))
			
			print_info(info_color, "Profile image URL:\t\t" + str(self.profile_image_url))
				
			print_info(info_color, "Tweets average:\t\t\t" + str(self.tweets_average) + " tweets/day")
			
		except Exception, e:
			show_error(e)
			sys.exit(1)


class Sources:
	"""Get tools used to publish tweets"""
	# source = [source1, source2, ... ]
	# sources_firstdate = {source1: first_date1, source2: first_date2, ... ]
	# sources_lastdate = {source1: last_date1, source2: last_date2, ... ]
	# sources_count = {source1: tweets_number1, source2: tweets_number2, ... ]
	sources = []
	sources_firstdate = {}
	sources_lastdate = {}
	sources_count = {}
	sources_total_count = 0
	sources_percent = {}
	
	# ----------------------------------------------------------------------
	def set_sources_information(self, tweet):
		try:
			add = 1
			for index, item in enumerate(self.sources):
				if tweet.source == item[0]:
					add = 0
					self.sources_count[tweet.source] += 1
					self.sources_total_count += 1
					if tweet.created_at < self.sources_firstdate[tweet.source]:
						self.sources_firstdate[tweet.source] = tweet.created_at
					if tweet.created_at > self.sources_lastdate[tweet.source]:
						self.sources_lastdate[tweet.source] = tweet.created_at
			
			if add:
				self.sources.append([tweet.source])
				self.sources_count[tweet.source] = 1
				self.sources_firstdate[tweet.source] = tweet.created_at
				self.sources_lastdate[tweet.source] = tweet.created_at
				self.sources_total_count += 1
						
		except Exception, e:
			show_error(e)
			sys.exit(1)


	# ----------------------------------------------------------------------
	def show_sources_information(self, info_color, header_color, fun_color):
		try:
			string = "CLIENT APPLICATIONS "
			print "\n\n\t" + chr(27) + fun_color + "\t" + string + chr(27) + "[0m"

			print_header(header_color, "Sources\t\t\t\t\t\tUses\t%\tFirst Use\tLast Use")

			for s in self.sources:
				value = get_string_with_padding(s[0], 40)
				self.sources_percent[s[0]] = round((self.sources_count[s[0]] * 100.0) / self.sources_total_count, 1) 
				print_info(info_color, value + "\t" + str(self.sources_count[s[0]]) + "\t" + str(self.sources_percent[s[0]]) + "%\t" + str(self.sources_firstdate[s[0]].strftime('%m/%d/%Y')) + "\t" + str(self.sources_lastdate[s[0]].strftime('%m/%d/%Y')))
			
			print_info(info_color, "\n\t" + str(len(self.sources)) + " results.")		
			
		except Exception, e:
			show_error(e)
			sys.exit(1)



class Geolocation:
	"""Get geolocation info included in tweets"""
	toplocations = {}
	toplocationsstartdate = {}
	toplocatonsenddate = {}
	geoimg = 0 # tweets with images and geolocation (parameter: -p 0)
	toplocations = {} # store the user most visited locations 
	toplocationsdatetime = {} # store date and time of the user most visited locations
	toplocationsstartdate = {} # store initial date of the user most visited locations
	toplocationsenddate = {} # store final date of the user most visited locations
	toplocationsstarttime = {} # store initial time of the user most visited locations
	toplocationsdays = {} # store week day of the user most visited locations
	toplocationsendtime = {} # store final time of the user most visited locations
	toplocationsdaysmo = {} # store week day of the user most visited locations
	toplocationsdaystu = {} # store week day of the user most visited locations
	toplocationsdayswe = {} # store week day of the user most visited locations
	toplocationsdaysth = {} # store week day of the user most visited locations
	toplocationsdaysfr = {} # store week day of the user most visited locations
	toplocationsdayssa = {} # store week day of the user most visited locations
	toplocationsdayssu = {} # store week day of the user most visited locations
	geo_info = []
	toplocations_tweets = {}
	toplocations_tweets_route = {}
		
	visited_locations = []
	visited_locations_startdate = []
	visited_locations_enddate = []
	visited_locations_starttime = []
	visited_locations_endtime = []
	visited_locations_days = []
	
	kml_info = []
	media_info = {}
	toploc = []
	

	# ----------------------------------------------------------------------
	def set_geolocation_information(self, tweet):
		try:
			
			add = 0
			splace = ""
			sgeo = ""
						
			if tweet.place:
				splace = tweet.place.name.encode('utf-8')
				add = 1
			if tweet.geo:
				sgeo = tweet.geo['coordinates']
				add = 1
				lat = str(sgeo[0])[:str(sgeo[0]).find(".")+4]
				lon = str(sgeo[1])[:str(sgeo[1]).find(".")+4]	
				location = "[" + lat + ", " + lon + "]"
				for i in range (1, 20-len(location)):
					location += " "
				location = location + "\t" + splace

				if location in self.toplocations.keys():
					self.toplocations[location] += 1
					if tweet.created_at < self.toplocationsstartdate[location]:
						self.toplocationsstartdate[location] = tweet.created_at 
					if tweet.created_at > self.toplocationsenddate[location]:
						self.toplocationsenddate[location] = tweet.created_at
					if tweet.created_at.time() < self.toplocationsstarttime[location]:
						self.toplocationsstarttime[location] = tweet.created_at.time() 
					if tweet.created_at.time() > self.toplocationsendtime[location]:
						self.toplocationsendtime[location] = tweet.created_at.time() 
				else:
					self.toplocations[location] = 1
					self.toplocationsstartdate[location] = tweet.created_at 
					self.toplocationsenddate[location] = tweet.created_at 
					self.toplocationsstarttime[location] = tweet.created_at.time()
					self.toplocationsendtime[location] = tweet.created_at.time()
					self.toplocationsdaysmo[location] = 0
					self.toplocationsdaystu[location] = 0
					self.toplocationsdayswe[location] = 0
					self.toplocationsdaysth[location] = 0
					self.toplocationsdaysfr[location] = 0
					self.toplocationsdayssa[location] = 0
					self.toplocationsdayssu[location] = 0
				if tweet.created_at.weekday() == 0: # Monday
						self.toplocationsdaysmo[location] += 1
				elif tweet.created_at.weekday() == 1:   # Tuesday
						self.toplocationsdaystu[location] += 1
				elif tweet.created_at.weekday() == 2: # Wednesday
						self.toplocationsdayswe[location] += 1
				elif tweet.created_at.weekday() == 3: # Thursday
						self.toplocationsdaysth[location] += 1
				elif tweet.created_at.weekday() == 4: # Friday
						self.toplocationsdaysfr[location] += 1
				elif tweet.created_at.weekday() == 5: # Saturday
						self.toplocationsdayssa[location] += 1
				elif tweet.created_at.weekday() == 6: # Sunday
						self.toplocationsdayssu[location] += 1					
															
			place = splace.decode('utf-8')
			if splace in self.toplocations_tweets:
				self.toplocations_tweets[place] += 1	
			else:
				self.toplocations_tweets[place] = 1
			
			sinfo = ""
			media_url = ""

			if tweet.entities.has_key('media') :
				medias = tweet.entities['media']
				for m in medias :
					media_url = m['media_url']
				
			if add:
				place = splace.decode('utf-8')
				sinfo = media_url + splace.decode('utf-8') + " " + str(sgeo).decode('utf-8')
				self.geo_info.append([media_url, place, str(sgeo).decode('utf-8'), str(tweet.created_at.strftime('%m/%d/%Y')), str(tweet.created_at.time()), str(tweet.id)])
				
				if len(self.visited_locations)>0 and place in self.visited_locations[len(self.visited_locations)-1][0]: 
					self.visited_locations[len(self.visited_locations)-1][1] = tweet.created_at 
					self.visited_locations[len(self.visited_locations)-1][2] = tweet.created_at.time() 
					delta = self.visited_locations[len(self.visited_locations)-1][3] - tweet.created_at 
					self.visited_locations[len(self.visited_locations)-1][5] = delta.days+1 
					self.visited_locations[len(self.visited_locations)-1][6] = self.toplocations_tweets[place]
					
				else:
					# [place, date (since), time (since), date (until), time (until), days, tweets] 
					self.visited_locations.append([place, tweet.created_at,  tweet.created_at.time(), tweet.created_at, tweet.created_at.time(), 1, 1])
					
			else:
				sinfo = ""		
			
				
		except Exception, e:
			show_error(e)
			sys.exit(1)

	# ----------------------------------------------------------------------
	def show_geolocation_information(self, info_color, header_color, fun_color):
		try:
			string = "GEOLOCATION "
			print "\n\n\t" + chr(27) + fun_color + "\t" + string + chr(27) + "[0m"
			
			# Show tweet coordinates
			print_header(header_color, "Date\t\tTime\t\tCoordinates\t\t\tMedia\tLocation")
			for g in self.geo_info:
				coord = get_string_with_padding(g[2], 30)
				media = ""
				if len(g[0]):
					if str(g[0]).find(".mp4") >= 0:
						media = "Video"
					else:
						media = "Photo"
					self.media_info[g[0]] = media
				
				print_info(info_color, g[3] + "\t" + g[4] + "\t" + coord + "\t" + media + "\t" + g[1])
				
			print_info(info_color, "\n\t" + str(len(self.geo_info)) + " results.")		

			# Show user route
			print_header(header_color, "User route\n\tTweets\t\tDate-Time (since)\tDate-Time (until)\tDays\tLocation")
			
			for l in self.visited_locations: 
				splace = l[0]
				value = get_string_with_padding(str(l[6]) + " [" + str(self.toplocations_tweets[splace]) + "]", 12)
					
				print_info(info_color,  value + "\t" + str(l[1].strftime('%m/%d/%Y')) + " " + str(l[2].strftime('%H:%M:%S')) + "\t" + str(l[3].strftime('%m/%d/%Y')) + " " + str(l[4].strftime('%H:%M:%S')) + "\t" + str(l[5]) + "\t" + splace)
				self.toplocations_tweets_route[splace] = 0
			print_info(info_color, "\n\t" + str(len(self.visited_locations)) + " results.")		
						
		except Exception, e:
			show_error(e)
			sys.exit(1)


	# ----------------------------------------------------------------------
	def show_top_locations(self, info_color, header_color, top, fun_color):
		try:
			string = "TOP LOCATIONS "
			print "\n\n\t" + chr(27) + fun_color + "\t" + string + chr(27) + "[0m"
			
			sort_loc = OrderedDict(sorted(self.toplocations.items(), key=itemgetter(1), reverse=True))
			loc = sort_loc.items()
			
			print_header(header_color, "Locations with more tweets\n\tTweets\tDate\t\t\tTime\t\t\tWeek Days\t\tCoordinates\t\tPlace")
			
			n = 1
			for place, value in loc:
				startdate = self.toplocationsstartdate[place]
				enddate = self.toplocationsenddate[place]
				starttime = self.toplocationsstarttime[place]
				endtime = self.toplocationsendtime[place]
				
				weekdays = "Mo Tu We Th Fr Sa Su"
				favorite = 1
				
				mo = self.toplocationsdaysmo[place]
				tu = self.toplocationsdaystu[place]
				we = self.toplocationsdayswe[place]
				th = self.toplocationsdaysth[place]
				fr = self.toplocationsdaysfr[place]
				sa = self.toplocationsdayssa[place]
				su = self.toplocationsdayssu[place]
				
				week = [mo, tu, we, th, fr, sa, su]
				week_sort = sorted(week, reverse = True)
				maxday = week_sort [0]
										
				if week_sort[0] > 0 and week_sort[1] == 0:
					favorite = 0
				else:
					while week_sort[0] == maxday:
						del week_sort[0]
					if len(week_sort) > 0:
						if week_sort[0] == 0:
							favorite = 0
				
				cad = chr(27) + "[1;31m" + "DD" + chr(27) + info_color 
				day = []
				fav = 0
				mo_day = "Mo"
				tu_day = "Tu"
				we_day = "We"
				th_day = "Th"
				fr_day = "Fr"
				sa_day = "Sa"
				su_day = "Su" 
				
				if mo == 0:
						weekdays = weekdays.replace("Mo", "__")
						mo_day = ""
				else:
						if mo == maxday and favorite:
							weekdays = weekdays.replace("Mo", cad.replace("DD","Mo"))
							fav = "1"
							day.append("Mo")
				if tu == 0:
						weekdays = weekdays.replace("Tu", "__")
						tu_day = ""
				else:
						if tu == maxday and favorite:
							weekdays = weekdays.replace("Tu", cad.replace("DD","Tu"))
							fav = "2"							
							day.append("Tu")
				if we == 0:
						weekdays = weekdays.replace("We", "__")
						we_day = ""
				else:
						if we == maxday and favorite:
							weekdays = weekdays.replace("We", cad.replace("DD","We"))
							fav = "3"
							day.append("We")
				if th == 0:
						weekdays = weekdays.replace("Th", "__")
						th_day = ""
				else:
						if th == maxday and favorite:
							weekdays = weekdays.replace("Th", cad.replace("DD","Th"))
							fav = "4"
							day.append("Th")
				if fr == 0:
						weekdays = weekdays.replace("Fr", "__")
						fr_day = ""
				else:
						if fr == maxday and favorite:
							weekdays = weekdays.replace("Fr", cad.replace("DD","Fr"))
							fav = "5"
							day.append("Fr")
				if sa == 0:
						weekdays = weekdays.replace("Sa", "__")
						sa_day = ""
				else:
						if sa == maxday and favorite:
							weekdays = weekdays.replace("Sa", cad.replace("DD","Sa"))
							fav = "6"
							day.append("Sa")
				if su == 0:
						weekdays = weekdays.replace("Su", "__")
						su_day = ""
				else:
						if su == maxday and favorite:
							weekdays = weekdays.replace("Su", cad.replace("DD","Su"))
							fav = "7"
							day.append("Su")
				
				coordinates = place[1:place.find("]")]
				location = place[20:len(place)]
				print_info(info_color, str(value) + "\t" + str(startdate.strftime('%m/%d/%Y')) + "-" + str(enddate.strftime('%m/%d/%Y')) + "\t" + str(starttime) + "-" + str(endtime) + "\t" + weekdays + "\t" + place)
				self.toploc.append([str(value), str(startdate.strftime('%m/%d/%Y')), str(enddate.strftime('%m/%d/%Y')), str(starttime), str(endtime), mo_day, tu_day, we_day, th_day, fr_day, sa_day, su_day, coordinates, location, fav, day])
				
				if  n == int(top):
					break
				n += 1
			
			print_info(info_color, "\n\t" + str(n-1) + " results.")		
						
		except Exception, e:
			show_error(e)
			sys.exit(1)



	# ----------------------------------------------------------------------
	def set_geofile_information(self, tweet, user):
		try:
			tweet_geo = 0
			place = ""
			geo = ""
			
			# Get place from tweet
			if tweet.place:
				place = tweet.place.name.encode('utf-8')
			
			# Get coordinates from tweet
			if tweet.geo:
				geo = tweet.geo['coordinates']
				tweet_geo = 1
			
			media_url = []
			# Get media content from tweet
			if tweet.entities.has_key('media') :
				medias = tweet.entities['media']
				for m in medias :
					media_url.append(m['media_url'])
						
			photo = ""
			if tweet_geo:
				# Tweet with coordinates
				content = "<table width=\"100%\"><tr><td width=\"48\"><img src=\""+user.profile_image_url.encode('utf-8') +"\"></td><td bgcolor=\"#cde4f3\"><b>" + user.name.encode('utf-8') + "</b> @" + user.screen_name.encode('utf-8') + "<br>" + tweet.text.encode('utf-8') + "</td></tr></table>"
				
				for media in media_url:
					photo = " [Media] "
					content += "<table width=\"100%\"><tr><td><img src=\"" + str(media) + "\"></td></tr></table>"
								
				date = tweet.created_at.strftime('%m/%d/%Y')
				time = tweet.created_at.time()
				self.kml_info.append([geo, content, photo, place, date, time])
					
		except Exception, e:
			show_error(e)
			sys.exit(1)


	# ----------------------------------------------------------------------
	def generates_geofile(self, geofile, parameters):
		kml_file_content = ""
		kml_file_header = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<kml xmlns=\"http://earth.google.com/kml/2.2\">\n<Folder>\n"
		kml_file_body = ""
		kml_file_foot = "</Folder>\n</kml>"
		header = ""
		content = ""

		try:
			f = open(geofile, "w")
			
			header = "<table bgcolor=\"#000000\" width=\"100%\"><tr><td><font color=\"white\"><b>" + parameters.program_name + " " + parameters.program_version + "</b></font><td align=\"right\"><font color=\"white\">" + parameters.program_author_twitter + "</font></td></tr></table>"
					
			for info in self.kml_info:
				#INFO: [coordinates, content, photo, place, date, time]
				coord = str(info[0])
				lat = coord[1:coord.find(",")]
				lon = coord[coord.find(",")+2:coord.find("]")]
				
				cdata = ""
				cdata = "\t\t<![CDATA[" + header + str(info[1]) + "]]>\n"
				snippet = ""
				
				# Place + [Photo]
				snippet = info[3] + " " + str(info[2])
				kml_file_body += "\t<Placemark>\n"
				# Date + Time
				kml_file_body += "\t\t<name>" + str(info[4]) + " - " + str(info[5]) + "</name>\n"
				kml_file_body += "\t\t<Snippet>" + snippet + "</Snippet>\n"
				kml_file_body += "\t\t<description>\n" + cdata + "\t\t</description>\n"				
				kml_file_body += "\t\t<Point>\n"
				kml_file_body += "\t\t\t<coordinates>" + lon + "," + lat + "</coordinates>\n"
				kml_file_body += "\t\t</Point>\n"
				kml_file_body += "\t</Placemark>\n"

			kml_file_content = kml_file_header + kml_file_body + kml_file_foot
			f.write(kml_file_content)
			f.close()			

		except Exception, e:
			show_error(e)
			sys.exit(1)



class Hashtags:
	"""Get hashtags included in tweets"""
	# hashtag = [hashtag1, hashtag2, ... ]
	# hashtags_firstdate = {hashtag1: first_date1, hashtag2: first_date2, ... ]
	# hashtags_lastdate = {hashtag1: last_date1, hashtag2: last_date2, ... ]
	# hashtags_count = {hashtag1: tweets_number1, hashtag2: tweets_number2, ... ]
	hashtags = []
	hashtags_firstdate = {}
	hashtags_lastdate = {}
	hashtags_count = {}
	hashtags_tweet = []
	hashtags_rt = {}
	hashtags_fv = {}
	hashtags_results1 = 0
	hashtags_results2 = 0
	hashtags_results3 = 0	
	hashtags_top = {}
	
	# ----------------------------------------------------------------------
	def set_hashtags_information(self, tweet):
		try:
			
			tmp = ""
			for i in tweet.entities['hashtags']:
				if i['text']:
					tmp = tmp + "#" + i['text'] + " "

				if i['text'].upper() in (name.upper() for name in self.hashtags_rt):
					self.hashtags_rt[i['text'].upper()] += tweet.retweet_count						
				else:
					self.hashtags_rt[i['text'].upper()] = tweet.retweet_count
				
				if i['text'].upper() in (name.upper() for name in self.hashtags_fv):
					self.hashtags_fv[i['text'].upper()] += tweet.favorite_count						
				else:
					self.hashtags_fv[i['text'].upper()] = tweet.favorite_count

			if len(tmp):
				self.hashtags_tweet.append([str(tweet.created_at.strftime('%m/%d/%Y')), str(tweet.created_at.time()), str(tweet.retweet_count), str(tweet.favorite_count), tmp, str(tweet.id)])
				self.hashtags_results1 += 1
			
			for h in tweet.entities['hashtags']:
				orig = h['text']
				upper = h['text'].upper()
				
				if upper in (name.upper() for name in self.hashtags):
					self.hashtags_count[upper] += 1
					if tweet.created_at < self.hashtags_firstdate[upper]:
						self.hashtags_firstdate[upper] = tweet.created_at
					if tweet.created_at > self.hashtags_lastdate[upper]:
						self.hashtags_lastdate[upper] = tweet.created_at
						
				else:
					self.hashtags.append(orig)
					self.hashtags_count[upper] = 1
					self.hashtags_firstdate[upper] = tweet.created_at
					self.hashtags_lastdate[upper] = tweet.created_at
					self.hashtags_results2 += 1
								
		except Exception, e:
			show_error(e)
			sys.exit(1)

	# ----------------------------------------------------------------------
	def show_hashtags_information(self, info_color, header_color, fun_color):
		try:
			string = "HASHTAGS "
			print "\n\n\t" + chr(27) + fun_color + "\t" + string + chr(27) + "[0m"
								
			print_info(info_color, "\n\n\tHASHTAGS IN TWEEETS")
						
			# Show hashtags in tweets
			print_header(header_color, "Date\t\tTime\t\tRTs\tFAVs\tHashtags")
			for h in self.hashtags_tweet:
				tmp = h[0] + "\t" + h[1] + "\t" + h[2] + "\t" + h[3] + "\t" + h[4]
				print_info(info_color, tmp)
			
			print_info(info_color, "\n\t" + str(len(self.hashtags_tweet)) + " results.")		
			
			print_info(info_color, "\n\n\tHASHTAG DETAIL")
			# Show summary for every hashtag
			print_header(header_color, "Date (since)\tDate (until)\tRTs\tFAVs\tCount\tHashtag")
			for h in self.hashtags:				
				print_info(info_color, str(self.hashtags_firstdate[h.upper()].strftime('%m/%d/%Y')) + "\t" + str(self.hashtags_lastdate[h.upper()].strftime('%m/%d/%Y')) + "\t" + str(self.hashtags_rt[h.upper()]) + "\t" + str(self.hashtags_fv[h.upper()]) + "\t" + str(self.hashtags_count[h.upper()]) + "\t" + "#" + h)
				self.hashtags_top[h] = self.hashtags_count[h.upper()]

			sort_has = OrderedDict(sorted(self.hashtags_top.items(), key=itemgetter(1), reverse=True))
			self.hashtags_top = sort_has.items()[0:10]
			self.hashtags_results3 = len (self.hashtags_top)
			
			print_info(info_color, "\n\t" + str(len(self.hashtags)) + " results.")

			print_info(info_color, "\n\n\tTOP HASHTAGS")
			# Show top 10 hashtags
			print_header(header_color, "Date (since)\tDate (until)\tRTs\tFAVs\tCount\tHashtag")
			for h in self.hashtags_top:				
				print_info(info_color, str(self.hashtags_firstdate[h[0].upper()].strftime('%m/%d/%Y')) + "\t" + str(self.hashtags_lastdate[h[0].upper()].strftime('%m/%d/%Y')) + "\t" + str(self.hashtags_rt[h[0].upper()]) + "\t" + str(self.hashtags_fv[h[0].upper()]) + "\t" + str(self.hashtags_count[h[0].upper()]) + "\t" + "#" + h[0])

			print_info(info_color, "\n\t" + str(len(self.hashtags_top)) + " results.")

			
		except Exception, e:
			show_error(e)
			sys.exit(1)


class Mentions:
	""" Get mentions included in tweets """
	# mention = [mention1, mention2, ... ]
	# mentions_count = {mention1: tweets_number1, mention2: tweets_number2, ... ]
	# mentions_firstdate = {mention1: first_date1, mention2: first_date2, ... ]
	# mentions_lastdate = {mention1: last_date1, mention2: last_date2, ... ]
	mentions = []
	mentions_firstdate = {}
	mentions_lastdate = {}
	mentions_count = {}
	mentions_tweet = []
	mentions_rt = {}
	mentions_fv = {}
	mentions_results3 = 0
	mentions_top = {}
	
	# ----------------------------------------------------------------------
	def set_mentions_information(self, tweet):
		try:
			tmp = ""
			for i in tweet.entities['user_mentions']:
				if i['screen_name'].encode('utf-8'):
					tmp = tmp + "@" + i['screen_name'].encode('utf-8') + " "

				if i['screen_name'].encode('utf-8').upper() in (name.upper() for name in self.mentions_rt):
					self.mentions_rt[i['screen_name'].encode('utf-8').upper()] += tweet.retweet_count						
				else:
					self.mentions_rt[i['screen_name'].encode('utf-8').upper()] = tweet.retweet_count
				
				if i['screen_name'].encode('utf-8').upper() in (name.upper() for name in self.mentions_fv):
					self.mentions_fv[i['screen_name'].encode('utf-8').upper()] += tweet.favorite_count						
				else:
					self.mentions_fv[i['screen_name'].encode('utf-8').upper()] = tweet.favorite_count
				
			if len(tmp):
				self.mentions_tweet.append([str(tweet.created_at.strftime('%m/%d/%Y')), str(tweet.created_at.time()), str(tweet.retweet_count), str(tweet.favorite_count), tmp, str(tweet.id)])
			
			for m in tweet.entities['user_mentions']:
				orig = m['screen_name']
				upper = m['screen_name'].upper()
				if upper in (name.upper() for name in self.mentions):
					self.mentions_count[upper] += 1
					if tweet.created_at < self.mentions_firstdate[upper]:
						self.mentions_firstdate[upper] = tweet.created_at
					if tweet.created_at > self.mentions_lastdate[upper]:
						self.mentions_lastdate[upper] = tweet.created_at
						
				else:
					self.mentions.append(orig)
					self.mentions_count[upper] = 1
					self.mentions_firstdate[upper] = tweet.created_at
					self.mentions_lastdate[upper] = tweet.created_at
				
		except Exception, e:
			show_error(e)
			sys.exit(1)

	# ----------------------------------------------------------------------
	def show_mentions_information(self, info_color, header_color, fun_color):
		try:
			string = "USER MENTIONS "
			print "\n\n\t" + chr(27) + fun_color + "\t" + string + chr(27) + "[0m"
			
			print_info(info_color, "\n\n\tUSER MENTIONS IN TWEEETS")
			# Show user mentions in tweets
			print_header(header_color, "Date\t\tTime\t\tRTs\tFAVs\tUser Mentions")
			for m in self.mentions_tweet:
				tmp = m[0] + "\t" + m[1] + "\t" + m[2] + "\t" + m[3] + "\t" + m[4]
				print_info(info_color, tmp)
			
			print_info(info_color, "\n\t" + str(len(self.mentions_tweet)) + " results.")		
			
			print_info(info_color, "\n\n\tUSER MENTION DETAIL")			
			# Show summary for every user mention			
			print_header(header_color, "Date (since)\tDate (until)\tRTs\tFAVs\tCount\tUser Mention")
			for m in self.mentions:
				print_info(info_color, str(self.mentions_firstdate[m.upper()].strftime('%m/%d/%Y')) + "\t" + str(self.mentions_lastdate[m.upper()].strftime('%m/%d/%Y')) + "\t" + str(self.mentions_rt[m.upper()]) + "\t" + str(self.mentions_fv[m.upper()]) + "\t" + str(self.mentions_count[m.upper()]) + "\t" + "@" + m)
				self.mentions_top[m] = self.mentions_count[m.upper()]

			sort_men = OrderedDict(sorted(self.mentions_top.items(), key=itemgetter(1), reverse=True))
			self.mentions_top = sort_men.items()[0:10]
			self.mentions_results3 = len (self.mentions_top)
			
			print_info(info_color, "\n\t" + str(len(self.mentions)) + " results.")		

			print_info(info_color, "\n\n\tTOP MENTIONS")
			# Show top 10 mentions
			print_header(header_color, "Date (since)\tDate (until)\tRTs\tFAVs\tCount\tUser Mention")
			for m in self.mentions_top:				
				print_info(info_color, str(self.mentions_firstdate[m[0].upper()].strftime('%m/%d/%Y')) + "\t" + str(self.mentions_lastdate[m[0].upper()].strftime('%m/%d/%Y')) + "\t" + str(self.mentions_rt[m[0].upper()]) + "\t" + str(self.mentions_fv[m[0].upper()]) + "\t" + str(self.mentions_count[m[0].upper()]) + "\t" + "@" + m[0])

			print_info(info_color, "\n\t" + str(len(self.mentions_top)) + " results.")

		
		except Exception, e:
			show_error(e)
			sys.exit(1)



class User_Tweets:
	""" Handle user tweets """
	
	find = "" # Search text in tweets
	tweets_find = [] # [[text, date, time], ...]
	

	# ----------------------------------------------------------------------
	def set_find_information(self, find, tweet):
		try:
			self.find = find

			if find.lower() in tweet.text.lower(): 
				self.tweets_find.append([tweet.text, tweet.created_at.strftime('%m/%d/%Y'), tweet.created_at.time(), tweet.id])
			
		except Exception, e:
			show_error(e)
			sys.exit(1)

	# ----------------------------------------------------------------------
	def show_find_information(self, info_color, header_color, fun_color):
		try:
			string = "FILTER TWEETS BY TEXT [" + self.find+ "]"
			print "\n\n\t" + chr(27) + fun_color + "\t" + string + chr(27) + "[0m"
			
			print_header(header_color, "Date\t\tTime\t\tTweet")
			count = 0
			for tweet in self.tweets_find:
				print_info(info_color, str(tweet[1]) + "\t" + str(tweet[2]) + "\t" + tweet[0].encode('utf-8')) 
				count +=1
		
			print_info(info_color, "\n\t" + str(count) + " results.")		
		
		except Exception, e:
			show_error(e)
			sys.exit(1)




class User_Images:
	""" Handle user images and metadata information """
	metadata = 0
	
	profile_image_url = ""
	profile_banner_url = ""
	screen_name = ""
	
	pic = [] 
	pics_directory = ""
	pics_result = 0
	username = ""
	images = ""
	meta = ""
	meta_description = {}
	meta_copyright = {}
	meta_date = {}
	meta_make = {}
	meta_model = {}
	meta_software = {}
	meta_distance = {}
	meta_size = {}
	meta_platform = {}
	meta_iccdate = {}
	meta_GPSLatitude = {}
	meta_coordinates = {}
	meta_thumb = {}
	meta_profile_image = []
	meta_profile_banner = []
	
	platforms = {
		"APPL" : "Apple Computer Inc.", 
		"MSFT" : "Microsoft Corporation", 
		"SGI " : "Silicon Graphics Inc.", 
		"SUNW" : "Sun Microsystems Inc.", 
		"TGNT" : "Taligent Inc.",
		}
		
	# ----------------------------------------------------------------------
	def set_images_information(self, tweet):
		try:
			media_url = ""
			image = ""
	
			if tweet.entities.has_key('media') :
				medias = tweet.entities['media']
				for m in medias :
					media_url = m['media_url']
					if str(media_url).find("video") >= 0:
						media_url = get_video_url(m['expanded_url'])
					else:
						if self.images == "d" or self.meta:
							if not os.path.isdir(self.username):
								os.mkdir(self.username)
							img = urllib2.urlopen(media_url).read()
							filename = media_url.split('/')[-1]
							self.pics_directory = os.path.dirname(os.path.abspath(__file__)) + "/" + self.username
							image = self.pics_directory + "/" +filename
							if not os.path.exists(self.username+"/"+filename):
								f = open(self.username+"/"+filename, 'wb')
								f.write(img)
								f.close()			

			if media_url:
				self.pic.append([media_url, image, str(tweet.created_at.strftime('%m/%d/%Y')), str(tweet.created_at.time())])
			
		except Exception, e:
			show_error(e)
			sys.exit(1)


	# ----------------------------------------------------------------------
	def show_images_information(self, info_color, header_color, fun_color):
		try:
			string = "MEDIA RESOURCES "
			print "\n\n\t" + chr(27) + fun_color + "\t" + string + chr(27) + "[0m"
			
			print_header(header_color, "User Images and Videos\t\t\t\t\tDate\t\tTime")
			n = 0
			for p in self.pic:
				if len(p[0]):
					n += 1
					value = get_string_with_padding(str(p[0]), 53)
					print_info(info_color, value + "\t" + p[2] + "\t" + p[3]) 			
		
			print_info(info_color, "\n\t" + str(n) + " results.")		
		
		except Exception, e:
			show_error(e)
			sys.exit(1)


	
	# ----------------------------------------------------------------------
	def set_metadata_information(self, tweet):
		try:
		
			for p in self.pic:
				path = p[1]
				self.meta_description[p[0]] = ""
				self.meta_copyright[p[0]] = ""
				self.meta_date[p[0]] = ""
				self.meta_make[p[0]] = ""
				self.meta_model[p[0]] = ""
				self.meta_software[p[0]] = ""
				self.meta_distance[p[0]] = ""
				self.meta_platform[p[0]] = ""
				self.meta_iccdate[p[0]] = ""
				self.meta_coordinates[p[0]] = ""
				self.meta_thumb[p[0]] = ""
				
				fileName, fileExtension = os.path.splitext(path)								
					
				if os.path.exists(path):
					img = Image.open(path)
					if fileExtension in (".jpg", ".jpeg"):			
						if img._getexif():
							metadata = 1
							exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }
							self.meta_description[p[0]] = unicode(exif['ImageDescription'])
							self.meta_copyright[p[0]] = unicode(exif['Copyright'])
							self.meta_date[p[0]] = unicode(exif['ImageDescription'])
							self.meta_make[p[0]] = unicode(exif['Make'])
							self.meta_model[p[0]] = unicode(exif['Model'])
							self.meta_software[p[0]] = unicode(exif['Software'])
							self.meta_distance[p[0]] = unicode(exif['SubjectDistance'][0]/float(exif['SubjectDistance'][1])) + " meters"
											
					self.meta_size[p[0]] = str(img.size[0]) + "x" + str(img.size[1]) + " px"
					if 'icc_profile' in img.info:
						icc_profile = img.info.get("icc_profile")
						if icc_profile:
							platform = icc_profile[40:44]
							metadata = 1
							if platform in ('APPL', 'MSFT', 'SGI ', 'SUNW', 'TGNT'):
								self.meta_platform[p[0]] = self.platforms[platform]
							datetime = struct.unpack('>hhhhhh',icc_profile[24:36])
							tmp_tuple = (0, 0, 0)
							final_tuple = datetime + tmp_tuple
							self.meta_iccdate[p[0]] = unicode(time.strftime('%Y/%m/%d %H:%M:%S', final_tuple))
					
					# Checkf for GPS information
					try:
						latitude = metadata.__getitem__("Exif.GPSInfo.GPSLatitude")
						latitudeRef = metadata.__getitem__("Exif.GPSInfo.GPSLatitudeRef")
						longitude = metadata.__getitem__("Exif.GPSInfo.GPSLongitude")
						longitudeRef = metadata.__getitem__("Exif.GPSInfo.GPSLongitudeRef")

						latitude = str(latitude).split("=")[1][1:-1].split(" ");
						latitude = map(lambda f: str(float(Fraction(f))), latitude)
						latitude = latitude[0] + u"\u00b0" + latitude[1] + "'" + latitude[2] + '"' + " " + str(latitudeRef).split("=")[1][1:-1]

						longitude = str(longitude).split("=")[1][1:-1].split(" ");
						longitude = map(lambda f: str(float(Fraction(f))), longitude)
						longitude = longitude[0] + u"\u00b0" + longitude[1] + "'" + longitude[2] + '"' + " " + str(longitudeRef).split("=")[1][1:-1]

						latitude_value = dms_to_decimal(*metadata.__getitem__("Exif.GPSInfo.GPSLatitude").value + [metadata.__getitem__("Exif.GPSInfo.GPSLatitudeRef").value]);
						longitude_value = dms_to_decimal(*metadata.__getitem__("Exif.GPSInfo.GPSLongitude").value + [metadata.__getitem__("Exif.GPSInfo.GPSLongitudeRef").value]);

						self.meta_coordinates[p[0]] = str(latitude_value) + ", " + str(longitude_value)
					except Exception, e:
						# No GPS information
						pass
				
		except Exception, e:
			show_error(e)
			sys.exit(1)

	# ----------------------------------------------------------------------
	def show_metadata_information(self, info_color, header_color, fun_color):
		try:
			string = "METADATA "
			print "\n\n\t" + chr(27) + fun_color + "\t" + string + chr(27) + "[0m"

			# Extract metadata from profile image
			self.get_metadata(self.profile_image_url.replace("_normal.", "."), 1, "Profile Image", 1, self.screen_name, header_color, info_color)
			print

			print_header(header_color, "User Images")
					
			for p in self.pic:
				if len(p[0]) and ".mp4" not in (p[0]):
					meta = 0
					print_info(info_color, p[0])
						
					description = self.meta_description[p[0]]
					copyright = self.meta_copyright[p[0]]
					date = self.meta_date[p[0]] 
					make = self.meta_make[p[0]] 
					model = self.meta_model[p[0]] 
					software = self.meta_software[p[0]] 
					distance = self.meta_distance[p[0]] 
					size = self.meta_size[p[0]]
					platform = self.meta_platform[p[0]]
					iccdate = self.meta_iccdate[p[0]]
					coordinates = self.meta_coordinates[p[0]]
					thumb = self.meta_thumb[p[0]]
					
					if len(description):
						print_info(info_color, "\tDescription: \t" + description)
						meta = 1
					if len(copyright):
						print_info(info_color, "\tCopyright: \t" + copyright)
						meta = 1
					if len(date):
						print_info(info_color, "\tDate: \t" + date)
						meta = 1
					if len(make):
						print_info(info_color, "\tMake: \t" + make)
						meta = 1
					if len(model):
						print_info(info_color, "\tModel: \t" + model)
						meta = 1
					if len(software):
						print_info(info_color, "\tSoftware: \t" + software)
						meta = 1
					if len(distance):
						print_info(info_color, "\tSubject distance: \t" + distance)
						meta = 1
					if len(size):
						print_info(info_color, "\tSize: \t\t" + size)
						meta = 1
					if len(platform):
						print_info(info_color, "\tPlatform: \t" + platform)
						meta = 1
					if len(iccdate):
						print_info(info_color, "\tICC Date: \t" + iccdate)
						meta = 1
					if thumb:
						print_info(info_color, "\tThumbnail: \t" + thumb)
						meta = 1
					if len(coordinates):
						print_info(info_color, "\tCoordinates: \t" + coordinates)
						meta = 1
								
					if not meta:
						print "\n\t\tNo metadata found."
			
		except Exception, e:
			show_error(e)
			sys.exit(1)
			
	# ----------------------------------------------------------------------			
	def get_metadata(self, filename, save, desc, header, username, header_color, info_color):
		try:
			metadata = 0
			platforms = {
				"APPL" : "Apple Computer Inc.", 
				"MSFT" : "Microsoft Corporation", 
				"SGI " : "Silicon Graphics Inc.", 
				"SUNW" : "Sun Microsystems Inc.", 
				"TGNT" : "Taligent Inc.",
			}

			if desc == "Profile Image":
					self.profile_image_url = filename

			if header:
				print_header(header_color, desc)
				print_info(info_color, "Image URL: \t\t\t" + filename)				
	
			if save:
				save_image(filename, username)
	
			pics_directory = os.path.dirname(os.path.abspath(__file__)) + "/" + username
	
			filename = filename.split('/')[-1]
			path = pics_directory + "/" + filename
			fileName, fileExtension = os.path.splitext(path)					
				
			
			if os.path.exists(path):			
				img = Image.open(path)
				if fileExtension in (".jpg", ".jpeg"):			
					if img._getexif():
						metadata = 1
						exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }
						print_info(info_color, "Description: \t\t\t" + unicode(exif['ImageDescription']))
						print_info(info_color, "Copyright: \t\t\t" + unicode(exif['Copyright']))
						print_info(info_color, "Date: \t\t\t\t" + unicode(exif['DateTimeOriginal']))
						print_info(info_color, "Make: \t\t\t\t" + unicode(exif['Make']))
						print_info(info_color, "Model: \t\t\t\t" + unicode(exif['Model']))
						print_info(info_color, "Software: \t\t\t" + unicode(exif['Software']))
						print_info(info_color, "Subject distance: \t\t" + unicode(exif['SubjectDistance'][0]/float(exif['SubjectDistance'][1])) + " meters")
					
						if desc == "Profile Image":
							self.meta_profile_image.append(unicode(exif['ImageDescription']))
							self.meta_profile_image.append(unicode(exif['Copyright']))
							self.meta_profile_image.append(unicode(exif['DateTimeOriginal']))
							self.meta_profile_image.append(unicode(exif['Make']))
							self.meta_profile_image.append(unicode(exif['Model']))
							self.meta_profile_image.append(unicode(exif['Software']))
							self.meta_profile_image.append(unicode(exif['SubjectDistance'][0]/float(exif['SubjectDistance'][1])) + " meters")
						
					else:	
						self.meta_profile_image.append("")
						self.meta_profile_image.append("")
						self.meta_profile_image.append("")
						self.meta_profile_image.append("")
						self.meta_profile_image.append("")
						self.meta_profile_image.append("")
						self.meta_profile_image.append("")
											
													
				print_info(info_color, "Size: \t\t\t\t" + str(img.size[0]) + "x" + str(img.size[1]) + " px")
				if 'icc_profile' in img.info:
					icc_profile = img.info.get("icc_profile")
					if icc_profile:
						platform = icc_profile[40:44]
						metadata = 1
						if platform in ('APPL', 'MSFT', 'SGI ', 'SUNW', 'TGNT'):
							print_info(info_color, "Platform: \t\t\t" + platforms[platform])
							if desc == "Profile Image":
								self.meta_profile_image.append(platforms[platform])
							else:
								self.meta_profile_image.append("")
								
						datetime = struct.unpack('>hhhhhh',icc_profile[24:36])
						tmp_tuple = (0, 0, 0)
						final_tuple = datetime + tmp_tuple
						print_info(info_color, "ICC Date: \t\t\t" + time.strftime('%Y/%m/%d %H:%M:%S', final_tuple))
						if desc == "Profile Image":
							self.meta_profile_image.append(time.strftime('%Y/%m/%d %H:%M:%S', final_tuple))
						else:
							self.meta_profile_image.append("")
					
				try:
					latitude = metadata.__getitem__("Exif.GPSInfo.GPSLatitude")
					latitudeRef = metadata.__getitem__("Exif.GPSInfo.GPSLatitudeRef")
					longitude = metadata.__getitem__("Exif.GPSInfo.GPSLongitude")
					longitudeRef = metadata.__getitem__("Exif.GPSInfo.GPSLongitudeRef")
	
					latitude = str(latitude).split("=")[1][1:-1].split(" ");
					latitude = map(lambda f: str(float(Fraction(f))), latitude)
					latitude = latitude[0] + u"\u00b0" + latitude[1] + "'" + latitude[2] + '"' + " " + str(latitudeRef).split("=")[1][1:-1]
	
					longitude = str(longitude).split("=")[1][1:-1].split(" ");
					longitude = map(lambda f: str(float(Fraction(f))), longitude)
					longitude = longitude[0] + u"\u00b0" + longitude[1] + "'" + longitude[2] + '"' + " " + str(longitudeRef).split("=")[1][1:-1]
	
					latitude_value = dms_to_decimal(*metadata.__getitem__("Exif.GPSInfo.GPSLatitude").value + [metadata.__getitem__("Exif.GPSInfo.GPSLatitudeRef").value]);
					longitude_value = dms_to_decimal(*metadata.__getitem__("Exif.GPSInfo.GPSLongitude").value + [metadata.__getitem__("Exif.GPSInfo.GPSLongitudeRef").value]);
	
					print_info(info_color, "GPS Information:\t\t" + str(latitude_value) + ", " + str(longitude_value))
				except Exception, e:
					print_info(info_color, "GPS Information:\t\tNot found")
	
			print 
	
		except Exception, e:
			show_error(e)
			sys.exit(1)

			
class Parameters:
	"""Global program parameters"""
	# ----------------------------------------------------------------------
	def __init__(self, **kwargs):
		try:
			config = Configuration()
			self.api = config.api
			self.info_color = config.color
			self.header_color = config.color_hdr
			self.function_color = config.color_fun
			self.screen_name= kwargs.get("username")
			self.tweets = kwargs.get("tweets")
			self.sdate = kwargs.get("sdate")
			self.edate = kwargs.get("edate")
			self.sdate = kwargs.get("stime")
			self.edate = kwargs.get("etime")
			self.elapsedtime = kwargs.get("elapsedtime")
			self.friend = kwargs.get("friend")
			self.geo = kwargs.get("geo")
			self.top = kwargs.get("top")
			self.find = kwargs.get("find")
			self.output = kwargs.get("output")
			
			self.program_name ="Tinfoleak"
			self.program_version = "v1.5"
			self.program_date = "03/20/2015"
			self.program_author_name = "Vicente Aguilera Diaz"
			self.program_author_twitter = "@VAguileraDiaz"
			self.program_author_companyname = "Internet Security Auditors"

		except Exception, e:
			show_error(e)
			sys.exit(1)


# ----------------------------------------------------------------------
def print_header(color, string):
	"""Print header in the console"""
	try:
		print
		print
		print chr(27) + color + "\t" + string + chr(27) + "[0m"
		print chr(27) + color + "\t====================================================================================" + chr(27) + "[0m"
	except Exception, e:
		show_error(e)
		sys.exit(1)
	

# ----------------------------------------------------------------------
def print_info(color, string):
	"""Print info in the console"""
	try:
		print chr(27) + color + "\t" + string + chr(27) + "[0m"
	except Exception, e:
		show_error(e)
		sys.exit(1)


# ----------------------------------------------------------------------
def is_valid(tweet, args):
	"""Verify if a tweet meets all requirements"""
	try:
		valid = 1
		
		date = str(tweet.created_at.strftime('%Y/%m/%d'))
		if date < args.sdate or date > args.edate:
			valid = 0
		time = str(tweet.created_at.strftime('%H:%M:%S'))
		if time< args.stime or time> args.etime:
			valid = 0
		
		return valid
		
	except Exception, e:
		show_error(e)
		sys.exit(1)


# ----------------------------------------------------------------------
def get_video_url(url):
	"""Get video URL from a tweet media URL"""
	try:
		video_url = ""
		
		response = urllib2.urlopen(str(url))  
		html = response.read()
		if html.find(".mp4") >= 0:
			begin = html.index('video-src="')
			end = html.index('.mp4"')
			video_url = html[begin+11:end+4]
		
		return video_url
		
	except Exception, e:
		show_error(e)
		sys.exit(1)



# ----------------------------------------------------------------------
def generates_HTML_file(parameters, user, source, hashtag, mention, geolocation, user_images, user_tweets):
	"""Generates a HTML output file"""
	try:
		tinfoleak_dir = os.path.dirname(os.path.abspath(__file__))
		jinja2_env = Environment(loader=FileSystemLoader(tinfoleak_dir), autoescape=True, trim_blocks=True)
		
		desc = user.description
		if user.expanded_description:
			desc = user.expanded_description

		url = user.url
		if user.expanded_url and len(user.expanded_url) < 50:
			url = user.expanded_url		
		
		template_values = {
			'program': parameters.program_name, 
			'version': parameters.program_version,
			'author_name': parameters.program_author_name,
			'author_twitter': parameters.program_author_twitter,
			'author_company': parameters.program_author_companyname,
			'profile_image': user.profile_image_url.replace("_normal.", "."),
			'screen_name': user.screen_name,
			'user_name': user.name, 
			'twitter_id': user.id,
			'date': user.created_at.strftime('%m/%d/%Y'),
			'followers': '{:,}'.format(user.followers_count),
			'friends': '{:,}'.format(user.friends_count),
			'geo': user.geo_enabled,
			'tweets': '{:,}'.format(user.statuses_count),
			'location': user.location,
			'timezone': user.time_zone,
			'description': desc, 
			'url': url,
			'tweets_average': user.tweets_average,
			
			# source
			'source': source.sources,
			'sources_count': source.sources_count,
			'sources_percent': source.sources_percent,
			'sources_firstdate': source.sources_firstdate,
			'sources_lastdate': source.sources_lastdate,
			'sources_results': len(source.sources),
			
			# hashtag
			'hashtags_tweet': hashtag.hashtags_tweet,
			'hashtags_results1': hashtag.hashtags_results1,
			'hashtags_results2': hashtag.hashtags_results2,
			'hashtags_results3': hashtag.hashtags_results3,
			'hashtags_firstdate': hashtag.hashtags_firstdate,
			'hashtags_lastdate': hashtag.hashtags_lastdate,
			'hashtag': hashtag.hashtags,
			'hashtags_rt': hashtag.hashtags_rt,
			'hashtags_fv': hashtag.hashtags_fv,
			'hashtags_count': hashtag.hashtags_count,
			'hashtags_top': hashtag.hashtags_top,

			# mention
			'mentions_tweet': mention.mentions_tweet,
			'mentions_results1': len(mention.mentions_tweet),
			'mentions_results2': len(mention.mentions_count),
			'mentions_results3': mention.mentions_results3,
			'mentions_firstdate': mention.mentions_firstdate,
			'mentions_lastdate': mention.mentions_lastdate,
			'mention': mention.mentions,
			'mentions_rt': mention.mentions_rt,
			'mentions_fv': mention.mentions_fv,
			'mentions_count': mention.mentions_count,
			'mentions_top': mention.mentions_top,
			
			# find text 
			'find': user_tweets.find,
			'tweet_find': user_tweets.tweets_find,
			'find_count': len(user_tweets.tweets_find),

			# media
			'media': user_images.pic,
			'media_directory': user_images.pics_directory,
			'media_count': len(user_images.pic),
			
			#meta
			'meta_size': user_images.meta_size,
			'meta_description': user_images.meta_description,
			'meta_copyright': user_images.meta_copyright,
			'meta_date': user_images.meta_date,
			'meta_make': user_images.meta_make,
			'meta_model': user_images.meta_model,
			'meta_software': user_images.meta_software,
			'meta_distance': user_images.meta_distance,
			'meta_platform': user_images.meta_platform,
			'meta_iccdate': user_images.meta_iccdate,
			'meta_coordinates': user_images.meta_coordinates,
			'meta_thumb': user_images.meta_thumb,
			'meta_profile_image': user_images.meta_profile_image,
			'meta_profile_banner': user_images.meta_profile_banner,
			'meta_profile_image_url': user_images.profile_image_url,
			'meta_profile_banner_url': user_images.profile_banner_url,
			
			# geolocation
			'geo_info': geolocation.geo_info,
			'geo_count': len(geolocation.geo_info),
			'geo_media': geolocation.media_info,			
			'geo_info_count': len(geolocation.geo_info),
			'geo_visited_locations': geolocation.visited_locations,
			'geo_visited_locations_count': len(geolocation.visited_locations),	
			'geo_toplocations_tweets': geolocation.toplocations_tweets,	
			'geo_toplocations': geolocation.toploc,
			'geo_toplocations_count': len(geolocation.toploc)
		}
		
		html_content = jinja2_env.get_template('ReportTemplate/tinfoleak-theme.html').render(template_values)
							
		f = open("ReportTemplate/"+parameters.output, "w")
		f.write(html_content.encode('utf-8'))
		f.close()
		
	except Exception, e:
		show_error(e)
		sys.exit(1)



# ----------------------------------------------------------------------
def save_image(url, username):
	try:
		if not os.path.isdir(username):
			os.mkdir(username)
		
		img = urllib2.urlopen(url).read()
		filename = url.split('/')[-1]
		pics_directory = os.path.dirname(os.path.abspath(__file__)) + "/" + username
		image = pics_directory + "/" +filename
		if not os.path.exists(username+"/"+filename):
			f = open(username+"/"+filename, 'wb')
			f.write(img)
			f.close()
					
	except Exception, e:
		show_error(e)
		sys.exit(1)


# ----------------------------------------------------------------------
def get_information(args, parameters):
	"""Get information about a Twitter user"""
	try:

		api = parameters.api.get_user(args.username)
		source = Sources()
		hashtag = Hashtags()
		mentions = Mentions()
		user_images = User_Images()
		geolocation = Geolocation()
		user = User()
		user.set_user_information(api)
		user.meta = args.meta
							
		if args.information:
			user.show_user_information(parameters.info_color, parameters.header_color, parameters.function_color)
			print "\n" 
		
		user_tweets = User_Tweets()
		
		if args.sources or args.hashtags or args.mentions or args.d or args.file or args.number or args.text:
		
			page = 1
			tweets_count = 0	
			while True:
				timeline = parameters.api.user_timeline(screen_name=args.username, include_rts=True, count=args.tweets, page=page)
			
				if timeline:
					for tweet in timeline:
						tweets_count += 1
						if is_valid(tweet, args):
							if args.sources:
								# Get information about the sources applications used to publish tweets
								source.set_sources_information(tweet)
							if args.hashtags:
								# Get hashtags included in tweets
								hashtag.set_hashtags_information(tweet)
							if args.mentions:
								# Get mentions included in tweets
								mentions.set_mentions_information(tweet)
							if args.d:
								# Get images included in tweets
								user_images.username = args.username
								user_images.images = args.d
								user_images.meta = args.meta
								user_images.set_images_information(tweet)
							if args.meta:
								# Get metadata information from user images
								user_images.set_metadata_information(tweet)
							if args.file or args.number:
								# Get geolocation information from user tweets
								geolocation.set_geolocation_information(tweet)
								geolocation.set_geofile_information(tweet, user)
							if args.text:
								# Search text in tweets
								user_tweets.find = args.text
								user_tweets.set_find_information(args.text, tweet)
											
						sys.stdout.write("\r\t" + str(tweets_count) + " tweets analyzed")
						sys.stdout.flush()										
						if tweets_count >= int(args.tweets):
							print
							break
				else:
					print
					break
				page += 1
				if tweets_count >= int(args.tweets):
					print
					break
			
			print
			
			if args.sources:
				source.show_sources_information(parameters.info_color, parameters.header_color, parameters.function_color)
			
			if args.hashtags:
				hashtag.show_hashtags_information(parameters.info_color, parameters.header_color, parameters.function_color)

			if args.mentions:
				mentions.show_mentions_information(parameters.info_color, parameters.header_color, parameters.function_color)

			if args.d:
				user_images.show_images_information(parameters.info_color, parameters.header_color, parameters.function_color)

			if args.meta and args.d:
				user_images.profile_image_url = user.profile_image_url
				user_images.profile_banner_url = user.profile_banner_url
				user_images.screen_name = user.screen_name
				user_images.show_metadata_information(parameters.info_color, parameters.header_color, parameters.function_color)

			if args.file:
				# Show geolocation information from user tweets
				geolocation.show_geolocation_information(parameters.info_color, parameters.header_color, parameters.function_color)
				geolocation.generates_geofile(args.file, parameters)

			if args.number:
				# Show top N geolocation information 
				geolocation.show_top_locations(parameters.info_color, parameters.header_color, parameters.top, parameters.function_color)
							
			if args.text:
				# Show results for search text in tweets
				user_tweets.show_find_information(parameters.info_color, parameters.header_color, parameters.function_color)
								
		if args.friendname:
			# Get friendship information
			friend = parameters.api.show_friendship(source_screen_name=args.username, target_screen_name=args.friendname)
			user.set_friendship(friend)
			user.show_friendship(parameters.info_color, parameters.header_color, parameters.function_color)
		
		if not args.information and not args.friendname and not args.file and not args.number and not args.d and not args.sources and not args.hashtags and not args.mentions and not args.text and not args.meta:
				print "\tYou need to specify an operation. Execute './tinfoleak.py -h' to see the available operations."
		else:
			if args.output:
				generates_HTML_file(parameters, user, source, hashtag, mentions, geolocation, user_images, user_tweets)
				
	except Exception as e:
		show_error(e)
		sys.exit(1)


# ----------------------------------------------------------------------
def show_error(error):
	""" Show error message """
	try:
		print "\tOops! Something went wrong:"
						
		if str(error).find("Name or service not known") >= 0:
			print "\n\tDo you have Internet connection?"
		else:
			if str(error).find("Could not authenticate you") >= 0:
				print "\n\tYou need to assign value to OAuth tokens. Please, read the README.txt file for more information."
			else:				
				print "\n\t" + str(sys.exc_info()[1][0][0]['message'])		
		print 
		
	except Exception, e:
		print "\n\t" + str(error) + "\n"
		sys.exit(1)


# ----------------------------------------------------------------------
def get_string_with_padding(string, lon):
	""" Return a string with the specified length """

	try:
		padding = " " * lon
		if len(string) < lon:
			string_tmp = string + padding[0:len(padding)-len(string)]
			string = string_tmp[0:len(padding)]
		else:
			string_tmp = string
			string = string_tmp[0:len(padding)]

		return string
		
	except Exception as e:
		show_error(e)
		sys.exit(1)
	

# ----------------------------------------------------------------------
def main():
	""" Main function"""
	try:
		parameters = Parameters() 
		credits(parameters)
		parser = argparse.ArgumentParser(version='Tinfoleak v1.5',description='Tinfoleak')
		parser.add_argument('-t', '--tweets', dest='tweets', default=200, help='number of tweets to be analysed (default: 200)')
		parser.add_argument('username', default='twitter', help='Twitter user name')
		parser.add_argument('-i', '--info', action='store_true', dest='information', help='general information about a user')
		parser.add_argument('-s', '--sources', action='store_true', dest='sources', help='show the client applications used to publish the tweets')
		parser.add_argument('--sdate', dest='sdate', default='1900/01/01', help='filter the results for this start date (format: yyyy/mm/dd)')
		parser.add_argument('--edate', dest='edate', default='2100/01/01', help='filter the results for this end date (format: yyyy/mm/dd)')
		parser.add_argument('--stime', dest='stime', default='00:00:00', help='filter the results for this start time (format: HH:MM:SS)')
		parser.add_argument('--etime', dest='etime', default='23:59:59', help='filter the results for this end date (format: HH:MM:SS)')
		parser.add_argument('--hashtags', action='store_true', dest='hashtags', help='show info about hashtags included in tweets')
		parser.add_argument('--mentions', action='store_true', dest='mentions', help='show info about user mentions')
		parser.add_argument('--meta', action='store_true', dest='meta', help='show metadata information from user images')
		parser.add_argument('--media', dest='d', const='*', help='[no value]: show user images and videos, [d]: download user images to \"username\" directory', type=str, nargs='?')
		parser.add_argument('--friend', dest='friendname', default='', help='Show friendship with the FRIENDNAME user')
		parser.add_argument('--geo', dest='file', default='', help='show geolocation info and generates a output FILE (KML format)')
		parser.add_argument('--top', dest='number', default='', help='show top NUMBER locations visited by the user')
		parser.add_argument('--find', dest='text', default='', help='search TEXT in user tweets')
		parser.add_argument('-o', '--output', dest='output', default='', help='generates a OUTPUT file (HTML format)')
			
		args = parser.parse_args()
		
		if args.sdate:
			parameters.sdate = args.sdate
		else:
			parameters.sdate = "1900/01/01"
		
		if args.edate:
			parameters.edate = args.edate
		else:
			parameters.edate = "2100/01/01"

		if args.stime:
			parameters.stime = args.stime
		else:
			parameters.stime = "00:00:00"
		
		if args.etime:
			parameters.etime= args.etime
		else:
			parameters.etime = "23:59:59"

		if args.friendname:
			parameters.etime= args.friendname
		else:
			parameters.etime = ""

		if args.file:
			parameters.geo = args.file
		else:
			parameters.geo = ""

		if args.number:
			parameters.top = args.number
		else:
			parameters.top = ""

		if args.text:
			parameters.find = args.text
		else:
			parameters.find = ""

		if args.output:
			parameters.output= args.output
		else:
			parameters.output = ""
		
		print "Looking info for @"  + args.username
		print "\n"
		
		# Get the current time
		sdatetime = datetime.datetime.now()
		
		# Obtain the information requested
		get_information(args, parameters)
		
		# Show the elapsed time
		tdelta = datetime.datetime.now() - sdatetime
		hours, remainder = divmod(tdelta.seconds, 3600)
		minutes, seconds = divmod(remainder, 60)
		print "\n\n\tElapsed time: %02d:%02d:%02d" % (hours, minutes, seconds)
		print "\nSee you soon!\n"
		
		parameters.elapsedtime = (hours, minutes, seconds)
		
	except Exception, e:
		show_error(e)
		sys.exit(1)
				
				
if __name__ == '__main__':
	main()

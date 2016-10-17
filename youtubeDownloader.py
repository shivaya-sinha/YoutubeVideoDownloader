import pafy
from urlparse import *

#Query the user for the URL of the video
url = raw_input("Paste the URL of the Youtube video: ")

flag = 0;
#Query for the quality required
"""
	The user has 3 options: 
	1. The best available quality
	2. The worst quality which is available
	3. For other(intermediate) quality
	
	This way user can adjust the quality as per the bandwidth of his internet connection.
""" 
quality = raw_input("Hit 1 for best clarity, 2 for worst, 3 for other: ")
quality = int(quality)
parsed_url = urlparse(url)

if quality<1 or quality>3:
	print("You entered a wrong choice...")
	exit(0)

#To check if the user entered an invalid URL.
if bool(parsed_url.scheme) == False :
	print "Not a valid url"
else :
	if quality == 3:
		falg = 1;
	c=0
	video = pafy.new(url)
	best = video.streams

	# List all available streams so that user can choose from them  
	print "Available streams are : \n"
	
	for b in best :
		print str(c) + " " + str(b)
		c += 1
	
	#Let the user choose from the available streams
	if flag == 1 :
		index = raw_input(" Enter index : ")
		index = int(index)
	
	#if qaulity was worst
	elif quality == 2:
		index = c-1

	#if quality was best
	elif quality == 1:
		index = 0
	
	filename = video.streams[index]
	print "Downloading Stream: "
	print filename
	x = filename.download(quiet=False)
	print "Downloaded " + filename.title + "." + filename.extension

	#Now the file is downloaded in the current folder.

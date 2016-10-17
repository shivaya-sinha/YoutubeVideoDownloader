import pafy
from urlparse import *
url=raw_input("Paste the URL of the Youtube video: ")
flag=0;
parsed_url = urlparse(url)
if bool(parsed_url.scheme)==False :
	print "Not a valid url"
else:
	c=0
	video=pafy.new(url)
	best=video.streams
	for b in best:
		print str(c)+" "+str(b)
		c+=1
	index=0
	filename=video.streams[index]
	print "Downloading Stream: "
	print filename
	x=filename.download(quiet=False)
	print "Downloaded "+filename.title+"."+filename.extension

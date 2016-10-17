import pafy
from urlparse import *
url=raw_input("Paste the URL of the Youtube video: ")
flag=0;
qual=raw_input("Hit 1 for best clarity, 2 for worst, 3 for other: ")
qual=int(qual)
parsed_url = urlparse(url)

if qual<1 or qual>3:
	print("Wrong Choice")

if bool(parsed_url.scheme)==False :
	print "Not a valid url"
else:
	if qual==3:
		falg=1;
	c=0
	video=pafy.new(url)
	best=video.streams
	print "Available Streams: \n"
	for b in best:
		print str(c)+" "+str(b)
		c+=1
	if flag==1:
		index=raw_input("Enter index: ")
		index=int(index)
	elif qual==2:
		index=c-1
	elif qual==1:
		index=0
	filename=video.streams[index]
	print "Downloading Stream: "
	print filename
	x=filename.download(quiet=False)
	print "Downloaded "+filename.title+"."+filename.extension

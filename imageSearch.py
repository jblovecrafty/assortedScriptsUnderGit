import urllib2
import urllib
import json
import PIL.Image
from PIL import ImageTk
from Tkinter import *
import io

googleSearchAPIKey = 'AIzaSyCVw5jBtJkbXS_DbxPOACJmpg_ZbDj1i-s'
googleSearchCX = "012658622856706736429:3kdel0ir5ha"
googleSeachString = 'https://www.googleapis.com/customsearch/v1?key=AIzaSyCVw5jBtJkbXS_DbxPOACJmpg_ZbDj1i-s&cx=012658622856706736429:3kdel0ir5ha&searchType=image&alt=json&'

query = raw_input("What do you want to search for ? >> ")
 
query = urllib.urlencode( {'q' : query } )

googleSeachString = googleSeachString + query
print googleSeachString

#trick google
#
req = urllib2.Request(googleSeachString) 
req.add_header('User-agent', 'Mozilla 5.10')

#open that url
#
response = urllib2.urlopen(req)

#build our json
#
data = json.loads ( response.read() )

results = data [ 'items' ]

imageTest = ""
photoTest = ""
urlTest = ""

#make index random with bounds of 0 and results length
#	
result = results[0]
title = result['title']
url = result['link']
urlTest = url
print ( title + '; ' + url )	

#set up root information here
#
root = Tk()
frame = Frame(root, width=900, height=300)

#get that image
#
fd = urllib.urlopen(urlTest)
image_file = io.BytesIO(fd.read())

imageTest = PIL.Image.open(image_file)

#image resize constants
#
baseWidth = 1200
baseHeight = 750

#ok if the image is larger than the smallest part of the bounds then
#scale the image down
#

#height = [1]
#width = [0]
#
print str(imageTest.size[0]) + " is the old width"
print str(imageTest.size[1]) + " is the old height"

#if((imageTest.size[0] >= imageTest.size[1]) and (imageTest.size[0] > baseWidth)):
if(imageTest.size[0] < imageTest.size[1]):
	width = baseWidth
	wPercent = (baseWidth/float(imageTest.size[0]))
	height = int((float(imageTest.size[1])*float(wPercent)))
	
#elif((imageTest.size[0] < imageTest.size[1]) and (imageTest.size[1] > baseHeight)):
elif(imageTest.size[1] < imageTest.size[0]):
	height = baseHeight
	hPercent = (baseHeight/float(imageTest.size[1]))
	width = int((float(imageTest.size[0])*float(hPercent)))
else:
	height = baseHeight
	width = baseHeight

	
imageTest = imageTest.resize((width, height), PIL.Image.ANTIALIAS)
photoTest = ImageTk.PhotoImage(imageTest)

print str(imageTest.size[0]) + " is the new width"
print str(imageTest.size[1]) + " is the new height"

label = Label(image=photoTest)
label.image = photoTest # keep a reference!
label.pack()

root.mainloop()



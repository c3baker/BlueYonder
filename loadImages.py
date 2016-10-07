import sys
import string
from urllib.request import urlopen
from urllib.request import urlretrieve
from urllib.parse import urlparse
from urllib import error

def main(filename):
	with open(filename, mode= 'rt') as file: #Open file in read-text mode			
		line = file.readline() #Read first line of file
		while line != '': #If not at EOF
			#if validateURL(line): #Proceed on valid URL 
			jpgOrPngFileName = getJPGOrPNGFileName(line)
			if jpgOrPngFileName != "": #Proceed on valid PNG or JPG file
				try :
					urlretrieve(line , jpgOrPngFileName) #Retrieve asset from URL and store		
				except (error.HTTPError, error.URLError) as err:
					print (line)
					print ("HTTP Error {} ".format(str(err)), file=sys.stderr)	
					
			line = file.readline() #Read next line

def getJPGOrPNGFileName(urlString):
	"""Retrieves the file name of the image to be retrieved (.jpg or .png)"""
	parseResult = urlparse(urlString) #Parse URL string
	urlPathSplit = str.split(parseResult.path, sep="/") #Split the path by '/' delimiter 
	jpgOrPngFileName = urlPathSplit[-1].strip(' \t\n\r') #The last item in the list should be the file name	
	if jpgOrPngFileName[-4:] == ".jpg" or jpgOrPngFileName[-4:] == ".png": #Accept .PNG and .JPG
		return jpgOrPngFileName
	return "" #No valid file name found
	
#If this module is being run as a script
#use the command line file name
if __name__ == '__main__': 
	main(sys.argv[1])

import sys
import loadImages
import string
import unittest
import os
from urllib.request import urlopen
from urllib.request import urlretrieve
from urllib.parse import urlparse
from urllib import error

class LoadImagesTests(unittest.TestCase):
	"""Tests for the ''loadImages'' modules """
	def setUp(self):
		"""Test Fixture to create an input file for the image loader"""
		self.testURLLineBad = 'http://www.fakeserver.com/wrongfile.htm'
		self.testURLLineGoodJPG = 'http://www.fakeserver.com/wrongfile.jpg'
		self.testURLLineGoodPNG = 'http://www.fakeserver.com/wrongfile.png'
		self.testFile = 'testInput.txt'
		with open(self.testFile,'w') as file:
			file.write('http://i.ndtvimg.com/i/2015-12/pasta_625x350_41450937320.jpg\n'
						'http://www.gettyimages.ca/gi-resources/images/Homepage/Hero/UK/CMS_Creative_164657191_Kingfisher.jpg')
	def tearDown(self):
		"""Remove test file"""
		try:
			os.remove(self.testFile)
		except:
			pass
			
	def test_function_runs(self):
		loadImages.main(self.testFile)
	
	def test_function_getImageFileNameRejectsNonJGP_PNG(self):
		self.assertEqual(loadImages.getJPGOrPNGFileName(self.testURLLineBad),"")
	
	def test_function_getImageFileNameAcceptsJGP(self):	
		self.assertNotEqual(loadImages.getJPGOrPNGFileName(self.testURLLineGoodJPG),"")

	def test_function_getImageFileNameAcceptsPNG(self):	
		self.assertNotEqual(loadImages.getJPGOrPNGFileName(self.testURLLineGoodPNG),"")
		
if __name__ == '__main__':
	unittest.main()
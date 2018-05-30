'''#download text
import urllib2

response = urllib2.urlopen('https://wordpress.org/plugins/about/readme.txt')
data = response.read()
print(data)

#download html
import urllib2
response = urllib2.urlopen('http://en.wikipedia.org/')
html = response.read()
print(html)



download file
'''

from urllib.request import urlopen

response = urllib2.urlopen('http://mac.majorgeeks.com/index.php?ct=files&action=download&')
data = response.read()

# Write data to file
filename = "test.txt"
file_ = open(filename, 'w')
file_.write(data)
file_.close()
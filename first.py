import urllib2

response = urllib2.urlopen('http://gutenberg.org/')
html = response.read()

sad = 0

list_of_words = html.split(' ')

for word in list_of_words:
	if word == 'sad':
		sad += 1

print sad


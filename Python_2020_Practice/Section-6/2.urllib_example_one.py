import urllib as url

web_data = url.urlopen("https://srsapireddy.github.io/")

print web_data.read()

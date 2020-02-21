from bs4 import BeautifulSoup
import requests
import lxml
import os.path

base_url = "https://news.ycombinator.com/"

response = requests.get(base_url)

#print(response.text)
directory = './output/'
filename = "headlines.html"
file_path = os.path.join(directory, filename)
if not os.path.isdir(directory):
    os.mkdir(directory)

f = open(file_path, "w+")

if response.status_code == requests.codes.ok:
  soup = BeautifulSoup(response.text, 'lxml')
  print(type(soup))
  f.write(response.text)

f.close()

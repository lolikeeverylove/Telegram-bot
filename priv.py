import urllib.request
from bs4 import BeautifulSoup

def get_html(url):
  response =urllib.request.urlopen(url)
  return response.read()
def parse(html):
  soup =BeautifulSoup(html)
  table = soup.find('div', class_ = "item")
  print(table.prettify().encode('utf-8'))
def main ():
  parse(get_html('https://rgsu.net/for-students/timetable/timetable.html?'
                 'template=&action=index&admin_mode=&f_Faculty=18&group=ИСТ-Б-01-Д-2018-1'))
if __name__ == '__main__':
    main()
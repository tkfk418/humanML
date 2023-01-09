import requests
from bs4 import BeautifulSoup 

# 데이터 수집
def crawling(soup):
  result = []
  
  tbody = soup.find('tbody')
  # print(tbody)
  # print('-----')

  for p in tbody.find_all('p', class_='title'):
    # print(p.get_text())
    # result.append(p.get_text().replace('\n',''))
    result.append(p.get_text().strip())

  return result

def main():
  
  custom_header = {
      'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
  }
  url= 'https://music.bugs.co.kr/chart'

  req = requests.get(url, headers = custom_header)

  # soup 객체 
  soup = BeautifulSoup(req.text, "html.parser")
  result = crawling(soup)
  print(result)

if __name__ == "__main__":
  main()
  
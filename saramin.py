import requests
from bs4 import BeautifulSoup

LIMIT = 1
URL = f"http://www.saramin.co.kr/zf_user/search/recruit?search_area=main&search_done=y&search_optional_item=n&searchType=default_mysearch&searchword=python&recruitPage={LIMIT}&recruitSort=relation&recruitPageCount=100&inner_com_type=&company_cd=0,1,2,3,4,5,6,7,9"


def extract_saramin_pages():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pagination = soup.find("div", {"class": "pagination"}).find_all('span')
  pages =[]
  for page in pagination:
      pages.append(int(page.string))
  last_page = pages[-1]
  return last_page



def extract_job(html):
    title = html.find('a')['title']
    company = html.find('strong',{'class':'corp_name'}).find('a')['title']
    locations=html.find('div',{'class':'job_condition'}).find_all('a')
    location=""
    for loc in locations:
        location += loc.string
        location += " "
    link = html.find('a')['href']
    link = "http://www.saramin.co.kr"+link
    return {"title":title,"company":company,"location":location,"link":link}



def extract_saramin_jobs(last_page):
    jobs=[]
    for page in range(1,last_page+1):
        print(f'Scraping page{page}')
        result = requests.get(f"http://www.saramin.co.kr/zf_user/search/recruit?search_area=main&search_done=y&search_optional_item=n&searchType=default_mysearch&searchword=python&recruitPage={page}&recruitSort=relation&recruitPageCount=100&inner_com_type=&company_cd=0,1,2,3,4,5,6,7,9")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div",{"class":"item_recruit"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs



def get_saramin_jobs():
  last_page = extract_saramin_pages()
  saramin_jobs = extract_saramin_jobs(last_page)
  return(saramin_jobs)
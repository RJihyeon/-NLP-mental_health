import pandas as pd
import requests
from bs4 import BeautifulSoup
df = pd.read_csv('blog.csv')   
count = 1 #진행상황 확인용도

for index, row in df.iterrows():

    url = row['link']
    m_url = "https://m." + url.replace("https://","")
    res = requests.get(m_url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    temp = soup.find("div", {'class':'se-main-container'})

    if(temp == None):
        try: 
            content = soup.find("div", {'id':'viewTypeSelector'}).text
        except:
            content = "error"    
    else: 
        content = temp.text

    content = " ".join(content.split()) 
    df.at[index, 'contents'] = content
    
    print(count) #진행상황출력
    count += 1 


# CSV 파일로 저장
df.to_csv('blog_crawled.csv')

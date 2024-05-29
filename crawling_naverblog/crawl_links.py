from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

#options = webdriver.ChromeOptions()
#options.add_argument("headless") Chrome(options=options)

driver = webdriver.Chrome()
df = pd.DataFrame(columns=["title", "link", "contents"])

count = 1 

#검색 결과 Crawling: url 수집

while (count <= 1):
    url = "https://section.blog.naver.com/Search/Post.naver?pageNo=" + str(count) + "&rangeType=ALL&orderBy=sim&keyword=%EA%B5%90%ED%99%98%ED%95%99%EC%83%9D%20%EC%9A%B0%EC%9A%B8"
    driver.get(url)
    time.sleep(3)
    post_links = driver.find_elements(By.CLASS_NAME, "desc")
    for i in range(len(post_links)):
        post_title = post_links[i].find_element(By.CLASS_NAME, "title_post").text
        post_link = post_links[i].find_element(By.TAG_NAME, "a").get_attribute("href")
        temp = pd.DataFrame({"title":[post_title], "link":[post_link], "contents":[""]})
        df = pd.concat([df, temp],  ignore_index=True)
    count += 1

driver.quit()
df.to_csv('blog.csv', encoding='utf-8', index=False)



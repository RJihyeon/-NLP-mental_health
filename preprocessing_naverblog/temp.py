from hanspell import spell_checker
import logging
import pandas as pd
from tqdm import tqdm
import re
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


def text_clean(text):
    pattern = '([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)' # E-mail제거
    text = re.sub(pattern, '', text)
    pattern = '(http|ftp|https)://(?:[-\w.]|(?:%[\da-fA-F]{2}))+' # URL제거
    text = re.sub(pattern, '', text)
    pattern = '([ㄱ-ㅎㅏ-ㅣ]+)'  # 한글 자음, 모음 제거    
    text = re.sub(pattern, '', text)
    pattern = '([a-zA-Z0-9]+)'   # 알파벳, 숫자 제거  
    text = re.sub(pattern, '', text)
    pattern = '<[^>]*>'         # HTML 태그 제거
    text = re.sub(pattern, '', text)
    pattern = '[^\w\s]'         # 특수기호제거
    text = re.sub(pattern, '', text)
    return text  

def blog_clean_data(data) :
    lst = data.split('\u200b')
    elements_to_remove = [',', ' ', '.', ', ','. ','']
    lst = [item for item in lst if item not in elements_to_remove]
    string = ' '
    for line in lst:
        line = text_clean(line)
        try :
            text_cleaned = spell_checker.check(line).checked
            string = string + text_cleaned + ' '
            print('correct')
        except :
            string = string + ' '
            print('error')
        
    return string

file = '../crawling_naverblog/blog_crawled.csv'
df = pd.read_csv(file)
df = df.drop(['Unnamed: 0.1',	'Unnamed: 0'],axis = 1)
df['contents'] = df['contents'].apply(blog_clean_data)


print(df)
df.to_csv('blog_clean_data.csv', index = False)

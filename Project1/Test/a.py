# %%
"""
# BeautyfulSoup 네이버 뉴스 기사 스크래핑
"""

# %%
"""
## 뉴스 기사 스크래핑 함수 정의
"""

import urllib.request
from urllib.parse import quote

import pandas as pd
# %%
from bs4 import BeautifulSoup


def get_news(query, page_num=10):
    news_df = pd.DataFrame(columns=('Title', 'Link', 'Press', 'Datetime', 'Article'))
    idx = 0

    url_query = quote(query)
    url = "https://search.naver.com/search.naver?where=news&sm=nws_hty&query=" + url_query

    for _ in range(0, page_num):

        search_url = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(search_url, 'html.parser')
        links = soup.find_all('dd', {'class': 'txt_inline'})

        for link in links:
            press = link.find('span', {'class': '_sp_each_source'}).get_text()
            news_url = link.find('a').get('href')

            if (news_url == '#'):
                continue
            else:
                news_link = urllib.request.urlopen(news_url).read()
                news_html = BeautifulSoup(news_link, 'html.parser')

                try:
                    title = news_html.find('h3', {'id': 'articleTitle'}).get_text()
                    datetime = news_html.find('span', {'class': 't11'}).get_text()
                    article = news_html.find('div', {'id': 'articleBodyContents'}).get_text()

                    article = article.replace("// flash 오류를 우회하기 위한 함수 추가", "")
                    article = article.replace("function _flash_removeCallback() {}", "")
                    article = article.replace("\n", "")
                    article = article.replace("\t", "")

                    news_df.loc[idx] = [title, news_url, press, datetime, article]
                    idx += 1
                    print('#', end="")
                except:
                    continue

        try:
            next = soup.find('a', {'class': 'next'}).get('href')
            url = "https://search.naver.com/search.naver" + next
        except:
            break

    return news_df


# %%
"""
## 뉴스 기사 스크래핑 실행
"""

# %%
query = input('검색 질의:')
news_df = get_news(query, 10)
print('Done')

# %%
news_df

# %%
news_df['Article']

# %%

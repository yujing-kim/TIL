
## Melon top 100 chart scraping
- 100곡 노래의 title, id 추출
- song의 Detail 페이지로 100번 요청해서 상세정보 추출
- Pandas의 dataFrame에 저장
- DB에 Song Table로 저장



***
* https://www.melon.com/album/detail.htm?albumId=10462799
* songld=32790516
* https://www.melon.com/song/detail.htm?songId=32790516  




* 노래 100곡 -> dict
* 개발자 도구 - network - index.html - request header - **<u>User-Agent</u>** 부분 필요
* User-Agent  :  Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36

***




```python
import requests
from bs4 import BeautifulSoup
import re  # 정규표현식 사용을 위함

url = 'https://www.melon.com/chart/index.htm'
req_header = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
}

html = requests.get(url, headers=req_header).text
soup = BeautifulSoup(html, 'html.parser')
```

* selecter ->    div#tb_list tr div.wrap_song_info a


```python
# selecter 찾아보기
print(len(soup.select('#tb_list')))
print(len(soup.select('#tb_list tr')))
print(len(soup.select('#tb_list tr div.wrap_song_info')))
print(len(soup.select('#tb_list tr div.wrap_song_info a')))
print(len(soup.select("#tb_list tr div.wrap_song_info a[href*='playSong']")))
```

    1
    101
    200
    418
    100
    

---
##### 정규표현식 연습 사이트
* https://regexr.com/
* 참고 사이트 : http://www.nextree.co.kr/p4327/


* 정규표현식 사이트에서 원하는 값을 찾아보았다.
![regexr](6/6_regexr.PNG)
---


```python
# 100 곡의 노래 a tag list를 만듦
song_atags_list = soup.select("#tb_list tr div.wrap_song_info a[href*='playSong']")

# 노래 한곡의 정보를 저장할 dict
song_dict = dict()
# 노래 100개의 dict를 담을 list
song_list = list()

for idx, atag in enumerate(song_atags_list,1):
    song_title = atag.text # 노래 제목만 뽑아냄
    link = atag['href'] # href 속성만 가져오기
    matched = re.search(r'(\d+)\)',link) # 정규표현식을 통해 원하는 문자열을 가져오기
    song_id = matched.group(1)
#     print(song_title, matched.group(0), matched.group(1))
#     print(idx, song_title, link)
#     print(atag)
#     print(idx, song_title, song_id)
    song_url = 'https://www.melon.com/song/detail.htm?songId=' + song_id
#     print(song_url)
    song_dict = {}
    song_dict['song_id'] = song_id
    song_dict['title'] = song_title
    song_dict['url'] = song_url
    song_list.append(song_dict) # list에 삽입
```



### 만들어진 리스트 출력해보기


```python
song_list[:5]
```




    [{'song_id': '32790516',
      'title': '다시 여기 바닷가',
      'url': 'https://www.melon.com/song/detail.htm?songId=32790516'},
     {'song_id': '32725013',
      'title': '마리아 (Maria)',
      'url': 'https://www.melon.com/song/detail.htm?songId=32725013'},
     {'song_id': '32720013',
      'title': 'How You Like That',
      'url': 'https://www.melon.com/song/detail.htm?songId=32720013'},
     {'song_id': '32734372',
      'title': 'Summer Hate (Feat. 비)',
      'url': 'https://www.melon.com/song/detail.htm?songId=32734372'},
     {'song_id': '32768945',
      'title': '여름 안에서 by 싹쓰리 (Feat. 황광희)',
      'url': 'https://www.melon.com/song/detail.htm?songId=32768945'}]




```python
import requests
from bs4 import BeautifulSoup
import re

req_header = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
}

song_lyric_lists = []



for song in song_list:
    # song : dict
    html= requests.get(song['url'], headers=req_header).text
    soup = BeautifulSoup(html, 'html.parser')
#     print(soup)
    
    song_lyric_dict = {} # 노래 정보 저장할 dict
    song_lyric_dict['곡명'] = song['title']
    song_lyric_dict['가수'] = soup.select('a[href*=".goArtistDetail"] span')[0].text
    song_lyric_dict['앨범'] = soup.select('div.meta dd')[0].text
    song_lyric_dict['발매일'] = soup.select('div.meta dd')[1].text
    song_lyric_dict['장르'] = soup.select('div.meta dd')[2].text
    #song_lyric_dict['좋아요'] = soup.select('span#d_like_count')[0].text
    lyric = soup.select('div#d_video_summary')[0].text
    regex = re.compile(r'[\n\r\t]')
    song_lyric_dict['가사'] = regex.sub('', lyric.strip())
    
    song_lyric_lists.append(song_lyric_dict)
    #print(song_lyric_dict)

len(song_lyric_lists)
```




    100




```python
song_lyric_lists[0]
```




    {'곡명': '다시 여기 바닷가',
     '가수': '싹쓰리 (유두래곤, 린다G, 비룡)',
     '앨범': '다시 여기 바닷가',
     '발매일': '2020.07.18',
     '장르': '댄스',
     '가사': '예아 호우 예예예싹쓰리 인더 하우스커커커커커몬 싹 쓰리 투 렛츠고나 다시 또 설레어이렇게 너를 만나서함께 하고 있는 지금 이 공기가다시는 널 볼 순 없을 거라고추억일 뿐이라서랍 속에 꼭 넣어뒀는데흐르는 시간 속에서너와 내 기억은점점 희미해져만 가끝난 줄 알았어지난여름 바닷가너와 나 단둘이파도에 취해서 노래하며같은 꿈을 꾸었지다시 여기 바닷가이제는 말하고 싶어네가 있었기에 내가 더욱 빛나별이 되었다고다들 덥다고 막 짜증내괜찮아 우리 둘은 따뜻해내게 퐁당 빠져버린 널이젠 구하러 가지 않을 거야모래 위 펴펴펴편지를 써밀물이 밀려와도 못 지워추억이 될 뻔한 첫 느낌너랑 다시 한번 받아 보고 싶어흐르는 시간 속에서너와 내 기억은점점 희미해져만 가끝난 줄 알았어지난여름 바닷가너와 나 단둘이파도에 취해서 노래하며같은 꿈을 꾸었지다시 여기 바닷가이제는 말하고 싶어네가 있었기에 내가 더욱 빛나별이 되었다고시간의 강을 건너또 맞닿은 너와 나소중한 사랑을 영원히간직해줘지난여름 바닷가너와 나 단둘이파도에 취해서 노래하며같은 꿈을 꾸었지다시 여기 바닷가이제는 말하고 싶어네가 있었기에 내가 더욱 빛나별이 되었다고'}



### song_lyric_lists를 DataFrame으로 저장


```python
import pandas as pd
# song_lyric_lists를 DataFrame으로 저장
song_df = pd.DataFrame(columns = song_lyric_lists[0].keys())
for s in song_lyric_lists:
    series_obj = pd.Series(s)
    song_df = song_df.append(series_obj, ignore_index=True)
song_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>곡명</th>
      <th>가수</th>
      <th>앨범</th>
      <th>발매일</th>
      <th>장르</th>
      <th>가사</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>다시 여기 바닷가</td>
      <td>싹쓰리 (유두래곤, 린다G, 비룡)</td>
      <td>다시 여기 바닷가</td>
      <td>2020.07.18</td>
      <td>댄스</td>
      <td>예아 호우 예예예싹쓰리 인더 하우스커커커커커몬 싹 쓰리 투 렛츠고나 다시 또 설레어...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>마리아 (Maria)</td>
      <td>화사 (Hwa Sa)</td>
      <td>María</td>
      <td>2020.06.29</td>
      <td>댄스</td>
      <td>욕을 하도 먹어 체했어 하도서러워도 어쩌겠어 I do모두들 미워하느라 애썼네날 무너...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>How You Like That</td>
      <td>BLACKPINK</td>
      <td>How You Like That</td>
      <td>2020.06.26</td>
      <td>랩/힙합</td>
      <td>보란 듯이 무너졌어바닥을 뚫고 저 지하까지옷 끝자락 잡겠다고저 높이 두 손을 뻗어봐...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Summer Hate (Feat. 비)</td>
      <td>지코 (ZICO)</td>
      <td>RANDOM BOX</td>
      <td>2020.07.01</td>
      <td>랩/힙합</td>
      <td>Good morning 하마터면 달 뜰 때까지 쿨쿨쿨 잠잘 뻔택배 아저씨 초인종 소...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>여름 안에서 by 싹쓰리 (Feat. 황광희)</td>
      <td>싹쓰리 (유두래곤, 린다G, 비룡)</td>
      <td>여름 안에서 by 싹쓰리</td>
      <td>2020.07.11</td>
      <td>댄스</td>
      <td>언제나 꿈꿔 온 순간이여기 지금 내게 시작되고 있어그렇게 너를 사랑했던내 마음을 넌...</td>
    </tr>
  </tbody>
</table>
</div>



### mariaDB에 songs 테이블로 저장하기


```python
# DB에 songs 테이블로 저장하기
import pymysql
pymysql.install_as_MySQLdb()

from sqlalchemy import create_engine

# 사용자명 + password + db 이름
engine = create_engine("mysql+mysqldb://python:"+"python"+"@localhost/python_db",\
                       encoding="utf-8")

conn = engine.connect() # 접속시 필요
# if_exists : table이 존재한다면?
song_df.to_sql(name='song', con=engine, if_exists='replace', index=False)
```

* mariaDB에서 생성된 table을 확인할 수 있다.
![song_table](6/6_song_table.PNG)

----
* 2020.07.24 오늘은 여기까지
----


## 1. matplotlib, seaborn를 사용한 시각화

### matplotlib 

>용어 설명
* Figure : 그림을 그리는 도화지
* Axes : plot이 그려지는 공간
* Axis : plot의 축

### csv file 읽기


```python
import pandas as pd

data = pd.read_csv('data/data_draw_korea.csv')
print(type(data)) # <class 'pandas.core.frame.DataFrame'>


```

    <class 'pandas.core.frame.DataFrame'>
    


```python
# 서울광역시
seoul_df =data.loc[data['광역시도'] == '서울특별시']
seoul_df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>인구수</th>
      <th>shortName</th>
      <th>x</th>
      <th>y</th>
      <th>면적</th>
      <th>광역시도</th>
      <th>행정구역</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>124</th>
      <td>124</td>
      <td>526157</td>
      <td>서울강남</td>
      <td>6</td>
      <td>7</td>
      <td>39.5</td>
      <td>서울특별시</td>
      <td>강남구</td>
    </tr>
    <tr>
      <th>125</th>
      <td>125</td>
      <td>432028</td>
      <td>서울강동</td>
      <td>8</td>
      <td>5</td>
      <td>24.6</td>
      <td>서울특별시</td>
      <td>강동구</td>
    </tr>
    <tr>
      <th>126</th>
      <td>126</td>
      <td>310292</td>
      <td>서울강북</td>
      <td>5</td>
      <td>2</td>
      <td>23.6</td>
      <td>서울특별시</td>
      <td>강북구</td>
    </tr>
    <tr>
      <th>127</th>
      <td>127</td>
      <td>554709</td>
      <td>서울강서</td>
      <td>4</td>
      <td>4</td>
      <td>41.4</td>
      <td>서울특별시</td>
      <td>강서구</td>
    </tr>
    <tr>
      <th>128</th>
      <td>128</td>
      <td>484478</td>
      <td>서울관악</td>
      <td>5</td>
      <td>6</td>
      <td>29.6</td>
      <td>서울특별시</td>
      <td>관악구</td>
    </tr>
  </tbody>
</table>
</div>




```python
# jupyter notebook에 플롯이 그려지게 하기 위한 설정
# 명시적으로 이 설정을 하면 notebook에서 show()함수를 사용하지 않아도 풀롯이 출력된다.
%matplotlib inline
```


```python
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
```


```python
# 버전 확인
print('matplotlib version: ' ,matplotlib.__version__)
print('seabor version: ' ,sns.__version__)
print('matplotlib version: ' ,pd.__version__)
```

    matplotlib version:  2.2.3
    seabor version:  0.9.0
    matplotlib version:  1.0.5
    


```python
# matplotlib에 맑은 고딕 한글 폰트 설정하기
font_path = 'C:/Windows/Fonts/malgun.ttf'

# font property 가져오기
font_prop = fm.FontProperties(fname=font_path).get_name()
# matplotlib의 rs(run command) 명령을 사용해서 한글 폰트 설정
matplotlib.rc('font', family=font_prop)
```


```python
#figure와 plot을 생성
figure,(axes1, axes2) = plt.subplots(nrows = 2, ncols=1)

# figure size 조정
figure.set_size_inches(18,12)
print(figure)
print(axes1, axes2)

sns.barplot(data=seoul_df.sort_values(by='인구수', ascending=False),\
            x = '행정구역', y = '인구수', ax=axes1) # 위에다가 그려줄 것
sns.barplot(data=seoul_df.sort_values(by='면적', ascending=False),\
            x="행정구역", y="면적", ax=axes2)
```

    Figure(1296x864)
    AxesSubplot(0.125,0.536818;0.775x0.343182) AxesSubplot(0.125,0.125;0.775x0.343182)
    




    <matplotlib.axes._subplots.AxesSubplot at 0x22e0dffd240>




![png](4/output_7_2.png)



```python
# sido를 넣었을 때, 인구수와 면적에 대한 그래프를 그리는 함수를 만들기

def people_area_graph(sido):
    #figure와 plot을 생성
    figure,(axes1, axes2) = plt.subplots(nrows = 2, ncols=1)
    # figure size 조정
    figure.set_size_inches(18,12)
    print(figure)
    print(axes1, axes2)
    
    # dataframe 만들기
    indata = data.loc[data['광역시도']==sido]
    
    # figure에 출력
    sns.barplot(data=indata, x='행정구역', y='인구수', ax=axes1) # 위에는 인구수
    sns.barplot(data=indata, x='행정구역', y='면적', ax=axes2) # 밑에는 면적

people_area_graph('강원도')
```

    Figure(1296x864)
    AxesSubplot(0.125,0.536818;0.775x0.343182) AxesSubplot(0.125,0.125;0.775x0.343182)
    


![png](4/output_8_1.png)


## 2. mariaDB 연동
* pymysql과 sqlalchemy 사용
* pymysql : python 프로그램과 DB연결해주는 역할
* sqlalchemy : object를 DB의 Table로 mapping해주는 역할



```python
!pip show sqlalchemy
```

    Name: SQLAlchemy
    Version: 1.2.11
    Summary: Database Abstraction Library
    Home-page: http://www.sqlalchemy.org
    Author: Mike Bayer
    Author-email: mike_mp@zzzcomputing.com
    License: MIT License
    Location: c:\anaconda3\lib\site-packages
    Requires: 
    Required-by: 
    

    You are using pip version 10.0.1, however version 20.2b1 is available.
    You should consider upgrading via the 'python -m pip install --upgrade pip' command.
    


```python
!pip show pymysql
```

    Name: PyMySQL
    Version: 0.10.0
    Summary: Pure Python MySQL Driver
    Home-page: https://github.com/PyMySQL/PyMySQL/
    Author: yutaka.matsubara
    Author-email: yutaka.matsubara@gmail.com
    License: "MIT"
    Location: c:\anaconda3\lib\site-packages
    Requires: 
    Required-by: 
    

    You are using pip version 10.0.1, however version 20.2b1 is available.
    You should consider upgrading via the 'python -m pip install --upgrade pip' command.
    


```python
def max_people_row2(sido):
    m = data.loc[data['광역시도'] == sido , '인구수'].max()
    res = data.loc[ data['인구수'] == m ,['광역시도', '행정구역', '인구수'] ]
    return res

max_people_row2('서울특별시')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>광역시도</th>
      <th>행정구역</th>
      <th>인구수</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>141</th>
      <td>서울특별시</td>
      <td>송파구</td>
      <td>615487</td>
    </tr>
  </tbody>
</table>
</div>




```python
max_pop_df = pd.DataFrame(columns=['광역시도', '행정구역', '인구수'])
for sido in data['광역시도'].unique():
    max_pop_df = max_pop_df.append(max_people_row2(sido), sort=False)
    # sort=False : 정렬안되어있으니까 정렬하라 는 뜻
max_pop_df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>광역시도</th>
      <th>행정구역</th>
      <th>인구수</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>8</th>
      <td>강원도</td>
      <td>원주시</td>
      <td>313851</td>
    </tr>
    <tr>
      <th>30</th>
      <td>경기도</td>
      <td>수원시</td>
      <td>1125461</td>
    </tr>
    <tr>
      <th>61</th>
      <td>경상남도</td>
      <td>창원시</td>
      <td>1010040</td>
    </tr>
    <tr>
      <th>89</th>
      <td>경상북도</td>
      <td>포항시</td>
      <td>488395</td>
    </tr>
    <tr>
      <th>93</th>
      <td>광주광역시</td>
      <td>북구</td>
      <td>439683</td>
    </tr>
  </tbody>
</table>
</div>




```python
# max_pop_df를 maxpop table로 저장
import pymysql
pymysql.install_as_MySQLdb()

from sqlalchemy import create_engine

# 사용자명 + password + db 이름
engine = create_engine("mysql+mysqldb://python:"+"python"+"@localhost/python_db",\
                       encoding="utf-8")

conn = engine.connect() # 접속시 필요
# if_exists : table이 존재한다면?
max_pop_df.to_sql(name='maxpop', con=engine, if_exists='fail', index=False)
```




    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-41-aab66c93986b> in <module>()
         10 conn = engine.connect() # 접속시 필요
         11 # if_exists : table이 존재한다면?
    ---> 12 max_pop_df.to_sql(name='maxpop', con=engine, if_exists='fail', index=False)
    

    C:\Anaconda3\lib\site-packages\pandas\core\generic.py in to_sql(self, name, con, schema, if_exists, index, index_label, chunksize, dtype, method)
       2661             chunksize=chunksize,
       2662             dtype=dtype,
    -> 2663             method=method,
       2664         )
       2665 
    

    C:\Anaconda3\lib\site-packages\pandas\io\sql.py in to_sql(frame, name, con, schema, if_exists, index, index_label, chunksize, dtype, method)
        519         chunksize=chunksize,
        520         dtype=dtype,
    --> 521         method=method,
        522     )
        523 
    

    C:\Anaconda3\lib\site-packages\pandas\io\sql.py in to_sql(self, frame, name, if_exists, index, index_label, schema, chunksize, dtype, method)
       1314             dtype=dtype,
       1315         )
    -> 1316         table.create()
       1317         table.insert(chunksize, method=method)
       1318         if not name.isdigit() and not name.islower():
    

    C:\Anaconda3\lib\site-packages\pandas\io\sql.py in create(self)
        644         if self.exists():
        645             if self.if_exists == "fail":
    --> 646                 raise ValueError(f"Table '{self.name}' already exists.")
        647             elif self.if_exists == "replace":
        648                 self.pd_sql.drop_table(self.name, self.schema)
    

    ValueError: Table 'maxpop' already exists.


* maxpop table이 이미 존재한다면 위와같은 오류가 날 수 있다.


#### MariaDB에 table 생성
* 생성된 maxpop table을 확인할 수 있다

![create_maxpop](4/create_table_in_db.PNG)

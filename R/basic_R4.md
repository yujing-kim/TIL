## R의 패키지

* 함수 꾸러미가 패키지 이다.
* 그래프를 그리는 등 함수를 사용하기 위해서는 패키지를 설치하고 불러들여야한다.

* 패키지를 사용하기 위해 설치 후, 로드해야한다.
* 패키지는 한 번만 설치하면 되지만, 로드는 R스튜디오를 시작할 때 마다 반복해야한다.
```
# 패키지 설치
install.packages("ggplot2")

# 패키지 로드
library(ggplot2)
```


* 함수 사용하기
```
# 변수 생성
x <- c("a", "a", "c", "d")

# 빈도막대그래프 생성
qplot(x)
```

* mpg 데이터를 사용한 그래프 표현

* 패키지에 함수 기능을 테스트할 수 있는 예제 데이터인 mpg 데이터가 있다.
* mpg( mile per gallon) 데이터는 1999~2008 년도 사이 미국에서 출시된 자동차 234동의 연비 관련 정보를 담고 있다.
```
# x축 cty
qplot(data = mpg, x = cty)

# x축 drv, y축 hwy
qplot(data = mpg, x = drv, y = hwy)

# line : 선 그래프 형태
qplot(data = mpg, x = drv, y = hwy, geom = "line")

# boxplot : 상자 그림 형태
qplot(data = mpg, x = drv, y = hwy, geom = "boxplot")

# colour = drv  : drv 별 색 표현
qplot(data = mpg, x = drv, y = hwy, geom = "boxplot", colour = drv)
```

* 함수 매뉴얼 출력
```
?qplot

```

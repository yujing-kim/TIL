## R의 함수

* 변수 만들기
```
var1 <- c(1, 2, 3, 4, 5)
var1

## [1] 1 2 3 4 5
```
* mean 함수 적용하기
```
mean(var1)

## [1] 3
```

* max, min 함수 적용하기
```
max(var1)

## [1] 5

min(var1)

## [1] 1
```


* 문자를 다루는 함수

* paste 함수 사용하기
```
str <- c("Hello", "World")

paste( str, collapse = ",")   # 쉼표로 구분하여 단어들 합치기

## [1] "Hello , World"
```

* 함수를 결과물로 새 변수 만들기
```
m <- mean(var1)
m

## [1] 3
```


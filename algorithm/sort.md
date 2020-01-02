# 정렬

* 선택, 버블, 삽입, 퀵, 힙, 병합...
* 퀵 정렬, 힙정렬, 병합정렬 => **O(n log n)** : 이 정렬들을 사용하는 것이 좋다.
    * 퀵 정렬 : 두 부분으로 나누어, 피벗을 기준으로 왼쪽과 오른쪽을 정렬하는 알고리즘 , 분할정복 알고리즘
    * 병합 정렬(merge sort) : 분할정복 알고리즘, 배열이 n개이면 n/2로 만들어 정렬 후 다시 합치는 것
* STL의 sort를 사용하는게 좋다.
   * sort 함수는 <algorithm>헤더를 include하여 사용


### sort() 사용하기

```
int a[10] = {};
sort(a, a+n);
```
* a[0] ~ a[n-1] 까지 정렬하는 소스

```
vector<int> a;
sort(a.begin(), a.end());
```
* vector 를 정렬하는 소스

#### pair 자료형
* 두 자료형을 묶어주는 C++ 컨테이너
```
vector<pair<int, int> > v;
```
* (x,y)좌표를 비교할 때, x가 증가하는 순으로 x가 같으면 y가 증가하는 순으로 인 경우
* 바로 sort 가능
```
sort(v.begin(), v.end());
```

#### 비교함수를 만들어 사용
* 비교 조건이 주어지는 경우, 비교함수를 직접 만들어 사용할 수 있다.
```
struct Point{  //좌표를 구조체 형식으로 생성
    int x,y;
};

bool cmp(Point &a, Point &b){ //bool함수라는 점
    if(a.y < b.y){ //오름차순
        return true;
    }else if(a.y == b.y){ //y좌표가 같으면 x좌표 오름차순
        if(a.x < b.x){
            return true;
        }
        else{ return false;}
    }else return false;
}
```

* 비교함수를 이용한 sort함수 사용
    * 세번째 인자로 넘겨주어 사용해야한다.
```
sort(v.begin(), v.end(), cmp);
```

### stable sorting
* 같은 것이 있는 경우에는 정렬되기 전의 순서를 유지하는 알고리즘
* 이것을 사용하는 알고리즘은 병합정렬이 있다. O(n logn)
* n^2알고리즘 중에서는 버블 sort가 해당
* STL : stable sorting  알고리즘 사용 가능

```
stable_sort(v.begin(), v.end());

stable_sort(v.begin(), v.end(), cmp);
```



# 다이나믹 프로그래밍
* 큰 문제를 작은 문제로 나누어 푸는 알고리즘

## 다이나믹 프로그래밍의 두가지 속성
* 아래 두가지 속성을 만족 할 때 다이나믹 프로그래밍이 가능하다.
### Overlapping subproblem
* 문제를 작은 문제로 쪼개서 풀 수 있다.
* 큰 문제와 작은 문제를 같은 방법으로 풀 수 있다.
### Optimal Substruture
* 문제의 정답을 작은 문제에서 구할 수 있다.
* 이 속성을 만족한다면, 문제의 크기와 관련없이 어떤 한 문제의 정답은 일정하다.
### memoization
* 다이나믹 프로그래밍에서 각 문제는 한번만 풀어야한다.
* Optimal substructure를 만족하기 때문에, 한 번 풀었던 문제의 정답은 같다.
* 즉, 한 번 구한 문제의 정답은 나중에 다시 사용하기 위해 메모해둔다.
* 배열에 저장하는 방법으로 메모해둘 수 있다.
* 이를 메모이제이션이라고 한다.

## 피보나치 수
```
int fibonacci(int n) {
    if (n <= 1) {
        return n;
    } else {
        return fibonacci(n-1) + fibonacci(n-2);
    }
}
```
 * 피보나치 수를 구하는 함수이다.
```
int memo[100];
int fibonacci(int n) {
    if (n <= 1) {
        memo[n] = n;
        return memo[n];
    } else {
        if (memo[n] > 0) {
            return memo[n];
        }
        memo[n] = fibonacci(n-1) + fibonacci(n-2);
        return memo[n];
} }
```
 * 메모이제이션을 적용한 피보나치 수 함수이다.

## 다이나믹을 푸는 두 가지 방법
### top down
* 문제를 작은 문제를 나눈다.
* 작은 문제를 푼 후, 진짜 문제를 푼다.
* 재귀 호출을 통해 쉽게 문제를 풀 수 있다.
  * 재귀 호출을 사용할 때, 메모이제이션은 필수적이다.

### bottom up
* 크기가 작은 문제부터 큰 문제의 순서로 푼다.
* 작은 문제를 풀면서 왔기 때문에 큰 문제는 무조건 풀 수 있다.
```
int d[100];
int fibonacci(int n) {
    d[0] = 1;
    d[1] = 1;
    for (int i=2; i<=n; i++) {
        d[i] = d[i-1] + d[i-2];
    }
    return d[n];
}
```
* bottom up 문제는 반복문을 사용하여 해결할 수 있다.

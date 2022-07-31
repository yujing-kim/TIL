# 나의 풀이 (통과)

def solution(num):
    answer = 0
    str_num = list(map(str, num)) # str로 변환
    str_num = list(map(lambda x : x*3, str_num)) # 문자열을 3배로 늘린 후 정렬하기 (앞 숫자를 기준으로 정렬)
    str_num.sort(reverse=True)
    str_num = list(map(lambda x : x[:len(x)//3], str_num))

    return str(int(''.join(str_num)))

# 다른 풀이
def solution2(num):
    answer = 0
    str_num = list(map(str, num)) # 1. str로 변환

    # 2. sort함수의 key값을 lambda로 준다.(원본 값을 바꾸지 않고 정렬함)
    str_num.sort(key=lambda x : x*3, reverse=True) 

    return str(int(''.join(str_num)))

if __name__ == '__main__':
    numbers = [3, 30, 34, 5, 9]
    solution(numbers)
    solution2(numbers)
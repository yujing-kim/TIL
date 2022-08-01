# 같은 숫자는 싫어 (통과)
# 굉장이 쉽다.ㅎ
def solution(arr):
    answer = [arr[0]]
    a_len = len(arr)
    for i in range(1,a_len):
        if answer[-1] != arr[i] :
            answer.append(arr[i])   
    return answer

if __name__ == '__main__':
    arr = arr = [1, 1, 3, 3, 0, 1, 1]
    solution(arr)
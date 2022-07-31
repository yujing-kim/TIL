# 처음 푼 해결방법 (통과함)
def solution(cita):
    answer = 0
    hidx = [0 for i in range(0,10)]

    for i in cita: 
        for j in range(0, i+1):
            hidx[j] = hidx[j] + 1

    h = []
    for i in hidx:
        if hidx[i] == i:
            h.append(i)

    print(max(h))

# 다른 방법
def solution2(cita):
    answer = 0
    cita = sorted(cita, reverse=True) # 1. 내림차순 정렬
    
    # 2. 현재 idx가 값보다 커지는 경우, idx 만큼 인용된 논문이 idx만큼(이상)존재한다.
    cita_len = len(cita)
    for i in range(cita_len):
        if cita[i] <= i: 
            return i
    return cita_len
    
    # cita = [100, 50, 10]인 경우, 답은 3이다. 
    # 10이 최소값이지만 논문은 3개만 존재, 3번 인용된 논문이 3개 (이상)있으므로.


if __name__ == "__main__" :
    cita = [3,0,6,1,5]
    solution(cita)
    solution2(cita)
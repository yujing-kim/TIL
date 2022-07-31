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



if __name__ == "__main__" :
    cita = [3,0,6,1,5]
    solution(cita)
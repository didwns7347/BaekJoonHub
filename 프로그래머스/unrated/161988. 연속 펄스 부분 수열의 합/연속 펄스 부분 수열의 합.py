
def solution(sequence):
    arr = []
    rearr = []
    for i in range(len(sequence)):
        if i%2 == 0:
            arr.append(sequence[i])
            rearr.append(-sequence[i])
        else:
            arr.append(-sequence[i])
            rearr.append(sequence[i])
    
    answer = arr[0]
    tmp = 0
    # print(arr)
    for i in range(len(sequence)):
        tmp += arr[i]

        if tmp < 0:
            tmp = 0

        answer = max(tmp,answer)
    tmp = 0
    for i in range(len(sequence)):
        tmp += rearr[i]

        if tmp < 0:
            tmp = 0

        answer = max(tmp,answer)

    return answer
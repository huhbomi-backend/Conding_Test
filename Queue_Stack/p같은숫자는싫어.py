from collections import deque

def solution(arr):
    answer = []
    
    q = deque(arr)
    pre = -1
    
    while(q) :
        num = q.popleft()

        if pre != num :
            answer.append(num)
            pre = num


    print(answer)

    return answer

solution([4,4,4,3,3])
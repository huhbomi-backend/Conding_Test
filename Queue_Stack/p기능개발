from collections import deque

import math
#ceil, floor

def solution(progresses, speeds):
    answer = []

    days = deque([])

    for progress, speed in zip(progresses,speeds) :
        days.append(math.ceil((100-progress)/speed))
    
    while days :
        day = days.popleft()
        cnt = 1

        while days :
            nextDay = days.popleft()

            if day>=nextDay :
                cnt += 1
            else :
                days.appendleft(nextDay)
                break
        answer.append(cnt)

    return answer

solution([93, 30, 55],[1, 30, 5])

#7, 3, 9
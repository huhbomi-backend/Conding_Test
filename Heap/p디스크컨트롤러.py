
import heapq
from collections import deque

# 작업의 소요시간이 짧은 것, 작업의 요청 시각이 빠른 것, 작업의 번호가 작은 것 순

def solution(jobs):
    answer = 0

    jobs.sort(key = lambda x : x[0])

    jobs = deque(jobs)

    sec = 0
    
    waiting_jobs = []
    working_jobs = []

    N = len(jobs)

    while True :
        if not working_jobs and not waiting_jobs and not jobs :
            return answer//N

        if working_jobs :
            start_time, finish_time = working_jobs[0]
            if finish_time == sec :
                working_jobs.pop()

        #대기 큐 먼저 삽입
        while jobs :
            req_sec, req_time = jobs[0]

            if req_sec == sec :
                jobs.popleft()

                heapq.heappush(waiting_jobs, (req_time, req_sec))
            else : 
                break

        if not working_jobs and waiting_jobs:
            req_time, req_sec = heapq.heappop(waiting_jobs)
            working_jobs.append([sec,sec+req_time])

            answer += sec+req_time-req_sec

        sec += 1

    return sec



#요청되는 시간, 소요시간
solution([[0, 3], [1, 9], [3, 5]])
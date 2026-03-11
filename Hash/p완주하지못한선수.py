participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

def solution(participant, completion):
    answer = ''
    
    for name in completion : 
        if name in participant :
            participant.remove(name)
    
    answer = participant[0]
    
    return answer

answer = solution(participant, completion)

print(answer)
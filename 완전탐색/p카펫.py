def solution(brown, yellow):
    answer = []
    
    #가로 x, 세로 y 개라고 치면
    #노란색 갯수 x*y
    #브라운 갯수 2(x+y)+4
    
    for i in range(1,int(yellow**0.5)+1) :
        if yellow%i == 0 :
            y = i
            x = yellow//y
            
            if brown == 2*(x+y) + 4 :
                return [x+2,y+2]
    return answer
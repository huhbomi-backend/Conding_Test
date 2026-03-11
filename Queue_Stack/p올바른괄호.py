def solution(s):
    answer = True
    
    SUM = 0

    for c in s : 
        if c == "(" :
            SUM += 1
        else :
            SUM -= 1

        if SUM < 0 :
            return False
        
    if SUM != 0 :
        return False

    return True
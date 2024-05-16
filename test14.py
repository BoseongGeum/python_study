def solution(clothes):
    variety = {}
    
    for cloth in clothes:
        if cloth[1] in variety:
            variety[cloth[1]] += 1
        else:
            variety[cloth[1]] = 1
    
    total = 1
    for n in variety.values():
        total *= (n+1)
    total -= 1
        
    return total

clothes	= [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))

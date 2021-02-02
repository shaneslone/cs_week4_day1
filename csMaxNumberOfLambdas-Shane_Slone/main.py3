def csMaxNumberOfLambdas(text):
    d = {}
    
    for i in range(len(text)):
        char = text[i]
        if char not in d:
            d[char] = 0
        d[char] += 1
    
    lcount = -1
    t = "lambda"
    finished = False
    
    while not finished:
        lcount += 1
        for i in range(len(t)):
            cur = t[i]
            if cur not in d:
                finished = True
                break
            d[cur] -= 1
            if d[cur] < 0:
                finished = True
                break
    return lcount


def csAverageOfTopFive(scores):
    d = {}
    result = []
    for score in scores:
        student = score[0]
        grade = score[1]
        if student not in d:
            d[student] = []
        d[student].append(grade)
    for k in d:
        d[k].sort(reverse=True)
        top_5 = d[k][:5]
        result.append([k, sum(top_5) // len(top_5)])
    return result
        


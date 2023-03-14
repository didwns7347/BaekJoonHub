def solution(today, terms, privacies):
    answer = []
    dateDict = dict()
    termsArr = [0 for _ in range(26)]
    cnt = 0
    for i in range(0,23):
        for j in range(1,13):
            for k in range(1,29):
                year = "{0:02d}".format(i)
                month = "{0:02d}".format(j)
                day = "{0:02d}".format(k)
                dateDict["20"+year+"."+month+"."+day] = cnt
                cnt+=1
    for term in terms:
        a,b = term.split()
        termsArr[ord(a)-ord('A')] = int(b) * 28
    now = dateDict[today]

    for i in range(len(privacies)):
        d,t = privacies[i].split()
        if now - dateDict[d] >= termsArr[ord(t)-ord('A')]:
            answer.append(i+1)

    return answer
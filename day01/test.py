players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

def solution(players, callings):
    answers = players
    for calling in callings:
        i = 0
        temp = ""
        i = answers.find(calling)
        temp = answers[i-1]
        answers[i-1] = calling
        answers[i] = temp
    return answers

result = solution(players, callings)

print(result)

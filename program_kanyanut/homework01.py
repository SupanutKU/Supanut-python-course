def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "E"
list_score = []
for i in range(5):
    l = int(input(f"Enter score [{i+1}]: "))
    list_score.append(l)
for i in range(5):
    s = grade(list_score[i])
    print(f"{i+1}. grade = {s}")
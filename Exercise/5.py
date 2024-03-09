def cg(exam_score,assignment_score,participation_score):
    exam_wight=.40
    assignment_wight=.30
    participation_wight=.30

    wighted_exam_score=exam_score*exam_wight
    wighted_assignment_score=assignment_score*assignment_wight
    wighted_participation_score=participation_score*participation_wight

    total_score=wighted_exam_score+wighted_assignment_score+wighted_participation_score

    if exam_score<40 or assignment_score<40 or participation_score<40:
        grade="F"
    elif participation_score==0:
        grade="F"
    elif total_score>=90:
        grade="S"
    elif 80< total_score>90:
        grade="A"
    elif 70< total_score>80:
        grade="B"
    elif 60< total_score>70:
        grade="C"
    elif 50< total_score>60:
        grade="D"
    else:
        grade="F"
    return grade

exam_score=float(input("Enter the Exam Score: "))
assignment_score=float(input("Entr the Assignment Score: "))
participation_score=float(input("Enter the Participation Score: "))
result=cg(exam_score,assignment_score,participation_score)
print(result)

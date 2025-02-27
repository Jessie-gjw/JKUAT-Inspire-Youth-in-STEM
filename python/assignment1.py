enter_name = input("Enter your name: ")
enter_exam_score = int(input("Enter your exam score: "))

if enter_exam_score < 0 or enter_exam_score > 100:
    print("Invalid score")
elif enter_exam_score >= 90:
    print(enter_name, "A")
elif enter_exam_score >= 80:
    print(enter_name, "B")
elif enter_exam_score >= 70:
    print(enter_name, "C")
elif enter_exam_score >= 60:
    print(enter_name, "D")
elif enter_exam_score >= 50:
    print(enter_name, "E")
elif enter_exam_score < 50:
    print(enter_name, "F")



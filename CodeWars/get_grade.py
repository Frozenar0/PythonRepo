def get_grade(s1, s2, s3):
    grade = (s1 + s2 + s3)/3
    if grade >= 90: return "A"
    elif grade >= 80: return 'B'
    elif grade >= 70: return 'C'
    elif grade >= 60: return 'D'
    else: return 'F'


get_grade(70, 70, 70)
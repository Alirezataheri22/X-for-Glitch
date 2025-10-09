"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    
   return [round(score) for score in student_scores]

def count_failed_students(student_scores):
    return sum(1 for score in student_scores if score <= 40)


def above_threshold(student_scores, threshold):
    return [score for score in student_scores if score >= threshold]



def letter_grades(highest):
    interval = (highest - 40) // 4
    
    d_threshold = 40 + 1  
    c_threshold = d_threshold + interval  
    b_threshold = c_threshold + interval 
    a_threshold = b_threshold + interval 
    
    return [d_threshold, c_threshold, b_threshold, a_threshold]


def student_ranking(student_scores, student_names):

    ranking = []
    for i, (score, name) in enumerate(zip(student_scores, student_names), 1):
        ranking.append(f"{i}. {name}: {score}")
    return ranking


def perfect_score(student_info):
    for student in student_info:
        if student[1] == 100:
            return student
    return []

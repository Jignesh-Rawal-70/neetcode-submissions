from typing import List, Tuple

def best_student(scores: List[Tuple[str, int]]) -> str:
    max_score = 0
    winner_student_name = ''
    for name, score in scores:
        #print(name, score, max_score)
        if score > max_score:
            max_score = score
            winner_student_name = name
    
    return winner_student_name


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))

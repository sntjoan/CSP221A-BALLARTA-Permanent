import pandas as pd
import numpy as np
from student import build_students, rank_students 

raw_rows = [
    {"name": " Amara ", "scores": "92,85,78"},
    {"name": "Leo", "scores": "88,91,73"},
    {"name": "Priya", "scores": "65,72,150"},         
    {"name": "Sam", "scores": "70,not_a_number,60"},  
    {"name": "Amara", "scores": "95,90,88"},          
    {"name": "Jade", "scores": "81,77,84,90"},
]

students, failures = build_students (raw_rows)

print("STUDENTS")
for students in students:
    print(student)
    
print("\nFAILURES")
for failures in failures:
    print(failures)

print 
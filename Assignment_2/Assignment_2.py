# Program Name: Assignment_2.py
# Course: IT3883/Section 01
# Student Name: Ceejay Raut
# Assignment Number: Lab2
# Due Date: 09/28/2026
# Purpose: Python program that calculates the final averages for a group of students and print the results in descending order by grade. 
# Resources: Claude (debugging hints, comment cleanup), Turbo AI (learning), GitHub (code snippets for arguments and parameters)

import statistics #Imported the statistics module to calculate the average of the scores for each student.



name_avg_grade = {}
with open ("/Users/ceejayraut/Downloads/Assignment2input.txt", "r") as file: #Import the txt files that has the values for calutating the avg of grades.
    for line in file:
        parts = line.split() #split the values in the txt file to be able to separate the name and the scores.
        name = parts[0]
        num_scores = [] #list to hold the scores for each student.
    
            

        for s in parts[1:]:
            num_scores.append(int(s)) #Seperation the values of the scores to be integers for calculating the average.]

        avg_score = statistics.mean(num_scores) #Use the statistics module to calculate the average of the scores for each student.
        
        name_avg_grade[name] = avg_score #Made a dictionary to hold the name and the average score for each student.

        
sorted_scores = sorted(name_avg_grade.items(), key=lambda x: x[1], reverse=True) #Sort the scores in descending order.

for name, avg in sorted_scores: #make a for loop to print the name and the average score in descending order.
    print(f"{name}: {avg:.2f}") #Print the name and the average score in descending order within 2 decimal places.
        









    
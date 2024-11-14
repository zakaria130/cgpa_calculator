import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
from pandas.plotting import table
from pdf_maker import dataframe_to_pdf
from jpg_maker import dataframe_to_jpg
from png_maker import dataframe_to_png
import os
df = pd.DataFrame(columns=["Subject", "Credits", "Marks", "Grade Point", "Score"])

def calculate_cgpa():
    num_courses = int(input("Enter the number of courses: "))
    total_credits = 0
    total_score = 0
    if num_courses==0:
        print("Invalid number")
        return
    
    for i in range(num_courses):
        subject_name = f"Subject {i+1}"
        print(subject_name)
        credits = float(input(f"Enter credits for {subject_name}: "))
        marks = float(input(f"Enter obtained marks for {subject_name}: "))
        grade_point = get_grade_point(marks)
        total_credits += credits
        total_score += credits * grade_point
        df.loc[i] = [subject_name, credits, marks, grade_point, credits * grade_point]

    df.loc[num_courses] = ['Total', total_credits, '', '', total_score]
    cgpa = total_score / total_credits
    #formatted_cgpa = f"{cgpa:.2f}"
    #cgpa=float(formatted_cgpa)
    df.loc[num_courses + 1] = ['CGPA',cgpa , '', '', ""]
    
    print(df)
    save_option(df)

def get_grade_point(marks):
    
    if marks < 40:
        grade_point = 0
    elif marks >= 40 and marks < 45:
        grade_point = 2
    elif marks >= 45 and marks < 50:
        grade_point = 2.25
    elif marks >= 50 and marks < 55:
        grade_point = 2.50
    elif marks >= 55 and marks < 60:
        grade_point = 2.75
    elif marks >= 60 and marks < 65:
        grade_point = 3
    elif marks >= 65 and marks < 70:
        grade_point = 3.25
    elif marks >= 70 and marks < 75:
        grade_point = 3.5
    elif marks >= 75 and marks < 80:
        grade_point = 3.75
    elif marks >= 80 and marks <= 100:
        grade_point = 4.00
    else:
        print("Invalid input! Marks should be between 0 and 100.")
        os.sys.exit("Exiting the program.")
        
    return grade_point
def save_option(f):
    print("Result Save as:\n1.xlsx\n2.PDF\n3.JPG\n4.PNG")
    loop_controler=True
    n=0
    
    while loop_controler:
        x=int(input())
        if x==1:
            file_path=check_and_rename("output.xlsx")
            f.to_excel(file_path, index=False, engine='openpyxl')
            print(f"File save as {file_path}")
            return
        elif x==2:
            file_path=check_and_rename("output.pdf")
            dataframe_to_pdf(f,file_path)
            return
        elif x==3:
            file_path=check_and_rename("output.jpg")
            dataframe_to_jpg(f,file_path)
            return
        elif x==4:
            file_path=check_and_rename("output.png")
            dataframe_to_png(f,file_path)
            return
        else:
            n+=1
            print("You Pressed the Wrong Number. Please select a valid option.")
            if n==4:
                print("file don't saved")
                return
def check_and_rename(file_path):
    """Check if file exists and rename it if necessary."""
    if os.path.exists(file_path):
        base, ext = os.path.splitext(file_path)
        counter = 1
        # Try renaming the file with a counter
        while os.path.exists(f"{base}_{counter}{ext}"):
            counter += 1
        file_path = f"{base}_{counter}{ext}"
    return file_path


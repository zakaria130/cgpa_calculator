import pandas as pd
import openpyxl
from others import get_grade_point
from others import save_option
from pdf_maker import dataframe_to_pdf
def dphysics_cgpa():
    year=int(input("Year :"))
    semester=int(input("Semester :"))
    row_file_path=f"Raw file\\{year}_{semester}.xlsx"
    df=pd.read_excel(row_file_path)
    n=df.shape[0]
    f="\t".join(str(df.iloc[1, i]) for i in range(2))


    for i in range(n):
        f="\t".join(str(df.iloc[i, j]) for j in range(2))
        credi=df.at[i,"Credit"]
        marks=int(input(f"{f} ........... Marks :"))
        df.at[i,"Marks"]=marks
        points=get_grade_point(marks)
        df.at[i,"Points"]=points
        score=credi* points
        df.at[i,"Score"]=score
    x=df["Score"].sum()
    y=df["Credit"].sum()
    df.loc[n]=['','',"Total",y,'','',x]
    cgpa=f"CGPA = {x/y:.2f}"
    df.loc[n+1]=['',cgpa,'','','','','']
    if year == 1:
        year = "First"
    elif year == 2:
        year = "Second"
    elif year == 3:
        year = "Third"
    elif year == 4:
        year = "Fourth"
    if semester==1:
        semester="First"
    elif semester==2:
        semester="Second"
    df.loc[n+2]=['Year',year,'','','','','']
    df.loc[n+3]=['Semester',semester,'','','','','']
    print(df)
    save_option(df)
    return
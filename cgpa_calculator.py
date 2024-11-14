import shutil
from others import calculate_cgpa 
from dphysics import dphysics_cgpa

terminal_size = shutil.get_terminal_size()
width = terminal_size.columns 
print(".................... CGPA Calculator System ....................".center(width))

loop_controler=True
while loop_controler:
    print("Select Option:\n1.Department of Physics, BSMRSTU\n2.Others\n3.Exit")
    x=int(input())
    if x==1:
        dphysics_cgpa()
    elif x==2:
        calculate_cgpa()
    elif x==3:
        loop_controler=False
        print("Successfully Exit")
    else:
        print("You Pressed the Wrong Number. Please select a valid option.")
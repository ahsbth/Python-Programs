
import os
print(os.name)
#os.makedirs("D:HEllo")
os.chdir("D:\\REALME 5S")
cwd=os.getcwd()
print("The current working directory=",cwd)
print(os.listdir(cwd))
os.rmdir("D:\\HEllo")
file1=open("grades.txt","r")
file2=open("errors.txt","w")
leng=(file1.read())
print("Length of file",len(leng))
file1.seek(0)
file1.readline()
file1.readline()
length=len(file1.readline())
print("Length of a line",length)
cout=0
for i in range (len(leng)):
   
    if str(leng[i])=="\n":
        cout+=1
print("Number of line ",cout)
file1.seek(0)
file1.readline()
file1.readline()
for i in range (1,21):
    ln=str(file1.readline())
    
    for j in range (len(ln)):
        if j<10:

            if ln[j]==" ":
                file2.write(f"{i+3} {ln}")
                break
file1.seek(0)
file1.readline()
file1.readline()
for i in range (1,21):
    ln=str(file1.readline())
    for j in range(len(ln)):
        if len(ln)<58:
            file2.write(f"{i+2} {ln}")

        if i == 21:
            file2.write(f"{i+2} {ln}")
        break
           

file1.seek(0)
for i in range(1,22):
    rln = file1.readline()
    for j in range(len(ln)):
        if len(ln)<58:
            file2.write(f"{i+2} {ln}")

        if i == 21:
            file2.write(f"{i-2} {ln}")
        break

file1.seek(0)
file1.readline()
file1.readline()
seek = 0
for i in range(1,22):
    read = file1.readline()

    if i == 3:
        read = file1.readline()
        file2.write(f"{i+3} {read}")
    if i == 9:
        read = file1.readline()
        file2.write(f"{i+4} {read}")
        

            
file1.close()
file2.close()





x=input("Enter a word : ")
y=[]
for i in x[:]:
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U" ):
        y.append(i)
print(y)
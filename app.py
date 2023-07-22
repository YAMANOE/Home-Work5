i=0
m=1
print("Hi buddy")
userName=input("enter your name : ")
fatherName=input(" Write the name of the father : ")
matherName=input("Write the name of the mother : ")
while i<=m:
    def printName(userName,fatherName,matherName):
        print("your name is "+userName)
        print("father name is "+fatherName)
        print("mother name is "+matherName)
        
    def lenOfname(userName,fatherName,matherName) :
        if  len(userName) <len(fatherName) :
            print("your name : ",userName,"  less than father name : ",fatherName)
        if len(userName) < len(matherName)  :
            print("your name : ",userName,"  less than mather name : ",matherName ) 
        if len(userName)==len(matherName) and len(fatherName) :   
            print("your name : ",userName,"  is sami mother name : ",matherName,"\n and ","father name ",fatherName,end= " ") 
        if  len(userName)==len(matherName):
            print("your name : ",userName,"  is sami mother name : ",matherName) 
        if  len(userName)==len(fatherName):
            print("your name : ",userName,"  is sami father name : ",fatherName)      
        if len(userName)>len(fatherName):
            print("your name : ",userName," is longer than father name :",fatherName)
        if len(userName) > len(matherName):
            print("your name : ",userName," is longer than mother name :",matherName)
        
    def printAndlen(userName,fatherName,matherName):
         printName(userName,fatherName,matherName)
         lenOfname(userName,fatherName,matherName)
                
    break 

printAndlen(userName,fatherName,matherName)


             






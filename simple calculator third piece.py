7#third simple calculator

print("Enter sign as '=' to stop ")
print()
num=0
while num>=0:
        if num==0:
            
            def cal():
                global a
            
                if s=="+":
                    a=float(n1)+float(n2)
                elif s=="-":
                    a=float(n1)-float(n2)
                elif s=="*":
                    a=float(n1)*float(n2)
                elif s=="/":
                    a=float(n1)/float(n2)
                return a
    

        
            n1=input("Enter number")
            i=0
            while i==0:
                count=0
                for j in range(len(n1)):
                        
                        if n1[j]==".":
                                count+=1
                
                        if n1[j] not in "1234567890.":
                            print("Error")
                            break

                        if count>1 or count==len(n1):
                                print("Error")
                                break
                                
                
                           
                else:       
                        break
                n1=input("Enter number")
               
                        
                    
      
            s=input("Enter sign")
            while i==0:
                if s not in ("+","-","*","/","="):
                    print("WRONG SIGN")
                    s=input("Enter sign")
                    
                else:
                    
                    break
                
            
            if len(s)>=2:
                print("Error")
                continue
            if s=="=":
                print("=",n1)
                break

            n2=input("Enter number")
            i=0
            while i==0:
                count=0
                for j in range(len(n2)):
                        
                        if n2[j]==".":
                                count+=1
                
                        if n2[j] not in "1234567890.":
                            print("Error")
                            break

                        if count>1 or count==len(n2):
                                print("Error")
                                break
                                
                
                           
                else:       
                        break
                n2=input("Enter number")
               
               
       

            a=cal()
        
            for i in range(len(str(a))):
                b=str(a)
            
                if b[i]==".":
                
                    if len(b[i:])>=3:
                        print(a)
    
                    else:
                        if b[i+1]!="0":
                            print(a)
    
                        else:
                            print(int(a))
        
    

        
        def cal1():
            global a
           
            if t=="+":
                    a+=float(n)
            elif t=="-":
                    a-=float(n)
            elif t=="*":
                    a*=float(n)
            elif t=="/":
                    a/=float(n)
            return a
        
        t=input("Enter sign")
        
        while t not in ("+","-","*","/","="):
            print("WRONG SIGN")
            t=input("Enter sign")
            
            

                
        if t=="=":
            A=cal1()
            for i in range(len(str(A))):
                B=str(A)
                if B[i]==".":
                    if len(B[i:])>=3:
                        print("=",A)
                    
                

                    else:
                        if B[i+1]!="0":
                            print("=",A)
                        
    
                        else:
                            print("=",int(A))
                        
            break
            
        n=input("Enter number")
        i=0
        while i==0:
                count=0
                for j in range(len(n)):
                        
                        if n[j]==".":
                                count+=1
                
                        if n[j] not in "1234567890.":
                            print("Error")
                            break

                        if count>1 or count==len(n):
                                print("Error")
                                break
                                
                
                           
                else:       
                        break
                n=input("Enter number")
               
                   
                    
                 
          
        A=cal1()
        for i in range(len(str(A))):
            B=str(A)
            if B[i]==".":
                if len(B[i:])>=3:
                    print(A)
                

                else:
                    if B[i+1]!="0":
                        print(A)

                    else:
                        print(int(A))

        num+=1

    
    


    
    




    


    

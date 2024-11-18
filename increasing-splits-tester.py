def split_tester(N, d):

    """
    (str,str)->bool
    Preconditions: positive integers and number of digits in N is divisble by number of integer represented by d
    returns True if sequence is strictly increasing and False otherwise
    """
    
    piece_length=int(d)
    pieces=[]

    #SPLITTING INTO PIECES
    for i in range(0,len(N), piece_length):
        piece=N[i:i+piece_length]
        pieces.append(piece)
            

    #PRINTING PIECES
    for i in range(len(pieces)):
        if i==len(pieces)-1:
            print(pieces[i])
        else:
            print(pieces[i],end=",")

    #CHECKS IF LENGTH OF PIECES ARE EQUAL            
    for i in range(1,len(pieces)):
        if int(pieces[i])<len(pieces[i-1]):
            return False
        
    #IF NUMBER REPEATS   
    sortedpieces=sorted(pieces)
    for i in range(1,len(pieces)-1):
        if sortedpieces[i]==sortedpieces[i+1]:
            return False
            
    #IF ITS INCREASING
    for i in range(len(pieces)-1):
        if int(pieces[i])>=int(pieces[i+1]):    
            return False
    return True 
    

    if True:
        print(pieces[i])  



def main():
    
    """
    ()->none
    Preconditions: only yes or no answers, and positive DIGITS
    prints wether the sequence is increasing or not.
    """
    
    welcome="__Welcome to my increasing-splits tester__"

    border1= "*" * (len(welcome)+10)
    print(border1)
    border2="*" + " "*(len(welcome)+8)+ "*"
    print(border2)
    border3="*" + "  "+ "__"+welcome+"__"+"  "+"*"
    print(border3)
    print(border2)
    print(border1)

    name=input("What is your name? ")

    splits=", welcome to my increasing-splits tester.__"
    border1= "*" * (len(name+splits)+10)
    print(border1)
    border2="*" + " "*(len(name+splits)+8)+ "*"
    print(border2)
    border3="*" + "  "+ "__"+name+splits+"__"+"  "+"*"
    print(border3)
    print(border2)
    print(border1)

    flag=True
    while flag:
        question=input(name+", would you like to test if a number admits an increasing-split of give size? ")
        question=(question.strip()).lower()
        
        if question=='no':
            goodbye="Good bye "+name+"!"
            border1= "*" * (len(goodbye)+10)
            print(border1)
            border2="*" + " "*(len(goodbye)+8)+ "*"
            print(border2)
            border3="*" + "  "+ "__"+goodbye+"__"+"  "+"*"
            print(border3)
            print(border2)
            print(border1)
            flag=False      
            
        elif question!="yes":
            print("Please enter yes or no. Try again.")
            
        elif question=="yes":
            print("Good choice!")

            valid=True
            while valid:
                N=input("Enter a positive integer: ").strip()

                if not N.strip("-").isdigit():
                    print("The input can only contain digits. Try again.")
                    valid=False
                    
                elif int(N)<=0:
                    print("The input has to be a positive integer")
                    valid=False
                
                else:
                    d=input("Input the split. The split has to divide the length of " + str(N) + " i.e "+ str(len(N))+"\n").strip()   

                    if not d.isdigit():
                        print("The split can only contain digits. Try again.")
                        valid=False                        

                    else:
                        d=int(d)

                        if d<=0:
                            print("The input cannot be 0")                    

                        elif int(len(N))%int(d)!=0:
                            print(str(d)+" does not divide "+str(len(N)))
                       
                        elif split_tester(N,d):
                            print("The sequence is increasing")
                       
                        else:
                            print("The sequence is not increasing")
                      
                valid=False
                  
main()

def greet():
    name=input("daweret tkveni saxeli")
    print("Hello world!")
    print("Hello "+ name)

greet()

# 1) შექმენით len ფუნქციის კლონი.
# 2) შექმენით find ფუნქციის(string ფუნქციის) კლონი
# 3) შექმენით range ფუნქციის კლონი

# Task 1
def kloni1(argumenti):
    number=0
    for i in argumenti:
        number+=1
    print(number)



# Task 2

def kloni2(word, sadziebo):
    counter=0
    while counter<len(word):
        if word[counter]==sadziebo:
          print (counter)
        counter+=1
    print(-1) 


kloni2("world","r")



def find_clone(text,char):
    result=-1
    index=0

    for i in text:
        if i== char and result==-1 :
            result=index
        index += 1
    print(result)


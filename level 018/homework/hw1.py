# 2) მოიძიეთ for ციკლზე ინფორმაცია და შეასრულეთ რამოდენიმე მაგალითი

# 3) for loop-ის გამოყენებით დაბეჭდეთ თქვენი სახელი 10-ჯერ

# 4) მომხმარებელს შემოატანინეთ 5 რიცხვი for loop-ის გამოყენებით გაიგეთ მათი საშუალო არითმეტიკული

# 5) ივარჯიშეთ if/elif/else-ებზე და გააკეთეთ რამოდენიმე მაგალითი მათზეც

# Task 2
# მაგალითი 1
for i in range(5):
    print("3")

# მაგალითი 2
for i in range (5):
    feri=input("დაწერეთ სამი საყვარელი ფერი")
    print(feri)

# Task 3
for i in range(10):
    print("inga")

# Task 4
jami=0
for i in range(5):
    num=int(input("shemoitanet ricxvi"))
    jami+=num
print(jami/5)

# Task 5 
# მაგალითი 1

sezoni=input("daweret tkveni sayvareli sezoni")

if sezoni=="gazafxuli":
    print("momxmareblis sayvareli sezonia Gazafxuli")
elif sezoni=="zafxuli":
    print("momxmareblis sayvareli sezonia zafxuli")
elif sezoni=="zamtari":
    print("momxmareblis sayvareli sezonia zamtari")
elif sezoni=="arcerti":
    print("momxmarebels ar akvs sayvareli sezoni")
else:
    print("momxmareblis sayvareli sezonia shemodgoma")

# მაგალითი 2
age=int(input("daweret tkveni asaki"))
if age<18:
    print("samwuxarod tkven ver sheqmnnit gverds")
else:
    print("shegidzliat shekmnat tkveni gverdi")

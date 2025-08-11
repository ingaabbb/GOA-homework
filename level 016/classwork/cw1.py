# 1) შექმენით პროგრამა, რომელიც მომხმარებელს შემოატანინებს თავის ასაკს, შეამოწმებს არის თუ არა ის 18-ზე ნაკლები და თუ ნაკლებია დაბეჭდავს "You are kid", ხოლოს სხვა ნებისმიერ შემთხვევაში დაბეჭდავს "You are adult"

# 2) შექმენით პროგრამა, რომელიც მომხმარებელს შემოატანინებს პაროლს და შეამოწმებს თუ ის არის "1234"-ის ტოლი მაშინ დაბეჭდავთ "Password is correct", სხვა შემთხვევაში "Password is incorrect"

# 3) მომხმარებელს შემოატანინეთ რიცხვი, თუ ის დადებითია დაბეჭდეთ "The number is positive", სხვა შემთხვევაში არაფერს აკეთებთ

# Task 1

age = int(input("shemoitanet tkveni asaki"))
if age< 18 :
    print("You are kid")
else:
    print("You are an adult")    

# Task 2

password=input("sheqmenit paroli")
if password =="1234":
    print("Password iscorrect")
else:
    print("password is incorrect")

# Task 3
number=float(input("shemoitanet ricxvi"))
if number>0 :
    print("The number is positive")

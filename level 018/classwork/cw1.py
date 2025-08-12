# 1) მომხმარებელს შემოატანინეთ რიცხვი, შემდეგ შეამოწმეთ თუ ეს რიცხვი არის 10-ზე დაბეჭდეთ "{ჩასვამთ რიცხვს, რომელსაც მომხარებელი
#  შემოიყვანს} არის 10-ზე ნაკლები", სხვა შემთხევევაში თუ 20-ზე ნაკლებია დაბეჭდავთ "{ჩასვამთ რიცხვს, რომელსაც მომხარებელი შემოიყვანს} 
# არის 20-ზე ნაკლები"

# ამისთვის დაგჭირდებათ if/elif

# 2) მომხარებელს შემოატანინეთ რიცხვი და თუ ის არის ლუწი დაბეჭდეთ "The number is even", სხვა შემთხვევაში დაბეჭდეთ "The number is odd"


# 3) მომხმარებელს შემოატანინეთ ამინდი და თუ ის არის "მზიანი", დაბეჭდეთ "ვივარჯიშებ გარეთ", სხვა შემთხვევაში თუ "წვიმიანი", დაბეჭდეთ
#  "ვივარჯიშებ გარეთ", ხოლო სხვა დანარჩენ შემთხვევაში დაბეჭდეთ "არ ვივარჯიშებ დღეს"

# Task 1 
num1=int(input("shemoitanet ricxvi"))

if num1<10:
    print(str(num1) + " naklebia 10ze")
elif num1<20:
    print(str(num1)+ " naklebia 20ze")
    
# Task 2
num2=int(input("shemoitanet ricxvi"))
if num2 % 2 == 0:
    print("The number is even")
else :
    print("The number is odd")

# Task 3
amindi=input("daweret rogori amindia")
if amindi=="mziani":
    print(" vivarjisheb garet")
elif amindi=="wvimiani":
    print("vivarjisheb saxlshi")
else:
    print("ar vivarjisheb dghes")

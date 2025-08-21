# 2) კომენტარებით ახსენით რა არის არგუმენტი

# 3) კომენტარებით ახსენით რა არის range ფუნქცია

# 4) დაბეჭდეთ 50-დან 100-ის ჩათვლით ყველა რიცხვის ჯამი

# 5) დაბეჭდეთ 100-დან 200-მდე ყველა რიცხვის ნამრავლი

# 6) კომენტარებით ახსენით რა განსხვავებაა for და while ციკლებს შორის

# 7) while ციკლის გამოყენებით დაბეჭდეთ დაბეჭდეთ 1-დან 10-ის ჩათვლით ყველა რიცხვი

# 8) შექმენით Guess number თამაში:

# შექმენით ცვლადი და შეინახეთ მასში 1-დან 10-ის ჩათვლით რიცხვი(ეს იქნება ჩაფიქრებული რიცხვი). მომხმარებელს იქამდე შემოატანინეთ რიცხვი,
# სანამ არ გამოიცნობს ჩაფიქრებულს. ყოველ არასწორად შეყვანილ რიცხვზე დაბეჭდეთ "Wrong number", ხოლო თუ მომხმარებელმა სწორად გამოიცნო
# რიცხვი, გათიშეთ while ციკლი და დაბეჭდეთ "You Win!"

# Task 4
jami=0
for i in range (50,101):
    jami+=i
print(jami)

# Task 5
namravli=1
for i in range(100,200):
    namravli*=i
print(namravli)

# Task 7 
i=1
while i<11:
    print(i)
    i+=1

# Task 8
chafikrebuli_ricxvi=7
ricxvi=int(input("shemoitanet ricxvi 1-10-is chatvlit"))
while chafikrebuli_ricxvi!=ricxvi:
    print("wrong number")
    ricxvi=int(input("shemoitanet ricxvi 1-10-is chatvlit"))

print("You win")


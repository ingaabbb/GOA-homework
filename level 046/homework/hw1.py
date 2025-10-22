# 1) შექმენი ფუნქცია, რომელიც ითვლის 1-დან 100-მდე რიცხვებიდან იმ რიცხვების რაოდენობას, რომლებიც იყოფა 3-ზე ან 5-ზე,
#  მაგრამ არა ორივეზე ერთად.

# 2) მომხმარებელს შეაყვანინე ნებისმიერი რიცხვი N. გამოიყენე for ციკლი და დაბეჭდე 1-დან N-მდე არსებული ყველა მარტივი რიცხვი 
# (prime numbers).

# 3) 50-დან 150-მდე ყველა რიცხვზე გააკეთე ციკლი და ცალცალკე დაითვალე ლუწი და კენტი რიცხვების ჯამი. ბოლოს დაბეჭდე ორივე ჯამი.

# 4) შექმენი ფუნქცია, რომელიც მომხმარებელს შემოატანინებს 5 სახელს შექმნის ამ სახელებისგან სიას და დააბრუნებს საბოლოოდ ამ სიას

# Task 1
def counter():
    counter=0
    for i in range(1,100):
        if (i%3==0 and i%5!=0) or (i%3!=0 and i%5==0):
            counter+=1
    return counter
print(counter())

# Task 3
luwi_jami=0
kenti_jami=0
for i in range(50,151):
    if i%2==0:
        luwi_jami+=i
    else:
        kenti_jami+=i

print(luwi_jami)
print(kenti_jami)
print(luwi_jami+kenti_jami)


def saxelebi():
    sia=[]
    for i in range(5):
        sia+=(input("shemoiyvanet saxeli"))
    
    return sia

print(saxelebi())
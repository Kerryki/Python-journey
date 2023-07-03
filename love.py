# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1o= name1.lower()
name2o=name2.lower()
t= name1o.count("t")+ name2o.count("t")
r=name1o.count("r")+ name2o.count("r")
u=name1o.count("u")+ name2o.count("u")
e=name1o.count("e")+ name2o.count("e")
l=name1o.count("l")+ name2o.count("l")
o=name1o.count("o")+ name2o.count("o")
v=name1o.count("v")+ name2o.count("v")
first=(t+r+u+e)*10
second=l+o+v+e
total= first+second
if total<10 or total>90:
    print("Your score is " + str(total) + ", you go together like coke and mentos")
elif total>=40 and total<=50:
    print("Your score is " + str(total) + ", you are alright together")
else:
    print("Your score is " + str(total))

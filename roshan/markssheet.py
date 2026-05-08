Hindi=int(input("enter your hindi marks: "))
science=int(input("enter your science marks: "))
math=int(input("enter your math marks: "))
english=int(input("enter your english marks: "))
social_science=int(input("enter your social socience number: "))


total = Hindi+science+math+english+social_science
percentage = total/5
print(f"total marks: ",total)
print(f"percentage: ",percentage)


if percentage>=90:
    print("Grade: A+")
elif percentage>=80:
    print("Grade: A")
elif percentage>=70:
    print("Grade: B")
elif percentage>=60:
    print("Grade: C")
else:
    print("Fail")
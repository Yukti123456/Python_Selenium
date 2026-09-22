# 13. Age Category
#
# Take age and classify it as:
#
# 0–12    → Child
# 13–19   → Teenager
# 20–59   → Adult
# 60+     → Senior
#
# Use guards with if.

age = int(input("Enter file age: "))
match age:
    case _ if (age >= 0 and age <= 12):
        print("Child")
    case _ if (age >= 13 and age <= 19):
        print("Teenager")
    case _ if (age >= 20 and age <= 59):
        print("Adult")
    case _ if(age >= 60):
        print("Senior")

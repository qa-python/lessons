print("Hello world!")

user_name = input("Enter your name: ")
print(f"Hello {user_name}")

print("*********\n"
      "*       *\n"
      "*       *\n"
      "*********")

#######################################################################################################################
# 2.1
health = int(input("Enter a number of HP: "))
if health <= 0:
    print("False")
else:
    print("True")

# 2.2
n = int(input("Enter even or odd num: "))
if n % 2 == 0:
    print("Четное")
else:
    print("Нечетное")

# 2.3
n = int(input("Enter year: "))
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print("Високосный")
else:
    print("Не високосный")

# 2.4
text = input("Write text here: ")
num = int(input("Number of counts: "))
for i in range(num):
    print(text)

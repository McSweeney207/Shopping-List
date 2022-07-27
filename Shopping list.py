import time

chilli = ["Onions", "Peppers", "Mushrooms", "Mixed Beans", "Spice Packet", "rice"]
tofu = ["tofu", "soy", "rice", "peas", "Mushrooms"]
curry = ["chicken", "peppers", "paste", "rice"]

print("Hello!")
time.sleep(1)
print("My name is Duncan Dinners.  I am here to help you with your meal plan.")
time.sleep(1)

mon = input("What would like to eat for dinner on monday? press 1 for Chilli, 2 for tofu or 3 for Curry: ")

if mon == "1":
    monday = chilli
if mon == "2":
    monday = tofu
if mon == "3":
    monday = curry

tue = input("Great, thanks for that. Now, What would like to eat for dinner on monday? press 1 for Chilli, 2 for tofu or 3 for Curry: ")

if tue == "1":
    tuesday = chilli
if tue == "2":
    tuesday = tofu
if tue == "3":
    tuesday = curry

print("Cool! now processing your list.....")
time.sleep(3)
print("...Processing...")
time.sleep(3)
print("OK! Here is your Shopping List!")

time.sleep(1)

list = monday + tuesday

word_count = []

for word in list:
  if word in word_count:
    word_count [word] += 1
  else:
    word_count [word] = 1

for i in word_count:
  print(i)
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

##Looping Through a String
for x in "banana":
  print(x)


#####
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

####
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

######starting from 0
for x in range(6):
  print(x)



for x in range(2, 6):
  print(x)


for x in range(2, 30, 3):
  print(x)


# Nested loops

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


###########
i = 1
while i < 6:
  print(i)
  i += 1
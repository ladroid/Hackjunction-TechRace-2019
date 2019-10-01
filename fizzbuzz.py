from __future__ import print_function

for num in range(1, 21):
  string = ""
  if num % 3 == 0:
    string = string + "Tech"
  if num % 5 == 0:
    string = string + "Race"
  if num % 5 != 0 and num % 3 != 0:
    string = string + str(num)
print(string, end ='') 

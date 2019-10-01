total_sum = 0
for i in range(10):
    if (i%3 == 0 or i%5 == 0 or i%7 == 0):
        total_sum = total_sum+i
print(total_sum)

def long_word(x):
  new_arr = x.split(' ')
  return (max(new_arr, key=len))

sen = input()
print(long_word(sen))

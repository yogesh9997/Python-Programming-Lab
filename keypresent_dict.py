d = eval(input("enter the dict"))

def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')

k=int(input("enter the dict"))
is_key_present(k)

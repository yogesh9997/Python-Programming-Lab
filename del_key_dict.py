d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      del d[k]
  else:
      print('Key is not present in the dictionary')

k=int(input("enter the key"))
is_key_present(k)

print("Updated dict is : ",d)

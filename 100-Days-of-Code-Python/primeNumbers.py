
prime = False
count = 0
min_range=1
max_range=100000
for num in range(min_range,max_range):
  for div in range(2,num):
    if num % div == 0:
      prime=False;
      break;
    else:
      prime=True
  if prime==True:
    count += 1
  if num % 10000 == 0:
      print(num)
print(f"Total of {count} primes between {min_range} and {max_range}")
num = int(input("enter number"))

if num < 1:
  print("not prime")

 for i in range(2,num):
          if num % i == 0:
              print(num+" is prime")
              break
 else:
  print("not prime")

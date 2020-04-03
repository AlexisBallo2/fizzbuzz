x = int(input(("WHhat number do you want to go until?: ")))

for a in range(1,x +1):
    if a % 3 == 0 and a % 5 == 0:
        print("Fizzbuzz")
    elif a % 3 == 0 and a % 5 != 0:
        print("Fizz")
    elif a %3 != 0 and a %5  ==0:
        print("buzz")
    else:
        print(a)

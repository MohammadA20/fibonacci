n = int(input("Please enter a number: "))
strt = 0
strt2 = 1
cnt = 0

#Here we will do the fibonacci sequence of the times entered in n
for cnt in range(n):
    print("Here we continue: ", strt)
    print("This is the second number: ", strt2)
    fibonacci = strt + strt2
    strt = strt2
    strt2 = fibonacci
    print("Here is the summation in fibonacci: ", fibonacci)
    cnt += 1
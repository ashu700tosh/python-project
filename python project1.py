
# checking whether number is prime or composite and  count  also....


# taking two number

num1 = int(input("enter Number1:"))
num2 = int(input("enter Number2:"))
# using count function
count1=0
count2=0

# by using for loop

for i in range(num1,num2+1):
    hello=0        # taking helllo variable
    for j in range(2,i):
        if(i%j==0):
            hello=1
            break  # use break to terminate the loop
#    using if , else statement
    if(hello==0):
        count1+=1
        print(i,"is prime number") # print prime
    else:
        count2+=1
        print(i,"is composite number") # print composite number

    # printing no. of prime number and composite

print('count:',count1,'prime number',count2,'composite number','in a range')

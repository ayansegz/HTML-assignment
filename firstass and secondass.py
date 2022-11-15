print ("THIS IS A PROGRAM THAT SHOW HOW A NUMBER IS DIVISIBLE BY 15 AND A MULTIPLE OF 5.❤🛴")


# TO DISPLAY M+NUMBER OF MULTIPLE OF 5 AND DIVISIBLE BY 15
num =[]
for x in range (10,150):
    if (x%15==0) and (x%5==0):
        num.append(str(x))
    print (','.join(num))
print (' #########🏴🏳🏳🏴#################🚩🚩🚩################################')


\n
print (' #########🏴🏳🏳🏴#################🚩🚩🚩################################')
# # TO PRINT PRIME NUMBER IN ANY NUMBER
# lower = int(input("Enter the beginning number:"))
# upper = int(input("enter the highest number:"))
# for num in range (lower,upper):
#     count = 0
#     for i in range (2, (num//2 + 1)):
#         if (num % i ==0):
#             count = count + 1
#             break 
#         if (count == 0 and num != 1):
#             print ("%d" %num, end='')
        
print ("Hey Bro, It's Done!")
sugar = int(input())

count3 = 10000
count5 = 10000
count35 = 10000

if sugar % 3 == 0:
    count3 = sugar // 3
    rest_sugar  = 0
if sugar % 5 == 0:
    count5 = sugar // 5
    rest_sugar = 0

count35 = sugar // 5
count35 += sugar % 5 // 3
rest_sugar = sugar % 5 % 3

if rest_sugar > 0 and (count3 == 10000 and count5 == 10000):
    print (-1)
elif rest_sugar > 0 and (count3 == 10000 or count5 == 10000): 
    print(min(count3,count5))
else:
    print(min(count3,count5,count35))

print(count3)
print(count5)
print(count35)




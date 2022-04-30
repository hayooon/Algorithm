# < 잃어버린 괄호 >

# eq = input()
# if '+' not in eq or '-' not in eq:
#     result = eval(''.join(eq))
# else:
#     eq = eq.split('-')
#     result = 0

#     for i in range(len(eq)):
#         if i == 0:
#             result += int(eq[i])
#         else:
#             result = result - eval(eq[i])   

# print(result)

eq = input()
result = 0
if '-' not in eq:
    for i in eq.split('+'):
        result += int(i)
elif '+' not in eq:
    for i in range(len(eq.split('-'))):
        if i == 0:
            result += int(i)
        else:
            result -= int(i)
else:
    eq = input().split('-')
    for i in range (len(eq)):
        if i == 0 :
            result += int(eq[i])
        else:
            small = eq[i].split('+')
            sum = 0
            for j in range (len(small)):
                sum += int(small[j])
            result -= sum
print(result)
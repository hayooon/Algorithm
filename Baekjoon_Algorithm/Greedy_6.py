# # < 잃어버린 괄호 >


eq = input()
result = 0

if '-' not in eq:
    for i in eq.split('+'):
        result += int(i)

elif '+' not in eq:
    eq = eq.split('-')
    for i in range(len(eq)):
        if i == 0:
            result += int(eq[i])
        else:
            result -= int(eq[i])
            
# 섞여있는 경우            
else:
    eq = eq.split('-')
    for i in range (len(eq)):
        small = eq[i].split('+')
        sum = 0
        for j in range (len(small)):
            sum += int(small[j])
        if i == 0:
            result += sum   
        else: result -= sum
print(result)

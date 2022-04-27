# <설탕 배달> # 틀림

sugar = int(input())

count = 0 

while(True):
    if sugar < 3:
        print (-1)
        break
    else:
        if sugar % 5 == 0:
            count += sugar // 5
            print(count)
            break
        else:
            sugar -= 3
            count += 1

    if sugar == 0:
        print(count)
        break     
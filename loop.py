x = 10
while (x <= 10) :
    print("while of x :",x)
    for i in range (1,6) :
        if i == 3:
            continue
        if i == 6:
            break
        print(i)
        x += 1
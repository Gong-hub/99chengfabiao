for i in range(1,10):
    for j in range(1,10):
        if j <= i:
            print("{}x{}={}".format(j,i,i*j),end=" ")
    print()

def primitiveRoot(g):
    results = []
    for i in range(1,23,1):
        k = pow(g,i,23)
        results.append(k)
        #results.sort()
    print("g=%d ise: "%(g), results)




primitiveRoot(5)





#print(pow(11,3,13))
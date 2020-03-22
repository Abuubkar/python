

with open("Test01.in","rt") as fin:
    pow1=fin.readline()
    power1=int(pow1.strip())
    v1 = fin.readline().split()
    val1=[]
    for i in v1:
        val1.append((int)(i))
    pow2 = fin.readline()
    power2 = int(pow2.strip())
    v2 = fin.readline().split()
    val2 = []
    for i in v2:
        val2.append((int)(i))

    print(str(power1+power2))

    ans=[]
    for i in range(0,power1+power2+1):
        ans.insert(i,0)

    for i in range(0,len(val1)):
        for j in range(0,len(val2)):
            ans[i+j]=ans[i+j]+(val1[i]*val2[j])

    anss=''
    for i in ans:
        anss= anss+ ' '+str(i)
    print(anss.strip())


#creates a ref for every page

str=input("Enter the pages separated by comas: ")
pages=str.split(",")
n=int(input("Enter the number of frames: "))
print("The pages are: ")
print(pages)
print("Clock page replacement algorithm")

for i in range(len(pages)):
    pages[i]=int(pages[i])

frame=[-1]*n
r=[-1]*n
fault=0
hit=0
pt=0

for i in range(len(pages)):
    flag=False
    if pages[i] in frame:
        hit+=1
        flag=True
        id=frame.index(pages[i])
        r[id]=1
    else:
        if i>=n:
            if r[pt]==0:
                frame[pt]=pages[i]
                pt=(pt+1)%n
            else:
                r[pt]=0
                pt=(pt+1)%n
                while r[pt]!=0:
                    r[pt]=0
                    pt=(pt+1)%n
                frame[pt]=pages[i]
                pt=(pt+1)%n
            # frame[pt]=pages[i]
            # pt+=1
        else:
            frame[pt]=pages[i]
            r[pt]=0
            pt=(pt+1)%n
            
            
        fault+=1

    print(frame)
    print(r)
    if flag==True:
        print("Page Hit")
    else:
        print("Page Fault")

print("Number of page hits: ",hit)
print("Number of page faults: ",fault)

print("Hit ratio: ",hit/len(pages))
print("Fault ratio: ",fault/len(pages))
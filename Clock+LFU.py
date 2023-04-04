#based on priority and reference bit
#derived from LRU and CLOCK

def count_frequency(i):
    print("Previous frame: ", end="")
    print(frame)
    print("Previous reference bit: ", end="")
    print(r)
    lst=pages[i:len(pages)]
    c=[]
    for p in frame:
        c.append(lst.count(p))
    min=c[0]
    print("Freq count: ", end="")
    print(c)
    for ch in c:
        if ch<min:
            min=ch
    print("Minimum frequency: ", end="")
    print(min)
    for j in range(len(c)):
        if c[j]==min:
            pr[j]="L"
        else:
            pr[j]="H"
    print("Priority initial: ", end="")
    print(pr)

def check_priorities(pt):
    if pr[pt]=="H":
        pr[pt]="L"
        pt=(pt+1)%n
        return pt
        # check_priorities(pt)
    else:
        if r[pt]==1:
            r[pt]=0
            pt=(pt+1)%n
            return pt
            # check_priorities(pt)        

print("Clock+LFU page replacement algorithm")    
str=input("Enter the pages separated by comas: ")
pages=str.split(",")
n=int(input("Enter the number of frames: "))
print("\nThe pages are: ")
print(pages)
print("\n")

for i in range(len(pages)):
    pages[i]=int(pages[i])

frame=[-1]*n
fault=0
hit=0
r=[-1]*n
pr=[-1]*n
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
            count_frequency(i)
            while pr[pt]=="H" or (pr[pt]=="L"and r[pt]==1):
                pt=check_priorities(pt)
                # print("Executed")
            
            frame[pt]=pages[i]
            pr[pt]="H"
            pt=(pt+1)%n

        else:
            frame[pt]=pages[i]
            r[pt]=0
            pr[pt]="H"
            pt=(pt+1)%n            
            
        fault+=1

    print(frame)
    # print(pt)
    print(r)
    print(pr)
    if flag==True:
        print("Page Hit")
    else:
        print("Page Fault")
    print()

print("Number of page hits: ",hit)
print("Number of page faults: ",fault)

print("Hit ratio: ",hit/len(pages))
print("Fault ratio: ",fault/len(pages))
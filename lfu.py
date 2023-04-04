#Least Frequently Used (LFU) Page Replacement Algorithm
#replaces the page that is least frequently used i.e. less count

str=input("Enter the pages separated by comas: ")
pages=str.split(",")
n=int(input("Enter the number of frames: "))
print("The pages are: ")
print(pages)
print("Clock page replacement algorithm")

for i in range(len(pages)):
    pages[i]=int(pages[i])

frame=[-1]*n
fault=0
hit=0

for i in range(len(pages)):
    flag=False
    if pages[i] in frame:
        flag=True
        hit+=1
    else:
        if i<n:
            frame[i]=pages[i]
        else:
            lst=pages[i:len(pages)]
            c=[]
            for p in frame:
                c.append(lst.count(p))
            id=c.index(min(c))
            frame[id]=pages[i]
        fault+=1

    print(frame)
    if flag==True:
        print("Page Hit")
    else:
        print("Page Fault")

print("Number of page hits: ",hit)
print("Number of page faults: ",fault)

print("Hit ratio: ",hit/len(pages))
print("Fault ratio: ",fault/len(pages))


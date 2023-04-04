#replaces the least recently used page, from the left 

str=input("Enter the pages separated by comas: ")
pages=str.split(",")
n=int(input("Enter the number of frames: "))
print("The pages are: ")
print(pages)
print("FIFO page replacement algorithm")

for i in range(len(pages)):
    pages[i]=int(pages[i])

frame=[-1]*n
fault=0
hit=0

for i in range(len(pages)):
    flag=False
    if pages[i] in frame:
        hit+=1
        flag=True
    else:
        if i>=n:
            temp=pages[0:i]
            temp.reverse()
            c=[]
            for j in range(len(frame)):
                if frame[j] in temp:
                    c.append(len(temp)-temp.index(frame[j])-1)
                else:
                    c.append(100)
            frame[c.index(min(c))]=pages[i]
        else:
            frame[i]=pages[i]
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

#To find the last index 

# l=[7,0,1,2,0,3,0,4,2,3,0,3,2]
# l.reverse()
# id=l.index(3)
# print(len(l)-id-1)
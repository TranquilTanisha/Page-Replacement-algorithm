#replaces the page that is used the farthest in the future, towards the right

str=input("Enter the pages separated by comas: ")
pages=str.split(",")
n=int(input("Enter the number of frames: "))
print("The pages are: ")
print(pages)
print("Optimal page replacement algorithm")

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
            temp=pages[i+1:]
            c=[]
            for j in range(len(frame)):
                if frame[j] in temp:
                    c.append(temp.index(frame[j]))
                else:
                    c.append(100)
            frame[c.index(max(c))]=pages[i]
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
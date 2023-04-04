#Replaces pages with fifo rule, if the page is already in the frame, pointer doesn't move

str=input("Enter the pages separated by comas: ")
pages=str.split(",")
n=int(input("Enter the number of frames: "))
print("The pages are: ")
print(pages)
print("FIFO page replacement algorithm")

for i in range(len(pages)):
    pages[i]=int(pages[i])

frames=[-1]*n
fault=0
hit=0

for i in range(len(pages)):
    flag=False
    if pages[i] in frames:
        hit+=1
        flag=True
    else:
        frames[i%n]=pages[i]
        fault+=1
    print(frames)
    if flag==True:
        print("Page Hit")
    else:
        print("Page Fault")

print("Number of page hits: ",hit)
print("Number of page faults: ",fault)

print("Hit ratio: ",hit/len(pages))
print("Fault ratio: ",fault/len(pages))


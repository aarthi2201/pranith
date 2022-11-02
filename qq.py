front=0
rear=0
mymax=eval(input("enter amximum size of queue:"))
def create Queue():
    queue=[ ]
    return queue
def isempty(queue):
    return len(queue)==0
def enqueue(queue,item):
    queue.append(item)
    print("enqueued to queue",item)
def dequeue(queue)
    if isempty(queue):
        return("queue is empty")
    item=queue[0]
    del queue[0]
    return item
    queue=create queue()
while True:
    print("1.enqueue")
    print("2.dequeue")
    print("3.display")
    print("4.quit")
    ch=int(input("enter your choice"))
    if ch==1:
        if rear<mymax
           item=input("enter any elemnts:")
        enqueue(queue,item)
        rear+=1
        else:
            print("queue is full")
        elif:
            print(dequeue(queue))
        elif ch==3:
            print(queue)
        else:
            print("exit")
            break

MAX = 6;
intArray = [0] * MAX
front = 0;
rear = -1;
itemCount = 0;
def isFull():
    return itemCount == MAX
def isEmpty():
    return itemCount == 0
def removeData():
    data = intArray[front+1]
    if(front == MAX):
        front = 0
    itemCount-1
    return data
def insert(data):
    global rear, itemCount
    if(not isFull()):
        if(rear == MAX-1):
            rear = -1
        rear = rear + 1
        intArray[rear] = data
        itemCount+1

def display():
    print(intArray)
insert(3);
display()
insert(5);
display()
insert(9);
insert(1);
insert(12);
insert(15);
insert(151);

# removeData()
# display()
print("Queue: ")
for i in range(MAX):
    print(intArray[i], end = " ")
while(not isEmpty()):
    n = removeData()
    print(n, end = " ")
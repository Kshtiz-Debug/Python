class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None
        '''SO ITS AN EMPTY LIST'''


    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        current=self.head
        while current.next is not None:
            current=current.next
        current.next=new_node

    def display(self):
        current=self.head
        while current is not None:
            print(current.data,end="--->")
            current=current.next
        print(None)

    def insert_at_beginning(self,new_data):
        new_data=Node(new_data)
        new_data.next=self.head
        current=new_data
        self.head=new_data


    def delete_node(self, key):
        current=self.head
        if key==current.data:
            current=current.next
            self.head=current

        while current is not None:
            if current.next is not None:
                second = current.next
                if key == second.data :
                    current.next = second.next
                    return
            current = current.next

    def search(self, key):
        current=self.head
        count=-1
        while current is not None:
            count+=1
            if key==current.data:
                print(count)
                return
            current=current.next
        print(-1)
        return
    def length(self):
        count=0
        current=self.head
        while current is not None:
            count+=1
        return count


    def find_middle(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current=current.next

        x=0
        print(count)
        current=self.head
        if count%2==0:
            while current is not None:
                if x==count/2:
                    print(current.data)
                    return
                current=current.next
                x+=1
        else:
            while current is not None:
                if x==count//2:
                    print(current.data)
                    return
                current=current.next
                x+=1


    def nth_from_end(self, n):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current=current.next
        find=count+1-n
        count=0
        current=self.head
        while current is not None:
            count+=1
            if count==find:
                print(current.data)
                return
            current = current.next
    def has_loop(self):
        current=self.head
        l=[]
        while current is not None:
            if current in l:
                print("It is linked")
                print(current.data)
                return
            l.append(current)
            current=current.next
        print("The links are not inked")
        return

    def Create_has_loops(self,a,b):
        current=self.head
        while current is not None:
            if current.data==b:
                start=current
            if current.data==a:
                current.next=start
                return
            current=current.next







l1=LinkedList()
l1.append(2)
l1.append(4)
l1.append(76534627)

l1.display()


l1.insert_at_beginning(10)
l1.display()

l1.delete_node(76534627)
l1.display()

l1.insert_at_beginning(1091)
l1.display()

l1.insert_at_beginning(102)
l1.display()

l1.insert_at_beginning(14230)
l1.display()

l1.insert_at_beginning(158674560)
l1.display()

l1.insert_at_beginning(17530)
l1.display()



l1.delete_node(1091)
l1.display()


l1.search(10)


l1.search(567)



l1.find_middle()


l1.append(2345678998765)
l1.display()

l1.find_middle()



l1.display()

l1.nth_from_end(3)

l1.has_loop()

l1.append(2)

l1.display()

l1.has_loop()


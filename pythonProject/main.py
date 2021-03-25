class Node:  # Example  6.1
    def _init_(self, v):
        self.Info = v
        self.Next = None

    def Print(self):
        print(self.Info)
        if (self.Next is not None):
            self.Next.Print()


class LinkedList:

    def _init_(self, value):
        self.Start = Node(value)

    def Print(self):
        if (self.Start == None):
            print('list is empty')
        else:
            self.Start.Print()

    def Insertatbegin(self, value):  # 6.3
        if (self.Start == None):
            self.Start = Node(value)
        else:
            Temp = Node(value)
            Temp.Next = self.Start
            self.Start = Temp

    def Insertatlast(self, value):  # 6.4
        if (self.Start is None):
            self.Start = Node(value)
        else:
            ptr = self.Start
            while (ptr.Next != None):
                ptr = ptr.Next
            ptr.Next = Node(value)  # 6.7

    def Search(self, value):
        if (self.Start is None):
            print("List is  empty")
        else:
            ptr = self.Start
            count = 1
            while (ptr != None and ptr.Info != value):
                ptr = ptr.Next
                count += 1
            if (ptr == None):
                print(f"Value {value} not found")
            else:
                print(f"Value {ptr.Info} Found on position {count}")


objectt = LinkedList(666)
objectt.Start.Next = Node(777)
objectt.Insertatbegin(555)
objectt.Insertatlast(888)
objectt.Print()
objectt.Search(888)
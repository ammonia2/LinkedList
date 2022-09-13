
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None  #first node of the list

    def printlist(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''  #string to output
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data) #no arrow if no node
            itr = itr.next
        print(llstr)

    def inceptive_insert(self, data):
        node = Node(data, self.head)  #creating a node with pointer
        self.head = node

    def end_insert(self, data):
        if self.head == None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:  #finds the last node
            itr = itr.next
        itr.next = Node(data, None)

    def get_length(self):
        Length = 0
        itr = self.head
        while itr:
            Length += 1
            itr = itr.next
        return Length 
    
    def selective_insert(self, data, position):
        if position < 0 or position >= self.get_length():
            raise Exception("Invalid Index")
        if position == 0:
            self.inceptive_insert(data)
            return
        count = 0
        itr = self.head
        while count != position-1:
            itr = itr.next
            count += 1
        node = Node(data, itr.next)  #previous pointer given to new node
        itr.next = node    #new node pointed to previous node

    def selective_deletion(self, position):
        if position < 1 or position > self.get_length():
            raise Exception("Invalid Index")
        elif position == 1:
            self.head = self.head.next
            return
        elif position == self.get_length():
            node = self.head
            count = 1
            while count != self.get_length()-1:
                node = node.next
                count += 1
            node.next = None
            return
        itr = self.head
        count = 1
        while count != position-1:
            itr = itr.next
            count += 1
        itr.next = itr.next.next

    def cumulative_insert(self, data_list):
        for data in data_list:
            self.end_insert(data)

    #swapping pointers pointed to the nodes
    def swapnodes(self, node1, node2):  
        if node1 == node2:  # no swaps needed
            return

        ploc1, ploc2, count = None, None, 1   #ploc : previous location
        lnode1 = self.head # for location of node1
        lnode2 = self.head 

        while True:   # loop to get positions of nodes identified earlier
            if count+1 == node1:  
                ploc1 = lnode1 
                lnode1 = lnode1.next
                if node1 > node2:
                    break
            elif count < node1:  #only move to next node until required
                lnode1 = lnode1.next    
                
            if count+1 == node2:
                ploc2 = lnode2
                lnode2 = lnode2.next
                if node2 > node1:
                    break
            elif count < node2:
                lnode2 = lnode2.next
                
            count += 1
        
        if node1 < node2: 
            if ploc1 != None: #to prevent condition from execution if node position is 1
                ploc1.next = lnode2
            
            ploc2.next = lnode1
        
        if node2 < node1:
            if node2 != 1:
                ploc2.next = lnode1
            ploc1.next = lnode2

        temp = lnode2.next  
        lnode2.next = lnode1.next
        lnode1.next = temp
        
        #assigning shifted node as new head (if a position is 1)
        if ploc1 == None:
            self.head = lnode2
        elif ploc2 == None:
            self.head = lnode1
    
    #finding middle. complexity = n
    def findmiddle(self):
        node = self.head
        node2 = self.head
        count1 = 1
        count2 = 1
        while node:
            if count1 % 2 == 0:    
                node = node.next
                count1 += 1
                node2 = node2.next
                count2 += 1
            else:
                node = node.next
                count1 += 1
        print(node2.data)
        return count2
    
    def reverselist(self):
        prev, node = None, self.head
        
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node=temp
        self.head=prev
    
    #finding middle. complexity = 3n
"""    def find_middle(self):
        if self.get_length() == 0 or self.get_length() == 1:
            return

        middle_node = int(self.get_length()/2) + 1
        node, count = self.head, 1
        while count != middle_node+1:
            if count == middle_node:
                nodedata = node.data
            node = node.next
            count += 1
        print("The middle node stores:" , nodedata)"""

    #swapping only the data in nodes
"""   def swap_nodes(self, node1, node2): 
        n1 = None
        n2 = None
        if node1 == node2:
            return
        count = 0
        itr = self.head
        while itr != None:
            itr = itr.next
            count += 1
            if count == node1 - 1:
                temp2 = itr.data
            if count == node2 - 1:
                temp1 = itr.data
        itr = self.head
        count = 0
        while itr != None:
            itr = itr.next
            count += 1
            if count == node1 - 1:
                itr.data = temp1
            if count == node2 - 1:
                itr.data = temp2    """
        
list1 = LinkedList()
list1.cumulative_insert([9, 9, 5, 7, 8, 9])
list1.printlist()

list2 = LinkedList()
list2.cumulative_insert([8, 9, 4, 3])
list2.printlist()

def list_addition(x, y):  #reverse list logic(same as in file: "addition list.py") # all correct # complexity = 2(n + m) + n = 3n
    x.reverselist()
    y.reverselist()
    curr_sum, returnlist, node1, node2 = 0, LinkedList(), x.head, y.head
    while node1:
        if node2:
            curr_sum += node1.data + node2.data
            returnlist.inceptive_insert(curr_sum%10)
            print(curr_sum)
            curr_sum = curr_sum // 10
            node1 = node1.next
            node2 = node2.next
        else:
            curr_sum += node1.data
            returnlist.inceptive_insert(curr_sum%10)
            print(curr_sum)
            curr_sum = curr_sum//10
            node1 = node1.next
    if curr_sum > 0:
        returnlist.inceptive_insert(curr_sum)
        curr_sum = 0
    returnlist.printlist()

list_addition(list1, list2) #expected: 1004732
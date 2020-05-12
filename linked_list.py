class Node:
    size = 0

    def __init__(self, data):
        self.data = data
        self.next = None
        Node.size += 1


class linked_list:
    def __init__(self):
        self.head = None

    def add(self, data):
        x = Node(data)
        if x.size == 1:
            self.head = x
            return f'{data} is Being Added!'
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = x
            return f'{data} is Being Added!'

    def lprint(self):
    	if self.head!=None:
	        temp = self.head
	        a = []
	        while temp:
	            a.append(temp.data)
	            if temp.next == None:
	                return a
	            temp = temp.next

    def remove(self, data):
    	if self.head!=None:
	        temp = self.head
	        if temp.data == data:
	            self.head = temp.next
	        else:
	            while temp.next:
	                if temp.next.data == data:
	                    temp.next = temp.next.next
	                    return f'{data} is Being Removed!'
	                temp = temp.next

    def search(self, data):
    	if self.head!=None:
	        temp = self.head
	        index = 1
	        if temp.data == data:
	            return f'{data} is Founded At {index} Index!'
	        else:
	            while temp.next:
	                index += 1
	                if temp.next.data == data:
	                    return f'{data} is Founded At {index} Index!'
	                temp = temp.next


llist = linked_list()
ask=None
while ask!='5':
    print('1.Add.2.Remove.3.Search.4.Print.5.Exit.')
    ask = str(input('>>>'))
    if ask == '1':
        a = input('Enter Data:')
        print(llist.add(a))
    elif ask == '2':
        a = input('Enter Data:')
        print(llist.remove(a))
    elif ask == '3':
        a = input('Enter Data:')
        print(llist.search(a))
    elif ask == '4':
        print(llist.lprint())
    elif ask=='5':
    	print('Bye!')
    else:
        print('Invalid Option')

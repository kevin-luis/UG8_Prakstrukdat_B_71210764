class MyCircularQueue():

    def __init__(self, c):
        self.capacity = c
        self.data = [None] * c
        self.head = self.tail = -1

    def enqueue(self, data):
        if ((self.tail + 1) % self.capacity == self.head):
            print("penuh!!\n")

        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.data[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.capacity
            self.data[self.tail] = data

    def dequeue(self):
        if (self.head == -1):
            print("kosong!!\n")

        elif (self.head == self.tail):
            hapus = self.data[self.head]
            self.head = -1
            self.tail = -1
            return hapus
        else:
            hapus = self.data[self.head]
            self.head = (self.head + 1) % self.capacity
            return hapus

    def display(self):
        if self.head == -1:
            print("Tidak ada data!!")

        elif self.tail >= self.head:
            print("Data ada pada antrian adalah: ", end="")
            for i in range(self.head, self.tail + 1):
                print(self.data[i], end=" ")
            print()
        elif len(self.data) == self.capacity:
            print("Data ada pada antrian circular adalah: ", end="")
            for i in range(self.head, self.capacity):
                print(self.data[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.data[i], end=" ")
            print()
            if ((self.tail + 1) % self.capacity == self.head):
                print("Antrian penuh!!")
            else:
                print()
circularQueue = MyCircularQueue(5) 
circularQueue.enqueue (14) 
circularQueue.enqueue (22) 
circularQueue.enqueue (13) 
circularQueue.enqueue (-6) 
circularQueue.display() 
print ("Data yang dihapus adalah = ", circularQueue.dequeue()) 
print ("Data yang dihapus adalah = ", circularQueue.dequeue()) 
circularQueue.display()
circularQueue.enqueue (9) 
circularQueue.enqueue (20) 
circularQueue.enqueue (5)
circularQueue.display()

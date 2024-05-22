class lib:
    def __init__(self,books):
        self.books=books
    def list(self):
        print("Available books")
        for book in self.books:
            print(book)
    def borrow(self,borrow):
        if borrow in self.books:
            print("Get your Books now")
            self.books.remove(borrow)
        else:
            print("No Availble Books")
    def receive(self,receive):
        print("YOu have Returned the books")
        self.books.append(receive)
books=['c','c++','java','python']
o=lib(books)
msg="""
        1.View Books
        2.Borrow Books
        3.REturn Books"""
while True:
    print(msg)
    ch=int(input("Enter ur choice "))
    if(ch==1):
        o.list()
    elif ch==2:
        books=input("Enter book name want to borrow     ")
        o.borrow(books)
    elif ch==3:
        book=input("Enter book to return  ")
        o.receive(book)
    else:
        print("Thanking You Visit Again!")
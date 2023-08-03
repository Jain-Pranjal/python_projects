# student library using the OOPS
class library:

        # construcutor which will automatially show 
    def __init__(self,listofbooks):
        self.books=listofbooks

    # it will display all the books 
    def displayAvailableBooks(self):
        print("the books present in this library are : ")
        for books in self.books:  #loop is inside the list 
            print("\t *",books,"\n")  #print all the books 
    

    def borrowbook(self,bookname):
        if bookname in self.books:
            print(f"u have been issued {bookname}")
            print("please keep it safe and return it on time within 30 days")
            self.books.remove(bookname)
            return True
            # remove the name of the book from the list after being issue
        else:
            print("Book is not available or issued by someone else please wait for sometime")
            return False

        

    def returnBook(self,bookname):
        self.books.append(bookname)
        print("thanks for returning this book . Hope u enjoy rading it ")
        


class Student:

    def requestBook(self):
        self.book=input("enter the name of the book u want to borrow : ")
        return self.book
    

    def returnBook(self):
        self.book=input("enter the name of the book u want to return : ")
        return self.book



# we have provided the list in the argument which will be stored insde the one variable only 
if __name__=="__main__":
    centrallibrary=library(["algo","django","Clrs","python notes"])
    student=Student()

    # centrallibrary.displayAvailableBooks()

    while True:
        welcomemsg='''+++++ WELCOME TO CENTRAL LIBRARY +++++
        please choose the option 
        1.listing all the books 
        2.request a book
        3.add/return a book
        4.exit the library'''
        

        print(welcomemsg)
        a=int(input("\nEnter a choice "))
        if a==1:
            centrallibrary.displayAvailableBooks()
        elif a==2:
            centrallibrary.borrowbook(student.requestBook())
        elif a==3:
            centrallibrary.returnBook(student.returnBook())
        elif a==4:
            print("thanks for choosing central library ")
            exit()
        else:
            print("invalid choice ...")
            print("please enter a valid choice \n")



# for using the backend in the webdev in python use the django 















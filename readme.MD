# Library Management System:
Design a library management system using classes such as Library, Book, and Member.
Implement features like adding books, borrowing and returning books, and tracking member information.
Use inheritance and encapsulation to model relationships between different entities in the system.

There are two files in this project. The main file is libsyst.py and the rough.py is for iterations of the project.
## the library class 
This class has attributes in the __init__ method namely;
* self.bookList = [] which is where all the books are contained
* self._name = name  is the name of the library
* self._address = address is the kibrary address
The library class methods include: 
* addBook method
This is used to add a new book to the lsit of books
through the library class by using the append() function.
it returns a new list of books with the new book added at the end
of the list
* removeBook method
is used to remove a book from the lsit of books
through the library class by using the remove() function.
it returns a new list of books without the book that was removed
* displayShelf method
this method is used to display the list of books in it's current form
## The Book class
This class is used to create specific book instances with the attributes and mthods below
This class has attributes in the __init__ method namely;
self.__pages = pages which details the nuber of pages in each new book instance
self._year = yearPublished detailes the year the book was published
self.bookName = Bookname detailes the name of the book instance 
self.author = author is the name of the author
the methods in this class are mostly getter functions that include;
* getAuthor
this function returns the name of the author (self.author) of a pecific book 
* getYear
returns the year the self._year protected attribute which is the year the book was published
* getNameandAuthor 
returns self.bookName and the author it was written by
* getPages returns the private attribute; number of pages of the bookName
## The Member class
This class is used to create individual member instances, keep track of borrowed and returned books
with the attributes and methods below
This class has attributes in the __init__ method namely;
self.Name = name is the name fo the new registered mamber or the new member instance
self.__ID = memberID is the private attribute that stores the Id of the individual member
self._borrowed = [] is a protected attribute for the list of borrowed books
the methods in this class are mostly getter functions that include;
* getName:
this is a getter function/method that is used to return the name of a specific registered member
* getID: this is a getter function/method used to get the id of this specific membe
* borrow: this method is used to borrow a book by appending this book to the self.borrowd list of books borrowed
by using the append() function
* bookReturn: this method uses the remove() function to remove a book that is in the self._borrowed list, 
returning its status from borrowed to unborrowed and printing a message to that effect
* checkBook: This method uses an if statement to determine if a book is in the self._borrowed list and returns a message granting or denying permission to borrow said book

## ENCAPSULATION
PRIVATE ATTRIBUTES: these are attributes whose access is restricted to only within the class they are initialised in. this means they cannot be acessed in any other classes and attempts to do so will return an error.
self.__pages in the book class 
self.__ID in the member class
PROTECTED ATTRIBUTES : these are attributes whose acecc is restricted to the class they were initialised in and their subclasses only
self._name in the library class
self._address in the library class
self._year in the book class
self._borrowed in the member class
the rest of the attributes are known as public attribtes, acessible from anywhere in the program.
i.e self.bookList

## END
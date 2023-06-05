# Library Management System:
Design a library management system using classes such as Library, Book, and Member.
Implement features like adding books, borrowing and returning books, and tracking member information.
Use inheritance and encapsulation to model relationships between different entities in the system.

## the library class 
has attributes in the __init__ method namely;
self.bookList = [] which is where all the books are contained
self._name = name  is the name of the library
self._address = address is the kibrary address
## addBook method
is used to add a new book to the lsit of books
through the library class by using the append() function.
it returns a new list of books with the new book added at the end
of the list

## removeBook method
is used to remove a book from the lsit of books
through the library class by using the remove() function.
it returns a new list of books without the book that was removed
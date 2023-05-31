'''
Library Management System:
Design a library management system using classes such as Library, Book, and Member.
Implement features like adding books, borrowing and returning books, and tracking member information.
Use inheritance and encapsulation to model relationships between different entities in the system.
'''

from abc import ABC #IMPORT THE ABC FROM abc module
from abc import abstractmethod #identifier/decorator


class Library:
    '''
    the library class is also the parent class, this means that all other classes
    will inherit at least one method from thr parent class
    '''
    def __init__(self,libName, libAddress):
        '''
        this function describes all the attributes of the library
        '''
        self.name = libName
        self.address = libAddress
        self.books = ['the alchemist', '12 rules for life', '12 more rules for life', 'history']

    @abstractmethod
    def addBook(self, book):
        '''
        addBook method is used to add a new book to the lsit of books
        through the library class by using the append() function.
        it returns a new list of books with the new book added at the end
        of the list
        '''
        self.books.append(book)

        return self.books
    

    def removeBook(self, book):
        '''
        removeBook method is used to remove a book from the lsit of books
        through the library class by using the remove() function.
        it returns a new list of books without the book that was removed
        '''
        self.books.remove(book)

        return self.books
    
    
    def bookStatus(self, book):
        '''
        bookStatus method is used to check the availability of a book the lsit of books
        through the library class by using a simple if statement.
        it returns a statement telling you if the book is in the library or not
        '''
        if book in self.books:
            return f'{book} is in the library' 
        else:
            return f'{book} is not in the lirary at this moment'
        
        
#new library class instances
new = Library('Peterson\'s library', 'Uyo, Akwaibom state')
print(new.name)
print(new.addBook('brave new world'))
print(new.bookStatus( '12 rules for life'))

#class Book(Library):

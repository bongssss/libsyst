'''
Library Management System:
Design a library management system using classes such as Library, Book, and Member.
Implement features like adding books, borrowing and returning books, and tracking member information.
Use inheritance and encapsulation to model relationships between different entities in the system.
'''

from abc import ABC #IMPORT THE ABC FROM abc module
from abc import abstractmethod #identifier/decorator


class Library():
    '''
    the library class is also the parent class, this means that all other classes
    will inherit at least one method from thr parent class
    '''
    _books =  ['The alchemist', '12 Rules for life', '12 more Rules for life',
                        'love me again', 'Brave new world']
    def __init__(self,libName, libAddress):
        '''
        this function describes all the attributes of the library
        '''
        self._name = libName
        self.address = libAddress
        self._books = ['The alchemist', '12 Rules for life', '12 more Rules for life',
                        'love me again', 'Brave new world']
    
    def getBookList(self):
       return self._books
        

    def getAddress(self):
       print(f'{self._name} is located in {self.address}')

    def getBooks(self, book):
        for book in self._books:
           print(book)
           f'The current list of books is {self._books}'   
    
    @abstractmethod
    def addBook(self,  book):
        pass
    
    @abstractmethod
    def removeBook(self, book):
        pass
    
    
    def bookStatus(self, book):
        pass
        
        

class Book(Library):
    
    def __init__(self,bookName ):
        self.bName = bookName
        self.authors = []
       # self.bAuthor = author
       # self._books 

    def getBookList(self):
       return super().getBookList()
        
    def addBook(self,  book):
        '''
        addBook method is used to add a new book to the lsit of books
        through the library class by using the append() function.
        it returns a new list of books with the new book added at the end
        of the list
        '''
        self._books.append(book)

        return self._books
    

    def removeBook(self, book):
        '''
        removeBook method is used to remove a book from the lsit of books
        through the library class by using the remove() function.
        it returns a new list of books without the book that was removed
        '''
        self._books.remove(book)

        return self._books
    
    
    def bookStatus(self, book):
        '''
        bookStatus method is used to check the availability of a book the lsit of books
        through the library class by using a simple if statement.
        it returns a statement telling you if the book is in the library or not
        '''
        
        if book in self._books:
          return print(f'{book} is in the library') 
        else:
          return print(f'{book} is not in the lirary at this moment')
        
    
        
    def addAuthor(self, book,  author):
       
       if book in self._books:
          self.authors.append(author)
          return print(f'The author {author} of {book} has been added sucessfully')
       else:
          return print(f' We cannot add the author because {book} is not in our library, try another book')
       
    def checkAuthor(self, book, author):
       if author in self.authors and book in self._books:
          return print(f'The author of {book} is {author}')
        
          
   
   
print('library class instances')
print('--------------------------')
new = Library('Peterson\'s library', 'Ontario, Canada')

print(f'Welcome to {new._name} library') #is a  way to get the name of the library since its is a protected 
#member of the class library
print('---------------------------------')
new.getAddress() #is the only way to acess the library address since it is a private
#member of the  library class
print('---------------------------------')
print(new.bookStatus('12 Rules for life'))
print('---------------------------------------------')

print('book instances')
print('----------------------------')
newbook = Book('12 Rules for life')
print(newbook.getBookList())
print('---------------------------------')
print(newbook.addBook('Newman\'s Journey'))
print('---------------------------------')
#print(newbook.addAuthor('12 Rules for life', 'Jordan peterson'))


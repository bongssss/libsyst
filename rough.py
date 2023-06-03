class Library():
    def __init__(self, name, address):
        self.bookList = []
        self._name = name
        self._address = address
        
    
    def getBookList(self):
           return self.bookList
    
    def addBook(self, book):
        if book not in self.bookList:
           self.bookList.append(book)
           return f'{book.bookName} sucessfully added to {self._name} Library '
        elif book in self.bookList:
            return f'cannot add because {book.bookName} record already exists'
    
    def removeBook(self, book):
        if book in self.bookList:
            self.bookList.remove(book)
            return f'{book} removed sucesfully from {self._name} library'
        else:
            return f'cannot remove as record of {book} is not found in {self._name} library'
        
    
    def displayShelf(self, book):
        for book in self.bookList:
            return print(book)
        


    
class Book():
    def __init__(self, Bookname, author, pages, yearPublished):
        self.__pages = pages
        self._year = yearPublished
        self.bookName = Bookname
        self.author = author

    def getAuthor(self):
        return self.author
    
    def  getNameandAuthor(self):
        return f'{self.bookName} was written by {self.author}.'
    
    def getYear(self):
        return f'{self.bookName} was published in {self._year}.'
    
    def getPages(self):
        return f'{self.bookName} has {self.__pages} pages.'
    




class Member():
    def __init__(self, name, memberID):
        self.Name = name
        self.__ID = memberID
        self._borrowed = []

  
    def getName(self):
        return f'{self.__ID}\'s name is {self.Name}.'

    def getId(self):
        return f'The member ID of {self.Name} is {self.__ID}.'

    def borrow(self, book):
        
            self._borrowed.append(book)
            return print(f'{self.Name} has borrowed {book.bookName} sucessfully!')
       

    def bookReturn(self, book):
        if book in self._borrowed:
            self._borrowed.remove(book)
            return print(f'{book.bookName} has been returned by {self.Name} sucessfully, borrow again sometime!')
        
        elif book not in self._borrowed :
            return print(f'{self.Name}, {book.bookName} has already been returned, thanks!')

    def checkBook(self, book):
        if  book in self._borrowed:
            return print(f'we\'re sorry {self.Name}, {book.bookName} is not available right now :(')
        elif  book not in self._borrowed:
            return print(f'''congratulations {self.Name}! {book.bookName} is available, you can go ahead and borrow it :)''')
        

print('------------------------instances--------------------------------------')
library = Library('Peterson\'s Library', 'Toronto, Canada')
print(f'welcome to {library._name}\'s library in {library._address}')


print('--------------------------------------------------------------')


rules_12 = Book('12 rules', 'Jordan Peterson', 448, 2018)
more_12_rules = Book('12 more rules', 'Jordan Peterson', 432, 2021)
maps_of_meaning = Book('Maps of meaning', 'Jordan Peterson', 564,1999)
order_in_chaos = Book('Order from Chaos', 'Jordan peterson', 450, 2012)
Orwellian = Book('1984', 'George Orwell', 280, 1949)
Brave_new_world = Book('Brave new world', 'Aldous, Huxley', 500, 1932)


print(rules_12.getNameandAuthor())
print('--------------------------------------------------------------')
print(Orwellian.getYear())
print('--------------------------------------------------------------')
print(maps_of_meaning.getPages())
print('--------------------------------------------------------------')

print(library.addBook(rules_12))
print(library.addBook(more_12_rules))
print(library.addBook(maps_of_meaning))
print(library.addBook(order_in_chaos))
print(library.addBook(Orwellian))
print(library.addBook(Brave_new_world))
#print('-------------------------------------------------------------------------')
#print(library.getBookList()) #problematic

print('-------------------------------------------------------------------------')
Ubong = Member('Ubongabasi', 1)
Itoro = Member('Itorobong', 2)

print(Ubong.getName())
print('------------------------------------------------------------------------')
print(Itoro.getId())

print('------------------------------------------------------------------------')
Ubong.checkBook(rules_12)
Ubong.borrow(rules_12)
Ubong.bookReturn(rules_12)
print('-------------------------------------------------------------------------')
Itoro.checkBook(Orwellian)
Itoro.checkBook(maps_of_meaning)
Itoro.checkBook(more_12_rules)
Itoro.checkBook(order_in_chaos)
Itoro.checkBook(Brave_new_world)
Itoro.borrow(Orwellian)
print('-------------------------------------------------------------------------')

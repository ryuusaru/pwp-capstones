class User:
    def __init__(self, user, email):
      self.user = user
      self.email = email
      self.books = {}

    def get_email(self):
      return self.email
    def change_email(self, new_email):
      self.email = new_email
      print("User email has been updated")

    def __repr__(self):
      return f"User: {self.name}, email: {self.email}, books read: {self.books}"

    def __eq__(self, other_user):
      if isinstance(other_user, User) and other_user.user == self.user and other_user.email == self.email:
        return True
      else:
        return False
    
    def read_book(self, book, value=None):
      self.books[book] = value
      if isinstance(value, int):
        book.add_rating(value)
    def get_average_rating(self):
      total = 0
      members = 0
      for value in self.books.values():
        if isinstance(value, int):
          total += value
          members += 1
      if members == 0:
        return 0
      else:
        return total/members

class Book:
    def __init__(self, title, isbn):
      self.title = title
      self.isbn = isbn
      self.ratings = []
    
    def get_title(self):
      return self.title
    def get_isbn(self):
      return self.isbn
    def set_isbn(self, new_isbn):
      self.isbn = new_isbn
      print(f"Set ISBN to {new_isbn}")
    def add_rating(self):
      
      if rating >= 0 and rating <= 4:
        self.ratings.append(rating)
      else:
        print("Invalid Rating")
    
    def __eq__(self, other_book):
      if isinstance(other_book, Book) and other_book.book == self.title and other_book.isbn = self.isbn:
        return True
      else:
        return False
    
    def get_average_rating(self):
      total = 0
      members = 0
      for value in self.rating.values():
        if isinstance(value, int):
          total += value
          members += 1
      if members == 0:
        return 0
      else:
        return total/members
    
    def __hash__(self):
      return hash((self.title, self.isbn)


class Fiction(Book):
    def __init__(self, title, author, isbn):
      Book.__init__(self, title, isbn)
      self.author = author
    def get_author(self):
      return self.author
    def __repr__(self):
      return f"{title} by {author}"

class NonFiction(Book):
    def __init__(self, title, subject, level, isbn):
      Book.__init__(self, title, isbn)
      self.subject = subject
      self.level = level
    def get_subject(self):
      return self.subject
    def get_level(self):
      return self.level
    def __repr__(self)
      print(f"{title}, a {level} manual on {subject}")


class TomeRater:
    def __init__(self):
      self.user = {}
      self.books = {}
    def create_book(self, title, isbn):
      new_book = Book(title, isbn)
      return new_book
    
    def create_novel(self, title, author, isbn):
      new_novel = Fiction(title, author, isbn)
      return new_novel
    def create_non_fiction(self, subject, level, isbn):
      new_non_fict = NonFiction(subject, level, isbn)
      return new_non_fict    
    def add_book_to_user(self, book, email, rating=None):
      user = self.users.get(email)
      if not user:
        print(f"No user with email {email}!")
        return
      user.read_book(book, rating)
      boot.add_rating(rating)

      if book not in self.books:
        self.books[book] = 1
      else:
        self.books[book] += 1
    def add_user(self, email, user_books=None):
      new_user = User(name, email)
      self.users[email] = new_user
      if isinstance(user_books, list):
        for book in user_books:
          self.add_book_to_user(new_user, book)
    def print_catalog(self):
      for book in self.books:
        print(book)

    def print_users(self):
      for user in self.users:
        print(user)
    def most_read_book(self):
      max = 0
      the_most_read_book = None
      for book, times_read in self.books.items():
        if times_read > max:
          max = times_read
          the_most_read_book = book
      return the_most_read_book
    def highest_rated_book(self):
      max = 0
      the_highest_rated_book = None
  
      for book in self.books:
        rating = book.get_average_rating()
        if rating > max:
          max = rating
          the_highest_rated_book = book
      return the_highest_rated_book
    def most_positive_user(self):
      max = 0
      the_most_positive_user = None
  
      for user in self.users:
        user = user.get_average_rating()
        if user > max:
          max = user
          the_most_positive_user = users
      return the_most_positive_user
    def __repr__(self):
      return f"{self.highest_rated_book()} is the highest rated book, and {self.most_read_book()} is the most popular book}"
    def __eq__(self, other_tome_rater):
      return (self.users == other_tome_rater.users and self.books == other_tome_rater.books)
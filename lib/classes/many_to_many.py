class Article:
    # Class variable to store all instances of Article
    all = []
    def __init__(self, author, magazine, title):
        # Initialize an article with an author, a magazine, and a title
        self.author = author
        self.magazine = magazine
        # Ensure title is always a string
        self._title = str(title)
        # Add the article instance to the class variable 'all'
        Article.all.append(self)

    @property
    def title(self):
         # Getter method for title
        return self._title

    @title.setter
    def title(self, new_title):
        # Setter method for title, not implemented correctly (should assign to self._title)
        return self._title
        

class Author:
    def __init__(self, name):
        # Initialize an author with a name and an empty list of articles
        self._name = name
        self._articles = []
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self.new_name = new_name
        return self._name

    def articles(self):
        # Return a list of articles written by this author
        return [article for article in Article.all if article.author == self]

    def magazines(self):
         # Return a list of unique magazines contributed to by this author
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
         # Create and return a new article associated with this author
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def topic_areas(self):
        # Return a list of unique categories of magazines the author has contributed to
        return list(set([article.magazine.category for article in self._articles])) if self._articles else None

    def contributing_authors(self):
         # Return a list of authors who have contributed at least one article
        return [author for author in Author.all if len(author.articles()) > 0]

class Magazine:
    def __init__(self, name, category):
        # Initialize a magazine with a name, a category, and an empty list of articles
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        # Getter method for name
        return self._name

    @name.setter
    def name(self, new_name):
        # Setter method for name
        if isinstance(new_name, str):
            if 2 <= len(new_name) <= 16:
               self._name = new_name
        return self._name

    @property
    def category(self):
         # Getter method for category
        return self._category

    @category.setter
    def category(self, new_category):
         # Setter method for category
        if isinstance(new_category, str):
           if len(new_category) > 0:
               self._category = new_category
        return self._name

    def add_article(self, article):
          # Add an article to the magazine's list of articles
        self._articles.append(article)

    def articles(self):
        # Return a list of articles published in this magazine
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        # Return a list of authors who have contributed to this magazine
        return list(set([article.author for article in self.articles()]))

    def article_titles(self):
         # Return a list of titles of articles published in this magazine
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        # Return a list of authors who have contributed more than 2 articles to this magazine
        authors = {}
        for article in self.articles():
            if article.author in authors:
                authors[article.author] += 1
            else:
                authors[article.author] = 1
        contributing_authors = [author for author, count in authors.items() if count > 2]
        return contributing_authors if contributing_authors else None

    @classmethod
    def top_publisher(cls):
        # Class method to find the magazine with the most articles
        if not cls.all:
            return None
        return max(cls.all, key=lambda magazine: len(magazine.articles))
from datetime import date
from PIL import Image


class Content(object):
    # list to keep track of all pieces of content
    existing_content = []

    def __init__(self, year, month, day, contributors):
        # log each piece of content as existing upon creation
        self.existing_content.append(self)

        # stores the year, month, and day
        self.creation_date = date(year, month, day)

        # list of contributors
        self.contributors = contributors

    # this defines a show method that has nothing in it, to be overridden later
    def show(self):
        print "This piece of content was created on {1}/{0}/{2} by {3}\n\n".format(self.creation_date.day,\
        	self.creation_date.month,self.creation_date.year,self.contributors)


# TODO: Define an Article class that extends the Content class
class Article(Content):
    existing_articles = []

    def __init__(self, year, month, day,headline, content,contributors):

        super(Article, self).__init__(year,month,day,contributors[0])
        self.headline = headline
        self.content = content
        self.existing_articles.append(self)

    def show(self):
        super(Article, self).show()
        print "Headline:\n{}\n\nContent:\n\n{}".format(self.headline,self.content)

        

# TODO: Define a Picture class that extends the Content class
class Picture(Content):

    def __init__(self, year, month, day, title,caption,path,contributors):

        super(Picture, self).__init__(year,month,day,contributors)
        self.title = title
        self.caption = caption
        self.path = path

    def show(self):
        super(Picture, self).show()
        print "This image's title is:\n{}\nCaption:\n{}".format(self.title,self.caption)
        Image.open(self.path).show()


        

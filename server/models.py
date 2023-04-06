from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.Integer)

    @validates('name')
    def validate_name(self, key, name):
        names = db.session.query(Author.name).all()
        if len(name) == 0:
            raise ValueError("Please enter your name.")
        elif name in names:
            raise ValueError("Name must be unique.")
        return name


    @validates('phone_number')
    def validate_pn(self, key, number):
        if not len(number) == 10:
            raise ValueError("Number must be 10 digits.")
        return number

    def __repr__(self):
        return f'<Author {self.name}>'

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String)
    content = db.Column(db.String)
    summary = db.Column(db.String)
    category = db.Column(db.String)
        
        
    @validates('title')
    def validate_title(self, key, title):
        clickbait = ["Won't Belive", "Secret", "Top", "Guess"]
        found_word = []
        # if not title:
        #     raise ValueError("Title field is required.")
 
        for word in clickbait:
            if word in title:
                found_word.append(word)
        if len(found_word) == 0:
            raise ValueError("Title must include clickbait words.")
        
        return title

        # elif not any(bait in title for bait in clickbait):
        #     raise ValueError('Post has no clickbait')
    
    @validates('content')
    def validate_content(self, key, content):
        if len(content) <= 250:
            raise ValueError("Content needs to be at lease 250 characters long.")
        return content
    
    @validates('summary')
    def validate_post(self, key, summary):
        if len(summary) >= 250:
            raise ValueError("Summary needs to be less than 250 characters long.")
        return summary
    
    @validates('category')
    def validate_category(self, key, category):
        categories = ['Fiction', 'Non-Fiction']
        if category not in categories:
            raise ValueError("Category must be either Fiction or Non-Fiction.")
        return category

    def __repr__(self):
        return f'<Post Title: {self.title}>'

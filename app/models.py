# functions that you wish to incorporate in the route files
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Projects(db.Model):
    """
    display_picture_url should be 350x200
    title_img_url anything goes for dimensions
    more_img_urls should be 350x200
    description should be short
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    display_picture_url = db.Column(db.String, nullable=False)
    title_img_url = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    text1 = db.Column(db.String)
    text2 = db.Column(db.String)
    more_imgs_urls = db.Column(db.String)
    technologies = db.Column(db.String, nullable=False)
    github_link = db.Column(db.String)
    website_link = db.Column(db.String)

    def __init__(self, title, display_picture_url, title_img_url, description, text1, text2, more_imgs_urls, technologies, github_link, website_link):
        self.title = title
        self.display_picture_url = display_picture_url
        self.title_img_url = title_img_url
        self.description = description
        self.text1 = text1
        self.text2 = text2
        self.more_imgs_urls = more_imgs_urls
        self.technologies = technologies
        self.github_link = github_link
        self.website_link = website_link

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def update_more_imgs(self, new_image_set):
        self.more_imgs_urls = new_image_set
        db.session.commit()

    def to_dict(self):
        d = {}
        d["title"] = self.title
        d["dp"] = self.display_picture_url
        d["title_img"] = self.title_img_url
        d["desc"] = self.description
        d["text1"] = self.text1 
        d["text2"] = self.text2 
        d["more_imgs"] = self.more_imgs_urls 
        d["techs"] = self.technologies
        d["github"] = self.github_link
        d["website"] = self.website_link
        return d


class MiniApps(db.Model):
    """
    display_picture_url should be 350x200
    title_img_url anything goes for dimensions
    more_img_urls should be 350x200
    description should be short
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    display_picture_url = db.Column(db.String, nullable=False)
    title_img_url = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    text = db.Column(db.String)
    more_imgs_urls = db.Column(db.String)
    technologies = db.Column(db.String, nullable=False)
    github_link = db.Column(db.String)
    website_link = db.Column(db.String)

    def __init__(self, title, display_picture_url, title_img_url, description, text, more_imgs_urls, technologies, github_link, website_link):
        self.title = title
        self.display_picture_url = display_picture_url
        self.title_img_url = title_img_url
        self.description = description
        self.text = text
        self.more_imgs_urls = more_imgs_urls
        self.technologies = technologies
        self.github_link = github_link
        self.website_link = website_link

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def update_more_imgs(self, new_image_set):
        self.more_imgs_urls = new_image_set
        db.session.commit()

    def to_dict(self):
        d = {}
        d["title"] = self.title
        d["dp"] = self.display_picture_url
        d["title_img"] = self.title_img_url
        d["desc"] = self.description
        d["text"] = self.text
        d["more_imgs"] = self.more_imgs_urls 
        d["techs"] = self.technologies
        d["github"] = self.github_link
        d["website"] = self.website_link
        return d


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    suggestion = db.Column(db.String, nullable=False)
    extra_feedback = db.Column(db.String)

    def __init__(self, suggestion, extra_feedback):
        self.suggestion = suggestion
        self.extra_feedback = extra_feedback

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
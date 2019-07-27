import webapp2
import jinja2
import os
import datetime

from models import BlogPost

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class ProfileHandler(webapp2.RequestHandler):
    def get(self):
        start_template = jinja_env.get_template("templates/index.html")
        self.response.write(start_template.render())

class newPostHandler(webapp2.RequestHandler):
    def get(self):
        start_template = jinja_env.get_template("templates/new_post.html")
        self.response.write(start_template.render())

class printedPostHandler(webapp2.RequestHandler):
    def post(self):
        dateTime_var = datetime.datetime.now()
        title_var = self.request.get("title")
        author_var = self.request.get("author")
        content_var = self.request.get("content")

        blog_post = BlogPost(name=author_var, title=title_var, content=content_var, time_date=dateTime_var)
        blog_post.put()
        all_posts = BlogPost.query().fetch()
        all_posts.insert(0, blog_post)

        template_vars = {
            "blogPosts": all_posts,
        }

        template = jinja_env.get_template("templates/posts_printed.html")
        self.response.write(template.render(template_vars))

app = webapp2.WSGIApplication([
    ('/', ProfileHandler),
    ('/new_post', newPostHandler),
    ('/posts_printed', printedPostHandler)
], debug=True)

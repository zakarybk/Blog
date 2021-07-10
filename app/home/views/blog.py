from flask import Blueprint, render_template

home = Blueprint(
    'home', 
    __name__,
    template_folder="../templates",
    static_folder="../../static"
)

class Post():
    def __init__(self, title, excerpt):
        self.title = title
        self.excerpt = excerpt

@home.route('/blog')
def blog():
    return render_template('blog.html', excerpts=[Post('one', 'first')])
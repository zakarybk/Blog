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

post1 = Post(
    'Making of a new blog', 
    (
        'Previously I have been using WordPress which has been working out '
        'fine so far but it never really felt like my own. So I\'ve decided '
        'to create a new Blog using Flask, HTMX, Bootstrap and Tabler!'
    )
)

post2 = Post('Some other post', 'Not much to say here')

@home.route('/blog')
def blog():
    return render_template('blog.html', excerpts=[post1 for p in range(50)])
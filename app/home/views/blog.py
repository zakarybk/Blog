from flask import Blueprint, render_template

home = Blueprint(
    'home', 
    __name__,
    template_folder="../templates",
    static_folder="../../static"
)

@home.route('/blog')
def blog():
    return render_template('blog.html', excerpts=['one', 'two', 'three'])
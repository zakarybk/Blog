from . import app
from flask import render_template


@app.route('/')
def home1():
    return render_template('./home/templates/layout.html')

@app.route('/news')
def news():
    return render_template('home/templates/layout.html')
@app.route('/about')
def about():
    return render_template('home/templates/layout.html')
@app.route('/contact')
def contact():
    return render_template('home/templates/layout.html')
@app.route('/home')
def home():
    return render_template('home/templates/layout.html')

@app.route('/htmx')
def htmx():
    return render_template('home/templates/test_htmx.html')

@app.route('/demo')
def demo():
    print('hi')
    row = '''
        <tr>
            <td>Agent Smith</td>
            <td>void29@null.org</td>
            <td>55F49448C0</td>
        </tr>
    '''
    rows = [row for i in range(20)]

    return '\n'.join(rows) + '''
        <tr hx-get="/demo?page=1"
            hx-trigger="revealed"
            hx-swap="afterend"
        >
            <td>Agent Smith</td>
            <td>void29@null.org</td>
            <td>55F49448C0</td>
        </tr>
    '''


    

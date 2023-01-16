from flask import render_template
from app import app

@app.route('/')
@app.route('/inventory')
def get_inventory():
    return "Hello, World!"


@app.route('/index')
def get_index():
    user = {'username': 'Rease'}
    posts = [
        {
            "author": {'username':'Rease'},
            "body": 'dog witha blog'
        },
        {   
            "author": {'username':'kilgore'},
            "body": 'kilgores feelings'
        
        }
    ]
    return render_template('index.html',user=user, posts=posts)

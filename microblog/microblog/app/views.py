from __init__ import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname','serena'} #fake user or mock user
    posts = [
        {
            'author':{'nickname':'John'},
            'body':'To be a better man!'
        },
        {
            'author':{'nickname':'Susan'},
            'body':'The movie is cool!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)

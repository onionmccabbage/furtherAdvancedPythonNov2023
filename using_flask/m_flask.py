# may need to pip install Flask
# Flask is a microservice that implements a simple web server
# if you need a public facing web then use Flask with Apache etc.
# ... or use Django
# Flask is a lightweight service - it leaves security to others

from flask import Flask

# to make a flask web server...
app = Flask(__name__) # this is conventional
# we declare routes for our app
@app.route('/')
def root():
    return 'Hello and welcome to Flask'
@app.route('/snowmap')
def map():
    return '<h2>Here is a map of Paris in very deep snow</h2>'
# it may be useful to offer more than one route to content
# e.g. alternative spelling, different product names/ids
@app.route('/info')
@app.route('/about')
def about():
    return 'this is info about stuff'
# we can pass parameters (a RESTful request)
@app.route('/greet')
@app.route('/greet/<person>') # the <> indicate a URL positional argument
# mini challenge
def greet(person=None):
    if person:
        return f'<h3>Greetings {person}'
    else:
        person = 'Default'
        return f'<h3>Greetings {person}'

if __name__ == '__main__':
    # debug=True lets us live reload when the code changes
    app.run(host='127.0.0.1', debug=True) # debug during development
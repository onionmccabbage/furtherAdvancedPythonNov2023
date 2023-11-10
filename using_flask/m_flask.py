# may need to pip install Flask
# Flask is a microservice that implements a simple web server
# if you need a public facing web then use Flask with Apache etc.
# ... or use Django
# Flask is a lightweight service - it leaves security to others

from flask import Flask
# this will use the templates folder
from flask import render_template

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
# mini challenge: add a surname RESTful route
@app.route('/greet/<person>/<surname>')
def greet(person=None, surname=None):
    if person:
        if surname:
            return f'<h3>Greetings {person} {surname}</h3>'
        else:
            return f'<h3>Greetings {person}</h3>'
    else:
        person = 'Default'
        return f'<h3>Greetings {person}</h3>'
# a route for a 'menu' of links
@app.route('/menu')
def menu():
    link1 = '<a href="/">Home</a>'
    link2 = '<a href="/about">About</a>'
    link3 = '<a href="/greet">Greet</a>'
    link4 = '<a href="/snowmap">Map</a>'
    return f'{link1} | {link2} | {link3} | {link4}'
@app.route('/lunch')
@app.route('/lunch/<dessert>') # REST
# a route using template syntax
def lunch(dessert=None):
    # all Flask templates exist in a 'templates' folder
    # we can write Flask micro-syntax within HTML templates
    # if required we can pass arguments into the template
    return render_template('lunch.html', dessert=dessert)

# Flask can handle get and post requests
# remember post does NOT represent the state
# instead post passes a data packet


if __name__ == '__main__':
    # debug=True lets us live reload when the code changes
    app.run(host='127.0.0.1', debug=True) # debug during development
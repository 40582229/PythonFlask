from flask import Flask, redirect, request, url_for
from requests import get
from random import randrange
app = Flask(__name__)

@app.route("/")
def  home():
    #response = #get('http://127.0.0.1:5000/users').content #api repsone from other flask program
    return 'response' #commented out for now

@app.route("/chalange2")
def htmlDiv():
    htmlElements = ['<h1>HELLO</hv>','<h1>THIS IS RANDOM</hv>', '<h1>TROLOLOLOLOLO</hv>']
    return htmlElements[randrange(0,3)]

@app.route("/test")
def test():
    return "This is test"

@app.errorhandler(404)
def page_not_found(error):
    return "Couldnt find the page requested.", 404

@app.route('/private')
def private():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return "WE ARE GETTING YOUR USERNAME AND PASSWORD"

@app.route('/static-example/img')
def static_example_img():
    cssUrl = url_for('static', filename='static.css')
    cssLink = f'<link rel="stylesheet"  href="{cssUrl}">'
    start = '<img id="image" src="'
    url = url_for('static', filename='vmask.jpg')
    end = '">'
    return cssLink+start+url+end, 200

@app.route('/requests')
def httpRequests():
    print(request.method , request.path , request.form )
    return request.method, request.path, request.form 

@app.route('/account', methods=['GET', 'POST'])
def account():
    if request.method == 'POST':
        print(request.form)
        name = request.form['name']
        return "Hello %s" % name
    else:
        page = '''
                <html>
                    <body>
                        <form action="" method="post" name="form">
                            <label for="name">name</label>
                            <input type="text" name="name" id="name" />
                            <input type="submit" name="submit" id="submit" />
                        </form>
                    </body>
                </html>
            '''
        return page

@app.route('/hello/')
def hello():
    name = request.args.get('name', '')
    if name == "":
        return "No Param supplied"
    
    return "Hello %s" % name

@app.route('/add/<int:first>/<int:second>')
def add(first, second):
    return str(first+second)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
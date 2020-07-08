from app import app
from flask import render_template, request


@app.route('/')
def hello_dev():
    return render_template('hello.html')

@app.route('/search/', methods=['POST', 'GET'])
def search():
    # result = request.args['search']  ## method GET
    result = ''
    if request.method == 'POST':
        result = request.form['search']
    return render_template('search.html', search=result)

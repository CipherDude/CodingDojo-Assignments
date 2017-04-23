from flask import Flask, render_template, redirect, request
app=Flask (__name__)

name=''
location=''
language=''
comment=''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def data():
    mydata = request.form
    print mydata
    name = request.form['name']
    print name
    location = request.form['location']
    print location
    language = request.form['language']
    print language
    comment = request.form['comment']
    print comment
    return redirect('/output')

@app.route('/output')
def output():
    return render_template('output.html', name=name, location=location, language=language, comment=comment)





app.run(debug=True)

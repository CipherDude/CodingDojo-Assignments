from flask import Flask, render_template,request,redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def create_data():
    print "Recieved survey data"
    data = request.form
    print data
    print request.form['name']
    print request.form['location']
    print request.form['language']
    print request.form['comments']
    name = request.form['name']
    location = request.form['location']
    fave_lang = request.form['fave_lang']
    comment = request.form['comment']
    print name, location, fave_lang, comment
    return redirect('/output')

@app.route('/output', methods=['POST'])
def output():
    return render_template('output.html', location = location, language=language, fave_lang=fave_lang, comment=comment)
app.run(debug=True)

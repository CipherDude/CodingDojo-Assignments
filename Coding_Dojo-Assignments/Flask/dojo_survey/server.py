from flask import Flask, render_template, redirect, request
app=Flask (__name__)

dictForm = {
'name':'',
'location':'',
'language':'',
'comment':''
}


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def data():
    dictForm['name'] = request.form['name']
    dictForm['location'] = request.form['location']
    dictForm['language'] = request.form['language']
    dictForm['comment'] = request.form['comment']
    return redirect('/results')

@app.route('/results', methods=['GET'])
def results():
    return render_template('results.html', name=dictForm['name'], location=dictForm['location'], language=dictForm['language'], comment=dictForm['comment'])





app.run(debug=True)

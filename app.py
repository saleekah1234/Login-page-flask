from flask import Flask, url_for ,request, render_template
app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('signin.html')

@app.route('/signup',methods=['POST'])
def profile():
    dict={'name':request.form['name'],'college':request.form['college']}
    return render_template('profile.html',dict=dict)

@app.route('/login',methods=['POST'])
def login():
    dict={'name':request.form['nm']}
    return render_template('index.html',dict=dict)
     

#to goto registartion page
@app.route('/signup')
def signup():
    return render_template('signup.html')
     




             

if __name__== "__main__" :
    app.run(debug=True)

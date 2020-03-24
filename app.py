from flask import Flask, url_for ,request, render_template
app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('signin.html')

@app.route('/signup',methods=['POST'])
def profile():
    user=request.form['name']
    det1=request.form['college']
    det2=request.form['branch']
    return render_template('profile.html')

@app.route('/login',methods=['POST'])
def login():
    user=request.form['nm']
    opstring='hey',+ user +'welcome to lfh'
    return opstring
     

#to goto registartion page
@app.route('/signup')
def signup():
    return render_template('signup.html')
     




             

if __name__== "__main__" :
    app.run(debug=True)

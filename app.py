from flask import Flask,url_for,request,render_template
app=Flask(__name__)

@app.route('/',methods=['GET'])
def hello():
    return render_template("index.html")
@app.route('/login')
def login():
    if request.method=='POST':
        user=request.form['nm']
        opstring='hey'+ user + 'welcome to Learn fro home' 
        return opstring          

if __name__=="__main__":
    app.run(debug=True)

from flask import Flask,render_template,request,redirect
app= Flask(__name__)

@app.route('/')
def home():
    return render_template('info.html')

@app.route('/certificate', methods=["GET", "POST"])
def certificate():
    if request.method=="POST":
     name= request.form.get("username")
    return render_template('index.html',name=name)

if __name__ == ("__main__"):
    app.run(debug=True)
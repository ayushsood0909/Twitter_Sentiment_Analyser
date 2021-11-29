# importing Flask and other modules
from flask import Flask, request, render_template ,redirect,session
from test import *

 

  
# Flask constructor
app = Flask(__name__)   

@app.route('/')
def login():
    return render_template('login.html')  
# A decorator used to tell the application
# which URL is associated function
@app.route('/home', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       first_name = request.form.get("fname")
       tweets=request.form.get("tweets")
       display_results(first_name,tweets)
        
    return render_template("projectgui.html")

@app.route('/login_validation', methods=['POST'])
def login_validation():
    
         return render_template("homepage.html")

@app.route('/analyse', methods=['POST'])
def analyse():
    return redirect('/home')

 
    



  
if __name__=='__main__':
   app.run(debug=True)
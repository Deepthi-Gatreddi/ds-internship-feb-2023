#  importing flask
from flask import Flask,request,render_template
import re

# creating a object with parameter name 
app=Flask(__name__)
 

 ##############################################
@app.route('/',methods=['GET','POST'])
def home_page():
   if request.method== 'GET':
      return render_template('searchstring.html')
   else:
      string=request.form.get('string')
      regex=request.form.get('regex')
      matchedstrings=re.findall(regex,string)
      strings=""
      for ele in matchedstrings:
         strings=strings+ele+"  "
      length=len(matchedstrings)
      return str("matched strings are : "+strings+ "<br>" + " Number of Matches : " +(str(length)))
      


 ##############################################

#  running the app 
if __name__ == "__main__":
    app.run()
#  importing flask
from flask import Flask,request,render_template

# creating a object with parameter name 
app=Flask(__name__)
 

 ##############################################
@app.route('/')
def home_page():
   return "Welcome to Deepthi's evil world...."

@app.route('/search')
def search_page():
    return render_template('home.html')

@app.route('/details', methods=['GET','POST'])
def details_page():
    if request.method == 'GET':
        return render_template('givedetails.html')
    else:
        name=request.form.get('name')
        age=request.form.get('age')
        return str("your Name is : "+name+"\n Your age is : "+age)
@app.route('/add')
def add_fun():
    a=request.args.get('a')
    b=request.args.get('b')
    return str(int(a)+int(b))

@app.route('/uppername')
def name_details():
    name=request.args.get('name')
    return str("\n" + name.upper()+"\n Welcome to the flask creating world ")

 ##############################################

#  running the app 
if __name__ == "__main__":
    app.run()
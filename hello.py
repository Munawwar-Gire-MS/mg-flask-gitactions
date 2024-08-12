from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def home():
    return 'I am Home Page'
 
 
@app.route('/about')
def about():
    return 'I am about Page'
 
 
@app.route('/help')
def help():
    return 'I am help Page'
 
 
@app.route('/contact')
def contact():
    return 'I am contact Page'
 
if __name__ == '__main__' :
    app.run(debug=True)



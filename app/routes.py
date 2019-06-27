from app import app
@app.route('/index')
def index():
    
    a=10
    b=10
    return(str(a+b))
@app.route('/vaibhav')
def vaibhav():
    return('Vaibhav sharma')
@app.route('/factorial')
def factorial():
    i=1
    for x in range(1,7):
        i=i*x
    return(str(i))



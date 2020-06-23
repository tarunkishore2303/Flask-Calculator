from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')

def hello():
    return render_template("index.html")

def addNums(number1,number2):
    total = number1 + number2
    return str(total)
def subtractNum(number1,number2):
    total = number1 - number2
    return str(total)
def multiplyNums(number1,number2):
    total = number1 * number2
    return str(total)
def divideNums(number1,number2):
    total = number1 / number2
    return str(total)


@app.route("/",methods=["POST"])
def addHandler():
    number1 = int(request.form["num1"])
    number2 = int(request.form["num2"])
    operation = request.form['operation']
    if(operation == 'add'):
        return addNums(number1,number2)
    elif(operation=='sub'):
        return subtractNum(number1,number2)
    elif(operation=='mul'):
        return multiplyNums(number1,number2)
    elif(operation=='div'):
        return divideNums(number1,number2)
        

if __name__=="__main__":
    app.run(debug=True)
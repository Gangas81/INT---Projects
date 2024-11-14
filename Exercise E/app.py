from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def clock():
    return render_template('url.html')

@app.route('/<filename>') #!!important!! import all the files related to that script, like CSS image and script.js
def static_files(filename):
    return app.send_static_file(filename) #will search in Folder name static

@app.route('/calc', methods=['GET'])
def calc():
    number1 = float(request.args.get('num1'))
    number2 = float(request.args.get('num2'))
    action = request.args.get('dropdown')

    if action == 'option1':
        result = number1 + number2    
    elif action == 'option2':
        result = number1 - number2   
    elif action == 'option3':
        result = number1 * number2    
    elif action == 'option4':
        result = number1 / number2    
    else:
        return jsonify(result="Error: Operation is invalid")
    print(f"Calculation result: {result}")
    return jsonify(result=f"the sum is {result:}")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
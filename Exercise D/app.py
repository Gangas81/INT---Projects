from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)
    
@app.route('/')
def clock():
    return render_template('url.html')

@app.route('/<filename>') #!!important!! import all the files related to that script, like CSS image and script.js
def static_files(filename):
    return app.send_static_file(filename) #will search in Folder name static

@app.route('/checktemp', methods=['GET'])  
def convert():
    temp = request.args.get('temp')
    if temp is None or temp == '':
        return jsonify(error="Temperature parameter missing"), 400
    
    try:
        temp = float(temp)
    except ValueError:
        return jsonify(error="Invalid temperature value"), 400

    if temp < 0:
        return jsonify(error="Temperature is below freezing."), 200
    elif temp > 100:
        return jsonify(error="Temperature is above boiling."), 200
    else:
        result = temp * 1.8 + 32  # Convert Celsius to Fahrenheit
        return jsonify(result=f"The temperature is {result:.2f} degrees F.")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")




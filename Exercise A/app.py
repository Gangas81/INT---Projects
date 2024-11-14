from flask import Flask, render_template 
import time


app = Flask(__name__)
    
@app.route('/', methods=['GET'])
def clock():
    return render_template('clock.html')

@app.route('/<filename>', methods=['GET']) #!!important!! bring us all the files related to that script, like CSS image and script.js
def static_files(filename):
    return app.send_static_file(filename) #will search in Folder name static


#Flask Route: The @app.route('/get_time') sets up a route that, when accessed, will call the get_time() function. 
#This function gets the current time and returns it in a JSON format.
@app.route('/get_time')  
def get_time():
    currentTime = time.asctime(time.localtime(time.time()))
    return {'time': currentTime}

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")



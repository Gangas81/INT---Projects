from flask import Flask, render_template, request
import requests
from tld import is_tld

app = Flask(__name__)

def is_valid_tld(url): 
    tld = url.split('.')[-1] #checks the ending, after the .
    return is_tld(tld)
    
@app.route('/')
def clock():
    return render_template('url.html')

@app.route('/<filename>') #!!important!! import all the files related to that script, like CSS image and script.js
def static_files(filename):
    return app.send_static_file(filename) #will search in Folder name static

@app.route('/check_url')  
def check_url():
    url = request.args.get ('url')
    if not is_valid_tld(url):
        return {'status_code': 'INVALID_URL_FORMAT'}
    try:
        response = requests.get(f'http://{url}', timeout=1)
        if response.status_code == 200:
                return {'status_code': 'OK'}
    except requests.exceptions.RequestException:    
            return {'status_code':'FAILED'}


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")



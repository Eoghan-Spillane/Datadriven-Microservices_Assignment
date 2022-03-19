from flask import Flask 
 
app = Flask(__name__) 


@app.route('/') 
def print_logs():
    output = ''
    try:
        output += "Hello World"
    except Exception as ex:
        output = 'Error:' + str(ex)
    return output
   
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
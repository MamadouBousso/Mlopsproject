from flask import Flask,jsonify,request
import calcularea as cal
app = Flask(__name__)

@app.get("/")
def convert_area():
    params = request.get_json()
    length = params['length']
    width = params['width']
    return 


if __name__ == '__main__':
    app.run(debug=True)
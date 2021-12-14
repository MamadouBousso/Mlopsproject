from flask import Flask,jsonify,request

app = Flask(__name__)

@app.get("/area")
def index():
    length = int(input("Give the length of the field "))
    width = int(input("Give the width of the field "))
    return str(length*width/43560)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask,jsonify,request

app = Flask(__name__)

@app.get("/greet")
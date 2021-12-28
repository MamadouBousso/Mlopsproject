# import modules
from flask import Flask, jsonify, request
from app.calc_acr import cal_acr

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def get_input():
    """
    A simple flask app to take input & invoke simple interest module to process the input parameters.
    """
    packet = request.get_json(force=True)
    width = packet["width"]
    length = packet["length"]
    

    surface= cal_acr(width, length)

    return jsonify(packet, surface)

# main driver function
if __name__ == '__main__':
    web: gunicorn __init__:app
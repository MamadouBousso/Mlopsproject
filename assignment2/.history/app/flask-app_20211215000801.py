from flask import Flask, json,jsonify,request
import calcularea as cal
app = Flask(__name__)

@app.route("/area",methods=['GET','POST'])
def convert_area():
    #data = json.loads(request.data)
    params = request.json(force=True)
    length = params['length']
    width = params['width']
    return jsonify({'length': length,'width':width,'area':cal.index(length,width)})


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask,jsonify,request
import calcularea as cal
app = Flask(__name__)

@app.route("/area",methods=['GET','POST'])
def convert_area():
    print(request.get_json())
    params = request.json
    length = params['length']
    width = params['width']
    return jsonify({'length': length,'width':width,'area':cal.index(length,width)})


if __name__ == '__main__':
    app.run(debug=True)
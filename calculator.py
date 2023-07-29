from flask import Flask, request, jsonify, render_template


app= Flask(__name__)

@app.route("/add",methods=["POST","GET"])
def add():
    if request.method == "POST":
        try:
            data = request.json
            a = data['a']
            b = data['b']
            c = a+b
        except Exception as e:
            return  jsonify({"error":str(e) })
    return jsonify(c)

@app.route("/sub",methods=["POST","GET"])
def sub():
    if request.method == "POST":
        try:
            data = request.json
            a = data['a']
            b = data['b']
            c = a-b
        except Exception as e:
             return  jsonify({"error":str(e) })
    return jsonify(c)

@app.route("/multi",methods=["POST","GET"])
def multi():
    if request.method == "POST":
        try:
            data = request.json
            a = data['a']
            b = data['b']
            c = a*b
        except Exception as e:
            return  jsonify({"error":str(e) })
    return jsonify(c)

@app.route("/div",methods=["POST","GET"])
def div():
    if request.method == "POST":
        try:
            data = request.json
            a = data['a']
            b = data['b']
            if b !=0:
                c = a/b
            else:
                return  jsonify("Zero is not allowed")
            return jsonify(c)
        except Exception as e:
            return  jsonify({"error":str(e) })


if __name__ == "__main__":
    app.run(debug=True)

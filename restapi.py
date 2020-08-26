# -*- coding: utf-8 -*-
from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app=Flask(__name__)

@app.route("/",methods=['GET'])

def get():
    return jsonify({"msg":"Hello WOrld"})

if __name__=="__main__":
    app.run(debug=True)
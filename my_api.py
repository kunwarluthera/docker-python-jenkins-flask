from flask import Flask
import boto3
import os

client = boto3.client('s3')
s3 = boto3.client('iam')
#print(client)
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World, this is my first python API inside docker"

@app.route("/list-buckets")
def buckets():
    #response = "Inside List buckets"
    response = client.list_buckets()
    #print(response)
    return str(response)

#print(str(buckets()))
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
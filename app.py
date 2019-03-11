from flask import Flask
import boto3
import os

#ACCESS_KEY = os.environ['AWS_ACCESS_KEY_ID']
#SECRET_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

client = boto3.client('s3')#,aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'], region_name='us-east-1')
s3 = boto3.client('iam')
#print(client)
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World, this is my first python API inside docker"

@app.route("/get-user")
def getUser():
    response = s3.get_user()
    res = s3.list_access_keys()
    print(res)
    print(response)
    return response

@app.route("/list-buckets")
def buckets():
    #response = "Inside List buckets"
    response = client.list_buckets()
    #print(response)
    return str(response)

#print(str(buckets()))
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
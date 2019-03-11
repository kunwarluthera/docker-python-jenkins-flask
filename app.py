from flask import Flask
import boto3
import os

ACCESS_KEY = os.environ['AWS_ACCESS_KEY_ID']
SECRET_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

client = boto3.client('s3',aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'], region_name='us-east-1')
client_ec2 = boto3.client('ec2',aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'], region_name='us-east-1')
#print(client)
app = Flask(__name__)

@app.route("/")
def hello():
    return "My first python API inside docker"

@app.route("/list-buckets")
def buckets():
    print("Inside List buckets")
    response = client.list_buckets()
    print("#####################")
    return str(response)

@app.route("/compute-details")
def ec2():
    response = client_ec2.describe_instances()
    return str(response)

#print(str(buckets()))
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
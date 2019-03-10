from flask import Flask
import boto3
import os

#ACCESS_KEY = os.environ['AWS_ACCESS_KEY_ID']
#SECRET_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

client = boto3.client('s3')#,aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY)

#print(client)
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World, this is my first python API inside docker"

@app.route("/list-buckets")
def buckets():
    response = client.list_buckets()
    print(response)
    return str(response)

#print(str(buckets()))
if __name__ == "__main__":
    app.run(debug=True)
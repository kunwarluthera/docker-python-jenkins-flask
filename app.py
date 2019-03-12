from flask import Flask, request
import boto3
import os

ACCESS_KEY = os.environ['AWS_ACCESS_KEY_ID']
SECRET_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

def client_method(service,region):
    client = boto3.client(service,aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'], region_name=region)
    return "received the "+ str(service) + str(region)

client = boto3.client('s3',aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'], region_name='us-east-1')
client_ec2 = boto3.client('ec2',aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'], region_name='us-east-1')
#print(client)
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        return "POST METHOD RECEIVED"
    else:
        return "My first python API inside docker"

@app.route("/admin")
def admin():
    service = request.args.get('service')
    region = request.args.get('region')
    print("type service  ",type(service))
    my = client_method(service,region)
    return 'Values returned '+ str(service) + str(region) +str(my)

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
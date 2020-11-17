from chalice import Chalice
from chalicelib import s3_service 
from chalicelib import s3_sqs_service 


app = Chalice(app_name='my-app')


@app.route('/')
def index():
    return {'hello': 'world'}


import boto3
  
BUCKET = 'aws-abhi-chalice'

@app.on_s3_event(bucket=BUCKET,
                 events=['s3:ObjectCreated:*'])
def handle_s3_event(event):
    app.log.debug("Received event for bucket: %s, key: %s",
                  event.bucket, event.key)
    print("Received event for bucket: %s, key: %s",
                  event.bucket, event.key)
    s3_sqs_service.sqs_send_message(event.key)



@app.route('/s3/upload/{file_name}', methods=['PUT'], content_types=['application/octet-stream'])
def upload_to_s3(file_name):
    return s3_service.upload_to_s3(app,file_name)
    
        
@app.route('/s3/list_buckets',methods=['GET'])
def list_buckets():
    return s3_service.s3_list_allbuckets(app)

#Create QUeue
@app.route('/sqs/create_queue',methods=['GET'])
def sqs_create_queue():
    return s3_sqs_service.sqs_create_queue()


#recieve messages
@app.route('/sqs/get_messages',methods=['GET'])
def get_messages():
    return s3_sqs_service.get_messages()

#recieve messages
@app.route('/sqs/send_message',methods=['GET'])
def send_messages():
    my_params=app.current_request.query_params
    message=my_params['message']
    return s3_sqs_service.sqs_send_message(message)



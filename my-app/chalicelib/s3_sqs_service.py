from chalice import Chalice,Response
import boto3


# Get the service resource
sqs = boto3.client('sqs')

# Create the queue. This returns an SQS.Queue instance

QUEUE_NAME="aws-chalice-demo-queue"

def sqs_create_queue():
    try:
        queue = sqs.create_queue(QueueName=QUEUE_NAME, Attributes={'DelaySeconds': '5'})
        return {"Success":'Queue has been created'+QUEUE_NAME,"status_code":200}     
    except Exception as e:
        #app.log.error('error occurred during creating queue')
        return {"Error":'error occurred during creating queue'+str(e),"status_code":400}


def sqs_send_message(message_body):
    
    try:
        queue_response = sqs.get_queue_url(QueueName=QUEUE_NAME)
        print(queue_response)
        queue_url=queue_response['QueueUrl']
        response = sqs.send_message(QueueUrl=queue_url,
        DelaySeconds=10,
        MessageBody=(message_body)
        )

       
        return {" message Id":response['MessageId']}
    
    except Exception as e:
        print(e)
        #app.log.error('error occurred during creating queue')
        return {"Error":'error occurred during sending message queue'+str(e),"status_code":400}


def get_messages():

    try:
        queue_response = sqs.get_queue_url(QueueName=QUEUE_NAME)
        #print(queue_response)
        queue_url=queue_response['QueueUrl']
        #print(queue_url)
        # Receive message from SQS queue
        response = sqs.receive_message(
        QueueUrl=queue_url,
        AttributeNames=[
            'SentTimestamp'
        ],
        MaxNumberOfMessages=10,
        MessageAttributeNames=[
            'All'
        ],
        VisibilityTimeout=20,
        WaitTimeSeconds=20
        )

        messages = response['Messages']
               
        return messages


    
    except Exception as e:
        print(str(e))
        #app.log.error('error occurred during creating queue')
        return {"Error":'error occurred during sending message queue'+str(e),"status_code":400}

    


        
        

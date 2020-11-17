from chalice import Chalice,Response
import boto3


s3 = boto3.client('s3', region_name='us-east-1')
BUCKET = 'aws-abhi-chalice'



def upload_to_s3(app,file_name):
    try:
        body = app.current_request.raw_body
        temp_file = '/tmp/' + file_name
        with open(temp_file, 'wb') as f:
            f.write(body)
        s3.upload_file(temp_file, BUCKET, file_name)
        return {"bucket_name":BUCKET,
        "file_uploaded":file_name
        }
    except Exception as e:
        app.log.error('error occurred during upload '+str(e))
        return {"Error":"Error occured while listing s3 bucket "+str(e),"status_code":400}
        
        
def s3_list_allbuckets(app):
    try:
        response = s3.list_buckets()
        buckets = [bucket['Name'] for bucket in response['Buckets']]
        return {"bucket_list":','.join(buckets)}
        
    except Exception as e:
        app.log.error("error occurred during upload "+str(e))
        return {"Error":"Error occured while listing s3 bucket "+str(e),"status_code":400}
        
        
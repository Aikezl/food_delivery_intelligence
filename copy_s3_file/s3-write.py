from io import StringIO
import boto3
import pandas as pd
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # Loads the .env file.


def write_to_s3(bucket_name, file_name):

        s3_resource = boto3.resource('s3',
                                        aws_access_key_id=os.getenv('ACCESS_KEY_ID'),  
                                        aws_secret_access_key=os.getenv("SECRET_ACCESS_KEY"))
        #s3 = boto3.client('s3',
                            #aws_access_key_id=os.getenv('ACCESS_KEY_ID'),  
                            #aws_secret_access_key=os.getenv("SECRET_ACCESS_KEY"))
    

        csv_buffer = StringIO()
        df.to_csv(csv_buffer)
        #obj = s3_resource.put_object(Bucket = bucket_name, Key = file_name, Body = csv_buffer.getvalue(), ACL = 'private')
        s3_resource.Object(bucket_name, file_name).put(Body=csv_buffer.getvalue())
        print("Done............")

def upload_from_local_to_s3(bucket_name, file_name):
    s3_resource = boto3.resource('s3',
                                 aws_access_key_id=os.getenv('ACCESS_KEY_ID'),
                                 aws_secret_access_key=os.getenv("SECRET_ACCESS_KEY"))

    s3_resource.upload_file(file_name, bucket_name, file)


        # We can call the function as follows:
bucket_name = "uk-naija-datascience-21032023"
file_name = "/Users/collinsorighose/Downloads/new-omolewa.csv"

file_contents = write_to_s3(bucket_name, file_name)

"""
Author: Javier J. Rodríguez
Date: 2024-11-05
Version: 1.0

Description:
	This Python script checks if a local file (counter.csv) exists at the specified path, 
	and if so, attempts to upload it to a predefined AWS S3 bucket (ggc-project-s3-bucket) using boto3; 
	it handles AWS operations and file handling errors, providing feedback on success or failure.

  You need to upload this code to your S3 bucket.

License: MIT License

"""

import os
import boto3
from botocore.exceptions import BotoCoreError, ClientError

# AWS S3 bucket name and file paths
BUCKET_NAME = 'ggc-project-s3-bucket'
FILE_NAME = '/home/ggc/greengrassv2/data/counter.csv'  # Full path to counter.csv on the Raspberry Pi

# Initialize S3 client
s3_client = boto3.client('s3')

def upload_file():
    """Upload the specified file to the designated S3 bucket."""
    if not os.path.exists(FILE_NAME):
        print(f"File {FILE_NAME} does not exist, cannot upload.")
        return

    try:
        # Upload file to S3
        s3_client.upload_file(FILE_NAME, BUCKET_NAME, UPLOAD_PATH)
        print(f"File {FILE_NAME} successfully uploaded to s3://{BUCKET_NAME}/{UPLOAD_PATH}")
    except (BotoCoreError, ClientError) as error:
        print(f"Failed to upload {FILE_NAME}: {error}")

if __name__ == "__main__":
    upload_file()


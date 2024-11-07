"""
Author: Javier J. Rodríguez
Date: 2024-11-05
Version: 1.0

Description:
	This Python script uses the boto3 library to connect to an AWS S3 bucket named ggc-project-s3-bucket,
	lists all objects within the specified prefix (greengrass_rpi4Project/1.0.0/), 
	and prints each file's key (name) and its last modified date.

License: MIT License

"""

import boto3

s3 = boto3.client('s3')
bucket_name = 'ggc-project-s3-bucket'
prefix = 'greengrass_rpi4Project/1.0.0/'

response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
for obj in response.get('Contents', []):
    print(f"File: {obj['Key']}, Last Modified: {obj['LastModified']}")


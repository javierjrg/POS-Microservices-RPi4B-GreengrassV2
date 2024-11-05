"""
Author: Javier J. Rodríguez
Date: 2024-11-05
Version: 1.0
Description:
  The s3_test1.py script performs a series of tests by appending results to a local CSV file, 
  checks network availability, uploads the CSV file to an S3 bucket if the network is available, 
  and prompts the user to rerun the test or display the file contents upon exit.
  
License: MIT License
"""

import os
import csv
import boto3
import socket
from botocore.exceptions import NoCredentialsError, ClientError

def check_file_exists(filepath):
    return os.path.exists(filepath)

def create_file(filepath):
    with open(filepath, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Test Number', 'Result'])

def append_test_result(filepath, test_number):
    with open(filepath, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([test_number, f"Test {test_number} successful!"])

def display_file_contents(filepath):
    with open(filepath, mode='r') as file:
        rows = file.readlines()
        for row in rows:
            print(row.strip())

def is_network_available():
    try:
        # Connect to Google DNS to check for network availability
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False

# AWS S3 bucket name and file name
BUCKET_NAME = 'ggc-project-s3-bucket'
S3_FILE_NAME = 'greengrass_rpi4Project/1.0.0/test.csv'

def upload_to_s3(file_path):
    """Upload a file to an S3 bucket."""
    if not is_network_available():
        print("Network unavailable. Skipping S3 upload.")
        return

    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_path, BUCKET_NAME, S3_FILE_NAME)
        print(f"File {file_path} uploaded to {BUCKET_NAME}/{S3_FILE_NAME}")
    except FileNotFoundError:
        print(f"The file was not found: {file_path}")
    except NoCredentialsError:
        print("Credentials not available")
    except ClientError as e:
        print(f"Failed to upload to S3: {e}")

def run_tests():
    filepath = os.path.expanduser("~/greengrassv2/data/test.csv")
    if not check_file_exists(filepath):
        create_file(filepath)
        test_number = 1
    else:
        with open(filepath, mode='r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            test_number = len(rows)  # Last row count determines the test number
            test_number += 1

    # Append test result to the CSV file
    append_test_result(filepath, test_number)
    print(f"Test {test_number} successful!")
    return filepath  # Return the filepath for uploading to S3

if __name__ == "__main__":
    while True:
        filepath = run_tests()  # Get the filepath after running tests
        upload_to_s3(filepath)  # Attempt upload after appending test result
        choice = input("Do you want to rerun the test? (y/n): ").strip().lower()
        if choice != 'y':
            print("Exiting the program. Here are the contents of the test.csv file:")
            display_file_contents(filepath)  # Display contents of the file
            break


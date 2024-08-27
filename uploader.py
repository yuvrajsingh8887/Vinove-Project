import boto3
import os
from botocore.exceptions import NoCredentialsError, ClientError
import logging

class Uploader:
    def __init__(self, s3_bucket, s3_access_key, s3_secret_key, screenshot_dir='screenshots'):
        self.s3_bucket = s3_bucket
        self.s3_access_key = s3_access_key
        self.s3_secret_key = s3_secret_key
        self.screenshot_dir = screenshot_dir

        self.s3_client = boto3.client('s3', aws_access_key_id=self.s3_access_key, aws_secret_access_key=self.s3_secret_key)
        logging.basicConfig(filename='uploader.log', level=logging.INFO)

    def upload_files(self):
        for filename in os.listdir(self.screenshot_dir):
            file_path = os.path.join(self.screenshot_dir, filename)
            try:
                logging.info(f"Uploading {filename}...")
                self.s3_client.upload_file(file_path, self.s3_bucket, filename)
                os.remove(file_path)  # Remove file after successful upload
                logging.info(f"Successfully uploaded and removed {filename}")
            except NoCredentialsError:
                logging.error("Credentials not available")
            except ClientError as e:
                logging.error(f"ClientError: {e}")
            except Exception as e:
                logging.error(f"Error uploading {filename}: {e}")

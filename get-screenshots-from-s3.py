import boto3
import os
from botocore.exceptions import NoCredentialsError, ClientError

def download_screenshots_from_s3(s3_bucket, s3_access_key, s3_secret_key, download_dir='downloaded_screenshots'):
    s3_client = boto3.client('s3', aws_access_key_id=s3_access_key, aws_secret_access_key=s3_secret_key)
    os.makedirs(download_dir, exist_ok=True)
    
    try:
        # List objects in the specified S3 bucket
        response = s3_client.list_objects_v2(Bucket=s3_bucket)
        for obj in response.get('Contents', []):
            filename = obj['Key']
            download_path = os.path.join(download_dir, filename)
            s3_client.download_file(s3_bucket, filename, download_path)
            print(f"Downloaded {filename} to {download_path}")
    except NoCredentialsError:
        print("Credentials not available")
    except ClientError as e:
        print(f"ClientError: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace these with your actual S3 credentials and bucket name
    s3_bucket = "monitoring-agent-vinove"
    s3_access_key = "AKIA4MEMOS3N5TEAOE3J"
    s3_secret_key = "P5ogtlKAaRo5N4MCl84U8WodFWPPMU1aGDMmwoQa"
    
    download_screenshots_from_s3(s3_bucket, s3_access_key, s3_secret_key)






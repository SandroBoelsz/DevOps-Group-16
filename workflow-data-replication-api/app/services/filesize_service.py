import boto3
import os

def get_file_size(bucket_name, filename):
    """
    Get file size from MinIO using boto3.

    :param bucket_name: MinIO bucket name
    :param filename: File name in the bucket
    :return: File size in bytes or None if not found.
    """
    # MinIO Client Configuration
    minio_client = boto3.client(
        's3',
        endpoint_url=os.getenv("SPAIN_MINIO_API"),
        aws_access_key_id=os.getenv("MINIO_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("MINIO_ACCESS_KEY"),
        region_name=os.getenv("MINIO_REGION") 
    )

    try:
        response = minio_client.head_object(Bucket=bucket_name, Key=filename)
        return response['ContentLength']
    except Exception as e:
        print(f"Error getting file size: {e}")
        return None

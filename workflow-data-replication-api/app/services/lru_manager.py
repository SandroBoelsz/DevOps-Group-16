import os
import boto3
from datetime import datetime

class LRUManager:
    def __init__(self):
        # Change SPAIN_MINIO_API to UVA_MINIO_API
        self.minio_client = boto3.client(
        's3',
        endpoint_url=os.getenv("SPAIN_MINIO_API"),
        aws_access_key_id=os.getenv("MINIO_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("MINIO_ACCESS_KEY"),
        region_name=os.getenv("MINIO_REGION") 
    )

    def get_oldest_file(self, min_size):
        """
        Find the oldest file that is at least `min_size` bytes.
        """
        
		# Change to get data from all buckets
        try:
            response = self.minio_client.list_objects_v2(Bucket="devopsgoup16")
            if "Contents" not in response:
                return None, None

            sorted_files = sorted(
                response["Contents"], 
                key=lambda x: x["LastModified"]
            )

            for obj in sorted_files:
                if obj["Size"] >= min_size:
                    return obj["Key"], obj["Size"]

        except Exception as e:
            print(f"Error retrieving file list: {e}")

        return None, None
    

    def remove_oldest_file(self, min_size):
        """
        Delete the least recently used (oldest) file that is at least `min_size` bytes.
        """
        filename, file_size = self.get_oldest_file(min_size)
        # if filename:
        #     try:
        #         self.minio_client.delete_object(Bucket="uva-minio-bucket", Key=filename)
        #         print(f"Deleted LRU file: {filename} ({file_size} bytes)")
        #         return filename
        #     except Exception as e:
        #         print(f"Error deleting file: {e}")

        return filename

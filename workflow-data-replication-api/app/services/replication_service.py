import logging
from dotenv import load_dotenv
from rclone_python import rclone
from rclone_python.remote_types import RemoteTypes

load_dotenv()


def trigger_replication(source_bucket, source_filepath, target_bucket, target_filepath):
    """
    Trigger a new data replication process using Rclone
    """
    source_path = f"source-minio-s3:{source_bucket}/{source_filepath}"
    target_path = f"target-minio-s3:{target_bucket}/{target_filepath}"

    try:
        rclone.copy(
            source_path,
            target_path,
            ignore_existing=True,
            show_progress=True,
            args=["--progress", "--s3-force-path-style", "--s3-no-check-bucket"]
        )
        return {"status": "success"}
    except Exception as e:
        logging.error(f"Replication failed: {e}")
        return {"status": "error", "message": f"Replication failed: {e}"}

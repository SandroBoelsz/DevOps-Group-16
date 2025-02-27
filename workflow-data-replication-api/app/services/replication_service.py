import logging
from rclone_python import rclone
from rclone_python.remote_types import RemoteTypes


def trigger_replication(source_path, target_path):
    """
    Trigger a new data replication process using Rclone
    """
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

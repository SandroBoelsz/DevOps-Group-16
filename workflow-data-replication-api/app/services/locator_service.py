from rclone_python import rclone
import os

def locate_file(source_path, target_path):
    """
    Locate the file in the target MinIO server
    """
    empty_local_path = os.makedirs("/tmp/empty", exist_ok=True)
    _, sourceDetails = rclone.check(source_path, empty_local_path, one_way=True)
    _, targetDetails = rclone.check(target_path, empty_local_path, one_way=True)

    for action, filepath in targetDetails:
        if action == "+":
            return {"status": "success", "message": "File already present in the Dutch S3 bucket", "startReplication": False}
        elif action == "!":
            return {"status": "error", "message": f"Error reading or hashing the target file: {filepath}", "startReplication": False}
        
    for action, filepath in sourceDetails:
        if action == "+":
            return {"status": "success", "message": "File is present in Spanish but not in Dutch S3 bucket", "startReplication": True}
        elif action == "!":
            return {"status": "error", "message": f"Error reading or hashing the source file: {filepath}", "startReplication": False}
    
    return {"status": "error", "message": "File is not present in both Spanish and Dutch S3 buckets", "startReplication": False}


import os
from flask_restx import Namespace, Resource
from app.services.locator_service import locate_file
from app.services.filesize_service import get_file_size
from app.services.lru_manager import LRUManager
from app.services.replication_service import trigger_replication
from app.models.replication_model import get_replication_model

replication_ns = Namespace(
    "workflow-data-replication", description="Endpoints for workflow replication")
replication_model = get_replication_model(replication_ns)
lru_manager = LRUManager()

@replication_ns.route("/trigger")
class StartReplication(Resource):
    @replication_ns.expect(replication_model)
    @replication_ns.doc(description="Trigger a new workflow data replication process")
    @replication_ns.response(200, "File is available on the target MinIO server")
    @replication_ns.response(400, "Invalid input")
    @replication_ns.response(500, "Internal server error")
    def post(self):
        """
        Start a new workflow data replication process
        """
        data = replication_ns.payload
        
        if (data["minioUrl"] == os.getenv("UVA_MINIO_API")):
            source_path = self.build_rclone_path("spain-minio-s3", "devopsgoup16", data["filename"])
            target_path = self.build_rclone_path('uva-minio-s3', data["bucket"], data["filename"])
        else:
            return {"message": "Only UvA MinIO URL is supported"}, 400

        locate_file_result = locate_file(source_path, target_path)
        if locate_file_result["status"] == "error":
            return {"message": locate_file_result["message"]}, 500
        
        if not locate_file_result["startReplication"]:
            return {"message": locate_file_result["message"]}, 200
        
        file_size = get_file_size(data["bucket"], data["filename"])
        if file_size is None:
            return {"message": "File not found in Spain MinIO"}, 400
        else:
            print(f"File size: {file_size} bytes")
        
        removed_file = lru_manager.remove_oldest_file(file_size)
        if removed_file:
            print(f"Removed LRU file: {removed_file} to make space.")
        else:
            print("No LRU file removed.")
            
        if locate_file_result["startReplication"]:
            target_path = os.path.dirname(target_path)
            result = trigger_replication(source_path, target_path)
            if result["status"] == "error":
                return {"message": result["message"]}, 500

        return {"message": "File is succesfully replicated on Dutch S3 bucket"}, 200

    def build_rclone_path(self, minio_url, bucket, filename):
        """
        Build the Rclone path for the MinIO server
        """            
        return f"{minio_url}:{bucket}/{filename}"


import os
from flask_restx import Namespace, Resource
from app.services.locator_service import locate_file
from app.services.replication_service import trigger_replication
from app.models.replication_model import get_replication_model
from rclone_python import rclone

supported_urls = os.getenv("SUPPORTED_URLS").split(",")

replication_ns = Namespace(
    "workflow-data-replication", description="Endpoints for workflow replication")
replication_model = get_replication_model(replication_ns)


@replication_ns.route("/trigger")
class StartReplication(Resource):
    @replication_ns.expect(replication_model)
    @replication_ns.doc(description="Trigger a new workflow data replication process")
    @replication_ns.response(200, "Replication started successfully")
    @replication_ns.response(400, "Invalid input")
    @replication_ns.response(500, "Internal server error")
    def post(self):
        """
        Start a new workflow data replication process
        """
        data = replication_ns.payload
        error_message, status_code = self.validate_input(data)
        if error_message:
            return {"message": error_message}, status_code

        # Example call to trigger_replication function
        source_bucket = "devopsgoup16"
        source_filepath = "Screenshot 2025-02-25 at 09.14.34.png"
        target_bucket = "naa-vre-user-data"
        target_filepath = "s.boelsz@gmail.com"

        result = trigger_replication(source_bucket, source_filepath, target_bucket, target_filepath)
        if result["status"] == "error":
            return {"message": result["message"]}, 500
        
        return {"message": "Replication completed successfully"}, 200

    def validate_input(self, data):
        """
        Validate the input data for the replication process
        """
        if data["minioUrl"] not in supported_urls:
            return "MinIO URL is not supported", 400

        if not locate_file(data["minioUrl"], data["bucket"], data["filename"]):
            return "File not found in Netherlands or Spain", 400

        return None, None

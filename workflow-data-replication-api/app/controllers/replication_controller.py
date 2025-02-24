from flask_restx import Namespace, Resource
from app.services.replication_service import trigger_replication
from app.models.replication_model import get_replication_model
from rclone_python import rclone

replication_ns = Namespace(
    "workflow-data-replication", description="Endpoints for workflow replication")
replication_model = get_replication_model(replication_ns)


@replication_ns.route("/trigger")
class StartReplication(Resource):
    @replication_ns.expect(replication_model)
    @replication_ns.doc(description="Trigger a new workflow data replication process")
    @replication_ns.response(200, "Replication started successfully")
    @replication_ns.response(400, "Invalid input")
    @replication_ns.response(500, "Rclone is unavailable at the moment")
    def post(self):
        """
        Start a new workflow data replication process
        """
        if not rclone.is_installed():
            return {"message": "Rclone is unavailable at the moment"}, 500
        
        data = replication_ns.payload
        result = trigger_replication(data["workflowUrl"], data["minioUrl"], data["bucket"], data["filename"], data["status"])
        return {"message": result}, 200

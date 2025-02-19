from flask_restx import Namespace, Resource
from app.services.replication_service import start_replication
from app.models.replication_model import get_replication_model

replication_ns = Namespace(
    "replication", description="Endpoints for data replication")
replication_model = get_replication_model(replication_ns)


@replication_ns.route("/start")
class StartReplication(Resource):
    @replication_ns.expect(replication_model)
    @replication_ns.doc(description="Starts a new data replication process")
    @replication_ns.response(200, "Replication started successfully")
    @replication_ns.response(400, "Invalid input")
    def post(self):
        """
        Start a data replication process
        """
        data = replication_ns.payload
        result = start_replication(data["source"], data["destination"])
        return {"message": result}, 200

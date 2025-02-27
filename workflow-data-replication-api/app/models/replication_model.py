from flask_restx import fields


def get_replication_model(replication_ns):
    return replication_ns.model("ReplicationModel", {
        "endpoint": fields.String(required=True, description="Endpoint of the MinIO server"),
        "bucket": fields.String(required=True, description="Name of the bucket"),
        "filename": fields.String(required=True, description="Name of the file"),
    })

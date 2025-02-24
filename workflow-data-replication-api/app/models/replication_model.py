from flask_restx import fields


def get_replication_model(replication_ns):
    return replication_ns.model("ReplicationModel", {
        "workflowUrl": fields.String(required=True, description="URL of the workflow"),
        "minioUrl": fields.String(required=True, description="URL of the MinIO server"),
        "bucket": fields.String(required=True, description="Name of the bucket"),
        "filename": fields.String(required=True, description="Name of the file"),
        "status": fields.String(required=True, description="Status of the workflow")
    })

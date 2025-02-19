from flask_restx import fields


def get_replication_model(replication_ns):
    return replication_ns.model("ReplicationModel", {
        "source": fields.String(required=True, description="Source database"),
        "destination": fields.String(required=True, description="Destination database")
    })

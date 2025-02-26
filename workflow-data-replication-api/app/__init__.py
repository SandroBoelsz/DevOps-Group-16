import os
import logging
from flask import Flask
from flask_restx import Api
from dotenv import load_dotenv
from rclone_python import rclone
from rclone_python.remote_types import RemoteTypes

load_dotenv()


def setup_rclone():
    if (not rclone.is_installed() or not os.getenv("UVA_MINIO_API") or
            not os.getenv("SPAIN_MINIO_API") or not os.getenv("MINIO_ACCESS_KEY_ID") or not os.getenv("MINIO_ACCESS_KEY")):
        raise Exception(
            "Rclone is not installed or environment variables are not set")

    logging.info("Setting up rclone remotes")
    if not rclone.check_remote_existing("source-minio-s3"):
        rclone.create_remote(
            "source-minio-s3",
            RemoteTypes.s3,
            provider="Minio",
            region=os.getenv("MINIO_REGION"),
            access_key_id=os.getenv("MINIO_ACCESS_KEY_ID"),
            secret_access_key=os.getenv("MINIO_ACCESS_KEY"),
            endpoint=os.getenv("UVA_MINIO_API")
        )

    if not rclone.check_remote_existing("target-minio-s3"):
        rclone.create_remote(
            "target-minio-s3",
            RemoteTypes.s3,
            provider="Minio",
            region=os.getenv("MINIO_REGION"),
            access_key_id=os.getenv("MINIO_ACCESS_KEY_ID"),
            secret_access_key=os.getenv("MINIO_ACCESS_KEY"),
            endpoint=os.getenv("SPAIN_MINIO_API")
        )


def init_app():
    try:
        setup_rclone()
    except Exception as e:
        print(f"Error setting up rclone: {e}")
        return None

    app = Flask(__name__)

    # Import controllers
    from app.controllers.replication_controller import replication_ns

    api = Api(app, version="1.0", title="Workflow Data Replication API",
              description="API for data replication between data sources")

    # Namespaces
    api.add_namespace(replication_ns, path="/workflow-data-replication")

    return app

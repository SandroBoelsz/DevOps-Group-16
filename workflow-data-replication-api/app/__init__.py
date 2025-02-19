from flask import Flask
from flask_restx import Api


def init_app():
    app = Flask(__name__)

    # Import controllers
    from app.controllers.replication_controller import replication_ns

    api = Api(app, version="1.0", title="Workflow Data Replication API",
              description="API for data replication between data sources")

    # Namespaces
    api.add_namespace(replication_ns, path="/replication")

    return app

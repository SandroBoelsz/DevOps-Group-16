def trigger_replication(workflow_url, minio_url, bucket, filename, status):
    """
    Trigger a new data replication process
    """
    return workflow_url + ", " + minio_url + ", " + bucket + ", " + filename + ", " + status

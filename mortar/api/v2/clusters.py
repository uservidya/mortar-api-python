# cluster status_code values
CLUSTER_STATUS_PENDING    = "pending"
CLUSTER_STATUS_STARTING   = "starting"
CLUSTER_STATUS_STARTING_REQUESTED_STOP = "starting_requested_stop"
CLUSTER_STATUS_RUNNING    = "running"
CLUSTER_STATUS_STOPPING   = "stopping"
CLUSTER_STATUS_DESTROYED  = "destroyed"
CLUSTER_STATUS_FAILED     = "failed"

# cluster types
CLUSTER_TYPE_SINGLE_JOB = 'single_job'
CLUSTER_TYPE_PERSISTENT = 'persistent'
CLUSTER_TYPE_PERMANENT  = 'permanent'

def get_clusters(api):
    return api.get('clusters')

def stop_cluster(api, cluster_id):
    api.delete('clusters/%s' % cluster_id)

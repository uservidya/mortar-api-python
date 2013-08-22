import time

from mortar.api.v2 import clusters

# Job Status constants
STATUS_STARTING          = 'starting'
STATUS_GATEWAY_STARTING  = 'GATEWAY_STARTING' #Comes from task.
STATUS_VALIDATING_SCRIPT = 'validating_script'
STATUS_SCRIPT_ERROR      = 'script_error'
STATUS_PLAN_ERROR        = 'plan_error'
STATUS_STARTING_CLUSTER  = 'starting_cluster'
STATUS_RUNNING           = 'running'
STATUS_SUCCESS           = 'success'
STATUS_EXECUTION_ERROR   = 'execution_error'
STATUS_SERVICE_ERROR     = 'service_error'
STATUS_STOPPING          = 'stopping'
STATUS_STOPPED           = 'stopped'

# All statuses that indicate a completed job
COMPLETE_STATUSES = (\
    STATUS_SCRIPT_ERROR, 
    STATUS_PLAN_ERROR, 
    STATUS_SUCCESS, 
    STATUS_EXECUTION_ERROR, 
    STATUS_SERVICE_ERROR,
    STATUS_STOPPED)

def post_job_new_cluster(api, project_name, script_name, cluster_size, cluster_type=clusters.CLUSTER_TYPE_PERSISTENT,
                         git_ref='master', parameters=None, notify_on_job_finish=True, is_control_script=False):
    body = {'project_name': project_name,
            'git_ref': git_ref,            
            'cluster_size': cluster_size,
            'cluster_type': cluster_type,
            'parameters': parameters or {},
            'notify_on_job_finish': notify_on_job_finish
    }
    
    if is_control_script:        
        body["controlscript_name"] = script_name
    else:
        body["pigscript_name"] = script_name
    
    return api.post('jobs', body)['job_id']


def post_job_existing_cluster(api, project_name, script_name, cluster_id, cluster_type=clusters.CLUSTER_TYPE_PERSISTENT,
                              git_ref='master', parameters=None, notify_on_job_finish=True, is_control_script=False):
    body = {'project_name': project_name,
            'git_ref': git_ref,            
            'cluster_id': cluster_id,
            'parameters': parameters or {},
            'notify_on_job_finish': notify_on_job_finish
    }
    
    if is_control_script:        
        body["controlscript_name"] = script_name
    else:
        body["pigscript_name"] = script_name
    
    return api.post('jobs', body)['job_id']
    

def get_job(api, job_id):
    return api.get('jobs/%s' % job_id)

def get_jobs(api, skip=None, limit=None):
    return api.get('jobs', 
                   params={'skip': skip, 'limit': limit})

def block_until_job_complete(api, job_id, poll_frequency_sec=5.0):
    while True:
        job_status = get_job(api, job_id)['status_code']
        if job_status in COMPLETE_STATUSES:
            return job_status
        time.sleep(poll_frequency_sec)

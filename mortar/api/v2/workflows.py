import time

def post_workflow(api, project_name, workflow_name, git_ref='master', parameters=None):
    body = {'project_name': project_name,
            'workflow_name': workflow_name,
            'git_ref': git_ref,
            'parameters': parameters or {}
    }
    
    return api.post('workflows', body)['workflow_id']

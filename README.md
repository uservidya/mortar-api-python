# mortar-api-python

The Mortar API Client for Python is a Python wrapper to interact with [Mortar](http://www.mortardata.com/).

## Running a Job

To run a job on a new cluster:

```python
from mortar.api.v2 import API
from mortar.api.v2 import jobs

# mortar credentials
email = 'myemail@me.org'
api_key = 'my-API-key'

# job to run
project_name = 'mortar-examples'
script_name = 'top_density_songs'
cluster_size = 2

# run and monitor the job
api = API(email, api_key)
final_job_status = jobs.block_until_job_complete(api, job_id)
```

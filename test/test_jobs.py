import unittest

from mortar.api.v2 import jobs

import mock

class TestJobs(unittest.TestCase):

    def setUp(self):
        self.api_mock = mock.Mock()
        self.project_name = 'my_project'
        self.script_name = 'my_script'
    
    def test_post_job_new_cluster(self):
        cluster_size = 2
        expected_job_id = 'abcdefghijklmnop'
        self.api_mock.post.return_value = {'job_id': expected_job_id}
        actual_job_id = jobs.post_job_new_cluster(self.api_mock, self.project_name, self.script_name, cluster_size)
        self.assertEquals(expected_job_id, actual_job_id)

    def test_post_job_existing_cluster(self):
        cluster_id = 'xyz123fdsa'
        expected_job_id = 'abcdefghijklmnop'
        self.api_mock.post.return_value = {'job_id': expected_job_id}
        actual_job_id = jobs.post_job_new_cluster(self.api_mock, self.project_name, self.script_name, cluster_id)
        self.assertEquals(expected_job_id, actual_job_id)

    def test_get_job(self):
        job_id = 'xyz'
        response = {'job_id': job_id, 'status_code': 'success'}
        self.api_mock.get.return_value = response
        job = jobs.get_job(self.api_mock, job_id)
        self.assertEquals(job, response)
    
    def test_get_jobs(self):
        response = [{'job_id': 'abc', 'status_code': 'success'},
                    {'job_id': 'xyz', 'status_code': 'success'}]
        self.api_mock.get.return_value = response
        return_jobs = jobs.get_jobs(self.api_mock)
        self.assertEquals(return_jobs, response)

import unittest

from mortar.api.v2 import clusters

import mock

class TestClusters(unittest.TestCase):

    def setUp(self):
        self.api_mock = mock.Mock()
        self.project_name = 'my_project'
        self.script_name = 'my_script'
    
    def test_get_clusters(self):
        response = [{'cluster_id': 'abc'},
                    {'cluster_id': 'xyz'}]
        self.api_mock.get.return_value = response
        return_clusters = clusters.get_clusters(self.api_mock)
        self.assertEquals(return_clusters, response)

    def test_stop_cluster(self):
        self.api_mock.delete.return_value = None
        clusters.stop_cluster(self.api_mock, '123456')
        self.api_mock.delete.assert_called_with('clusters/123456')

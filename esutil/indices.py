import json
import elasticsearch

from config import ES_HOST, ES_PORT

class EsIndices(object):
    """
    This class manages ElasticSearch index creation, update, and deletion.  It provides a wrapper
    to the RESTful API.
    """

    def __init__(self, **kwargs):
        """
        Constructor
        """
        pass

    def create_index(self, index_name, shards, replicas):
        """
        Create an index
        """

    def update_index(self, index_name, replicas):
        """
        Update the configuration of an index
        """

    def delete_index(self, index_name):
        """
        Delete an index from ElasticSearch
        """

    def create_indices(self):
        """
        Parses JSON and creates multiple indices, one at a time by calling CreateIndex.
        """


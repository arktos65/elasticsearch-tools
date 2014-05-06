import json
import elasticsearch

from config import ES_HOST, ES_PORT

class Mappings(object):
    """
    This class provides functions to list, display, and delete index mappings from ElasticSearch.
    """

    def __init__(self):
        pass

    def list_mappings(self):
        """
        List all mappings stored in the ElasticSearch cluster.
        """

    def delete_mapping(self, map_name):
        """
        Delete the specific mapping from the ElasticSearch cluster.
        """

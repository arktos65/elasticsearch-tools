import json
import elasticsearch

from config import ES_HOST, ES_PORT

class EsAliases(object):
    """
    This class manages ElasticSearch alias creation and deletion.  It provides a wrapper
    to the RESTful API.
    """

    def __init__(self, **kwargs):
        """
        Constructor
        """
        pass

    def create_alias(self, alias_name, index_name):
        """
        Create an index alias
        """

    def delete_alias(self, alias_name):
        """
        Delete an index from ElasticSearch
        """



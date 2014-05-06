import json
import elasticsearch

from config import ES_HOST, ES_PORT

class EsAliases(object):
    """ This class manages ElasticSearch alias creation and deletion.  It provides a wrapper
        to the RESTful API.
    """

    def __init__(self, **kwargs):
        """ Constructor
        """

    def CreateAlias(self):
        """ Create an index
        """

    def DeleteAlias(self):
        """ Delete an index from ElasticSearch
        """



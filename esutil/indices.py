import json
import elasticsearch

from config import ES_HOST, ES_PORT

class EsIndices(object):
    """ This class manages ElasticSearch index creation, update, and deletion.  It provides a wrapper
        to the RESTful API.
    """

    def __init__(self, **kwargs):
        """ Constructor
        """

    def CreateIndex(self):
        """ Create an index
        """

    def UpdateIndex(self):
        """ Update the configuration of an index
        """

    def DeleteIndex(self):
        """ Delete an index from ElasticSearch
        """

    def CreateIndices(self):
        """ Parses JSON and creates multiple indices, one at a time by calling CreateIndex.
        """


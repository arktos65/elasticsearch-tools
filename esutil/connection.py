from elasticsearch import Elasticsearch

class Connection(object):
    """
    Creates and returns an ElasticSearch connection object.
    """

    def __init__(self, host_name, port_num):
        """
        Instantiate the ElasticSearch connection object.
        """
        self.es_host = "%s:%s" % (host_name, port_num)

    def get_connection(self):
        return Elasticsearch(self.es_host)

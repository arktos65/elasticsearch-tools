from elasticsearch import Elasticsearch

class Connection(object):
    """
    Creates and returns an ElasticSearch connection object.
    """

    def __init__(self, host_name, port_num):
        """
        Instantiate the ElasticSearch connection object.
            host_name       Host name of an ElasticSearch node
            port_number     Port number of the ElasticSearch API on node
        """
        self.es_host = "%s:%s" % (host_name, port_num)

    def get_connection(self):
        """
        Returns an ElasticSearch connection object.
        """
        return Elasticsearch(self.es_host)

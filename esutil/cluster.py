import json

from connection import Connection
from result import acknowledge_result

class Cluster(object):
    """
    This class provides access to ElasticSearch cluster management features.
    """

    def __init__(self, host_name, port_number):
        """
        Instantiate object with the following parameters:
            host_name       ElasticSearch host name
            port_number     ElasticsSearch API port number
        """
        self.es_connection = Connection(host_name, port_number)

    def cluster_health(self, index_name):
        """
        Display basic cluster health information, or if index is specified, of that index.
            index_name      Index to get health status on
        """
        es = self.es_connection.get_connection()
        if index_name == "_all":
            result = es.cluster.health()
        else:
            result = es.cluster.health(index=index_name)

        # Print an error if one occurred
        if not acknowledge_result(result):
            # Display results
            print json.dumps(result, sort_keys=True, indent=4, separators=(',',': '))
import json

from connection import Connection
from elasticsearch import RequestError

class Aliases(object):
    """
    This class contains all the methods related to ElasticSearch alias management.
    """

    def __init__(self, host_name, port_number):
        """
        Instantiate object with the following parameters:
            host_name       ElasticSearch host name
            port_number     ElasticsSearch API port number
        """
        self.es_connection = Connection(host_name, port_number)

    def create_alias(self, alias_name, index_name):
        """
        Create an alias to the specified index.
            alias_name      The alias name to create
            index_name      The index the alias points to
        """
        es = self.es_connection.get_connection()
        result = es.indices.put_alias(
            name=alias_name,
            index=index_name,
            ignore=400
        )

        if result and result.get('acknowledged'):
            print "acknowledged: %s" % result['acknowledged']
        elif result.get('error'):
            print "error: %s" % result['error']
        else:
            raise RequestError("An unknown error occurred in your request.")

    def delete_alias(self, alias_name, index_name):
        """
        Delete the specified alias from ElasticSearch.
            alias_name      The alias name to delete
            index_name      The index that the alias points to
        """
        es = self.es_connection.get_connection()
        result = es.indices.delete_alias(
            index=index_name,
            name=alias_name
        )

        if result and result.get('acknowledged'):
            print "acknowledged: %s" % result['acknowledged']
        elif result.get('error'):
            print "error: %s" % result['error']
        else:
            raise RequestError("An unknown error occurred in your request.")

    def list_alias(self, index_name):
        """
        List the aliases defined on the ElasticSearch cluster.
        """
        es = self.es_connection.get_connection()
        if not index_name:
            result = es.indices.get_aliases()
        else:
            result = es.indices.get_aliases(index=index_name)

        # Print an error if one occurred
        if result.get('error'):
            print "error: %s" % result['error']
            return

        # Display results
        print json.dumps(result, sort_keys=True, indent=4, separators=(',',': '))

    def show_alias(self, alias_name):
        """
        Show the details about the specified alias.
            alias_name      The name of the alias to show
        """
        print "Not implemented."
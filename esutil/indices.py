import json

from connection import Connection

class Indices(object):
    """
    This class contains all the methods related to ElasticSearch index management.
    """

    def __init__(self, host_name, port_number):
        """
        Instantiate object with the following parameters:
            host_name       ElasticSearch host name
            port_number     ElasticsSearch API port number
        """
        self.es_connection = Connection(host_name, port_number)

    def create_index(self, index_name, shards, replicas):
        """
        Create an ElasticSearch index
            index_name      Name of index to be created
            shards          Number of shards for index
            replicas        Number of replicas for index
        """
        es = self.es_connection.get_connection()
        es.indices.create(
            index=index_name,
            body={
                'settings': {
                    'number_of_shards': shards,
                    'number_of_replicas' : replicas
                }
            },
            # Do not generate an error if index exists
            ignore=400
        )

    def delete_index(self, index_name):
        """
        Delete an ElasticSearch index
            index_name      Name of index to be deleted
        """
        es = self.es_connection.get_connection()
        es.indices.delete(index=index_name)

    def open_index(self, index_name):
        """
        Open a closed index in the ElasticSearch cluster
            index_name      Name of index to be opened
        """
        es = self.es_connection.get_connection()
        es.indices.open(index=index_name)

    def close_index(self, index_name):
        """
        Close an index on the ElasticSearch cluster
            index_name      Name of index to be closed
        """
        es = self.es_connection.get_connection()
        es.indices.close(index=index_name)

    def flush_index(self, index_name):
        """
        Flush all of the documents out of the target index
            index_name      Name of index to be flushed
        """
        es = self.es_connection.get_connection()
        es.indices.flush(index=index_name)



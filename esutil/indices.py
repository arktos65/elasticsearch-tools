import json
import elasticsearch
import argparse

from config import ES_HOST, ES_PORT, DEFAULT_REPLICAS, DEFAULT_SHARDS

class EsIndices(object):
    """
    This class manages ElasticSearch index creation, update, and deletion.  It provides a wrapper
    to the RESTful API.
    """

    def __init__(self, args):
        """
        Instantiated with the following keyword arguments:
            action          Action verb: create, update, delete
            index           Name of the ES index
            host            ES cluster host name
            port            ES cluster port number
            shards          Number of shards (available only for create)
            replicas        Number of replicas (available only for create and update)
        """


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



import sys
import json
import argparse

from connection import Connection
from config import ES_HOST, ES_PORT, DEFAULT_SHARDS, DEFAULT_REPLICAS
from indices import Indices

class EsUtil(object):
    """
    Shell utility class that parses command line arguments for managing ElasticSearch.
    """

    # Available actions
    OBJECT_ACTION_MAP = {'index': ['create', 'delete', 'update', 'flush', 'list', 'show', 'open', 'close'],
                         'alias': ['create', 'delete', 'list', 'show'],
                         'mapping': ['delete', 'list', 'show']}

    def __init__(self, args):
        """
        Instantiate with an argument parser.
        """
        self.object = args.object
        self.action = args.action
        self.target = args.target
        self.target_index = args.target_index
        self.host = args.host
        self.port = args.port
        self.shards = args.shards
        self.replicas = args.replicas
        self.es_connection = Connection(self.host, self.port)

    def execute(self):
        """
        Route the command to the appropriate command processor method in this class
        """
        if self.object == "index":
            self.index_command()

    def index_command(self):
        """
        Route index command to appropriate method in the Indices class
        """
        action = Indices(self.host, self.port)

        if self.action == "create":
            action.create_index(self.target, self.host, self. port)
        elif self.action == "delete":
            action.delete_index(self.target)
        elif self.action == "open":
            action.open_index(self.target)
        elif self.action == "close":
            action.close_index(self.target)
        elif self.action == "flush":
            action.flush_index(self.target)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='This utility provides a shell commandline wrapper to the ElasticSearch RESTful API, simplifying '
                    'index management.')

    # Declare the objects and actions
    parser.add_argument('object', choices=EsUtil.OBJECT_ACTION_MAP.keys(), required=True)
    parser.add_argument('action', choices=list(set(sum(EsUtil.OBJECT_ACTION_MAP.values(), []))), required=True)
    parser.add_argument('target', action='store', dest='target', required=True)
    parser.add_argument('target_index', action='store', dest='target_index')

    # Declare command line switches
    parser.add_argument('-h', '--host', action='store', dest='host', default=ES_HOST)
    parser.add_argument('-p', '--port', action='store', dest='port', type=int, default=ES_PORT)
    parser.add_argument('-s', '--shards', action='store', dest='shards', type=int, default=DEFAULT_SHARDS)
    parser.add_argument('-r', '--replicas', action='store', dest='replicas', type=int, default=DEFAULT_REPLICAS)

    # Parse the arguments and check for a match
    args = parser.parse_args()
    if args.action not in EsUtil.OBJECT_ACTION_MAP.get(args.object):
        parser.error("Object %s does not support action %s." % (args.object, args.action))

    # Now go for it
    esu = EsUtil(args)
    esu.execute()

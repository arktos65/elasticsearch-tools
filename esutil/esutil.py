import sys
import json
import argparse

from connection import Connection


from config import ES_HOST, ES_PORT, DEFAULT_SHARDS, DEFAULT_REPLICAS


class EsUtil(object):
    """
    Shell utility class that parses command line arguments for managing ElasticSearch.
    """

    # Available actions
    OBJECT_ACTION_MAP = {'index': ['create', 'update', 'delete', 'list', 'show'],
                         'alias': ['create', 'delete', 'list', 'show'],
                         'mapping': ['delete', 'list', 'show']}

    def __init__(self, args):
        """
        Instantiate with an argument parser.
        """
        self.object = args.object
        self.action = args.action
        self.target = args.target
        self.host = args.host
        self.port = args.port
        self.shards = args.shards
        self.replicas = args.replicas
        self.es_connection = Connection(self.host, self.port)

    def execute(self):
        """
        Route the command to the appropriate object
        """
        pass

    def create_index(self):
        """
        Create an ElasticSearch index
        """
        search = self.es_connection.get_connection()
        search.indices.create(
            index=self.target,
            body={
                'settings': {
                    'number_of_shards': self.shards,
                    'number_of_replicas' : self.replicas
                }
            },
            ignore=400
        )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='This utility provides a shell commandline wrapper to the ElasticSearch RESTful API, simplifying '
                    'index management.')

    # Declare the objects and actions
    parser.add_argument('object', choices=EsUtil.OBJECT_ACTION_MAP.keys())
    parser.add_argument('action', choices=list(set(sum(EsUtil.OBJECT_ACTION_MAP.values(), []))))
    parser.add_argument('target', action='store', dest='target')

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

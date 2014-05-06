import sys
import json
import argparse

from config import ES_HOST, ES_PORT, DEFAULT_SHARDS, DEFAULT_REPLICAS

class EsUtil(object):
    """
    Shell utility class that parses command line arguments for managing ElasticSearch.
    """

    # Available actions
    OBJECT_ACTION_MAP = {'index':['create', 'update', 'delete', 'list', 'show'],
                         'alias':['create', 'delete', 'list', 'show'],
                         'mapping':['delete', 'list', 'show']}

    def __init__(self, args):
        """
        Instantiate with an argument parser.
        """

        action = args.action
        parser = argparse.ArgumentParser(description='This utility provides a shell commandline wrapper to the ElasticSearch RESTful API, simplifying index management.')

        # Declare the objects and actions
        parser.add_argument('object', choices=EsUtil.OBJECT_ACTION_MAP.keys())
        parser.add_argument('action', choices=list(set(sum(EsUtil.OBJECT_ACTION_MAP.values(),[]))))

        # Declare command line switches
        parser.add_argument('-h', action='store', dest='host', default=ES_HOST)
        parser.add_argument('-p', action='store', dest='port', type=int, default=ES_PORT)
        parser.add_argument('-s', action='store', dest='shards', type=int, default=DEFAULT_SHARDS)
        parser.add_argument('-r', action='store', dest='replicas', type=int, default=DEFAULT_REPLICAS)

        # Parse the arguments and check for a match
        args = parser.parse_args()
        if args.action not in EsUtil.OBJECT_ACTION_MAP.get(args.object):
            parser.error("Object %s does not support action %s." % (args.object, args.action))

        # Now go for it
        esu = EsUtil(args)

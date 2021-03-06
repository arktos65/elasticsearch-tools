#!/usr/bin/env python

# Copyright (c) 2014 Pulselocker, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import argparse

from lib.aliases import Aliases
from lib.cluster import Cluster
from lib.indices import Indices
from lib.mapping import Mapping
from lib.connection import Connection

from config import ES_HOST, ES_PORT, DEFAULT_SHARDS, DEFAULT_REPLICAS

class EsUtil(object):
    """
    Shell utility class that parses command line arguments for managing ElasticSearch.
    """

    # Available actions
    OBJECT_ACTION_MAP = {'index': ['create', 'delete', 'flush', 'list', 'open', 'close'],
                         'alias': ['create', 'delete', 'list'],
                         'mapping': ['list', 'show'],
                         'cluster': ['health', 'state'],
                         'stats': ['show']}

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
        elif self.object == "alias":
            self.alias_command()
        elif self.object == "cluster":
            self.cluster_command()
        elif self.object == "mapping":
            self.mapping_command()
        elif self.object == "stats":
            self.stats_command()

    def index_command(self):
        """
        Route index command to appropriate method in the Indices class
        """
        action = Indices(self.host, self.port)

        if self.action == "create":
            action.create_index(self.target, self.shards, self.replicas)
        elif self.action == "delete":
            action.delete_index(self.target)
        elif self.action == "open":
            action.open_index(self.target)
        elif self.action == "close":
            action.close_index(self.target)
        elif self.action == "flush":
            action.flush_index(self.target)
        elif self.action == "list":
            action.list_index(self.target)

    def alias_command(self):
        """
        Route alias command to appropriate method in the Aliases class
        """
        action = Aliases(self.host, self.port)

        if self.action == "create":
            action.create_alias(self.target, self.target_index)
        elif self.action == "delete":
            action.delete_alias(self.target, self.target_index)
        elif self.action == "list":
            action.list_alias(self.target_index)

    def cluster_command(self):
        """
        Route cluster command to appropriate method in Cluster class
        """
        action = Cluster(self.host, self.port)

        if self.action == "health":
            action.cluster_health(self.target_index)

    def mapping_command(self):
        """
        Route mapping command to appropriate method in the Mapping class
        """
        action = Mapping(self.host, self.port)

        if self.action == "list":
            action.list_mapping(self.target_index)

    def stats_command(self):
        """
        Show performance metrics of ElasticSearch cluster
        """

        action = Indices(self.host, self.port)

        if self.action == "show":
            action.show_stats(self.target_index)

# Parse the arguments before instantiating the object class
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='This utility provides a shell commandline wrapper to the ElasticSearch RESTful API, simplifying '
                    'index management.')

    # Declare the objects and actions
    parser.add_argument('object', choices=EsUtil.OBJECT_ACTION_MAP.keys())
    parser.add_argument('action', choices=list(set(sum(EsUtil.OBJECT_ACTION_MAP.values(), []))))
    parser.add_argument('target', action='store', nargs="?", default="_all")

    # Declare command line switches
    parser.add_argument('-H', '--host', action='store', dest='host', default=ES_HOST)
    parser.add_argument('-P', '--port', action='store', dest='port', type=int, default=ES_PORT)
    parser.add_argument('-s', '--shards', action='store', dest='shards', type=int, default=DEFAULT_SHARDS)
    parser.add_argument('-r', '--replicas', action='store', dest='replicas', type=int, default=DEFAULT_REPLICAS)
    parser.add_argument('-i', '--index', action='store', dest='target_index', default="_all")
    parser.add_argument('-f', '--field', action='store', dest='field', default="_all")

    # Parse the arguments and check for a match
    args = parser.parse_args()
    if args.action not in EsUtil.OBJECT_ACTION_MAP.get(args.object):
        parser.error("Object %s does not support action %s." % (args.object, args.action))

    # Now go for it
    esu = EsUtil(args)
    esu.execute()

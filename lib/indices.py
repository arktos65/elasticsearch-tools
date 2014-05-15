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

from lib.connection import Connection
from lib.result import acknowledge_result

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
        result = es.indices.create(
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

        # Display error if there is one
        acknowledge_result(result)


    def delete_index(self, index_name):
        """
        Delete an ElasticSearch index
            index_name      Name of index to be deleted
        """
        es = self.es_connection.get_connection()
        result = es.indices.delete(index=index_name)

        # Display error if there is one
        acknowledge_result(result)

    def open_index(self, index_name):
        """
        Open a closed index in the ElasticSearch cluster
            index_name      Name of index to be opened
        """
        es = self.es_connection.get_connection()
        result = es.indices.open(index=index_name)

        # Display error if there is one
        acknowledge_result(result)

    def close_index(self, index_name):
        """
        Close an index on the ElasticSearch cluster
            index_name      Name of index to be closed
        """
        es = self.es_connection.get_connection()
        result = es.indices.close(index=index_name)

        # Print an error if one occurred
        acknowledge_result(result)

    def flush_index(self, index_name):
        """
        Flush all of the documents out of the target index
            index_name      Name of index to be flushed
        """
        es = self.es_connection.get_connection()
        result = es.indices.flush(index=index_name)

        # Print an error if one occurred
        acknowledge_result(result)

    def list_index(self, index_name):
        """
        Display a list of indices in the ElasticSearch cluster.
            index_name      Name of index to list (default is _all)
        """
        es = self.es_connection.get_connection()
        result = es.indices.get_settings(index=index_name)

        # Print an error if one occurred
        acknowledge_result(result)


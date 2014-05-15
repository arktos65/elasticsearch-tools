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

        # Display error if there is one
        acknowledge_result(result)

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

        # Display error if there is one
        acknowledge_result(result)

    def list_alias(self, index_name):
        """
        List the aliases defined on the ElasticSearch cluster.
            index_name      Name of index to list aliases (default is _all)
        """
        es = self.es_connection.get_connection()
        if not index_name:
            result = es.indices.get_aliases()
        else:
            result = es.indices.get_aliases(index=index_name)

        # Print an error if one occurred
        acknowledge_result(result)

    def show_alias(self, alias_name):
        """
        Show the details about the specified alias.
            alias_name      The name of the alias to show
        """
        print "Not implemented."
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

class Mapping(object):
    """
    Provide functions for managing index mappings on an ElasticSearch cluster.
    """

    def __init__(self, host_name, port_number):
        """
        Instantiate object with the following parameters:
            host_name       ElasticSearch host name
            port_number     ElasticsSearch API port number
        """
        self.es_connection = Connection(host_name, port_number)

    def list_mapping(self, index_name):
        """
        Show the mappings for a specified index.
            index_name      Index to display mappings.
        """

        es = self.es_connection.get_connection()
        result = es.indices.get_mapping(index=index_name)

        # Display error if there is one
        acknowledge_result(result)

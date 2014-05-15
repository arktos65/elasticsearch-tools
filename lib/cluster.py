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

class Cluster(object):
    """
    This class provides access to ElasticSearch cluster management features.
    """

    def __init__(self, host_name, port_number):
        """
        Instantiate object with the following parameters:
            host_name       ElasticSearch host name
            port_number     ElasticsSearch API port number
        """
        self.es_connection = Connection(host_name, port_number)

    def cluster_health(self, index_name):
        """
        Display basic cluster health information, or if index is specified, of that index.
            index_name      Index to get health status on
        """
        es = self.es_connection.get_connection()
        if index_name == "_all":
            result = es.cluster.health()
        else:
            result = es.cluster.health(index=index_name)

        # Print an error if one occurred
        acknowledge_result(result)
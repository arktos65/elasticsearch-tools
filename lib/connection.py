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

from elasticsearch import Elasticsearch

class Connection(object):
    """
    Creates and returns an ElasticSearch connection object.
    """

    def __init__(self, host_name, port_num):
        """
        Instantiate the ElasticSearch connection object.
            host_name       Host name of an ElasticSearch node
            port_number     Port number of the ElasticSearch API on node
        """
        self.es_host = "%s:%s" % (host_name, port_num)

    def get_connection(self):
        """
        Returns an ElasticSearch connection object.
        """
        return Elasticsearch(self.es_host)

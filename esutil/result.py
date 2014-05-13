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

import json

from elasticsearch import RequestError

def acknowledge_result(results):
    """
    Interpret a result from an ElasticSearch API call and display it.
        result          Dictionary object from ElasticSearch API

    Returns
        error_status    Boolean value indicating if result was an error or not.
    """

    error_status = True

    if results and results.get('acknowledged'):
        print "acknowledged: %s" % results['acknowledged']
        error_status = False
    elif results and results.get('error'):
        print "error: %s" % results['error']
    elif not results:
        raise RequestError("An unknown error occurred in your request.")
    else:
        print json.dumps(results, sort_keys=True, indent=4, separators=(',',': '))

    return error_status
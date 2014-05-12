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
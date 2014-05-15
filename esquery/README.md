ESQUERY Release Notes
====================

This utility provides a shell command line wrapper to the ElasticSearch RESTful API for simple queries.

Prequisites
-----------

The following prerequisites must be met:

#### Python Packages

Python 2.7, ElasticSearch 0.90+

- `elasticsearch` - ElasticSearch client API for Python.  (`pip install elasticsearch`)
- `argparse` - Library for argument parsing. (`pip install argparse`)

Usage
-----

The utility can be used from any non-privileged account.  The syntax is:

    $ esquery -i [indices] -q [query] -H <host> -P <port>

#### Objects and Actions

- `index` - Interact with ElasticSearch indices.  Actions: create, update, delete, open, close, flush
- `alias` - Interact with ElasticSearch index aliases.  Actions:  create, delete
- `mapping` - Interact with ElasticSearch index mappings.  Actions: list, delete
- `cluster` - ElasticSearch management features.  Actions: health, state

#### Switches

- `-H or --host` - Specify the host name of the ElasticSearch cluster.  Default: localhost
- `-P or --port` - Specify the port number of the ElasticSearch cluster API.  Default: 9200
- `-i or --index` - Specify a target index to perform operation on.
- `-q or --query` - Specify the query to be executed against index.
- `--help` - Display usage information.


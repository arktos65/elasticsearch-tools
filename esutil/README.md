ESUTIL Release Notes
====================

This utility provides a shell command line wrapper to the ElasticSearch RESTful API simplifying index management.

Prequisites
-----------

The following prerequisites must be met:

#### Python Packages

- `elasticsearch` - ElasticSearch client API for Python.  (`pip install elasticsearch`)

Usage
-----

The utility can be used from any non-privileged account.  The syntax is:

    $ esutil <object> <action> [switches]

#### Objects and Actions

- `index` - Interact with ElasticSearch indices.  Actions: create, update, delete
- `alias` - Interact with ElasticSearch index aliases.  Actions:  create, delete
- `mapping` - Interact with ElasticSearch index mappings.  Actions: list, delete

#### Switches

- `-h or --host` - Specify the host name of the ElasticSearch cluster.  Default: localhost
- `-p or --port` - Specify the port number of the ElasticSearch cluster API.  Default: 9200
- `--help` - Display usage information.


ESUTIL Release Notes
====================

This utility provides a shell command line wrapper to the ElasticSearch RESTful API simplifying index management.

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

    $ esutil <object> <action> <target> [switches]

#### Objects and Actions

- `index` - Interact with ElasticSearch indices.  Actions: create, update, delete, open, close, flush
- `alias` - Interact with ElasticSearch index aliases.  Actions:  create, delete
- `mapping` - Interact with ElasticSearch index mappings.  Actions: list, delete

#### Switches

- `-h or --host` - Specify the host name of the ElasticSearch cluster.  Default: localhost
- `-p or --port` - Specify the port number of the ElasticSearch cluster API.  Default: 9200
- `-s or --shards` - Specify the number of shards to create.  Default: 5
- `-r or --replicas` - Specify the number of replicas to create.  Default: 1
- `-i or --index` - Specify a target index to perform operation on.
- `--help` - Display usage information.

#### Examples

Create an index with 2 shards and 0 replicas:

    $ esutil index create test_index -s 2 -r 0

Create an alias:

    $ esutil alias create test_alias test_index

List all indices in cluster:

    $ esutil index list



ElasticSearch-Tools
===================

A variety of tools for making managing ElasticSearch a bit easier.


This utility provides a shell command line wrapper to the ElasticSearch RESTful API simplifying index management.

Prequisites
-----------

The following prerequisites must be met:

#### Python Packages

Python 2.7, ElasticSearch 0.90+

- `elasticsearch` - ElasticSearch client API for Python.  (`pip install elasticsearch`)
- `argparse` - Library for argument parsing. (`pip install argparse`)

ESUTIL Usage
------------
The utility can be used from any non-privileged account.  The syntax is:

    $ esutil <object> <action> <target> [switches]

#### Objects and Actions

- `index` - Interact with ElasticSearch indices.  Actions: create, update, delete, open, close, flush
- `alias` - Interact with ElasticSearch index aliases.  Actions:  create, delete
- `mapping` - Interact with ElasticSearch index mappings.  Actions: list, delete
- `cluster` - ElasticSearch management features.  Actions: health, state
- `stats` - ElasticSearch performance metrics.  Actions: show

#### Switches

- `-h or --host` - Specify the host name of the ElasticSearch cluster.  Default: localhost
- `-p or --port` - Specify the port number of the ElasticSearch cluster API.  Default: 9200
- `-s or --shards` - Specify the number of shards to create.  Default: 5
- `-r or --replicas` - Specify the number of replicas to create.  Default: 1
- `-i or --index` - Specify a target index to perform operation on.
- `-f or --field` - Specify a field to perform operation on.
- `--help` - Display usage information.

#### Examples

Create an index with 2 shards and 0 replicas:

    $ esutil index create test_index -s 2 -r 0

Create an alias:

    $ esutil alias create test_alias test_index

List all indices in cluster:

    $ esutil index list

ESQUERY Usage
-------------
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




Authors & License
-----------------
Author: Sean M. Sullivan (<sean@pulselocker.com>)
Contributor: Mike McConnell (<mikem@pulselocker.com>)

```text
Copyright:: 2014 Pulselocker, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```





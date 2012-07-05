This repo contains some simple tools to help extract data and metadata from relational databases for use in Veritable.

# Installation

    $ git clone https://github.com/priorknowledge/db_tools.git
    $ cd db_tools
    $ python setup.py install

# Usage

    $ veritable-db-tools extract-schema <db uri> <table name>

More complete usage info can be obtained with:

    $ vertiable-db-tools extract-schema -h
    
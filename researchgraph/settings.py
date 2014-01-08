#!/usr/bin/env python
# -*- coding: utf-8 -*-
_default_dbservice = "http://localhost:7474/db/data/"

def add_arguments(parser):
    parser.add_argument("-d", "--database", metavar='URL',
        default=_default_dbservice,
        help="Neo4J database address, like http://localhost:7474/db/data/ (include the trailing slash!)")
    return parser

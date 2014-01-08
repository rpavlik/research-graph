#!/usr/bin/env python
# -*- coding: utf-8 -*-

def connect(args):
    from py2neo import neo4j
    return neo4j.GraphDatabaseService(args.database)

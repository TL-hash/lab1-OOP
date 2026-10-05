#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def search_by_destination(trains, destination):
    found = []
    for train in trains:
        if train['destination'].lower() == destination.lower():
            found.append(train)
    return found
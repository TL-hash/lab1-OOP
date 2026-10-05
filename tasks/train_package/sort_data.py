#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def sort_trains(trains):
    return sorted(trains, key=lambda train: train['departure_time'])
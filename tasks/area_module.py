#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_area_function(type=0):
    def triangle_area(base, height):
        return 0.5 * base * height

    def rectangle_area(length, width):
        return length * width

    if type == 0:
        return triangle_area
    else:
        return rectangle_area

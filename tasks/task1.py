#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import area_module


def main():
    triangle_func = area_module.get_area_function()
    print(f"Площадь треугольника: {triangle_func(6, 4)}")

    rectangle_func = area_module.get_area_function(type=1)
    print(f"Площадь прямоугольника: {rectangle_func(5, 3)}")


if __name__ == '__main__':
    main()
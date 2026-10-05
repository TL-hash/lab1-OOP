#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def display_trains(trains):
    if not trains:
        print("Нет поездов для отображения.")
        return

    print("\n{:<20} {:<15} {:<15}".format("Пункт назначения", "Номер поезда", "Время отправления"))
    print("-" * 50)
    for train in trains:
        print("{:<20} {:<15} {:<15}".format(
            train['destination'],
            train['train_number'],
            train['departure_time']
        ))
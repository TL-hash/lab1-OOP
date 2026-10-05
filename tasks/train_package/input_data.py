#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def input_trains():
    trains = []
    n = int(input("Введите количество поездов: "))

    for i in range(n):
        print(f"\nПоезд №{i + 1}:")
        destination = input("  Пункт назначения: ").strip()
        train_number = input("  Номер поезда: ").strip()
        departure_time = input("  Время отправления (ЧЧ:ММ): ").strip()

        train = {
            'destination': destination,
            'train_number': train_number,
            'departure_time': departure_time
        }
        trains.append(train)

    return trains
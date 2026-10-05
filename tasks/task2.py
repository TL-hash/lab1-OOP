#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import train_package as tp


def main():
    print("Ввод данных о поездах")
    trains = tp.input_trains()

    trains = tp.sort_trains(trains)
    print("\nПоезда, отсортированные по времени отправления")
    tp.display_trains(trains)

    destination = input("\nВведите пункт назначения для поиска: ").strip()
    found = tp.search_by_destination(trains, destination)

    if found:
        print(f"\nПоезда, направляющиеся в пункт '{destination}'")
        tp.display_trains(found)
    else:
        print(f"\nПоездов, направляющихся в пункт '{destination}', не найдено.")


if __name__ == '__main__':
    main()
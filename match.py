# -*- coding: utf-8 -*-
"""Lunch picker
"""

import json


def main():
    """main() reads two files from the current path - users.json adn venues.json
    it uses them to generate suitable venues list and output it into stdout

    """
    with open('./users.json') as f:
        users = json.load(f)

    with open('./venues.json') as f:
        venues = json.load(f)

    for venue in venues:
        food_venue = set(venue["food"])
        drink_venue = set(venue["drinks"])

        venue["picky_eaters"] = []
        venue["picky_drinkers"] = []

        for user in users:
            food_user = set(user["wont_eat"])
            drink_user = set(user["drinks"])

            if len(food_venue - food_user) == 0:
                venue["picky_eaters"].append(user["name"])

            if len(drink_venue & drink_user) == 0:
                venue["picky_drinkers"].append(user["name"])

    print("\n Places to go:")
    for venue in venues:
        if venue["picky_eaters"] or venue["picky_drinkers"]:
            continue
        print(f"* {venue['name']}")

    print("\n Places to avoid:")
    for venue in venues:
        if venue["picky_eaters"] or venue["picky_drinkers"]:
            print(f"* {venue['name']}")
        for eater in venue["picky_eaters"]:
            print(f"\t * There's nothing for {eater} to eat")
        for drinker in venue["picky_drinkers"]:
            print(f"\t * There's nothing for {drinker} to drink")


if __name__ == "__main__":
    main()

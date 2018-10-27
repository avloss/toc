# -*- coding: utf-8 -*-
"""Lunch picker
"""

import json


def vet_venues(venues, users):
    for venue in venues:
        food_venue = set([s.lower() for s in venue["food"]])
        drink_venue = set([s.lower() for s in venue["drinks"]])

        venue["picky_eaters"] = []
        venue["picky_drinkers"] = []

        for user in users:
            food_user = set([s.lower() for s in user["wont_eat"]])
            drink_user = set([s.lower() for s in user["drinks"]])

            if len(food_venue - food_user) == 0:
                venue["picky_eaters"].append(user["name"])

            if len(drink_venue & drink_user) == 0:
                venue["picky_drinkers"].append(user["name"])
    return venues


def test_main():
    users = [
        {
            "name": "John Davis",
            "wont_eat": ["Fish", "Chinese"],
            "drinks": ["Cider", "Rum", "Soft drinks"]
        },
        {
            "name": "Gary Jones",
            "wont_eat": ["Eggs", "Pasta"],
            "drinks": ["Tequila", "Coffee"]
        }
    ]

    venues = [
        {
            "name": "El Cantina",
            "food": ["Mexican"],
            "drinks": ["Soft drinks", "Tequila", "Beer"]
        },
        {
            "name": "Twin Dynasty",
            "food": ["Chinese"],
            "drinks": ["Soft Drinks", "Rum", "Beer", "Whisky", "Cider"]
        }
    ]

    venues = vet_venues(venues, users)

    assert venues == [{'drinks': ['Soft drinks', 'Tequila', 'Beer'],
                       'food': ['Mexican'],
                       'name': 'El Cantina',
                       'picky_drinkers': [],
                       'picky_eaters': []},
                      {'drinks': ['Soft Drinks', 'Rum', 'Beer', 'Whisky', 'Cider'],
                       'food': ['Chinese'],
                       'name': 'Twin Dynasty',
                       'picky_drinkers': ['Gary Jones'],
                       'picky_eaters': ['John Davis']}]


def main():
    """main() reads two files from the current path - users.json adn venues.json
    it uses them to generate suitable venues list and output it into stdout

    """
    with open('./users.json') as f:
        users = json.load(f)

    with open('./venues.json') as f:
        venues = json.load(f)

    venues = vet_venues(venues, users)

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

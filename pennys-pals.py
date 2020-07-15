#!/usr/bin/env python

# This program greets you especially if you're one of Penny's Pals!
# i.e. if you respond with a name of one of Penny's pals.
# TODO I.E. vs E.G.

import sys


def main():

    friends = [
        {
            "name": "Penny",
            "prefix": "Miss",
            "color": "Purple",
            "species": "Penguin"
        },
        {
            "name": "Sammy",
            "color": "Gray",
            "species": "Seal"
        },
        {
            "name": "Sonny",
            "prefix": "Mr.",
            "color": "Silver",
            "species": "Snowman"
        }
    ]

    names = []
    for friend in friends:
        names.append(friend['name'])

    def greet(name):
        if name in names:
            for friend in friends:
                if answer == friend['name']:
                    if friend.get("prefix"):
                        print(
                            f"*** Hello {friend['prefix']} {friend['name']} the {friend['color']} {friend['species']}!!! ***")
                    else:
                        print(
                            f"*** Hello {friend['name']} the {friend['color']} {friend['species']}!!! ***"
                        )
        else:
            print(f"Hello {answer}!")

    prompt = "Hello! What's your name!\n"
    answer = input(prompt)
    greet(answer)

    sys.exit()


if __name__ == "__main__":
    main()

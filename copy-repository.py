#!/usr/bin/env python

# System
import argparse

# Local
from git_sync import copy_repository


# Setup arguments
parser = argparse.ArgumentParser()
parser.add_argument(
    "origin",
    help="A git URL for the origin repository to synchronise from"
)
parser.add_argument(
    "destination",
    help="A git URL for the mirror repository to synchronise to"
)

if __name__ == "__main__":
    arguments = parser.parse_args()
    copy_repository(
        origin=arguments.origin,
        destination=arguments.destination
    )

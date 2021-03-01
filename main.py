#!/usr/bin/env python3

import argparse

from lib.config import Config

def main(args):
    configuration = Config(args.config)
    state = State(configuration)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", "-c",
                        help="Config file",
                        required=True)
    args = parser.parse_args()
    main(args)
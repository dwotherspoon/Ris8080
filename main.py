#!/usr/bin/env python3

import argparse

from lib.config import Config
from lib.state import State
from lib.generator import StreamGenerator

def main(args):
    config = Config(args.config)
    state = State(config)
    StreamGenerator(state)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", "-c",
                        help="Config file",
                        required=True)
    args = parser.parse_args()
    main(args)
#!/usr/bin/env python3
'''combine.py <first_array> <second_array>

returns a combined and sorted array from two arrays

  first_array    json formatted array of numbers
  second_array   json formatted array of numbers
'''
import sys
import json
from typing import List, Union


def parse(arg: str):
    '''parses shell argument and returns a list of numbers
    '''
    try:
        parsed = json.loads(arg)
    except json.JSONDecodeError:
        raise TypeError(f'unable to parse argument: {arg}')

    if not isinstance(parsed, list):
        raise TypeError(f'{arg} must be an array')

    if any([not isinstance(_, (float, int)) for _ in parsed]):
        raise TypeError(f'{arg} must only contain numbers')

    return parsed


def format_output(item: List[Union[float, int]]):
    '''formats and returns a lit of numbers as a string
    '''
    return json.dumps(item)


def combine(item_a: List[Union[float, int]], item_b: List[Union[float, int]]):
    '''returns a combined and sorted array from two lists
    '''
    return sorted(item_a + item_b)


def main(args: List[str]):
    '''main script
    '''
    try:
        if len(args) != 3:
            raise RuntimeError(
                f'requires 2 arguments but {len(args)} were given')

        print(format_output(combine(parse(args[1]), parse(args[2]))))

    except (TypeError, RuntimeError) as error:
        print(str(error))
        print(__doc__)
        sys.exit(1)


if __name__ == '__main__':
    main(sys.argv)

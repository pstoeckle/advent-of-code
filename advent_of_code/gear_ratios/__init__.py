# SPDX-FileCopyrightText: 2023 Patrick Stoeckle
#
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path
from string import digits
from typing import MutableMapping, MutableSet, Optional, Sequence, Tuple
from math import prod


def solve_puzzle(t_file: Path) -> int:
    """
    Reads puzzle and returns the sum of gears.
    """
    lines = [list(line) for line in t_file.read_text().splitlines()]
    numbers = []
    for i, line in enumerate(lines):
        for j, _ in enumerate(line):
            if lines[i][j] in digits:
                symbol_adje = False
                n = j
                while line[n] in digits:
                    symbol_adje = symbol_adje | symbol_next_to_field(i, n, lines)
                    n += 1
                    if n == len(line):
                        break
                current_number = int("".join(line[j:n]))
                if symbol_adje:
                    print(f"Adding {current_number}")
                    numbers.append(current_number)
                else:
                    print(f"We will ignore {current_number}")
                for k in range(j, n):
                    line[k] = "."

    all_sum = sum(numbers)
    print(f"The overall sum is {all_sum}")
    return all_sum


def part_two(t_file: Path) -> int:
    """
    Reads puzzle and returns the sum of gears.
    """
    lines = [list(line) for line in t_file.read_text().splitlines()]
    gears_to_numbers: MutableMapping[Tuple[int, int], MutableSet[int]] = {}
    numbers = []
    for i, line in enumerate(lines):
        for j, _ in enumerate(line):
            if lines[i][j] in digits:
                n = j
                gear = None
                while line[n] in digits:
                    gear_near = next_gear(i, n, lines)
                    if gear_near is not None:
                        if gear is not None and gear != gear_near:
                            raise ValueError("Two gears ...")
                        gear = gear_near
                    n += 1
                    if n == len(line):
                        break
                current_number = int("".join(line[j:n]))
                if gear is not None:
                    print(f"Adding {current_number}")
                    if gears_to_numbers.get(gear) is None:
                        gears_to_numbers[gear] = set()
                    gears_to_numbers[gear].add(current_number)
                else:
                    print(f"We will ignore {current_number}")
                for k in range(j, n):
                    line[k] = "."

    gear_ratio = sum(
        prod(values) for gear, values in gears_to_numbers.items() if len(values) == 2
    )
    print(f"The gear ratio is {gear_ratio}")
    return gear_ratio


def next_gear(
    x: int, y: int, lines: Sequence[Sequence[str]]
) -> Optional[Tuple[int, int]]:
    # Links oben
    if x - 1 >= 0 and y - 1 >= 0 and lines[x - 1][y - 1] == "*":
        return (x - 1, y - 1)

    # Links unten
    if x - 1 >= 0 and y + 1 < len(lines[x]) and lines[x - 1][y + 1] == "*":
        return (x - 1, y + 1)

    # Rechts oben
    if x + 1 < len(lines) and y - 1 >= 0 and lines[x + 1][y - 1] == "*":
        return (x + 1, y - 1)

    # Rechts unten
    if x + 1 < len(lines) and y + 1 < len(lines[x]) and lines[x + 1][y + 1] == "*":
        return (x + 1, y + 1)

    # Oben
    if x - 1 >= 0 and lines[x - 1][y] == "*":
        return (x - 1, y)
    # Unten
    if x + 1 < len(lines) and lines[x + 1][y] == "*":
        return (x + 1, y)

    # Links
    if y - 1 >= 0 and lines[x][y - 1] == "*":
        return (x, y - 1)

    # Rechts
    if y + 1 < len(lines[x]) and lines[x][y + 1] == "*":
        return (x, y + 1)
    return None


def symbol_next_to_field(x: int, y: int, lines: Sequence[Sequence[str]]) -> bool:
    # Links oben
    if (
        x - 1 >= 0
        and y - 1 >= 0
        and lines[x - 1][y - 1] not in digits
        and lines[x - 1][y - 1] != "."
    ):
        return True

    # Links unten
    if (
        x - 1 >= 0
        and y + 1 < len(lines[x])
        and lines[x - 1][y + 1] not in digits
        and lines[x - 1][y + 1] != "."
    ):
        return True

    # Rechts oben
    if (
        x + 1 < len(lines)
        and y - 1 >= 0
        and lines[x + 1][y - 1] not in digits
        and lines[x + 1][y - 1] != "."
    ):
        return True

    # Rechts unten
    if (
        x + 1 < len(lines)
        and y + 1 < len(lines[x])
        and lines[x + 1][y + 1] not in digits
        and lines[x + 1][y + 1] != "."
    ):
        return True

    # Oben
    if x - 1 >= 0 and lines[x - 1][y] not in digits and lines[x - 1][y] != ".":
        return True
    # Unten
    if x + 1 < len(lines) and lines[x + 1][y] not in digits and lines[x + 1][y] != ".":
        return True

    # Links
    if y - 1 >= 0 and lines[x][y - 1] not in digits and lines[x][y - 1] != ".":
        return True

    # Rechts
    if (
        y + 1 < len(lines[x])
        and lines[x][y + 1] not in digits
        and lines[x][y + 1] != "."
    ):
        return True
    return False


if "__main__" == __name__:
    solve_puzzle(Path("tests/rsc/real.txt"))
    part_two(Path("tests/rsc/real.txt"))

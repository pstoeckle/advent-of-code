# SPDX-FileCopyrightText: 2023 2023 Patrick Stoeckle
#
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path
from string import digits
from typing import Sequence


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
    solve_puzzle(Path("real.txt"))

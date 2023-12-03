from unittest import TestCase
from pathlib import Path
from advent_of_code.gear_ratios import solve_puzzle


class QuizTest(TestCase):
    def test_normal(self) -> None:
        self.assertEqual(solve_puzzle(Path("tests") / "rsc" / "t.txt"), 4361)

    def test_normal_with_number_at_the_end(self) -> None:
        self.assertEqual(solve_puzzle(Path("tests") / "rsc" / "t_with_end.txt"), 4361)

    def test_real(self) -> None:
        self.assertEqual(solve_puzzle(Path("tests") / "rsc" / "real.txt"), 533775)

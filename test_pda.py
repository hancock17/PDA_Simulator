import unittest

from pda import PDASimulator


class PDASimulatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.pda = PDASimulator()

    def test_accepts_valid_strings(self) -> None:
        for value in ("", "ab", "aabb", "aaabbb"):
            with self.subTest(value=value):
                self.assertTrue(self.pda.process(value))

    def test_rejects_unbalanced_or_out_of_order_strings(self) -> None:
        for value in ("a", "b", "aab", "abb", "bbaa", "aba"):
            with self.subTest(value=value):
                self.assertFalse(self.pda.process(value))

    def test_rejects_invalid_symbols_with_reason(self) -> None:
        result = self.pda.simulate("a1b")

        self.assertFalse(result.accepted)
        self.assertIn("invalid symbol", result.reason)


if __name__ == "__main__":
    unittest.main()

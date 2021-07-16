import unittest
import japanese_parser


class TestJapaneseParser(unittest.TestCase):
    def test_sentence_parser(self):
        input_sentence = "カレーが好きです。"

        output = japanese_parser.get_words_from_sentence(input_sentence)
        expected = ["カレー", "が", "好き", "です"]
        self.assertListEqual(sorted(output), sorted(expected))

    def test_half_width_parantheses_removed(self):
        input_sentence = "(カレー)が好きです。"
        output = japanese_parser.get_words_from_sentence(input_sentence)
        expected = ["カレー", "が", "好き", "です"]
        self.assertListEqual(sorted(output), sorted(expected))

    def test_full_width_parantheses_removed(self):
        input_sentence = "（カレー）が好きです。"
        output = japanese_parser.get_words_from_sentence(input_sentence)
        expected = ["カレー", "が", "好き", "です"]
        self.assertListEqual(sorted(output), sorted(expected))

    def test_only_extract_unique_words(self):
        input_sentence = "カレーが好きです　カレーが好きです"
        output = japanese_parser.get_words_from_sentence(input_sentence)
        expected = ["カレー", "が", "好き", "です"]
        self.assertListEqual(sorted(output), sorted(expected))


if __name__ == "__main__":
    unittest.main()

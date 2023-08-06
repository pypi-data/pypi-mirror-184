import unittest

from promptware.utils.py_util import generate_format_func


class TestPYUtils(unittest.TestCase):
    def test_generate_format_func(self):

        # convert a string to lambda function
        pattern = "[Query]:{query}\n[Documents]:{documents}\n[URL]:{url}"

        # f = lambda input: f"{input['query']} {input['documents']} {input['url']}"
        f = generate_format_func(pattern)

        input = {"query": "query", "documents": "documents", "url": "url"}
        print(f(input))

        self.assertEqual(f(input), "[Query]:query\n[Documents]:documents\n[URL]:url")

    def test_generate_format_func_no_bracket(self):

        pattern = "Input:"
        f = generate_format_func(pattern)
        input = "I love this movie"
        self.assertEqual(f(input), input)


if __name__ == "__main__":
    unittest.main()

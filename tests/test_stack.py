import unittest
from src.stack import Stack, Node


class TestStack(unittest.TestCase):

    """
    Тесты для класса Stack
    """

    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        assert self.stack.size == 0
        self.stack.push(10)
        assert self.stack.size == 1
        assert self.stack.top.data == 10

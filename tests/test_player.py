import unittest
from unittest.mock import patch
from source.player import player_pon
class TestPlayerPon(unittest.TestCase):
    @patch('builtins.input', side_effect = '1')
    def test_input_1_returns_goo(self, mock_input):
        gu = player_pon()
        self.assertEqual(gu, 'グー')
        
    @patch('builtins.input', side_effect = '2')
    def test_input_2_returns_choki(self, mock_input):
        tyoki = player_pon()
        self.assertEqual(tyoki, 'チョキ')
        
    @patch('builtins.input', side_effect = '3')
    def test_input_3_returns_paa(self, mock_input):
        pa = player_pon()
        self.assertEqual(pa, 'パー')
        
    @patch('builtins.input', side_effect = ['0', '4', '1'])
    def test_invalid_input_then_valid_input(self, mock_input):
        bug = player_pon()
        self.assertEqual(bug, 'グー')
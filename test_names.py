import unittest
import names


class TestNames(unittest.TestCase):

    def test_get_first_female_names_len(self):
        first_female_names = names.Names.get_first_female_names()
        self.assertEqual(len(first_female_names), 4273)

    def test_get_first_female_names(self):
        first_female_names = names.Names.get_first_female_names()
        self.assertTrue('Kathy'.upper() in first_female_names)
        self.assertFalse('Harvey'.upper() in first_female_names)

    def test_get_last_names_2010_len(self):
        last_names = names.Names.get_last_names_2010()
        self.assertEqual(len(last_names), 1000)

    def test_get_last_names_2010(self):
        last_names = names.Names.get_last_names_2010()
        self.assertTrue('Smith'.upper() in last_names)
        self.assertFalse('Mxyzptlk'.upper() in last_names)


if __name__ == '__main__':
    unittest.main()

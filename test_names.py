import unittest
import names


class TestNames(unittest.TestCase):

    # test first female

    def test_get_first_female_names_len(self):
        first_female_names = names.get_first_female_names()
        self.assertEqual(len(first_female_names), 4274)

    def test_get_first_female_names_gets_name_row0(self):
        first_female_names = names.get_first_female_names()
        self.assertTrue('Mary'.upper() in first_female_names)

    def test_get_first_female_names(self):
        first_female_names = names.get_first_female_names()
        self.assertTrue('Kathy'.upper() in first_female_names)
        self.assertFalse('Harvey'.upper() in first_female_names)

    # test last names 1990

    def test_get_last_names_1990_len(self):
        last_names = names.get_last_names_1990()
        self.assertEqual(len(last_names), 88797)

    def test_get_last_names_1990_gets_name_row0(self):
        last_names = names.get_last_names_1990()
        self.assertTrue('Smith'.upper() in last_names)

    def test_get_last_names_1990(self):
        last_names = names.get_last_names_1990()
        self.assertFalse('Mxyzptlk'.upper() in last_names)

    # test last names 2010

    def test_get_last_names_2010_len(self):
        last_names = names.get_last_names_2010()
        self.assertEqual(len(last_names), 1000)

    def test_get_last_names_2010_gets_name_row0(self):
        last_names = names.get_last_names_2010()
        self.assertTrue('Smith'.upper() in last_names)

    def test_get_last_names_2010(self):
        last_names = names.get_last_names_2010()
        self.assertFalse('Mxyzptlk'.upper() in last_names)


if __name__ == '__main__':
    unittest.main()

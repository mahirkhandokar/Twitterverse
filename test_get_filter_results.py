import unittest
import twitterverse_functions as tf


class TestGetFilterResults(unittest.TestCase):
    def test_filter_no_users(self):
        """Test get_filter_results with a list of no users.

        """

        data = open('small_data.txt')
        actual = tf.get_filter_results(tf.process_data(data), [],
                                    {'following: tomCruise'})
        expected = []
        msg = message('''tf.get_filter_results(tf.process_data(data), [],
        {'following: tomCruise'})''', str(expected), str(actual))
        data.close()
        self.assertEqual(actual, expected, msg)

    def test_filter_one_to_none_by_following(self):
        """Test get_filter_results with a list of one user, who gets
        filtered out by filter, following.

        """

        data = open('data.txt')
        actual = tf.get_filter_results(tf.process_data(data), ['katieH'],
                                    {'following': 'tomCruise'})
        expected = []
        msg = message('''tf.get_filter_results(tf.process_data(data),
        ['katieH'], {'following': 'tomCruise'})''', str(expected), str(actual))
        data.close()
        self.assertEqual(actual, expected, msg)

    def test_filter_one_to_none_by_follower(self):
        """Test get_filter_results with a list of one user, who gets
        filtered out by filter, follower.

        """

        data = open('data.txt')
        actual = tf.get_filter_results(tf.process_data(data), ['katieH'],
                                    {'follower': 'tomfan'})
        expected = []
        msg = message('''tf.get_filter_results(tf.process_data(data),
        ['katieH'], {'follower': 'tomfan'})''', str(expected), str(actual))
        data.close()
        self.assertEqual(actual, expected, msg)

    def test_filter_one_to_none_by_name(self):
        """Test get_filter_results with a list of one user, who gets
        filtered out by filter, name-includes.

        """

        data = open('data.txt')
        actual = tf.get_filter_results(tf.process_data(data), ['katieH'],
                                    {'name-includes': 'y'})
        expected = []
        msg = message('''tf.get_filter_results(tf.process_data(data),
        ['katieH'], {'name-includes': 'y'})''', str(expected), str(actual))
        data.close()
        self.assertEqual(actual, expected, msg)

    def test_filter_one_to_none_by_location(self):
        """Test get_filter_results with a list of one user, who gets
        filtered out by filter, location-includes.

        """

        data = open('data.txt')
        actual = tf.get_filter_results(tf.process_data(data), ['tomfan'],
                                    {'location-includes': 'CA'})
        expected = []
        msg = message('''tf.get_filter_results(tf.process_data(data),
        ['tomfan'], {'location-includes': 'CA'})''', str(expected), str(actual))
        data.close()
        self.assertEqual(actual, expected, msg)

    def test_filter_one_user(self):
        """Test get_filter_results with a list of one user, who doesn't get
        filtered out.

        """

        data = open('data.txt')
        actual = tf.get_filter_results(tf.process_data(data), ['tomCruise'],
                                    {'following': 'katieH'})
        expected = ['tomCruise']
        msg = message('''tf.get_filter_results(tf.process_data(data),
        ['tomCruise'], {'following': 'katieH'})''', str(expected), str(actual))
        data.close()
        self.assertEqual(actual, expected, msg)

    def test_filter_many_to_none_by_following(self):
        """Test get_filter_results with a list of many users, who get
        filtered out due to filter, following.

        """

        data = open('data.txt')
        actual = tf.get_filter_results(tf.process_data(data),
        ['tomCruise', 'katieH', 'PerezHilton', 'z', 'c', 'x'],
        {'following': 'q'})
        expected = []
        msg = message('''tf.get_filter_results(tf.process_data(data),
        ['tomCruise', 'katieH', 'PerezHilton', 'z', 'c', 'x'],
        {'following': 'q'})''', str(expected), str(actual))
        data.close()
        self.assertEqual(actual, expected, msg)

    def test_filter_many_to_none_by_followers(self):
        """Test get_filter_results with a list of many users, who get
        filtered out due to filter, followers.

        """

        data = open('data.txt')
        actual = tf.get_filter_results(tf.process_data(data),
        ['tomCruise', 'katieH', 'PerezHilton', 'q', 'p', 'x'],
        {'follower': 'c'})
        expected = []
        msg = message('''tf.get_filter_results(tf.process_data(data),
        ['tomCruise', 'katieH', 'PerezHilton', 'q', 'p', 'x'],
        {'follower': 'c'})''', str(expected), str(actual))
        data.close()
        self.assertEqual(actual, expected, msg)

    def test_filter_many_to_none_by_name(self):
        """Test get_filter_results with a list of many users, who get
        filtered out due to filter, name-includes.

        """

        data = open('data.txt')
        actual = tf.get_filter_results(tf.process_data(data),
        ['katieH', 'PerezHilton', 'q', 'p', 'x'], {'name-includes': 'c'})
        expected = []
        msg = message('''tf.get_filter_results(tf.process_data(data),
        ['katieH', 'PerezHilton', 'q', 'p', 'x'],
        {'name-includes': 'c'})''', str(expected), str(actual))
        data.close()
        self.assertEqual(actual, expected, msg)

    def test_filter_many_to_none_by_location(self):
        """Test get_filter_results with a list of many users, who get
        filtered out due to filter, location-includes.

        """

        data = open('data.txt')
        actual = tf.get_filter_results(tf.process_data(data),
        ['katieH', 'PerezHilton', 'q', 'p', 'x', 'a'],
        {'location-includes': 'Texas'})
        expected = []
        msg = message('''tf.get_filter_results(tf.process_data(data),
        ['katieH', 'PerezHilton', 'q', 'p', 'x', 'a'],
        {'location-includes': 'Texas'})''', str(expected), str(actual))
        data.close()
        self.assertEqual(actual, expected, msg)

    def test_filter_many_users(self):
        """Test get_filter_results with a list of many users, who don't get
        filtered out.

        """

        data = open('data.txt')
        actual = tf.get_filter_results(tf.process_data(data),
        ['tomCruise', 'katieH', 'PerezHilton', 'NicoleKidman'],
        {'name-includes': 'e'})
        expected = ['tomCruise', 'katieH', 'PerezHilton', 'NicoleKidman']
        msg = message('''tf.get_filter_results(tf.process_data(data),
        ['tomCruise', 'katieH', 'PerezHilton', 'NicoleKidman'],
        {'name-includes': 'e'})''', str(expected), str(actual))
        data.close()
        self.assertEqual(actual, expected, msg)

    def test_filter_many_to_some_by_following(self):
        """Test get_filter_results with a list of many users, where some get
        filtered out due to filter, following.

        """

        data = open('data.txt')
        actual = tf.get_filter_results(tf.process_data(data),
        ['tomCruise', 'katieH', 'PerezHilton', 'NicoleKidman'],
        {'following': 'katieH'})
        expected = ['tomCruise', 'PerezHilton']
        msg = message('''tf.get_filter_results(tf.process_data(data),
        ['tomCruise', 'katieH', 'PerezHilton', 'NicoleKidman'],
        {'following': 'katieH'})''', str(expected), str(actual))
        data.close()
        self.assertEqual(actual, expected, msg)

    def test_filter_many_to_some_by_follower(self):
        """Test get_filter_results with a list of many users, where some get
        filtered out due to filter, follower.

        """

        data = open('data.txt')
        actual = tf.get_filter_results(tf.process_data(data),
        ['tomCruise', 'katieH', 'PerezHilton', 'NicoleKidman'],
        {'follower': 'tomfan'})
        expected = ['tomCruise']
        msg = message('''tf.get_filter_results(tf.process_data(data),
        ['tomCruise', 'katieH', 'PerezHilton', 'NicoleKidman'],
        {'follower': 'tomfan'})''', str(expected), str(actual))
        data.close()
        self.assertEqual(actual, expected, msg)

    def test_filter_many_to_some_by_name(self):
        """Test get_filter_results with a list of many users, where some get
        filtered out by the filter, name-includes.

        """

        data = open('data.txt')
        actual = tf.get_filter_results(tf.process_data(data),
        ['tomCruise', 'katieH', 'PerezHilton', 'NicoleKidman', 'tomfan'],
        {'name-includes': 'tom'})
        expected = ['tomCruise', 'tomfan']
        msg = message('''tf.get_filter_results(tf.process_data(data),
        ['tomCruise', 'katieH', 'PerezHilton', 'NicoleKidman', 'tomfan'],
        {'name-includes': 'tom'})''', str(expected), str(actual))
        data.close()
        self.assertEqual(actual, expected, msg)

    def test_filter_many_to_some_by_location(self):
        """Test get_filter_results with a list of many users, whhere some get
        filtered out by the filter, location-includes.

        """

        data = open('data.txt')
        actual = tf.get_filter_results(tf.process_data(data),
        ['tomCruise', 'katieH', 'PerezHilton', 'NicoleKidman', 'tomfan'],
        {'location-includes': 'CA'})
        expected = ['tomCruise', 'PerezHilton']
        msg = message('''tf.get_filter_results(tf.process_data(data),
        ['tomCruise', 'katieH', 'PerezHilton', 'NicoleKidman', 'tomfan'],
        {'location-includes': 'CA'})''', str(expected), str(actual))
        data.close()
        self.assertEqual(actual, expected, msg)

    def test_filter_two_filters(self):
        """Test get_filter_results with a list of many users, where all or some
        get filtered out by filter, following and follower.

        """

        data = open('data.txt')
        actual = tf.get_filter_results(tf.process_data(data),
            ['katieH', 'tomCruise'], {'following': '', 'follower': 'tomfan'})
        expected = []
        msg = message('''tf.get_filter_results(tf.process_data(data),
        ['katieH', 'tomCruise'], {'following': '', 'follower': 'tomCruise'})''',
        str(expected), str(actual))
        data.close()
        self.assertEqual(actual, expected, msg)

    def test_filter_three_filters(self):
        """Test get_filter_results with a list of many users, where all or none
        get filtered out by filter, following, follower and name-includes.

        """

        data = open('data.txt')
        actual = tf.get_filter_results(tf.process_data(data),
            ['katieH', 'tomCruise', 'tomfan'],
            {'following': 'katieH', 'follower':
             'PerezHilton', 'name-includes': 'tom'})
        expected = ['tomCruise']
        msg = message('''tf.get_filter_results(tf.process_data(data),
        ['katieH', 'tomCruise', 'tomfan'], {'following': 'katieH', 'follower':
        'PerezHilton', 'name-includes': 'tom'})''',
        str(expected), str(actual))
        data.close()
        self.assertEqual(actual, expected, msg)

    def test_filter_all_filters(self):
        """Test get_filter_results with a list of many users, where all or none
        get filtered out by filter, following, follower, name-includes and
        location-includes.

        """

        data = open('data.txt')
        actual = tf.get_filter_results(tf.process_data(data),
            ['katieH', 'tomCruise', 'tomfan', 'PerezHilton'],
            {'following': 'katieH', 'follower':
             'PerezHilton', 'name-includes': 'tom', 'location-includes': 'CA'})
        expected = ['tomCruise']
        msg = message('''tf.get_filter_results(tf.process_data(data),
        ['katieH', 'tomCruise', 'tomfan', 'PerezHilton'],
        {'following': 'katieH', 'follower':'PerezHilton',
        'name-includes': 'tom', 'location-includes': 'CA'})''',
        str(expected), str(actual))
        data.close()
        self.assertEqual(actual, expected, msg)

    def test_filter_no_filters(self):
        """Test get_filter_results with a list of many users, where none
        due to there being no filters.

        """

        data = open('data.txt')
        actual = tf.get_filter_results(tf.process_data(data),
            ['katieH', 'tomCruise', 'tomfan', 'PerezHilton'],
            {})
        expected = ['katieH', 'tomCruise', 'tomfan', 'PerezHilton']
        msg = message('''tf.get_filter_results(tf.process_data(data),
        ['katieH', 'tomCruise', 'tomfan', 'PerezHilton'], {})''',
        str(expected), str(actual))
        data.close()
        self.assertEqual(actual, expected, msg)

def message(test_case: str, expected: str, actual: str) -> str:
    """Return an error message for the function call test_case that
    resulted in a value actual, when the correct value is expected.

    """

    return ("When we called " + test_case + " we expected " + expected
            + ", but got " + actual)


if __name__ == '__main__':
    unittest.main(exit=False)

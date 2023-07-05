import unittest   # model testing framework this helps CI test the code


class Apptest():
    def test_t0001_smoketest(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
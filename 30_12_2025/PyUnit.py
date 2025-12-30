# import unittest
# class TestExample(unittest.TestCase):

#     def test_sample(self):   # test name must start with test_
#         self.assertEqual(2+2,4)   # assertions 
#     def clean_salary(salary):
#         return int(salary.replace(",",""))
#     def test_clean_salary(self):
#         self.assertEqual(clean_salary("50,000",50000))

# if __name__ == "__main__":
#     unittest.main()   # run thw method


# import unittest 
# import calc

# class TestCalc(unittest.TestCase):
#     def test_add(self):
       
#        self.assertEqual(calc.add(10,5),15)
#        self.assertEqual(calc.add(-1,1),0)
#        self.assertEqual(calc.add(-1,-1),-2)

#     #    result = calc.add(10,5)
#     #    self.assertEqual(result,14)

# if __name__ == '__main__':
#     unittest.main()


# import unittest

# class TestExample(unittest.TestCase):

#     def setUp(self):
#         print("before test")
#     def test_case(self):
#         self.assertTrue(10<5)
#     def tearDown(self):
#         print("After test")

# if __name__ == "__main__":
#     unittest.main()



import unittest

class Exampletest(unittest.TestCase):
    def setUp(self):
        print("before test")
    def test_check(self):
        self.assertTrue(10>5)
    def test_find(self):
        self.assertFalse(10>5)
    def tearDown(self):
        print("After test")

if __name__ == "__main__":
    unittest.main()

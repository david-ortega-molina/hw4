import unittest
import func

class testCaseCube(unittest.TestCase):
    def test_cube(self):
       self.assertEqual(func.cube(5,5,5), 125)

    def test_cube2(self):
       self.assertEqual(func.cube(7,7,7), 343)

    def test_cube3(self):
        self.assertEqual(func.cube(-4 ,-4,-4), -64)

class testCaseElement(unittest.TestCase):
    def test_Element(self):

        array = [10,10,10]
        self.assertEqual(func.element(array), 10)

    def test_element1(self):
        array1 = [10,3,9,2,3]
        self.assertEqual(func.element(array1), 5.4)

    def test_element2(self):
        array2 = [10,12]
        self.assertNotEqual(func.element(array2), 0)

class testCaseName(unittest.TestCase):
    def test_name(self):
        first = 'david'
        last = 'ortega'
        self.assertEqual(func.name(first,last), ('david' , 'ortega'))
    
    def test_name1(self):
        first1 = 'ben'
        last1 = 'baller'
        self.assertEqual(func.name(first1,last1), ('ben', 'baller'))
    
    def test_name1(self):
        first2 = 'steph'
        last2 = 'curry'
        self.assertEqual(func.name(first2,last2), ('steph', 'curry'))


        

    
   
       

if __name__ == '__main__':
    unittest.main()
    

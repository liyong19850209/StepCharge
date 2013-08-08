import math
import unittest
def eratosthenes(begin,end):
    result = []
    if begin == 2:
        result.append(begin)
    if begin%2 == 0:
        begin += 1
    e = int(math.pow(end,0.5))+1
    for i in range(begin,end+1,2):
        flag = 1
        for j in range(3,e,2):
            if i%j == 0 and i != j:
                flag = 0
        if flag == 1:
            result.append(i)
    return result
class eratosthenesTestCase(unittest.TestCase):
    def setUp(self):
        print "Try to fine primes between begin and end"
    def tearDown(self):
        print "OK,it is over!"
    def testEratosthenes(self):
        self.assertEqual(eratosthenes(2,9),[2,3,5,7])
        self.assertEqual(eratosthenes(3,15),[3,5,7,11,13])
        self.assertEqual(eratosthenes(5,25),[5,7,11,13,17,19,23])
        self.assertEqual(eratosthenes(7,50),[7,11,13,17,19,23,29,31,37,41,43,47])
if __name__ == "__main__":
    unittest.main()

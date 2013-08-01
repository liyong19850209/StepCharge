import unittest
def intersectionVer0(listA,listB):
    resultList = []
    for a in listA:
        if a in listB:
            resultList.append(a)
    return resultList

def intersectionVer1(listA,listB):
    listA.sort()
    listB.sort()
    resultList = []
    i = 0;j = 0
    while i < len(listA) and j < len(listB):
        if listA[i] > listB[j]:
            j += 1
        elif listA[i] < listB[j]:
            i += 1
        else:
            resultList.append(listA[i])
            i += 1;j += 1;
    return resultList

def intersectionVer2(listA,listB):
    return list(set(listA).intersection(set(listB)))

class intersectionTestCase(unittest.TestCase):
    def setUp(self):
        print "test start"
    def tearDown(self):
        print "test stop"
    def testIntersection(self):
        self.assertEqual(intersectionVer0([8,5,9,3,1],[7,9,3,4]),[9,3])
        self.assertEqual(intersectionVer1([8,5,9,3,1],[7,9,3,4]),[3,9])
        self.assertEqual(intersectionVer2([8,5,9,3,1],[7,9,3,4]),[9,3])

if __name__ == "__main__":
    unittest.main()

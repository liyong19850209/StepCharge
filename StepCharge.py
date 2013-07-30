import unittest

def charge_ver0(degree):
  standard = ((0,0.5),(100,0.4),(200,0.3),(800,0.2),(float('inf'),0))
  price = 0
  for i in range(len(standard)-1):
    fix_delta = (standard[i+1][0] - standard[i][0]) * standard[i][1]
    var_delta = (degree - standard[i][0]) * standard[i][1]
    if degree >= standard[i][0]:
      if degree < standard[i+1][0]:
        price += var_delta
        break
      else:
        price += fix_delta
  return price

def charge_ver1(degree):
  standard = ((0,0.5),(100,0.4),(200,0.3),(800,0.2),(float('inf'),0))
  price = 0
  for i in range(len(standard)-1):
    fix_delta = (standard[i+1][0] - standard[i][0]) * standard[i][1]
    var_delta = (degree - standard[i][0]) * standard[i][1]
    if degree < standard[i+1][0]:
      price += var_delta
      break
    else:
      price += fix_delta
  return price

def charge_ver2(degree):
  standard = ((0,0.5),(100,0.4),(200,0.3),(800,0.2),(float('inf'),0))
  price = 0;i = 0;flag = True
  while flag:
    fix_delta = (standard[i+1][0] - standard[i][0]) * standard[i][1]
    var_delta = (degree - standard[i][0]) * standard[i][1]
    delta,flag = (degree < standard[i+1][0]) and (var_delta,False) or (fix_delta,True)
    price,i = price+delta,i+1
  return price

class ChargeTestCase(unittest.TestCase):
  def setUp(self):
    print "test start"
  def tearDown(self):
    print "test stop"
  def testVer0(self):
    print "test ver0"
    self.assertEqual(charge_ver0(50),25)
    self.assertEqual(charge_ver0(150),70)
    self.assertEqual(charge_ver0(300),120)
    self.assertEqual(charge_ver0(900),290)
  def testVer1(self):
    print "test ver1"
    self.assertEqual(charge_ver1(50),25)
    self.assertEqual(charge_ver1(150),70)
    self.assertEqual(charge_ver1(300),120)
    self.assertEqual(charge_ver1(900),290)
  def testVer2(self):
    print "test ver2"
    self.assertEqual(charge_ver2(50),25)
    self.assertEqual(charge_ver2(150),70)
    self.assertEqual(charge_ver2(300),120)
    self.assertEqual(charge_ver2(900),290)
if __name__ == "__main__":
  unittest.main()

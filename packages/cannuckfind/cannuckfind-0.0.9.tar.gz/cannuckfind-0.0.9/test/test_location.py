print(40*'*')
print('testing location \n')
import sys,math
import unittest



sys.path.append('/media/henskyconsulting/easystore/Hensky/Projects/2022twitloccan/cannuckfind/src')
from cannuckfind import geolocation
from cannuckfind import C3


class test_unknownC(unittest.TestCase):
    """
    Test unknownC
    """
    def test_unknownC(self):
        print('*** test_unknownC')
        from cannuckfind import geolocation
        testloc = geolocation.unknownC()
        self.assertTrue(testloc.MX == 106)

class test_CanC3SC(unittest.TestCase):
    """
    Test SpaCy C3 countrie identication
    """        
    def test_isCanC3SC(self):
        print('*** test CanC3SC')
        from cannuckfind import geolocation
        testisCanC3SC = geolocation.isC3SC()
        testisCanC3SC.loadraw("Toronto, Canada")
        junkval = testisCanC3SC.isCanC3SC()
        self.assertTrue(junkval == True ) 
        testisCanC3SC.loadraw("Ottawa, Canada")
        junkval = testisCanC3SC.isCanC3SC()
        self.assertTrue(junkval == True ) 
        testisCanC3SC.loadraw("Paris, France")
        junkval = testisCanC3SC.isCanC3SC()
        self.assertTrue(junkval == False ) 
       
    def test_isUSC3SC(self):
        from cannuckfind import geolocation
        testisCanC3SC = geolocation.isC3SC()
        testisCanC3SC.loadraw("New York,United States")
        print(testisCanC3SC.isUSC3SC())
        junkval = testisCanC3SC.isUSC3SC()
        print(junkval)
        self.assertTrue(junkval == True )
               
    def test_isOthSC(self):
        from cannuckfind import geolocation
        testisCanC3SC = geolocation.isC3SC()
        testisCanC3SC.loadraw("Paris, France")
        print(testisCanC3SC.isOthC3SC())
        junkval = testisCanC3SC.isOthC3SC()
        print(junkval)
        self.assertTrue(junkval == True )           

class test_CanC3GP(unittest.TestCase):
    """
    Test GeoGraphy C3 country identication
    """        
    def test_isCanC3GP(self):
        print('*** test CanC3GP')
        from cannuckfind import geolocation
        testisCanC3GP = geolocation.isC3GP()
        testisCanC3GP.loadraw("Toronto, Canada")
        junkval = testisCanC3GP.isCanC3GP()
        self.assertTrue(junkval == True ) 
        testisCanC3GP.loadraw("Ottawa, Canada")
        junkval = testisCanC3GP.isCanC3GP()
        self.assertTrue(junkval == True ) 
        testisCanC3GP.loadraw("Paris, France")
        junkval = testisCanC3GP.isCanC3GP()
        self.assertTrue(junkval == False ) 

    def test_isUSC3GP(self):
        from cannuckfind import geolocation
        testisCanC3GP = geolocation.isC3GP()
        testisCanC3GP.loadraw("New York,United States")
        print(testisCanC3GP.isUSC3GP())
        junkval = testisCanC3GP.isUSC3GP()
        print(junkval)
        self.assertTrue(junkval == True )
        
    def test_isOthGP(self):
        from cannuckfind import geolocation
        testisCanC3GP = geolocation.isC3GP()
        testisCanC3GP.loadraw("Paris, France")
        print(testisCanC3GP.isOthC3GP())
        junkval = testisCanC3GP.isOthC3GP()
        print(junkval)
        self.assertTrue(junkval == True )           


print('*** test cannuckfind geolocation complete')
print(40*'*')       


if __name__ == '__main__':
    unittest.main()



print(40*'*')



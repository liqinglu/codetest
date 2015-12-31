import unittest
import interpreter

class testInterpreter(unittest.TestCase):
    def setUp(self):
        self.tclass = interpreter.interpreter("None")
    def tearDown(self):
        pass
    def test_only5(self):
        self.tclass._setexpr('5')
        self.assertEqual(self.tclass.gotit(),'5')
    def test_plus(self):
        self.tclass._setexpr('5 + 3')
        self.assertEqual(self.tclass.gotit(),'8')
    def test_minos(self):
        self.tclass._setexpr(' 5- 2 ')
        self.assertEqual(self.tclass.gotit(),'3')
    def test_multiply(self):
        self.tclass._setexpr('8*12')
        self.assertEqual(self.tclass.gotit(),'96')
    def test_division(self):
        self.tclass._setexpr('65/5')
        self.assertEqual(self.tclass.gotit(),'13.0')
    def test_multiplyplus(self):
        self.tclass._setexpr('5+3*7')
        self.assertEqual(self.tclass.gotit(),'26')
    def test_multinumber(self):
        self.tclass._setexpr('5+3-2+22+103-77')
        self.assertEqual(self.tclass.gotit(),'54')
    def test_brace(self):
        self.tclass._setexpr('(3+4)*5+(6-3)*8/4')
        self.assertEqual(self.tclass.gotit(),'41.0')
    def test_nestbrace(self):
        self.tclass._setexpr('((3+4)*5+1)*3')
        self.assertEqual(self.tclass.gotit(),'108')

if __name__ == "__main__":
    unittest.main()

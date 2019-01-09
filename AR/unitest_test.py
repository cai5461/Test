#coding=utf-8

import unittest

class TestStringMethods(unittest.TestCase):

	def test_upper(self):
		#判断相等
		self.assertEqual('foo'.upper(),'FOO')

	def test_isupper(self):
		#判断结果是真还是假
		self.assertTrue('FOO'.isupper())
		self.assertFalse('Foo'.isupper())

	def test_split(self):
		s = 'hello world'
		self.assertEqual(s.split(),['hello','world'])
		# check that s.split fails when the separator is not string
		with self.assertRaises(TypeError):
			s.split(2)
		# print(s.split(2))

	@unittest.skip("demonstarting skipping")
	#无条件跳过装饰的测试，并说明测试的原因
	def test_nothing(self):
		self.fail("shouldn't happen")

	@unittest.skipIf(3>2,
		             "not supported in this library version")
	#@unittest.skipIf(reason): skipIf(condition,reason)装饰器：条件为真时，跳过装饰的测试，并说明测试的原因
	def test_format(self):
		pass

	@unittest.skipUnless(1>2,"requires Windows")
	#条件为假时，跳过装饰的测试，并在后面说明测试的原因
	def test_windows_support(self):
		pass






if __name__ == '__main__':
	# unittest.main()

	suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
	unittest.TextTestRunner(verbosity=2).run(suite)
	#verbosity=2表示输入完整信息

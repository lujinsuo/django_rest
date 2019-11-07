# #-*-coding:utf-8-*-
# #作者：test
# #创建时间： 2019/8/19 16:00
# #文件：  rest_test.PY
import  unittest
import requests
import  json

class UserTest(unittest.TestCase):
	'''用户查询测试'''

	def setUp(self):
		self.base_url='http://127.0.0.1:8000/users'
		self.auth=('admin','testadmin')

	def test_user1(self):
		'''test user admin'''
		r=requests.get(self.base_url+'/1/',auth=self.auth)
		result=json.loads(r.text)
		print(result)
		self.assertEqual(result['username'],'admin')
		self.assertEqual(result['email'],'test@qq.com')

class GroupTest(unittest.TestCase):

	''' 用户组测试'''

	def setUp(self):
		self.base_url='http://127.0.0.1:8000/groups'
		self.auth=('admin','testadmin')

	def test_group1(self):
		r=requests.get(self.base_url+'/1/',auth=self.auth)
		result=json.loads(r.text)
		print(result)
		self.assertEqual(result['name'],'test')

if __name__ == '__main__':
	unittest.main()
import unittest

import boto3
from moto import mock_s3

from external_data_structures.dictionaries.s3 import S3Dict



class TestS3Dict(unittest.TestCase):

  @mock_s3
  def test_s3_dict_int_assignment_and_retrieval(self):
    self.bucket = S3Dict('test-4e1243')
    self.bucket.s3.create_bucket(Bucket='test-4e1243')
    self.bucket['asd'] = 123
    self.assertEqual(123, self.bucket['asd'])

  @mock_s3
  def test_s3_dict_str_assignment_and_retrieval(self):
    self.bucket = S3Dict('test-4e1243')
    self.bucket.s3.create_bucket(Bucket='test-4e1243')
    self.bucket['msg'] = "hello world"
    self.assertEqual("hello world", self.bucket['msg'])

  @mock_s3
  def test_s3_dict_list_assignment_and_retrieval(self):
    self.bucket = S3Dict('test-4e1243')
    self.bucket.s3.create_bucket(Bucket='test-4e1243')
    self.bucket['msg'] = [1,2, 3, "a", "b", "c"]
    self.assertEqual([1,2, 3, "a", "b", "c"], self.bucket['msg'])

  @mock_s3
  def test_s3_dict_dict_assignment_and_retrieval(self):
    self.bucket = S3Dict('test-4e1243')
    self.bucket.s3.create_bucket(Bucket='test-4e1243')
    self.bucket['msg'] = {"a": None, "b": 2, "c" : "c"}
    self.assertEqual({"a": None, "b": 2, "c" : "c"}, self.bucket['msg'])

  @mock_s3
  def test_s3_dict_keys(self):
    self.bucket = S3Dict('test-4e1243')
    self.bucket.s3.create_bucket(Bucket='test-4e1243')
    self.assertEqual([], self.bucket.keys())
    self.bucket['msg'] = "a"
    self.assertEqual(['msg'], self.bucket.keys())
    self.bucket['msg2'] = "b"
    self.assertEqual(['msg', 'msg2'], self.bucket.keys())
    del self.bucket['msg']
    self.assertEqual(['msg2'], self.bucket.keys())

  @mock_s3
  def test_s3_dict_contains(self):
    self.bucket = S3Dict('test-4e1243')
    self.bucket.s3.create_bucket(Bucket='test-4e1243')
    self.assertFalse("something" in self.bucket)
    self.bucket["something"] = 123
    self.assertTrue("something" in self.bucket)


if __name__ == '__main__':
    unittest.main()
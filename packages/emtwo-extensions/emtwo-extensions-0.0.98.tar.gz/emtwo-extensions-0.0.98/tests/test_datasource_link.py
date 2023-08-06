import mock

from tests import BaseTestCase
from flask import Flask

from redash.models import DataSource
from redash.query_runner.pg import PostgreSQL
from redash_stmo.datasource_link import datasource_link, BaseQueryRunner


class TestDatasourceLink(BaseTestCase):
	EXPECTED_DOC_URL = "www.example.com"
	def setUp(self):
		super(TestDatasourceLink, self).setUp()
		self.path = "/api/data_sources/{}".format(self.factory.data_source.id)
		self.patched_query_runners = self._setup_mock('redash_stmo.datasource_link.query_runners')
		self.patched_query_runners.return_value = {}

		app = Flask("test")
		datasource_link(app)

	def _setup_mock(self, function_to_patch):
		patcher = mock.patch(function_to_patch)
		patched_function = patcher.start()
		self.addCleanup(patcher.stop)
		return patched_function

	def test_updates_data_source(self):
		admin = self.factory.create_admin()
		new_name = 'New Name'
		new_options = {"dbname": "newdb", "doc_url": self.EXPECTED_DOC_URL}
		rv = self.make_request('post', self.path,
		                       data={
									'name': new_name,
									'type': 'pg',
									'type_name': 'Postgres',
									'options': new_options},
		                       user=admin)
		self.assertEqual(rv.status_code, 200)
		data_source = DataSource.query.get(self.factory.data_source.id)
		self.assertEqual(data_source.name, new_name)
		self.assertEqual(data_source.options.to_dict(), new_options)
		self.assertEqual(rv.json['type_name'], data_source.query_runner.name())
		self.assertEqual(rv.json['options']["doc_url"], self.EXPECTED_DOC_URL)

	def test_creates_data_source(self):
		admin = self.factory.create_admin()
		rv = self.make_request('post', '/api/data_sources',
		                       data={'name': 'DS 1', 'type': 'pg',
		                             'options': {"dbname": "redash", "doc_url": self.EXPECTED_DOC_URL},
		                             'doc_url': None}, user=admin)
		self.assertEqual(rv.status_code, 200)
		data_source = DataSource.query.get(self.factory.data_source.id)
		self.assertIsNotNone(DataSource.query.get(rv.json['id']))
		self.assertEqual(rv.json['type_name'], data_source.query_runner.name())
		self.assertEqual(rv.json['options']["doc_url"], self.EXPECTED_DOC_URL)

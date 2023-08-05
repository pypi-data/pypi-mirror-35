from tests import BaseTestCase

from redash.models import DataSource


class TestDatasourceLink(BaseTestCase):
	def setUp(self):
		super(TestDatasourceLink, self).setUp()
		self.path = "/api/data_sources/{}".format(self.factory.data_source.id)

	def test_updates_data_source(self):
		admin = self.factory.create_admin()
		new_name = 'New Name'
		new_options = {"dbname": "newdb"}
		rv = self.make_request('post', self.path,
		                       data={'name': new_name, 'type': 'pg', 'options': new_options,
		                             'doc_url': None},
		                       user=admin)
		self.assertEqual(rv.status_code, 200)
		data_source = DataSource.query.get(self.factory.data_source.id)
		self.assertEqual(data_source.name, new_name)
		self.assertEqual(data_source.options.to_dict(), new_options)

	def test_creates_data_source(self):
		admin = self.factory.create_admin()
		rv = self.make_request('post', '/api/data_sources',
		                       data={'name': 'DS 1', 'type': 'pg',
		                             'options': {"dbname": "redash"},
		                             'doc_url': None}, user=admin)
		self.assertEqual(rv.status_code, 200)
		self.assertIsNotNone(DataSource.query.get(rv.json['id']))
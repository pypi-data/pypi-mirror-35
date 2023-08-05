from redash.query_runner.pg import PostgreSQL, Redshift
from redash.models import DataSource

original_datasource_to_dict = DataSource.to_dict

def datasource_to_dict():
	d = original_datasource_to_dict()
	d['type_name'] = self.query_runner.name()
	return d

def datasource_link(app=None):
	PostgreSQL.default_doc_url = "https://www.postgresql.org/docs/current/"
	PostgreSQL.add_configuration_property("doc_url", {
        "type": "string",
        "title": "Documentation URL",
        "default": PostgreSQL.default_doc_url})

	DataSource.to_dict = datasource_to_dict
	print DataSource
	print DataSource.to_dict
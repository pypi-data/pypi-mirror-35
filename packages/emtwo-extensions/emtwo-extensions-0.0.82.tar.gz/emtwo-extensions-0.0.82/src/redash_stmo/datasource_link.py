from redash.models import DataSource
from redash.query_runner.pg import PostgreSQL, Redshift
from redash.query_runner import get_configuration_schema_for_query_runner_type


original_datasource_to_dict = DataSource.to_dict

def datasource_to_dict(self, all=False, with_permissions_for=None):
	d = original_datasource_to_dict(self)
	d['type_name'] = self.query_runner.name()
	schema = get_configuration_schema_for_query_runner_type(self.type)
	self.options.set_schema(schema)
	d['options'] = self.options.to_dict(mask_secrets=True)
	return d

def datasource_link(app=None):
	PostgreSQL.default_doc_url = "https://www.postgresql.org/docs/current/"
	PostgreSQL.add_configuration_property("doc_url", {
        "type": "string",
        "title": "Documentation URL",
        "default": PostgreSQL.default_doc_url})

	DataSource.to_dict = datasource_to_dict

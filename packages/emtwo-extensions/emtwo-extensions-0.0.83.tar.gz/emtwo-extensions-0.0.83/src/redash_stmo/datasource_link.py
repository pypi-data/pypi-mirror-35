from redash.models import DataSource
from redash.query_runner import BaseQueryRunner, query_runners
from redash.query_runner import get_configuration_schema_for_query_runner_type


original_datasource_to_dict = DataSource.to_dict

DATASOURCE_URLS = {
	"bigquery": "https://cloud.google.com/bigquery/docs/reference/legacy-sql",
	"Cassandra": "http://cassandra.apache.org/doc/latest/cql/index.html",
	"dynamodb_sql": "https://dql.readthedocs.io/en/latest/",
	"baseelasticsearch": "https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html",
	"google_spreadsheets": "http://redash.readthedocs.io/en/latest/datasources.html#google-spreadsheets",
	"hive": "https://cwiki.apache.org/confluence/display/Hive/LanguageManual",
	"impala": "http://www.cloudera.com/documentation/enterprise/latest/topics/impala_langref.html",
	"influxdb": "https://docs.influxdata.com/influxdb/v1.0/query_language/spec/",
	"jirajql": "https://confluence.atlassian.com/jirasoftwarecloud/advanced-searching-764478330.html",
	"mongodb": "https://docs.mongodb.com/manual/reference/operator/query/",
	"mssql": "https://msdn.microsoft.com/en-us/library/bb510741.aspx",
	"mysql": "https://dev.mysql.com/doc/refman/5.7/en/",
	"oracle": "http://docs.oracle.com/database/121/SQLRF/toc.htm",
	"pg": "https://www.postgresql.org/docs/current/",
	"redshift": "http://docs.aws.amazon.com/redshift/latest/dg/cm_chap_SQLCommandRef.html",
	"presto": "https://prestodb.io/docs/current/",
	"python": "http://redash.readthedocs.io/en/latest/datasources.html#python",
	"insecure_script": "http://redash.readthedocs.io/en/latest/datasources.html#python",
	"sqlite": "http://sqlite.org/lang.html",
	"treasuredata": "https://docs.treasuredata.com/categories/hive",
	"url": "http://redash.readthedocs.io/en/latest/datasources.html#url",
	"vertica": (
		"https://my.vertica.com/docs/8.0.x/HTML/index.htm#Authoring/"
        "ConceptsGuide/Other/SQLOverview.htm%3FTocPath%3DSQL"
        "%2520Reference%2520Manual%7C_____1")
}


def datasource_to_dict(self, all=False, with_permissions_for=None):
	d = original_datasource_to_dict(self)
	d['type_name'] = self.query_runner.name()
	schema = get_configuration_schema_for_query_runner_type(self.type)
	self.options.set_schema(schema)
	d['options'] = self.options.to_dict(mask_secrets=True)
	return d


def datasource_link(app=None):
	BaseQueryRunner.default_doc_url = None

	for runner_type, runner_class in query_runners.items():
		if runner_type not in DATASOURCE_URLS:
			continue

		runner_class.default_doc_url = DATASOURCE_URLS[runner_type]
		runner_class.add_configuration_property("doc_url", {
	        "type": "string",
	        "title": "Documentation URL",
	        "default": runner_class.default_doc_url})

	DataSource.to_dict = datasource_to_dict

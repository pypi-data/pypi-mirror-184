from google.cloud import bigquery
from tinybird_cdk import logger, connector, export, formats, errors, utils
from tinybird_cdk.cloud import gcp, gcs

# This connector expects the standard environment variable
#
#     GOOGLE_APPLICATION_CREDENTIALS
#
# to be set to a path to the JSON file with the application credentials you can
# obtain by following the steps explained in
#
#     https://cloud.google.com/docs/authentication/getting-started
#
# The GCS bucket used for exports is taken from the standard environment
# variable GCS_BUCKET.
class Connector(connector.SQLConnector):
    def __init__(self):
        super().__init__()
        self.bigquery = bigquery.Client(credentials=gcp.credentials(), project=gcp.project_id())
        self.client = gcs.Client()

    #
    # --- Scopes ----------------------------------------------------------------------------------
    #

    def get_scopes(self):
        return (
            connector.Scope(name='Projects', value='project'),
            connector.Scope(name='Datasets', value='dataset'),
            connector.Scope(name='Tables', value='table')
        )

    def list_scope(self, parents={}):
        if 'project' in parents:
            if 'dataset' in parents:
                return self._list_tables(parents['project'], parents['dataset'])
            return self._list_datasets(parents['project'])
        return self._list_projects()

    def _list_projects(self):
        projects = []
        for project in list(self.bigquery.list_projects()):
            projects.append(connector.Scope(name=project.friendly_name, value=project.project_id))
        projects.sort(key=lambda project: project.name)
        return projects

    def _list_datasets(self, project):
        datasets = []
        for dataset in list(self.bigquery.list_datasets(project=project)):
            datasets.append(connector.Scope(name=dataset.dataset_id, value=dataset.dataset_id))
        datasets.sort(key=lambda dataset: dataset.name)
        return datasets

    def _list_tables(self, project, dataset):
        tables = []
        for table in list(self.bigquery.list_tables(dataset=f'{project}.{dataset}')):
            tables.append(connector.Scope(name=table.table_id, value=table.table_id))
        tables.sort(key=lambda table: table.name)
        return tables

    #
    # --- Query -----------------------------------------------------------------------------------
    #

    def _query(self, sql):
        query_job = self.bigquery.query(sql)
        return [dict(row) for row in query_job.result()]

    #
    # --- Export ----------------------------------------------------------------------------------
    #

    # https://cloud.google.com/bigquery/docs/exporting-data
    # https://cloud.google.com/bigquery/docs/reference/standard-sql/other-statements#export_data_statement
    def _export(self, query, fmt):
        if fmt == formats.CSV:
            export_fmt = 'CSV'
        elif fmt == formats.NDJSON:
            export_fmt = 'JSON'
        else:
            raise errors.UnsupportedFormat(fmt)

        bucket = gcp.gcs_bucket()

        directory = utils.random_dirname()
        if folder := gcp.gcs_folder():
            directory = folder + '/' + directory

        uri = self.client.uri(bucket, f'{directory}/*.{fmt}')
        logger.info(f'Exporting to {uri}')
        query_job = self.bigquery.query(f"EXPORT DATA OPTIONS (format='{export_fmt}', uri='{uri}') AS {query}")
        query_job.result() # Wait for job to complete.

        return export.CloudDir(self.client, bucket, directory)

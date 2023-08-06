from collections import Iterable

from google.api_core.exceptions import GoogleAPIError
from google.cloud import bigquery
from google.cloud.bigquery import QueryJobConfig, QueryJob, TableReference, DatasetReference

from bigquery.ems_api_error import EmsApiError
from bigquery.ems_query_config import EmsQueryConfig, EmsQueryPriority
import logging

logger = logging.getLogger(__name__)

class EmsBigqueryClient:

    def __init__(self, project_id: str, location: str = "EU"):
        self.__project_id = project_id
        self.__bigquery_client = bigquery.Client(project_id)
        self.__location = location

    def run_async_query(self,
                        query: str,
                        job_id_prefix: str = None,
                        ems_query_config: EmsQueryConfig = EmsQueryConfig(
                            priority=EmsQueryPriority.INTERACTIVE)) -> str:
        return self.__execute_query_job(query=query,
                                        ems_query_config=ems_query_config,
                                        job_id_prefix=job_id_prefix).job_id

    def run_sync_query(self,
                       query: str,
                       ems_query_config: EmsQueryConfig = EmsQueryConfig(priority=EmsQueryPriority.INTERACTIVE)
                       ) -> Iterable:

        logger.info("Sync query executed with priority: %s", ems_query_config.priority)
        try:
            return self.__get_mapped_iterator(
                self.__execute_query_job(query=query,
                                         ems_query_config=ems_query_config).result()
            )
        except GoogleAPIError as e:
            raise EmsApiError("Error caused while running query | {} |: {}!".format(query, e.args[0]))

    def __execute_query_job(self, query: str, ems_query_config: EmsQueryConfig, job_id_prefix=None) -> QueryJob:
        return self.__bigquery_client.query(query=query,
                                            job_config=(self.__create_job_config(ems_query_config)),
                                            job_id_prefix=job_id_prefix,
                                            location=self.__location)

    def __create_job_config(self, ems_query_config: EmsQueryConfig) -> QueryJobConfig:
        job_config = QueryJobConfig()
        job_config.priority = ems_query_config.priority.value
        if ems_query_config.destination_table is not None:
            table_reference = TableReference(
                DatasetReference(
                    self.__project_id,
                    ems_query_config.destination_dataset),
                ems_query_config.destination_table)
            job_config.destination = table_reference
            job_config.write_disposition = ems_query_config.write_disposition.value
            job_config.create_disposition = ems_query_config.create_disposition.value
        return job_config

    @staticmethod
    def __get_mapped_iterator(result: Iterable):
        for row in result:
            yield dict(list(row.items()))

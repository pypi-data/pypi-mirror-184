import os
import re
from typing import Dict, Any, TextIO

import yaml
import jinja2


def dest(destination_dataset_table, prefix_dataset='tmp', return_dataset_only=False, return_table_only=False,
         ignore_env=False) -> str:
    """If `AIRFLOW_ENV != PROD` then write results to `prefix_dataset` instead.

    :param destination_dataset_table: destination to write results to.
    :return: destination_dataset_table: destination to write results to with prefix added if needed.
    """

    AIRFLOW_ENV = os.environ.get("AIRFLOW_ENV", "UNK")

    if AIRFLOW_ENV != 'PROD':

        if ignore_env in (False, 'False', 0, 'f', 'FALSE', 'false'):

            destination_dataset_table_list = destination_dataset_table.split('$')
            destination_dataset_table_base = destination_dataset_table_list[0]
            destination_dataset_table_partition = destination_dataset_table_list[1] if len(destination_dataset_table_list) == 2 else None
            destination_dataset_table_base_list = destination_dataset_table_base.replace(':', '.').split('.')
            destination_project = destination_dataset_table_base_list[0]
            destination_dataset = prefix_dataset
            if destination_dataset_table_partition:
                destination_table = f'{destination_dataset_table_base_list[1]}_{destination_dataset_table_base_list[2]}${destination_dataset_table_partition}'
            else:
                destination_table = f'{destination_dataset_table_base_list[1]}_{destination_dataset_table_base_list[2]}'
            destination_dataset_table = f'{destination_project}.{destination_dataset}.{destination_table}'

    destination_parts = destination_dataset_table.split('.')

    if return_dataset_only == True:
        return destination_parts[1]
    elif return_table_only == True:
        return destination_parts[2]
    else:
        return destination_dataset_table


def dest_dict(destination_dataset_table, prefix_dataset='tmp', ignore_env=False) -> Dict[str, str]:
    """Wrapper for `dest()` but to return as dict.
    """
    destination_dataset_table = dest(destination_dataset_table, prefix_dataset, ignore_env=ignore_env)
    destination_parts = destination_dataset_table.split('.')
    return {
        "projectId": destination_parts[0],
        "datasetId": destination_parts[1],
        "tableId": '.'.join(destination_parts[2:])
    }


def sched(schedule: Any, ignore_env=False) -> Any:
    """If AIRFLOW_ENV != PROD then schedule should be `@once`.

    :param schedule: schedule for prod.
    :return: schedule: `schedule` if prod else `@once`.
    """

    AIRFLOW_ENV = os.environ.get("AIRFLOW_ENV", "UNK")

    if AIRFLOW_ENV == 'PROD' or ignore_env == True:
        return schedule
    else:
        return '@once'


RE_SUPPORTED_LABEL_CHARS = re.compile(r"[a-z0-9_\-]")


def valid_label(label: str) -> str:
    """Remove unsupported label characters, transform upper to lower case and replace dots with dashes.

    :param label: raw label
    :return: transformed valid BQ label
    """
    label_max_len = 62
    return ''.join(re.findall(RE_SUPPORTED_LABEL_CHARS, label.lower().replace('.', '-')))[0:label_max_len]


def metadata_yaml_read(dag_abs_path: str, filename: str) -> TextIO:
    """Read yaml files from inside the given DAG folder.

    :param dag_abs_path: the absolute path of the dag.
    :param filename: the yaml filename.
    :return: yaml content.
    """
    with open(os.path.join(os.path.dirname(dag_abs_path), "metadata", filename), "r") as f:
        return yaml.safe_load(f)


def load_jinja_yaml_file(dag_abs_path: str, filename: str, template_variables: dict) -> dict:
    creds = template_variables.pop('creds')
    with open(os.path.join(os.path.dirname(dag_abs_path), filename), "r") as f:
        content = yaml.load(jinja2.Template(f.read()).render(**template_variables), yaml.FullLoader)
        content['source']['config']['credential'] = creds
        return content

import csv
from functools import lru_cache
from typing import Dict, List

# from src.insights.jobs import read


@lru_cache
def read(path: str) -> List[Dict]:
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    with open(path) as csv_file:
        file = csv.DictReader(csv_file)
        return [line for line in file]
        # result = []
        # for line in file:
        #      result.append(line)
        #      return result


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    file = read(path)
    list = []
    for line in file:
        if line["job_type"] not in list:
            list.append(line["job_type"])
    return list


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    return [line for line in jobs if line["job_type"] == job_type]

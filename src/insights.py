from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    all_jobs_types = list(set(job["job_type"] for job in jobs))
    return all_jobs_types


def filter_by_job_type(jobs, job_type):
    job_type_filtered = list(
        job for job in jobs if job["job_type"] == job_type
    )
    return job_type_filtered


def get_unique_industries(path):
    jobs = read(path)
    all_industries_types = list(
        set(job["industry"] for job in jobs if job["industry"] != "")
    )
    return all_industries_types


def filter_by_industry(jobs, industry):
    filtered_industry = list(
        job for job in jobs if job["industry"] == industry
    )
    return filtered_industry


def get_max_salary(path):
    jobs = read(path)
    max_salary = max(
        (int(job["max_salary"]) for job in jobs if job["max_salary"].isdigit())
    )
    return max_salary


def get_min_salary(path):
    jobs = read(path)
    min_salary = min(
        int(job["min_salary"]) for job in jobs if job["min_salary"].isdigit()
    )
    return min_salary


def matches_salary_range(job, salary):
    try:
        if (
            (type(salary) != int)
            or (not ("min_salary" or "max_salary") in job)
            or type(job["min_salary"]) != int
            or type(job["max_salary"]) != int
            or (job["min_salary"] > job["max_salary"])
        ):
            raise ValueError
        return job["max_salary"] >= salary >= job["min_salary"]

    except ValueError:
        raise ValueError

    # pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []

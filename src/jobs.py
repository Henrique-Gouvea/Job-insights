import csv
from functools import lru_cache


@lru_cache
def read(path):
    try:
        with open(path) as file:
            jobs = list(csv.DictReader(file))
            print(jobs[0])
            return jobs
    except FileNotFoundError as exc:
        print("arquivo nao encontrado" + exc)
    except csv.Error as err:
        print("Arquivo nao CSV error: %s" % err)

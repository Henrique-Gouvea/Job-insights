from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    pass
    brazilian_jobs_mock = read_brazilian_file(
        "tests/mocks/brazilians_jobs.csv"
    )
    assert {
        "title": "Auxiliar usinagem",
        "salary": "1400",
        "type": " full time",
    } in brazilian_jobs_mock

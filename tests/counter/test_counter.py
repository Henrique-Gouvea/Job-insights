from src.counter import count_ocurrences


def test_counter():
    pass
    print(count_ocurrences("src/jobs.csv", "java"))
    print('sdijaiosdjaiojdoijsaiodjsaiodj')
    assert count_ocurrences("src/jobs.csv", "java") != 10
    assert count_ocurrences("src/jobs.csv", "javascript") == 122

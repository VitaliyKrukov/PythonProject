import pytest


@pytest.fixture
def lis_test_dic():
    return [
        {"id": 41, "state": "EXECUTED"},
        {"id": 41, "state": "CANCELED"},
        {"id": 41, "stated": "EXECUTED"},
        {"id": 41, "state": 10},
    ]


@pytest.fixture
def list_test_data():
    return [
        {"date": "2019-07-03T18:35:29.512364"},
        {"date": "2018-06-30T02:08:58.425572"},
        {"date": "2018-06-30T02:08:58.425572"},
        {"dated": "2018-09-12T21:27:25.249"},
        {"date": 1234535},
    ]

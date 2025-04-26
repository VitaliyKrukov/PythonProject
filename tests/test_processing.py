from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_wrong_list():
    assert filter_by_state(True) == []


def test_filter_by_state():
    assert filter_by_state(
        [
            {"id": 41, "state": "EXECUTED"},
            {"id": 93, "state": "EXECUTED"},
            {"id": 59, "state": "CANCELED"},
            {"id": 61, "state": "CANCELED"},
        ]
    ) == [{"id": 41, "state": "EXECUTED"}, {"id": 93, "state": "EXECUTED"}]


def test_filter_by_state_mark(lis_test_dic):
    assert filter_by_state(lis_test_dic) == [{"id": 41, "state": "EXECUTED"}]


def test_sort_by_date():
    assert sort_by_date(
        [
            {"date": "2019-07-03T18:35:29.512364"},
            {"date": "2018-06-30T02:08:58.425572"},
            {"date": "2018-09-12T21:27:25.241689"},
            {"date": "2018-10-14T08:21:33.419441"},
        ]
    ) == [
        {"date": "2019-07-03T18:35:29.512364"},
        {"date": "2018-10-14T08:21:33.419441"},
        {"date": "2018-09-12T21:27:25.241689"},
        {"date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_mark(list_test_data):
    assert sort_by_date(list_test_data) == [
        {"date": "2019-07-03T18:35:29.512364"},
        {"date": "2018-06-30T02:08:58.425572"},
        {"date": "2018-06-30T02:08:58.425572"},
        {"date": 1234535},
        {"dated": "2018-09-12T21:27:25.249"},
    ]

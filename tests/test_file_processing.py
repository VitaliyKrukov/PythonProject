from unittest.mock import patch

from src.file_processing import (processing_function_csv,
                                 processing_function_excel)


@patch("pandas.read_csv")
def test_processing_function_csv(test_mock_csv, data_frame):
    test_mock_csv.return_value = data_frame
    assert processing_function_csv("") == data_frame.to_dict("records")


@patch("pandas.read_csv")
def test_processing_function_csv_wrong_value(test_mock_csv):
    test_mock_csv.side_effect = ValueError
    assert processing_function_csv("") == []


def test_processing_function_csv_open():
    assert processing_function_csv("") == []


@patch("pandas.read_excel")
def test_processing_function_excel(test_mock_excel, data_frame):
    test_mock_excel.return_value = data_frame
    assert processing_function_excel("") == data_frame.to_dict("records")


@patch("pandas.read_excel")
def test_processing_function_excel_wrong_value(test_mock_excel):
    test_mock_excel.side_effect = ValueError
    assert processing_function_excel("") == []


def test_processing_function_excel_open():
    assert processing_function_excel("") == []

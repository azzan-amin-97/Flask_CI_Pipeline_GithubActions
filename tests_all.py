import unittest

import requests




def test_addition():
    # Given
    num1 = 100
    num2 = 200

    # When
    response = requests.post("http://127.0.0.1:5000/api/addition",
                             data={'num1': num1,
                                   'num2': num2})

    res_json = response.json()
    result = res_json['result']

    # Then
    assert result == 300

def test_subtraction():
    # Given
    num1 = 1
    num2 = 1

    # When
    response = requests.post("http://127.0.0.1:5000/api/subtraction",
                             data={'num1': num1,
                                   'num2': num2})

    res_json = response.json()
    result = res_json['result']

    # Then
    assert result == 0

def test_multiplication():
    # Given
    num1 = 2
    num2 = 2

    # When
    response = requests.post("http://127.0.0.1:5000/api/multiplication",
                             data={'num1': num1,
                                   'num2': num2})

    res_json = response.json()
    result = res_json['result']

    # Then
    assert result == 4

def test_division():
    # Given
    num1 = 2
    num2 = 2

    # When
    response = requests.post("http://127.0.0.1:5000/api/division",
                             data={'num1': num1,
                                   'num2': num2})

    res_json = response.json()
    result = res_json['result']

    # Then
    assert result == 1



#!/usr/bin/env python3
'''
    CIT 175: DevOps Engineering in AWS
    Unit Tests for Labs 1 - 5
'''

def mock_input(s):
    "Mock up the user CLI input() Process"
    global input_values, output
    output.append(s)
    return input_values.pop(0)


def test_lab01():
    "Test of Lab 1"

    # Import Lab Function for Testing
    from lab01 import lab_1_hello_world as app

    # Assert Test of My Code vs Expected Result
    assert app.hello_world() == "hello world"


def test_lab02():
    "Test of Lab 2"

    # Import Lab Function for Testing
    from lab02 import lab_2_intro_to_boto3 as app

    # Get Translation from AWS and save print statement to variable output
    output = []
    app.print = lambda r : output.extend([r])
    app.translate_text()

    # Assert Test of My Code vs Expected Result
    assert type(output[0]) is dict
    assert output[0]['TranslatedText'] == "J'apprends à coder dans AWS"


def test_lab03a():
    "Test of Lab 3"
    
    # Import Lab Function for Testing
    from lab03 import lab_3_main_function as app

    # Get Translation from AWS and save return value to a variable
    translate = app.translate_text()

    # Assert Test of My Code vs Expected Result
    assert type(translate) is dict
    assert translate['TranslatedText'] == "J'apprends à coder dans AWS"


def test_lab03b():
    "Test of Lab 3"

    # Import Lab Function for Testing
    from lab03 import lab_3_main_function as app

    # Get Translation from AWS and save print statement to variable output
    output = []
    app.print = lambda r : output.extend([r])
    app.main()

    # Assert Test of My Code vs Expected Result
    assert type(output[0]) is dict
    assert output[0]['TranslatedText'] == "J'apprends à coder dans AWS"


def test_lab04_1():
    "Test of Lab 4 - Step 1"

    # Import Lab Function for Testing
    from lab04 import lab_4_step_1_positional_arguments as app

    # Get Translation from AWS and save print statement to variable output
    output = []
    app.print = lambda r : output.extend([r])
    app.main()

    # Assert Test of My Code vs Expected Result
    assert type(output[0]) is dict
    assert output[0]['TranslatedText'] == "Estoy aprendiendo a programar en AWS"

def test_lab04_2():
    "Test of Lab 4 - Step 2"

    # Import Lab Function for Testing
    from lab04 import lab_4_step_2_keyword_arguments as app

    # Get Translation from AWS and save print statement to variable output
    output = []
    app.print = lambda r : output.extend([r])
    app.main()

    # Assert Test of My Code vs Expected Result
    assert type(output[0]) is dict
    assert output[0]['TranslatedText'] == "Sto imparando a programmare in AWS"


def test_lab05():
    "Test of Lab 5"
    pass


def test_lab06():
    "Test of Lab 6"
    pass


def test_lab07():
    "Test of Lab 7"
    pass


def test_lab08():
    "Test of Lab 8"
    pass


def test_lab09():
    "Test of Lab 9"
    pass
from operations import addition, subtraction, multiplication, division, exponentiation, modulo


def test_addition():
    """
    GIVEN: Two numbers
    WHEN:  passed in to the function addition
    THEN:  the resulting is the addition of the two numbers
    """
    pass


def test_subtraction():
    """
    GIVEN: Two numbers
    WHEN:  passed in to the function subtraction
    THEN:  the resulting is the subtraction of the two numbers
    """
    pass


def test_multiplication():
    """
    GIVEN: Two numbers
    WHEN:  passed in to the function multiplication
    THEN:  the resulting is the multiplication of the two numbers
    """
    pass


def test_division():
    """
    GIVEN: Two numbers
    WHEN:  passed in to the function division
    THEN:  the resulting is the division of the two number
    """
    pass


def test_division_exception_on_zero():
    """
    GIVEN: Two numbers
    WHEN:  passed in to the function division
    THEN:  the resulting is the division of the two number

    Hint: https://stackoverflow.com/questions/23337471/how-to-properly-assert-that-an-exception-gets-raised-in-pytest
    """
    pass

def test_exponentiation():
    """
    GIVEN: Two numbers
    WHEN:  passed in to the function exponentiation
    THEN:  the resulting is the exponentiation of the two number
    """
    pass

def test_modulo():
    """
    GIVEN: two numbers
    WHEN: passed in to the function modulo
    THEN: the resulting is the modulo of the two numbers
    """
    assert modulo(8, 2) == 0
    assert modulo(9, 2) == 1

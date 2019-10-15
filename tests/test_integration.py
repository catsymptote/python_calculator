from app.calc import Calculator


def test_addition():
    calc = Calculator()

    a = calc.do("3+4")
    assert type(a) == float
    assert a == 7.0
    
    b = calc.do("1+2+3")
    assert type(b) == float
    assert b == 6.0

    c = calc.do("1+2+3+4+5+6+7+8+9")
    assert type(c) == float
    assert c == 45.0


def test_subtraction():
    calc = Calculator()

    a = calc.do("8-5")
    assert type(a) == float
    assert a == 3.0
    
    b = calc.do("3-2-1")
    assert type(b) == float
    assert b == 0.0

    c = calc.do("1000-1-1-1-1-1")
    assert type(c) == float
    assert c == 995.0


def test_multiplication():
    calc = Calculator()

    a = calc.do("8*5")
    assert type(a) == float
    assert a == 40.0
    
    b = calc.do("3*2*4")
    assert type(b) == float
    assert b == 24.0

    c = calc.do("3*3*3*3*3*3")
    assert type(c) == float
    assert c == 729.0


def test_division():
    calc = Calculator()

    a = calc.do("40/5")
    assert type(a) == float
    assert a == 8.0
    
    b = calc.do("24/3/2")
    assert type(b) == float
    assert b == 4.0

    c = calc.do("3/3")
    assert type(c) == float
    assert c == 1.0


def test_modulus():
    calc = Calculator()

    a = calc.do("7%2")
    assert type(a) == float
    assert a == 1.0
    
    b = calc.do("40%5")
    assert type(b) == float
    assert b == 0.0

    c = calc.do("13%11")
    assert type(c) == float
    assert c == 2.0


def test_power():
    calc = Calculator()

    a = calc.do("2^5")
    assert type(a) == float
    assert a == 32.0
    
    # Intended to mean (2^3)^5, not 2^(3^5).
    b = calc.do("2^3^5")
    assert type(b) == float
    assert b == 32768.0

    c = calc.do("0^0")
    assert type(c) == float
    assert c == 1.0

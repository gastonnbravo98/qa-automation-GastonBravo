from ejercicio1 import fizzbuzz

def test_multiplo_de_3():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(9) == "Fizz"

def test_multiplo_de_5():
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(10) == "Buzz"

def test_multiplo_de_3_y_5():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"

def test_numero_normal():
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(7) == "7"
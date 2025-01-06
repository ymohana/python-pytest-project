import pytest
def test_one_plus_one():
  assert 1 + 1 == 2

def test_one_plus_two():
  a = 1
  b = 2
  c = 3
  assert a + b == c

def test_divisible_by_Zero():
  with pytest.raises(ZeroDivisionError) as e:
   num = 1/0
   assert 'division by zero' in str(e.num)

product = [
  (2, 3, 6),        # positive integers
  (1, 99, 99),      # identity
  (0, 88, 0),       # zero
  (3, -4, -12),     # positive by negative
  (-5, -5, 25),     # negative by negative
  (2.5, 6.7, 16.75) #float
]

@pytest.mark.parametrize('a, b, product', product)  # we need to make pytest pass the parametrized values into the new test case.                                                     
def test_multiplication(a, b, product):             #That's where we use @pytest.mark.parametrize. Make sure import pytest is already in the test module.
  assert a * b == product                           #@pytest.mark.parametrize is a decorator for the test_multiplication function.



def test_something():
    assert(1 + 2)==(3)
    assert len("hello")==5
    assert ("hello").startswith("h")
    assert ("hello").endswith("o")
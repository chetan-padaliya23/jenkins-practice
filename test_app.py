# Tests for Calculator
import sys
sys.path.insert(0, '.')
from app import add, subtract, multiply, divide

def test_add():
    assert add(5, 3) == 8
    assert add(-1, 1) == 0
    print("✅ Add test pass!")

def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(0, 5) == -5
    print("✅ Subtract test pass!")

def test_multiply():
    assert multiply(6, 7) == 42
    assert multiply(0, 100) == 0
    print("✅ Multiply test pass!")

def test_divide():
    assert divide(15, 3) == 5.0
    assert divide(10, 2) == 5.0
    print("✅ Divide test pass!")

def test_divide_by_zero():
    try:
        divide(10, 0)
        print("❌ Error nahi aaya!")
    except ValueError as e:
        print(f"✅ Zero divide test pass: {e}")

if __name__ == "__main__":
    print("=== Tests Shuru ===")
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    test_divide_by_zero()
    print("=== Saare Tests Pass! ===")
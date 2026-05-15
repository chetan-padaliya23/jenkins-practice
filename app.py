# Simple Calculator App
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Zero se divide nahi kar sakte!")
    return a / b

if __name__ == "__main__":
    print("=== Chetan Ka Calculator ===")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 x 7 = {multiply(6, 7)}")
    print(f"15 / 3 = {divide(15, 3)}")
    print("Calculator successfully run hua!")
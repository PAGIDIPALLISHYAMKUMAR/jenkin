from app import add

def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    print("All tests passed!")

if __name__ == "__main__":
    test_add()

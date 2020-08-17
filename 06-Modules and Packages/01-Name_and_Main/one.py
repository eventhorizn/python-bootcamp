def func():
    print("func() in One.py")

print("Top Level in One.py")

if __name__ == "__main__":
    print("One.py is being run directly")
else:
    print("one.py has been imported")
import one

print("Top Level in two.py")

one.func()

if __name__ == '__main__':
    # run the script
    print("two.py is being run directly")
else:
    print('two.py has been imported')
import os
from main import *
from test_cases import *


#os.system('clear') # For windows: os.system('cls'). For macOS and Linux: os.system('clear')
print("-------------------------------")
passed = 0
failed = 0
i = 0
for test in test_case:
    print("Input")
    for t in test:
        print(f"{t}")
    result = ghost_legs(test)
    print(f"Expected: {expected[i]}")
    print(f"Actual:   {result}")

    if expected[i] == result:
        passed += 1
        print("=====PASS=====")
    else:
        failed += 1
        print("=====FAIL=====")
    i += 1
    print("-------------------------------")
print(f"Passed: {passed}, Failed: {failed}")
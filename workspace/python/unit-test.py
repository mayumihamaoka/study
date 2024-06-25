def main():
    print(test1())
    print(GIVEN_0_AND_5_WHEN_sum_THEN_5())

# GIVEN 2 AND 3 WHEN sum THEN 5
def test1():
    # GIVEN
    first = 2
    second = 3
    
    # WHEN
    result = sumMay(first, second)

    # THEN
    expected = 5
    return f"GIVEN 2 AND 3 WHEN sum THEN 5: {result == expected}"

def GIVEN_0_AND_5_WHEN_sum_THEN_5():
    # GIVEN
    first = 0
    second = 5
    
    # WHEN
    result = sumMay(first, second)

    # THEN
    expected = 5
    return f"GIVEN_0_AND_5_WHEN_sum_THEN_5: {result == expected}"

def sumMay(first, second):
    return first + second

if __name__ == "__main__":
    main()

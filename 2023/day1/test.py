from pt2 import get_first_digit, get_second_digit

def test_function(function, test_cases):
    for indata, outdata in test_cases.items():
        result = function(indata)
        if result != outdata:
            print('Test failure!')
            print('Input: {indata}'.format(indata=indata))
            print('Expected output: {outdata}'.format(outdata=outdata))
            print('Obtained output: {result}'.format(result=result))
            break

def get_first_digit_test():
    test_cases = {
        'two1nine': 2,
        'abcone2threexyz': 1,
        '4nineeightseven2': 4,
        'dowek5gfourqow1': 5,
        'doweightek5gfourqow1': 8,
    }
    test_function(get_first_digit, test_cases)

def get_second_digit_test():
    test_cases = {
        'two1nine': 9,
        'abcone2threexyz': 3,
        '4nineeightseven2': 2,
        'dowek5gfourqo1w': 1,
    }
    test_function(get_second_digit, test_cases)

get_first_digit_test()
get_second_digit_test()
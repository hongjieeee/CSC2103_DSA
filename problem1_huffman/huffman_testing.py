
##this file only uses predetermined inputs within the code

from problem1_huffman import (count_frequencies,
                              build_huffman_tree,
                              build_codes,
                              encode_text,
                              decode_text,
                              )
##Initial dec's
check_pass = 0
check_fail = 0

def check_result(test_name, expected, actual):

    global check_pass #globals are used so that the variables can be accessed throughout the files.
    global check_fail

    print("\nTest : ", test_name)
    print("Expected : ", expected)
    print("Actual : ", actual)

    if expected == actual:
        print("Status :  PASS")
        check_pass += 1
    else:
        print("Status : FAILED")
        check_fail += 1

def encode_and_decode(text):
    frequencies = count_frequencies(text)
    tree = build_huffman_tree(frequencies)
    codes = build_codes(tree)
    encoded_text = encode_text(text,codes)
    decoded_text = decode_text(encoded_text, tree)

    return frequencies, tree, codes, encoded_text, decoded_text


def test_frequency_counting():
    actual = count_frequencies
    expected = {
        "b": 1,
        "a": 3,
        "n": 2
    }
    check_result(
        "Frequency counting",
        expected,
        actual
    )

def test_normal_word():
    text = "banana"
    frequencies, tree, codes, encoded_text, decoded_text = (encode_and_decode(text))
    check_result("Encode and decode normal word",text,decoded_text)

def test_text_with_space():
    text = "hello world"
    frequencies, tree, codes, encoded_text, decoded_text = (encode_and_decode(text))
    check_result("Encode and decode text with spacing",text,decoded_text)


    check_result("Space receives a Huffman code",True,"" in codes)

def test_single_character():
    text="aaaaa"
    frequencies, tree, codes, encoded_text, decoded_text = (encode_and_decode(text))

    check_result("Single char code", "0", codes["a"])

    check_result("single character encoded result", "00000", encoded_text)

    check_result("Single character decoded resilt", text, decoded_text)

def test_uppercase_and_lowercase():
    text = "AaAaBbBb"

    frequencies, tree, codes, encoded_text, decoded_text = (encode_and_decode(text))

    check_result("Uppercase and lowercase decoding", text, decoded_text)

    check_result("Uppercase A frequency",2,frequencies ["A"])

    check_result("Lowercase a frequency",2,frequencies["a"])

def test_prefix_free_codes():
    text = "aaabbcdef"

    frequencies, tree, codes, encoded_text, decoded_text = (
        encode_and_decode(text)
    )

    code_list = []

    for character in codes:
        code_list.append(codes[character])

    prefix_free = True

    for first_code in code_list:
        for second_code in code_list:

            if first_code != second_code:
                if second_code.startswith(first_code):
                    prefix_free = False

    check_result(
        "Huffman codes are prefix-free",
        True,
        prefix_free
    )


def test_invalid_bit():
    text = "banana"

    frequencies, tree, codes, encoded_text, decoded_text = (
        encode_and_decode(text)
    )

    error_detected = False

    try:
        decode_text(encoded_text + "2", tree)

    except ValueError:
        error_detected = True

    check_result(
        "Invalid encoded bit is rejected",
        True,
        error_detected
    )

def test_huffman_capabilities():
    text = "aaaaaaaaaabbbbbcccd A!"

    frequencies, tree, codes, encoded_text, decoded_text = (
        encode_and_decode(text)
    )

    # Check the complete encode-decode process.
    check_result(
        "Capability test round-trip",
        text,
        decoded_text
    )

    # Check the expected frequencies.
    expected_frequencies = {
        "a": 10,
        "b": 5,
        "c": 3,
        "d": 1,
        " ": 1,
        "A": 1,
        "!": 1
    }

    check_result(
        "Capability test frequency counting",
        expected_frequencies,
        frequencies
    )

    # Frequent characters should receive shorter codes.
    greedy_behavior = (
        len(codes["a"]) < len(codes["b"])
        and len(codes["b"]) < len(codes["c"])
        and len(codes["c"]) < len(codes["d"])
    )

    check_result(
        "Frequent characters receive shorter codes",
        True,
        greedy_behavior
    )

    # Check that spaces are supported.
    check_result(
        "Space receives a Huffman code",
        True,
        " " in codes
    )

    # Check that uppercase and lowercase are different.
    check_result(
        "Uppercase and lowercase are separate",
        True,
        "a" in codes and "A" in codes
    )

    # Check whether compression occurred.
    original_bits = len(text.encode("utf-8")) * 8
    compression_achieved = len(encoded_text) < original_bits

    check_result(
        "Encoded data is smaller than original data",
        True,
        compression_achieved
    )

def run_tests():
    print("=" * 55)
    print("HUFFMAN CODING TESTING AND VALIDATION")
    print("=" * 55)

    test_frequency_counting()
    test_normal_word()
    test_text_with_space()
    test_single_character()
    test_uppercase_and_lowercase()
    test_prefix_free_codes()
    test_invalid_bit()
    test_huffman_capabilities()

    print("\n" + "=" * 55)
    print("TEST SUMMARY")
    print("=" * 55)
    print("Passed:", check_pass)
    print("Failed:", check_fail)

    if check_fail == 0:
        print("Overall result: ALL TESTS PASSED")
    else:
        print("Overall result: SOME TESTS FAILED")


run_tests()



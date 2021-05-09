
def capital_indexes(text):
    result = []

    for index, letter in enumerate(text):
        if letter == letter.upper():
            result.append(index)

    return result


def mid(text):
    if len(text) % 2 == 0:
        return ""
    else:
        return text[int((len(text) - 1) / 2)]


statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}


def online_count(d: dict):
    counter = 0
    for v in d.values():
        if v == "online":
            counter += 1

    return counter


def random_number():
    import random

    return random.randint(1, 100)


def only_ints(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return True
    else:
        return False


def double_letters(text):
    prev_letter = ""

    for letter in text:
        if letter == prev_letter:
            return True
        else:
            prev_letter = letter

    return False


def add_dots(text):
    result = ""
    for letter in text:
        result += f"{letter}."

    return result[:-1]


def remove_dots(text):
    result = ""
    for letter in text:
        if letter != ".":
            result += letter

    return result


def count(text: str):
    return len(text.split("-"))


def is_anagram(text_a, text_b):
    return sorted(text_a.lower()) == sorted(text_b.lower())


def flatten(input_list: list):
    result = []

    for element in input_list:
        if isinstance(element, list):
            result += flatten(element)
        else:
            result.append(element)

    return result


def largest_difference(input_list):
    return max(input_list) - min(input_list)


def div_3(number):
    return number % 3 == 0


def div_n(divider):

    def div_by(dividend):
        return dividend % divider == 0

    return div_by


def get_row_col(coordinates):
    x_label = "ABC"
    y_label = "123"

    for i, cords in enumerate(zip(x_label, y_label)):
        if cords[0] == coordinates[0]:
            x_coordinate = i
        if cords[1] == coordinates[1]:
            y_coordinate = i

    return x_coordinate, y_coordinate


def up_down(number):
    return number - 1, number + 1


def consecutive_zeros(binary_string: str) -> int:
    global_counter = 0
    current_counter = 0

    for number in binary_string:
        if number == "0":
            current_counter += 1
        else:
            if current_counter > global_counter:
                global_counter = current_counter
            current_counter = 0

    return global_counter


def all_equal(input_list: list) -> bool:
    input_list.sort()

    return input_list[0] == input_list[-1]


def triple_and(a: bool, b: bool, c: bool) -> bool:
    if a and b and c:
        return True
    else:
        return False


def convert(number_list: list) -> list:
    return [str(x) for x in number_list]


def zap(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists are not the same length!")

    result = []
    for el in zip(list1, list2):
        result.append(el)

    return result


def validate(function):
    if "def" not in function:
        return "missing def"
    elif ":" not in function:
        return "missing :"
    elif "(" not in function or ")" not in function:
        return "missing paren"
    elif "("+")" in function:
        return "missing param"
    elif "    " not in function:
        return "missing indent"
    elif "validate" not in function:
        return "wrong name"
    elif "return" not in function:
        return "missing return"
    else:
        return True


def list_xor(n, list_1, list_2):
    if n in list_1 and n in list_2:
        return False
    if n not in list_1 and n not in list_2:
        return False
    else:
        return True


# assert list_xor(1, [1, 2, 3], [4, 5, 6]) is True
# assert list_xor(1, [0, 2, 3], [1, 5, 6]) is True
# assert list_xor(1, [1, 2, 3], [1, 5, 6]) is False
# assert list_xor(1, [0, 0, 0], [4, 5, 6]) is False


def param_count(*args):
    return len(args)


def format_number(number):
    result = ""
    for i, num in enumerate(str(number)[::-1]):
        if i == 0:
            result += num
        elif i % 3 == 0:
            result += f",{num}"
        else:
            result += num

    return result[::-1]


print(format_number(10000000))

import os
import pytest

# @pytest.fixture
# def sample_data():
#     return [1, 2, 5]

# def test_sum(sample_data):
#     actual_sum = sum(sample_data)
#     expected_sum = 8
#     assert actual_sum == expected_sum

# def test_len(sample_data):
#     actual_len = len(sample_data)
#     expected_len = 3
#     assert actual_len == expected_len

# @pytest.fixture
# def first_name():
#     return "Joe"

# @pytest.fixture
# def last_name():
#     return "Smith"

# @pytest.fixture
# def item():
#     return "an apple"

# @pytest.fixture()
# def full_sentence(first_name, last_name, item):
#     return f"{first_name} {last_name} has {item}"


# def test_sentence_full_is_correct(full_sentence):
#     expected_sentence = "Joe Smith has an apple"
#     assert full_sentence == expected_sentence

# def test_sentence_has_word_has(full_sentence):
#     assert "has" in full_sentence

# @pytest.fixture()
# def number():
#     raise NotImplementedError
#     return 42

# def test_number(number):
#     assert number == 30

# @pytest.fixture
# def temp_file():
#     file_path = "temp_notes_file.txt"

#     if not os.path.exists(file_path):
#         with open(file_path, "w") as f:
#             f.write("Notes for pytest course\n")

#     yield file_path

#     os.remove(file_path)


# def test_file_starts_with_name(temp_file):
#     with open(temp_file, "r") as f:
#         contents = f.read()
#     assert contents == "Notes for pytest course\n"

# def test_file_write_task(temp_file):
#     with open(temp_file, "a") as f:
#         f.write("task_1")

#     with open(temp_file, "r") as f:
#         contents = f.read()
#     assert contents == "Notes for pytest course\ntask_1"


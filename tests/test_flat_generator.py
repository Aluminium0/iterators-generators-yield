from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from flat_generator import flat_generator


def test_2():
    list_of_lists_1 = [
        ["a", "b", "c"],
        ["d", "e", "f", "h", False],
        [1, 2, None],
    ]

    for flat_generator_item, check_item in zip(
        flat_generator(list_of_lists_1),
        ["a", "b", "c", "d", "e", "f", "h", False, 1, 2, None],
    ):
        assert flat_generator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "h",
        False,
        1,
        2,
        None,
    ]


if __name__ == "__main__":
    test_2()

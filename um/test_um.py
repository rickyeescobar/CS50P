import um
import pytest

def test_count_1():
    assert um.count("um") == 1

def test_count_punctuation():
    assert um.count("um?") == 1

def test_um_sentence():
    assert um.count("Um, thanks for the album") == 1

def test_um_sentence_um():
    assert um.count("Um, thanks, um...") == 2

if __name__ == "__main__":
    main()

import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("banana", "7")
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(4, 4)

    assert encrypt_message("banana", 7) == "ananab"

    assert encrypt_message("banana", 1) == "b_anana"

    assert encrypt_message("banana", 4) == "an_anab"

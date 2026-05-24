from hsutt_starter.main import greet


def test_greet_returns_expected_message() -> None:
    assert greet() == "Hello, HsuTT starter!"

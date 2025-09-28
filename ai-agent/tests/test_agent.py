import os
import sys
import importlib
import types
from unittest import mock

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

try:
    importlib.import_module("src.api_client")
except Exception:
    fake = types.ModuleType("src.api_client")

    def ask_gemini(prompt):
        return "MOCK_RESPONSE"

    fake.ask_gemini = ask_gemini
    sys.modules["src.api_client"] = fake

from src.agent import handle_command
from src import utils


def test_utils_normalize_and_extract_prefix():
    assert utils.normalize_command("  hello   world  ") == "hello world"
    prefix, rest = utils.extract_prefix("Summarize   These  lines ")
    assert prefix == "summarize"
    assert rest == "These lines"
    prefix2, rest2 = utils.extract_prefix("hello")
    assert prefix2 == "hello"
    assert rest2 == ""


def test_summarize_calls_api_and_returns():
    with mock.patch("src.agent.ask_gemini", return_value="SHORT SUMMARY") as patched:
        result = handle_command("summarize The quick brown fox")
        patched.assert_called_once_with("Summarize this text: The quick brown fox")
        assert result == "SHORT SUMMARY"


def test_question_calls_api_and_returns():
    with mock.patch("src.agent.ask_gemini", return_value="ANSWER") as patched:
        result = handle_command("question What is 2+2?")
        patched.assert_called_once_with("Answer this: What is 2+2?")
        assert result == "ANSWER"


def test_fallback_calls_api_with_original_command():
    with mock.patch("src.agent.ask_gemini", return_value="JOKE") as patched:
        cmd = "Tell me a joke"
        result = handle_command(cmd)
        patched.assert_called_once_with(cmd)
        assert result == "JOKE"
 

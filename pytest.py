import pytest

from unittest.mock import patch
from cs325_project3_final import OllamaModel 

@pytest.fixture
def ollama_model():
    return OllamaModel(model_name="test-model")

@pytest.mark.parametrize("question, mock_response, expected_result", [
    ("This is awesome!", {"response": "positive"}, "positive"),
    ("I hate this.", {"response": "negative"}, "negative"),
    ("I am indifferent.", {"response": "neutral"}, "neutral"),
])
def test_ask_question_valid_responses(question, mock_response, expected_result):
    model = OllamaModel(model_name="test-model")
    with patch("your_module.ollama.generate", return_value=mock_response):
        result = model.ask_question(question)
        assert result == expected_result
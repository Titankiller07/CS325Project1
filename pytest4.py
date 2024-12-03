import pytest
from unittest.mock import patch, mock_open
from cs325_project3_final import SentimentAnalyzer, OllamaModel, FileReader  # Adjust this import

@pytest.fixture
def mock_sentiment_analyzer():
    model = OllamaModel(model_name="test-model")
    file_reader = FileReader(file_path_pattern="test_file_{}.txt", num_files=1)
    analyzer = SentimentAnalyzer(ollama_model=model, file_reader=file_reader, output_path_pattern="output_{}.txt")
    return analyzer

def test_analyze_lines(mock_sentiment_analyzer):
    # Mock the file reading and Ollama model response
    with patch("builtins.open", mock_open(read_data="This is amazing!\nI don't care.\n")):
        with patch("your_module.ollama.generate", return_value={"response": "positive"}):
            mock_sentiment_analyzer.file_reader.read_files()
            mock_sentiment_analyzer.analyze_lines()
    
    # Check that the output files were written (mocked, no real files are created)
    mock_sentiment_analyzer.file_reader.get_lines("test_file_1.txt")  # Check the file reading step
    assert mock_sentiment_analyzer.file_reader.get_lines("test_file_1.txt") == ["This is amazing!\n", "I don't care.\n"]
    # Ensure the sentiment responses were processed correctly (positive for the first line)
    assert "positive" in mock_sentiment_analyzer.output_path_pattern.format(1)  # Check sentiment classification

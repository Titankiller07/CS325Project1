import os
import pytest
from unittest.mock import patch
from cs325_project3_final import FileReader  # Adjust this import

@pytest.fixture
def mock_file_reader():
    return FileReader(file_path_pattern="missing_file_{}.txt", num_files=2)

def test_read_files_file_not_found(mock_file_reader):
    with patch("builtins.open", side_effect=FileNotFoundError):
        mock_file_reader.read_files()
    
    # Ensure files not found are handled correctly
    assert "missing_file_1.txt" in mock_file_reader.files_content
    assert "missing_file_2.txt" in mock_file_reader.files_content
    assert mock_file_reader.get_lines("missing_file_1.txt") == []
    assert mock_file_reader.get_lines("missing_file_2.txt") == []
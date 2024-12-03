import os
import pytest
from unittest.mock import mock_open, patch
from cs325_project3_final import FileReader  # Adjust this import

@pytest.fixture
def mock_files():
    return FileReader(file_path_pattern="test_file_{}.txt", num_files=2)

def test_read_files(mock_files):
    # Mock open for two files
    with patch("builtins.open", mock_open(read_data="line 1\nline 2\n")):
        mock_files.read_files()
    
    assert "test_file_1.txt" in mock_files.files_content
    assert "test_file_2.txt" in mock_files.files_content
    assert mock_files.get_lines("test_file_1.txt") == ["line 1\n", "line 2\n"]
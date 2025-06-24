import pytest
import tempfile
import shutil
from pathlib import Path
from unittest.mock import Mock, patch
import json
import os


@pytest.fixture
def temp_dir():
    """Create a temporary directory for testing."""
    temp_path = tempfile.mkdtemp()
    yield Path(temp_path)
    shutil.rmtree(temp_path)


@pytest.fixture
def mock_openai_client():
    """Mock OpenAI client for testing."""
    with patch('openai.OpenAI') as mock_client:
        mock_instance = Mock()
        mock_client.return_value = mock_instance
        
        # Mock completion response
        mock_response = Mock()
        mock_response.choices = [Mock(message=Mock(content="Test response"))]
        mock_instance.chat.completions.create.return_value = mock_response
        
        yield mock_instance


@pytest.fixture
def sample_questions_file(temp_dir):
    """Create a sample questions file for testing."""
    file_path = temp_dir / "test_questions.txt"
    content = """Question 1:
What is the capital of France?

Question 2:
What is 2 + 2?

Question 3:
Explain quantum physics.
"""
    file_path.write_text(content)
    return file_path


@pytest.fixture
def sample_json_data():
    """Provide sample JSON data for testing."""
    return [
        {"instruction": "What is the capital of France?", "output": "Paris"},
        {"instruction": "What is 2 + 2?", "output": "4"},
    ]


@pytest.fixture
def mock_env_variables():
    """Mock environment variables for testing."""
    with patch.dict(os.environ, {'OPENAI_KEY': 'test-api-key'}):
        yield


@pytest.fixture
def mock_file_system(temp_dir):
    """Create a mock file system structure for testing."""
    # Create directories
    (temp_dir / "principles").mkdir()
    (temp_dir / "gpt4").mkdir()
    
    # Create sample principle files
    for i in range(1, 4):
        file_path = temp_dir / "principles" / f"principle_{i}.txt"
        file_path.write_text(f"Question {i}:\\nSample question {i}")
    
    return temp_dir


@pytest.fixture(autouse=True)
def cleanup_test_artifacts():
    """Automatically clean up any test artifacts after each test."""
    yield
    # Clean up any test-generated files
    test_output_dirs = ['gpt4', 'test_output']
    for dir_name in test_output_dirs:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)


@pytest.fixture
def capture_logs():
    """Capture log messages during tests."""
    import logging
    
    class LogCapture:
        def __init__(self):
            self.records = []
            self.handler = logging.Handler()
            self.handler.emit = lambda record: self.records.append(record)
        
        def __enter__(self):
            logging.root.addHandler(self.handler)
            return self
        
        def __exit__(self, *args):
            logging.root.removeHandler(self.handler)
        
        def get_messages(self, level=None):
            if level:
                return [r.getMessage() for r in self.records if r.levelno >= level]
            return [r.getMessage() for r in self.records]
    
    return LogCapture()


@pytest.fixture
def mock_time():
    """Mock time-related functions for consistent testing."""
    with patch('time.time', return_value=1234567890):
        with patch('time.sleep', return_value=None):
            yield
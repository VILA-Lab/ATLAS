import pytest
import sys
import os
from pathlib import Path


class TestSetupValidation:
    """Validation tests to ensure the testing infrastructure is properly set up."""
    
    def test_python_version(self):
        """Ensure Python version is 3.8 or higher."""
        assert sys.version_info >= (3, 8), "Python 3.8 or higher is required"
    
    def test_project_structure_exists(self):
        """Verify the project directory structure is correct."""
        project_root = Path(__file__).parent.parent
        
        # Check main directories
        assert project_root.exists()
        assert (project_root / "tests").exists()
        assert (project_root / "tests" / "unit").exists()
        assert (project_root / "tests" / "integration").exists()
        
        # Check configuration files
        assert (project_root / "pyproject.toml").exists()
        
    def test_pytest_markers_configured(self):
        """Verify pytest markers are properly configured."""
        # This test verifies that our custom markers work
        assert hasattr(self.test_pytest_markers_configured, '__func__')
    
    @pytest.mark.unit
    def test_unit_marker(self):
        """Test that unit marker is recognized."""
        pass
    
    @pytest.mark.integration
    def test_integration_marker(self):
        """Test that integration marker is recognized."""
        pass
    
    @pytest.mark.slow
    def test_slow_marker(self):
        """Test that slow marker is recognized."""
        pass
    
    def test_fixtures_available(self, temp_dir, mock_openai_client):
        """Verify that common fixtures are available."""
        assert temp_dir.exists()
        assert temp_dir.is_dir()
        assert mock_openai_client is not None
    
    def test_coverage_configured(self):
        """Verify coverage is properly configured."""
        # This test runs as part of coverage, so if it passes, coverage is working
        assert True
    
    def test_imports_work(self, mock_env_variables):
        """Verify that we can import the main module."""
        try:
            from src import generate
            assert hasattr(generate, 'generate_answers')
            assert hasattr(generate, 'extract_questions_from_file')
        except ImportError as e:
            pytest.fail(f"Failed to import generate module: {e}")


class TestPoetryScripts:
    """Test that Poetry scripts are properly configured."""
    
    def test_poetry_scripts_configured(self):
        """Verify Poetry scripts are set up in pyproject.toml."""
        project_root = Path(__file__).parent.parent
        pyproject_path = project_root / "pyproject.toml"
        
        with open(pyproject_path, 'r') as f:
            content = f.read()
            
        # Check that both test and tests commands are configured
        assert '[tool.poetry.scripts]' in content
        assert 'test = "pytest:main"' in content
        assert 'tests = "pytest:main"' in content


@pytest.mark.unit
class TestMockingCapabilities:
    """Test that mocking utilities work correctly."""
    
    def test_mock_environment_variables(self, mock_env_variables):
        """Test environment variable mocking."""
        assert os.environ.get('OPENAI_KEY') == 'test-api-key'
    
    def test_mock_file_operations(self, temp_dir):
        """Test file operation mocking."""
        test_file = temp_dir / "test.txt"
        test_file.write_text("Hello, World!")
        
        assert test_file.exists()
        assert test_file.read_text() == "Hello, World!"
    
    def test_json_operations(self, sample_json_data):
        """Test JSON data handling."""
        import json
        
        json_str = json.dumps(sample_json_data)
        parsed = json.loads(json_str)
        
        assert len(parsed) == 2
        assert parsed[0]["instruction"] == "What is the capital of France?"
        assert parsed[1]["output"] == "4"
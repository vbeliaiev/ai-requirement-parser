import pytest

@pytest.fixture
def sample_requirement():
  return "Build a file sharing app with search and user auth"

@pytest.fixture
def valid_api_response():
  """Typical api response for mocks"""
  return {
    "features": ["file upload", "search", "login"],
    "modules": ["storate", "search_engine", "auth"]
  }

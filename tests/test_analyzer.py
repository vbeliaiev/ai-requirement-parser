import pytest
from unittest.mock import Mock, patch
import json

from src.analyzer import analyze_requirements

class TestAnalyzerUnit:
  """Tests with mock - without real api call"""

  @patch('src.analyzer.OpenAI')
  def test_returns_parsed_json(self, mock_openai_class, valid_api_response):
    # Setup Mock
    mock_client = Mock()
    mock_openai_class.return_value = mock_client
    mock_client.responses.create.return_value = Mock(
      output_text = json.dumps(valid_api_response)
    )

    result = analyze_requirements("any text")

    assert result == valid_api_response
    assert "features" in result
    assert "modules" in result

  @patch('src.analyzer.OpenAI')
  def test_raises_on_invalid_fields(self, mock_openai_class):
    mock_client = Mock()
    mock_openai_class.return_value = mock_client
    mock_client.responses.create.return_value = Mock(
      output_text='not a json'
    )

    with pytest.raises(json.JSONDecodeError):
      analyze_requirements('any text')

  @patch('src.analyzer.OpenAI')
  def test_raises_on_missing_fields(self, mock_openai_class):
    mock_client = Mock()
    mock_openai_class.return_value = mock_client
    mock_client.responses.create.return_value = Mock(
      output_text='{"something": "else"}'
    )

    with pytest.raises(ValueError, match="missing required fields"):
      analyze_requirements("any text")

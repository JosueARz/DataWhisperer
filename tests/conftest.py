import pytest

@pytest.fixture
def fake_llm_client():
    class FakeClient:
        def chat(self, messages):
            return "# Código de prueba\nprint('OK')"
    return FakeClient()


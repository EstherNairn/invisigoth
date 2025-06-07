class MockClient:
    def query(self, prompt: str) -> str:
        """
        Return a static fake goal for offline testing or dry runs.
        """
        return '[{"id": "goal_mock", "description": "Mock goal", "filename": "mock.py", "prompt": "Do nothing", "dependencies": [], "status": "pending"}]'

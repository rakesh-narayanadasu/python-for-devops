# Module 14: Testing & Debugging

## 📖 What You'll Learn
- Unit testing with pytest
- Test automation
- Debugging techniques
- Best practices for reliable code

---

## 1. Unit Testing with pytest

### Code Example

```python
# test_server_utils.py
import pytest

def validate_port(port):
    """Validate port number"""
    if not isinstance(port, int):
        raise TypeError("Port must be integer")
    if port < 1 or port > 65535:
        raise ValueError("Port out of range")
    return True

# Tests
def test_validate_port_valid():
    """Test valid port"""
    assert validate_port(8080) == True
    assert validate_port(80) == True
    assert validate_port(443) == True

def test_validate_port_invalid_type():
    """Test invalid type"""
    with pytest.raises(TypeError):
        validate_port("8080")

def test_validate_port_out_of_range():
    """Test out of range"""
    with pytest.raises(ValueError):
        validate_port(0)
    with pytest.raises(ValueError):
        validate_port(99999)

# Run tests: pytest test_server_utils.py
```

---

## 2. Testing Best Practices

### Code Example

```python
import pytest
from unittest.mock import Mock, patch

class ServerAPI:
    def __init__(self, base_url):
        self.base_url = base_url
    
    def get_status(self):
        import requests
        response = requests.get(f"{self.base_url}/status")
        return response.json()

# Test with mocking
def test_get_status():
    """Test API call with mock"""
    with patch('requests.get') as mock_get:
        # Setup mock
        mock_response = Mock()
        mock_response.json.return_value = {'status': 'healthy'}
        mock_get.return_value = mock_response
        
        # Test
        api = ServerAPI('http://example.com')
        result = api.get_status()
        
        # Assertions
        assert result['status'] == 'healthy'
        mock_get.assert_called_once_with('http://example.com/status')

# Fixtures
@pytest.fixture
def sample_config():
    """Provide test configuration"""
    return {
        'host': 'localhost',
        'port': 8080,
        'timeout': 30
    }

def test_with_fixture(sample_config):
    """Test using fixture"""
    assert sample_config['host'] == 'localhost'
    assert sample_config['port'] == 8080
```

---

## 3. Debugging Techniques

### Code Example

```python
import pdb
import logging

# Using print debugging (basic)
def process_data(data):
    print(f"DEBUG: Processing {len(data)} items")
    for item in data:
        print(f"DEBUG: Item = {item}")
        result = item * 2
        print(f"DEBUG: Result = {result}")
    return result

# Using logging (better)
logger = logging.getLogger(__name__)

def process_data_logged(data):
    logger.debug(f"Processing {len(data)} items")
    for item in data:
        logger.debug(f"Item = {item}")
        result = item * 2
        logger.debug(f"Result = {result}")
    return result

# Using debugger (best for complex issues)
def complex_function(x, y):
    result = x + y
    pdb.set_trace()  # Debugger will stop here
    result = result * 2
    return result

# Using assertions
def divide(a, b):
    assert b != 0, "Cannot divide by zero"
    assert isinstance(a, (int, float)), "a must be numeric"
    assert isinstance(b, (int, float)), "b must be numeric"
    return a / b
```

---

## 4. Integration Testing

### Code Example

```python
import pytest
import subprocess

def test_deployment_script():
    """Test deployment script execution"""
    result = subprocess.run(
        ['python', 'deploy.py', '--dry-run'],
        capture_output=True,
        text=True
    )
    
    assert result.returncode == 0
    assert 'Success' in result.stdout

def test_api_endpoint():
    """Test API endpoint"""
    import requests
    response = requests.get('http://localhost:8080/health')
    
    assert response.status_code == 200
    data = response.json()
    assert data['status'] == 'healthy'

@pytest.mark.slow
def test_long_running_process():
    """Test that takes a long time"""
    # This test is marked as slow
    import time
    time.sleep(5)
    assert True

# Run only fast tests: pytest -m "not slow"
```

---

## 📝 Key Takeaways

✅ **Write tests** - Catch bugs early
✅ **Use pytest** - Modern testing framework
✅ **Mock external dependencies** - Isolate tests
✅ **Use fixtures** - Reusable test data
✅ **Debug systematically** - Use proper tools
✅ **Test automation** - Run tests in CI/CD

---

## Next Module

Ready for **Module 15: Final Projects**? 🎯

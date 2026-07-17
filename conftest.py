pytest_plugins = ["pytest_playwright"]

def pytest_addoption(parser):
    """Registers custom command line arguments globally at initialization."""
    parser.addoption(
        "--ids", 
        action="store", 
        default=None, 
        help="Comma-separated list of Excel Test Case IDs to execute (e.g., TS-001,TS-002)"
    )
    parser.addoption(
        "--limit", 
        action="store", 
        default=None, 
        type=int, 
        help="Limit the total execution to the first N test cases found in Excel"
    )
    parser.addoption(
        "--feature-file",
        action="append",
        default=[],
        help="Run only scenarios whose feature file name or path contains the given text. Repeat or use comma-separated values."
    )
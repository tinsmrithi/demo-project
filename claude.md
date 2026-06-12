# Weather Demo – AI-Assisted Python Development

## Project Overview
A minimal Python project that models and displays weather data using clean
print-based output. Built to practise AI-assisted workflows: code generation,
test generation, code review, and PR creation using Claude Code.

## Tech Stack
- **Language**: Python 3.10+
- **Testing**: pytest + pytest-cov
- **Style Guide**: PEP 8
- **IDE**: IntelliJ IDEA with Python plugin

## Project Structure
- `src/` – Application source code
- `src/weather.py` – Weather data logic and validation
- `src/display.py` – Formatted print output functions
- `tests/` – Pytest test files (naming: `test_<filename>.py`)
- `.claude/commands/` – Custom slash commands for AI workflow

## Coding Conventions
- Use snake_case for variables, functions, and file names
- Use UPPER_SNAKE_CASE for module-level constants
- Use strict equality checks (`==`, `is`) appropriately
- Always validate inputs at the top of functions before any logic
- All functions must have a clear single responsibility
- Every function must have a docstring explaining what it does
- Prefer f-strings over `.format()` or `%` formatting

## Type & Safety Rules
- Add type hints to all function signatures
- Never silently swallow exceptions — always raise with a clear message
- Never log or print sensitive data
- Validate all external inputs before use

## Error Handling
- Raise `ValueError` for invalid input data
- Raise `TypeError` for wrong data types when needed
- Always include a human-readable message in raised exceptions

## Testing Guidelines
- Use pytest as the test runner (`pytest` or `pytest --cov=src`)
- Place all test files in the `tests/` directory
- Name test files: `test_<source_filename>.py`
- Name test functions: `test_<function>_<behavior>_when_<condition>`
- Cover happy path, edge cases, and error scenarios
- Use `capsys` fixture to capture and assert print output
- Use `pytest.raises` for all exception testing
- Each test must be independent — no shared mutable state

## Commands
- `pytest` – Run all tests
- `pytest --cov=src` – Run tests with coverage report
- `pytest -v` – Run tests in verbose mode
- `python -m src.display` – Run display output manually

## Claude Slash Commands
- `/generate-tests` – Auto-generate pytest tests for all src files
- `/review-code` – Get a structured senior-level code review
- `/create-pr` – Generate a professional PR description from current changes

##Tone and Style
- Clear and concise language
- Professional and respectful tone
- Focus on constructive feedback and continuous improvement
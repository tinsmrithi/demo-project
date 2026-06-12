Generate pytest unit tests for all functions in `src/`. Be fast – do NOT over-analyze.

Rules:
- Read ALL src files in a single parallel batch first
- Separate functions into two buckets:
    1. **Correct code** – no bugs, no security issues, follows project conventions
    2. **Broken/problematic code** – has bugs, missing validation, or convention violations
- Write tests ONLY for bucket 1 (correct code)
- For each testable function write 2-3 tests max: one happy path, one edge case
- Write test files to `tests/test_<filename>.py`
- Use descriptive names: `test_<function>_<expected behavior>_when_<condition>`
- Use `capsys` fixture for testing print output
- Use `pytest.raises` for exception testing
- Write ALL test files in a single parallel batch
- Do NOT use subagents – do everything directly
- Do NOT explain the tests – just write them and run `pytest`
- Do NOT retry if tests fail. Report the failure and stop.

After writing and running tests, print a summary:

### Skipped (needs fixing first)
For each skipped function, list:
- Function name
- File and line number
- What's wrong (one line)

Tell the user: "Fix these issues, then re-run `/generate-tests` to cover them."

Go straight to writing code. No planning, no analysis output, no summaries before writing.
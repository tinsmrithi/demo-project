Analyze all staged and unstaged changes in this repository compared to the main branch. Include untracked files as new additions. Then generate a professional pull request description.

IMPORTANT: You MUST always produce the full formatted PR output below, regardless of how small or large the changes are. Even for a single line change, always generate every section.

Use this exact format:

## PR Title
`<short descriptive title under 70 characters>`

## Summary
- <bullet point 1: what changed and why>
- <bullet point 2: what changed and why>
- <bullet point 3 (optional)>

## Changes Detail
| File | Change Type | Description |
|------|-------------|-------------|
| `<file path>` | Added / Modified / Deleted | <brief description> |

## Testing Steps
1. <step 1>
2. <step 2>
3. <step 3>

## Checklist
- [ ] Tests added/updated
- [ ] Documentation updated (if applicable)
- [ ] No breaking changes
- [ ] No sensitive data exposed

If there are no changes at all (no staged, unstaged, or untracked files), still output the format above but note "No changes detected" in each section.
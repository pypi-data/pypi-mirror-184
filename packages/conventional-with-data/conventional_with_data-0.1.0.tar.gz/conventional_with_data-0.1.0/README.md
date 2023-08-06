# conventional_with_data

Extends [Commitizen's](https://github.com/commitizen-tools/commitizen) [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/#specification) implementation with one additional prefix: `data:` to cover committed data, blog content, designs, etc. Commits with the `data:` prefix will correlate with PATCH in Sematic Versioning.

Created with [https://www.github.com/ShayHill/conventionalish](https://www.github.com/ShayHill/conventionalish).

```
questions = [
    ("fix", "A bug fix", "x", PATCH),
    ("feat", "A new feature", "f", MINOR),
    ("data", "Changes to content (data, blog articles, designs, etc.)", "a", PATCH),
    ("docs", "Documentation only changes", "d", None),
    ("style", "Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc.)", "s", None),
    ("refactor", "A code change that neither fixes a bug nor adds a feature", "r", PATCH),
    ("perf", "A code change that improves performance", "p", PATCH),
    ("test", "Adding missing or correcting existing tests", "t", None),
    ("build", "Changes that affect the build system or external dependencies (example scopes: pip, docker, npm)", "b", None),
    ("ci", "Changes to our CI configuration files and scripts (example scopes: GitLabCI)", "c", None)
]
```

## Use

Install in your environment (e.g., `pip install conventional_with_data` then run `cz init` and choose `conventional_with_data`. [Commitizen](https://github.com/commitizen-tools/commitizen) has great documentation.

## Author
Shay Hill (shay_public@hotmail.com)

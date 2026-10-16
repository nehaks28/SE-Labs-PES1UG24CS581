# Reflection

> NOTE: the handout PDF did not list the 4 questions, so these use the usual Lab 5 questions. Check the wording against the original handout.

**1. Which issues were the easiest and which were the hardest to fix?**
Easiest were the Flake8 ones (E203, E302, E261, E501) and the Pylint docstrings/naming, since the tool tells you exactly what to change. Hardest was the Bandit group. The `os.system` command injection and `mktemp` race condition needed me to understand *why* they are unsafe and pick a correct replacement (`subprocess.run` with an argument list, `mkstemp`), not just silence a warning. Renaming functions to snake_case was also easy to get wrong because every call site in `main()` had to change too.

**2. Did the tools report any false positives, or issues you chose not to fix?**
Mostly no, they were all real. The one grey area is Bandit's B404/B603/B607 notes about using `subprocess` and `xdg-open`. With a fixed argument list and no shell, the injection risk is gone, so I marked those with a specific `# nosec` code instead of removing the feature. The hardcoded-password finding (B105) was labelled Low, but it is still a real problem because secrets in source end up in git history. Also, Pylint can't tell that the password is only a "demo" value, so it looks like a false positive but isn't a good habit.

**3. How could static analysis be integrated into your development workflow?**
Run Flake8 and Pylint automatically in a pre-commit hook and in CI (e.g. GitHub Actions) so a pull request fails if the score drops below a threshold (here 9.5) or Bandit finds a High/Medium issue. Editors can also show Pylint/Flake8 warnings live while typing, which catches things before they are ever committed.

**4. What tangible improvements in code quality, security and maintainability did you see?**
Pylint went from 5.27 to 10.00 and Bandit/Flake8 went to zero issues, with the program output unchanged. Security improved the most (no shell injection, no race-prone temp files, no secret in source). Maintainability improved through docstrings, consistent naming, no global state, and a `main()` guard so the module can be imported and tested. The key lesson is that static analysis finds real bugs and risks without running the code, but it doesn't replace testing and review, since it can't judge whether the logic is correct.

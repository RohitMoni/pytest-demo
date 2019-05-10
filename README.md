# Pytest

## Strengths
1. Highly configurable
2. Easy to run large sets of tests
3. Easy to automate running tests

## Weaknesses
1. Can be hard to debug if pytest itself fails (collection fails, etc)

## Best Practices
1. Keep individual test functions as small as possible. As few asserts as possible (Ideally one assert per test). If you want to run multiple scenarios of the same test, parameterize it.
2. Use fixtures and conftest for shared resources and data files / configuration files. Setup / teardown is invaluable and helps keep test functions easy to understand (while still having dependent fixtures as function parameters).

## Pitfalls
1. Be careful of file paths (Ex: Common data files like licenses or configuration files). Pytest can be run from different directories and thus might have a different working directory. Usually need to convert relative paths into absolute paths.
2. Fixture failures can be *really* hard to debug because their initialization / teardown can be hard to predict.

## Debugging test collection
1. Is the file named `test_*`?
2. Is the function named `test_*` or `*_test`?

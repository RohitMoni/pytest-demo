# Automatic Test Discovery / Collection

**Almost everything is configurable**

1. Looks for `testpath` if configured.
2. Recurses into directories, ignoring anything matching `norecursedirs` or are defined via the `--ignore` option.
3. Look for files named `test_*` or `*_test`.
4. Look for functions and classes named `test*`.


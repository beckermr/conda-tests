test -f ${PREFIX}/bin/pkg-d-first
pkg-d-first
touch ${HOME}/tests/d_first_tests_ran

{
    test -f ${PREFIX}/bin/pkg-x
} || {
    echo "package x is not in test env!"
    exit 1
}

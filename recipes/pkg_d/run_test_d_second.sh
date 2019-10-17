test -f ${PREFIX}/bin/pkg-d-second
pkg-d-second
touch ${HOME}/tests/d_second_tests_ran

{
    test -f ${PREFIX}/bin/pkg-x
} || {
    echo "package x is not in test env!"
    exit 1
}

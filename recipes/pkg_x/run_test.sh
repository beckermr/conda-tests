test -f ${PREFIX}/bin/pkg-{{ name }}
pkg-{{ name }}
touch ${HOME}/tests/{{ name }}_tests_ran

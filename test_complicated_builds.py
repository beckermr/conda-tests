import subprocess
import os

CONDA_BLD = os.path.join(os.environ['HOME'], 'miniconda', 'conda-bld')
TESTS = os.path.join(os.environ['HOME'], 'tests')


def test_build_c():
    subprocess.run("rm -f ${HOME}/tests/*", shell=True, check=True)
    subprocess.run(
        "conda build --use-local recipes/pkg_c", shell=True, check=True)

    # this one runs downstreams
    assert os.path.exists(os.path.join(TESTS, 'a_tests_ran'))
    assert os.path.exists(os.path.join(TESTS, 'b_tests_ran'))
    assert os.path.exists(os.path.join(TESTS, 'c_tests_ran'))

    pname = os.path.join(
        CONDA_BLD, 'linux-64', 'c-1-py37_0.tar.bz2')
    assert os.path.exists(pname)


def test_build_d():
    subprocess.run("rm -f ${HOME}/tests/*", shell=True, check=True)
    subprocess.run(
        "conda build --use-local recipes/pkg_d", shell=True, check=True)

    # this one runs downstreams
    assert os.path.exists(os.path.join(TESTS, 'a_tests_ran'))
    assert os.path.exists(os.path.join(TESTS, 'b_tests_ran'))
    assert os.path.exists(os.path.join(TESTS, 'd_first_tests_ran'))
    assert os.path.exists(os.path.join(TESTS, 'd_second_tests_ran'))

    pname = os.path.join(
        CONDA_BLD, 'linux-64', 'd-first-1-py37_0.tar.bz2')
    assert os.path.exists(pname)

    pname = os.path.join(
        CONDA_BLD, 'linux-64', 'd-second-1-py37_0.tar.bz2')
    assert os.path.exists(pname)

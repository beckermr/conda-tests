import subprocess
import os

CONDA_BLD = os.path.join(os.environ['HOME'], 'miniconda', 'conda-bld')
TESTS = os.path.join(os.environ['HOME'], 'tests')


def test_build_a():
    subprocess.run("rm -f ${HOME}/tests/*", shell=True, check=True)
    subprocess.run("conda build recipes/pkg_a", shell=True, check=True)

    assert os.path.exists(os.path.join(TESTS, 'a_tests_ran'))

    for pyver in ['27', '36', '37']:
        pname = os.path.join(
            CONDA_BLD, 'linux-64', 'a-1-py%s_0.tar.bz2' % pyver)
        assert os.path.exists(pname)


def test_build_b():
    subprocess.run("rm -f ${HOME}/tests/*", shell=True, check=True)
    subprocess.run("conda build recipes/pkg_b", shell=True, check=True)

    assert os.path.exists(os.path.join(TESTS, 'b_tests_ran'))

    pname = os.path.join(
        CONDA_BLD, 'linux-64', 'b-1-py37_0.tar.bz2')
    assert os.path.exists(pname)


def test_build_x():
    subprocess.run("rm -f ${HOME}/tests/*", shell=True, check=True)
    subprocess.run("conda build recipes/pkg_x", shell=True, check=True)

    assert os.path.exists(os.path.join(TESTS, 'x_tests_ran'))

    pname = os.path.join(
        CONDA_BLD, 'linux-64', 'x-1-py37_0.tar.bz2')
    assert os.path.exists(pname)


def test_build_y():
    subprocess.run("rm -f ${HOME}/tests/*", shell=True, check=True)
    subprocess.run("conda build recipes/pkg_y", shell=True, check=True)

    assert os.path.exists(os.path.join(TESTS, 'y_tests_ran'))

    pname = os.path.join(
        CONDA_BLD, 'noarch', 'y-1-py_0.tar.bz2')
    assert os.path.exists(pname)


def test_build_f():
    subprocess.run("rm -f ${HOME}/tests/*", shell=True, check=True)
    subprocess.run("conda build recipes/pkg_f", shell=True, check=True)

    assert os.path.exists(os.path.join(TESTS, 'f_tests_ran'))

    pname = os.path.join(
        CONDA_BLD, 'linux-64', 'f-1-py37_0.tar.bz2')
    assert os.path.exists(pname)


def test_build_g():
    subprocess.run("rm -f ${HOME}/tests/*", shell=True, check=True)
    subprocess.run("conda build recipes/pkg_g", shell=True, check=True)

    assert os.path.exists(os.path.join(TESTS, 'g_tests_ran'))

    pname = os.path.join(
        CONDA_BLD, 'linux-64', 'g-1-py37_0.tar.bz2')
    assert os.path.exists(pname)

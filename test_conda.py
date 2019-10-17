import os
import pytest

CONDA_BLD = os.path.join(os.environ['HOME'], 'miniconda', 'conda-bld')


@pytest.mark.parametrize('pyver', ['27', '36', '37'])
def test_a_python_versions(pyver):
    pname = os.path.join(CONDA_BLD, 'linux-64', 'a-1-py%s_0.tar.bz2' % pyver)
    assert os.path.exists(pname)


def test_b_exists():
    pname = os.path.join(CONDA_BLD, 'linux-64', 'b-1-py37_0.tar.bz2')
    assert os.path.exists(pname)

import os
from mpi4py import rc


def setup_mpi():
    rc.initialize = False
    if 'ZCFD_TRACE' in os.environ:
        rc.profile('vt-mpi', logfile='zcfd')

    from mpi4py import MPI
    return MPI


MPI = setup_mpi()

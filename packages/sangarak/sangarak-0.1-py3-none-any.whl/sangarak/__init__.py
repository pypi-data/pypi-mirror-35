import numpy as np
import math

def convert_to_number_list(string):
    return [float(s) for s in string.split(' ')]

def generate_file_dict(f_name, procs,**kwargs):
    path = kwargs.get('path')
    if not path:
        path = ""
        
    d = {}
    for proc in range(0,procs):
        d[proc] = path + str(proc) + f_name + ".txt"

    return d

def read_matrix(files, major, n, nb, pb, num_procs, dist="block_cyclic"):
    """
    Read matrices from files specified inside a dict called 'files'. The key of 
    the dict is the process number from the file was outputted and the
    corresponding value is the actual name of the file. Only works for square 
    matrix (for now).

    This implementation is specific to block cyclic matrices stored on multiple MPI processes.
    
    Parameters
    ----------
    files : dict
        Dict specifying the process names with corresponding file names.

    major : string
        Can be either "row" or "col" depending on storage format.

    n : int
        side size of the matrix.

    nb : int
        Block size of matrix.

    pb : int
        Number of processes in one side.

    num_procs : int
        Total number of processes.

    Returns
    -------
    numpy.array
    """
    matrix = np.zeros([n,n])
    width = math.sqrt(num_procs)
    nb_r = nb // pb
    nb_c = nb // pb
    num_block_nrows = n // nb
    num_block_ncols = n // nb
    numroc = num_block_nrows * nb_r # num elements in process row
    
    for proc, file_name in files.items():
        f = open(file_name, "r")
        r = f.read().strip()
        arr = convert_to_number_list(r)
        f.close()
        myrow = int(proc // width)
        mycol = int(proc - (myrow * width))

        if major == "row":
            for pr in range(num_block_nrows):
                for r in range(nb_r):
                    for pc in range(num_block_ncols):
                        for c in range(nb_c):
                            glob_row = int(r + myrow*nb_r + pr*nb)
                            glob_col = int(c + mycol*nb_c + pc*nb)
                            index = (r + pr*nb_r)*numroc + c + pc*nb_c
                            matrix[glob_row, glob_col] = arr[index]
        elif major == "col":
            raise NotImplementedError("column-major not implemented.")

    return matrix

def read_file(file_name, n, nb, pb, num_procs, **kwargs):
    """
    Helper method for reading a distributed matrix just by specifying a common
    filename postfix. Defaults to row major.
    
    Say you have 4 files "0input.txt", "1input.txt", "2input.txt" and "3input.txt"
    then the file_name argument should be "input".

    Arguments
    ---------

    file_name : string

    Keyword arguments
    -----------------
    path : string
    """
    path = kwargs.get('path')

    d = generate_file_dict(file_name, num_procs, path=path)
    return read_matrix(d, "row", n, nb, pb, num_procs)

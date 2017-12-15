"""
    biclustlib: A Python library of biclustering algorithms and evaluation measures.
    Copyright (C) 2017  Victor Alexandre Padilha

    This file is part of biclustlib.

    biclustlib is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    biclustlib is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from ._base import ExecutableWrapper
from ._util import parse_in_chunks
from ...models import Bicluster, Biclustering
from os.path import dirname, join

import os
import numpy as np

class BinaryInclusionMaximalBiclusteringAlgorithm(ExecutableWrapper):
    """Binary Inclusion-Maximal Biclustering Algorithm (Bimax)

    Bimax searches for submatrices with all values equal to 1 in a binary matrix.

    Reference
    ---------
    Ben-Dor, A., Chor, B., Karp, R., and Yakhini, Z. (2003). Discovering local structure in gene expression
    data: the order-preserving submatrix problem. Journal of computational biology, 10(3-4), 373-384.

    Parameters
    ----------
    num_best_partial_models : int, default: 100
        Number of best partial models to maintain from one iteration to another.

    tmp_dir : str, default: '.opsm_tmp'
        Temporary directory to save the outputs generated by OPSM's jar.
    """

    def __init__(self, min_rows=2, min_cols=2, tmp_dir='.bimax_tmp'):
        module_dir = dirname(__file__)
        exec_comm = join(module_dir, 'bin', 'bimax') + ' {_data_filename} > {_output_filename}'
        super().__init__(exec_comm, tmp_dir=tmp_dir, data_type=np.bool)

        self.min_rows = min_rows
        self.min_cols = min_cols

    def _write_data(self, data):
        with open(self._data_filename, 'wb') as f:
            np.savetxt(f, data, delimiter=' ', header=self._get_header(data), fmt='%d', comments='')

    def _get_header(self, data):
        num_rows, num_cols = data.shape
        return '{} {} {} {}'.format(num_rows, num_cols, self.min_rows, self.min_cols)

    def _parse_output(self):
        biclusters = []

        if os.path.exists(self._output_filename):
            for rows, cols in parse_in_chunks(self._output_filename, chunksize=4, rows_idx=2, cols_idx=3):
                b = Bicluster(rows - 1, cols - 1)
                biclusters.append(b)

        return Biclustering(biclusters)

    def _validate_parameters(self):
        if self.min_rows <= 0:
            raise ValueError("num_rows must be > 0, got {}".format(self.num_rows))

        if self.min_cols <= 0:
            raise ValueError("num_cols must be > 0, got {}".format(self.num_cols))

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

from .spectral import Spectral
from .fabia import FactorAnalysisForBiclusterAcquisition
from .bbc import BayesianBiclustering
from .qubic import QualitativeBiclustering
from .opsm import OrderPreservingSubMatrix
from .bimax import BinaryInclusionMaximalBiclusteringAlgorithm
from .rbimax import RBinaryInclusionMaximalBiclusteringAlgorithm
from .rcca import RChengChurchAlgorithm
from .rplaid import RPlaid
from .isa2 import IterativeSignatureAlgorithm2
from .xmotifs import RConservedGeneExpressionMotifs
from .rinclose import RInClose

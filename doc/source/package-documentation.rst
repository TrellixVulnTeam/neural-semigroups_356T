======================
Package Documentation
======================

Associator Loss
===============
.. autoclass:: neural_semigroups.AssociatorLoss
   :special-members: __init__
   :members:

Constant Baseline
=================
.. autoclass:: neural_semigroups.ConstantBaseline
   :special-members: __init__
   :members:

Cyclic Group
============
.. autoclass:: neural_semigroups.CyclicGroup
   :special-members: __init__      

Denoising Autoencoder for Magmas
================================
.. autoclass:: neural_semigroups.MagmaDAE
   :special-members: __init__
   :members:

Magma
======
.. autoclass:: neural_semigroups.Magma
   :special-members: __init__
   :members:

Precise Guess Loss
===================
.. autoclass:: neural_semigroups.PreciseGuessLoss
   :special-members: __init__
   :members:
      
Datasets
=========

Random Dataset
---------------
.. autoclass:: neural_semigroups.datasets.RandomDataset
   :special-members: __init__
   :members:

Semigroups Dataset
-------------------
.. autoclass:: neural_semigroups.datasets.SemigroupsDataset
   :special-members: __init__
   :members:
      
.. _smallsemi-dataset:

Smallsemi Dataset
------------------
.. autoclass:: neural_semigroups.datasets.Smallsemi
   :special-members: __init__
   :members:

Mace4 Semigroups Dataset
-------------------------
.. autoclass:: neural_semigroups.datasets.Mace4Semigroups
   :special-members: __init__
   :members:

utils
======
.. currentmodule:: neural_semigroups.utils

A collection of different functions used by other modules.

.. autofunction:: random_semigroup
.. autofunction:: get_magma_by_index
.. autofunction:: import_smallsemi_format
.. autofunction:: download_file_from_url
.. autofunction:: find_substring_by_pattern
.. autofunction:: get_newest_file
.. autofunction:: make_discrete
.. autofunction:: count_different
.. autofunction:: hide_cells
.. autofunction:: read_whole_file
.. autofunction:: partial_table_to_cube
.. autofunction:: connect_to_db
.. autofunction:: create_table_if_not_exists
.. autofunction:: insert_values_into_table
.. autofunction:: gunzip
		  
generate_data_with_mace4
=========================
.. currentmodule:: neural_semigroups.generate_data_with_mace4

A script which generates semigroups with ``mace4`` and saves them in an ``sqlite`` database.

.. autofunction:: generate_data_with_mace4

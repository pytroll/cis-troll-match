.. _installation:

************
Installation
************

To install the package and its dependencies you will need to packages: ``git-core`` and ``miniconda``.

Installing dependencies
-----------------------

Clone git repository to obtain the project

.. code:
   
   git clone https://github.com/pytroll/cis-troll-match

Currently two major dependencies are ``satpy`` and ``cistools``.

To install ``cistools`` you will need a package miniconda. For miniconda installation refer to miniconda_link_.
To install ``cistools`` do:

.. code::
   
  /usr/local/miniconda/bin/conda create -c conda-forge -n cis_env cis 
 
This will install cistools and its dependencies.

Next step is to activate the conda environment:

.. code::

   source activate cis_env

Once the environment is activated navigate to the ``cis-troll-match`` folder and do:

.. code::

   python setup.py install

This will install package along with the `cistools` package

.. _miniconda_link: https://conda.io/docs/install/quick.html

|banner|

.. raw:: html

   <h1 align="center">

oceandb-bigchaindb-driver

.. raw:: html

   </h1>

..

    🐳 Ocean DB `BigchainDB <https://www.bigchaindb.com/>`_ driver (Python).

.. |banner| image:: doc/img/repo-banner@2x.png
   :target: https://oceanprotocol.com

.. image:: https://img.shields.io/pypi/v/oceandb-bigchaindb-driver.svg
        :target: https://pypi.python.org/pypi/oceandb-bigchaindb-driver

.. image:: https://travis-ci.com/oceanprotocol/oceandb-bigchaindb-driver.svg?token=pA8zcB6SCxKW5MHpqs6L&branch=master
        :target: https://travis-ci.com/oceanprotocol/oceandb-bigchaindb-driver

.. image:: https://readthedocs.org/projects/oceandb-plugin-system/badge/?version=latest
        :target: https://oceandb-plugin-system.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


BigchainDB driver to connect implementing OceanDB.

* Free software: Apache Software License 2.0
* Documentation: https://oceandb-plugin-system.readthedocs.io.


How to use it
-------------

First of all we have to specify where is allocated our config.
To do that we have to pass the following argument:

.. code-block:: python

    --config=/path/of/my/config
..

If you do not provide a configuration path, by default the config is expected in the config folder.

In the configuration we are going to specify the following parameters to

.. code-block:: python

    [oceandb]

    enabled=true            # In order to enable or not the plugin
    module=bigchaindb       # You can use one the plugins already created. Currently we have mongodb and bigchaindb.
    module.path=            # You can specify the location of your custom plugin.
    db.hostname=localhost   # Address of your bigchaindb nodes.
    db.port=9985            # Port of your bigchaindb database.

    # Bigchaindb specific config:
    secret=                 # A secret that serves as a seed.
    db.namespace=namespace  # Namespace that you are going to use in bigchaindb
    db.app_id=              # App id of your bigchaindb application.
    db.app_key=             # App key of your bigchaindb application.
..

Once you have defined this the only thing that you have to do it is use it:

.. code-block:: python

    oceandb = OceanDb(confPath)
    tx_id = oceandb.write({"value": "test"})  #Write a new transaction in bdb.
    oceandb.read(tx_id)                       #Read the content of this transaction
    oceandb.update({"value": "update"},tx_id) #Update value of the transaction.
    oceandb.delete(tx_id)                     #Delete transaction
..


About BigchainDB plugin implementation
--------------------------------------

CRAB is the CRUD model in databases applied to blockchains:

+--------------+----------------+
| Database     | Blockchain     |
+==============+================+
| **C**\ reate | **C**\ reate   |
+--------------+----------------+
| **R**\ ead   | **R**\ etrieve |
+--------------+----------------+
| **U**\ pdate | **A**\ ppend   |
+--------------+----------------+
| **D**\ elete | **B**\ urn     |
+--------------+----------------+

You can find `here <https://blog.bigchaindb.com/crab-create-retrieve-append-burn-b9f6d111f460>`_ a link talking about the CRAB model.

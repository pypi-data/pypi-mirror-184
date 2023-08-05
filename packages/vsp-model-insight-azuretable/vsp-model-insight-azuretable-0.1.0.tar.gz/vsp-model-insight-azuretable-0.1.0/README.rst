VSP Model Insight
==================================


Installation
------------

::

    pip install vsp-model-insight-azuretable

Prerequisites
-------------

* Create an VSP Model Monitor resource and get the connection string, more information can be found in the official docs.
* Place your connection string directly into your code.
  
Usage
-----

Log
~~~

The **Model Performance Log Handler** allows you to export Python logs to `VSP`.

This example shows how to send a warning level log to Azure Monitor.

.. code:: python

    import logging

    from vsp_model_insight.azuretable import ModelPerformanceLogHandler

    logging.basicConfig(level=logging.DEBUG)
    rootlogger = logging.getLogger()
    handler = ModelPerformanceLogHandler(connection_string='****')
    rootlogger.addHandler(handler)

    properties = {'model_signature': 'demo','model_performance': {'key_1': 'value_1', 'key_2': 'value_2'}}
    logging.info(f"{datetime.now()}",extra=properties)


References
----------


* `Examples <https://please.todo.com>`_

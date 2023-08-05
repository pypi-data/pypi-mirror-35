## 0.2.1 (2018-08-01)

### Fixes

* #8: Add an `exchange_type` parameter to `ConsumerClient` to determine the [type exchange](https://www.rabbitmq.com/tutorials/tutorial-four-python.html) (fanout, direct, topic)

## 0.2.0 (2018-07-31)

### Features

* New `api` function: 
  * Simplify calls to internal REST APIs
  * Status code error handling
  * Logging management
* New `ConsumerClient` class: 
  * Pika client with a blocking connection
  * Bind a queue to an exchange to consume incoming messages

### Changes

*  The default logging level for every Pika client is set to `logging.INFO`

## 0.1.1 (2018-07-23)

### Changes

* `MANIFEST.in` added to `setup.py` process

## 0.1.0 (2018-07-23)

### Features

* `RpcClient` class with context manager, and `call/send` public methods 
* Test suite foundations using [pytest](https://docs.pytest.org/en/latest/) accessible in the `tests/` folder
* Gitlab pipeline introduction: test suite execution, `.tar.gz` distribution package build, deployement to Pypi
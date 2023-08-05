ExoEdge Python Library
========================
This library provides functionality to interpret ExoSense data
schemas and self-configure gateways. It is expected that the
user will write a gateway application to leverage this library,
but many use cases can be covered in very few lines of
application code.

Requirements
---------------

* Python 2.7.9+, 3.4, 3.5, 3.6
* docopt (>=0.6.2)
* murano_client (>=1.0.0)

Getting started in 15m
----------------------

Install ExoEdge
~~~~~~~~~~~~~~~~~
  .. code-block :: bash

    pip install exoedge

Start Reporting
~~~~~~~~~~~~~~~~~~
  .. code-block :: bash

      edged -s <YOUR_NEW_SN> -H <YOUR_PRODUCT_HOST> go

  Meanwhile, set your config_io to this in Murano:

  .. code-block :: json

      {
        "channels": {
          "one": {
            "display_name": "Temperature",
            "description": "It's the temperature",
            "properties": {
              "max": 1000,
              "data_unit": "DEG_CELSIUS",
              "precision": 4,
              "data_type": "TEMPERATURE",
              "min": 0
            },
            "protocol_config": {
              "application": "ExoSimulator",
              "report_on_change": false,
              "report_rate": 10000,
              "sample_rate": 10000,
              "mode": "poll",
              "down_sample": "ACT",
              "app_specific_config": {
                "function": "sin_wave",
                "module": "exo_simulator",
                "parameters": {}
              }
            }
          }
        }
      }

  The device should have started reporting.

  Then, in ``channels.one.protocol_config.app_specific_config.parameters``, add these keys and set
  their values:

  .. code-block :: json

      {
        "period": 120,
        "amplitude": 10,
        "offset": 100,
        "precision": 0,
      }

  Verify that the device started reporting a sin wave with those characteristics.

  Try changing `sample_rate` to 1000 and `down_sample` to "AVG". This will sample
  the sin wave once per second and average (AVG) those datapoints every 10 seconds.
  Add a channel. Remove a channel. Keep reading and learn how to use an INI file with `edged`.

CLI
---


Usage
~~~~~

.. code-block ::

    Usage:
        edged [options] [<command>] [<args>...]

    Commands:
        go          Start reporting to ExoSense

    Options:
        -h --help                       Show this screen.
        -v --version                    Print the current version of the ExoEdge library.
        -L --list-commands              Print installed and available commands.
        -i --ini-file <file>            INI file with device information.
        -c --config-io-file <cfgfile>   Local file in which to cache config_io. If
                                        `--local-strategy` flag is used, this file is
                                        expected to contain a valid config_io.
        -s --murano-id <sn>             The device serial number to use.
        -t --murano-token <token>       Token for device authentication.
        -K --pkeyfile <pkey>            Private key for TLS provisioning.
        -C --certfile <cert>            Public cert for TLS provisioning.
        -E --murano-cacert <cacert>     CA cert for PKI integration.
        -H --murano-host <host>         Set host for API requests.
        -p --murano-port <port>         Set port for API requests.
        -d --debug <lvl>                Tune the debug output. Logs curl commands at
                                        DEBUG.
                                        (DEBUG|INFO|WARNING|ERROR|CRITICAL).
        --local-strategy                Use `local` config_io strategy. If not present,
                                        use `remote` strategy.
        --no-filesystem                 Don't rely on a file system.
        --no-config-cache               Don't store a local copy of config_io.
        --no-config-sync                Don't keep config_io synced with ExoSense.
        --http-timeout <timeout>        Timeout to use for requests.
        --edged-timeout <timeout>       Timeout for edged process, in seconds.
        --watchlist <watchlist>         Murano resources to watch. Comma separated list.
                                            e.g. --watchlist=config_io,remote_control
        <command>                       The ExoEdge subcommand name.
        <args>                          Supported arguments for <command>

Argument Support
~~~~~~~~~~~~~~~~~~
``edged`` supports supplying arguments via CLI flags, environment variables, and INI files.
Naming conventions differ slightly between these methods—for a generic argument
``some_argument`` they are named as follows:

* CLI: ``--some-argument``
* Environment: ``EDGED_SOME_ARGUMENT``
* INI: ``some_argument``

Argument Precedence:
~~~~~~~~~~~~~~~~~~~~~
In handling conflicting arguments from different sources, ``edged`` evaluates arguments in
the following order:

1. CLI (overrides Environment and INI)
#. Environent (overriden by CLI, overrides INI)
#. INI (overriden by CLI and Environment)


Examples
~~~~~~~~~~
With command line arguments and a local config_io:
  .. code-block :: bash

      edged --host=https://abcdef123456.m2.exosite.io/ -s device01.ini --local -c my_config.json -i device01.ini go

      cat device01.ini
        [device]
        murano_token = XXXXXXXXX

With INI file:
  .. code-block :: bash

      cat device01.ini
        [device]
        murano_host = https://abcdef123456.m2.exosite.io/
        murano_id = device01
        watchlist = config_io
        debug = INFO

      edged -i device01.ini --local -c my_config.json go

Note that the `murano_token` option is not present in the .ini file prior to activation.
If `murano_token` is present, the client will attempt to use
that token, even if it's blank, to communicate with Murano.

For Starters
--------------
The primary things to note are:

* The burden of device creation is on the application. Usage of the ``lib_murano_client_python`` library simplifies this greatly. The device is passed into the ``ExoEdge`` object.
* ``ExoEdge`` uses one of two strategies to instantiate itself:

  * ``remote``: get config_io from Murano
  * ``local``: read from a local config_io file

* ``ExoEdge`` spins up ``ConfigIO`` and ``Channel`` objects. Channels contain their own logic regarding how frequently and what data to send to Murano/ExoSense.
* Optionally, ``ExoEdge`` subscribes to ``config_io`` and resets its ``ConfigIO`` and instances of ``Channel`` upon receiving an update.

config_io
-----------
A ``config_io`` resource expects a JSON string. A full config_io spec can be found here_.

.. _here: https://exosense.readme.io/docs/channel-configuration#section-parameter-description/

One such JSON string might look like this:

.. code-block :: json

    {
      "channels": {
        "one": {
          "display_name": "Temperature",
          "description": "It's the temperature",
          "properties": {
            "max": 1000,
            "data_unit": "DEG_CELSIUS",
            "precision": 4,
            "data_type": "TEMPERATURE",
            "min": 0
          },
          "protocol_config": {
            "application":"ExoSimulator",
            "report_on_change": false,
            "report_rate": 10000,
            "sample_rate": 1000,
            "mode": "poll",
            "down_sample": "AVG",
            "app_specific_config": {
              "function": "sin_wave",
              "module": "exo_simulator",
              "parameters": {}
            }
          }
        }
      }
    }

* Create a ``ConfigIO`` object, which serves as a proxy for communication between each ``Channel`` and ``ExoEdge``.
* Create a ``Channel`` object called 'cpu' which will ``poll`` the function ``sin_wave`` in the module ``exo_simulator`` every 1 second. The value from this function will be multiplied by 0.01 and incremented by 5 before being put in the Channel's queue. After 10 seconds, the values in the channel's queue will be down-sampled as the average (AVG) value.

  * If the function's value does not change between calls, the value is not written.
  * If the function's value `does` change, a request is made to send a data_in packet.

* Upon request for data_in to be sent, all Channel queues are checked for values and a data_in packet is formed.
* The device used to instantiate a Murano connection sends this data_in packet to Murano.

Application-Specific Config
----------------------------
Channels refer to a source to get data, an interaction defined in ``app_specific_config``. An application could be a simulated sin
wave, a Modbus port, or anything in between. The only criteria is that it
must be accessible by a Python process.

Creating a Source
~~~~~~~~~~~~~~~~~
A source consists of two components:

1. a Python module installed on the machine
#. a function within that module

The module can contain whatever logic is required to procure a value each
time the specified function is called. The module could define a thread
which puts data in a queue, and the function could fetch queued items,
analyze them, and return a final value.

For example:

.. code-block :: python

    # in my_source/__init__.py
    import time

    def minutes_to_seconds(min):
      return min * 60

    def minutes_from_now(minutes=0):
      # Returns the timestamp `minutes` after the current time.
      return time.time() + minutes_to_seconds(minutes)

For more in-depth information on creating Python modules and packages, see the docs_.

.. _docs: https://docs.python.org/2/tutorial/modules.html#packages

.. code-block ::

    # in config_io object
    {
      ...,
      "channels": {
        "a": {
          "display_name": "30 Minutes from Now",
          ...,
          "protocol_config": {
            "application": "Custom Application",
            "app_specific_config": {
              "module": "my_source",
              "function": "minutes_from_now",
              "parameters": {
                "minutes": 30
              }
            }
            ...
          }
        }
      }
    }

Passing Parameters
~~~~~~~~~~~~~~~~~~
Some application functions take keyword arguments which are passed in the
parameters section of the ``app_specific_config`` object in ``config_io``.
For instance, a function ``random_integer(lower=0, upper=10)`` which
returns—you guessed it—a random integer between it's ``lower`` and ``upper``
keyword arguments might have a parameters section like this:

.. code-block :: json

  "parameters": {
    "lower": 100,
    "upper": 200
  }

Modes
-----
Three channel modes are provided to get data from a source:

1. ``poll``: the function defined in ``protocol_config.source`` is run every time the ``sample_rate`` comes around.
#. ``async``: the function starts a thread, which emits an event when new data is generated. The channel listens for this event and puts the value in its queue when the event is emitted. For ``async`` channels, ``sample_rate`` and ``report_rate`` are ignored.
#. ``async2``: the function returns after an unspecified period of time. For instance, a function that sleeps for a random interval and then returns a value. For ``async2`` channels, ``sample_rate`` and ``report_rate`` are ignored.

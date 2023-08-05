Alexa Voice Service Client
==========================

|code-climate-image| |circle-ci-image| |codecov-image|

**Python Client for Alexa Voice Service (AVS)**

--------------

Installation
------------

.. code:: sh

    pip install avs_client

Usage
-----

File audio
~~~~~~~~~~

.. code:: py

    from avs_client import AlexaVoiceServiceClient


    alexa_client = AlexaVoiceServiceClient(
        client_id='my-client-id',
        secret='my-secret',
        refresh_token='my-refresh-token',
    )
    alexa_client.connect()  # authenticate and other handshaking steps
    with open('./tests/resources/alexa_what_time_is_it.wav', 'rb') as f:
        alexa_response_audio = alexa_client.send_audio_file(f)
    with open('./output.wav', 'wb') as f:
        f.write(alexa_response_audio)

Now listen to ``output.wave`` and Alexa should tell you the time.

Microphone audio
~~~~~~~~~~~~~~~~

.. code:: py

    from io import BytesIO

    import pyaudio

    from avs_client import AlexaVoiceServiceClient


    buffer = BytesIO()

    def callback(in_data, frame_count, time_info, status):
        buffer.write(in_data)
        return (in_data, pyaudio.paContinue)
    p = pyaudio.PyAudio()
    stream = p.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=16000,
        input=True,
        stream_callback=callback,
    )


    alexa_client = AlexaVoiceServiceClient(
        client_id='my-client-id',
        secret='my-secret',
        refresh_token='my-refresh-token',
    )


    try:
        stream.start_stream()
        print('listening. Press CTRL + C to exit.')
        alexa_client.connect()
        alexa_response_audio = alexa_client.send_audio_file(buffer)
        if alexa_response_audio:
            with open('./output.wav', 'wb') as f:
                f.write(alexa_response_audio)
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()

Authentication
--------------

To use AVS you must first have a `developer
account <http://developer.amazon.com>`__. Then register your product
`here <https://developer.amazon.com/avs/home.html#/avs/products/new>`__.
Choose "Application" under "Is your product an app or a device"?

The client requires your ``client_id``, ``secret`` and
``refresh_token``:

+---------------------+-------------------------------------------------------------------------------------------------------------------+
| client kwarg        | Notes                                                                                                             |
+=====================+===================================================================================================================+
| ``client_id``       | Retrieve by clicking on the your product listed `here <https://developer.amazon.com/avs/home.html#/avs/home>`__   |
+---------------------+-------------------------------------------------------------------------------------------------------------------+
| ``secret``          | Retrieve by clicking on the your product listed `here <https://developer.amazon.com/avs/home.html#/avs/home>`__   |
+---------------------+-------------------------------------------------------------------------------------------------------------------+
| ``refresh_token``   | You must generate this. `See here <#refresh-token>`__                                                             |
+---------------------+-------------------------------------------------------------------------------------------------------------------+

Refresh token
~~~~~~~~~~~~~

You will need to login to Amazon via a web browser to get your refresh
token.

To enable this first go
`here <https://developer.amazon.com/avs/home.html#/avs/home>`__ and
click on your product to set some security settings under
``Security Profile``:

+-----------------------+------------------------------------+
| setting               | value                              |
+=======================+====================================+
| Allowed Origins       | https://localhost:9000             |
+-----------------------+------------------------------------+
| Allowed Return URLs   | https://localhost:9000/callback/   |
+-----------------------+------------------------------------+

Then run:

.. code:: sh

    python ./avs_client/refreshtoken/serve.py \
        --device-type-id=enter-device-type-id-here \
        --client-id=enter-client-id-here \
        --client-secret=enter-client-secret-here

Follow the on-screen instructions shown at ``http://localhost:9000`` in
your web browser. On completion Amazon will return your
``refresh_token``.

Steaming audio to AVS
---------------------

``alexa_client.send_audio_file`` streaming uploads a file-like object to
AVS for great latency. The file-like object can be an actual file on
your filesystem, an in-memory BytesIo buffer containing audio from your
microphone, or even audio streaming from `your browser over a websocket
in real-time <https://github.com/richtier/alexa-browser-client>`__.

AVS requires the audio data to be 16bit Linear PCM (LPCM16), 16kHz
sample rate, single-channel, and little endian.

Persistent AVS connection
-------------------------

Calling ``alexa_client.connect()`` creates a persistent connection to
AVS. The connection may get forcefully closed due to inactivity. Keep
open by calling ``alexa_client.alexa_client.conditional_ping()``:

.. code:: py

    import threading


    def ping_avs():
        while True:
            alexa_client.conditional_ping()

    ping_thread = threading.Thread(target=ping_avs)
    ping_thread.start()

You will only need this if you intend to run the process for more than
five minutes. `More
information <https://developer.amazon.com/public/solutions/alexa/alexa-voice-service/docs/managing-an-http-2-connection>`__.

Unit test
---------

To run the unit tests, call the following commands:

.. code:: sh

    pip install -r requirements-dev.txt
    ./scripts/tests.sh

Other projects
--------------

This library is used by
`alexa-browser-client <https://github.com/richtier/alexa-browser-client>`__,
which allows you to talk to Alexa from your browser.

.. |code-climate-image| image:: https://codeclimate.com/github/richtier/alexa-voice-service-client/badges/gpa.svg
   :target: https://codeclimate.com/github/richtier/alexa-voice-service-client
.. |circle-ci-image| image:: https://circleci.com/gh/richtier/alexa-voice-service-client/tree/master.svg?style=svg
   :target: https://circleci.com/gh/richtier/alexa-voice-service-client/tree/master
.. |codecov-image| image:: https://codecov.io/gh/richtier/alexa-voice-service-client/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/richtier/alexa-voice-service-client



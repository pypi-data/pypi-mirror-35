**Build an SMS service with Infobip**
*************************************

*Building blocks to write an SMS service with infobip from scratch with simulator for TDD.*

1. Write the test.
2. Get your function right until the test passes.
3. Remove ``@responses.activate`` and ``sms_server(**connection)`` to put your script live.

While you get your stuff right, you don’t risk to send any real SMS.
You don’t even need a connection to the web.

When you switch your code to live there’s no reason to worry now either.
Your test assures you that the very first real SMS will be delivered (presuming your login and balance allow).

`Documentation`_

.. _Documentation: https://ibires.rtfd.io



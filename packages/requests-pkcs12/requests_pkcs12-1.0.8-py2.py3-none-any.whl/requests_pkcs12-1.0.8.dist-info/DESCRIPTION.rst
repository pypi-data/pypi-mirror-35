PKCS#12 support for requests
============================

This library adds PKCS#12 support to the Python `requests <http://python-requests.org>`_ library.

It is a **clean implementation**: it uses neither monkey patching nor temporary files. Instead, it is integrated into ``requests`` as recommended by its authors: creating a custom ``TransportAdapter``, which provides a custom ``SSLContext``.

This library is meant to be a transitional solution until this functionality is provided by ``requests`` directly. However, that will take some time. See the `corresponding issue <https://github.com/requests/requests/issues/1573>`_ for more details.



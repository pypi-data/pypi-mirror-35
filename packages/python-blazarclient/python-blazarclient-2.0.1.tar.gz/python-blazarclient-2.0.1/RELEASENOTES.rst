===================
python-blazarclient
===================

.. _python-blazarclient_2.0.1:

2.0.1
=====

.. _python-blazarclient_2.0.1_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/bug-1784038-fix-lease-create-without-start-date-73ce2bb28bc883f7.yaml @ b'ef481e8d9a99a0d2bb7b3f43370dc7a96583b8f6'

- Creating leases using version 2.0.0 of the CLI client without specifying a
  start date was failing with the error ``The lease parameters are
  incorrect``, following changes related to `bug 1783296
  <https://launchpad.net/bugs/1783296>`_. For more details, see `bug 1784038
  <https://launchpad.net/bugs/1784038>`_.

.. releasenotes/notes/bug-1786030-fix-error-message-with-same-name-leases-561ece8e602b4c68.yaml @ b'ef481e8d9a99a0d2bb7b3f43370dc7a96583b8f6'

- When there are multiple leases with the same name, lease actions
  identifying the lease by name would display an error message including a
  dictionary of lease values, instead of ``type 'lease'``. For more details,
  see `bug 1786030 <https://launchpad.net/bugs/1786030>`_.


.. _python-blazarclient_2.0.0:

2.0.0
=====

.. _python-blazarclient_2.0.0_Upgrade Notes:

Upgrade Notes
-------------

.. releasenotes/notes/bug-1783296-set-start-date-to-now-e329a6923c11432f.yaml @ b'f017a924d301bed939f8811923c83b9a41740560'

- When creating a lease using the CLI client, the default value for start
  date was changed to use the string 'now', which is resolved to the current
  time on the server rather than on the client. Note that if the request is
  sent at the end of a minute and interpreted by the service at the beginning of
  the next minute, this can result in leases that are one minute shorter than
  what the user might expect, as the end date is still specified by the
  client. Users who care about the exact timing of their leases should
  explicitly specify both start and end dates.


.. _python-blazarclient_2.0.0_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/bug-1783296-set-start-date-to-now-e329a6923c11432f.yaml @ b'f017a924d301bed939f8811923c83b9a41740560'

- Creating a lease using the CLI client without specifying a start date no
  longer fails if the request is sent to the Blazar service just before the
  end of a minute. For more details, see `bug 1783296
  <https://launchpad.net/bugs/1783296>`_.


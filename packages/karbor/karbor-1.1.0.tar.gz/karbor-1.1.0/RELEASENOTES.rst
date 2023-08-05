======
karbor
======

.. _karbor_0.4.0:

0.4.0
=====

.. _karbor_0.4.0_New Features:

New Features
------------

.. releasenotes/notes/s3-bank-plugin-b55ca44739d492b0.yaml @ b'323d17b6fb900a47558915ab8e41ef80bca31e65'

- Add support for using S3 comptatible storage as bank plugin.


.. _karbor_0.4.0_Other Notes:

Other Notes
-----------

.. releasenotes/notes/use-oslo-config-generator-f2a9be9e71d90b1f.yaml @ b'dba51806f209adcee01c578bf1aded496886ebe9'

- oslo-config-generator is now used to generate a karbor.conf.sample file


.. _karbor_0.2.0:

0.2.0
=====

.. _karbor_0.2.0_New Features:

New Features
------------

.. releasenotes/notes/ical-rfc24445-b98313a8c3eefb62.yaml @ b'da0bd1f9c989ab1e5ea99add1a451de4e0b46d7b'

- Added RFC2445 (iCal) format for time triggers.

.. releasenotes/notes/protection-plugin-api-063fd84b1f37d8e2.yaml @ b'da0bd1f9c989ab1e5ea99add1a451de4e0b46d7b'

- Revised Protection Plugin interface which now supports multiple hooks for
  each operation. Hooks dictate when specific parts of the protection plugin
  code runs in relation to the operation phase and other resource's state.

.. releasenotes/notes/protection-plugins-adjust-d228139bd2f19765.yaml @ b'da0bd1f9c989ab1e5ea99add1a451de4e0b46d7b'

- Revised Cinder protection plugin, which takes a snapshot, backs up from the
  snapshot, and deletes the snapshot afterwards.

.. releasenotes/notes/protection-plugins-adjust-d228139bd2f19765.yaml @ b'da0bd1f9c989ab1e5ea99add1a451de4e0b46d7b'

- Revised Glance protection plugin, which uploads the glance image in chunks
  to the bank.


.. _karbor_0.2.0_Deprecation Notes:

Deprecation Notes
-----------------

.. releasenotes/notes/protection-plugin-api-063fd84b1f37d8e2.yaml @ b'da0bd1f9c989ab1e5ea99add1a451de4e0b46d7b'

- Old Protection Plugin interface and BaseProtectionPlugin are deprecated.


.. _karbor_0.2.0_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/fix-checkpoint-list-c0435fcbdf26858b.yaml @ b'da0bd1f9c989ab1e5ea99add1a451de4e0b46d7b'

- Fix checkpoint listing bug, which caused results to be not filtered
  correctly according to set filters.


.. _karbor_0.2.0_Other Notes:

Other Notes
-----------

.. releasenotes/notes/restore-auth-79cd504bc0cc3712.yaml @ b'da0bd1f9c989ab1e5ea99add1a451de4e0b46d7b'

- Restore auth parameters now reside in restore_auth instead of restore
  parameters.


.. _karbor_0.1.0:

0.1.0
=====

.. _karbor_0.1.0_Other Notes:

Other Notes
-----------

.. releasenotes/notes/added-reno-releasenotes-ae36507a78246a50.yaml @ b'd20a834543e3e2e7bd1d64d27a3417730756f9ce'

- Started using Reno for release notes


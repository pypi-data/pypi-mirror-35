======
rdopkg
======

.. _rdopkg_0.47.0:

0.47.0
======

.. _rdopkg_0.47.0_Prelude:

Prelude
-------

.. releasenotes/notes/introduce-reno-0c400f440d89ffff.yaml @ 01ae72aad9b45fca6a18790fb1a08bbcfa738961

This rdopkg release brings support for distroinfo and reno.


.. _rdopkg_0.47.0_New Features:

New Features
------------

.. releasenotes/notes/introduce-reno-0c400f440d89ffff.yaml @ 01ae72aad9b45fca6a18790fb1a08bbcfa738961

- Use distroinfo module to access rdoinfo. distroinfo was created by forking rdoinfo parsing code from rdopkg and rdoinfo itself into a generic module.

.. releasenotes/notes/introduce-reno-0c400f440d89ffff.yaml @ 01ae72aad9b45fca6a18790fb1a08bbcfa738961

- Try using reno module to maintain release notes.

.. releasenotes/notes/introduce-reno-0c400f440d89ffff.yaml @ 01ae72aad9b45fca6a18790fb1a08bbcfa738961

- Allow '|' in patches_ignore regex.

.. releasenotes/notes/introduce-reno-0c400f440d89ffff.yaml @ 01ae72aad9b45fca6a18790fb1a08bbcfa738961

- Reworked ``rdopkg doctor`` with rainbows.


.. _rdopkg_0.47.0_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/introduce-reno-0c400f440d89ffff.yaml @ 01ae72aad9b45fca6a18790fb1a08bbcfa738961

- Fix version to tag translations for vX.Y.Z tag style.

.. releasenotes/notes/introduce-reno-0c400f440d89ffff.yaml @ 01ae72aad9b45fca6a18790fb1a08bbcfa738961

- Prevent unneeded patch file changes using extra format-patch parameters.

.. releasenotes/notes/introduce-reno-0c400f440d89ffff.yaml @ 01ae72aad9b45fca6a18790fb1a08bbcfa738961

- Improve Python 3 compatibility.


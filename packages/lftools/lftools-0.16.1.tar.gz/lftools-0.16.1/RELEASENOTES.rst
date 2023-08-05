=======
lftools
=======

.. _lftools_v0.16.1:

v0.16.1
=======

.. _lftools_v0.16.1_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/ldap-b50f699fc066890f.yaml @ b'3a409e15b5ad16715525fc86ad163f61b890645f'

- The v0.16.0 pulled in a new ldap module which breaks if the ldap devel
  libraries are not available on the system trying to use it. This hotfix
  makes the ldap module optional.


.. _lftools_v0.16.0:

v0.16.0
=======

.. _lftools_v0.16.0_New Features:

New Features
------------

.. releasenotes/notes/debug-e80d591d478e69cc.yaml @ b'2380b4e056c54b0258bffa43972fbc171b4af481'

- Add a new ``--debug`` flag to enable extra troubleshooting information.
  This flag can also be set via environment variable ``DEBUG=True``.

.. releasenotes/notes/ldap-info-017df79c3c8f9585.yaml @ b'4d7ce295121e166f2fb18417acd8f5193d4b382c'

- $ lftools ldap
  
  Usage: lftools ldap [OPTIONS] COMMAND [ARGS]...
  
  .. code-block:: none
  
     Commands:
       autocorrectinfofile  Verify INFO.yaml against LDAP group.
       csv                  Query an Ldap server.
       inactivecommitters   Check committer participation.
       yaml4info            Build yaml of commiters for your INFO.yaml.

.. releasenotes/notes/ldap-info-017df79c3c8f9585.yaml @ b'4d7ce295121e166f2fb18417acd8f5193d4b382c'

- $ lftools infofile
  
  .. code-block:: none
  
     Commands:
       get-committers   Extract Committer info from INFO.yaml or LDAP...
       sync-committers  Sync committer information from LDAP into...


.. _lftools_v0.16.0_Deprecation Notes:

Deprecation Notes
-----------------

.. releasenotes/notes/logger-1aa26520f6d39fcb.yaml @ b'28fc57084d22dd96db149069666e945b039b474a'

- Remove support for modifying the logger via logging.ini. It was a good idea
  but in practice this is not really used and adds extra complexity to
  lftools.


.. _lftools_v0.16.0_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/docs-cad1f396741b9526.yaml @ b'32275fd2e51e759b4b2c4c4b5f6c6ea4baaffa6c'

- Fix broken openstack and sign help command output in docs.


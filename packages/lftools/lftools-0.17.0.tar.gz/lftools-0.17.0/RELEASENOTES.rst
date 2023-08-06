=======
lftools
=======

.. _lftools_v0.17.0:

v0.17.0
=======

.. _lftools_v0.17.0_Prelude:

Prelude
-------

.. releasenotes/notes/openstack-stack-08f643f16b75bfb8.yaml @ b'0a5942299f83aaa74da3bf1fdf985d4003ce30f3'

Add new stack command feature to allow creation and deletion of stacks using lftools.
Usage: lftools openstack stack create|delete <params>


.. _lftools_v0.17.0_New Features:

New Features
------------

.. releasenotes/notes/jenkins-25629106553ebbd5.yaml @ b'54c0bdb08963841eecd01cc816d485d15f1e9de1'

- Add support to the **jenkins** command to parse ``jenkins_jobs.ini`` for
  configuration if **server** parameter passed is not a URL.

.. releasenotes/notes/jenkins-c247796de6390391.yaml @ b'7d2b155ff78d52a94ada949cf85ffd17512cbc45'

- Add a **jobs** sub-command to **jenkins** command to enable or disable Jenkins
  Jobs that match a regular expression.

.. releasenotes/notes/openstack-stack-08f643f16b75bfb8.yaml @ b'0a5942299f83aaa74da3bf1fdf985d4003ce30f3'

- Add stack command.
  https://jira.linuxfoundation.org/browse/RELENG-235

.. releasenotes/notes/openstack-stack-08f643f16b75bfb8.yaml @ b'0a5942299f83aaa74da3bf1fdf985d4003ce30f3'

- Add stack create sub-command.
  https://jira.linuxfoundation.org/browse/RELENG-235
  
  Usage: lftools openstack stack create NAME TEMPLATE_FILE PARAMETER_FILE

.. releasenotes/notes/openstack-stack-08f643f16b75bfb8.yaml @ b'0a5942299f83aaa74da3bf1fdf985d4003ce30f3'

- Add stack delete sub-command.
  https://jira.linuxfoundation.org/browse/RELENG-235
  
  Usage: lftools openstack stack create NAME


.. _lftools_v0.17.0_Other Notes:

Other Notes
-----------

.. releasenotes/notes/logger-c53984ef7b1da53f.yaml @ b'4edf459161faeaebe1614ff16f18101f0785adc6'

- Enhance logger subsystem to work better as a CLI program. This is a first
  step to migrating all lftools subsystems to use the logger instead of print
  statements everywhere.


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


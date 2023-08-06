=======
neutron
=======

.. _neutron_13.0.1:

13.0.1
======

.. _neutron_13.0.1_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/fix-co-existence-bug-between-sg-logging-and-fwg-logging-ef16077880d76449.yaml @ b'3e68398335795d422d58a6e2110f2025907c5892'

- Add ``resource_type`` into log object query to distinguish between security
  group and firewall group log objects.
  For more information see bug
  `1787119 <https://bugs.launchpad.net/neutron/+bug/1787119>`_.


.. _neutron_13.0.0:

13.0.0
======

.. _neutron_13.0.0_Other Notes:

Other Notes
-----------

.. releasenotes/notes/metering-iptables-driver-load-interface-driver-ca397f1db40ec643.yaml @ b'ad2c1bc374b6c21439cddc92e97d6f6d941e3507'

- The metering agent iptables driver can now load its interface driver by
  using a stevedore alias in the ``metering_agent.ini`` file. For example,
  ``interface_driver = openvswitch``  instead of
  ``interface_driver = neutron.agent.linux.interface.OVSInterfaceDriver``


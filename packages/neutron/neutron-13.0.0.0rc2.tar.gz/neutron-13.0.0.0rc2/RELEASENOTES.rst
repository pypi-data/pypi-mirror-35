=======
neutron
=======

.. _neutron_13.0.0.0rc2:

13.0.0.0rc2
===========

.. _neutron_13.0.0.0rc2_Other Notes:

Other Notes
-----------

.. releasenotes/notes/metering-iptables-driver-load-interface-driver-ca397f1db40ec643.yaml @ b'ad2c1bc374b6c21439cddc92e97d6f6d941e3507'

- The metering agent iptables driver can now load its interface driver by
  using a stevedore alias in the ``metering_agent.ini`` file. For example,
  ``interface_driver = openvswitch``  instead of
  ``interface_driver = neutron.agent.linux.interface.OVSInterfaceDriver``


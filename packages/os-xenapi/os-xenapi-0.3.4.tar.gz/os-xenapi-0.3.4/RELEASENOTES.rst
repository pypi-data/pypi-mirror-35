=========
os-xenapi
=========

.. _os-xenapi_0.3.2:

0.3.2
=====

.. _os-xenapi_0.3.2_New Features:

New Features
------------

.. releasenotes/notes/compute-bootstrap-54cb5eb24b6ba133.yaml @ 9f31d2af8f3d7d8ac6f9f059ba97b8fce5477c25

- Now we can support boostrap an OpenStack compute node by running the command of
  ``xenapi_bootstrap`` from a VM which is running on XenServer. It will automatically
  finish the following bootstrap tasks:
  
  * configure HIMN interface (firstly need add a VIF for the VM to connect to HIMN.)
  
  * configure iptalbes to allow OpenStack traffic between compute VM and Dom0.
  
  * install OpenStack XAPI plugins into Dom0
  
  * gather XenAPI facts and save them into a json file which can be used
    as input for other OpenStack deployment tasks.
  
  * and other misc bootstrap operations: e.g. enable Linux bridge in Dom0.
  
  .. note::
  
         At the moment, ``xenapi_bootstrap`` only supports CentOS 7.x.

.. releasenotes/notes/vdi-stream-536202fc2f0a4d0a.yaml @ b61ca2a13cd3d63da76fbd2c4aa2f61d94431724

- The os-xenapi library now supports the VDI streaming feature which will
  allow the library user to create XenServer VDI from a gzipped image data
  stream; or create gzipped image data stream from a specified XenServer
  VDI.
  
  By comparing to the existing dom0 glance plugin, the image data gets
  processed on the fly via streams. So it doesn't create intermediate files.
  And it completely uses the formal VDI import or export APIs when it
  exchanges VDI data with XenServer.

.. releasenotes/notes/xapi-pool-f6282fbca7c0690a.yaml @ b61ca2a13cd3d63da76fbd2c4aa2f61d94431724

- The os-xenapi library now supports XAPI pool. We can deploy OpenStack on
  hosts which belong to a XAPI pool, so that we can get the benefits from
  XAPI pool features: e.g. it's able to live migrate between two hosts
  without moving the disks on shared storage.


========
masakari
========

.. _masakari_6.0.0.0rc1:

6.0.0.0rc1
==========

.. _masakari_6.0.0.0rc1_New Features:

New Features
------------

.. releasenotes/notes/recovery-method-customization-3438b0e26e322b88.yaml @ b'ad3dc737c984c267980e7479acc2bf8856b556d5'

- Operator can now customize workflows to process each type of failure
  notifications (hosts, instance and process) as per their requirements.
  Added below new config section for customized recovery flow in a new conf
  file masakari-custom-recovery-methods.conf
  
  - [taskflow_driver_recovery_flows]
  
  Under [taskflow_driver_recovery_flows] is added below five new config options
  
  - 'instance_failure_recovery_tasks' is a dict of tasks which will recover
    instance failure.
  - 'process_failure_recovery_tasks' is a dict of tasks which will recover
    process failure.
  - 'host_auto_failure_recovery_tasks' is a dict of tasks which will recover
    host failure for auto recovery.
  - 'host_rh_failure_recovery_tasks' is a dict of tasks which will recover
    host failure for rh recovery on failure host.


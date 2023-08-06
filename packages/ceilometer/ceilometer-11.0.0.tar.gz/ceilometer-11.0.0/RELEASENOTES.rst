==========
ceilometer
==========

.. _ceilometer_11.0.0:

11.0.0
======

.. _ceilometer_11.0.0_New Features:

New Features
------------

.. releasenotes/notes/add-disk-latency-metrics-9e5c05108a78c3d9.yaml @ b'8fdd19e78a2053285569cda05cdc4875b716190c'

- Add `disk.device.read.latency` and `disk.device.write.latency` meters to
  capture total time used by read or write operations.

.. releasenotes/notes/instance-record-launched-created-deleted-d7f44df3bbcf0790.yaml @ b'36414e1cebe3a43d962f8d2adfe7cc34742e9057'

- `launched_at`/`created_at`/`deleted_at` of Nova instances are now tracked.

.. releasenotes/notes/polling-batch-size-7fe11925df8d1221.yaml @ b'2dc21a5f05ee670292a8a7f97952d3942c32f5cf'

- Add support for configuring the size of samples the poller will send in each batch.

.. releasenotes/notes/prometheus-bcb201cfe46d5778.yaml @ b'2b8052052d861b856b3522a8d7f857735793f01b'

- A new pulisher have been added to push data to Prometheus Pushgateway.

.. releasenotes/notes/save-rate-in-gnocchi-66244262bc4b7842.yaml @ b'e906bcda82918aff000ab76f067a2dc49660d0b4'

- Archive policies can now be configured per metrics in gnocchi_resources.yaml.
  A default list of archive policies is now created by Ceilometer.
  They are called "ceilometer-low-rate" for all IOs metrics and "ceilometer-low"
  for others.

.. releasenotes/notes/use-usable-metric-if-available-970ee58e8fdeece6.yaml @ b'2dee485da7a6f2cdf96525fabc18a8c27c8be570'

- use memory usable metric from libvirt memoryStats if available.


.. _ceilometer_11.0.0_Known Issues:

Known Issues
------------

.. releasenotes/notes/gnocchi-no-metric-by-default-b643e09f5ffef2c4.yaml @ b'826ba35c6eb9900bb0a557f6e4f06f7d1b9bd394'

- Ceilometer created metrics that could never get measures depending on the
  polling configuration. Metrics are now created only if Ceilometer gets at
  least a measure for them.


.. _ceilometer_11.0.0_Upgrade Notes:

Upgrade Notes
-------------

.. releasenotes/notes/add-ipmi-sensor-data-gnocchi-70573728499abe86.yaml @ b'663c523328690dfcc30c1ad986ba57e566bd194c'

- `ceilometer-upgrade` must be run to build IPMI sensor resource in Gnocchi.

.. releasenotes/notes/polling-batch-size-7fe11925df8d1221.yaml @ b'2dc21a5f05ee670292a8a7f97952d3942c32f5cf'

- batch_size option added to [polling] section of configuration. Use batch_size=0 to disable batching of samples.

.. releasenotes/notes/remove-gnocchi-dispatcher-options-4f4ba2a155c1a766.yaml @ b'c567258979064d4a6e82057f68587b184ee939aa'

- The deprecated `gnocchi_dispatcher` option group has been removed.

.. releasenotes/notes/removed-rgw-ae3d80c2eafc9319.yaml @ b'dd1b7abf329755c8377862328f770e0b7974f5c2'

- Deprecated `rgw.*` meters have been removed. Use `radosgw.*` instead.

.. releasenotes/notes/save-rate-in-gnocchi-66244262bc4b7842.yaml @ b'e906bcda82918aff000ab76f067a2dc49660d0b4'

- Ceilometer now creates it own archive policies in Gnocchi and use them to
  create metrics in Gnocchi. Old metrics kept their current archive policies
  and will not be updated with ceilometer-upgrade. Only newly created metrics
  will be impacted. Archive policy can still be overridden with the publisher url
  (e.g: gnocchi://archive_policy=high).


.. _ceilometer_11.0.0_Deprecation Notes:

Deprecation Notes
-----------------

.. releasenotes/notes/polling-batch-size-7fe11925df8d1221.yaml @ b'2dc21a5f05ee670292a8a7f97952d3942c32f5cf'

- The option batch_polled_samples in the [DEFAULT] section is deprecated. Use batch_size option in [polling] to configure and/or disable batching.

.. releasenotes/notes/save-rate-in-gnocchi-66244262bc4b7842.yaml @ b'e906bcda82918aff000ab76f067a2dc49660d0b4'

- cpu_util and \*.rate meters are deprecated and will be removed in future
  release in favor of the Gnocchi rate calculation equivalent.

.. releasenotes/notes/transformer-ed4b1ea7d1752576.yaml @ b'1dcbd607df0696101b40f77d7721489679ebe0ba'

- Usage of transformers in Ceilometer pipelines is deprecated. Transformers in Ceilometer
  have never computed samples correctly when you have multiple workers. This functionality can
  be done by the storage backend easily without all issues that Ceilometer has. For example, the
  rating is already computed in Gnocchi today.

.. releasenotes/notes/transformer-ed4b1ea7d1752576.yaml @ b'1dcbd607df0696101b40f77d7721489679ebe0ba'

- Pipeline Partitioning is also deprecated. This was only useful to
  workaround of some issues that tranformers has.


.. _ceilometer_11.0.0_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/add-ipmi-sensor-data-gnocchi-70573728499abe86.yaml @ b'663c523328690dfcc30c1ad986ba57e566bd194c'

- Ceilometer previously did not create IPMI sensor data from IPMI agent or
  Ironic in Gnocchi. This data is now pushed to Gnocchi.


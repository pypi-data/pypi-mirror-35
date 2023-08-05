=======
tempest
=======

.. _tempest_19.0.0:

19.0.0
======

.. _tempest_19.0.0_Prelude:

Prelude
-------

.. releasenotes/notes/tempest-rocky-release-0fc3312053923380.yaml @ 94743a111bf368b40c419c257b6a9796a0661fde

This release is to tag the Tempest for OpenStack Rocky release. After this release, Tempest will support below OpenStack Releases:

  * Rocky
  * Queens
  * Pike
  * Ocata

Current development of Tempest is for OpenStack Stein development cycle. Every Tempest commit is also tested against master during the Stein cycle. However, this does not necessarily mean that using Tempest as of this tag will work against a Stein (or future release) cloud. To be on safe side, use this tag to test the OpenStack Rocky release.

.. _tempest_19.0.0_New Features:

New Features
------------

.. releasenotes/notes/add-additional-methods-to-policy-client-library-b8279c18335588c9.yaml @ 1269c617ddb82bd2a5d713e7b4c1da2359c33855

- Add ``v3-ext/OS-ENDPOINT-POLICY`` API calls to support creation, deletion and
  retrieval of associations between service endpoints and policies. Such associations
  enable an endpoint to request its policy.

.. releasenotes/notes/add-extra-apis-to-volume-v3-services-client-bf9b235cf5a611fe.yaml @ 408cf57f1d2a306a1cd448943d3f0a6fc397601c

- Add ``enable_service``, ``disable_service`` , ``disable_log_reason``,
  ``freeze_host`` and ``thaw_host`` API endpoints to volume v3
  ``services_client``.

.. releasenotes/notes/add-storyboard-in-skip-because-decorator-3e139aa8a4f7970f.yaml @ 7d8c2810319b606f7a04cd79d63734394c70dcd0

- Add a new parameter called ``bug_type`` to
  ``tempest.lib.decorators.related_bug`` and
  ``tempest.lib.decorators.skip_because`` decorators, which accepts
  2 values:
  
  * launchpad
  * storyboard
  
  This offers the possibility of tracking bugs related to tests using
  launchpad or storyboard references. The default value is launchpad
  for backward compatibility.
  
  Passing in a non-digit ``bug`` value to either decorator will raise
  a ``InvalidParam`` exception (previously ``ValueError``).

.. releasenotes/notes/add-update-flavor--api-to-flavors-client-a859542fe54aab7c.yaml @ 52c5d28190a1b3ee4d76c42021495b04f4fe5eb0

- Add update flavor API to compute flavors_client library.

.. releasenotes/notes/bp-application-credentials-df69b1f617db1bb9.yaml @ 0e52d4e706e43099efc2fb5df16f5bd9466d9b30

- [`blueprint application-credentials <https://blueprints.launchpad.net/keystone/+spec/application-credentials>`_]
  Tempest can test keystone's application credentials interface. A new client
  library is added for application credentials, and a new config option,
  ``[identity-feature-enabled]/application_credentials``, can control whether
  the application credentials feature is tested (defaults to False,
  indicating the feature is not enabled in the cloud under test).

.. releasenotes/notes/identity-v3-project-tags-client-36683c6a8644e54b.yaml @ a3b2d8e1b2320c0418ef5cd95d11a018b92cd2a1

- Add ``project_tags_client`` to the identity v3 library. This feature
  enables the possibility of invoking the following API actions:
  
  * update_project_tag
  * list_project_tags
  * update_all_project_tags
  * check_project_tag_existence
  * delete_project_tag
  * delete_all_project_tags

.. releasenotes/notes/tempest-lib-compute-update-service-6019d2dcfe4a1c5d.yaml @ c0348ee84e4ea1c7d874f170554ac369d57702b6

- The ``update_service`` API is added to the ``services_client`` compute
  library. This API is introduced in microversion 2.53 and supersedes
  the following APIs:
  
  * ``PUT /os-services/disable`` (``disable_service``)
  * ``PUT /os-services/disable-log-reason`` (``disable_log_reason``)
  * ``PUT /os-services/enable`` (``enable_service``)
  * ``PUT /os-services/force-down`` (``update_forced_down``)

.. releasenotes/notes/vnc-hardcoded-server-name-removed-6f8d1e90a175dc08.yaml @ 82b6aebee79e3a4709268a45861069cb87b3f96a

- New string configuration option ``vnc_server_header`` is added
  to ``compute-feature-enabled`` section. It offers to provide VNC server
  name that is to be expected in the responce header. For example, obvious
  at hand names is 'WebSockify', 'nginx'.

.. releasenotes/notes/volume-v3-service-clients-a863a6336af56cca.yaml @ de676babd37270c99288ec5906ef33b9f85102ae

- Adds volume service clients for v3 APIs. As v3 base API should be
  identical to v2 APIs, we just copy all existing v2 service client
  for v3 API.


.. _tempest_19.0.0_Upgrade Notes:

Upgrade Notes
-------------

.. releasenotes/notes/cinder-use-os-endpoint-type-c11f63fd468ceb4c.yaml @ 2e354d7a03d846ecc1342563f5cfc563dbecb145

- Cinder CLI calls have now been updated to use the ``--os-endpoint-type``
  option instead of ``--endpoint-type``. The latter had been deprecated in
  Cinder and has been removed in the Rocky release.

.. releasenotes/notes/remove-allow_tenant_isolation-option-03f0d998eb498d44.yaml @ 553d7cbddc99798cc4adfa032f7e57f6ddb0ff45

- Remove deprecated config option ``allow_tenant_isolation`` from
  ``auth`` and ``compute`` groups. Use ``use_dynamic_credentials`` directly
  instead of the removed option.

.. releasenotes/notes/volume-service-testing-default-to-v3-endpoints-20b86895a590925d.yaml @ 89c213fb355f0ec672ae8002c516cf11f568960b

- The volume config option ``catalog_type`` default is changed to
  ``volumev3`` which is v3 API endpoint configured in devstack.
  With this change Tempest will be testing v3 API as default.
  User who want to test v2 API can still test by configuring the
  ``catalog_type`` to v2 endpoint.


.. _tempest_19.0.0_Deprecation Notes:

Deprecation Notes
-----------------

.. releasenotes/notes/deprecate-volume-api-selection-config-options-b95c5c0ccbf38916.yaml @ f2f4384563ad6eadabd4ae787bfd5bc54fe7aa45

- The v2 volume API has been deprecated since Pike release.
  Volume v3 API is current and Tempest volume tests can
  be run against v2 or v3 API based on config option
  ``CONF.volume.catalog_type``. If catalog_type is ``volumev2``, then
  all the volume tests will run against v2 API. If catalog_type is
  ``volumev3`` which is default in Tempest, then all the volume
  tests will run against v3 API.
  That makes below config options unusable in Tempest which used to
  select the target volume API for volume tests.
  
  * ``CONF.volume-feature-enabled.api_v2``
  * ``CONF.volume-feature-enabled.api_v3``
  
  Tempest deprecate the above two config options in Rocky release
  and will be removed in future. Alternatively ``CONF.volume.catalog_type``
  can be used to run the Tempest against volume v2 or v3 API.

.. releasenotes/notes/volume-v3-service-clients-a863a6336af56cca.yaml @ de676babd37270c99288ec5906ef33b9f85102ae

- Deprecates the volume service clients for v2 APIs. Volume v2 APIs
  are deprecated in all supported stable branches, so it's time
  to deprecate the tempest service clients for v2 APIs and remove in future
  release.


.. _tempest_19.0.0_Security Issues:

Security Issues
---------------

.. releasenotes/notes/omit_X-Subject-Token_from_log-1bf5fef88c80334b.yaml @ 2902a7bcd6b839525a632b0102c5589d2e50f0c8

- The x-subject-token of a response header is ommitted from log,
  but clients specify the same token on a request header on
  Keystone API and that was not omitted. In this release,
  that has been omitted for a security reason.


.. _tempest_19.0.0_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/fix-show-image-file-expected-code-92d97342d0f6d60e.yaml @ fd5a14b7383ac49ad4ffbef6ddcc8509222c030d

- Fix show_image_file interface in v2 ImagesClient: Bug#1756264.
  The expected success code of show_image_file is changed from
  ``200`` to ``[200, 204, 206]``.

.. releasenotes/notes/vnc-hardcoded-server-name-removed-6f8d1e90a175dc08.yaml @ 82b6aebee79e3a4709268a45861069cb87b3f96a

- Fix VNC server response header issue when it is behind reverse proxy


.. _tempest_18.0.0:

18.0.0
======

.. _tempest_18.0.0_Prelude:

Prelude
-------

.. releasenotes/notes/start-of-queens-support-fea9051ba1d85fc7.yaml @ 891299e4480f45f7326fa43a6f2613ef5cfe42bd

This release marks the start of Queens release support in Tempest. This release also marks the end of support for Newton in Tempest.


.. _tempest_18.0.0_New Features:

New Features
------------

.. releasenotes/notes/add-group-type-specs-apis-to-v3-group-types-client-10390b52dedede54.yaml @ 98dc45ca3ce3371e93cc1973d9f1608b04a2597d

- Add group type specs APIs to v3 group_types_client library.
  
  * create_or_update_group_type_specs
  * list_group_type_specs
  * show_group_type_specs_item
  * update_group_type_specs_item
  * delete_group_type_specs_item

.. releasenotes/notes/add-port-profile-config-option-2610b2fa67027960.yaml @ 16d9cf067119fe837834b7a848a808cf785ebca3

- A new config option 'port_profile' is added to the section 'network' to specify capabilities of the port. By default this is set to {}. When using OVS HW offload feature we need to create Neutron port with a certain capability. This is done by creating Neutron port with binding profile. To be able to test this we need profile capability support in Tempest as well.

.. releasenotes/notes/add-show-default-quotas-api-to-network-quotas-client-3a7c1159af9e56ff.yaml @ 6e695c9626518c58720adf2858ab80f65ca873ef

- Add show default quotas API to network quotas_client library.
  This feature enables the possibility to show default network quotas for
  a specified project.

.. releasenotes/notes/add-show-encryption-specs-item-api-to-v2-encryption-types-client-290b421cd4bc0c0e.yaml @ d88a250924c034ba1c82793e04e99c95f037525e

- Add show encryption specs item API to v2 encryption_types_client library.
  This feature enables the possibility to show specific encryption specs for
  a volume type.

.. releasenotes/notes/add-show-quota-details-api-to-network-quotas-client-3fffd302cc5d335f.yaml @ 5aeb551a58078abd34884583ac70ad425f4590ba

- Add extension API show quota details to network quotas_client library.
  This feature enables the possibility to show a quota set for a specified
  project that includes the quota's used, limit and reserved counts per
  resource.

.. releasenotes/notes/add-update-api-to-group-types-client-09c06ccdf80d5003.yaml @ a2f69f11a786565be6d9aa46e09190f2cd0dbf76

- Add update group types API to v3 ``group_types_client`` library;
  min_microversion of this API is 3.11.

.. releasenotes/notes/create-mount-config-drive-to-lib-1a6e912b8afbcc7e.yaml @ b6c6d2a128ded6bcda1ae3536da237a71c4780a4

- A function has been added to the common library to allow mounting and unmounting of the config drive consistently.

.. releasenotes/notes/switch-to-stestr-8c9f834b3f5a55d8.yaml @ 8a4396e3d3b48447a1ea1b9c20810e1cc3a6c357

- The Tempest CLI commands have switched from calling testrepository internally to use stestr instead. This means that all of the features and bug fixes from moving to stestr are available to the tempest commands.

.. releasenotes/notes/tempest-run-fix-updates-564b41706decbba1.yaml @ 7ba22721e544d4f02172ffa59cc7ebc7a27c1ddf

- Adds a new CLI arg in tempest run, ``--black-regex``, which is a
  regex to exclude the tests that match it.

.. releasenotes/notes/volume-backed-live-mig-5a38b496ba1ec093.yaml @ 334f313220b97761a9bab3976e72f4cef4f53b3a

- A new boolean configuration option
  ``[compute-feature-enabled]/volume_backed_live_migration`` has been added.
  If enabled, tests which validate the behavior of Nova's *volume-backed live
  migration* feature will be executed. The option defaults to ``False``.


.. _tempest_18.0.0_Upgrade Notes:

Upgrade Notes
-------------

.. releasenotes/notes/removal-deprecated-config-options-3db535b979fe3509.yaml @ 6283daa5ad4c92ca5d1917cdde8dd96ff4b28e04

- Below config options or feature flags were deprecated for removal.
  It's time to remove them as all supported stable branches are
  good to handle them.
  
  * ``[identity-feature-enabled].forbid_global_implied_dsr``
  * ``[image-feature-enabled].deactivate_image``
  * ``[default].resources_prefix``
  * config group ``orchestration``
  * ``[service_available].heat``

.. releasenotes/notes/remove-deprecated-skip_unless_attr-decorator-02bde59a00328f5c.yaml @ 0648215f58c3806cba43a38518956cdb3a3e81c0

- Remove the deprecated decorator ``skip_unless_attr`` in lib/decorators.py.

.. releasenotes/notes/removed-tox-ostestr-8997a93d199c44f3.yaml @ be11739269714276c3619762f1aba126d5fd399f

- The tox ostestr job (normally invoked with ``tox -eostestr``) has been
  removed. This was lightly used, and in the near future ostestr will be
  removed from the tempest requirements file. If you were relying on this
  functionality you can replicate it by using the venv-tempest tox job. For
  example, simply running ``tox -evenv-tempest -- ostestr`` will do the same
  thing the old ostestr job did.

.. releasenotes/notes/switch-to-stestr-8c9f834b3f5a55d8.yaml @ 8a4396e3d3b48447a1ea1b9c20810e1cc3a6c357

- Tempest CLI commands will no long rely on anything from testr. This means any data in existing testr internals that were being exposed are no longer present. For example things like the .testr directories will be silently ignored. There is a potential incompatibility for existing users who are relying on test results being stored by testr. Anything relying on previous testr behavior will need to be updated to handle stestr.


.. _tempest_18.0.0_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/tempest-run-fix-updates-564b41706decbba1.yaml @ 7ba22721e544d4f02172ffa59cc7ebc7a27c1ddf

- Fixes tempest run CLI args mutually exclusive behavior which should not
  be the case anymore (Bug#1751201).


.. _tempest_18.0.0_Other Notes:

Other Notes
-----------

.. releasenotes/notes/cli-tests-v3fixes-fb38189cefd64213.yaml @ 7ba22721e544d4f02172ffa59cc7ebc7a27c1ddf

- The CLIClient class, when it calls a command line client, uses
  ``--os-project-name`` instead of ``--os-tenant-name`` for the
  project, and passes ``--os-identity-api-version`` (default empty).
  All CLI clients still available in supported releases of OpenStack
  which are wrapped by the ``cmd_with_auth()`` method support those
  switches.

.. releasenotes/notes/config-volume-multiattach-ea8138dfa4fd308c.yaml @ 81fa9b6aaa7330995310069b8511e90b1a6d5181

- A new configuration option ``[compute-feature-enabled]/volume_multiattach``
  has been added which defaults to False. Set this to True to enable volume
  multiattach testing. These tests require that compute API version 2.60 is
  available and block storage API version 3.44 is available.
  
  .. note:: In the Queens release, the only compute driver that supports
    volume multiattach is the libvirt driver, and only then when qemu<2.10
    or libvirt>=3.10. The only volume backend in Queens that supports volume
    multiattach is lvm.

.. releasenotes/notes/start-of-queens-support-fea9051ba1d85fc7.yaml @ 891299e4480f45f7326fa43a6f2613ef5cfe42bd

- OpenStack Releases supported after this release are **Queens**, **Pike**, and **Ocata**.
  The release under current development of this tag is Rocky, meaning that every Tempest commit is also tested against master during the Rocky cycle. However, this does not necessarily mean that using Tempest as of this tag will work against a Rocky (or future release) cloud.


.. _tempest_17.2.0:

17.2.0
======

.. _tempest_17.2.0_New Features:

New Features
------------

.. releasenotes/notes/add-support-args-kwargs-in-call-until-true-a91k592h5a64exf7.yaml @ 1382e971fbb3506ecec7c8549cb8ecac7e1c43e1

- Add support of args and kwargs when calling func in call_until_true, also to log the cost time when call_until_true returns True or False for debugging.

.. releasenotes/notes/list-auth-domains-v3-endpoint-9ec60c7d3011c397.yaml @ 60ebc5d0e35c806bf882a0bf99453702ad0749ad

- Add ``list_auth_domains`` API endpoint to the identity v3 client. This
  allows the possibility of listing all domains a user has access to
  via role assignments.


.. _tempest_17.2.0_Upgrade Notes:

Upgrade Notes
-------------

.. releasenotes/notes/drop-DEFAULT_PARAMS-bfcc2e7b74ef880b.yaml @ cad70e20cf8a04b809be54f122bff82aae8f4137

- Replace any call in your code to credentials_factory.DEFAULT_PARAMS with
  a call to config.service_client_config().

.. releasenotes/notes/remove-deprecated-volume-apis-from-v2-volumes-client-cf35e5b4cca89860.yaml @ 710c8422fe20c28c229637588f6f4fa7bffee762

- Remove deprecated APIs (``show_pools`` and ``show_backend_capabilities``)
  from volume v2 volumes_client, and the deprecated APIs are re-realized in
  volume v2 scheduler_stats_client (``list_pools``) and capabilities_client
  (``show_backend_capabilities``) accordingly.


.. _tempest_17.2.0_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/drop-DEFAULT_PARAMS-bfcc2e7b74ef880b.yaml @ cad70e20cf8a04b809be54f122bff82aae8f4137

- The credentials_factory module used to load configuration at import time
  which caused configuration being loaded at test discovery time.
  This was fixed by removing the DEFAULT_PARAMS variable. This variable
  was redundant (and outdated), the same dictionary (but up to date) can
  be obtained via invoking config.service_client_config() with no service
  parameter.


.. _tempest_17.1.0:

17.1.0
======

.. _tempest_17.1.0_Prelude:

Prelude
-------

.. releasenotes/notes/intermediate-queens-release-2f9f305775fca454.yaml @ a22794d93f5845d2787f34b4f8f154db1ffbef17

This is an intermediate release during the Queens development cycle to make new functionality available to plugins and other consumers.


.. _tempest_17.1.0_New Features:

New Features
------------

.. releasenotes/notes/add-load-list-cmd-35a4a2e6ea0a36fd.yaml @ 7ba22721e544d4f02172ffa59cc7ebc7a27c1ddf

- Adds a new cli option to tempest run, ``--load-list <list-file>``
  to specify target tests to run from a list-file. The list-file
  supports the output format of the tempest run ``--list-tests``
  command.

.. releasenotes/notes/add-reset-group-snapshot-status-api-to-v3-group-snapshots-client-248d41827daf2a0c.yaml @ 23df2c0ac52b9a2a8f0cb9adb72ddebb5c86f775

- Add reset group snapshot status API to v3 group_snapshots_client library,
  min_microversion of this API is 3.19. This feature enables the possibility
  to reset group snapshot status.

.. releasenotes/notes/add-reset-group-status-api-to-v3-groups-client-9aa048617c66756a.yaml @ cca9974d338c89b20778e44a277149563aa6805b

- Add reset group status API to v3 groups_client library, min_microversion
  of this API is 3.20. This feature enables the possibility to reset group
  status.

.. releasenotes/notes/add-validation-resources-to-lib-dc2600c4324ca4d7.yaml @ 0477accd328220c725bdf227b25cbe8ce2862e72

- Add the `validation_resources` module to tempest.lib. The module provides
  a set of helpers that can be used to provision and cleanup all the
  resources required to perform ping / ssh tests against a virtual machine:
  a keypair, a security group with targeted rules and a floating IP.

.. releasenotes/notes/add_proxy_url_get_credentials-aef66b085450513f.yaml @ cb94b5e506808463caef9fcd302cb1f40c6216a9

- Add the proxy_url optional parameter to the get_credentials method in
  tempest/lib/auth.py so that that helper can be used when going through
  and HTTP proxy.

.. releasenotes/notes/compare-header-version-func-de5139b2161b3627.yaml @ 1382e971fbb3506ecec7c8549cb8ecac7e1c43e1

- Add a new function called ``compare_version_header_to_response`` to
  ``tempest.lib.common.api_version_utils``, which compares the API
  microversion in the response header to another microversion using the
  comparators defined in
  ``tempest.lib.common.api_version_request.APIVersionRequest``.
  
  It is now possible to determine how to retrieve an attribute from a
  response body of an API call, depending on the returned microversion.
  
  Add a new exception type called ``InvalidParam`` to
  ``tempest.lib.exceptions``, allowing the possibility of raising an
  exception if an invalid parameter is passed to a library function.

.. releasenotes/notes/http_proxy_config-cb39b55520e84db5.yaml @ 74514400a2042ea8362c40a166e014b47b838f7d

- Adds a new config options, ``proxy_url``. This options is used to configure running tempest through a proxy server.

.. releasenotes/notes/http_proxy_config-cb39b55520e84db5.yaml @ 74514400a2042ea8362c40a166e014b47b838f7d

- The RestClient class in tempest.lib.rest_client has a new kwarg parameters, ``proxy_url``, that is used to set a proxy server.

.. releasenotes/notes/http_proxy_config-cb39b55520e84db5.yaml @ 74514400a2042ea8362c40a166e014b47b838f7d

- A new class was added to tempest.lib.http, ClosingProxyHttp. This behaves identically to ClosingHttp except that it requires a proxy url and will establish a connection through a proxy

.. releasenotes/notes/identity-tests-domain-drivers-76235f6672221e45.yaml @ 9cafd3d045b6253a6821e38857ebfd9f3675aeda

- A new boolean config option ``domain_specific_drivers``
  is added to the section ``identity-feature-enabled``.
  This option must be enabled when testing an environment that
  is configured to use domain-specific identity drivers.

.. releasenotes/notes/make-object-storage-client-as-stable-interface-d1b07c7e8f17bef6.yaml @ 986407ddd3e8cafac9e699ca90886ae8cb5c1bf9

- Define below object storage service clients as libraries.
  Add new service clients to the library interface so the
  other projects can use these modules as stable libraries
  without any maintenance changes.
  
    * account_client
    * container_client
    * object_client

.. releasenotes/notes/test-clients-stable-for-plugin-90b1e7dc83f28ccd.yaml @ bf142fc3d8cab33aca1756869c92954a05de4a0c

- Two extra modules are now marked as stable for plugins, test.py and clients.py.
  The former includes the test base class with its automatic credentials
  provisioning and test resource managing fixtures.
  The latter is built on top of ServiceClients and it adds aliases and a few custom
  configurations to it.


.. _tempest_17.1.0_Upgrade Notes:

Upgrade Notes
-------------

.. releasenotes/notes/disable-identity-v2-testing-4ef1565d1a5aedcf.yaml @ 1fbad23824bbb5f43cddb796a3f950d448cf9cc5

- As of the Queens release, tempest no longer tests the identity v2.0 API
  because the majority of the v2.0 API have been removed from the identity
  project. Once the Queens release reaches end-of-life, we can remove the
  v2.0 tempest tests and clean up v2.0 testing cruft.

.. releasenotes/notes/remove-deprecated-apis-from-v2-volumes-client-3ca4a5db5fea518f.yaml @ 0befe81e68bf765cc7c74d511a55092b1c503a19

- Remove deprecated APIs from volume v2 volumes_client, and the deprecated
  APIs are re-realized in volume v2 transfers_client.
  
  * create_volume_transfer
  * show_volume_transfer
  * list_volume_transfers
  * delete_volume_transfer
  * accept_volume_transfer

.. releasenotes/notes/remove-deprecated-skip-decorators-f8b42d812d20b537.yaml @ f92e6d42f0105004f6647b028acc64a202c2b2ca

- Remove two deprecated skip decorators in ``config`` module:
  ``skip_unless_config`` and ``skip_if_config``.

.. releasenotes/notes/remove-get-ipv6-addr-by-EUI64-c79972d799c7a430.yaml @ 712dafab0d0606e1a656c0e8c78111db7fed3844

- Remove deprecated get_ipv6_addr_by_EUI64 method from data_utils.
  Use the same method from oslo_utils.netutils.


.. _tempest_17.1.0_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/add-domain-param-in-cliclient-a270fcf35c8f09e6.yaml @ b441134c584f948c35526e932f0d1ae077eaeb98

- Allow to specify new domain parameters:
  
  * `user_domain_name`
  * `user_domain_id`
  * `project_domain_name`
  * `project_domain_id`
  
  for CLIClient class, whose values will be substituted to
  ``--os-user-domain-name``, ``--os-user-domain-id``,
  ``--os-project-domain-name`` and ``--os-project-domain-id`` respectively
  during command execution.
  
  This allows to prevent possible test failures with authentication in
  Keystone v3. Bug: #1719687

.. releasenotes/notes/fix-list-group-snapshots-api-969d9321002c566c.yaml @ 6ec582f1115a290bce4cb0a40d8e97d3ab77b86c

- Fix list_group_snapshots API in v3 group_snapshots_client: Bug#1715786.
  The url path for list group snapshots with details API is changed from
  ``?detail=True`` to ``/detail``.


.. _tempest_17.0.0:

17.0.0
======

.. _tempest_17.0.0_Prelude:

Prelude
-------

.. releasenotes/notes/start-of-pike-support-f2a1b7ea8e8b0311.yaml @ 35976ed20697cd4e4077c8f2279f02ec01a7c6d7

This release marks the start of support for the Pike release in Tempest.


.. _tempest_17.0.0_New Features:

New Features
------------

.. releasenotes/notes/add-create-group-from-src-tempest-tests-9eb8b0b4b5c52055.yaml @ d56edc35ecc6774f92e2f4ff6e2c6a219ca35759

- Add create_group_from_source to groups_client in the volume service library.

.. releasenotes/notes/add-is-resource-deleted-sg-client-f4a7a7a54ff024d7.yaml @ 463a8a64ef5ba8f9e295cafc0f7d71826c414267

- Implement the `rest_client` method `is_resource_deleted` in the network
  security group client.

.. releasenotes/notes/add-params-to-v2-list-backups-api-c088d2b4bfe90247.yaml @ a2df0f57a7cadec02b498395439cc7ed9445fea2

- The ``list_backups`` method of the v2 ``BackupsClient`` class now has
  an additional ``**params`` argument that enables passing additional
  information in the query string of the HTTP request.

.. releasenotes/notes/add-show-volume-image-metadata-api-to-v2-volumes-client-ee3c027f35276561.yaml @ f0599b19fdb9a4cf035aff550369f8a91793241e

- Add show volume image metadata API to v2 volumes_client library.
  This feature enables the possibility to show volume's image metadata.

.. releasenotes/notes/add-update-group-tempest-tests-72f8ec19b2809849.yaml @ 9ee986075935eaa10c3102af87e669618b634ee1

- Add update_group to groups_client in the volume service library.

.. releasenotes/notes/add-volume-group-snapshots-tempest-tests-840df3da26590f5e.yaml @ 41ed715c2306b701fea19adfc9e0f187a5dcf381

- Add group_snapshots client for the volume service as library.
  Add tempest tests for create group snapshot, delete group snapshot, show
  group snapshot, and list group snapshots volume APIs.

.. releasenotes/notes/add-volume-group-types-tempest-tests-1298ab8cb4fe8b7b.yaml @ 6891411395a581ec42f8d28f42842e35cc15ddb4

- Add list_group_type and show_group_type in the group_types client for
  the volume service. Add tests for create/delete/show/list group types.

.. releasenotes/notes/credentials-factory-stable-c8037bd9ae642482.yaml @ 17347f0effe9d0dd85408dd623446873cafa4a36

- The credentials_factory.py module is now marked as stable for Tempest
  plugins. It provides helpers that can be used by Tempest plugins to
  obtain test credentials for their test cases in a format that honors the
  Tempest configuration in use.
  Credentials may be provisioned on the fly during the test run, or they
  can be setup in advance and fed to test via a YAML file; they can be
  setup for identity v2 or identity v3.

.. releasenotes/notes/extra-compute-services-tests-92b6c0618972e02f.yaml @ fe399fdfeb1521189a18f4d32f1fe0d8b3695ed0

- Add the ``disable_log_reason`` and the ``update_forced_down`` API endpoints
  to the compute ``services_client``.
  Add '2.11' compute validation schema for compute services API.

.. releasenotes/notes/identity_client-635275d43abbb807.yaml @ 1e8a0ed3e5feb9c113d54ce1252d7a3e8ce750ce

- Enhances the v3 identity client with the ``check_token_existence``
  endpoint, allowing users to check the existence of tokens

.. releasenotes/notes/migrate-dynamic-creds-ecebb47528080761.yaml @ c51b712dec2013edeeaa3e91e65f94a7bb185574

- The tempest module tempest.common.dynamic creds which is used for
  dynamically allocating credentials has been migrated into tempest lib.

.. releasenotes/notes/migrate-object-storage-as-stable-interface-42014c7b43ecb254.yaml @ b282eb767f8b4b12b4588ea1f6293464a9d422e2

- Define below object storage service clients as libraries.
  Add new service clients to the library interface so the
  other projects can use these modules as stable libraries
  without any maintenance changes.
  
    * bulk_middleware_client
    * capabilities_client

.. releasenotes/notes/migrate-preprov-creds-ef61a046ee1ec604.yaml @ b19c55df4bb30a65e3e6abfa977dd9e857a330a4

- The tempest module tempest.common.preprov_creds which is used to provide credentials from a list of preprovisioned resources has been migrated into tempest lib at tempest.lib.common.preprov_creds.

.. releasenotes/notes/migrate-preprov-creds-ef61a046ee1ec604.yaml @ b19c55df4bb30a65e3e6abfa977dd9e857a330a4

- The InvalidTestResource exception class from tempest.exceptions has been migrated into tempest.lib.exceptions

.. releasenotes/notes/migrate-preprov-creds-ef61a046ee1ec604.yaml @ b19c55df4bb30a65e3e6abfa977dd9e857a330a4

- The tempest module tempest.common.fixed_network which provided utilities for finding fixed networks by and helpers for picking the network to use when multiple tenant networks are available has been migrated into tempest lib at tempest.lib.common.fixed_network.

.. releasenotes/notes/plugin-client-registration-enhancements-e09131742391225b.yaml @ 2d7b40a45376186c5abc7b64a388ab9cfae8f2c3

- When registering service clients from installed plugins, all registrations
  are now processed, even if one or more fails. All exceptions encountered
  during the registration process are recorded.  If at least one exception
  was encountered, the registration process fails and all interim errors are
  reported.

.. releasenotes/notes/plugin-client-registration-enhancements-e09131742391225b.yaml @ 2d7b40a45376186c5abc7b64a388ab9cfae8f2c3

- The __repr__ method is now implemented for the base `tempest.Exception`
  class, its implementation is identical to __str__: it reports the error
  message merged with input parameters.

.. releasenotes/notes/tempest-identity-catalog-client-f5c8589a9d7c1eb5.yaml @ d02951667de88008a4cdd215255f5b49df800f15

- Add a new identity catalog client. At this point, the new client contains a single functionality, "show_catalog", which returns a catalog object.


.. _tempest_17.0.0_Upgrade Notes:

Upgrade Notes
-------------

.. releasenotes/notes/raise-exception-when-error-deleting-on-volume-18d0d0c5886212dd.yaml @ 4723fde77b6a3d001586eea2e2528fb44b53fac6

- Tempest checks a volume delete by waiting for NotFound(404) on
  show_volume(). Sometime a volume delete fails and the volume status
  becomes error_deleting which means the delete is failed.
  So Tempest doesn't need to wait anymore. A new release of Tempest
  raises an exception DeleteErrorException instead of waiting.


.. _tempest_17.0.0_Deprecation Notes:

Deprecation Notes
-----------------

.. releasenotes/notes/remove-support-of-py34-7d59fdb431fefe24.yaml @ 27127378b63ea706c457544200fff3a6abed98ed

- Remove the support of python3.4, because in Ubuntu Xenial only
  python3.5 is available (python3.4 is restricted to <= Mitaka).


.. _tempest_17.0.0_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/add-ip-version-check-in-addresses-x491ac6d9abaxa12.yaml @ 816358471f328f1ddffab58ad915b0c91428c54a

- Add more accurate ip version check in addresses schema which will limit the ip version value in [4, 6].

.. releasenotes/notes/add-return-value-to-retype-volume-a401aa619aaa2457.yaml @ 15429d8c0f1dfe0ef312ee030aa5a79cfb8021a3

- Add a missing return statement to the retype_volume API in the v2
  volumes_client library: Bug#1703997
  
  This changes the response body from None to an empty dictionary.

.. releasenotes/notes/fix-remoteclient-default-ssh-shell-prologue-33e99343d086f601.yaml @ d8152de0da08e1654e6d25deee408f45d8a8f2bd

- Fix RemoteClient default ssh_shell_prologue: Bug#1707478
  
  The default ssh_shell_proloque has been modified from
  specifying erroneous PATH=$$PATH:/sbin to PATH=$PATH:/sbin.


.. _tempest_17.0.0_Other Notes:

Other Notes
-----------

.. releasenotes/notes/start-of-pike-support-f2a1b7ea8e8b0311.yaml @ 35976ed20697cd4e4077c8f2279f02ec01a7c6d7

- OpenStack Releases supported after this release are **Pike**, **Ocata**, and **Newton**.
  The release under current development of this tag is Queens, meaning that every Tempest commit is also tested against master during the Queens cycle. However, this does not necessarily mean that using Tempest as of this tag will work against a Queens (or future release) cloud.


.. _tempest_16.1.0:

16.1.0
======

.. _tempest_16.1.0_Prelude:

Prelude
-------

.. releasenotes/notes/intermediate-pike-release-2ce492432ff8f012.yaml @ 87226e30a41498ad74bce9ee012b8570562d7601

This is an intermediate release during the Pike development cycle to make new functionality available to plugins and other consumers.


.. _tempest_16.1.0_New Features:

New Features
------------

.. releasenotes/notes/add-OAUTH-Token-Client-tempest-tests-6351eda451b95a86.yaml @ d9594f5119ab558ecfa316c3abe64e2d5716c434

- Add a new client to handle the OAUTH token feature from the identity API.

.. releasenotes/notes/add-compute-feature-serial-console-45583c4341e34fc9.yaml @ 69d58b8f34f75b0d718d18ea8f303e764720799e

- A new boolean config option ``serial_console`` is added to the section
  ``compute-feature-enabled``. If enabled, tests, which validate the
  behavior of Nova's *serial console* feature (an alternative to VNC,
  RDP, SPICE) can be executed.

.. releasenotes/notes/add-domain-configuration-client-tempest-tests-e383efabdbb9ad03.yaml @ 94d85773650c805d329486b152f72d116c8811c9

- Add a new client to handle the domain configuration feature from the
  identity v3 API.

.. releasenotes/notes/add-floating-ip-config-option-e5774bf77702ce9f.yaml @ 3312de38c9903cd86ab3922ef3a153cc7701e0bf

- A new config option in the network-feature-enabled section, floating_ips, to specify whether floating ips are available in the cloud under test. By default this is set to True.

.. releasenotes/notes/add-force-detach-volume-to-volumes-client-library-b2071f2954f8e8b1.yaml @ 7b0eaf8f544cfbaab521a80abfff33e7b637b90d

- Add force detach volume feature API to v2 volumes_client library.
  This feature enables the possibility to force a volume to detach, and
  roll back an unsuccessful detach operation after you disconnect the volume.

.. releasenotes/notes/add-identity-v3-clients-for-os-ep-filter-api-endpoint-groups-3518a90bbb731d0f.yaml @ d0ed8b00d089c37e518bcdf77420c4b5278b05f9

- Defines the identity v3 OS-EP-FILTER EndPoint Groups API client.
  This client manages Create, Get, Update, Check, List, and Delete
  of EndPoint Group.

.. releasenotes/notes/add-identity-v3-clients-for-os-ep-filter-api-extensions-9cfd217fd2c6a61f.yaml @ 5d52d3af8a37782aa3bc0f47e9c3c68276c27545

- Defines the identity v3 OS-EP-FILTER extension API client.
  This client manages associations between endpoints, projects
  along with groups.

.. releasenotes/notes/add-kwargs-to-delete-vol-of-vol-client-1ecde75beb62933c.yaml @ cb5f650fd4d132f2a34b4a27d388536c8e8dbd98

- The ``delete_volume`` method of the ``VolumesClient`` class
  now has an additional ``**params`` argument that enables passing
  additional information in the query string of the HTTP request.

.. releasenotes/notes/add-list-volume-transfers-with-detail-to-transfers-client-80169bf78cf4fa66.yaml @ c2618d9ce96ab425941b0a981525bb6e1ec3238c

- Add list volume transfers with details API to v2 transfers_client library.
  This feature enables the possibility to list volume transfers with details.

.. releasenotes/notes/add-manage-snapshot-ref-config-option-67efd04897335b67.yaml @ ebc752b59dd3e2164807930e31b313a92bce70d5

- A new config option 'manage_snapshot_ref' is added in the volume section,
  to specify snapshot ref parameter for different storage backend drivers
  when managing an existing snapshot. By default it is set to fit the LVM
  driver.

.. releasenotes/notes/add-params-to-identity-v3-list-endpoints-958a155be4e17e5b.yaml @ 63444d61a7ed4906b9bdf4952f1e40e68de18972

- The ``list_endpoints`` method of the v3 ``EndPointsClient`` class now has
  an additional ``**params`` argument that enables passing additional
  information in the query string of the HTTP request.

.. releasenotes/notes/add-save-state-option-5ea67858cbaca969.yaml @ 7ba22721e544d4f02172ffa59cc7ebc7a27c1ddf

- Add ``--save-state`` option to allow saving state of cloud before
  tempest run.

.. releasenotes/notes/add-server-diagnostics-validation-schema-b5a3c55b45aa718a.yaml @ 0cb4f2255c8331e091a9143b65d73927ade6e757

- Add validation schema for Nova server diagnostics API

.. releasenotes/notes/add-show-host-to-hosts-client-library-c60c4eb49d139480.yaml @ 44c2e0f24a2a7e781c711fbefdd177a004f9c029

- Add show host API to the volume v2 hosts_client library.
  This feature enables the possibility to show details for a host.

.. releasenotes/notes/add-show-snapshot-metadata-item-api-to-v2-snapshots-client-bd3cbab3c7f0e0b3.yaml @ 69719076552bed89c2b15fc00153314d3b363601

- Add show snapshot metadata item API to v2 snapshots_client library.
  This feature enables the possibility to show a snapshot's metadata for
  a specific key.

.. releasenotes/notes/add-show-volume-metadata-item-api-to-v2-volumes-client-47d59ecd999ca9df.yaml @ b40cb198ce9ed879a8fb2708ef9502df080a2db2

- Add show volume metadata item API to v2 volumes_client library.
  This feature enables the possibility to show a volume's metadata for
  a specific key.

.. releasenotes/notes/add-show-volume-summary-api-to-v3-volumes-client-96e7b01abdb5c9c3.yaml @ 79a1cbf2ddde03a07dd290913cc45934be691214

- Define v3 volumes_client for the volume service as a library interface,
  allowing other projects to use this module as a stable library without
  maintenance changes.
  Add show volume summary API to v3 volumes_client library, min_microversion
  of this API is 3.12.
  
  * volumes_client(v3)

.. releasenotes/notes/add-update-backup-api-to-v3-backups-client-e8465b2b66617dc0.yaml @ f4ce417b8b87e68f14e81b5a01f2068a7172027c

- Define v3 backups_client for the volume service as a library interface,
  allowing other projects to use this module as a stable library without
  maintenance changes.
  Add update backup API to v3 backups_client library, min_microversion
  of this API is 3.9.
  
  * backups_client(v3)

.. releasenotes/notes/add-volume-groups-tempest-tests-dd7b2abfe2b48427.yaml @ 0ddf83ead7869bcb42394a78d69240b507f0aa81

- Add groups and group_types clients for the volume service as library.
  Add tempest tests for create group, delete group, show group, and
  list group volume APIs.

.. releasenotes/notes/add-volume-quota-class-client-as-library-c4c2b22c36ff807e.yaml @ 644b01dafe3f03ba7b30515d4c6b8e8918e4358d

- Define v2 quota_classes_client for the volume service as library
  interfaces, allowing other projects to use this module as stable libraries
  without maintenance changes.
  
  * quota_classes_client(v2)

.. releasenotes/notes/api_v2_admin_flag-dea5ca9bc2ce63bc.yaml @ 1413ba9c0686956463d0f4e61c44927fba45541f

- A new configuration flag api_v2_admin is introduced in the identity
  feature flag group to allow for enabling/disabling all identity v2
  admin tests. The new flag only applies when the existing api_v2 flag
  is set to True

.. releasenotes/notes/identity-token-client-8aaef74b1d61090a.yaml @ 1c796287606776c609ef900061df96f695df5699

- Add additional API endpoints to the identity v2 client token API:
  -  list_endpoints_for_token
  -  check_token_existence

.. releasenotes/notes/move-attr-decorator-to-lib-a1e80c42ba9c5392.yaml @ 3b46d27c90aa6289724f4c137a0838c89d116b62

- A new ``attr`` decorator has been added in the ``tempest.lib.decorators``
  module. For example, use it to tag specific tests, which could be leveraged
  by test runners to run only a subset of Tempest tests.

.. releasenotes/notes/move-related_bug-decorator-to-lib-dbfd5c543bbb2805.yaml @ c5665a6cc75b5140227942dfe7ec994f021d8ba5

- A new ``related_bug`` decorator has been added to
  ``tempest.lib.decorators``. Use it to decorate and tag a test that was
  added in relation to a launchpad bug report.

.. releasenotes/notes/move-volume-v3-base_client-to-volume-1edbz0f207c3b283.yaml @ 027365220604ec2bafaf043e144dda874a2d04de

- Move base_client from tempest.lib.services.volume.v3 to
  tempest.lib.services.volume, so if we want to add new
  interfaces based on a v2 client, we can make that v2
  client inherit from volume.base_client.BaseClient to
  get microversion support, and then to make the new v3
  client inherit from the v2 client, thus to avoid the
  multiple inheritance.

.. releasenotes/notes/network-tag-client-f4614029af7927f0.yaml @ 1177942f0eb4724a3585b77bbcb6e2b9b27b0a40

- Define v2.0 ``tags_client`` for the network service as a library
  interface, allowing other projects to use this module as a stable
  library without maintenance changes.
  
  * tags_client(v2.0)

.. releasenotes/notes/pause_teardown-45c9d60ffa889f7f.yaml @ ae155b70952a196751bb9c83af818810cc7288ab

- Pause teardown
  When pause_teardown flag in tempest.conf is set to True a pdb breakpoint
  is added to tearDown and tearDownClass methods in test.py.
  This allows to pause cleaning resources process, so that used resources
  can be examined. Closer examination of used resources may lead to faster
  debugging.

.. releasenotes/notes/tempest-workspace-delete-directory-feature-74d6d157a5a05561.yaml @ 7ba22721e544d4f02172ffa59cc7ebc7a27c1ddf

- Added tempest workspace remove ``--name <workspace_name> --rmdir``
  feature to delete the workspace directory as well as entry.


.. _tempest_16.1.0_Upgrade Notes:

Upgrade Notes
-------------

.. releasenotes/notes/deprecate-compute-images-client-in-volume-tests-92b6dd55fcaba620.yaml @ 59fdd2a210c6ceb0fb857dc725ac0329c61f0e59

- Switch to use Glance v2 APIs in volume tests, by adding the Glance v2
  client images_client.

.. releasenotes/notes/remove-heat-tests-9efb42cac3e0b306.yaml @ 909891d61318cdf9d6b98f0d5e15b60ffadebfb3

- The Heat API tests have been removed from tempest, they were unmaintained. The future direction of api test for heat is their in-tree Gabbi tests

.. releasenotes/notes/set-cinder-api-v3-option-true-1b3e61e3129b7c00.yaml @ 0f107bcdbe56ce4b1bf7df5deb12e739d4e6f967

- The volume config option 'api_v3' default is changed to
  ``True`` because the volume v3 API is CURRENT.

.. releasenotes/notes/use-cinder-v3-client-for-verify_tempest_config-2bf3d817b0070064.yaml @ 8b876dd4535b2fc6a53038c9f331e552504a1073

- verify_tempest_config command starts using extension_client of cinder v2 API only, because cinder v3 API is current and v2 and v1 are deprecated and v3 extension API is the same as v2. Then we can reuse the v2 client for v3 API also.


.. _tempest_16.1.0_Deprecation Notes:

Deprecation Notes
-----------------

.. releasenotes/notes/deprecate-compute-images-client-in-volume-tests-92b6dd55fcaba620.yaml @ 59fdd2a210c6ceb0fb857dc725ac0329c61f0e59

- Image APIs in compute are deprecated, Image native APIs are recommended.
  And Glance v1 APIs are deprecated and v2 APIs are current. Image client
  compute_images_client and Glance v1 APIs are removed in volume tests.

.. releasenotes/notes/deprecate-config-forbid_global_implied_dsr-e64cfa66e6e3ded5.yaml @ bd391dc5d93efb443ec2448796077cf819144c3a

- The config option ``forbid_global_implied_dsr`` from the ``IdentityFeature`` group is now deprecated. This feature flag was introduced to support testing of old OpenStack versions which are not supported anymore.

.. releasenotes/notes/deprecate-default-value-for-v3_endpoint_type-fb9e47c5ba1c719d.yaml @ b4c0c822821ad38456d2132119055829452ed39f

- Deprecate default value for configuration parameter v3_endpoint_type
  of identity section in OpenStack Pike and modify the default value to
  publicURL in OpenStack Q release.

.. releasenotes/notes/move-volume-v3-base_client-to-volume-1edbz0f207c3b283.yaml @ 027365220604ec2bafaf043e144dda874a2d04de

- Deprecate class BaseClient from volume.v3.base_client
  and move it to volume.base_client.
  ``tempest.lib.services.volume.v3.base_client.BaseClient``
  (new ``tempest.lib.services.volume.base_client.BaseClient``)


.. _tempest_16.1.0_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/prevent-error-in-parse-resp-when-nullable-list-9898cd0f22180986.yaml @ 69a8edc1ac7eb9260094f972fe1677205c9a8f0e

- When receiving nullable list as a response body, tempest.lib
  rest_client module raised an exception without valid json
  deserialization. A new release fixes this bug.


.. _tempest_16.0.0:

16.0.0
======

.. _tempest_16.0.0_Prelude:

Prelude
-------

.. releasenotes/notes/16/16.0.0-mitaka-eol-88ff8355fff81b55.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

This release indicates end of support for Mitaka in Tempest.


.. _tempest_16.0.0_New Features:

New Features
------------

.. releasenotes/notes/16/16.0.0-add-OAUTH-Consumer-Client-tempest-tests-db1df7aae4a9fd4e.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Add a new client to handle the OAUTH consumers feature from the identity API.

.. releasenotes/notes/16/16.0.0-add-additional-methods-to-roles-client-library-178d4a6000dec72d.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Add missing API call, list all role inference rules,
  to the roles_client library. This feature enables the
  possibility of listing all role inference rules in the
  system.

.. releasenotes/notes/16/16.0.0-add-cascade-parameter-to-volumes-client-ff4f7f12795003a4.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Add cascade parameter to volumes_client.
  This option provides the ability to delete a volume and have Cinder
  handle deletion of snapshots associated with that volume by passing
  an additional argument to volume delete, "cascade=True".

.. releasenotes/notes/16/16.0.0-add-compute-server-evaculate-client-as-a-library-ed76baf25f02c3ca.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Define the compute server evacuate client method in the servers_client library.

.. releasenotes/notes/16/16.0.0-add-list-auth-project-client-5905076d914a3943.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Add the list auth projects API to the identity client library. This feature
  enables the possibility to list projects that are available to be scoped
  to based on the X-Auth-Token provided in the request.

.. releasenotes/notes/16/16.0.0-add-list-glance-api-versions-ec5fc8081fc8a0ae.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Add versions_client module for image service.
  This new module provides list_versions() method which shows API versions
  from Image service.

.. releasenotes/notes/16/16.0.0-add-list-security-groups-by-servers-to-servers-client-library-088df48f6d81f4be.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Add the list security groups by server API to the servers_client
  library. This feature enables the possibility to list security
  groups for a server instance.

.. releasenotes/notes/16/16.0.0-add-list-version-to-identity-client-944cb7396088a575.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Add versions_client module for identity service.
  This new module provides list_versions() method which shows API versions
  from Identity service.

.. releasenotes/notes/16/16.0.0-add-list-version-to-volume-client-4769dd1bd4ab9c5e.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Add versions_client module for volume service.
  This new module provides list_versions() method which shows API versions
  from Volume service.

.. releasenotes/notes/16/16.0.0-add-quota-sets-detail-kwarg-74b72183295b3ce7.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Interface show_quota_set of compute quotas_client has been extended to include the
  argument "detail", which allows for detailed quota set information for a project to be
  retrieved, if set to True.

.. releasenotes/notes/16/16.0.0-add-tempest-lib-remote-client-adbeb3f42a36910b.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Add remote_client under tempest.lib.
  This remote_client under tempest.lib is defined as stable
  interface, and now this module provides the following
  essential methods.
  
  - exec_command
  - validate_authentication
  - ping_host

.. releasenotes/notes/16/16.0.0-add-tempest-run-combine-option-e94c1049ba8985d5.yaml @ 7ba22721e544d4f02172ffa59cc7ebc7a27c1ddf

- Adds a new cli option to tempest run, ``--combine``, which is used
  to indicate you want the subunit stream output combined with the
  previous run's in the testr repository

.. releasenotes/notes/16/16.0.0-add-update-encryption-type-to-encryption-types-client-f3093532a0bcf9a1.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Add update encryption type API to the v2 encryption_types_client library.
  This feature enables the possibility to update an encryption type for an
  existing volume type.

.. releasenotes/notes/16/16.0.0-add-volume-manage-client-as-library-78ab198a1dc1bd41.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Add the unmanage volume API service method in v2 volumes_client library.
  Define v2 volume_manage_client client for the volume service as library
  interfaces, allowing other projects to use this module as stable libraries
  without maintenance changes.
  
  * volume_manage_client(v2)

.. releasenotes/notes/16/16.0.0-create-server-tags-client-8c0042a77e859af6.yaml @ 1382e971fbb3506ecec7c8549cb8ecac7e1c43e1

- Add server tags APIs to the servers_client library.
  This feature enables the possibility of updating, deleting
  and checking existence of a tag on a server, as well
  as updating and deleting all tags on a server.

.. releasenotes/notes/16/16.0.0-volume-transfers-client-e5ed3f5464c0cdc0.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Define volume transfers service clients as libraries.
  The following volume transfers service clients are defined as library interface.
  
  * transfers_client(v2)


.. _tempest_16.0.0_Upgrade Notes:

Upgrade Notes
-------------

.. releasenotes/notes/16/16.0.0-add-content-type-without-spaces-b2c9b91b257814f3.yaml @ 7ba22721e544d4f02172ffa59cc7ebc7a27c1ddf

- The ``JSON_ENC`` and ``TXT_ENC`` option in the ``_error_checker`` section have been added with additional content-type which are defined in RFC7231 but missing in the current rest_client.py file. The lack of these additional content-type will cause defcore test to fail for OpenStack public cloud which uses tomcat module in the api gateway. The additions are ``application/json;charset=utf-8``, ``text/html;charset=utf-8``, ``text/plain;charset=utf-8``

.. releasenotes/notes/16/16.0.0-deprecate-resources-prefix-option-ad490c0a30a0266b.yaml @ 1382e971fbb3506ecec7c8549cb8ecac7e1c43e1

- The default value of rand_name()'s prefix argument is changed to 'tempest' from None to identify resources are created by Tempest.

.. releasenotes/notes/16/16.0.0-deprecated-cinder-api-v1-option-df7d5a54d93db5cf.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- The volume config option 'api_v1' default is changed to
  ``False`` because the volume v1 API has been deprecated
  since Juno release.

.. releasenotes/notes/16/16.0.0-remove-call_until_true-of-test-de9c13bc8f969921.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- The *call_until_true* of *test* module is removed because it was marked as deprecated and Tempest provides it from *test_utils* as a stable interface instead. Please switch to use *test_utils.call_until_true* if necessary.

.. releasenotes/notes/16/16.0.0-remove-cinder-v1-api-tests-71e266b8d55d475f.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Remove Cinder v1 API tests. Cinder v1 API has been deprecated since Juno release, and Juno is not supported by current Tempest. Then Cinder v1 API tests are removed from Tempest.

.. releasenotes/notes/16/16.0.0-remove-deprecated-allow_port_security_disabled-option-d0ffaeb2e7817707.yaml @ 7ba22721e544d4f02172ffa59cc7ebc7a27c1ddf

- The deprecated config option ``allow_port_security_disabled`` from
  ``compute_feature_enabled`` group has been removed.

.. releasenotes/notes/16/16.0.0-remove-deprecated-compute-validation-config-options-part-2-5cd17b6e0e6cb8a3.yaml @ 7ba22721e544d4f02172ffa59cc7ebc7a27c1ddf

- Below deprecated config options from compute group have been removed.
  Corresponding config options already been available in validation group.
  
  - ``compute.image_ssh_user`` (available as ``validation.image_ssh_user``)
  - ``compute.ssh_user`` (available as ``validation.image_ssh_user``)
  - ``scenario.ssh_user`` (available as ``validation.image_ssh_user``)
  - ``compute.network_for_ssh`` (available as ``validation.network_for_ssh``)
  - ``compute.ping_timeout`` (available as ``validation.ping_timeout``)

.. releasenotes/notes/16/16.0.0-remove-deprecated-dvr_extra_resources-option-e8c441c38eab7ddd.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- The deprecated config option 'dvr_extra_resources' from network group has been removed.
  This option was for extra resources which were provisioned to bind a router to Neutron
  L3 agent. The extra resources need to be provisioned in Liberty release or older,
  and are not required since Mitaka release. Current Tempest doesn't support Liberty, so
  this option has been removed from Tempest.

.. releasenotes/notes/16/16.0.0-remove-deprecated-identity-reseller-option-4411c7e3951f1094.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- The deprecated config option 'reseller' from identity_feature_enabled group has been removed.

.. releasenotes/notes/16/16.0.0-remove-volume_feature_enabled.volume_services-c6aa142cc1021297.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- The deprecated ``volume_services`` option in the ``volume_feature_enabled``
  section has now been removed.

.. releasenotes/notes/16/16.0.0-use-keystone-v3-api-935860d30ddbb8e9.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Tempest now defaults to using Keystone v3 API for the authentication, because Keystone v3 API is CURRENT and the v2 API is deprecated.


.. _tempest_16.0.0_Deprecation Notes:

Deprecation Notes
-----------------

.. releasenotes/notes/16/16.0.0-deprecate-deactivate_image-config-7a282c471937bbcb.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- The ``deactivate_image`` configuration switch from the ``config`` module
  is deprecated. It was added to support the older-than-kilo releases
  which we don't support anymore.

.. releasenotes/notes/16/16.0.0-deprecate-dvr_extra_resources-config-8c319d6dab7f7e5c.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- The ``dvr_extra_resources`` configuration switch from the ``config`` module
  is deprecated. It was added to support the Liberty Release which we don't
  support anymore.

.. releasenotes/notes/16/16.0.0-deprecate-glance-api-version-config-options-8370b63aea8e14cf.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Glance v1 APIs are deprecated and v2 are current.
  Tempest should tests only v2 APIs.
  Below API version selection config options
  for glance have been deprecated and will be removed in future.
  
  * CONF.image_feature_enabled.api_v2
  * CONF.image_feature_enabled.api_v1

.. releasenotes/notes/16/16.0.0-deprecate-resources-prefix-option-ad490c0a30a0266b.yaml @ 1382e971fbb3506ecec7c8549cb8ecac7e1c43e1

- The resources_prefix is marked as deprecated because it is enough to set 'tempest' as the prefix on rand_name() to identify resources which are created by Tempest and no projects set this option on OpenStack dev community.

.. releasenotes/notes/16/16.0.0-deprecate-skip_unless_attr-decorator-450a1ed727494724.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- The ``skip_unless_attr`` decorator in lib/decorators.py has been deprecated, please use the standard ``testtools.skipUnless`` and ``testtools.skipIf`` decorators.

.. releasenotes/notes/16/16.0.0-deprecate-skip_unless_config-decorator-64c32d588043ab12.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- The ``skip_unless_config`` and ``skip_if_config`` decorators in the ``config`` module have been deprecated and will be removed in the Queens dev cycle. Use the ``testtools.skipUnless`` (or a variation of) instead.

.. releasenotes/notes/16/16.0.0-deprecated-cinder-api-v1-option-df7d5a54d93db5cf.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Volume v1 API is deprecated and the v3 are CURRENT.
  Tempest doesn't need to test the v1 API as the default.
  The volume config option 'api_v1' has been marked as
  deprecated.

.. releasenotes/notes/16/16.0.0-dreprecate_client_parameters-cb8d069e62957f7e.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Deprecate the client_parameters argument in
  `tempest.lib.services.clients.ServiceClients`. The parameter is actually
  not honoured already - see https://bugs.launchpad.net/tempest/+bug/1680915

.. releasenotes/notes/16/16.0.0-volume-transfers-client-e5ed3f5464c0cdc0.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Deprecate volume v2 transfers resource methods from volumes_client(v2) libraries.
  Same methods are available in new transfers service client: transfers_client(v2)
  The following methods of volume v2 volumes_clients have been deprecated:
  
  * create_volume_transfer (v2.volumes_client)
  * show_volume_transfer (v2.volumes_client)
  * list_volume_transfers (v2.volumes_client)
  * delete_volume_transfer (v2.volumes_client)
  * accept_volume_transfer (v2.volumes_client)


.. _tempest_16.0.0_Bug Fixes:

Bug Fixes
---------

.. releasenotes/notes/16/16.0.0-fix-volume-v2-service-clients-bugfix-1667354-73d2c3c8fedc08bf.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Fix below volume v2 service clients to make v2 API call: Bug#1667354
  
  - SchedulerStatsClient
  - CapabilitiesClient

.. releasenotes/notes/16/16.0.0-remove-sahara-service-available-44a642aa9c634ab4.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- The 'sahara' config option in the 'service-available' group has been moved to the sahara plugin
  (openstack/sahara-tests) along with tests and service client during the Ocata timeframe.
  A 'sahara' config option was left over on Tempest side, and it's removed now.
  As long as the sahara plugin is installed, this change as no impact on users of sahara tests.


.. _tempest_16.0.0_Other Notes:

Other Notes
-----------

.. releasenotes/notes/16/16.0.0-mitaka-eol-88ff8355fff81b55.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- OpenStack Releases Supported after this release are **Newton**
  and **Ocata**
  
  The release under current development as of this tag is Pike,
  meaning that every Tempest commit is also tested against master branch
  during the Pike cycle. However, this does not necessarily mean that
  using Tempest as of this tag will work against Pike (or future
  releases) cloud.


.. _tempest_15.0.0:

15.0.0
======

.. _tempest_15.0.0_Prelude:

Prelude
-------

.. releasenotes/notes/15/15.0.0-remove-deprecated-compute-validation-config-options-e3d1b89ce074d71c.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

This release is marking the start of Ocata release support in Tempest


.. _tempest_15.0.0_New Features:

New Features
------------

.. releasenotes/notes/15/15.0.0-add-image-clients-tests-49dbc0a0a4281a77.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- As in the [doc]:
  http://developer.openstack.org/api-ref/image/v2/metadefs-index.html,
  there are some apis are not included, add them.
  
    * namespace_objects_client(v2)
    * namespace_tags_client(v2)

.. releasenotes/notes/15/15.0.0-add-implied-roles-to-roles-client-library-edf96408ad9ba82e.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Add the implied roles feature API to the roles_client library. This
  feature enables the possibility to create inferences rules between
  roles (a role being implied by another role).

.. releasenotes/notes/15/15.0.0-add-snapshot-manage-client-as-library-a76ffdba9d8d01cb.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Define v2 snapshot_manage_client client for the volume service as
  library interfaces, allowing other projects to use this module as
  stable libraries without maintenance changes.
  
  * snapshot_manage_client(v2)

.. releasenotes/notes/15/15.0.0-jsonschema-validator-2377ba131e12d3c7.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Added customized JSON schema format checker for 'date-time' format. Compute response schema will be validated against customized format checker.


.. _tempest_15.0.0_Upgrade Notes:

Upgrade Notes
-------------

.. releasenotes/notes/15/15.0.0-deprecate-allow_port_security_disabled-option-2d3d87f6bd11d03a.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- The default value for the ``allow_port_security_disabled`` option in the ``compute-feature-enabled`` section has been changed from ``False`` to ``True``.

.. releasenotes/notes/15/15.0.0-deprecate-identity-feature-enabled.reseller-84800a8232fe217f.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- The default value for the ``reseller`` option in the ``identity-feature-enabled`` section has been changed from ``False`` to ``True``.

.. releasenotes/notes/15/15.0.0-deprecate-volume_feature_enabled.volume_services-dbe024ea067d5ab2.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- The default value for the ``volume_services`` option in the ``volume_feature_enabled`` section has been changed from ``False`` to ``True``.

.. releasenotes/notes/15/15.0.0-remove-deprecated-compute-microversion-config-options-eaee6a7d2f8390a8.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- The deprecated compute microversion config options from 'compute-feature-enabled' group have been removed. Those config options are available under 'compute' group to configure the min and max microversion for compute service.
  * CONF.compute.min_microversion * CONF.compute.max_microversion

.. releasenotes/notes/15/15.0.0-remove-deprecated-compute-validation-config-options-e3d1b89ce074d71c.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Below deprecated config options from compute group have been removed.
  Corresponding config options already been available in validation group.
  
  - ``compute.use_floatingip_for_ssh`` (available as ``validation.connect_method``)
  - ``compute.ssh_auth_method`` (available as ``validation.auth_method``)
  - ``compute.image_ssh_password`` (available as ``validation.image_ssh_password``)
  - ``compute.ssh_shell_prologue`` (available as ``validation.ssh_shell_prologue``)
  - ``compute.ping_size `` (available as ``validation.ping_size``)
  - ``compute.ping_count `` (available as ``validation.ping_count``)
  - ``compute.floating_ip_range `` (available as ``validation.floating_ip_range``)

.. releasenotes/notes/15/15.0.0-remove-deprecated-input-scenario-config-options-414e0c5442e967e9.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- The deprecated input-scenario config options and group have been removed. The input scenarios functionality already being removed from tempest and from this release, their corresponding config options too.

.. releasenotes/notes/15/15.0.0-remove-deprecated-network-config-options-f9ce276231578fe6.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Below deprecated network config options have been removed.
  Those config options already been renamed to below meaningful names.
  
  - ``tenant_network_cidr`` (removed) -> ``project_network_cidr``
  - ``tenant_network_mask_bits`` (removed) -> ``project_network_mask_bits``
  - ``tenant_network_v6_cidr`` (removed) -> ``project_network_v6_cidr``
  - ``tenant_network_v6_mask_bits`` (removed) -> ``project_network_v6_mask_bits``
  - ``tenant_networks_reachable`` (removed) -> ``project_networks_reachable``


.. _tempest_15.0.0_Deprecation Notes:

Deprecation Notes
-----------------

.. releasenotes/notes/15/15.0.0-deprecate-allow_port_security_disabled-option-2d3d87f6bd11d03a.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- The ``allow_port_security_disabled`` option in the ``compute-feature-enabled`` section is now deprecated.

.. releasenotes/notes/15/15.0.0-deprecate-identity-feature-enabled.reseller-84800a8232fe217f.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- The ``reseller`` option in the ``identity-feature-enabled`` section is now deprecated.

.. releasenotes/notes/15/15.0.0-deprecate-volume_feature_enabled.volume_services-dbe024ea067d5ab2.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- The ``volume_services`` option in the ``volume_feature_enabled`` section is now deprecated.


.. _tempest_15.0.0_Other Notes:

Other Notes
-----------

.. releasenotes/notes/15/15.0.0-remove-deprecated-compute-validation-config-options-e3d1b89ce074d71c.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- OpenStack releases supported at this time are **Mitaka**, **Newton**,
  and **Ocata**.
  
  The release under current development as of this tag is Pike,
  meaning that every Tempest commit is also tested against master during
  the Pike cycle. However, this does not necessarily mean that using
  Tempest as of this tag will work against a Pike (or future releases)
  cloud.


.. _tempest_14.0.0:

14.0.0
======

.. _tempest_14.0.0_Prelude:

Prelude
-------

.. releasenotes/notes/14/14.0.0-remo-stress-tests-81052b211ad95d2e.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

This release is marking the end of Liberty release support in Tempest


.. _tempest_14.0.0_New Features:

New Features
------------

.. releasenotes/notes/14/14.0.0-add-cred-provider-abstract-class-to-lib-70ff513221f8a871.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- The cred_provider abstract class which serves as the basis for both of tempest's cred providers, pre-provisioned credentials and dynamic credentials, is now a library interface. This provides the common signature required for building a credential provider.

.. releasenotes/notes/14/14.0.0-add-cred_client-to-tempest.lib-4d4af33f969c576f.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- The cred_client module was added to tempest.lib. This module provides a wrapper to the keystone services client which provides a uniform interface that abstracts out the differences between keystone api versions.

.. releasenotes/notes/14/14.0.0-add-image-clients-af94564fb34ddca6.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- As in the [doc]:
  http://developer.openstack.org/api-ref/image/v2/metadefs-index.html,
  there are some apis are not included, add them.
  
    * namespace_properties_client(v2)

.. releasenotes/notes/14/14.0.0-add-role-assignments-client-as-a-library-d34b4fdf376984ad.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Define the identity service role_assignments_client as a library. Add role_assignments_client to the library interface so the other projects can use this module as a stable library without any maintenance changes.

.. releasenotes/notes/14/14.0.0-add-service-provider-client-cbba77d424a30dd3.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- A Neutron Service Providers client is added to deal with resources of the '/service-providers' route.

.. releasenotes/notes/14/14.0.0-add-ssh-port-parameter-to-client-6d16c374ac4456c1.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- A new optional parameter `port` for ssh client (`tempest.lib.common.ssh.Client`) to specify destination port for a host. The default value is 22.

.. releasenotes/notes/14/14.0.0-move-cinder-v3-to-lib-service-be3ba0c20753b594.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Define the Volume v3 service clients as library interfaces,
  allowing other projects to use these modules as stable
  libraries without maintenance changes.
  
  * messages_client(v3)

.. releasenotes/notes/14/14.0.0-new-volume-limit-client-517c17d9090f4df4.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- The volume_limits client was added to tempest.lib.

.. releasenotes/notes/14/14.0.0-volume-clients-as-library-309030c7a16e62ab.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Define volume service clients as libraries.
  The following volume service clients are defined as library interface,
  so the other projects can use these modules as stable libraries without
  any maintenance changes.
  
  * volumes_client(v1)
  * volumes_client(v2)
  * capabilities_client(v2)
  * scheduler_stats_client(v2)


.. _tempest_14.0.0_Upgrade Notes:

Upgrade Notes
-------------

.. releasenotes/notes/14/14.0.0-add-error-code-translation-to-versions-clients-acbc78292e24b014.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Add an error translation to list_versions() of versions_client of both compute and network. This can affect users who are expecting that these clients return error status code instead of the exception. It is needed to change the code for handling the exception like the other clients code.

.. releasenotes/notes/14/14.0.0-remo-stress-tests-81052b211ad95d2e.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- The Stress tests framework and all the stress tests have been removed.

.. releasenotes/notes/14/14.0.0-remove-baremetal-tests-65186d9e15d5b8fb.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- All tests for the Ironic project have been removed from Tempest. Those exist as a Tempest plugin in the Ironic project.

.. releasenotes/notes/14/14.0.0-remove-negative-test-generator-1653f4c0f86ccf75.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- The Negative Tests Generator has been removed (it was not used by any Tempest tests).

.. releasenotes/notes/14/14.0.0-remove-sahara-tests-1532c47c7df80e3a.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- All tests for the Sahara project have been removed from Tempest. They now live as a Tempest plugin in the ``openstack/sahara-tests`` repository.


.. _tempest_14.0.0_Deprecation Notes:

Deprecation Notes
-----------------

.. releasenotes/notes/14/14.0.0-deprecate-nova-api-extensions-df16b02485dae203.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- The *api_extensions* config option in the *compute-feature-enabled* group is now deprecated. This option will be removed from tempest when all the OpenStack releases supported by tempest no longer support the API extensions mechanism. This was removed from Nova during the Newton cycle, so this will be removed at the Mitaka EOL.

.. releasenotes/notes/14/14.0.0-remove-bootable-option-024f8944c056a3e0.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- The *bootable* config option in the *volume_feature_enabled* group is removed because the corresponding feature os-set_bootable has been implemented 2.5 years ago and all OpenStack versions which are supported by Tempest should support the feature.


.. _tempest_14.0.0_Other Notes:

Other Notes
-----------

.. releasenotes/notes/14/14.0.0-remo-stress-tests-81052b211ad95d2e.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- OpenStack releases supported at this time are **Mitaka** and **Newton**.
  
  The release under current development as of this tag is Ocata, meaning that
  every Tempest commit is also tested against master during the Ocata cycle.
  However, this does not necessarily mean that using Tempest as of this tag
  will work against a Ocata (or future releases) cloud.


.. _tempest_13.0.0:

13.0.0
======

.. _tempest_13.0.0_Prelude:

Prelude
-------

.. releasenotes/notes/13/13.0.0-start-of-newton-support-3ebb274f300f28eb.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

This release is marking the start of Newton release support in Tempest


.. _tempest_13.0.0_New Features:

New Features
------------

.. releasenotes/notes/13/13.0.0-add-new-identity-clients-as-library-5f7ndha733nwdsn9.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Define identity service clients as libraries.
  Add new service clients to the library interface so the other projects can use these modules as stable libraries without
  any maintenance changes.
  
    * identity_client(v2)
    * groups_client(v3)
    * trusts_client(v3)
    * users_client(v3)
    * identity_client(v3)
    * roles_client(v3)
    * inherited_roles_client(v3)
    * credentials_client(v3)

.. releasenotes/notes/13/13.0.0-add-volume-clients-as-a-library-d05b6bc35e66c6ef.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Define volume service clients as libraries.
  The following volume service clients are defined as library interface,
  so the other projects can use these modules as stable libraries without
  any maintenance changes.
  
  * backups_client
  * encryption_types_client (v1)
  * encryption_types_client (v2)
  * qos_clients (v1)
  * qos_clients (v2)
  * snapshots_client (v1)
  * snapshots_client (v2)

.. releasenotes/notes/13/13.0.0-volume-clients-as-library-660811011be29d1a.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Define the v1 and v2 types_client clients for the volume service as
  library interfaces, allowing other projects to use these modules as
  stable libraries without maintenance changes.


.. _tempest_13.0.0_Upgrade Notes:

Upgrade Notes
-------------

.. releasenotes/notes/13/13.0.0-tempest-cleanup-nostandalone-39df2aafb2545d35.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- the already deprecated tempest-cleanup standalone command has been removed. The corresponding functionalities can be accessed through the unified `tempest` command (`tempest cleanup`).


.. _tempest_13.0.0_Deprecation Notes:

Deprecation Notes
-----------------

.. releasenotes/notes/13/13.0.0-deprecate-get_ipv6_addr_by_EUI64-4673f07677289cf6.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Oslo.utils provides same method get_ipv6_addr_by_EUI64, so deprecate it in Newton and remove it in Ocata.

.. releasenotes/notes/13/13.0.0-move-call-until-true-to-tempest-lib-c9ea70dd6fe9bd15.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- The ``call_until_true`` function is moved from the ``tempest.test`` module to the ``tempest.lib.common.utils.test_utils`` module. Backward compatibility is preserved until Ocata.


.. _tempest_13.0.0_Other Notes:

Other Notes
-----------

.. releasenotes/notes/13/13.0.0-start-of-newton-support-3ebb274f300f28eb.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- OpenStack releases supported at this time are **Liberty**, **Mitaka**,
  and **Newton**.
  
  The release under current development as of this tag is Ocata,
  meaning that every Tempest commit is also tested against master during
  the Ocata cycle. However, this does not necessarily mean that using
  Tempest as of this tag will work against a Ocata (or future releases)
  cloud.


.. _tempest_12.2.0:

12.2.0
======

.. _tempest_12.2.0_New Features:

New Features
------------

.. releasenotes/notes/12/12.2.0-add-httptimeout-in-restclient-ax78061900e3f3d7.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- RestClient now supports setting timeout in urllib3.poolmanager. Clients will use CONF.service_clients.http_timeout for timeout value to wait for http request to response.

.. releasenotes/notes/12/12.2.0-add-httptimeout-in-restclient-ax78061900e3f3d7.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- KeystoneAuthProvider will accept http_timeout and will use it in get_credentials.

.. releasenotes/notes/12/12.2.0-add-new-identity-clients-3c3afd674a395bde.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Define identity service clients as libraries.
  The following identity service clients are defined as library interface,
  so the other projects can use these modules as stable libraries without
  any maintenance changes.
  
   * endpoints_client(v3)
   * policies_client (v3)
   * regions_client(v3)
   * services_client(v3)
   * projects_client(v3)

.. releasenotes/notes/12/12.2.0-clients_module-16f3025f515bf9ec.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- The Tempest plugin interface contains a new optional method, which allows plugins to declare and automatically register any service client defined in the plugin.

.. releasenotes/notes/12/12.2.0-clients_module-16f3025f515bf9ec.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- tempest.lib exposes a new stable interface, the clients module and ServiceClients class, which provides a convenient way for plugin tests to access service clients defined in Tempest as well as service clients defined in all loaded plugins. The new ServiceClients class only exposes for now the service clients which are in tempest.lib, i.e. compute, network and image. The remaining service clients (identity, volume and object-storage) will be added in future updates.

.. releasenotes/notes/12/12.2.0-plugin-service-client-registration-00b19a2dd4935ba0.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- A new optional interface `TempestPlugin.get_service_clients` is available to plugins. It allows them to declare any service client they implement. For now this is used by tempest only, for auto-registration of service clients in the new class `ServiceClients`.

.. releasenotes/notes/12/12.2.0-plugin-service-client-registration-00b19a2dd4935ba0.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- A new singleton class `clients.ClientsRegistry` is available. It holds the service clients registration data from all plugins. It is used by `ServiceClients` for auto-registration of the service clients implemented in plugins.

.. releasenotes/notes/12/12.2.0-service_client_config-8a1d7b4de769c633.yaml @ 1382e971fbb3506ecec7c8549cb8ecac7e1c43e1

- A new helper method `service_client_config` has been added to the stable module config.py that returns extracts from configuration into a dictionary the configuration settings relevant for the initialization of a service client.

.. releasenotes/notes/12/12.2.0-volume-clients-as-library-9a3444dd63c134b3.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Define volume service clients as libraries
  The following volume service clients are defined as library interface,
  so the other projects can use these modules as stable libraries
  without any maintenance changes.
  
    * availability_zone_client(v1)
    * availability_zone_client(v2)
    * extensions_client(v1)
    * extensions_client(v2)
    * hosts_client(v1)
    * hosts_client(v2)
    * quotas_client(v1)
    * quotas_client(v2)
    * services_client(v1)
    * services_client(v2)


.. _tempest_12.2.0_Upgrade Notes:

Upgrade Notes
-------------

.. releasenotes/notes/12/12.2.0-nova_cert_default-90eb7c1e3cde624a.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- The ``nova_cert`` option default is changed to ``False``. The nova certification management APIs were a hold over from ec2, and are not used by any other parts of nova. They are deprecated for removal in nova after the newton release. This makes false a more sensible default going forward.

.. releasenotes/notes/12/12.2.0-remove-javelin-276f62d04f7e4a1d.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- The previously deprecated Javelin utility has been removed from Tempest. As an alternative Ansible can be used to construct similar yaml workflows to what Javelin used to provide.


.. _tempest_12.2.0_Deprecation Notes:

Deprecation Notes
-----------------

.. releasenotes/notes/12/12.2.0-clients_module-16f3025f515bf9ec.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- The new clients module provides a stable alternative to tempest classes manager.Manager and clients.Manager. manager.Manager only exists now to smoothen the transition of plugins to the new interface, but it will be removed shortly without further notice.


.. _tempest_12.1.0:

12.1.0
======

.. _tempest_12.1.0_New Features:

New Features
------------

.. releasenotes/notes/12/12.1.0-add-network-versions-client-d90e8334e1443f5c.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Adds a network version client for querying Neutron's API version discovery URL ("GET /").

.. releasenotes/notes/12/12.1.0-add-scope-to-auth-b5a82493ea89f41e.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Tempest library auth interface now supports scope. Scope allows to control the scope of tokens requested via the identity API. Identity V2 supports unscoped and project scoped tokens, but only the latter are implemented. Identity V3 supports unscoped, project and domain scoped token, all three are available.

.. releasenotes/notes/12/12.1.0-add-tempest-run-3d0aaf69c2ca4115.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Adds the tempest run command to the unified tempest CLI. This new command is used for running tempest tests.

.. releasenotes/notes/12/12.1.0-add-tempest-workspaces-228a2ba4690b5589.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Adds tempest workspaces command and WorkspaceManager. This is used to have a centralized repository for managing different tempest configurations.

.. releasenotes/notes/12/12.1.0-add_subunit_describe_calls-5498a37e6cd66c4b.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Adds subunit-describe-calls. A parser for subunit streams to determine what
  REST API calls are made inside of a test and in what order they are called.
  
    * Input can be piped in or a file can be specified
    * Output is shortened for stdout, the output file has more information

.. releasenotes/notes/12/12.1.0-bug-1486834-7ebca15836ae27a9.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Tempest library auth interface now supports
  filtering with catalog name.  Note that filtering by
  name is only successful if a known service type is
  provided.

.. releasenotes/notes/12/12.1.0-identity-clients-as-library-e663c6132fcac6c2.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Define identity service clients as libraries
  The following identity service clients are defined as library interface,
  so the other projects can use these modules as stable libraries without
  any maintenance changes.
  
    * endpoints_client(v2)
    * roles_client(v2)
    * services_client(v2)
    * tenants_client(v2)
    * users_client(v2)

.. releasenotes/notes/12/12.1.0-image-clients-as-library-86d17caa26ce3961.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Define image service clients as libraries
  The following image service clients are defined as library interface,
  so the other projects can use these modules as stable libraries
  without any maintenance changes.
  
    * image_members_client(v1)
    * images_client(v1)
    * image_members_client(v2)
    * images_client(v2)
    * namespaces_client(v2)
    * resource_types_client(v2)
    * schemas_client(v2)

.. releasenotes/notes/12/12.1.0-new-test-utils-module-adf34468c4d52719.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- A new `test_utils` module has been added to tempest.lib.common.utils. It should hold any common utility functions that help writing Tempest tests.

.. releasenotes/notes/12/12.1.0-new-test-utils-module-adf34468c4d52719.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- A new utility function called `call_and_ignore_notfound_exc` has been added to the `test_utils` module. That function call another function passed as parameter and ignore the NotFound exception if it raised.

.. releasenotes/notes/12/12.1.0-routers-client-as-library-25a363379da351f6.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Define routers_client as stable library interface. The routers_client module is defined as library interface, so the other projects can use the module as stable library without any maintenance changes.

.. releasenotes/notes/12/12.1.0-support-chunked-encoding-d71f53225f68edf3.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- The RestClient (in tempest.lib.common.rest_client) now supports POSTing and PUTing data with chunked transfer encoding. Just pass an `iterable` object as the `body` argument and set the `chunked` argument to `True`.

.. releasenotes/notes/12/12.1.0-support-chunked-encoding-d71f53225f68edf3.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- A new generator called `chunkify` is added in tempest.lib.common.utils.data_utils that yields fixed-size chunks (slices) from a Python sequence.


.. _tempest_12.1.0_Upgrade Notes:

Upgrade Notes
-------------

.. releasenotes/notes/12/12.1.0-remove-input-scenarios-functionality-01308e6d4307f580.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- The input scenarios functionality no longer exists in tempest. This caused a large number of issues for limited benefit and was only used by a single test, test_server_basic_ops. If you were using this functionality you'll now have to do it manually with a script and/or tempest workspaces

.. releasenotes/notes/12/12.1.0-remove-integrated-horizon-bb57551c1e5f5be3.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- The integrated dashboard scenario test has been removed and is now in a separate tempest plugin tempest-horizon. The removed test coverage can be used by installing tempest-horizon on the server where you run tempest.

.. releasenotes/notes/12/12.1.0-remove-legacy-credential-providers-3d653ac3ba1ada2b.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- The deprecated legacy credential provider has been removed. The only way to configure credentials in tempest now is to use the dynamic or preprovisioned credential providers

.. releasenotes/notes/12/12.1.0-remove-trove-tests-666522e9113549f9.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- All tests for the Trove project have been removed from tempest. They now live as a tempest plugin in the trove project.

.. releasenotes/notes/12/12.1.0-tempest-init-global-config-dir-location-changes-12260255871d3a2b.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- The location on disk that the *tempest init* command looks for has changed. Previously it would attempt to use python packaging's data files to guess where setuptools/distutils were installing data files, which was incredibly unreliable and depended on how you installed tempest and which versions of setuptools, distutils, and python you had installed. Instead, now it will use either /etc/tempest, $XDG_CONFIG_PATH/.config/tempest, or ~/.tempest/etc (attempted in that order). If none of these exist it will create an empty ~/.tempest/etc directory. If you were relying on the previous behavior and none of these directories were being used you will need to move the files to live in one of these directories.


.. _tempest_12.1.0_Deprecation Notes:

Deprecation Notes
-----------------

.. releasenotes/notes/12/12.1.0-new-test-utils-module-adf34468c4d52719.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- tempest.lib.common.utils.misc.find_test_caller has been moved into the tempest.lib.common.utils.test_utils module. Calling the find_test_caller function with its old location is deprecated.

.. releasenotes/notes/12/12.1.0-remove-input-scenarios-functionality-01308e6d4307f580.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- All the options in the input-scenario group are now deprecated. These were only used in tree by the now removed input scenarios functionality in test_server_basic_ops. They were only deprecated because there could be external consumers via plugins. They will be removed during the Ocata cycle.


.. _tempest_12.0.0:

12.0.0
======

.. _tempest_12.0.0_Prelude:

Prelude
-------

.. releasenotes/notes/12/12.0.0-supported-openstack-releases-f10aac381d933dd1.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

This release is marking the end of Kilo release support in Tempest


.. _tempest_12.0.0_Other Notes:

Other Notes
-----------

.. releasenotes/notes/12/12.0.0-supported-openstack-releases-f10aac381d933dd1.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- OpenStack Releases Supported after this release are **Liberty** and **Mitaka**
  The release under current development as of this tag is Newton, meaning that every Tempest commit is also tested against master during the Newton cycle. However, this does not necessarily mean that using Tempest as of this tag will work against a Newton (or future releases) cloud.


.. _tempest_11.0.0:

11.0.0
======

.. _tempest_11.0.0_Prelude:

Prelude
-------

.. releasenotes/notes/11/11.0.0-supported-openstack-releases-1e5d7295d939d439.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

This release is marking the start of Mitaka release support in tempest


.. _tempest_11.0.0_New Features:

New Features
------------

.. releasenotes/notes/11/11.0.0-api-microversion-testing-support-2ceddd2255670932.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Tempest library interface addition(API Microversion testing interfaces).

.. releasenotes/notes/11/11.0.0-compute-microversion-support-e0b23f960f894b9b.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Compute Microversion testing support in Service Clients.


.. _tempest_11.0.0_Other Notes:

Other Notes
-----------

.. releasenotes/notes/11/11.0.0-supported-openstack-releases-1e5d7295d939d439.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- OpenStack Releases Supported at this time are **Kilo**, **Liberty**, **Mitaka**
  The release under current development as of this tag is Newton, meaning that every Tempest commit is also tested against master during the Newton cycle. However, this does not necessarily mean that using Tempest as of this tag will work against a Newton (or future releases) cloud.


.. _tempest_10.0.0:

10.0.0
======

.. _tempest_10.0.0_Prelude:

Prelude
-------

.. releasenotes/notes/10/10.0.0-Tempest-library-interface-0eb680b810139a50.yaml @ e98720a22f70079a2b3bc55dce2c7ff214dd1ff5

This release includes the addition of the stable library interface for
tempest. This behaves just as tempest-lib did prior to this, but instead
it lives directly in the tempest project. For more information refer to
the `library docs`_.

.. _library docs: https://docs.openstack.org/tempest/latest/library.html#current-library-apis


.. _tempest_10.0.0_New Features:

New Features
------------

.. releasenotes/notes/10/10.0.0-Tempest-library-interface-0eb680b810139a50.yaml @ e98720a22f70079a2b3bc55dce2c7ff214dd1ff5

- Tempest library interface


.. _tempest_10.0.0_Other Notes:

Other Notes
-----------

.. releasenotes/notes/10/10.0-supported-openstack-releases-b88db468695348f6.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- OpenStack Releases Supported at this time are the same as in the previous release 9, **Kilo** and **Liberty**.
  
  The release under current development as of this tag is Mitaka, meaning that every Tempest commit is also tested against master during the Mitaka cycle. However, this does not necessarily mean that using Tempest as of this tag will work against a Mitaka (or future releases) cloud.

.. releasenotes/notes/10/10.0.0-start-using-reno-ed9518126fd0e1a3.yaml @ 2bbc49212e319292dfabaf17c313bd156de93d3c

- Start using reno for managing release notes.


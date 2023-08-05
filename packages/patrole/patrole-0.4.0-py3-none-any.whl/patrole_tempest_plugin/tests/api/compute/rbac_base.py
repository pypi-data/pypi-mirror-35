# Copyright 2017 AT&T Corporation
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from tempest.api.compute import base as compute_base
from tempest import config
from tempest.lib.common.utils import data_utils
from tempest.lib.common.utils import test_utils

from patrole_tempest_plugin import rbac_utils

CONF = config.CONF


class BaseV2ComputeRbacTest(rbac_utils.RbacUtilsMixin,
                            compute_base.BaseV2ComputeTest):

    @classmethod
    def skip_checks(cls):
        super(BaseV2ComputeRbacTest, cls).skip_checks()
        cls.skip_rbac_checks()

    @classmethod
    def setup_clients(cls):
        super(BaseV2ComputeRbacTest, cls).setup_clients()
        cls.setup_rbac_utils()
        cls.hosts_client = cls.os_primary.hosts_client
        cls.tenant_usages_client = cls.os_primary.tenant_usages_client
        cls.networks_client = cls.os_primary.networks_client
        cls.subnets_client = cls.os_primary.subnets_client
        cls.ports_client = cls.os_primary.ports_client

    @classmethod
    def create_flavor(cls, **kwargs):
        flavor_kwargs = {
            "name": data_utils.rand_name(cls.__name__ + '-flavor'),
            "ram": data_utils.rand_int_id(1, 10),
            "vcpus": data_utils.rand_int_id(1, 10),
            "disk": data_utils.rand_int_id(1, 10),
            "id": data_utils.rand_uuid(),
        }
        if kwargs:
            flavor_kwargs.update(kwargs)
        flavor = cls.flavors_client.create_flavor(**flavor_kwargs)['flavor']
        cls.addClassResourceCleanup(
            cls.flavors_client.wait_for_resource_deletion, flavor['id'])
        cls.addClassResourceCleanup(
            test_utils.call_and_ignore_notfound_exc,
            cls.flavors_client.delete_flavor, flavor['id'])
        return flavor

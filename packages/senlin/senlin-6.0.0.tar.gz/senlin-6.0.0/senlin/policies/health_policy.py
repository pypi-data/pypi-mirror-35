# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from oslo_config import cfg

from senlin.common import constraints
from senlin.common import consts
from senlin.common import exception as exc
from senlin.common.i18n import _
from senlin.common import scaleutils
from senlin.common import schema
from senlin.engine import health_manager
from senlin.policies import base


class HealthPolicy(base.Policy):
    """Policy for health management of a cluster."""

    VERSION = '1.0'
    VERSIONS = {
        '1.0': [
            {'status': consts.EXPERIMENTAL, 'since': '2017.02'},
            {'status': consts.SUPPORTED, 'since': '2018.06'},
        ]
    }
    PRIORITY = 600

    TARGET = [
        ('BEFORE', consts.CLUSTER_RECOVER),
        ('BEFORE', consts.CLUSTER_DEL_NODES),
        ('BEFORE', consts.CLUSTER_SCALE_IN),
        ('BEFORE', consts.CLUSTER_RESIZE),
        ('BEFORE', consts.NODE_DELETE),
        ('AFTER', consts.CLUSTER_DEL_NODES),
        ('AFTER', consts.CLUSTER_SCALE_IN),
        ('AFTER', consts.CLUSTER_RESIZE),
        ('AFTER', consts.NODE_DELETE),
    ]

    # Should be ANY if profile provides health check support?
    PROFILE_TYPE = [
        'os.nova.server',
        'os.heat.stack',
    ]

    KEYS = (DETECTION, RECOVERY) = ('detection', 'recovery')

    _DETECTION_KEYS = (
        DETECTION_TYPE, DETECTION_OPTIONS,
    ) = (
        'type', 'options'
    )

    _DETECTION_OPTIONS = (
        DETECTION_INTERVAL, POLL_URL, POLL_URL_SSL_VERIFY,
        POLL_URL_HEALTHY_RESPONSE, POLL_URL_RETRY_LIMIT,
        POLL_URL_RETRY_INTERVAL, NODE_UPDATE_TIMEOUT,
    ) = (
        'interval', 'poll_url', 'poll_url_ssl_verify',
        'poll_url_healthy_response', 'poll_url_retry_limit',
        'poll_url_retry_interval', 'node_update_timeout',
    )

    _RECOVERY_KEYS = (
        RECOVERY_ACTIONS, RECOVERY_FENCING, RECOVERY_DELETE_TIMEOUT,
        RECOVERY_FORCE_RECREATE,
    ) = (
        'actions', 'fencing', 'node_delete_timeout', 'node_force_recreate',
    )

    FENCING_OPTION_VALUES = (
        COMPUTE,
        # STORAGE, NETWORK,
    ) = (
        'COMPUTE',
        # 'STORAGE', 'NETWORK'
    )

    ACTION_KEYS = (
        ACTION_NAME, ACTION_PARAMS,
    ) = (
        'name', 'params',
    )

    properties_schema = {
        DETECTION: schema.Map(
            _('Policy aspect for node failure detection.'),
            schema={
                DETECTION_TYPE: schema.String(
                    _('Type of node failure detection.'),
                    constraints=[
                        constraints.AllowedValues(consts.DETECTION_TYPES),
                    ],
                    required=True,
                ),
                DETECTION_OPTIONS: schema.Map(
                    schema={
                        DETECTION_INTERVAL: schema.Integer(
                            _("Number of seconds between pollings. Only "
                              "required when type is 'NODE_STATUS_POLLING' or "
                              "'NODE_STATUS_POLL_URL'."),
                            default=60,
                        ),
                        POLL_URL: schema.String(
                            _("URL to poll for node status. See documentation "
                              "for valid expansion parameters. Only required "
                              "when type is 'NODE_STATUS_POLL_URL'."),
                            default='',
                        ),
                        POLL_URL_SSL_VERIFY: schema.Boolean(
                            _("Whether to verify SSL when calling URL to poll "
                              "for node status. Only required when type is "
                              "'NODE_STATUS_POLL_URL'."),
                            default=True,
                        ),
                        POLL_URL_HEALTHY_RESPONSE: schema.String(
                            _("String pattern in the poll URL response body "
                              "that indicates a healthy node. "
                              "Required when type is 'NODE_STATUS_POLL_URL'."),
                            default='',
                        ),
                        POLL_URL_RETRY_LIMIT: schema.Integer(
                            _("Number of times to retry URL polling when its "
                              "return body is missing "
                              "POLL_URL_HEALTHY_RESPONSE string before a node "
                              "is considered down. Required when type is "
                              "'NODE_STATUS_POLL_URL'."),
                            default=3,
                        ),
                        POLL_URL_RETRY_INTERVAL: schema.Integer(
                            _("Number of seconds between URL polling retries "
                              "before a node is considered down. "
                              "Required when type is 'NODE_STATUS_POLL_URL'."),
                            default=3,
                        ),
                        NODE_UPDATE_TIMEOUT: schema.Integer(
                            _("Number of seconds since last node update to "
                              "wait before checking node health. "
                              "Required when type is 'NODE_STATUS_POLL_URL'."),
                            default=300,
                        ),
                    },
                    default={}
                ),
            },
            required=True,
        ),

        RECOVERY: schema.Map(
            _('Policy aspect for node failure recovery.'),
            schema={
                RECOVERY_ACTIONS: schema.List(
                    _('List of actions to try for node recovery.'),
                    schema=schema.Map(
                        _('Action to try for node recovery.'),
                        schema={
                            ACTION_NAME: schema.String(
                                _("Name of action to execute."),
                                constraints=[
                                    constraints.AllowedValues(
                                        consts.RECOVERY_ACTIONS),
                                ],
                                required=True
                            ),
                            ACTION_PARAMS: schema.Map(
                                _("Parameters for the action")
                            ),
                        }
                    )
                ),
                RECOVERY_FENCING: schema.List(
                    _('List of services to be fenced.'),
                    schema=schema.String(
                        _('Service to be fenced.'),
                        constraints=[
                            constraints.AllowedValues(FENCING_OPTION_VALUES),
                        ],
                        required=True,
                    ),
                ),
                RECOVERY_DELETE_TIMEOUT: schema.Integer(
                    _("Number of seconds to wait for node deletion to "
                      "finish and start node creation for recreate "
                      "recovery option. Required when type is "
                      "'NODE_STATUS_POLL_URL and recovery action "
                      "is RECREATE'."),
                    default=20,
                ),
                RECOVERY_FORCE_RECREATE: schema.Boolean(
                    _("Whether to create node even if node deletion "
                      "failed. Required when type is "
                      "'NODE_STATUS_POLL_URL' and action recovery "
                      "action is RECREATE."),
                    default=False,
                ),
            }
        ),
    }

    def __init__(self, name, spec, **kwargs):
        super(HealthPolicy, self).__init__(name, spec, **kwargs)

        self.check_type = self.properties[self.DETECTION][self.DETECTION_TYPE]

        options = self.properties[self.DETECTION][self.DETECTION_OPTIONS]
        self.interval = options.get(self.DETECTION_INTERVAL, 60)
        self.poll_url = options.get(self.POLL_URL, '')
        self.poll_url_ssl_verify = options.get(self.POLL_URL_SSL_VERIFY, True)
        self.poll_url_healthy_response = options.get(
            self.POLL_URL_HEALTHY_RESPONSE, '')
        self.poll_url_retry_limit = options.get(self.POLL_URL_RETRY_LIMIT, '')
        self.poll_url_retry_interval = options.get(
            self.POLL_URL_RETRY_INTERVAL, '')
        self.node_update_timeout = options.get(self.NODE_UPDATE_TIMEOUT, 300)

        recover_settings = self.properties[self.RECOVERY]
        self.recover_actions = recover_settings[self.RECOVERY_ACTIONS]
        self.fencing_types = recover_settings[self.RECOVERY_FENCING]
        self.node_delete_timeout = recover_settings.get(
            self.RECOVERY_DELETE_TIMEOUT, None)
        self.node_force_recreate = recover_settings.get(
            self.RECOVERY_FORCE_RECREATE, False)

    def validate(self, context, validate_props=False):
        super(HealthPolicy, self).validate(context,
                                           validate_props=validate_props)

        if len(self.recover_actions) > 1:
            message = _("Only one '%s' is supported for now."
                        ) % self.RECOVERY_ACTIONS
            raise exc.ESchema(message=message)

        if self.interval < cfg.CONF.health_check_interval_min:
            message = _("Specified interval of %(interval)d seconds has to be "
                        "larger than health_check_interval_min of "
                        "%(min_interval)d seconds set in configuration."
                        ) % {"interval": self.interval,
                             "min_interval":
                                 cfg.CONF.health_check_interval_min}
            raise exc.InvalidSpec(message=message)

        # TODO(Qiming): Add detection of duplicated action names when
        # support to list of actions is implemented.

    def attach(self, cluster, enabled=True):
        """"Hook for policy attach.

        Register the cluster for health management.

        :param cluster: The cluster to which the policy is being attached to.
        :param enabled: The attached cluster policy is enabled or disabled.
        :return: A tuple comprising execution result and policy data.
        """
        p_type = cluster.rt['profile'].type_name
        action_names = [a['name'] for a in self.recover_actions]
        if p_type != 'os.nova.server':
            if consts.RECOVER_REBUILD in action_names:
                err_msg = _("Recovery action REBUILD is only applicable to "
                            "os.nova.server clusters.")
                return False, err_msg

            if consts.RECOVER_REBOOT in action_names:
                err_msg = _("Recovery action REBOOT is only applicable to "
                            "os.nova.server clusters.")
                return False, err_msg

        kwargs = {
            'check_type': self.check_type,
            'interval': self.interval,
            'params': {
                'recover_action': self.recover_actions,
                'poll_url': self.poll_url,
                'poll_url_ssl_verify': self.poll_url_ssl_verify,
                'poll_url_healthy_response': self.poll_url_healthy_response,
                'poll_url_retry_limit': self.poll_url_retry_limit,
                'poll_url_retry_interval': self.poll_url_retry_interval,
                'node_update_timeout': self.node_update_timeout,
                'node_delete_timeout': self.node_delete_timeout,
                'node_force_recreate': self.node_force_recreate,
            },
            'enabled': enabled
        }

        health_manager.register(cluster.id, engine_id=None, **kwargs)

        data = {
            'check_type': self.check_type,
            'interval': self.interval,
            'poll_url': self.poll_url,
            'poll_url_ssl_verify': self.poll_url_ssl_verify,
            'poll_url_healthy_response': self.poll_url_healthy_response,
            'poll_url_retry_limit': self.poll_url_retry_limit,
            'poll_url_retry_interval': self.poll_url_retry_interval,
            'node_update_timeout': self.node_update_timeout,
            'node_delete_timeout': self.node_delete_timeout,
            'node_force_recreate': self.node_force_recreate,
        }

        return True, self._build_policy_data(data)

    def detach(self, cluster):
        """Hook for policy detach.

        Unregister the cluster for health management.
        :param cluster: The target cluster.
        :returns: A tuple comprising the execution result and reason.
        """
        health_manager.unregister(cluster.id)
        return True, ''

    def pre_op(self, cluster_id, action, **args):
        """Hook before action execution.

        One of the task for this routine is to disable health policy if the
        action is a request that will shrink the cluster. The reason is that
        the policy may attempt to recover nodes that are to be deleted.

        :param cluster_id: The ID of the target cluster.
        :param action: The action to be examined.
        :param kwargs args: Other keyword arguments to be checked.
        :returns: Boolean indicating whether the checking passed.
        """
        if action.action in (consts.CLUSTER_SCALE_IN,
                             consts.CLUSTER_DEL_NODES,
                             consts.NODE_DELETE):
            health_manager.disable(cluster_id)
            return True

        if action.action == consts.CLUSTER_RESIZE:
            deletion = action.data.get('deletion', None)
            if deletion:
                health_manager.disable(cluster_id)
                return True

            cluster = action.entity
            current = len(cluster.nodes)
            res, reason = scaleutils.parse_resize_params(action, cluster,
                                                         current)
            if res == base.CHECK_ERROR:
                action.data['status'] = base.CHECK_ERROR
                action.data['reason'] = reason
                return False

            if action.data.get('deletion', None):
                health_manager.disable(cluster_id)
                return True

        pd = {
            'recover_action': self.recover_actions,
            'fencing': self.fencing_types,
        }
        action.data.update({'health': pd})
        action.store(action.context)

        return True

    def post_op(self, cluster_id, action, **args):
        """Hook before action execution.

        One of the task for this routine is to re-enable health policy if the
        action is a request that will shrink the cluster thus the policy has
        been temporarily disabled.

        :param cluster_id: The ID of the target cluster.
        :param action: The action to be examined.
        :param kwargs args: Other keyword arguments to be checked.
        :returns: Boolean indicating whether the checking passed.
        """
        if action.action in (consts.CLUSTER_SCALE_IN,
                             consts.CLUSTER_DEL_NODES,
                             consts.NODE_DELETE):
            health_manager.enable(cluster_id)
            return True

        if action.action == consts.CLUSTER_RESIZE:
            deletion = action.data.get('deletion', None)
            if deletion:
                health_manager.enable(cluster_id)
                return True

            cluster = action.entity
            current = len(cluster.nodes)
            res, reason = scaleutils.parse_resize_params(action, cluster,
                                                         current)
            if res == base.CHECK_ERROR:
                action.data['status'] = base.CHECK_ERROR
                action.data['reason'] = reason
                return False

            if action.data.get('deletion', None):
                health_manager.enable(cluster_id)
                return True

        return True

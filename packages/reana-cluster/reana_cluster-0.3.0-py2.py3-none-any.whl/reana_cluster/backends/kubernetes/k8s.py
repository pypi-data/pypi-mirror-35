# -*- coding: utf-8 -*-
#
# This file is part of REANA.
# Copyright (C) 2017 CERN.
#
# REANA is free software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# REANA is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# REANA; if not, write to the Free Software Foundation, Inc., 59 Temple Place,
# Suite 330, Boston, MA 02111-1307, USA.
#
# In applying this license, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization or
# submit itself to any jurisdiction.
"""Abstract Base Class representing REANA cluster backend."""

import json
import logging
import subprocess

import pkg_resources
import yaml
from jinja2 import Environment, FileSystemLoader, TemplateNotFound
from kubernetes import client as k8s_client
from kubernetes import config as k8s_config
from kubernetes.client import Configuration
from kubernetes.client.rest import ApiException
from pkg_resources import parse_version

from reana_cluster import ReanaBackendABC


class KubernetesBackend(ReanaBackendABC):
    """A class for interacting with Kubernetes.

    Attributes:
        __cluster_type  Type of the backend this class implements support for.
        _conf   Configuration.

    """

    __cluster_type = 'Kubernetes'

    _conf = {
        'templates_folder': pkg_resources.resource_filename(
            __name__, '/templates'),
        'min_version': 'v1.9.4',
        'max_version': 'v1.9.4',
    }

    def __init__(self,
                 cluster_spec,
                 cluster_conf=None,
                 kubeconfig=None,
                 kubeconfig_context=None,
                 production=False):
        """Initialise Kubernetes specific ReanaBackend-object.

        :param cluster_spec: Dictionary representing complete REANA
            cluster spec file.

        :param cluster_conf: A generator/iterable of Kubernetes YAML manifests
            of REANA components as Python objects. If set to `None`
            cluster_conf will be generated from manifest templates in
            `templates` folder specified in `_conf.templates_folder`

        :param kubeconfig: Name of the kube-config file to use for configuring
            reana-cluster. If set to `None` then `$HOME/.kube/config` will be
            used.
            Note: Might pickup a config-file defined in $KUBECONFIG as well.

        :param kubeconfig_context: set the active context. If is set to `None`,
            current_context from config file will be used.
        :param production: Boolean which represents whether REANA is
            is configured with production setup (using CEPH) or not.

        """
        logging.debug('Creating a ReanaBackend object '
                      'for Kubernetes interaction.')

        # Load Kubernetes cluster configuration. If reana-cluster.yaml
        # doesn't specify this K8S Python API defaults to '$HOME/.kube/config'
        self.kubeconfig = kubeconfig or \
            cluster_spec['cluster'].get('config', None)
        self.kubeconfig_context = kubeconfig_context or \
            cluster_spec['cluster'].get('config_context', None)

        k8s_api_client_config = Configuration()

        k8s_config.load_kube_config(kubeconfig, self.kubeconfig_context,
                                    k8s_api_client_config)

        Configuration.set_default(k8s_api_client_config)

        # Instantiate clients for various Kubernetes REST APIs
        self._corev1api = k8s_client.CoreV1Api()
        self._versionapi = k8s_client.VersionApi()
        self._extbetav1api = k8s_client.ExtensionsV1beta1Api()
        self._rbacauthorizationv1api = k8s_client.RbacAuthorizationV1Api()

        self.k8s_api_client_config = k8s_api_client_config

        self.cluster_spec = cluster_spec
        self.cluster_conf = cluster_conf or \
            self.generate_configuration(cluster_spec, production=production)

    @property
    def cluster_type(self):
        """."""
        return self.__cluster_type

    @property
    def cluster_url(self):
        """Return URL of Kubernetes instance `reana-cluster` connects to."""
        return self.k8s_api_client_config.host

    @property
    def current_config(self):
        """Return Kubernetes configuration (e.g. `~/.kube/config`)."""
        return self.k8s_api_client_config

    @property
    def current_kubeconfig_context(self):
        """Return K8S kubeconfig context used to initialize K8S Client(s)."""
        return self.kubeconfig_context

    @property
    def current_kubeconfig(self):
        """Return K8S kubeconfig used to initialize K8S Client(s).

        (e.g. `~/.kube/config`)

        """
        return self.kubeconfig

    @classmethod
    def generate_configuration(cls, cluster_spec, production=False):
        """Generate Kubernetes manifest files used to init REANA cluster.

        :param cluster_spec: Dictionary representing complete REANA
            cluster spec file.
        :param production: Boolean which represents whether REANA is
            deployed with production setup (using CEPH) or not.

        :return: A generator/iterable of generated Kubernetes YAML manifests
            as Python objects.
        """
        # Setup an Environment for Jinja
        env = Environment(
            loader=FileSystemLoader(
                cls._conf['templates_folder']),
            keep_trailing_newline=False
        )

        # Define where are backend conf params needed when rendering templates.
        be_conf_params_fp = cls._conf['templates_folder'] + '/config.yaml'

        try:
            with open(be_conf_params_fp) as f:

                # Load backend conf params
                backend_conf_parameters = yaml.load(f.read())
                # change type of deployment (prod|local) if requested
                if production or cluster_spec['cluster'].get('production'):
                    backend_conf_parameters['DEPLOYMENT'] = 'prod'

                if cluster_spec['cluster'].get('root_path'):
                    backend_conf_parameters['ROOT_PATH'] = \
                        cluster_spec['cluster'].get('root_path')

                if cluster_spec['cluster'].get('cephfs_monitors'):
                    backend_conf_parameters['CEPHFS_MONITORS'] = \
                        cluster_spec['cluster'].get('cephfs_monitors')

                if cluster_spec['cluster'].get('db_persistence_path'):
                    backend_conf_parameters['DB_PERSISTENCE_PATH'] = \
                        cluster_spec['cluster'].get('db_persistence_path')

                # Would it be better to combine templates or populated
                # templates in Python code for improved extensibility?
                # Just drop a .yaml template and add necessary to config.yaml
                # without changing anything?

                # Load template combining all other templates from
                # templates folder
                template = env.get_template('backend_conf.yaml')

                components = cluster_spec['components']
                rs_img = components['reana-server']['image']
                rjc_img = components['reana-job-controller']['image']
                rwfc_img = components['reana-workflow-controller']['image']
                rwm_img = components['reana-workflow-monitor']['image']
                rmb_img = components['reana-message-broker']['image']
                rweyadage_img = components[
                    'reana-workflow-engine-yadage']['image']
                rwecwl_img = components[
                    'reana-workflow-engine-cwl']['image']
                rweserial_img = components[
                    'reana-workflow-engine-serial']['image']

                rs_environment = components['reana-server']\
                    .get('environment', [])
                rjc_environment = components['reana-job-controller'] \
                    .get('environment', [])
                rwfc_environment = components['reana-workflow-controller'] \
                    .get('environment', [])
                rwm_environment = components['reana-workflow-monitor'] \
                    .get('environment', [])
                rmb_environment = components['reana-message-broker'] \
                    .get('environment', [])
                rweyadage_environment = components[
                    'reana-workflow-engine-yadage'] \
                    .get('environment', [])
                rwecwl_environment = components[
                    'reana-workflow-engine-cwl'] \
                    .get('environment', [])
                rweserial_environment = components[
                    'reana-workflow-engine-serial'] \
                    .get('environment', [])

                rs_environment = components['reana-server']\
                    .get('environment', [])
                rjc_environment = components['reana-job-controller'] \
                    .get('environment', [])
                rwfc_environment = components['reana-workflow-controller'] \
                    .get('environment', [])
                rwm_environment = components['reana-workflow-monitor'] \
                    .get('environment', [])
                rmb_environment = components['reana-message-broker'] \
                    .get('environment', [])

                rs_mountpoints = components['reana-server']\
                    .get('mountpoints', [])
                rjc_mountpoints = components['reana-job-controller']\
                    .get('mountpoints', [])
                rwfc_mountpoints = components['reana-workflow-controller']\
                    .get('mountpoints', [])
                rwm_mountpoints = components['reana-workflow-monitor'] \
                    .get('mountpoints', [])
                rmb_mountpoints = components['reana-message-broker'] \
                    .get('mountpoints', [])
                rweyadage_mountpoints = components[
                    'reana-workflow-engine-yadage'] \
                    .get('mountpoints', [])
                rwecwl_mountpoints = components[
                    'reana-workflow-engine-cwl'] \
                    .get('mountpoints', [])
                rweserial_mountpoints = components[
                    'reana-workflow-engine-serial'] \
                    .get('mountpoints', [])

                # Render the template using given backend config parameters
                cluster_conf = template.\
                    render(backend_conf_parameters,
                           REANA_URL=cluster_spec['cluster'].get(
                               'reana_url',
                               'reana.cern.ch'),
                           SERVER_IMAGE=rs_img,
                           JOB_CONTROLLER_IMAGE=rjc_img,
                           WORKFLOW_CONTROLLER_IMAGE=rwfc_img,
                           WORKFLOW_MONITOR_IMAGE=rwm_img,
                           MESSAGE_BROKER_IMAGE=rmb_img,
                           WORKFLOW_ENGINE_YADAGE_IMAGE=rweyadage_img,
                           WORKFLOW_ENGINE_CWL_IMAGE=rwecwl_img,
                           WORKFLOW_ENGINE_SERIAL_IMAGE=rweserial_img,
                           RS_MOUNTPOINTS=rs_mountpoints,
                           RJC_MOUNTPOINTS=rjc_mountpoints,
                           RWFC_MOUNTPOINTS=rwfc_mountpoints,
                           RWM_MOUNTPOINTS=rwm_mountpoints,
                           RMB_MOUNTPOINTS=rmb_mountpoints,
                           RWEYADAGE_MOUNTPOINTS=rweyadage_mountpoints,
                           RWECWL_MOUNTPOINTS=rwecwl_mountpoints,
                           RWESERIAL_MOUNTPOINTS=rweserial_mountpoints,
                           RS_ENVIRONMENT=rs_environment,
                           RJC_ENVIRONMENT=rjc_environment,
                           RWFC_ENVIRONMENT=rwfc_environment,
                           RWM_ENVIRONMENT=rwm_environment,
                           RMB_ENVIRONMENT=rmb_environment,
                           RWEYADAGE_ENVIRONMENT=rweyadage_environment,
                           RWECWL_ENVIRONMENT=rwecwl_environment,
                           RWESERIAL_ENVIRONMENT=rweserial_environment,
                           )

                # Strip empty lines for improved readability
                cluster_conf = '\n'.join(
                    [line for line in cluster_conf.splitlines() if
                     line.strip()])

                # Should print the whole configuration in a loop
                # Now prints just memory address of generator object
                logging.debug('Loaded K8S config successfully: \n {}'
                              .format(yaml.load_all(cluster_conf)))

        except TemplateNotFound as e:
            logging.info(
                'Something wrong when fetching K8S config file templates from '
                '{filepath} : \n'
                '{error}'.format(
                    filepath=cls._conf['templates_folder'],
                    error=e.strerror))
            raise e

        except IOError as e:
            logging.info(
                'Something wrong when reading K8S config parameters-file from '
                '{filepath} : \n'
                '{error}'.format(filepath=be_conf_params_fp,
                                 error=e.strerror))
            raise e

        # As Jinja rendered string is basically multiple YAML documents in one
        # string parse it with YAML-library and return a generator containing
        # independent YAML documents (split from `---`) as Python objects.
        return yaml.load_all(cluster_conf)

    def init(self):
        """Initialize REANA cluster, i.e. deploy REANA components to backend.

        :return: `True` if init was completed successfully.
        :rtype: bool

        :raises ApiException: Failed to successfully interact with
            Kubernetes REST API. Reason for failure is indicated as HTTP error
            codes in addition to a textual description of the error.

        """
        if not self._cluster_running():
            pass

        # Should check that cluster is not already initialized.
        # Maybe use `verify_components()` or `get()` each component?

        for manifest in self.cluster_conf:
            try:

                logging.debug(json.dumps(manifest))

                if manifest['kind'] == 'Deployment':

                    # REANA Job Controller needs access to K8S-cluster's
                    # service-account-token in order to create new Pods.
                    if manifest['metadata']['name'] == 'job-controller':
                        manifest = self._add_service_acc_key_to_jc(manifest)

                    self._extbetav1api.create_namespaced_deployment(
                        body=manifest,
                        namespace=manifest['metadata'].get('namespace',
                                                           'default'))

                elif manifest['kind'] == 'Namespace':
                    self._corev1api.create_namespace(body=manifest)

                elif manifest['kind'] == 'ResourceQuota':
                    self._corev1api.create_namespaced_resource_quota(
                        body=manifest,
                        namespace=manifest['metadata']['namespace'])

                elif manifest['kind'] == 'Service':
                    self._corev1api.create_namespaced_service(
                        body=manifest,
                        namespace=manifest['metadata'].get('namespace',
                                                           'default'))
                elif manifest['kind'] == 'ClusterRole':
                    self._rbacauthorizationv1api.create_cluster_role(
                        body=manifest)
                elif manifest['kind'] == 'ClusterRoleBinding':
                    self._rbacauthorizationv1api.\
                        create_cluster_role_binding(body=manifest)

                elif manifest['kind'] == 'Ingress':
                    self._extbetav1api.create_namespaced_ingress(
                            body=manifest,
                            namespace=manifest['metadata'].get('namespace',
                                                               'default'))

            except ApiException as e:  # Handle K8S API errors

                if e.status == 409:
                    logging.info(
                        '{0} {1} already exists, continuing ...'.format(
                            manifest['kind'],
                            manifest['metadata'].get('name')))
                    continue

                if e.status == 400:
                    pass

                raise e

        return True

    def _add_service_acc_key_to_jc(self, rjc_manifest):
        """Add K8S service account credentials to REANA Job Controller.

        In order to interact (e.g. create Pods to run workflows) with
        Kubernetes cluster REANA Job Controller needs to have access to
        API credentials of Kubernetes service account.

        :param rjc_manifest: Python object representing Kubernetes Deployment-
            manifest file of REANA Job Controller generated with
            `generate_configuration()`.

        :return: Python object representing Kubernetes Deployment-
            manifest file of REANA Job Controller with service account
            credentials of the Kubernetes instance `reana-cluster`
            if configured to interact with.
        """
        # Get all secrets for default namespace
        # Cannot use `k8s_corev1.read_namespaced_secret()` since
        # exact name of the token (e.g. 'default-token-8p260') is not know.
        secrets = self._corev1api.list_namespaced_secret(
            'default', include_uninitialized='false')

        # Maybe debug print all secrets should not be enabled?
        # logging.debug(k8s_corev1.list_secret_for_all_namespaces())

        # K8S might return many secrets. Find `service-account-token`.
        for item in secrets.items:
            if item.type == 'kubernetes.io/service-account-token':
                srv_acc_token = item.metadata.name

                # Search for appropriate place to place the token
                # in job-controller deployment manifest
                for i in rjc_manifest['spec']['template']['spec']['volumes']:
                    if i['name'] == 'svaccount':
                        i['secret']['secretName'] = srv_acc_token

        return rjc_manifest

    def _cluster_running(self):
        """Verify that interaction with cluster backend is possible.

        THIS IS CURRENTLY JUST A MOCKUP. NO REAL CHECKS ARE DONE.

        Verifies that Kubernetes deployment is reachable through it's REST API.
        Only very basic checking is done and it is not guaranteed that REANA
        cluster can be initialized, just that interaction with the specified
        Kubernetes deployment is possible.

        :return: `True` if Kubernetes deployment is reachable through
            it's REST API.
        """
        # Maybe just do a request to `/healthz/ping` -endpoint at cluster_url?
        # i.e no kubernetes-python client interaction?
        return True

    def restart(self):
        """Restarts all deployed components. NOT CURRENTLY IMPLEMENTED.

        :raises NotImplementedError:

        """
        raise NotImplementedError()

    def down(self):
        """Bring REANA cluster down, i.e. deletes all deployed components.

        Deletes all Kubernetes Deployments, Namespaces, Resourcequotas and
        Services that were created during initialization of REANA cluster.

        :return: `True` if all components were destroyed successfully.
        :rtype: bool

        :raises ApiException: Failed to successfully interact with
            Kubernetes REST API. Reason for failure is indicated as HTTP error
            codes in addition to a textual description of the error.

        """
        # What is a good propagationPolicy of `V1DeleteOptions`?
        # Default is `Orphan`
        # https://kubernetes.io/docs/concepts/workloads/controllers/garbage-collection/
        # https://github.com/kubernetes-incubator/client-python/blob/master/examples/notebooks/create_deployment.ipynb

        if not self._cluster_running():
            pass

        # All K8S objects seem to use default -namespace.
        # Is this true always, or do we create something for non-default
        # namespace (in the future)?
        for manifest in self.cluster_conf:
            try:
                logging.debug(json.dumps(manifest))

                if manifest['kind'] == 'Deployment':
                    self._extbetav1api.delete_namespaced_deployment(
                        name=manifest['metadata']['name'],
                        body=k8s_client.V1DeleteOptions(
                            propagation_policy="Foreground",
                            grace_period_seconds=5),
                        namespace=manifest['metadata'].get('namespace',
                                                           'default'))

                elif manifest['kind'] == 'Namespace':
                    self._corev1api.delete_namespace(
                        name=manifest['metadata']['name'],
                        body=k8s_client.V1DeleteOptions())

                elif manifest['kind'] == 'ResourceQuota':
                    self._corev1api.delete_namespaced_resource_quota(
                        name=manifest['metadata']['name'],
                        body=k8s_client.V1DeleteOptions(),
                        namespace=manifest['metadata'].get('namespace',
                                                           'default'))

                elif manifest['kind'] == 'Service':
                    self._corev1api.delete_namespaced_service(
                        name=manifest['metadata']['name'],
                        body=k8s_client.V1DeleteOptions(),
                        namespace=manifest['metadata'].get('namespace',
                                                           'default'))

                elif manifest['kind'] == 'ClusterRole':
                    self._rbacauthorizationv1api.delete_cluster_role(
                        name=manifest['metadata']['name'],
                        body=k8s_client.V1DeleteOptions())

                elif manifest['kind'] == 'ClusterRoleBinding':
                    self._rbacauthorizationv1api.\
                        delete_cluster_role_binding(
                            name=manifest['metadata']['name'],
                            body=k8s_client.V1DeleteOptions())

                elif manifest['kind'] == 'Ingress':
                    self._extbetav1api.delete_namespaced_ingress(
                            name=manifest['metadata']['name'],
                            body=k8s_client.V1DeleteOptions(),
                            namespace=manifest['metadata'].get('namespace',
                                                               'default'))

            except ApiException as e:  # Handle K8S API errors

                if e.status == 409:  # Conflict, object probably already exists
                    pass

                if e.status == 404:
                    pass

                if e.status == 400:
                    pass

        return True

    def get_component(self, component_name, component_namespace='default'):
        """Fetch info (e.g.URL) about deployed REANA component.

        Fetches information such as URL(s) of a REANA component deployed to
        REANA cluster.

        :param component_name: Name of the REANA component whose information
            is to be fetched.
        :type component_name: string

        :param component_namespace: Namespace where REANA component specified
            with `component_name` is deployed. Kubernetes specific information.
        :type component_namespace: string

        :return: Information (e.g. URL(s)) about a deployed REANA component.
        :rtype: dict

        :raises ApiException: Failed to successfully interact with
            Kubernetes REST API. Reason for failure is indicated as HTTP error
            codes in addition to a textual description of the error.

        """
        comp_info = {
            'internal_ip': '',
            'ports': [],
            'external_ip_s': [],
            'external_name': '',
        }

        try:

            # Strip reana-prefix from component name if it is there.
            component_name_without_prefix = None
            if not component_name.startswith('reana-'):
                component_name_without_prefix = component_name
            else:
                component_name_without_prefix = component_name[len('reana-'):]

            minikube_ip = None

            # If running on Minikube, ip-address is Minikube VM-address
            nodeconf = self._corev1api.list_node()

            # There can be many Nodes. Is this a problem?
            # (i.e. How to know which is the one should be connected to?)
            for item in nodeconf.items:
                if item.metadata.name == 'minikube' or \
                        item.metadata.name == self.kubeconfig_context:

                    # Running on minikube --> get ip-addr
                    minikube_ip = subprocess.check_output(['minikube', 'ip'])
                    minikube_ip = minikube_ip.decode("utf-8")
                    minikube_ip = minikube_ip.replace('\n', '')

            # Get ip-addresses and ports of the component (K8S service)
            comp = self._corev1api.read_namespaced_service(
                component_name_without_prefix,
                component_namespace)

            logging.debug(comp)

            comp_info['external_name'] = comp.spec.external_name
            comp_info['external_ip_s'] = [minikube_ip] or \
                comp.spec.external_i_ps
            comp_info['internal_ip'] = comp.spec.external_i_ps

            for port in comp.spec.ports:
                if minikube_ip:
                    comp_info['ports'].append(str(port.node_port))
                else:
                    comp_info['ports'].append(str(port.port))

            logging.debug(comp_info)

        except ApiException as e:  # Handle K8S API errors

            if e.status == 409:  # Conflict
                pass

            if e.status == 404:
                pass

            if e.status == 400:
                pass

            raise e

        return comp_info

    def verify_components(self):
        """Verify that REANA components are setup according to specifications.

        Verifies that REANA components are set up as specified in REANA
        cluster specifications file.
        Components must be deployed first, before verification can be done.

        Currently verifies only that docker image (<NAME>:<TAG> -string) of a
        deployed component matches to docker image specified in REANA cluster
        specification file.

        :return: Dictionary with component names for keys and booleans
        for values stating if verification was successful.
        :rtype: dict

        :raises ApiException: Failed to successfully interact with
            Kubernetes REST API. Reason for failure is indicated as HTTP error
            codes in addition to a textual description of the error.

        """
        if not self._cluster_running():
            pass

        try:
            matching_components = dict()
            for manifest in self.cluster_conf:

                # We are only interested in Deployment manifests since
                # these define docker images that Kubernetes Pods based on
                # these Deployments should be using.
                if manifest['kind'] == 'Deployment':
                    component_name = manifest['metadata']['name']

                    # Kubernetes Deployment manifest could have multiple
                    # containers per manifest file. Current implementation
                    # expects only one container per manifest file.
                    spec_img = manifest['spec'][
                        'template']['spec']['containers'][0]['image']

                    deployed_comp = self._extbetav1api. \
                        read_namespaced_deployment(component_name, 'default')

                    logging.debug(deployed_comp)

                    # Kubernetes Deployment could have multiple containers per
                    # Deployment. Current implementation expects only one
                    # container per deployment.
                    # THIS WILL CAUSE PROBLEM if there are two Pods and one
                    # of them is (even temporarily, e.g. update situation)
                    # based on "old" image defined in older REANA cluster
                    # specification file.
                    deployed_img = deployed_comp.spec.template.spec.containers[
                        0].image

                    logging.info('Component name: {}\n'
                                 'Specified image: {}\n'
                                 'Currently deployed image: {}\n'
                                 .format(component_name,
                                         spec_img,
                                         deployed_img))

                    matching_components[component_name] = True
                    if not spec_img == deployed_img:
                        matching_components[component_name] = False
                        logging.error('Mismatch between specified and '
                                      'deployed image of {}. \n'
                                      'Specified image: {}\n'
                                      'Currently deployed image: {}\n'
                                      .format(component_name,
                                              spec_img,
                                              deployed_img))

        except ApiException as e:  # Handle K8S API errors

            if e.status == 409:
                pass

            if e.status == 404:
                pass

            if e.status == 400:
                pass

            raise e

        return matching_components

    def verify_backend(self):
        """Verify that cluster backend is compatible with REANA.

        Verifies that REANA cluster backend is 1) compatible with REANA and
        2) set up as specified in REANA cluster specifications file.

        Currently includes just a version check.

        :return: `True` if verification of backend was successful.
        :rtype: bool

        """
        return self._verify_k8s_version()

    def _verify_k8s_version(self):
        """Verify version of K8S instance is compatible with REANA cluster.

        Verifies that the version of Kubernetes instance `reana-cluster` is
        connecting to is compatible with REANA (min, max versions in config)
        and that version is compatible with target version in REANA cluster
        specifications file.

        Version strings are parsed according to PEP440, which seems to support
        semantic versioning style what Kubernetes uses.
        (PEP440 not fully compliant with semver)

        :return: Dictionary containing the current version, if it is compatible
        and the maximum compatible version.
        :rtype: dict

        """
        if not self._cluster_running():
            pass

        curr_ver = parse_version(self._versionapi.get_code().git_version)
        expected_ver = parse_version(
            self.cluster_spec['cluster']['version'])
        max_ver = parse_version(self._conf['max_version'])
        min_ver = parse_version(self._conf['min_version'])

        logging.info('Current K8S version: {}\n'
                     'Specified K8S version: {}\n'
                     'Max supported K8S version: {}\n'
                     'Min supported K8S version: {}'
                     .format(curr_ver, expected_ver, max_ver, min_ver))

        k8s_version_compatibility = dict(current_version=curr_ver,
                                         is_compatible=True,
                                         max_version=max_ver)
        # Compare current K8S version to max / min
        if curr_ver > max_ver:
            k8s_version_compatibility['is_compatible'] = False
            logging.error('Your Kubernetes version is too new: {cur} \n'
                          'Newest version REANA supports is: {max}'
                          .format(cur=curr_ver, max=max_ver))

        elif curr_ver < min_ver:
            k8s_version_compatibility['is_compatible'] = False
            logging.error('Your Kubernetes version is too old: {cur} \n'
                          'Oldest version REANA supports is: {min}'
                          .format(cur=curr_ver, min=min_ver))

        # Compare specified version to max/min
        elif expected_ver > max_ver:
            k8s_version_compatibility['is_compatible'] = False
            logging.error('Specified Kubernetes version is too new: {cur} \n'
                          'Newest version REANA supports is: {max}'
                          .format(cur=curr_ver, max=max_ver))

        elif expected_ver < min_ver:
            k8s_version_compatibility['is_compatible'] = False
            logging.error('Specified Kubernetes version is too old: {cur} \n'
                          'Oldest version REANA supports is: {min}'
                          .format(cur=curr_ver, min=min_ver))

        # Compare specified version to current K8S version
        elif expected_ver < curr_ver:
            k8s_version_compatibility['is_compatible'] = False
            logging.error('Your Kubernetes version is too new: {cur} \n'
                          'Specification expects: {expected}'
                          .format(cur=curr_ver, expected=expected_ver))

        elif expected_ver > curr_ver:
            k8s_version_compatibility['is_compatible'] = False
            logging.error('Your Kubernetes version is too old: {cur} \n'
                          'Specification expects: {expected}'
                          .format(cur=curr_ver, expected=expected_ver))

        return k8s_version_compatibility

    def get_components_status(self, component=None):
        """Return status for components in cluster.

        Gets all pods in the k8s namespace and matches them with the
        equivalent component, writing their status in a dictionary.

        :return: Dictionary containing each component and its status
        :rtype: dict

        """
        def _write_status(pod, component_name, components_status):
            """Determine the component status."""
            if pod.status.container_statuses[0].ready:
                components_status[component_name] = 'Running'
            elif pod.status.container_statuses[0].\
                    state.waiting is not None:
                components_status[component_name] = \
                    pod.status.container_statuses[0].\
                    state.waiting.reason
            else:
                components_status[component] = 'Unavailable'

        if component and component.startswith('reana-'):
            component = component.replace('reana-', '')
        all_pods = self._corev1api.list_namespaced_pod('default')
        components_status = dict()

        if component:
            for current_pod in all_pods.items:
                if current_pod.metadata.name.startswith(component):
                    _write_status(current_pod, component, components_status)
                    break
        else:
            deployment_manifests = [m for m in self.cluster_conf
                                    if m['kind'] == 'Deployment']
            for manifest in deployment_manifests:
                current_pod = None
                for pod in all_pods.items:
                    if pod.metadata.name.startswith(
                            manifest['metadata']['name']):
                        current_pod = pod
                        break
                if current_pod:
                    _write_status(current_pod, manifest['metadata']['name'],
                                  components_status)
        return components_status

    def exec_into_component(self, component_name, command):
        """Execute a command inside a component.

        :param component_name: Name of the component where the command will be
            executed.
        :param command: String which represents the command to execute inside
            the component.
        :return: Returns a string which represents the output of the command.
        """
        available_components = [manifest['metadata']['name'] for manifest in
                                self.cluster_conf
                                if manifest['kind'] == 'Deployment']

        if component_name not in available_components:
            raise Exception('{0} does not exist.'.format(component_name))

        component_pod_name = subprocess.check_output([
            'kubectl', 'get', 'pods',
            '-l=app={component_name}'.format(component_name=component_name),
            '-o', 'jsonpath="{.items[0].metadata.name}"'
        ]).decode('UTF-8').replace('"', '')

        component_shell = [
            'kubectl', 'exec', '-t', component_pod_name, '--']

        command_inside_component = []
        command_inside_component.extend(component_shell)
        command_inside_component.extend(command)

        output = subprocess.check_output(command_inside_component)
        return output.decode('UTF-8')

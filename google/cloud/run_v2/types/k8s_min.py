# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from typing import MutableMapping, MutableSequence

import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.run.v2",
    manifest={
        "Container",
        "ResourceRequirements",
        "EnvVar",
        "EnvVarSource",
        "SecretKeySelector",
        "ContainerPort",
        "VolumeMount",
        "Volume",
        "SecretVolumeSource",
        "VersionToPath",
        "CloudSqlInstance",
        "Probe",
        "HTTPGetAction",
        "HTTPHeader",
        "TCPSocketAction",
        "GRPCAction",
    },
)


class Container(proto.Message):
    r"""A single application container.
    This specifies both the container to run, the command to run in
    the container and the arguments to supply to it.
    Note that additional arguments may be supplied by the system to
    the container at runtime.

    Attributes:
        name (str):
            Name of the container specified as a DNS_LABEL.
        image (str):
            Required. URL of the Container image in
            Google Container Registry or Google Artifact
            Registry. More info:
            https://kubernetes.io/docs/concepts/containers/images
        command (MutableSequence[str]):
            Entrypoint array. Not executed within a shell. The docker
            image's ENTRYPOINT is used if this is not provided. Variable
            references $(VAR_NAME) are expanded using the container's
            environment. If a variable cannot be resolved, the reference
            in the input string will be unchanged. The $(VAR_NAME)
            syntax can be escaped with a double $$, ie: $$(VAR_NAME).
            Escaped references will never be expanded, regardless of
            whether the variable exists or not. More info:
            https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell
        args (MutableSequence[str]):
            Arguments to the entrypoint. The docker image's CMD is used
            if this is not provided. Variable references $(VAR_NAME) are
            expanded using the container's environment. If a variable
            cannot be resolved, the reference in the input string will
            be unchanged. The $(VAR_NAME) syntax can be escaped with a
            double $$, ie: $$(VAR_NAME). Escaped references will never
            be expanded, regardless of whether the variable exists or
            not. More info:
            https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell
        env (MutableSequence[google.cloud.run_v2.types.EnvVar]):
            List of environment variables to set in the
            container.
        resources (google.cloud.run_v2.types.ResourceRequirements):
            Compute Resource requirements by this
            container. More info:
            https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources
        ports (MutableSequence[google.cloud.run_v2.types.ContainerPort]):
            List of ports to expose from the container.
            Only a single port can be specified. The
            specified ports must be listening on all
            interfaces (0.0.0.0) within the container to be
            accessible.
            If omitted, a port number will be chosen and
            passed to the container through the PORT
            environment variable for the container to listen
            on.
        volume_mounts (MutableSequence[google.cloud.run_v2.types.VolumeMount]):
            Volume to mount into the container's
            filesystem.
        working_dir (str):
            Container's working directory.
            If not specified, the container runtime's
            default will be used, which might be configured
            in the container image.
        liveness_probe (google.cloud.run_v2.types.Probe):
            Periodic probe of container liveness.
            Container will be restarted if the probe fails.
            More info:
            https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
        startup_probe (google.cloud.run_v2.types.Probe):
            Startup probe of application within the
            container. All other probes are disabled if a
            startup probe is provided, until it succeeds.
            Container will not be added to service endpoints
            if the probe fails.
            More info:
            https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    image: str = proto.Field(
        proto.STRING,
        number=2,
    )
    command: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    args: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    env: MutableSequence["EnvVar"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="EnvVar",
    )
    resources: "ResourceRequirements" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="ResourceRequirements",
    )
    ports: MutableSequence["ContainerPort"] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="ContainerPort",
    )
    volume_mounts: MutableSequence["VolumeMount"] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message="VolumeMount",
    )
    working_dir: str = proto.Field(
        proto.STRING,
        number=9,
    )
    liveness_probe: "Probe" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="Probe",
    )
    startup_probe: "Probe" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="Probe",
    )


class ResourceRequirements(proto.Message):
    r"""ResourceRequirements describes the compute resource
    requirements.

    Attributes:
        limits (MutableMapping[str, str]):
            Only memory and CPU are supported. Note: The
            only supported values for CPU are '1', '2',
            '4', and '8'. Setting 4 CPU requires at least
            2Gi of memory. The values of the map is string
            form of the 'quantity' k8s type:
            https://github.com/kubernetes/kubernetes/blob/master/staging/src/k8s.io/apimachinery/pkg/api/resource/quantity.go
        cpu_idle (bool):
            Determines whether CPU should be throttled or
            not outside of requests.
    """

    limits: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=1,
    )
    cpu_idle: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class EnvVar(proto.Message):
    r"""EnvVar represents an environment variable present in a
    Container.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. Name of the environment variable. Must be a
            C_IDENTIFIER, and mnay not exceed 32768 characters.
        value (str):
            Variable references $(VAR_NAME) are expanded using the
            previous defined environment variables in the container and
            any route environment variables. If a variable cannot be
            resolved, the reference in the input string will be
            unchanged. The $(VAR_NAME) syntax can be escaped with a
            double $$, ie: $$(VAR_NAME). Escaped references will never
            be expanded, regardless of whether the variable exists or
            not. Defaults to "", and the maximum length is 32768 bytes.

            This field is a member of `oneof`_ ``values``.
        value_source (google.cloud.run_v2.types.EnvVarSource):
            Source for the environment variable's value.

            This field is a member of `oneof`_ ``values``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    value: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="values",
    )
    value_source: "EnvVarSource" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="values",
        message="EnvVarSource",
    )


class EnvVarSource(proto.Message):
    r"""EnvVarSource represents a source for the value of an EnvVar.

    Attributes:
        secret_key_ref (google.cloud.run_v2.types.SecretKeySelector):
            Selects a secret and a specific version from
            Cloud Secret Manager.
    """

    secret_key_ref: "SecretKeySelector" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="SecretKeySelector",
    )


class SecretKeySelector(proto.Message):
    r"""SecretEnvVarSource represents a source for the value of an
    EnvVar.

    Attributes:
        secret (str):
            Required. The name of the secret in Cloud Secret Manager.
            Format: {secret_name} if the secret is in the same project.
            projects/{project}/secrets/{secret_name} if the secret is in
            a different project.
        version (str):
            The Cloud Secret Manager secret version.
            Can be 'latest' for the latest version, an
            integer for a specific version, or a version
            alias.
    """

    secret: str = proto.Field(
        proto.STRING,
        number=1,
    )
    version: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ContainerPort(proto.Message):
    r"""ContainerPort represents a network port in a single
    container.

    Attributes:
        name (str):
            If specified, used to specify which protocol
            to use. Allowed values are "http1" and "h2c".
        container_port (int):
            Port number the container listens on. This must be a valid
            TCP port number, 0 < container_port < 65536.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    container_port: int = proto.Field(
        proto.INT32,
        number=3,
    )


class VolumeMount(proto.Message):
    r"""VolumeMount describes a mounting of a Volume within a
    container.

    Attributes:
        name (str):
            Required. This must match the Name of a
            Volume.
        mount_path (str):
            Required. Path within the container at which the volume
            should be mounted. Must not contain ':'. For Cloud SQL
            volumes, it can be left empty, or must otherwise be
            ``/cloudsql``. All instances defined in the Volume will be
            available as ``/cloudsql/[instance]``. For more information
            on Cloud SQL volumes, visit
            https://cloud.google.com/sql/docs/mysql/connect-run
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    mount_path: str = proto.Field(
        proto.STRING,
        number=3,
    )


class Volume(proto.Message):
    r"""Volume represents a named volume in a container.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. Volume's name.
        secret (google.cloud.run_v2.types.SecretVolumeSource):
            Secret represents a secret that should
            populate this volume. More info:
            https://kubernetes.io/docs/concepts/storage/volumes#secret

            This field is a member of `oneof`_ ``volume_type``.
        cloud_sql_instance (google.cloud.run_v2.types.CloudSqlInstance):
            For Cloud SQL volumes, contains the specific
            instances that should be mounted. Visit
            https://cloud.google.com/sql/docs/mysql/connect-run
            for more information on how to connect Cloud SQL
            and Cloud Run.

            This field is a member of `oneof`_ ``volume_type``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    secret: "SecretVolumeSource" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="volume_type",
        message="SecretVolumeSource",
    )
    cloud_sql_instance: "CloudSqlInstance" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="volume_type",
        message="CloudSqlInstance",
    )


class SecretVolumeSource(proto.Message):
    r"""The secret's value will be presented as the content of a file
    whose name is defined in the item path. If no items are defined,
    the name of the file is the secret.

    Attributes:
        secret (str):
            Required. The name of the secret in Cloud
            Secret Manager. Format: {secret} if the secret
            is in the same project.
            projects/{project}/secrets/{secret} if the
            secret is in a different project.
        items (MutableSequence[google.cloud.run_v2.types.VersionToPath]):
            If unspecified, the volume will expose a file whose name is
            the secret, relative to VolumeMount.mount_path. If
            specified, the key will be used as the version to fetch from
            Cloud Secret Manager and the path will be the name of the
            file exposed in the volume. When items are defined, they
            must specify a path and a version.
        default_mode (int):
            Integer representation of mode bits to use on created files
            by default. Must be a value between 0000 and 0777 (octal),
            defaulting to 0444. Directories within the path are not
            affected by this setting.

            Notes

            -  Internally, a umask of 0222 will be applied to any
               non-zero value.
            -  This is an integer representation of the mode bits. So,
               the octal integer value should look exactly as the chmod
               numeric notation with a leading zero. Some examples: for
               chmod 777 (a=rwx), set to 0777 (octal) or 511 (base-10).
               For chmod 640 (u=rw,g=r), set to 0640 (octal) or 416
               (base-10). For chmod 755 (u=rwx,g=rx,o=rx), set to 0755
               (octal) or 493 (base-10).
            -  This might be in conflict with other options that affect
               the file mode, like fsGroup, and the result can be other
               mode bits set.

            This might be in conflict with other options that affect the
            file mode, like fsGroup, and as a result, other mode bits
            could be set.
    """

    secret: str = proto.Field(
        proto.STRING,
        number=1,
    )
    items: MutableSequence["VersionToPath"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="VersionToPath",
    )
    default_mode: int = proto.Field(
        proto.INT32,
        number=3,
    )


class VersionToPath(proto.Message):
    r"""VersionToPath maps a specific version of a secret to a relative file
    to mount to, relative to VolumeMount's mount_path.

    Attributes:
        path (str):
            Required. The relative path of the secret in
            the container.
        version (str):
            The Cloud Secret Manager secret version.
            Can be 'latest' for the latest value, or an
            integer or a secret alias for a specific
            version.
        mode (int):
            Integer octal mode bits to use on this file, must be a value
            between 01 and 0777 (octal). If 0 or not set, the Volume's
            default mode will be used.

            Notes

            -  Internally, a umask of 0222 will be applied to any
               non-zero value.
            -  This is an integer representation of the mode bits. So,
               the octal integer value should look exactly as the chmod
               numeric notation with a leading zero. Some examples: for
               chmod 777 (a=rwx), set to 0777 (octal) or 511 (base-10).
               For chmod 640 (u=rw,g=r), set to 0640 (octal) or 416
               (base-10). For chmod 755 (u=rwx,g=rx,o=rx), set to 0755
               (octal) or 493 (base-10).
            -  This might be in conflict with other options that affect
               the file mode, like fsGroup, and the result can be other
               mode bits set.
    """

    path: str = proto.Field(
        proto.STRING,
        number=1,
    )
    version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    mode: int = proto.Field(
        proto.INT32,
        number=3,
    )


class CloudSqlInstance(proto.Message):
    r"""Represents a specific Cloud SQL instance.

    Attributes:
        instances (MutableSequence[str]):
            The Cloud SQL instance connection names, as
            can be found in
            https://console.cloud.google.com/sql/instances.
            Visit
            https://cloud.google.com/sql/docs/mysql/connect-run
            for more information on how to connect Cloud SQL
            and Cloud Run. Format:
            {project}:{location}:{instance}
    """

    instances: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class Probe(proto.Message):
    r"""Probe describes a health check to be performed against a
    container to determine whether it is alive or ready to receive
    traffic.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        initial_delay_seconds (int):
            Number of seconds after the container has
            started before the probe is initiated.
            Defaults to 0 seconds. Minimum value is 0.
            Maximum value for liveness probe is 3600.
            Maximum value for startup probe is 240. More
            info:
            https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
        timeout_seconds (int):
            Number of seconds after which the probe times out. Defaults
            to 1 second. Minimum value is 1. Maximum value is 3600. Must
            be smaller than period_seconds. More info:
            https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
        period_seconds (int):
            How often (in seconds) to perform the probe. Default to 10
            seconds. Minimum value is 1. Maximum value for liveness
            probe is 3600. Maximum value for startup probe is 240. Must
            be greater or equal than timeout_seconds.
        failure_threshold (int):
            Minimum consecutive failures for the probe to
            be considered failed after having succeeded.
            Defaults to 3. Minimum value is 1.
        http_get (google.cloud.run_v2.types.HTTPGetAction):
            HTTPGet specifies the http request to
            perform. Exactly one of httpGet, tcpSocket, or
            grpc must be specified.

            This field is a member of `oneof`_ ``probe_type``.
        tcp_socket (google.cloud.run_v2.types.TCPSocketAction):
            TCPSocket specifies an action involving a TCP
            port. Exactly one of httpGet, tcpSocket, or grpc
            must be specified.

            This field is a member of `oneof`_ ``probe_type``.
        grpc (google.cloud.run_v2.types.GRPCAction):
            GRPC specifies an action involving a gRPC
            port. Exactly one of httpGet, tcpSocket, or grpc
            must be specified.

            This field is a member of `oneof`_ ``probe_type``.
    """

    initial_delay_seconds: int = proto.Field(
        proto.INT32,
        number=1,
    )
    timeout_seconds: int = proto.Field(
        proto.INT32,
        number=2,
    )
    period_seconds: int = proto.Field(
        proto.INT32,
        number=3,
    )
    failure_threshold: int = proto.Field(
        proto.INT32,
        number=4,
    )
    http_get: "HTTPGetAction" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="probe_type",
        message="HTTPGetAction",
    )
    tcp_socket: "TCPSocketAction" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="probe_type",
        message="TCPSocketAction",
    )
    grpc: "GRPCAction" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="probe_type",
        message="GRPCAction",
    )


class HTTPGetAction(proto.Message):
    r"""HTTPGetAction describes an action based on HTTP Get requests.

    Attributes:
        path (str):
            Path to access on the HTTP server. Defaults
            to '/'.
        http_headers (MutableSequence[google.cloud.run_v2.types.HTTPHeader]):
            Custom headers to set in the request. HTTP
            allows repeated headers.
    """

    path: str = proto.Field(
        proto.STRING,
        number=1,
    )
    http_headers: MutableSequence["HTTPHeader"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="HTTPHeader",
    )


class HTTPHeader(proto.Message):
    r"""HTTPHeader describes a custom header to be used in HTTP
    probes

    Attributes:
        name (str):
            Required. The header field name
        value (str):
            The header field value
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    value: str = proto.Field(
        proto.STRING,
        number=2,
    )


class TCPSocketAction(proto.Message):
    r"""TCPSocketAction describes an action based on opening a socket

    Attributes:
        port (int):
            Port number to access on the container. Must
            be in the range 1 to 65535. If not specified,
            defaults to 8080.
    """

    port: int = proto.Field(
        proto.INT32,
        number=1,
    )


class GRPCAction(proto.Message):
    r"""GRPCAction describes an action involving a GRPC port.

    Attributes:
        port (int):
            Port number of the gRPC service. Number must
            be in the range 1 to 65535. If not specified,
            defaults to 8080.
        service (str):
            Service is the name of the service to place
            in the gRPC HealthCheckRequest (see
            https://github.com/grpc/grpc/blob/master/doc/health-checking.md).
            If this is not specified, the default behavior
            is defined by gRPC.
    """

    port: int = proto.Field(
        proto.INT32,
        number=1,
    )
    service: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))

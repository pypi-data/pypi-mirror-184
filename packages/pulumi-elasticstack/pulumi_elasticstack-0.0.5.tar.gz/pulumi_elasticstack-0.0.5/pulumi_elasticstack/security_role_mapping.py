# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['SecurityRoleMappingArgs', 'SecurityRoleMapping']

@pulumi.input_type
class SecurityRoleMappingArgs:
    def __init__(__self__, *,
                 rules: pulumi.Input[str],
                 elasticsearch_connection: Optional[pulumi.Input['SecurityRoleMappingElasticsearchConnectionArgs']] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 metadata: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 role_templates: Optional[pulumi.Input[str]] = None,
                 roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a SecurityRoleMapping resource.
        :param pulumi.Input[str] rules: The rules that determine which users should be matched by the mapping. A rule is a logical condition that is expressed by using a JSON DSL.
        :param pulumi.Input['SecurityRoleMappingElasticsearchConnectionArgs'] elasticsearch_connection: Elasticsearch connection configuration block.
        :param pulumi.Input[bool] enabled: Mappings that have `enabled` set to `false` are ignored when role mapping is performed.
        :param pulumi.Input[str] metadata: Additional metadata that helps define which roles are assigned to each user. Keys beginning with `_` are reserved for system usage.
        :param pulumi.Input[str] name: The distinct name that identifies the role mapping, used solely as an identifier.
        :param pulumi.Input[str] role_templates: A list of mustache templates that will be evaluated to determine the roles names that should granted to the users that match the role mapping rules.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] roles: A list of role names that are granted to the users that match the role mapping rules.
        """
        pulumi.set(__self__, "rules", rules)
        if elasticsearch_connection is not None:
            pulumi.set(__self__, "elasticsearch_connection", elasticsearch_connection)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if role_templates is not None:
            pulumi.set(__self__, "role_templates", role_templates)
        if roles is not None:
            pulumi.set(__self__, "roles", roles)

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Input[str]:
        """
        The rules that determine which users should be matched by the mapping. A rule is a logical condition that is expressed by using a JSON DSL.
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: pulumi.Input[str]):
        pulumi.set(self, "rules", value)

    @property
    @pulumi.getter(name="elasticsearchConnection")
    def elasticsearch_connection(self) -> Optional[pulumi.Input['SecurityRoleMappingElasticsearchConnectionArgs']]:
        """
        Elasticsearch connection configuration block.
        """
        return pulumi.get(self, "elasticsearch_connection")

    @elasticsearch_connection.setter
    def elasticsearch_connection(self, value: Optional[pulumi.Input['SecurityRoleMappingElasticsearchConnectionArgs']]):
        pulumi.set(self, "elasticsearch_connection", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Mappings that have `enabled` set to `false` are ignored when role mapping is performed.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[str]]:
        """
        Additional metadata that helps define which roles are assigned to each user. Keys beginning with `_` are reserved for system usage.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The distinct name that identifies the role mapping, used solely as an identifier.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="roleTemplates")
    def role_templates(self) -> Optional[pulumi.Input[str]]:
        """
        A list of mustache templates that will be evaluated to determine the roles names that should granted to the users that match the role mapping rules.
        """
        return pulumi.get(self, "role_templates")

    @role_templates.setter
    def role_templates(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role_templates", value)

    @property
    @pulumi.getter
    def roles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of role names that are granted to the users that match the role mapping rules.
        """
        return pulumi.get(self, "roles")

    @roles.setter
    def roles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "roles", value)


@pulumi.input_type
class _SecurityRoleMappingState:
    def __init__(__self__, *,
                 elasticsearch_connection: Optional[pulumi.Input['SecurityRoleMappingElasticsearchConnectionArgs']] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 metadata: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 role_templates: Optional[pulumi.Input[str]] = None,
                 roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 rules: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SecurityRoleMapping resources.
        :param pulumi.Input['SecurityRoleMappingElasticsearchConnectionArgs'] elasticsearch_connection: Elasticsearch connection configuration block.
        :param pulumi.Input[bool] enabled: Mappings that have `enabled` set to `false` are ignored when role mapping is performed.
        :param pulumi.Input[str] metadata: Additional metadata that helps define which roles are assigned to each user. Keys beginning with `_` are reserved for system usage.
        :param pulumi.Input[str] name: The distinct name that identifies the role mapping, used solely as an identifier.
        :param pulumi.Input[str] role_templates: A list of mustache templates that will be evaluated to determine the roles names that should granted to the users that match the role mapping rules.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] roles: A list of role names that are granted to the users that match the role mapping rules.
        :param pulumi.Input[str] rules: The rules that determine which users should be matched by the mapping. A rule is a logical condition that is expressed by using a JSON DSL.
        """
        if elasticsearch_connection is not None:
            pulumi.set(__self__, "elasticsearch_connection", elasticsearch_connection)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if role_templates is not None:
            pulumi.set(__self__, "role_templates", role_templates)
        if roles is not None:
            pulumi.set(__self__, "roles", roles)
        if rules is not None:
            pulumi.set(__self__, "rules", rules)

    @property
    @pulumi.getter(name="elasticsearchConnection")
    def elasticsearch_connection(self) -> Optional[pulumi.Input['SecurityRoleMappingElasticsearchConnectionArgs']]:
        """
        Elasticsearch connection configuration block.
        """
        return pulumi.get(self, "elasticsearch_connection")

    @elasticsearch_connection.setter
    def elasticsearch_connection(self, value: Optional[pulumi.Input['SecurityRoleMappingElasticsearchConnectionArgs']]):
        pulumi.set(self, "elasticsearch_connection", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Mappings that have `enabled` set to `false` are ignored when role mapping is performed.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[str]]:
        """
        Additional metadata that helps define which roles are assigned to each user. Keys beginning with `_` are reserved for system usage.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The distinct name that identifies the role mapping, used solely as an identifier.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="roleTemplates")
    def role_templates(self) -> Optional[pulumi.Input[str]]:
        """
        A list of mustache templates that will be evaluated to determine the roles names that should granted to the users that match the role mapping rules.
        """
        return pulumi.get(self, "role_templates")

    @role_templates.setter
    def role_templates(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role_templates", value)

    @property
    @pulumi.getter
    def roles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of role names that are granted to the users that match the role mapping rules.
        """
        return pulumi.get(self, "roles")

    @roles.setter
    def roles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "roles", value)

    @property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[str]]:
        """
        The rules that determine which users should be matched by the mapping. A rule is a logical condition that is expressed by using a JSON DSL.
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rules", value)


class SecurityRoleMapping(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 elasticsearch_connection: Optional[pulumi.Input[pulumi.InputType['SecurityRoleMappingElasticsearchConnectionArgs']]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 metadata: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 role_templates: Optional[pulumi.Input[str]] = None,
                 roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 rules: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manage role mappings. See, https://www.elastic.co/guide/en/elasticsearch/reference/current/security-api-put-role-mapping.html

        ## Example Usage

        ```python
        import pulumi
        import json
        import pulumi_elasticstack as elasticstack

        example = elasticstack.SecurityRoleMapping("example",
            enabled=True,
            roles=["admin"],
            rules=json.dumps({
                "any": [
                    {
                        "field": {
                            "username": "esadmin",
                        },
                    },
                    {
                        "field": {
                            "groups": "cn=admins,dc=example,dc=com",
                        },
                    },
                ],
            }))
        pulumi.export("role", example.name)
        ```

        ## Import

        ```sh
         $ pulumi import elasticstack:index/securityRoleMapping:SecurityRoleMapping my_role_mapping <cluster_uuid>/<role mapping name>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['SecurityRoleMappingElasticsearchConnectionArgs']] elasticsearch_connection: Elasticsearch connection configuration block.
        :param pulumi.Input[bool] enabled: Mappings that have `enabled` set to `false` are ignored when role mapping is performed.
        :param pulumi.Input[str] metadata: Additional metadata that helps define which roles are assigned to each user. Keys beginning with `_` are reserved for system usage.
        :param pulumi.Input[str] name: The distinct name that identifies the role mapping, used solely as an identifier.
        :param pulumi.Input[str] role_templates: A list of mustache templates that will be evaluated to determine the roles names that should granted to the users that match the role mapping rules.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] roles: A list of role names that are granted to the users that match the role mapping rules.
        :param pulumi.Input[str] rules: The rules that determine which users should be matched by the mapping. A rule is a logical condition that is expressed by using a JSON DSL.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SecurityRoleMappingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manage role mappings. See, https://www.elastic.co/guide/en/elasticsearch/reference/current/security-api-put-role-mapping.html

        ## Example Usage

        ```python
        import pulumi
        import json
        import pulumi_elasticstack as elasticstack

        example = elasticstack.SecurityRoleMapping("example",
            enabled=True,
            roles=["admin"],
            rules=json.dumps({
                "any": [
                    {
                        "field": {
                            "username": "esadmin",
                        },
                    },
                    {
                        "field": {
                            "groups": "cn=admins,dc=example,dc=com",
                        },
                    },
                ],
            }))
        pulumi.export("role", example.name)
        ```

        ## Import

        ```sh
         $ pulumi import elasticstack:index/securityRoleMapping:SecurityRoleMapping my_role_mapping <cluster_uuid>/<role mapping name>
        ```

        :param str resource_name: The name of the resource.
        :param SecurityRoleMappingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SecurityRoleMappingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 elasticsearch_connection: Optional[pulumi.Input[pulumi.InputType['SecurityRoleMappingElasticsearchConnectionArgs']]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 metadata: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 role_templates: Optional[pulumi.Input[str]] = None,
                 roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 rules: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SecurityRoleMappingArgs.__new__(SecurityRoleMappingArgs)

            __props__.__dict__["elasticsearch_connection"] = elasticsearch_connection
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["metadata"] = metadata
            __props__.__dict__["name"] = name
            __props__.__dict__["role_templates"] = role_templates
            __props__.__dict__["roles"] = roles
            if rules is None and not opts.urn:
                raise TypeError("Missing required property 'rules'")
            __props__.__dict__["rules"] = rules
        super(SecurityRoleMapping, __self__).__init__(
            'elasticstack:index/securityRoleMapping:SecurityRoleMapping',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            elasticsearch_connection: Optional[pulumi.Input[pulumi.InputType['SecurityRoleMappingElasticsearchConnectionArgs']]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            metadata: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            role_templates: Optional[pulumi.Input[str]] = None,
            roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            rules: Optional[pulumi.Input[str]] = None) -> 'SecurityRoleMapping':
        """
        Get an existing SecurityRoleMapping resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['SecurityRoleMappingElasticsearchConnectionArgs']] elasticsearch_connection: Elasticsearch connection configuration block.
        :param pulumi.Input[bool] enabled: Mappings that have `enabled` set to `false` are ignored when role mapping is performed.
        :param pulumi.Input[str] metadata: Additional metadata that helps define which roles are assigned to each user. Keys beginning with `_` are reserved for system usage.
        :param pulumi.Input[str] name: The distinct name that identifies the role mapping, used solely as an identifier.
        :param pulumi.Input[str] role_templates: A list of mustache templates that will be evaluated to determine the roles names that should granted to the users that match the role mapping rules.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] roles: A list of role names that are granted to the users that match the role mapping rules.
        :param pulumi.Input[str] rules: The rules that determine which users should be matched by the mapping. A rule is a logical condition that is expressed by using a JSON DSL.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SecurityRoleMappingState.__new__(_SecurityRoleMappingState)

        __props__.__dict__["elasticsearch_connection"] = elasticsearch_connection
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["metadata"] = metadata
        __props__.__dict__["name"] = name
        __props__.__dict__["role_templates"] = role_templates
        __props__.__dict__["roles"] = roles
        __props__.__dict__["rules"] = rules
        return SecurityRoleMapping(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="elasticsearchConnection")
    def elasticsearch_connection(self) -> pulumi.Output[Optional['outputs.SecurityRoleMappingElasticsearchConnection']]:
        """
        Elasticsearch connection configuration block.
        """
        return pulumi.get(self, "elasticsearch_connection")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Mappings that have `enabled` set to `false` are ignored when role mapping is performed.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[str]]:
        """
        Additional metadata that helps define which roles are assigned to each user. Keys beginning with `_` are reserved for system usage.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The distinct name that identifies the role mapping, used solely as an identifier.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="roleTemplates")
    def role_templates(self) -> pulumi.Output[Optional[str]]:
        """
        A list of mustache templates that will be evaluated to determine the roles names that should granted to the users that match the role mapping rules.
        """
        return pulumi.get(self, "role_templates")

    @property
    @pulumi.getter
    def roles(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of role names that are granted to the users that match the role mapping rules.
        """
        return pulumi.get(self, "roles")

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Output[str]:
        """
        The rules that determine which users should be matched by the mapping. A rule is a logical condition that is expressed by using a JSON DSL.
        """
        return pulumi.get(self, "rules")


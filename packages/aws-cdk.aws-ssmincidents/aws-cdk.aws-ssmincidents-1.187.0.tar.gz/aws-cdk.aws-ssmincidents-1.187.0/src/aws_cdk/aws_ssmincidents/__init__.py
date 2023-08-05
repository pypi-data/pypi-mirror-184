'''
# AWS::SSMIncidents Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_ssmincidents as ssmincidents
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for SSMIncidents construct libraries](https://constructs.dev/search?q=ssmincidents)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::SSMIncidents resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SSMIncidents.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::SSMIncidents](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SSMIncidents.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/master/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ._jsii import *

import aws_cdk.core as _aws_cdk_core_f4b25747


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnReplicationSet(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-ssmincidents.CfnReplicationSet",
):
    '''A CloudFormation ``AWS::SSMIncidents::ReplicationSet``.

    The ``AWS::SSMIncidents::ReplicationSet`` resource specifies a set of Regions that Incident Manager data is replicated to and the KMS key used to encrypt the data.

    :cloudformationResource: AWS::SSMIncidents::ReplicationSet
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-replicationset.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_ssmincidents as ssmincidents
        
        cfn_replication_set = ssmincidents.CfnReplicationSet(self, "MyCfnReplicationSet",
            regions=[ssmincidents.CfnReplicationSet.ReplicationRegionProperty(
                region_configuration=ssmincidents.CfnReplicationSet.RegionConfigurationProperty(
                    sse_kms_key_id="sseKmsKeyId"
                ),
                region_name="regionName"
            )],
        
            # the properties below are optional
            deletion_protected=False,
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        regions: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[typing.Union["CfnReplicationSet.ReplicationRegionProperty", typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable]]],
        deletion_protected: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::SSMIncidents::ReplicationSet``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param regions: Specifies the Regions of the replication set.
        :param deletion_protected: Determines if the replication set deletion protection is enabled or not. If deletion protection is enabled, you can't delete the last Region in the replication set.
        :param tags: ``AWS::SSMIncidents::ReplicationSet.Tags``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c4a5f2015ac0fcdd0216a42b439aa534bcff1514191a1248defc16a8442009b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnReplicationSetProps(
            regions=regions, deletion_protected=deletion_protected, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9061e36eaa63fa8ca490b30ac6a69acb29016ee87b286a7987748d2e951a647f)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b658c3b4ad8566fac72cebe2eb7bee4207efd64cddb9a0454c9d9183203f372)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _aws_cdk_core_f4b25747.TagManager:
        '''``AWS::SSMIncidents::ReplicationSet.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-replicationset.html#cfn-ssmincidents-replicationset-tags
        '''
        return typing.cast(_aws_cdk_core_f4b25747.TagManager, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="regions")
    def regions(
        self,
    ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union["CfnReplicationSet.ReplicationRegionProperty", _aws_cdk_core_f4b25747.IResolvable]]]:
        '''Specifies the Regions of the replication set.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-replicationset.html#cfn-ssmincidents-replicationset-regions
        '''
        return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union["CfnReplicationSet.ReplicationRegionProperty", _aws_cdk_core_f4b25747.IResolvable]]], jsii.get(self, "regions"))

    @regions.setter
    def regions(
        self,
        value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union["CfnReplicationSet.ReplicationRegionProperty", _aws_cdk_core_f4b25747.IResolvable]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a06fad9d66ac04a548a402b41ec087f43956b3ab1077eb0835b75bd0e560573)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regions", value)

    @builtins.property
    @jsii.member(jsii_name="deletionProtected")
    def deletion_protected(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
        '''Determines if the replication set deletion protection is enabled or not.

        If deletion protection is enabled, you can't delete the last Region in the replication set.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-replicationset.html#cfn-ssmincidents-replicationset-deletionprotected
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], jsii.get(self, "deletionProtected"))

    @deletion_protected.setter
    def deletion_protected(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e30e3bde80aff73843e09e2a133a743088ad21ea17d18cdf4ee45fe61888b69a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deletionProtected", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-ssmincidents.CfnReplicationSet.RegionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"sse_kms_key_id": "sseKmsKeyId"},
    )
    class RegionConfigurationProperty:
        def __init__(self, *, sse_kms_key_id: builtins.str) -> None:
            '''The ``RegionConfiguration`` property specifies the Region and KMS key to add to the replication set.

            :param sse_kms_key_id: The KMS key ID to use to encrypt your replication set.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-replicationset-regionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_ssmincidents as ssmincidents
                
                region_configuration_property = ssmincidents.CfnReplicationSet.RegionConfigurationProperty(
                    sse_kms_key_id="sseKmsKeyId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0ac1937894930a47409413e821e2d32d6b04ccdf1c31d40fd440a0b4828fe733)
                check_type(argname="argument sse_kms_key_id", value=sse_kms_key_id, expected_type=type_hints["sse_kms_key_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "sse_kms_key_id": sse_kms_key_id,
            }

        @builtins.property
        def sse_kms_key_id(self) -> builtins.str:
            '''The KMS key ID to use to encrypt your replication set.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-replicationset-regionconfiguration.html#cfn-ssmincidents-replicationset-regionconfiguration-ssekmskeyid
            '''
            result = self._values.get("sse_kms_key_id")
            assert result is not None, "Required property 'sse_kms_key_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RegionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-ssmincidents.CfnReplicationSet.ReplicationRegionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "region_configuration": "regionConfiguration",
            "region_name": "regionName",
        },
    )
    class ReplicationRegionProperty:
        def __init__(
            self,
            *,
            region_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnReplicationSet.RegionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            region_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``ReplicationRegion`` property type specifies the Region and KMS key to add to the replication set.

            :param region_configuration: Specifies the Region configuration.
            :param region_name: Specifies the region name to add to the replication set.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-replicationset-replicationregion.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_ssmincidents as ssmincidents
                
                replication_region_property = ssmincidents.CfnReplicationSet.ReplicationRegionProperty(
                    region_configuration=ssmincidents.CfnReplicationSet.RegionConfigurationProperty(
                        sse_kms_key_id="sseKmsKeyId"
                    ),
                    region_name="regionName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4bfa4b992e76330396573d9b01bed98052f02975e53b371f19ce62879c4b9411)
                check_type(argname="argument region_configuration", value=region_configuration, expected_type=type_hints["region_configuration"])
                check_type(argname="argument region_name", value=region_name, expected_type=type_hints["region_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if region_configuration is not None:
                self._values["region_configuration"] = region_configuration
            if region_name is not None:
                self._values["region_name"] = region_name

        @builtins.property
        def region_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnReplicationSet.RegionConfigurationProperty"]]:
            '''Specifies the Region configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-replicationset-replicationregion.html#cfn-ssmincidents-replicationset-replicationregion-regionconfiguration
            '''
            result = self._values.get("region_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnReplicationSet.RegionConfigurationProperty"]], result)

        @builtins.property
        def region_name(self) -> typing.Optional[builtins.str]:
            '''Specifies the region name to add to the replication set.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-replicationset-replicationregion.html#cfn-ssmincidents-replicationset-replicationregion-regionname
            '''
            result = self._values.get("region_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ReplicationRegionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-ssmincidents.CfnReplicationSetProps",
    jsii_struct_bases=[],
    name_mapping={
        "regions": "regions",
        "deletion_protected": "deletionProtected",
        "tags": "tags",
    },
)
class CfnReplicationSetProps:
    def __init__(
        self,
        *,
        regions: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[typing.Union[CfnReplicationSet.ReplicationRegionProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable]]],
        deletion_protected: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnReplicationSet``.

        :param regions: Specifies the Regions of the replication set.
        :param deletion_protected: Determines if the replication set deletion protection is enabled or not. If deletion protection is enabled, you can't delete the last Region in the replication set.
        :param tags: ``AWS::SSMIncidents::ReplicationSet.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-replicationset.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_ssmincidents as ssmincidents
            
            cfn_replication_set_props = ssmincidents.CfnReplicationSetProps(
                regions=[ssmincidents.CfnReplicationSet.ReplicationRegionProperty(
                    region_configuration=ssmincidents.CfnReplicationSet.RegionConfigurationProperty(
                        sse_kms_key_id="sseKmsKeyId"
                    ),
                    region_name="regionName"
                )],
            
                # the properties below are optional
                deletion_protected=False,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c9ecebfbb55e497e146ca09196081a97de754c65ba375c7cbe762a9f3ab5e45)
            check_type(argname="argument regions", value=regions, expected_type=type_hints["regions"])
            check_type(argname="argument deletion_protected", value=deletion_protected, expected_type=type_hints["deletion_protected"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "regions": regions,
        }
        if deletion_protected is not None:
            self._values["deletion_protected"] = deletion_protected
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def regions(
        self,
    ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[CfnReplicationSet.ReplicationRegionProperty, _aws_cdk_core_f4b25747.IResolvable]]]:
        '''Specifies the Regions of the replication set.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-replicationset.html#cfn-ssmincidents-replicationset-regions
        '''
        result = self._values.get("regions")
        assert result is not None, "Required property 'regions' is missing"
        return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[CfnReplicationSet.ReplicationRegionProperty, _aws_cdk_core_f4b25747.IResolvable]]], result)

    @builtins.property
    def deletion_protected(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
        '''Determines if the replication set deletion protection is enabled or not.

        If deletion protection is enabled, you can't delete the last Region in the replication set.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-replicationset.html#cfn-ssmincidents-replicationset-deletionprotected
        '''
        result = self._values.get("deletion_protected")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]]:
        '''``AWS::SSMIncidents::ReplicationSet.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-replicationset.html#cfn-ssmincidents-replicationset-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnReplicationSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnResponsePlan(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-ssmincidents.CfnResponsePlan",
):
    '''A CloudFormation ``AWS::SSMIncidents::ResponsePlan``.

    The ``AWS::SSMIncidents::ResponsePlan`` resource specifies the details of the response plan that are used when creating an incident.

    :cloudformationResource: AWS::SSMIncidents::ResponsePlan
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_ssmincidents as ssmincidents
        
        cfn_response_plan = ssmincidents.CfnResponsePlan(self, "MyCfnResponsePlan",
            incident_template=ssmincidents.CfnResponsePlan.IncidentTemplateProperty(
                impact=123,
                title="title",
        
                # the properties below are optional
                dedupe_string="dedupeString",
                incident_tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                notification_targets=[ssmincidents.CfnResponsePlan.NotificationTargetItemProperty(
                    sns_topic_arn="snsTopicArn"
                )],
                summary="summary"
            ),
            name="name",
        
            # the properties below are optional
            actions=[ssmincidents.CfnResponsePlan.ActionProperty(
                ssm_automation=ssmincidents.CfnResponsePlan.SsmAutomationProperty(
                    document_name="documentName",
                    role_arn="roleArn",
        
                    # the properties below are optional
                    document_version="documentVersion",
                    dynamic_parameters=[ssmincidents.CfnResponsePlan.DynamicSsmParameterProperty(
                        key="key",
                        value=ssmincidents.CfnResponsePlan.DynamicSsmParameterValueProperty(
                            variable="variable"
                        )
                    )],
                    parameters=[ssmincidents.CfnResponsePlan.SsmParameterProperty(
                        key="key",
                        values=["values"]
                    )],
                    target_account="targetAccount"
                )
            )],
            chat_channel=ssmincidents.CfnResponsePlan.ChatChannelProperty(
                chatbot_sns=["chatbotSns"]
            ),
            display_name="displayName",
            engagements=["engagements"],
            integrations=[ssmincidents.CfnResponsePlan.IntegrationProperty(
                pager_duty_configuration=ssmincidents.CfnResponsePlan.PagerDutyConfigurationProperty(
                    name="name",
                    pager_duty_incident_configuration=ssmincidents.CfnResponsePlan.PagerDutyIncidentConfigurationProperty(
                        service_id="serviceId"
                    ),
                    secret_id="secretId"
                )
            )],
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        incident_template: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnResponsePlan.IncidentTemplateProperty", typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        actions: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnResponsePlan.ActionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        chat_channel: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnResponsePlan.ChatChannelProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        display_name: typing.Optional[builtins.str] = None,
        engagements: typing.Optional[typing.Sequence[builtins.str]] = None,
        integrations: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnResponsePlan.IntegrationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::SSMIncidents::ResponsePlan``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param incident_template: Details used to create an incident when using this response plan.
        :param name: The name of the response plan.
        :param actions: The actions that the response plan starts at the beginning of an incident.
        :param chat_channel: The AWS Chatbot chat channel used for collaboration during an incident.
        :param display_name: The human readable name of the response plan.
        :param engagements: The Amazon Resource Name (ARN) for the contacts and escalation plans that the response plan engages during an incident.
        :param integrations: Information about third-party services integrated into the response plan.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0d0141c81292b027e1db5c662b0e184e7cb6fe536bb7c8a227eac662cac08a1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnResponsePlanProps(
            incident_template=incident_template,
            name=name,
            actions=actions,
            chat_channel=chat_channel,
            display_name=display_name,
            engagements=engagements,
            integrations=integrations,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b7cae3159fe0acfb5f877134c9f89c57d234aac0ac24143b8bc868a18a63601)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1072dd039dde19ff08cddec253ad1244076f6052f31460b19d1c054d96c88ed2)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _aws_cdk_core_f4b25747.TagManager:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html#cfn-ssmincidents-responseplan-tags
        '''
        return typing.cast(_aws_cdk_core_f4b25747.TagManager, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="incidentTemplate")
    def incident_template(
        self,
    ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnResponsePlan.IncidentTemplateProperty"]:
        '''Details used to create an incident when using this response plan.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html#cfn-ssmincidents-responseplan-incidenttemplate
        '''
        return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnResponsePlan.IncidentTemplateProperty"], jsii.get(self, "incidentTemplate"))

    @incident_template.setter
    def incident_template(
        self,
        value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnResponsePlan.IncidentTemplateProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed501da644cb3215823c12d3af0887a518ac451e02026eb8e15762efda711dd8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "incidentTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the response plan.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html#cfn-ssmincidents-responseplan-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b63d22b9154ae185bcbaf816bec454af0589a0513e3603811d6fbe467896b226)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="actions")
    def actions(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnResponsePlan.ActionProperty"]]]]:
        '''The actions that the response plan starts at the beginning of an incident.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html#cfn-ssmincidents-responseplan-actions
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnResponsePlan.ActionProperty"]]]], jsii.get(self, "actions"))

    @actions.setter
    def actions(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnResponsePlan.ActionProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d7a3e799b753f6f4176f2ef8b58691a09067e1f167b79b9871927bdf80029a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actions", value)

    @builtins.property
    @jsii.member(jsii_name="chatChannel")
    def chat_channel(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnResponsePlan.ChatChannelProperty"]]:
        '''The AWS Chatbot chat channel used for collaboration during an incident.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html#cfn-ssmincidents-responseplan-chatchannel
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnResponsePlan.ChatChannelProperty"]], jsii.get(self, "chatChannel"))

    @chat_channel.setter
    def chat_channel(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnResponsePlan.ChatChannelProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db69a94996cb75583772a58f7530b3536616873f65993c6c89a5e9288b2163df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "chatChannel", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The human readable name of the response plan.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html#cfn-ssmincidents-responseplan-displayname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2b71ee8c671bb4dbd2f5406633596df83de3bf1dca505e5057d88ad254bb040)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="engagements")
    def engagements(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The Amazon Resource Name (ARN) for the contacts and escalation plans that the response plan engages during an incident.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html#cfn-ssmincidents-responseplan-engagements
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "engagements"))

    @engagements.setter
    def engagements(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__003e73c2c22d4ad8b35216ca99d3f5d999ea53a74b06e66f41511da5070f6fbf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engagements", value)

    @builtins.property
    @jsii.member(jsii_name="integrations")
    def integrations(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnResponsePlan.IntegrationProperty"]]]]:
        '''Information about third-party services integrated into the response plan.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html#cfn-ssmincidents-responseplan-integrations
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnResponsePlan.IntegrationProperty"]]]], jsii.get(self, "integrations"))

    @integrations.setter
    def integrations(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnResponsePlan.IntegrationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87c7ee6b48ceee79d7201bff261236f5f31ae9fc540494d401ecb76aeeb0e6a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "integrations", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-ssmincidents.CfnResponsePlan.ActionProperty",
        jsii_struct_bases=[],
        name_mapping={"ssm_automation": "ssmAutomation"},
    )
    class ActionProperty:
        def __init__(
            self,
            *,
            ssm_automation: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnResponsePlan.SsmAutomationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The ``Action`` property type specifies the configuration to launch.

            :param ssm_automation: Details about the Systems Manager automation document that will be used as a runbook during an incident.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-action.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_ssmincidents as ssmincidents
                
                action_property = ssmincidents.CfnResponsePlan.ActionProperty(
                    ssm_automation=ssmincidents.CfnResponsePlan.SsmAutomationProperty(
                        document_name="documentName",
                        role_arn="roleArn",
                
                        # the properties below are optional
                        document_version="documentVersion",
                        dynamic_parameters=[ssmincidents.CfnResponsePlan.DynamicSsmParameterProperty(
                            key="key",
                            value=ssmincidents.CfnResponsePlan.DynamicSsmParameterValueProperty(
                                variable="variable"
                            )
                        )],
                        parameters=[ssmincidents.CfnResponsePlan.SsmParameterProperty(
                            key="key",
                            values=["values"]
                        )],
                        target_account="targetAccount"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a150f6cdafa8eef83b6c947b195beceec74930628dda404ce33ca2f6d9342a8c)
                check_type(argname="argument ssm_automation", value=ssm_automation, expected_type=type_hints["ssm_automation"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ssm_automation is not None:
                self._values["ssm_automation"] = ssm_automation

        @builtins.property
        def ssm_automation(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnResponsePlan.SsmAutomationProperty"]]:
            '''Details about the Systems Manager automation document that will be used as a runbook during an incident.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-action.html#cfn-ssmincidents-responseplan-action-ssmautomation
            '''
            result = self._values.get("ssm_automation")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnResponsePlan.SsmAutomationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-ssmincidents.CfnResponsePlan.ChatChannelProperty",
        jsii_struct_bases=[],
        name_mapping={"chatbot_sns": "chatbotSns"},
    )
    class ChatChannelProperty:
        def __init__(
            self,
            *,
            chatbot_sns: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The AWS Chatbot chat channel used for collaboration during an incident.

            :param chatbot_sns: The SNS targets that AWS Chatbot uses to notify the chat channel of updates to an incident. You can also make updates to the incident through the chat channel by using the SNS topics

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-chatchannel.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_ssmincidents as ssmincidents
                
                chat_channel_property = ssmincidents.CfnResponsePlan.ChatChannelProperty(
                    chatbot_sns=["chatbotSns"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e08fec843c7f3a43b9b8dbe39acdad149d4c3c2aedd31731c815d53078cf2fd2)
                check_type(argname="argument chatbot_sns", value=chatbot_sns, expected_type=type_hints["chatbot_sns"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if chatbot_sns is not None:
                self._values["chatbot_sns"] = chatbot_sns

        @builtins.property
        def chatbot_sns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The SNS targets that AWS Chatbot uses to notify the chat channel of updates to an incident.

            You can also make updates to the incident through the chat channel by using the SNS topics

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-chatchannel.html#cfn-ssmincidents-responseplan-chatchannel-chatbotsns
            '''
            result = self._values.get("chatbot_sns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ChatChannelProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-ssmincidents.CfnResponsePlan.DynamicSsmParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class DynamicSsmParameterProperty:
        def __init__(
            self,
            *,
            key: builtins.str,
            value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnResponsePlan.DynamicSsmParameterValueProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''When you add a runbook to a response plan, you can specify the parameters the runbook should use at runtime.

            Response plans support parameters with both static and dynamic values. For static values, you enter the value when you define the parameter in the response plan. For dynamic values, the system determines the correct parameter value by collecting information from the incident. Incident Manager supports the following dynamic parameters:

            *Incident ARN*

            When Incident Manager creates an incident, the system captures the Amazon Resource Name (ARN) of the corresponding incident record and enters it for this parameter in the runbook.
            .. epigraph::

               This value can only be assigned to parameters of type ``String`` . If assigned to a parameter of any other type, the runbook fails to run.

            *Involved resources*

            When Incident Manager creates an incident, the system captures the ARNs of the resources involved in the incident. These resource ARNs are then assigned to this parameter in the runbook.
            .. epigraph::

               This value can only be assigned to parameters of type ``StringList`` . If assigned to a parameter of any other type, the runbook fails to run.

            :param key: The key parameter to use when running the Systems Manager Automation runbook.
            :param value: The dynamic parameter value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-dynamicssmparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_ssmincidents as ssmincidents
                
                dynamic_ssm_parameter_property = ssmincidents.CfnResponsePlan.DynamicSsmParameterProperty(
                    key="key",
                    value=ssmincidents.CfnResponsePlan.DynamicSsmParameterValueProperty(
                        variable="variable"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__55fa9def59d6bb1736c01bb99f9e1093fe280cedd9ddd1c1558e6fdb1dbc0ee1)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''The key parameter to use when running the Systems Manager Automation runbook.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-dynamicssmparameter.html#cfn-ssmincidents-responseplan-dynamicssmparameter-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(
            self,
        ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnResponsePlan.DynamicSsmParameterValueProperty"]:
            '''The dynamic parameter value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-dynamicssmparameter.html#cfn-ssmincidents-responseplan-dynamicssmparameter-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnResponsePlan.DynamicSsmParameterValueProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DynamicSsmParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-ssmincidents.CfnResponsePlan.DynamicSsmParameterValueProperty",
        jsii_struct_bases=[],
        name_mapping={"variable": "variable"},
    )
    class DynamicSsmParameterValueProperty:
        def __init__(self, *, variable: typing.Optional[builtins.str] = None) -> None:
            '''The dynamic parameter value.

            :param variable: Variable dynamic parameters. A parameter value is determined when an incident is created.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-dynamicssmparametervalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_ssmincidents as ssmincidents
                
                dynamic_ssm_parameter_value_property = ssmincidents.CfnResponsePlan.DynamicSsmParameterValueProperty(
                    variable="variable"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5cd67bb9afc755d4968a737bc00946cb474aca90cb98caec4468e21f3ca629e3)
                check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if variable is not None:
                self._values["variable"] = variable

        @builtins.property
        def variable(self) -> typing.Optional[builtins.str]:
            '''Variable dynamic parameters.

            A parameter value is determined when an incident is created.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-dynamicssmparametervalue.html#cfn-ssmincidents-responseplan-dynamicssmparametervalue-variable
            '''
            result = self._values.get("variable")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DynamicSsmParameterValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-ssmincidents.CfnResponsePlan.IncidentTemplateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "impact": "impact",
            "title": "title",
            "dedupe_string": "dedupeString",
            "incident_tags": "incidentTags",
            "notification_targets": "notificationTargets",
            "summary": "summary",
        },
    )
    class IncidentTemplateProperty:
        def __init__(
            self,
            *,
            impact: jsii.Number,
            title: builtins.str,
            dedupe_string: typing.Optional[builtins.str] = None,
            incident_tags: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]]]] = None,
            notification_targets: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnResponsePlan.NotificationTargetItemProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            summary: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``IncidentTemplate`` property type specifies details used to create an incident when using this response plan.

            :param impact: Defines the impact to the customers. Providing an impact overwrites the impact provided by a response plan. **Possible impacts:** - ``1`` - Critical impact, this typically relates to full application failure that impacts many to all customers. - ``2`` - High impact, partial application failure with impact to many customers. - ``3`` - Medium impact, the application is providing reduced service to customers. - ``4`` - Low impact, customer might aren't impacted by the problem yet. - ``5`` - No impact, customers aren't currently impacted but urgent action is needed to avoid impact.
            :param title: The title of the incident is a brief and easily recognizable.
            :param dedupe_string: Used to create only one incident record for an incident.
            :param incident_tags: Tags to assign to the template. When the ``StartIncident`` API action is called, Incident Manager assigns the tags specified in the template to the incident.
            :param notification_targets: The SNS targets that AWS Chatbot uses to notify the chat channel of updates to an incident. You can also make updates to the incident through the chat channel using the SNS topics.
            :param summary: The summary describes what has happened during the incident.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-incidenttemplate.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_ssmincidents as ssmincidents
                
                incident_template_property = ssmincidents.CfnResponsePlan.IncidentTemplateProperty(
                    impact=123,
                    title="title",
                
                    # the properties below are optional
                    dedupe_string="dedupeString",
                    incident_tags=[CfnTag(
                        key="key",
                        value="value"
                    )],
                    notification_targets=[ssmincidents.CfnResponsePlan.NotificationTargetItemProperty(
                        sns_topic_arn="snsTopicArn"
                    )],
                    summary="summary"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1cdd0deb991ca23b1dd1b146169956ee19358324d31f46343c8021fed8772499)
                check_type(argname="argument impact", value=impact, expected_type=type_hints["impact"])
                check_type(argname="argument title", value=title, expected_type=type_hints["title"])
                check_type(argname="argument dedupe_string", value=dedupe_string, expected_type=type_hints["dedupe_string"])
                check_type(argname="argument incident_tags", value=incident_tags, expected_type=type_hints["incident_tags"])
                check_type(argname="argument notification_targets", value=notification_targets, expected_type=type_hints["notification_targets"])
                check_type(argname="argument summary", value=summary, expected_type=type_hints["summary"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "impact": impact,
                "title": title,
            }
            if dedupe_string is not None:
                self._values["dedupe_string"] = dedupe_string
            if incident_tags is not None:
                self._values["incident_tags"] = incident_tags
            if notification_targets is not None:
                self._values["notification_targets"] = notification_targets
            if summary is not None:
                self._values["summary"] = summary

        @builtins.property
        def impact(self) -> jsii.Number:
            '''Defines the impact to the customers. Providing an impact overwrites the impact provided by a response plan.

            **Possible impacts:** - ``1`` - Critical impact, this typically relates to full application failure that impacts many to all customers.

            - ``2`` - High impact, partial application failure with impact to many customers.
            - ``3`` - Medium impact, the application is providing reduced service to customers.
            - ``4`` - Low impact, customer might aren't impacted by the problem yet.
            - ``5`` - No impact, customers aren't currently impacted but urgent action is needed to avoid impact.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-incidenttemplate.html#cfn-ssmincidents-responseplan-incidenttemplate-impact
            '''
            result = self._values.get("impact")
            assert result is not None, "Required property 'impact' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def title(self) -> builtins.str:
            '''The title of the incident is a brief and easily recognizable.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-incidenttemplate.html#cfn-ssmincidents-responseplan-incidenttemplate-title
            '''
            result = self._values.get("title")
            assert result is not None, "Required property 'title' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def dedupe_string(self) -> typing.Optional[builtins.str]:
            '''Used to create only one incident record for an incident.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-incidenttemplate.html#cfn-ssmincidents-responseplan-incidenttemplate-dedupestring
            '''
            result = self._values.get("dedupe_string")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def incident_tags(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, _aws_cdk_core_f4b25747.CfnTag]]]]:
            '''Tags to assign to the template.

            When the ``StartIncident`` API action is called, Incident Manager assigns the tags specified in the template to the incident.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-incidenttemplate.html#cfn-ssmincidents-responseplan-incidenttemplate-incidenttags
            '''
            result = self._values.get("incident_tags")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, _aws_cdk_core_f4b25747.CfnTag]]]], result)

        @builtins.property
        def notification_targets(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnResponsePlan.NotificationTargetItemProperty"]]]]:
            '''The SNS targets that AWS Chatbot uses to notify the chat channel of updates to an incident.

            You can also make updates to the incident through the chat channel using the SNS topics.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-incidenttemplate.html#cfn-ssmincidents-responseplan-incidenttemplate-notificationtargets
            '''
            result = self._values.get("notification_targets")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnResponsePlan.NotificationTargetItemProperty"]]]], result)

        @builtins.property
        def summary(self) -> typing.Optional[builtins.str]:
            '''The summary describes what has happened during the incident.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-incidenttemplate.html#cfn-ssmincidents-responseplan-incidenttemplate-summary
            '''
            result = self._values.get("summary")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IncidentTemplateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-ssmincidents.CfnResponsePlan.IntegrationProperty",
        jsii_struct_bases=[],
        name_mapping={"pager_duty_configuration": "pagerDutyConfiguration"},
    )
    class IntegrationProperty:
        def __init__(
            self,
            *,
            pager_duty_configuration: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnResponsePlan.PagerDutyConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Information about third-party services integrated into a response plan.

            :param pager_duty_configuration: Information about the PagerDuty service where the response plan creates an incident.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-integration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_ssmincidents as ssmincidents
                
                integration_property = ssmincidents.CfnResponsePlan.IntegrationProperty(
                    pager_duty_configuration=ssmincidents.CfnResponsePlan.PagerDutyConfigurationProperty(
                        name="name",
                        pager_duty_incident_configuration=ssmincidents.CfnResponsePlan.PagerDutyIncidentConfigurationProperty(
                            service_id="serviceId"
                        ),
                        secret_id="secretId"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ed50bcc40d436ba4d38c4dd77f3cf2523401f732eb3724860d85f13ec49cfa88)
                check_type(argname="argument pager_duty_configuration", value=pager_duty_configuration, expected_type=type_hints["pager_duty_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "pager_duty_configuration": pager_duty_configuration,
            }

        @builtins.property
        def pager_duty_configuration(
            self,
        ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnResponsePlan.PagerDutyConfigurationProperty"]:
            '''Information about the PagerDuty service where the response plan creates an incident.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-integration.html#cfn-ssmincidents-responseplan-integration-pagerdutyconfiguration
            '''
            result = self._values.get("pager_duty_configuration")
            assert result is not None, "Required property 'pager_duty_configuration' is missing"
            return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnResponsePlan.PagerDutyConfigurationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IntegrationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-ssmincidents.CfnResponsePlan.NotificationTargetItemProperty",
        jsii_struct_bases=[],
        name_mapping={"sns_topic_arn": "snsTopicArn"},
    )
    class NotificationTargetItemProperty:
        def __init__(
            self,
            *,
            sns_topic_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The SNS topic that's used by AWS Chatbot to notify the incidents chat channel.

            :param sns_topic_arn: The Amazon Resource Name (ARN) of the SNS topic.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-notificationtargetitem.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_ssmincidents as ssmincidents
                
                notification_target_item_property = ssmincidents.CfnResponsePlan.NotificationTargetItemProperty(
                    sns_topic_arn="snsTopicArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fd903433ca07ba7faa203fbd116a6666def684244587c10b1468c86cbda88f55)
                check_type(argname="argument sns_topic_arn", value=sns_topic_arn, expected_type=type_hints["sns_topic_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if sns_topic_arn is not None:
                self._values["sns_topic_arn"] = sns_topic_arn

        @builtins.property
        def sns_topic_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the SNS topic.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-notificationtargetitem.html#cfn-ssmincidents-responseplan-notificationtargetitem-snstopicarn
            '''
            result = self._values.get("sns_topic_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NotificationTargetItemProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-ssmincidents.CfnResponsePlan.PagerDutyConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "pager_duty_incident_configuration": "pagerDutyIncidentConfiguration",
            "secret_id": "secretId",
        },
    )
    class PagerDutyConfigurationProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            pager_duty_incident_configuration: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnResponsePlan.PagerDutyIncidentConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            secret_id: builtins.str,
        ) -> None:
            '''Details about the PagerDuty configuration for a response plan.

            :param name: The name of the PagerDuty configuration.
            :param pager_duty_incident_configuration: Details about the PagerDuty service associated with the configuration.
            :param secret_id: The ID of the AWS Secrets Manager secret that stores your PagerDuty key, either a General Access REST API Key or User Token REST API Key, and other user credentials.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-pagerdutyconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_ssmincidents as ssmincidents
                
                pager_duty_configuration_property = ssmincidents.CfnResponsePlan.PagerDutyConfigurationProperty(
                    name="name",
                    pager_duty_incident_configuration=ssmincidents.CfnResponsePlan.PagerDutyIncidentConfigurationProperty(
                        service_id="serviceId"
                    ),
                    secret_id="secretId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7d73662b06fad341e8372f7fdaad154428c00f3f94048013671b28078c9e335b)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument pager_duty_incident_configuration", value=pager_duty_incident_configuration, expected_type=type_hints["pager_duty_incident_configuration"])
                check_type(argname="argument secret_id", value=secret_id, expected_type=type_hints["secret_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "pager_duty_incident_configuration": pager_duty_incident_configuration,
                "secret_id": secret_id,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the PagerDuty configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-pagerdutyconfiguration.html#cfn-ssmincidents-responseplan-pagerdutyconfiguration-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def pager_duty_incident_configuration(
            self,
        ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnResponsePlan.PagerDutyIncidentConfigurationProperty"]:
            '''Details about the PagerDuty service associated with the configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-pagerdutyconfiguration.html#cfn-ssmincidents-responseplan-pagerdutyconfiguration-pagerdutyincidentconfiguration
            '''
            result = self._values.get("pager_duty_incident_configuration")
            assert result is not None, "Required property 'pager_duty_incident_configuration' is missing"
            return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnResponsePlan.PagerDutyIncidentConfigurationProperty"], result)

        @builtins.property
        def secret_id(self) -> builtins.str:
            '''The ID of the AWS Secrets Manager secret that stores your PagerDuty key, either a General Access REST API Key or User Token REST API Key, and other user credentials.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-pagerdutyconfiguration.html#cfn-ssmincidents-responseplan-pagerdutyconfiguration-secretid
            '''
            result = self._values.get("secret_id")
            assert result is not None, "Required property 'secret_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PagerDutyConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-ssmincidents.CfnResponsePlan.PagerDutyIncidentConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"service_id": "serviceId"},
    )
    class PagerDutyIncidentConfigurationProperty:
        def __init__(self, *, service_id: builtins.str) -> None:
            '''
            :param service_id: The ID of the PagerDuty service that the response plan associates with an incident when it launches.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-pagerdutyincidentconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_ssmincidents as ssmincidents
                
                pager_duty_incident_configuration_property = ssmincidents.CfnResponsePlan.PagerDutyIncidentConfigurationProperty(
                    service_id="serviceId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a095c37d3be492022157b2a1bfc759f1ee4c2747f74f44cdceaad0f3a41d1607)
                check_type(argname="argument service_id", value=service_id, expected_type=type_hints["service_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "service_id": service_id,
            }

        @builtins.property
        def service_id(self) -> builtins.str:
            '''The ID of the PagerDuty service that the response plan associates with an incident when it launches.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-pagerdutyincidentconfiguration.html#cfn-ssmincidents-responseplan-pagerdutyincidentconfiguration-serviceid
            '''
            result = self._values.get("service_id")
            assert result is not None, "Required property 'service_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PagerDutyIncidentConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-ssmincidents.CfnResponsePlan.SsmAutomationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "document_name": "documentName",
            "role_arn": "roleArn",
            "document_version": "documentVersion",
            "dynamic_parameters": "dynamicParameters",
            "parameters": "parameters",
            "target_account": "targetAccount",
        },
    )
    class SsmAutomationProperty:
        def __init__(
            self,
            *,
            document_name: builtins.str,
            role_arn: builtins.str,
            document_version: typing.Optional[builtins.str] = None,
            dynamic_parameters: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnResponsePlan.DynamicSsmParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            parameters: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnResponsePlan.SsmParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            target_account: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``SsmAutomation`` property type specifies details about the Systems Manager automation document that will be used as a runbook during an incident.

            :param document_name: The automation document's name.
            :param role_arn: The Amazon Resource Name (ARN) of the role that the automation document will assume when running commands.
            :param document_version: The automation document's version to use when running.
            :param dynamic_parameters: The key-value pairs to resolve dynamic parameter values when processing a Systems Manager Automation runbook.
            :param parameters: The key-value pair parameters to use when running the automation document.
            :param target_account: The account that the automation document will be run in. This can be in either the management account or an application account.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-ssmautomation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_ssmincidents as ssmincidents
                
                ssm_automation_property = ssmincidents.CfnResponsePlan.SsmAutomationProperty(
                    document_name="documentName",
                    role_arn="roleArn",
                
                    # the properties below are optional
                    document_version="documentVersion",
                    dynamic_parameters=[ssmincidents.CfnResponsePlan.DynamicSsmParameterProperty(
                        key="key",
                        value=ssmincidents.CfnResponsePlan.DynamicSsmParameterValueProperty(
                            variable="variable"
                        )
                    )],
                    parameters=[ssmincidents.CfnResponsePlan.SsmParameterProperty(
                        key="key",
                        values=["values"]
                    )],
                    target_account="targetAccount"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7764d012dd61df480423dd2b2519aa4998ec311d7ccabbee5dde21f2462a716c)
                check_type(argname="argument document_name", value=document_name, expected_type=type_hints["document_name"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument document_version", value=document_version, expected_type=type_hints["document_version"])
                check_type(argname="argument dynamic_parameters", value=dynamic_parameters, expected_type=type_hints["dynamic_parameters"])
                check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
                check_type(argname="argument target_account", value=target_account, expected_type=type_hints["target_account"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "document_name": document_name,
                "role_arn": role_arn,
            }
            if document_version is not None:
                self._values["document_version"] = document_version
            if dynamic_parameters is not None:
                self._values["dynamic_parameters"] = dynamic_parameters
            if parameters is not None:
                self._values["parameters"] = parameters
            if target_account is not None:
                self._values["target_account"] = target_account

        @builtins.property
        def document_name(self) -> builtins.str:
            '''The automation document's name.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-ssmautomation.html#cfn-ssmincidents-responseplan-ssmautomation-documentname
            '''
            result = self._values.get("document_name")
            assert result is not None, "Required property 'document_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the role that the automation document will assume when running commands.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-ssmautomation.html#cfn-ssmincidents-responseplan-ssmautomation-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def document_version(self) -> typing.Optional[builtins.str]:
            '''The automation document's version to use when running.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-ssmautomation.html#cfn-ssmincidents-responseplan-ssmautomation-documentversion
            '''
            result = self._values.get("document_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def dynamic_parameters(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnResponsePlan.DynamicSsmParameterProperty"]]]]:
            '''The key-value pairs to resolve dynamic parameter values when processing a Systems Manager Automation runbook.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-ssmautomation.html#cfn-ssmincidents-responseplan-ssmautomation-dynamicparameters
            '''
            result = self._values.get("dynamic_parameters")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnResponsePlan.DynamicSsmParameterProperty"]]]], result)

        @builtins.property
        def parameters(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnResponsePlan.SsmParameterProperty"]]]]:
            '''The key-value pair parameters to use when running the automation document.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-ssmautomation.html#cfn-ssmincidents-responseplan-ssmautomation-parameters
            '''
            result = self._values.get("parameters")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnResponsePlan.SsmParameterProperty"]]]], result)

        @builtins.property
        def target_account(self) -> typing.Optional[builtins.str]:
            '''The account that the automation document will be run in.

            This can be in either the management account or an application account.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-ssmautomation.html#cfn-ssmincidents-responseplan-ssmautomation-targetaccount
            '''
            result = self._values.get("target_account")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SsmAutomationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-ssmincidents.CfnResponsePlan.SsmParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "values": "values"},
    )
    class SsmParameterProperty:
        def __init__(
            self,
            *,
            key: builtins.str,
            values: typing.Sequence[builtins.str],
        ) -> None:
            '''The key-value pair parameters to use when running the automation document.

            :param key: The key parameter to use when running the automation document.
            :param values: The value parameter to use when running the automation document.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-ssmparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_ssmincidents as ssmincidents
                
                ssm_parameter_property = ssmincidents.CfnResponsePlan.SsmParameterProperty(
                    key="key",
                    values=["values"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__78ed91874812ad3b5b3b479e5115e2a10c2392249d66bfc0a5b57759bf9ed491)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "values": values,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''The key parameter to use when running the automation document.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-ssmparameter.html#cfn-ssmincidents-responseplan-ssmparameter-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def values(self) -> typing.List[builtins.str]:
            '''The value parameter to use when running the automation document.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmincidents-responseplan-ssmparameter.html#cfn-ssmincidents-responseplan-ssmparameter-values
            '''
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SsmParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-ssmincidents.CfnResponsePlanProps",
    jsii_struct_bases=[],
    name_mapping={
        "incident_template": "incidentTemplate",
        "name": "name",
        "actions": "actions",
        "chat_channel": "chatChannel",
        "display_name": "displayName",
        "engagements": "engagements",
        "integrations": "integrations",
        "tags": "tags",
    },
)
class CfnResponsePlanProps:
    def __init__(
        self,
        *,
        incident_template: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnResponsePlan.IncidentTemplateProperty, typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        actions: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnResponsePlan.ActionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        chat_channel: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnResponsePlan.ChatChannelProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        display_name: typing.Optional[builtins.str] = None,
        engagements: typing.Optional[typing.Sequence[builtins.str]] = None,
        integrations: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnResponsePlan.IntegrationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnResponsePlan``.

        :param incident_template: Details used to create an incident when using this response plan.
        :param name: The name of the response plan.
        :param actions: The actions that the response plan starts at the beginning of an incident.
        :param chat_channel: The AWS Chatbot chat channel used for collaboration during an incident.
        :param display_name: The human readable name of the response plan.
        :param engagements: The Amazon Resource Name (ARN) for the contacts and escalation plans that the response plan engages during an incident.
        :param integrations: Information about third-party services integrated into the response plan.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_ssmincidents as ssmincidents
            
            cfn_response_plan_props = ssmincidents.CfnResponsePlanProps(
                incident_template=ssmincidents.CfnResponsePlan.IncidentTemplateProperty(
                    impact=123,
                    title="title",
            
                    # the properties below are optional
                    dedupe_string="dedupeString",
                    incident_tags=[CfnTag(
                        key="key",
                        value="value"
                    )],
                    notification_targets=[ssmincidents.CfnResponsePlan.NotificationTargetItemProperty(
                        sns_topic_arn="snsTopicArn"
                    )],
                    summary="summary"
                ),
                name="name",
            
                # the properties below are optional
                actions=[ssmincidents.CfnResponsePlan.ActionProperty(
                    ssm_automation=ssmincidents.CfnResponsePlan.SsmAutomationProperty(
                        document_name="documentName",
                        role_arn="roleArn",
            
                        # the properties below are optional
                        document_version="documentVersion",
                        dynamic_parameters=[ssmincidents.CfnResponsePlan.DynamicSsmParameterProperty(
                            key="key",
                            value=ssmincidents.CfnResponsePlan.DynamicSsmParameterValueProperty(
                                variable="variable"
                            )
                        )],
                        parameters=[ssmincidents.CfnResponsePlan.SsmParameterProperty(
                            key="key",
                            values=["values"]
                        )],
                        target_account="targetAccount"
                    )
                )],
                chat_channel=ssmincidents.CfnResponsePlan.ChatChannelProperty(
                    chatbot_sns=["chatbotSns"]
                ),
                display_name="displayName",
                engagements=["engagements"],
                integrations=[ssmincidents.CfnResponsePlan.IntegrationProperty(
                    pager_duty_configuration=ssmincidents.CfnResponsePlan.PagerDutyConfigurationProperty(
                        name="name",
                        pager_duty_incident_configuration=ssmincidents.CfnResponsePlan.PagerDutyIncidentConfigurationProperty(
                            service_id="serviceId"
                        ),
                        secret_id="secretId"
                    )
                )],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bea743bd933093a1edf9008236db2e46c6f975c185e8bb9d71e87f42c1bc4676)
            check_type(argname="argument incident_template", value=incident_template, expected_type=type_hints["incident_template"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
            check_type(argname="argument chat_channel", value=chat_channel, expected_type=type_hints["chat_channel"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument engagements", value=engagements, expected_type=type_hints["engagements"])
            check_type(argname="argument integrations", value=integrations, expected_type=type_hints["integrations"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "incident_template": incident_template,
            "name": name,
        }
        if actions is not None:
            self._values["actions"] = actions
        if chat_channel is not None:
            self._values["chat_channel"] = chat_channel
        if display_name is not None:
            self._values["display_name"] = display_name
        if engagements is not None:
            self._values["engagements"] = engagements
        if integrations is not None:
            self._values["integrations"] = integrations
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def incident_template(
        self,
    ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnResponsePlan.IncidentTemplateProperty]:
        '''Details used to create an incident when using this response plan.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html#cfn-ssmincidents-responseplan-incidenttemplate
        '''
        result = self._values.get("incident_template")
        assert result is not None, "Required property 'incident_template' is missing"
        return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnResponsePlan.IncidentTemplateProperty], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the response plan.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html#cfn-ssmincidents-responseplan-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def actions(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnResponsePlan.ActionProperty]]]]:
        '''The actions that the response plan starts at the beginning of an incident.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html#cfn-ssmincidents-responseplan-actions
        '''
        result = self._values.get("actions")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnResponsePlan.ActionProperty]]]], result)

    @builtins.property
    def chat_channel(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnResponsePlan.ChatChannelProperty]]:
        '''The AWS Chatbot chat channel used for collaboration during an incident.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html#cfn-ssmincidents-responseplan-chatchannel
        '''
        result = self._values.get("chat_channel")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnResponsePlan.ChatChannelProperty]], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The human readable name of the response plan.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html#cfn-ssmincidents-responseplan-displayname
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def engagements(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The Amazon Resource Name (ARN) for the contacts and escalation plans that the response plan engages during an incident.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html#cfn-ssmincidents-responseplan-engagements
        '''
        result = self._values.get("engagements")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def integrations(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnResponsePlan.IntegrationProperty]]]]:
        '''Information about third-party services integrated into the response plan.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html#cfn-ssmincidents-responseplan-integrations
        '''
        result = self._values.get("integrations")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnResponsePlan.IntegrationProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-responseplan.html#cfn-ssmincidents-responseplan-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResponsePlanProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnReplicationSet",
    "CfnReplicationSetProps",
    "CfnResponsePlan",
    "CfnResponsePlanProps",
]

publication.publish()

def _typecheckingstub__3c4a5f2015ac0fcdd0216a42b439aa534bcff1514191a1248defc16a8442009b(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    regions: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[typing.Union[CfnReplicationSet.ReplicationRegionProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable]]],
    deletion_protected: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9061e36eaa63fa8ca490b30ac6a69acb29016ee87b286a7987748d2e951a647f(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b658c3b4ad8566fac72cebe2eb7bee4207efd64cddb9a0454c9d9183203f372(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a06fad9d66ac04a548a402b41ec087f43956b3ab1077eb0835b75bd0e560573(
    value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[CfnReplicationSet.ReplicationRegionProperty, _aws_cdk_core_f4b25747.IResolvable]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e30e3bde80aff73843e09e2a133a743088ad21ea17d18cdf4ee45fe61888b69a(
    value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ac1937894930a47409413e821e2d32d6b04ccdf1c31d40fd440a0b4828fe733(
    *,
    sse_kms_key_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bfa4b992e76330396573d9b01bed98052f02975e53b371f19ce62879c4b9411(
    *,
    region_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnReplicationSet.RegionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    region_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c9ecebfbb55e497e146ca09196081a97de754c65ba375c7cbe762a9f3ab5e45(
    *,
    regions: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[typing.Union[CfnReplicationSet.ReplicationRegionProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable]]],
    deletion_protected: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0d0141c81292b027e1db5c662b0e184e7cb6fe536bb7c8a227eac662cac08a1(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    incident_template: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnResponsePlan.IncidentTemplateProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    actions: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnResponsePlan.ActionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    chat_channel: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnResponsePlan.ChatChannelProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    display_name: typing.Optional[builtins.str] = None,
    engagements: typing.Optional[typing.Sequence[builtins.str]] = None,
    integrations: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnResponsePlan.IntegrationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b7cae3159fe0acfb5f877134c9f89c57d234aac0ac24143b8bc868a18a63601(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1072dd039dde19ff08cddec253ad1244076f6052f31460b19d1c054d96c88ed2(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed501da644cb3215823c12d3af0887a518ac451e02026eb8e15762efda711dd8(
    value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnResponsePlan.IncidentTemplateProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b63d22b9154ae185bcbaf816bec454af0589a0513e3603811d6fbe467896b226(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d7a3e799b753f6f4176f2ef8b58691a09067e1f167b79b9871927bdf80029a2(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnResponsePlan.ActionProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db69a94996cb75583772a58f7530b3536616873f65993c6c89a5e9288b2163df(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnResponsePlan.ChatChannelProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2b71ee8c671bb4dbd2f5406633596df83de3bf1dca505e5057d88ad254bb040(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__003e73c2c22d4ad8b35216ca99d3f5d999ea53a74b06e66f41511da5070f6fbf(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87c7ee6b48ceee79d7201bff261236f5f31ae9fc540494d401ecb76aeeb0e6a3(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnResponsePlan.IntegrationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a150f6cdafa8eef83b6c947b195beceec74930628dda404ce33ca2f6d9342a8c(
    *,
    ssm_automation: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnResponsePlan.SsmAutomationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e08fec843c7f3a43b9b8dbe39acdad149d4c3c2aedd31731c815d53078cf2fd2(
    *,
    chatbot_sns: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55fa9def59d6bb1736c01bb99f9e1093fe280cedd9ddd1c1558e6fdb1dbc0ee1(
    *,
    key: builtins.str,
    value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnResponsePlan.DynamicSsmParameterValueProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cd67bb9afc755d4968a737bc00946cb474aca90cb98caec4468e21f3ca629e3(
    *,
    variable: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cdd0deb991ca23b1dd1b146169956ee19358324d31f46343c8021fed8772499(
    *,
    impact: jsii.Number,
    title: builtins.str,
    dedupe_string: typing.Optional[builtins.str] = None,
    incident_tags: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    notification_targets: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnResponsePlan.NotificationTargetItemProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    summary: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed50bcc40d436ba4d38c4dd77f3cf2523401f732eb3724860d85f13ec49cfa88(
    *,
    pager_duty_configuration: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnResponsePlan.PagerDutyConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd903433ca07ba7faa203fbd116a6666def684244587c10b1468c86cbda88f55(
    *,
    sns_topic_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d73662b06fad341e8372f7fdaad154428c00f3f94048013671b28078c9e335b(
    *,
    name: builtins.str,
    pager_duty_incident_configuration: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnResponsePlan.PagerDutyIncidentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    secret_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a095c37d3be492022157b2a1bfc759f1ee4c2747f74f44cdceaad0f3a41d1607(
    *,
    service_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7764d012dd61df480423dd2b2519aa4998ec311d7ccabbee5dde21f2462a716c(
    *,
    document_name: builtins.str,
    role_arn: builtins.str,
    document_version: typing.Optional[builtins.str] = None,
    dynamic_parameters: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnResponsePlan.DynamicSsmParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    parameters: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnResponsePlan.SsmParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    target_account: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78ed91874812ad3b5b3b479e5115e2a10c2392249d66bfc0a5b57759bf9ed491(
    *,
    key: builtins.str,
    values: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bea743bd933093a1edf9008236db2e46c6f975c185e8bb9d71e87f42c1bc4676(
    *,
    incident_template: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnResponsePlan.IncidentTemplateProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    actions: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnResponsePlan.ActionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    chat_channel: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnResponsePlan.ChatChannelProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    display_name: typing.Optional[builtins.str] = None,
    engagements: typing.Optional[typing.Sequence[builtins.str]] = None,
    integrations: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnResponsePlan.IntegrationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

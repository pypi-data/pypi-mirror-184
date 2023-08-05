'''
# AWS::IoTWireless Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_iotwireless as iotwireless
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for IoTWireless construct libraries](https://constructs.dev/search?q=iotwireless)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::IoTWireless resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IoTWireless.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::IoTWireless](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IoTWireless.html).

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
class CfnDestination(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-iotwireless.CfnDestination",
):
    '''A CloudFormation ``AWS::IoTWireless::Destination``.

    Creates a new destination that maps a device message to an AWS IoT rule.

    :cloudformationResource: AWS::IoTWireless::Destination
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_iotwireless as iotwireless
        
        cfn_destination = iotwireless.CfnDestination(self, "MyCfnDestination",
            expression="expression",
            expression_type="expressionType",
            name="name",
            role_arn="roleArn",
        
            # the properties below are optional
            description="description",
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
        expression: builtins.str,
        expression_type: builtins.str,
        name: builtins.str,
        role_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::IoTWireless::Destination``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param expression: The rule name to send messages to.
        :param expression_type: The type of value in ``Expression`` .
        :param name: The name of the new resource.
        :param role_arn: The ARN of the IAM Role that authorizes the destination.
        :param description: The description of the new resource. Maximum length is 2048 characters.
        :param tags: The tags are an array of key-value pairs to attach to the specified resource. Tags can have a minimum of 0 and a maximum of 50 items.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c07d5546eee9891c06c041a98e64d55f9258f40f6c57d8229496a1bbe14b62a3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDestinationProps(
            expression=expression,
            expression_type=expression_type,
            name=name,
            role_arn=role_arn,
            description=description,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0f588c8b63304988e3b3b2747e4fa527dd621202103e6556535d686f4f1d553)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8289c3ab4984a46f3dc227436cb9232bc83f5f487623f0e442617a0df9f9a887)
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
        '''The ARN of the destination created.

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
        '''The tags are an array of key-value pairs to attach to the specified resource.

        Tags can have a minimum of 0 and a maximum of 50 items.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-tags
        '''
        return typing.cast(_aws_cdk_core_f4b25747.TagManager, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        '''The rule name to send messages to.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-expression
        '''
        return typing.cast(builtins.str, jsii.get(self, "expression"))

    @expression.setter
    def expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__391ef63f878229f7f3e7af4f145ad11cb958bcc169f0c50808d4771f48d370fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expression", value)

    @builtins.property
    @jsii.member(jsii_name="expressionType")
    def expression_type(self) -> builtins.str:
        '''The type of value in ``Expression`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-expressiontype
        '''
        return typing.cast(builtins.str, jsii.get(self, "expressionType"))

    @expression_type.setter
    def expression_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3753e7d52d06779443eda5bcccb44a47dc2e29d425c7557181b183dcb245e37)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expressionType", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the new resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fc1f0622e35c3e0ca44862dbcaafd68711d012e0c949c61c60b43ecb966edb3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The ARN of the IAM Role that authorizes the destination.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1d8c10f8c9db42b8dd5d0bbd7ab1686db99a868d4a1ac6e3f7fa917aa6d3c7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the new resource.

        Maximum length is 2048 characters.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a296168c930d693598e4578e8edca9fc5e36eb2bd8a7dbdc80986ca7327aee5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-iotwireless.CfnDestinationProps",
    jsii_struct_bases=[],
    name_mapping={
        "expression": "expression",
        "expression_type": "expressionType",
        "name": "name",
        "role_arn": "roleArn",
        "description": "description",
        "tags": "tags",
    },
)
class CfnDestinationProps:
    def __init__(
        self,
        *,
        expression: builtins.str,
        expression_type: builtins.str,
        name: builtins.str,
        role_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDestination``.

        :param expression: The rule name to send messages to.
        :param expression_type: The type of value in ``Expression`` .
        :param name: The name of the new resource.
        :param role_arn: The ARN of the IAM Role that authorizes the destination.
        :param description: The description of the new resource. Maximum length is 2048 characters.
        :param tags: The tags are an array of key-value pairs to attach to the specified resource. Tags can have a minimum of 0 and a maximum of 50 items.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_iotwireless as iotwireless
            
            cfn_destination_props = iotwireless.CfnDestinationProps(
                expression="expression",
                expression_type="expressionType",
                name="name",
                role_arn="roleArn",
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9070cb0529d6006b3d56cf59fedb7e85cd9879dd12ada9cec779f836ee530780)
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
            check_type(argname="argument expression_type", value=expression_type, expected_type=type_hints["expression_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "expression": expression,
            "expression_type": expression_type,
            "name": name,
            "role_arn": role_arn,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def expression(self) -> builtins.str:
        '''The rule name to send messages to.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-expression
        '''
        result = self._values.get("expression")
        assert result is not None, "Required property 'expression' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def expression_type(self) -> builtins.str:
        '''The type of value in ``Expression`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-expressiontype
        '''
        result = self._values.get("expression_type")
        assert result is not None, "Required property 'expression_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the new resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The ARN of the IAM Role that authorizes the destination.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the new resource.

        Maximum length is 2048 characters.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]]:
        '''The tags are an array of key-value pairs to attach to the specified resource.

        Tags can have a minimum of 0 and a maximum of 50 items.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-destination.html#cfn-iotwireless-destination-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDestinationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnDeviceProfile(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-iotwireless.CfnDeviceProfile",
):
    '''A CloudFormation ``AWS::IoTWireless::DeviceProfile``.

    Creates a new device profile.

    :cloudformationResource: AWS::IoTWireless::DeviceProfile
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_iotwireless as iotwireless
        
        cfn_device_profile = iotwireless.CfnDeviceProfile(self, "MyCfnDeviceProfile",
            lo_ra_wan=iotwireless.CfnDeviceProfile.LoRaWANDeviceProfileProperty(
                class_bTimeout=123,
                class_cTimeout=123,
                factory_preset_freqs_list=[123],
                mac_version="macVersion",
                max_duty_cycle=123,
                max_eirp=123,
                ping_slot_dr=123,
                ping_slot_freq=123,
                ping_slot_period=123,
                reg_params_revision="regParamsRevision",
                rf_region="rfRegion",
                rx_data_rate2=123,
                rx_delay1=123,
                rx_dr_offset1=123,
                rx_freq2=123,
                supports32_bit_fCnt=False,
                supports_class_b=False,
                supports_class_c=False,
                supports_join=False
            ),
            name="name",
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
        lo_ra_wan: typing.Optional[typing.Union[typing.Union["CfnDeviceProfile.LoRaWANDeviceProfileProperty", typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::IoTWireless::DeviceProfile``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param lo_ra_wan: LoRaWAN device profile object.
        :param name: The name of the new resource.
        :param tags: The tags are an array of key-value pairs to attach to the specified resource. Tags can have a minimum of 0 and a maximum of 50 items.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00e6fd505e7c19020d64d1f59d1e418008c69e6745daf7166e5689b3c7d4c1d0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDeviceProfileProps(lo_ra_wan=lo_ra_wan, name=name, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d212c1cc213f0e1ec1e2426fbf8980588bad6cff13c5477b329031eca87e1be4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__554aa51c6b28db8423c61a0fccd803fdde2a7747de576bcecb340af3eeef498b)
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
        '''The ARN of the device profile created.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the device profile created.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _aws_cdk_core_f4b25747.TagManager:
        '''The tags are an array of key-value pairs to attach to the specified resource.

        Tags can have a minimum of 0 and a maximum of 50 items.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html#cfn-iotwireless-deviceprofile-tags
        '''
        return typing.cast(_aws_cdk_core_f4b25747.TagManager, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="loRaWan")
    def lo_ra_wan(
        self,
    ) -> typing.Optional[typing.Union["CfnDeviceProfile.LoRaWANDeviceProfileProperty", _aws_cdk_core_f4b25747.IResolvable]]:
        '''LoRaWAN device profile object.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html#cfn-iotwireless-deviceprofile-lorawan
        '''
        return typing.cast(typing.Optional[typing.Union["CfnDeviceProfile.LoRaWANDeviceProfileProperty", _aws_cdk_core_f4b25747.IResolvable]], jsii.get(self, "loRaWan"))

    @lo_ra_wan.setter
    def lo_ra_wan(
        self,
        value: typing.Optional[typing.Union["CfnDeviceProfile.LoRaWANDeviceProfileProperty", _aws_cdk_core_f4b25747.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1382ed615daabd4b75b523bc91cc1dcc3de85da4ee705a63ab1df96711868ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loRaWan", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the new resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html#cfn-iotwireless-deviceprofile-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0afe21458b494e68210528688ab3f8ee25530ebed85a849ad5f3787338cb54d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotwireless.CfnDeviceProfile.LoRaWANDeviceProfileProperty",
        jsii_struct_bases=[],
        name_mapping={
            "class_b_timeout": "classBTimeout",
            "class_c_timeout": "classCTimeout",
            "factory_preset_freqs_list": "factoryPresetFreqsList",
            "mac_version": "macVersion",
            "max_duty_cycle": "maxDutyCycle",
            "max_eirp": "maxEirp",
            "ping_slot_dr": "pingSlotDr",
            "ping_slot_freq": "pingSlotFreq",
            "ping_slot_period": "pingSlotPeriod",
            "reg_params_revision": "regParamsRevision",
            "rf_region": "rfRegion",
            "rx_data_rate2": "rxDataRate2",
            "rx_delay1": "rxDelay1",
            "rx_dr_offset1": "rxDrOffset1",
            "rx_freq2": "rxFreq2",
            "supports32_bit_f_cnt": "supports32BitFCnt",
            "supports_class_b": "supportsClassB",
            "supports_class_c": "supportsClassC",
            "supports_join": "supportsJoin",
        },
    )
    class LoRaWANDeviceProfileProperty:
        def __init__(
            self,
            *,
            class_b_timeout: typing.Optional[jsii.Number] = None,
            class_c_timeout: typing.Optional[jsii.Number] = None,
            factory_preset_freqs_list: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[jsii.Number]]] = None,
            mac_version: typing.Optional[builtins.str] = None,
            max_duty_cycle: typing.Optional[jsii.Number] = None,
            max_eirp: typing.Optional[jsii.Number] = None,
            ping_slot_dr: typing.Optional[jsii.Number] = None,
            ping_slot_freq: typing.Optional[jsii.Number] = None,
            ping_slot_period: typing.Optional[jsii.Number] = None,
            reg_params_revision: typing.Optional[builtins.str] = None,
            rf_region: typing.Optional[builtins.str] = None,
            rx_data_rate2: typing.Optional[jsii.Number] = None,
            rx_delay1: typing.Optional[jsii.Number] = None,
            rx_dr_offset1: typing.Optional[jsii.Number] = None,
            rx_freq2: typing.Optional[jsii.Number] = None,
            supports32_bit_f_cnt: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            supports_class_b: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            supports_class_c: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            supports_join: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
        ) -> None:
            '''LoRaWAN device profile object.

            :param class_b_timeout: The ClassBTimeout value.
            :param class_c_timeout: The ClassCTimeout value.
            :param factory_preset_freqs_list: The list of values that make up the FactoryPresetFreqs value. Valid range of values include a minimum value of 1000000 and a maximum value of 16700000.
            :param mac_version: The MAC version (such as OTAA 1.1 or OTAA 1.0.3) to use with this device profile.
            :param max_duty_cycle: The MaxDutyCycle value.
            :param max_eirp: The MaxEIRP value.
            :param ping_slot_dr: The PingSlotDR value.
            :param ping_slot_freq: The PingSlotFreq value.
            :param ping_slot_period: The PingSlotPeriod value.
            :param reg_params_revision: The version of regional parameters.
            :param rf_region: The frequency band (RFRegion) value.
            :param rx_data_rate2: The RXDataRate2 value.
            :param rx_delay1: The RXDelay1 value.
            :param rx_dr_offset1: The RXDROffset1 value.
            :param rx_freq2: The RXFreq2 value.
            :param supports32_bit_f_cnt: The Supports32BitFCnt value.
            :param supports_class_b: The SupportsClassB value.
            :param supports_class_c: The SupportsClassC value.
            :param supports_join: The SupportsJoin value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_iotwireless as iotwireless
                
                lo_ra_wANDevice_profile_property = iotwireless.CfnDeviceProfile.LoRaWANDeviceProfileProperty(
                    class_bTimeout=123,
                    class_cTimeout=123,
                    factory_preset_freqs_list=[123],
                    mac_version="macVersion",
                    max_duty_cycle=123,
                    max_eirp=123,
                    ping_slot_dr=123,
                    ping_slot_freq=123,
                    ping_slot_period=123,
                    reg_params_revision="regParamsRevision",
                    rf_region="rfRegion",
                    rx_data_rate2=123,
                    rx_delay1=123,
                    rx_dr_offset1=123,
                    rx_freq2=123,
                    supports32_bit_fCnt=False,
                    supports_class_b=False,
                    supports_class_c=False,
                    supports_join=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4df874c71da347f86d91b106d8ff2c80ea04e8abd384f8aa3e3adc2c7e19d9d1)
                check_type(argname="argument class_b_timeout", value=class_b_timeout, expected_type=type_hints["class_b_timeout"])
                check_type(argname="argument class_c_timeout", value=class_c_timeout, expected_type=type_hints["class_c_timeout"])
                check_type(argname="argument factory_preset_freqs_list", value=factory_preset_freqs_list, expected_type=type_hints["factory_preset_freqs_list"])
                check_type(argname="argument mac_version", value=mac_version, expected_type=type_hints["mac_version"])
                check_type(argname="argument max_duty_cycle", value=max_duty_cycle, expected_type=type_hints["max_duty_cycle"])
                check_type(argname="argument max_eirp", value=max_eirp, expected_type=type_hints["max_eirp"])
                check_type(argname="argument ping_slot_dr", value=ping_slot_dr, expected_type=type_hints["ping_slot_dr"])
                check_type(argname="argument ping_slot_freq", value=ping_slot_freq, expected_type=type_hints["ping_slot_freq"])
                check_type(argname="argument ping_slot_period", value=ping_slot_period, expected_type=type_hints["ping_slot_period"])
                check_type(argname="argument reg_params_revision", value=reg_params_revision, expected_type=type_hints["reg_params_revision"])
                check_type(argname="argument rf_region", value=rf_region, expected_type=type_hints["rf_region"])
                check_type(argname="argument rx_data_rate2", value=rx_data_rate2, expected_type=type_hints["rx_data_rate2"])
                check_type(argname="argument rx_delay1", value=rx_delay1, expected_type=type_hints["rx_delay1"])
                check_type(argname="argument rx_dr_offset1", value=rx_dr_offset1, expected_type=type_hints["rx_dr_offset1"])
                check_type(argname="argument rx_freq2", value=rx_freq2, expected_type=type_hints["rx_freq2"])
                check_type(argname="argument supports32_bit_f_cnt", value=supports32_bit_f_cnt, expected_type=type_hints["supports32_bit_f_cnt"])
                check_type(argname="argument supports_class_b", value=supports_class_b, expected_type=type_hints["supports_class_b"])
                check_type(argname="argument supports_class_c", value=supports_class_c, expected_type=type_hints["supports_class_c"])
                check_type(argname="argument supports_join", value=supports_join, expected_type=type_hints["supports_join"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if class_b_timeout is not None:
                self._values["class_b_timeout"] = class_b_timeout
            if class_c_timeout is not None:
                self._values["class_c_timeout"] = class_c_timeout
            if factory_preset_freqs_list is not None:
                self._values["factory_preset_freqs_list"] = factory_preset_freqs_list
            if mac_version is not None:
                self._values["mac_version"] = mac_version
            if max_duty_cycle is not None:
                self._values["max_duty_cycle"] = max_duty_cycle
            if max_eirp is not None:
                self._values["max_eirp"] = max_eirp
            if ping_slot_dr is not None:
                self._values["ping_slot_dr"] = ping_slot_dr
            if ping_slot_freq is not None:
                self._values["ping_slot_freq"] = ping_slot_freq
            if ping_slot_period is not None:
                self._values["ping_slot_period"] = ping_slot_period
            if reg_params_revision is not None:
                self._values["reg_params_revision"] = reg_params_revision
            if rf_region is not None:
                self._values["rf_region"] = rf_region
            if rx_data_rate2 is not None:
                self._values["rx_data_rate2"] = rx_data_rate2
            if rx_delay1 is not None:
                self._values["rx_delay1"] = rx_delay1
            if rx_dr_offset1 is not None:
                self._values["rx_dr_offset1"] = rx_dr_offset1
            if rx_freq2 is not None:
                self._values["rx_freq2"] = rx_freq2
            if supports32_bit_f_cnt is not None:
                self._values["supports32_bit_f_cnt"] = supports32_bit_f_cnt
            if supports_class_b is not None:
                self._values["supports_class_b"] = supports_class_b
            if supports_class_c is not None:
                self._values["supports_class_c"] = supports_class_c
            if supports_join is not None:
                self._values["supports_join"] = supports_join

        @builtins.property
        def class_b_timeout(self) -> typing.Optional[jsii.Number]:
            '''The ClassBTimeout value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-classbtimeout
            '''
            result = self._values.get("class_b_timeout")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def class_c_timeout(self) -> typing.Optional[jsii.Number]:
            '''The ClassCTimeout value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-classctimeout
            '''
            result = self._values.get("class_c_timeout")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def factory_preset_freqs_list(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[jsii.Number]]]:
            '''The list of values that make up the FactoryPresetFreqs value.

            Valid range of values include a minimum value of 1000000 and a maximum value of 16700000.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-factorypresetfreqslist
            '''
            result = self._values.get("factory_preset_freqs_list")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[jsii.Number]]], result)

        @builtins.property
        def mac_version(self) -> typing.Optional[builtins.str]:
            '''The MAC version (such as OTAA 1.1 or OTAA 1.0.3) to use with this device profile.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-macversion
            '''
            result = self._values.get("mac_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def max_duty_cycle(self) -> typing.Optional[jsii.Number]:
            '''The MaxDutyCycle value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-maxdutycycle
            '''
            result = self._values.get("max_duty_cycle")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_eirp(self) -> typing.Optional[jsii.Number]:
            '''The MaxEIRP value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-maxeirp
            '''
            result = self._values.get("max_eirp")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def ping_slot_dr(self) -> typing.Optional[jsii.Number]:
            '''The PingSlotDR value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-pingslotdr
            '''
            result = self._values.get("ping_slot_dr")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def ping_slot_freq(self) -> typing.Optional[jsii.Number]:
            '''The PingSlotFreq value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-pingslotfreq
            '''
            result = self._values.get("ping_slot_freq")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def ping_slot_period(self) -> typing.Optional[jsii.Number]:
            '''The PingSlotPeriod value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-pingslotperiod
            '''
            result = self._values.get("ping_slot_period")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def reg_params_revision(self) -> typing.Optional[builtins.str]:
            '''The version of regional parameters.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-regparamsrevision
            '''
            result = self._values.get("reg_params_revision")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def rf_region(self) -> typing.Optional[builtins.str]:
            '''The frequency band (RFRegion) value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-rfregion
            '''
            result = self._values.get("rf_region")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def rx_data_rate2(self) -> typing.Optional[jsii.Number]:
            '''The RXDataRate2 value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-rxdatarate2
            '''
            result = self._values.get("rx_data_rate2")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def rx_delay1(self) -> typing.Optional[jsii.Number]:
            '''The RXDelay1 value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-rxdelay1
            '''
            result = self._values.get("rx_delay1")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def rx_dr_offset1(self) -> typing.Optional[jsii.Number]:
            '''The RXDROffset1 value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-rxdroffset1
            '''
            result = self._values.get("rx_dr_offset1")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def rx_freq2(self) -> typing.Optional[jsii.Number]:
            '''The RXFreq2 value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-rxfreq2
            '''
            result = self._values.get("rx_freq2")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def supports32_bit_f_cnt(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''The Supports32BitFCnt value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-supports32bitfcnt
            '''
            result = self._values.get("supports32_bit_f_cnt")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def supports_class_b(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''The SupportsClassB value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-supportsclassb
            '''
            result = self._values.get("supports_class_b")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def supports_class_c(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''The SupportsClassC value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-supportsclassc
            '''
            result = self._values.get("supports_class_c")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def supports_join(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''The SupportsJoin value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-deviceprofile-lorawandeviceprofile.html#cfn-iotwireless-deviceprofile-lorawandeviceprofile-supportsjoin
            '''
            result = self._values.get("supports_join")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoRaWANDeviceProfileProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-iotwireless.CfnDeviceProfileProps",
    jsii_struct_bases=[],
    name_mapping={"lo_ra_wan": "loRaWan", "name": "name", "tags": "tags"},
)
class CfnDeviceProfileProps:
    def __init__(
        self,
        *,
        lo_ra_wan: typing.Optional[typing.Union[typing.Union[CfnDeviceProfile.LoRaWANDeviceProfileProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDeviceProfile``.

        :param lo_ra_wan: LoRaWAN device profile object.
        :param name: The name of the new resource.
        :param tags: The tags are an array of key-value pairs to attach to the specified resource. Tags can have a minimum of 0 and a maximum of 50 items.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_iotwireless as iotwireless
            
            cfn_device_profile_props = iotwireless.CfnDeviceProfileProps(
                lo_ra_wan=iotwireless.CfnDeviceProfile.LoRaWANDeviceProfileProperty(
                    class_bTimeout=123,
                    class_cTimeout=123,
                    factory_preset_freqs_list=[123],
                    mac_version="macVersion",
                    max_duty_cycle=123,
                    max_eirp=123,
                    ping_slot_dr=123,
                    ping_slot_freq=123,
                    ping_slot_period=123,
                    reg_params_revision="regParamsRevision",
                    rf_region="rfRegion",
                    rx_data_rate2=123,
                    rx_delay1=123,
                    rx_dr_offset1=123,
                    rx_freq2=123,
                    supports32_bit_fCnt=False,
                    supports_class_b=False,
                    supports_class_c=False,
                    supports_join=False
                ),
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__786fff6434f78dd9f30b4cfe18f3ed2ed4c80556a2b98404510ae635247bea60)
            check_type(argname="argument lo_ra_wan", value=lo_ra_wan, expected_type=type_hints["lo_ra_wan"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if lo_ra_wan is not None:
            self._values["lo_ra_wan"] = lo_ra_wan
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def lo_ra_wan(
        self,
    ) -> typing.Optional[typing.Union[CfnDeviceProfile.LoRaWANDeviceProfileProperty, _aws_cdk_core_f4b25747.IResolvable]]:
        '''LoRaWAN device profile object.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html#cfn-iotwireless-deviceprofile-lorawan
        '''
        result = self._values.get("lo_ra_wan")
        return typing.cast(typing.Optional[typing.Union[CfnDeviceProfile.LoRaWANDeviceProfileProperty, _aws_cdk_core_f4b25747.IResolvable]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the new resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html#cfn-iotwireless-deviceprofile-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]]:
        '''The tags are an array of key-value pairs to attach to the specified resource.

        Tags can have a minimum of 0 and a maximum of 50 items.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-deviceprofile.html#cfn-iotwireless-deviceprofile-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDeviceProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnFuotaTask(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-iotwireless.CfnFuotaTask",
):
    '''A CloudFormation ``AWS::IoTWireless::FuotaTask``.

    A FUOTA task.

    :cloudformationResource: AWS::IoTWireless::FuotaTask
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_iotwireless as iotwireless
        
        cfn_fuota_task = iotwireless.CfnFuotaTask(self, "MyCfnFuotaTask",
            firmware_update_image="firmwareUpdateImage",
            firmware_update_role="firmwareUpdateRole",
            lo_ra_wan=iotwireless.CfnFuotaTask.LoRaWANProperty(
                rf_region="rfRegion",
        
                # the properties below are optional
                start_time="startTime"
            ),
        
            # the properties below are optional
            associate_multicast_group="associateMulticastGroup",
            associate_wireless_device="associateWirelessDevice",
            description="description",
            disassociate_multicast_group="disassociateMulticastGroup",
            disassociate_wireless_device="disassociateWirelessDevice",
            name="name",
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
        firmware_update_image: builtins.str,
        firmware_update_role: builtins.str,
        lo_ra_wan: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnFuotaTask.LoRaWANProperty", typing.Dict[builtins.str, typing.Any]]],
        associate_multicast_group: typing.Optional[builtins.str] = None,
        associate_wireless_device: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        disassociate_multicast_group: typing.Optional[builtins.str] = None,
        disassociate_wireless_device: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::IoTWireless::FuotaTask``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param firmware_update_image: The S3 URI points to a firmware update image that is to be used with a FUOTA task.
        :param firmware_update_role: The firmware update role that is to be used with a FUOTA task.
        :param lo_ra_wan: The LoRaWAN information used with a FUOTA task.
        :param associate_multicast_group: The ID of the multicast group to associate with a FUOTA task.
        :param associate_wireless_device: The ID of the wireless device to associate with a multicast group.
        :param description: The description of the new resource.
        :param disassociate_multicast_group: The ID of the multicast group to disassociate from a FUOTA task.
        :param disassociate_wireless_device: The ID of the wireless device to disassociate from a FUOTA task.
        :param name: The name of a FUOTA task.
        :param tags: The tags are an array of key-value pairs to attach to the specified resource. Tags can have a minimum of 0 and a maximum of 50 items.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fac50800fa79fde1d0f1a7bfce65467532f94e2dd3e9500046e6714c9ee8990e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFuotaTaskProps(
            firmware_update_image=firmware_update_image,
            firmware_update_role=firmware_update_role,
            lo_ra_wan=lo_ra_wan,
            associate_multicast_group=associate_multicast_group,
            associate_wireless_device=associate_wireless_device,
            description=description,
            disassociate_multicast_group=disassociate_multicast_group,
            disassociate_wireless_device=disassociate_wireless_device,
            name=name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__574b4629294334955ce6611455e2967cdf368d8d573cf9e0967c46ed618cb602)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8bc81f32f2986cf67b5338aeaba0d8357a04e4dd0383b3b0e850dc8ec9baec68)
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
        '''The ARN of a FUOTA task.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrFuotaTaskStatus")
    def attr_fuota_task_status(self) -> builtins.str:
        '''The status of a FUOTA task.

        :cloudformationAttribute: FuotaTaskStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFuotaTaskStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of a FUOTA task.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrLoRaWanStartTime")
    def attr_lo_ra_wan_start_time(self) -> builtins.str:
        '''Start time of a FUOTA task.

        :cloudformationAttribute: LoRaWAN.StartTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLoRaWanStartTime"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _aws_cdk_core_f4b25747.TagManager:
        '''The tags are an array of key-value pairs to attach to the specified resource.

        Tags can have a minimum of 0 and a maximum of 50 items.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-tags
        '''
        return typing.cast(_aws_cdk_core_f4b25747.TagManager, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="firmwareUpdateImage")
    def firmware_update_image(self) -> builtins.str:
        '''The S3 URI points to a firmware update image that is to be used with a FUOTA task.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-firmwareupdateimage
        '''
        return typing.cast(builtins.str, jsii.get(self, "firmwareUpdateImage"))

    @firmware_update_image.setter
    def firmware_update_image(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b99a931b2d8ad5f6646c170e4eeab1c40b6594745f02910413d4a4f5f4de66a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firmwareUpdateImage", value)

    @builtins.property
    @jsii.member(jsii_name="firmwareUpdateRole")
    def firmware_update_role(self) -> builtins.str:
        '''The firmware update role that is to be used with a FUOTA task.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-firmwareupdaterole
        '''
        return typing.cast(builtins.str, jsii.get(self, "firmwareUpdateRole"))

    @firmware_update_role.setter
    def firmware_update_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a13d972a00b2e05226cccf6f832174bb0318fc14f92e178a44ef297404714f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firmwareUpdateRole", value)

    @builtins.property
    @jsii.member(jsii_name="loRaWan")
    def lo_ra_wan(
        self,
    ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnFuotaTask.LoRaWANProperty"]:
        '''The LoRaWAN information used with a FUOTA task.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-lorawan
        '''
        return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnFuotaTask.LoRaWANProperty"], jsii.get(self, "loRaWan"))

    @lo_ra_wan.setter
    def lo_ra_wan(
        self,
        value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnFuotaTask.LoRaWANProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1dfcb6d788444ab7fddf1d72a0fed6ee51ba0b594a4e005f7da26398eeb252b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loRaWan", value)

    @builtins.property
    @jsii.member(jsii_name="associateMulticastGroup")
    def associate_multicast_group(self) -> typing.Optional[builtins.str]:
        '''The ID of the multicast group to associate with a FUOTA task.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-associatemulticastgroup
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "associateMulticastGroup"))

    @associate_multicast_group.setter
    def associate_multicast_group(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3b31f9255759727056bf9c371484663111b2a25fcbc621806adbd08b23e9bf6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "associateMulticastGroup", value)

    @builtins.property
    @jsii.member(jsii_name="associateWirelessDevice")
    def associate_wireless_device(self) -> typing.Optional[builtins.str]:
        '''The ID of the wireless device to associate with a multicast group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-associatewirelessdevice
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "associateWirelessDevice"))

    @associate_wireless_device.setter
    def associate_wireless_device(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ef7ee0475718cd5e7cce1ab7bc2db177557a091137e157b1a31c93a252c6278)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "associateWirelessDevice", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the new resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2a29dcd7459b584c8f47ef33fbe5ac33c53b6f9499a6647962851ffc48e3044)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="disassociateMulticastGroup")
    def disassociate_multicast_group(self) -> typing.Optional[builtins.str]:
        '''The ID of the multicast group to disassociate from a FUOTA task.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-disassociatemulticastgroup
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "disassociateMulticastGroup"))

    @disassociate_multicast_group.setter
    def disassociate_multicast_group(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63dddc2cbfffcab1ce28810bc7fd476c21d6c3ffe89753f0339b3946d596c780)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disassociateMulticastGroup", value)

    @builtins.property
    @jsii.member(jsii_name="disassociateWirelessDevice")
    def disassociate_wireless_device(self) -> typing.Optional[builtins.str]:
        '''The ID of the wireless device to disassociate from a FUOTA task.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-disassociatewirelessdevice
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "disassociateWirelessDevice"))

    @disassociate_wireless_device.setter
    def disassociate_wireless_device(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b57451d39cf92c1c3968b85e86f24d3d5c84f59993bcc64472aae0afce9f40b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disassociateWirelessDevice", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of a FUOTA task.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cb0945d4b06e6d9555be90c010b58e1188907319028ca761c8f40ab1bfd44ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotwireless.CfnFuotaTask.LoRaWANProperty",
        jsii_struct_bases=[],
        name_mapping={"rf_region": "rfRegion", "start_time": "startTime"},
    )
    class LoRaWANProperty:
        def __init__(
            self,
            *,
            rf_region: builtins.str,
            start_time: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The LoRaWAN information used with a FUOTA task.

            :param rf_region: The frequency band (RFRegion) value.
            :param start_time: Start time of a FUOTA task.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-fuotatask-lorawan.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_iotwireless as iotwireless
                
                lo_ra_wANProperty = iotwireless.CfnFuotaTask.LoRaWANProperty(
                    rf_region="rfRegion",
                
                    # the properties below are optional
                    start_time="startTime"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b7f394b2c3cada2f758424af2b04612603fd774011a3cf64273266119928877b)
                check_type(argname="argument rf_region", value=rf_region, expected_type=type_hints["rf_region"])
                check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "rf_region": rf_region,
            }
            if start_time is not None:
                self._values["start_time"] = start_time

        @builtins.property
        def rf_region(self) -> builtins.str:
            '''The frequency band (RFRegion) value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-fuotatask-lorawan.html#cfn-iotwireless-fuotatask-lorawan-rfregion
            '''
            result = self._values.get("rf_region")
            assert result is not None, "Required property 'rf_region' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def start_time(self) -> typing.Optional[builtins.str]:
            '''Start time of a FUOTA task.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-fuotatask-lorawan.html#cfn-iotwireless-fuotatask-lorawan-starttime
            '''
            result = self._values.get("start_time")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoRaWANProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-iotwireless.CfnFuotaTaskProps",
    jsii_struct_bases=[],
    name_mapping={
        "firmware_update_image": "firmwareUpdateImage",
        "firmware_update_role": "firmwareUpdateRole",
        "lo_ra_wan": "loRaWan",
        "associate_multicast_group": "associateMulticastGroup",
        "associate_wireless_device": "associateWirelessDevice",
        "description": "description",
        "disassociate_multicast_group": "disassociateMulticastGroup",
        "disassociate_wireless_device": "disassociateWirelessDevice",
        "name": "name",
        "tags": "tags",
    },
)
class CfnFuotaTaskProps:
    def __init__(
        self,
        *,
        firmware_update_image: builtins.str,
        firmware_update_role: builtins.str,
        lo_ra_wan: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnFuotaTask.LoRaWANProperty, typing.Dict[builtins.str, typing.Any]]],
        associate_multicast_group: typing.Optional[builtins.str] = None,
        associate_wireless_device: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        disassociate_multicast_group: typing.Optional[builtins.str] = None,
        disassociate_wireless_device: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnFuotaTask``.

        :param firmware_update_image: The S3 URI points to a firmware update image that is to be used with a FUOTA task.
        :param firmware_update_role: The firmware update role that is to be used with a FUOTA task.
        :param lo_ra_wan: The LoRaWAN information used with a FUOTA task.
        :param associate_multicast_group: The ID of the multicast group to associate with a FUOTA task.
        :param associate_wireless_device: The ID of the wireless device to associate with a multicast group.
        :param description: The description of the new resource.
        :param disassociate_multicast_group: The ID of the multicast group to disassociate from a FUOTA task.
        :param disassociate_wireless_device: The ID of the wireless device to disassociate from a FUOTA task.
        :param name: The name of a FUOTA task.
        :param tags: The tags are an array of key-value pairs to attach to the specified resource. Tags can have a minimum of 0 and a maximum of 50 items.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_iotwireless as iotwireless
            
            cfn_fuota_task_props = iotwireless.CfnFuotaTaskProps(
                firmware_update_image="firmwareUpdateImage",
                firmware_update_role="firmwareUpdateRole",
                lo_ra_wan=iotwireless.CfnFuotaTask.LoRaWANProperty(
                    rf_region="rfRegion",
            
                    # the properties below are optional
                    start_time="startTime"
                ),
            
                # the properties below are optional
                associate_multicast_group="associateMulticastGroup",
                associate_wireless_device="associateWirelessDevice",
                description="description",
                disassociate_multicast_group="disassociateMulticastGroup",
                disassociate_wireless_device="disassociateWirelessDevice",
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e35293df026c833950b6cca8691adb2956ae230656d925e366bac133d424834a)
            check_type(argname="argument firmware_update_image", value=firmware_update_image, expected_type=type_hints["firmware_update_image"])
            check_type(argname="argument firmware_update_role", value=firmware_update_role, expected_type=type_hints["firmware_update_role"])
            check_type(argname="argument lo_ra_wan", value=lo_ra_wan, expected_type=type_hints["lo_ra_wan"])
            check_type(argname="argument associate_multicast_group", value=associate_multicast_group, expected_type=type_hints["associate_multicast_group"])
            check_type(argname="argument associate_wireless_device", value=associate_wireless_device, expected_type=type_hints["associate_wireless_device"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument disassociate_multicast_group", value=disassociate_multicast_group, expected_type=type_hints["disassociate_multicast_group"])
            check_type(argname="argument disassociate_wireless_device", value=disassociate_wireless_device, expected_type=type_hints["disassociate_wireless_device"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "firmware_update_image": firmware_update_image,
            "firmware_update_role": firmware_update_role,
            "lo_ra_wan": lo_ra_wan,
        }
        if associate_multicast_group is not None:
            self._values["associate_multicast_group"] = associate_multicast_group
        if associate_wireless_device is not None:
            self._values["associate_wireless_device"] = associate_wireless_device
        if description is not None:
            self._values["description"] = description
        if disassociate_multicast_group is not None:
            self._values["disassociate_multicast_group"] = disassociate_multicast_group
        if disassociate_wireless_device is not None:
            self._values["disassociate_wireless_device"] = disassociate_wireless_device
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def firmware_update_image(self) -> builtins.str:
        '''The S3 URI points to a firmware update image that is to be used with a FUOTA task.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-firmwareupdateimage
        '''
        result = self._values.get("firmware_update_image")
        assert result is not None, "Required property 'firmware_update_image' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def firmware_update_role(self) -> builtins.str:
        '''The firmware update role that is to be used with a FUOTA task.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-firmwareupdaterole
        '''
        result = self._values.get("firmware_update_role")
        assert result is not None, "Required property 'firmware_update_role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lo_ra_wan(
        self,
    ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnFuotaTask.LoRaWANProperty]:
        '''The LoRaWAN information used with a FUOTA task.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-lorawan
        '''
        result = self._values.get("lo_ra_wan")
        assert result is not None, "Required property 'lo_ra_wan' is missing"
        return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnFuotaTask.LoRaWANProperty], result)

    @builtins.property
    def associate_multicast_group(self) -> typing.Optional[builtins.str]:
        '''The ID of the multicast group to associate with a FUOTA task.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-associatemulticastgroup
        '''
        result = self._values.get("associate_multicast_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def associate_wireless_device(self) -> typing.Optional[builtins.str]:
        '''The ID of the wireless device to associate with a multicast group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-associatewirelessdevice
        '''
        result = self._values.get("associate_wireless_device")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the new resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disassociate_multicast_group(self) -> typing.Optional[builtins.str]:
        '''The ID of the multicast group to disassociate from a FUOTA task.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-disassociatemulticastgroup
        '''
        result = self._values.get("disassociate_multicast_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disassociate_wireless_device(self) -> typing.Optional[builtins.str]:
        '''The ID of the wireless device to disassociate from a FUOTA task.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-disassociatewirelessdevice
        '''
        result = self._values.get("disassociate_wireless_device")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of a FUOTA task.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]]:
        '''The tags are an array of key-value pairs to attach to the specified resource.

        Tags can have a minimum of 0 and a maximum of 50 items.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-fuotatask.html#cfn-iotwireless-fuotatask-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFuotaTaskProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnMulticastGroup(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-iotwireless.CfnMulticastGroup",
):
    '''A CloudFormation ``AWS::IoTWireless::MulticastGroup``.

    A multicast group.

    :cloudformationResource: AWS::IoTWireless::MulticastGroup
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_iotwireless as iotwireless
        
        cfn_multicast_group = iotwireless.CfnMulticastGroup(self, "MyCfnMulticastGroup",
            lo_ra_wan=iotwireless.CfnMulticastGroup.LoRaWANProperty(
                dl_class="dlClass",
                rf_region="rfRegion",
        
                # the properties below are optional
                number_of_devices_in_group=123,
                number_of_devices_requested=123
            ),
        
            # the properties below are optional
            associate_wireless_device="associateWirelessDevice",
            description="description",
            disassociate_wireless_device="disassociateWirelessDevice",
            name="name",
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
        lo_ra_wan: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnMulticastGroup.LoRaWANProperty", typing.Dict[builtins.str, typing.Any]]],
        associate_wireless_device: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        disassociate_wireless_device: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::IoTWireless::MulticastGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param lo_ra_wan: The LoRaWAN information that is to be used with the multicast group.
        :param associate_wireless_device: The ID of the wireless device to associate with a multicast group.
        :param description: The description of the multicast group.
        :param disassociate_wireless_device: The ID of the wireless device to disassociate from a multicast group.
        :param name: The name of the multicast group.
        :param tags: The tags are an array of key-value pairs to attach to the specified resource. Tags can have a minimum of 0 and a maximum of 50 items.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a2e05fa345b05f90f387c25508cdd51b56624ed2f49a6606328d2d548181820)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMulticastGroupProps(
            lo_ra_wan=lo_ra_wan,
            associate_wireless_device=associate_wireless_device,
            description=description,
            disassociate_wireless_device=disassociate_wireless_device,
            name=name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4de8527c39ab1d6e8c43a277cc2621cfd2749312f1e0694f9650adc9b23a2073)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0823deac008b9fb7f95e9bc1675655a06c6d4f388e8b0859225ad9b14a442741)
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
        '''The ARN of the multicast group.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the multicast group.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrLoRaWanNumberOfDevicesInGroup")
    def attr_lo_ra_wan_number_of_devices_in_group(self) -> jsii.Number:
        '''The number of devices that are associated to the multicast group.

        :cloudformationAttribute: LoRaWAN.NumberOfDevicesInGroup
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrLoRaWanNumberOfDevicesInGroup"))

    @builtins.property
    @jsii.member(jsii_name="attrLoRaWanNumberOfDevicesRequested")
    def attr_lo_ra_wan_number_of_devices_requested(self) -> jsii.Number:
        '''The number of devices that are requested to be associated with the multicast group.

        :cloudformationAttribute: LoRaWAN.NumberOfDevicesRequested
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrLoRaWanNumberOfDevicesRequested"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of a multicast group.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _aws_cdk_core_f4b25747.TagManager:
        '''The tags are an array of key-value pairs to attach to the specified resource.

        Tags can have a minimum of 0 and a maximum of 50 items.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html#cfn-iotwireless-multicastgroup-tags
        '''
        return typing.cast(_aws_cdk_core_f4b25747.TagManager, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="loRaWan")
    def lo_ra_wan(
        self,
    ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnMulticastGroup.LoRaWANProperty"]:
        '''The LoRaWAN information that is to be used with the multicast group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html#cfn-iotwireless-multicastgroup-lorawan
        '''
        return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnMulticastGroup.LoRaWANProperty"], jsii.get(self, "loRaWan"))

    @lo_ra_wan.setter
    def lo_ra_wan(
        self,
        value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnMulticastGroup.LoRaWANProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cbe8a4f8e06bb7a860cb0baab06842b8f4b0598afba3017867156d184004132)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loRaWan", value)

    @builtins.property
    @jsii.member(jsii_name="associateWirelessDevice")
    def associate_wireless_device(self) -> typing.Optional[builtins.str]:
        '''The ID of the wireless device to associate with a multicast group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html#cfn-iotwireless-multicastgroup-associatewirelessdevice
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "associateWirelessDevice"))

    @associate_wireless_device.setter
    def associate_wireless_device(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__707cc48ddfdd5448a4a796d8f52b97fe9da0b1fc8b209a6091ca0e5382908174)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "associateWirelessDevice", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the multicast group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html#cfn-iotwireless-multicastgroup-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18801e24de5d350eb998f7a24278e5de6cba1d4979b3899774f51d95f04a32db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="disassociateWirelessDevice")
    def disassociate_wireless_device(self) -> typing.Optional[builtins.str]:
        '''The ID of the wireless device to disassociate from a multicast group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html#cfn-iotwireless-multicastgroup-disassociatewirelessdevice
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "disassociateWirelessDevice"))

    @disassociate_wireless_device.setter
    def disassociate_wireless_device(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__babf64259763222e9200372f8f9a0dc47f9344c566a0e18735c034109a5e4dca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disassociateWirelessDevice", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the multicast group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html#cfn-iotwireless-multicastgroup-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab82d1d3876064a7214b1df689f194e9045000c7650ab8ad9f395a4739628719)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotwireless.CfnMulticastGroup.LoRaWANProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dl_class": "dlClass",
            "rf_region": "rfRegion",
            "number_of_devices_in_group": "numberOfDevicesInGroup",
            "number_of_devices_requested": "numberOfDevicesRequested",
        },
    )
    class LoRaWANProperty:
        def __init__(
            self,
            *,
            dl_class: builtins.str,
            rf_region: builtins.str,
            number_of_devices_in_group: typing.Optional[jsii.Number] = None,
            number_of_devices_requested: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The LoRaWAN information that is to be used with the multicast group.

            :param dl_class: DlClass for LoRaWAN. Valid values are ClassB and ClassC.
            :param rf_region: The frequency band (RFRegion) value.
            :param number_of_devices_in_group: Number of devices that are associated to the multicast group.
            :param number_of_devices_requested: Number of devices that are requested to be associated with the multicast group.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-multicastgroup-lorawan.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_iotwireless as iotwireless
                
                lo_ra_wANProperty = iotwireless.CfnMulticastGroup.LoRaWANProperty(
                    dl_class="dlClass",
                    rf_region="rfRegion",
                
                    # the properties below are optional
                    number_of_devices_in_group=123,
                    number_of_devices_requested=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__be6c8762f813fbf9a7591812bd531240173637e378321fb3b31d14215401aeaf)
                check_type(argname="argument dl_class", value=dl_class, expected_type=type_hints["dl_class"])
                check_type(argname="argument rf_region", value=rf_region, expected_type=type_hints["rf_region"])
                check_type(argname="argument number_of_devices_in_group", value=number_of_devices_in_group, expected_type=type_hints["number_of_devices_in_group"])
                check_type(argname="argument number_of_devices_requested", value=number_of_devices_requested, expected_type=type_hints["number_of_devices_requested"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "dl_class": dl_class,
                "rf_region": rf_region,
            }
            if number_of_devices_in_group is not None:
                self._values["number_of_devices_in_group"] = number_of_devices_in_group
            if number_of_devices_requested is not None:
                self._values["number_of_devices_requested"] = number_of_devices_requested

        @builtins.property
        def dl_class(self) -> builtins.str:
            '''DlClass for LoRaWAN.

            Valid values are ClassB and ClassC.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-multicastgroup-lorawan.html#cfn-iotwireless-multicastgroup-lorawan-dlclass
            '''
            result = self._values.get("dl_class")
            assert result is not None, "Required property 'dl_class' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def rf_region(self) -> builtins.str:
            '''The frequency band (RFRegion) value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-multicastgroup-lorawan.html#cfn-iotwireless-multicastgroup-lorawan-rfregion
            '''
            result = self._values.get("rf_region")
            assert result is not None, "Required property 'rf_region' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def number_of_devices_in_group(self) -> typing.Optional[jsii.Number]:
            '''Number of devices that are associated to the multicast group.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-multicastgroup-lorawan.html#cfn-iotwireless-multicastgroup-lorawan-numberofdevicesingroup
            '''
            result = self._values.get("number_of_devices_in_group")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def number_of_devices_requested(self) -> typing.Optional[jsii.Number]:
            '''Number of devices that are requested to be associated with the multicast group.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-multicastgroup-lorawan.html#cfn-iotwireless-multicastgroup-lorawan-numberofdevicesrequested
            '''
            result = self._values.get("number_of_devices_requested")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoRaWANProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-iotwireless.CfnMulticastGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "lo_ra_wan": "loRaWan",
        "associate_wireless_device": "associateWirelessDevice",
        "description": "description",
        "disassociate_wireless_device": "disassociateWirelessDevice",
        "name": "name",
        "tags": "tags",
    },
)
class CfnMulticastGroupProps:
    def __init__(
        self,
        *,
        lo_ra_wan: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnMulticastGroup.LoRaWANProperty, typing.Dict[builtins.str, typing.Any]]],
        associate_wireless_device: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        disassociate_wireless_device: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnMulticastGroup``.

        :param lo_ra_wan: The LoRaWAN information that is to be used with the multicast group.
        :param associate_wireless_device: The ID of the wireless device to associate with a multicast group.
        :param description: The description of the multicast group.
        :param disassociate_wireless_device: The ID of the wireless device to disassociate from a multicast group.
        :param name: The name of the multicast group.
        :param tags: The tags are an array of key-value pairs to attach to the specified resource. Tags can have a minimum of 0 and a maximum of 50 items.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_iotwireless as iotwireless
            
            cfn_multicast_group_props = iotwireless.CfnMulticastGroupProps(
                lo_ra_wan=iotwireless.CfnMulticastGroup.LoRaWANProperty(
                    dl_class="dlClass",
                    rf_region="rfRegion",
            
                    # the properties below are optional
                    number_of_devices_in_group=123,
                    number_of_devices_requested=123
                ),
            
                # the properties below are optional
                associate_wireless_device="associateWirelessDevice",
                description="description",
                disassociate_wireless_device="disassociateWirelessDevice",
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6520d54ed44ebc8cc25979431512f73387c8209299844ee263df28b92033bb1d)
            check_type(argname="argument lo_ra_wan", value=lo_ra_wan, expected_type=type_hints["lo_ra_wan"])
            check_type(argname="argument associate_wireless_device", value=associate_wireless_device, expected_type=type_hints["associate_wireless_device"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument disassociate_wireless_device", value=disassociate_wireless_device, expected_type=type_hints["disassociate_wireless_device"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "lo_ra_wan": lo_ra_wan,
        }
        if associate_wireless_device is not None:
            self._values["associate_wireless_device"] = associate_wireless_device
        if description is not None:
            self._values["description"] = description
        if disassociate_wireless_device is not None:
            self._values["disassociate_wireless_device"] = disassociate_wireless_device
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def lo_ra_wan(
        self,
    ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnMulticastGroup.LoRaWANProperty]:
        '''The LoRaWAN information that is to be used with the multicast group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html#cfn-iotwireless-multicastgroup-lorawan
        '''
        result = self._values.get("lo_ra_wan")
        assert result is not None, "Required property 'lo_ra_wan' is missing"
        return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnMulticastGroup.LoRaWANProperty], result)

    @builtins.property
    def associate_wireless_device(self) -> typing.Optional[builtins.str]:
        '''The ID of the wireless device to associate with a multicast group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html#cfn-iotwireless-multicastgroup-associatewirelessdevice
        '''
        result = self._values.get("associate_wireless_device")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the multicast group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html#cfn-iotwireless-multicastgroup-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disassociate_wireless_device(self) -> typing.Optional[builtins.str]:
        '''The ID of the wireless device to disassociate from a multicast group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html#cfn-iotwireless-multicastgroup-disassociatewirelessdevice
        '''
        result = self._values.get("disassociate_wireless_device")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the multicast group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html#cfn-iotwireless-multicastgroup-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]]:
        '''The tags are an array of key-value pairs to attach to the specified resource.

        Tags can have a minimum of 0 and a maximum of 50 items.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html#cfn-iotwireless-multicastgroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMulticastGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnNetworkAnalyzerConfiguration(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-iotwireless.CfnNetworkAnalyzerConfiguration",
):
    '''A CloudFormation ``AWS::IoTWireless::NetworkAnalyzerConfiguration``.

    Network analyzer configuration.

    :cloudformationResource: AWS::IoTWireless::NetworkAnalyzerConfiguration
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-networkanalyzerconfiguration.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_iotwireless as iotwireless
        
        # trace_content: Any
        
        cfn_network_analyzer_configuration = iotwireless.CfnNetworkAnalyzerConfiguration(self, "MyCfnNetworkAnalyzerConfiguration",
            name="name",
        
            # the properties below are optional
            description="description",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            trace_content=trace_content,
            wireless_devices=["wirelessDevices"],
            wireless_gateways=["wirelessGateways"]
        )
    '''

    def __init__(
        self,
        scope: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
        trace_content: typing.Any = None,
        wireless_devices: typing.Optional[typing.Sequence[builtins.str]] = None,
        wireless_gateways: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::IoTWireless::NetworkAnalyzerConfiguration``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: Name of the network analyzer configuration.
        :param description: The description of the resource.
        :param tags: The tags to attach to the specified resource. Tags are metadata that you can use to manage a resource.
        :param trace_content: Trace content for your wireless gateway and wireless device resources.
        :param wireless_devices: Wireless device resources to add to the network analyzer configuration. Provide the ``WirelessDeviceId`` of the resource to add in the input array.
        :param wireless_gateways: Wireless gateway resources to add to the network analyzer configuration. Provide the ``WirelessGatewayId`` of the resource to add in the input array.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d967395ceebc9ab2779b47d78fba79166b5164b9ddcf171e133a13c7e899d4d1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnNetworkAnalyzerConfigurationProps(
            name=name,
            description=description,
            tags=tags,
            trace_content=trace_content,
            wireless_devices=wireless_devices,
            wireless_gateways=wireless_gateways,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7bc22364251ed1bcc2143106adcf75e5da9af83909fb8dbb99b4aebfcb0ff1e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fa939ffc0ec5d1811a752ca54b711682aaa2cb478c3770f3c37aee0bf77d8809)
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
        '''The Amazon Resource Name (ARN) of the resource.

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
        '''The tags to attach to the specified resource.

        Tags are metadata that you can use to manage a resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-networkanalyzerconfiguration.html#cfn-iotwireless-networkanalyzerconfiguration-tags
        '''
        return typing.cast(_aws_cdk_core_f4b25747.TagManager, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''Name of the network analyzer configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-networkanalyzerconfiguration.html#cfn-iotwireless-networkanalyzerconfiguration-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de7a3f4635556d9edd70ebfdc7ac76aae27772707d845e4abef3cce418b4c740)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="traceContent")
    def trace_content(self) -> typing.Any:
        '''Trace content for your wireless gateway and wireless device resources.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-networkanalyzerconfiguration.html#cfn-iotwireless-networkanalyzerconfiguration-tracecontent
        '''
        return typing.cast(typing.Any, jsii.get(self, "traceContent"))

    @trace_content.setter
    def trace_content(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8df36495c789634bd67810c6db00a288f2ba47fc6339669d0c775506dd31cb9a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "traceContent", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-networkanalyzerconfiguration.html#cfn-iotwireless-networkanalyzerconfiguration-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20758c77a313146e5260d9586cec253e25535329d4a39dcaf98051d9957e1c18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="wirelessDevices")
    def wireless_devices(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Wireless device resources to add to the network analyzer configuration.

        Provide the ``WirelessDeviceId`` of the resource to add in the input array.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-networkanalyzerconfiguration.html#cfn-iotwireless-networkanalyzerconfiguration-wirelessdevices
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "wirelessDevices"))

    @wireless_devices.setter
    def wireless_devices(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aafaec887cd8114ccf9d608c5397bd1f127ebb95cabe2668eb2903348b478433)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wirelessDevices", value)

    @builtins.property
    @jsii.member(jsii_name="wirelessGateways")
    def wireless_gateways(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Wireless gateway resources to add to the network analyzer configuration.

        Provide the ``WirelessGatewayId`` of the resource to add in the input array.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-networkanalyzerconfiguration.html#cfn-iotwireless-networkanalyzerconfiguration-wirelessgateways
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "wirelessGateways"))

    @wireless_gateways.setter
    def wireless_gateways(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5d18077851536aad976972dffe900741f397b7339e333381ce7c1dab2fd0a60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wirelessGateways", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotwireless.CfnNetworkAnalyzerConfiguration.TraceContentProperty",
        jsii_struct_bases=[],
        name_mapping={
            "log_level": "logLevel",
            "wireless_device_frame_info": "wirelessDeviceFrameInfo",
        },
    )
    class TraceContentProperty:
        def __init__(
            self,
            *,
            log_level: typing.Optional[builtins.str] = None,
            wireless_device_frame_info: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param log_level: ``CfnNetworkAnalyzerConfiguration.TraceContentProperty.LogLevel``.
            :param wireless_device_frame_info: ``CfnNetworkAnalyzerConfiguration.TraceContentProperty.WirelessDeviceFrameInfo``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-networkanalyzerconfiguration-tracecontent.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_iotwireless as iotwireless
                
                trace_content_property = iotwireless.CfnNetworkAnalyzerConfiguration.TraceContentProperty(
                    log_level="logLevel",
                    wireless_device_frame_info="wirelessDeviceFrameInfo"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__62e528c8e83ed1e47d66e196d0f9b1d67bd658d26a7c43bc9a0e0c4e590aebbc)
                check_type(argname="argument log_level", value=log_level, expected_type=type_hints["log_level"])
                check_type(argname="argument wireless_device_frame_info", value=wireless_device_frame_info, expected_type=type_hints["wireless_device_frame_info"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if log_level is not None:
                self._values["log_level"] = log_level
            if wireless_device_frame_info is not None:
                self._values["wireless_device_frame_info"] = wireless_device_frame_info

        @builtins.property
        def log_level(self) -> typing.Optional[builtins.str]:
            '''``CfnNetworkAnalyzerConfiguration.TraceContentProperty.LogLevel``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-networkanalyzerconfiguration-tracecontent.html#cfn-iotwireless-networkanalyzerconfiguration-tracecontent-loglevel
            '''
            result = self._values.get("log_level")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def wireless_device_frame_info(self) -> typing.Optional[builtins.str]:
            '''``CfnNetworkAnalyzerConfiguration.TraceContentProperty.WirelessDeviceFrameInfo``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-networkanalyzerconfiguration-tracecontent.html#cfn-iotwireless-networkanalyzerconfiguration-tracecontent-wirelessdeviceframeinfo
            '''
            result = self._values.get("wireless_device_frame_info")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TraceContentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-iotwireless.CfnNetworkAnalyzerConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "description": "description",
        "tags": "tags",
        "trace_content": "traceContent",
        "wireless_devices": "wirelessDevices",
        "wireless_gateways": "wirelessGateways",
    },
)
class CfnNetworkAnalyzerConfigurationProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
        trace_content: typing.Any = None,
        wireless_devices: typing.Optional[typing.Sequence[builtins.str]] = None,
        wireless_gateways: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnNetworkAnalyzerConfiguration``.

        :param name: Name of the network analyzer configuration.
        :param description: The description of the resource.
        :param tags: The tags to attach to the specified resource. Tags are metadata that you can use to manage a resource.
        :param trace_content: Trace content for your wireless gateway and wireless device resources.
        :param wireless_devices: Wireless device resources to add to the network analyzer configuration. Provide the ``WirelessDeviceId`` of the resource to add in the input array.
        :param wireless_gateways: Wireless gateway resources to add to the network analyzer configuration. Provide the ``WirelessGatewayId`` of the resource to add in the input array.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-networkanalyzerconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_iotwireless as iotwireless
            
            # trace_content: Any
            
            cfn_network_analyzer_configuration_props = iotwireless.CfnNetworkAnalyzerConfigurationProps(
                name="name",
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                trace_content=trace_content,
                wireless_devices=["wirelessDevices"],
                wireless_gateways=["wirelessGateways"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14b9c0811c4a82e27972c18d49cfc19d2dfeff1e5299795b35da2982117d441c)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument trace_content", value=trace_content, expected_type=type_hints["trace_content"])
            check_type(argname="argument wireless_devices", value=wireless_devices, expected_type=type_hints["wireless_devices"])
            check_type(argname="argument wireless_gateways", value=wireless_gateways, expected_type=type_hints["wireless_gateways"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags
        if trace_content is not None:
            self._values["trace_content"] = trace_content
        if wireless_devices is not None:
            self._values["wireless_devices"] = wireless_devices
        if wireless_gateways is not None:
            self._values["wireless_gateways"] = wireless_gateways

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the network analyzer configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-networkanalyzerconfiguration.html#cfn-iotwireless-networkanalyzerconfiguration-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-networkanalyzerconfiguration.html#cfn-iotwireless-networkanalyzerconfiguration-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]]:
        '''The tags to attach to the specified resource.

        Tags are metadata that you can use to manage a resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-networkanalyzerconfiguration.html#cfn-iotwireless-networkanalyzerconfiguration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]], result)

    @builtins.property
    def trace_content(self) -> typing.Any:
        '''Trace content for your wireless gateway and wireless device resources.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-networkanalyzerconfiguration.html#cfn-iotwireless-networkanalyzerconfiguration-tracecontent
        '''
        result = self._values.get("trace_content")
        return typing.cast(typing.Any, result)

    @builtins.property
    def wireless_devices(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Wireless device resources to add to the network analyzer configuration.

        Provide the ``WirelessDeviceId`` of the resource to add in the input array.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-networkanalyzerconfiguration.html#cfn-iotwireless-networkanalyzerconfiguration-wirelessdevices
        '''
        result = self._values.get("wireless_devices")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def wireless_gateways(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Wireless gateway resources to add to the network analyzer configuration.

        Provide the ``WirelessGatewayId`` of the resource to add in the input array.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-networkanalyzerconfiguration.html#cfn-iotwireless-networkanalyzerconfiguration-wirelessgateways
        '''
        result = self._values.get("wireless_gateways")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNetworkAnalyzerConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnPartnerAccount(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-iotwireless.CfnPartnerAccount",
):
    '''A CloudFormation ``AWS::IoTWireless::PartnerAccount``.

    A partner account. If ``PartnerAccountId`` and ``PartnerType`` are ``null`` , returns all partner accounts.

    :cloudformationResource: AWS::IoTWireless::PartnerAccount
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_iotwireless as iotwireless
        
        cfn_partner_account = iotwireless.CfnPartnerAccount(self, "MyCfnPartnerAccount",
            account_linked=False,
            fingerprint="fingerprint",
            partner_account_id="partnerAccountId",
            partner_type="partnerType",
            sidewalk=iotwireless.CfnPartnerAccount.SidewalkAccountInfoProperty(
                app_server_private_key="appServerPrivateKey"
            ),
            sidewalk_update=iotwireless.CfnPartnerAccount.SidewalkUpdateAccountProperty(
                app_server_private_key="appServerPrivateKey"
            ),
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
        account_linked: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
        fingerprint: typing.Optional[builtins.str] = None,
        partner_account_id: typing.Optional[builtins.str] = None,
        partner_type: typing.Optional[builtins.str] = None,
        sidewalk: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnPartnerAccount.SidewalkAccountInfoProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        sidewalk_update: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnPartnerAccount.SidewalkUpdateAccountProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::IoTWireless::PartnerAccount``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param account_linked: ``AWS::IoTWireless::PartnerAccount.AccountLinked``.
        :param fingerprint: ``AWS::IoTWireless::PartnerAccount.Fingerprint``.
        :param partner_account_id: The ID of the partner account to update.
        :param partner_type: ``AWS::IoTWireless::PartnerAccount.PartnerType``.
        :param sidewalk: The Sidewalk account credentials.
        :param sidewalk_update: ``AWS::IoTWireless::PartnerAccount.SidewalkUpdate``.
        :param tags: The tags are an array of key-value pairs to attach to the specified resource. Tags can have a minimum of 0 and a maximum of 50 items.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70fa94c1bc06e6c68aa2fb8408642703cf7651fcca48eee0a681153c5361bfc4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPartnerAccountProps(
            account_linked=account_linked,
            fingerprint=fingerprint,
            partner_account_id=partner_account_id,
            partner_type=partner_type,
            sidewalk=sidewalk,
            sidewalk_update=sidewalk_update,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__361d87c6c60da6c1a65dbc96b9d6f09302f8fe6b2551bc7d5ed16242aa3a05e9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e0e6929d69455bc76d2614d96d62c6c2f5e7d298052b3cd99d5be6e9e056683e)
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
        '''The Amazon Resource Name (ARN) of the resource.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrSidewalkResponseAmazonId")
    def attr_sidewalk_response_amazon_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: SidewalkResponse.AmazonId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSidewalkResponseAmazonId"))

    @builtins.property
    @jsii.member(jsii_name="attrSidewalkResponseArn")
    def attr_sidewalk_response_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: SidewalkResponse.Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSidewalkResponseArn"))

    @builtins.property
    @jsii.member(jsii_name="attrSidewalkResponseFingerprint")
    def attr_sidewalk_response_fingerprint(self) -> builtins.str:
        '''
        :cloudformationAttribute: SidewalkResponse.Fingerprint
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSidewalkResponseFingerprint"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _aws_cdk_core_f4b25747.TagManager:
        '''The tags are an array of key-value pairs to attach to the specified resource.

        Tags can have a minimum of 0 and a maximum of 50 items.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-tags
        '''
        return typing.cast(_aws_cdk_core_f4b25747.TagManager, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="accountLinked")
    def account_linked(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
        '''``AWS::IoTWireless::PartnerAccount.AccountLinked``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-accountlinked
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], jsii.get(self, "accountLinked"))

    @account_linked.setter
    def account_linked(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54c3658dd86f8c293397ceebb41841106b95ea260fd61b6ab5f04f09f37e8a1f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountLinked", value)

    @builtins.property
    @jsii.member(jsii_name="fingerprint")
    def fingerprint(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTWireless::PartnerAccount.Fingerprint``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-fingerprint
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fingerprint"))

    @fingerprint.setter
    def fingerprint(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1183306b1b10cd491c3bdbb0fcaa09113a705efd6407184bea12bd682f27f91a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fingerprint", value)

    @builtins.property
    @jsii.member(jsii_name="partnerAccountId")
    def partner_account_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the partner account to update.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-partneraccountid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "partnerAccountId"))

    @partner_account_id.setter
    def partner_account_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__968d6c73746e0ec8da5bb8f0b9470adc72e1c8cf2241ecfa9a1bd3a22e393f57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partnerAccountId", value)

    @builtins.property
    @jsii.member(jsii_name="partnerType")
    def partner_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTWireless::PartnerAccount.PartnerType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-partnertype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "partnerType"))

    @partner_type.setter
    def partner_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16046c75847d64ccb61aaf3f1e5226de8ac3ac2c7af34ee879fdbfcb85f07595)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partnerType", value)

    @builtins.property
    @jsii.member(jsii_name="sidewalk")
    def sidewalk(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnPartnerAccount.SidewalkAccountInfoProperty"]]:
        '''The Sidewalk account credentials.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-sidewalk
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnPartnerAccount.SidewalkAccountInfoProperty"]], jsii.get(self, "sidewalk"))

    @sidewalk.setter
    def sidewalk(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnPartnerAccount.SidewalkAccountInfoProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be9da21e25b74972fc3cccb1a59fa7790e236e910c522f33402511663fc89542)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sidewalk", value)

    @builtins.property
    @jsii.member(jsii_name="sidewalkUpdate")
    def sidewalk_update(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnPartnerAccount.SidewalkUpdateAccountProperty"]]:
        '''``AWS::IoTWireless::PartnerAccount.SidewalkUpdate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-sidewalkupdate
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnPartnerAccount.SidewalkUpdateAccountProperty"]], jsii.get(self, "sidewalkUpdate"))

    @sidewalk_update.setter
    def sidewalk_update(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnPartnerAccount.SidewalkUpdateAccountProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30de54314a9ba79d2acc51a5b90823a0c2b5ca7ce2eaa40df13553d911ec5a7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sidewalkUpdate", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotwireless.CfnPartnerAccount.SidewalkAccountInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"app_server_private_key": "appServerPrivateKey"},
    )
    class SidewalkAccountInfoProperty:
        def __init__(self, *, app_server_private_key: builtins.str) -> None:
            '''Information about a Sidewalk account.

            :param app_server_private_key: The Sidewalk application server private key. The application server private key is a secret key, which you should handle in a similar way as you would an application password. You can protect the application server private key by storing the value in the AWS Secrets Manager and use the `secretsmanager <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-secretsmanager>`_ to reference this value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-partneraccount-sidewalkaccountinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_iotwireless as iotwireless
                
                sidewalk_account_info_property = iotwireless.CfnPartnerAccount.SidewalkAccountInfoProperty(
                    app_server_private_key="appServerPrivateKey"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b46e7e557b3d3afeee1d77a34fe5a132c0912080c061e0a95d82ab815def6b65)
                check_type(argname="argument app_server_private_key", value=app_server_private_key, expected_type=type_hints["app_server_private_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "app_server_private_key": app_server_private_key,
            }

        @builtins.property
        def app_server_private_key(self) -> builtins.str:
            '''The Sidewalk application server private key.

            The application server private key is a secret key, which you should handle in a similar way as you would an application password. You can protect the application server private key by storing the value in the AWS Secrets Manager and use the `secretsmanager <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-secretsmanager>`_ to reference this value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-partneraccount-sidewalkaccountinfo.html#cfn-iotwireless-partneraccount-sidewalkaccountinfo-appserverprivatekey
            '''
            result = self._values.get("app_server_private_key")
            assert result is not None, "Required property 'app_server_private_key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SidewalkAccountInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotwireless.CfnPartnerAccount.SidewalkAccountInfoWithFingerprintProperty",
        jsii_struct_bases=[],
        name_mapping={
            "amazon_id": "amazonId",
            "arn": "arn",
            "fingerprint": "fingerprint",
        },
    )
    class SidewalkAccountInfoWithFingerprintProperty:
        def __init__(
            self,
            *,
            amazon_id: typing.Optional[builtins.str] = None,
            arn: typing.Optional[builtins.str] = None,
            fingerprint: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Information about a Sidewalk account.

            :param amazon_id: The Sidewalk Amazon ID.
            :param arn: The Amazon Resource Name (ARN) of the resource.
            :param fingerprint: The fingerprint of the Sidewalk application server private key.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-partneraccount-sidewalkaccountinfowithfingerprint.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_iotwireless as iotwireless
                
                sidewalk_account_info_with_fingerprint_property = iotwireless.CfnPartnerAccount.SidewalkAccountInfoWithFingerprintProperty(
                    amazon_id="amazonId",
                    arn="arn",
                    fingerprint="fingerprint"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b049fcd6c2dd99820d74621419ff2d298754483761f2e7a3c6d1c7201b7cb63d)
                check_type(argname="argument amazon_id", value=amazon_id, expected_type=type_hints["amazon_id"])
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
                check_type(argname="argument fingerprint", value=fingerprint, expected_type=type_hints["fingerprint"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if amazon_id is not None:
                self._values["amazon_id"] = amazon_id
            if arn is not None:
                self._values["arn"] = arn
            if fingerprint is not None:
                self._values["fingerprint"] = fingerprint

        @builtins.property
        def amazon_id(self) -> typing.Optional[builtins.str]:
            '''The Sidewalk Amazon ID.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-partneraccount-sidewalkaccountinfowithfingerprint.html#cfn-iotwireless-partneraccount-sidewalkaccountinfowithfingerprint-amazonid
            '''
            result = self._values.get("amazon_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the resource.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-partneraccount-sidewalkaccountinfowithfingerprint.html#cfn-iotwireless-partneraccount-sidewalkaccountinfowithfingerprint-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def fingerprint(self) -> typing.Optional[builtins.str]:
            '''The fingerprint of the Sidewalk application server private key.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-partneraccount-sidewalkaccountinfowithfingerprint.html#cfn-iotwireless-partneraccount-sidewalkaccountinfowithfingerprint-fingerprint
            '''
            result = self._values.get("fingerprint")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SidewalkAccountInfoWithFingerprintProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotwireless.CfnPartnerAccount.SidewalkUpdateAccountProperty",
        jsii_struct_bases=[],
        name_mapping={"app_server_private_key": "appServerPrivateKey"},
    )
    class SidewalkUpdateAccountProperty:
        def __init__(
            self,
            *,
            app_server_private_key: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Sidewalk update.

            :param app_server_private_key: The new Sidewalk application server private key.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-partneraccount-sidewalkupdateaccount.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_iotwireless as iotwireless
                
                sidewalk_update_account_property = iotwireless.CfnPartnerAccount.SidewalkUpdateAccountProperty(
                    app_server_private_key="appServerPrivateKey"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fb7cc79f47ef6e08577cb3eb6b56f8b6dd8e8a60703b4ab85fab0f10c4708237)
                check_type(argname="argument app_server_private_key", value=app_server_private_key, expected_type=type_hints["app_server_private_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if app_server_private_key is not None:
                self._values["app_server_private_key"] = app_server_private_key

        @builtins.property
        def app_server_private_key(self) -> typing.Optional[builtins.str]:
            '''The new Sidewalk application server private key.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-partneraccount-sidewalkupdateaccount.html#cfn-iotwireless-partneraccount-sidewalkupdateaccount-appserverprivatekey
            '''
            result = self._values.get("app_server_private_key")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SidewalkUpdateAccountProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-iotwireless.CfnPartnerAccountProps",
    jsii_struct_bases=[],
    name_mapping={
        "account_linked": "accountLinked",
        "fingerprint": "fingerprint",
        "partner_account_id": "partnerAccountId",
        "partner_type": "partnerType",
        "sidewalk": "sidewalk",
        "sidewalk_update": "sidewalkUpdate",
        "tags": "tags",
    },
)
class CfnPartnerAccountProps:
    def __init__(
        self,
        *,
        account_linked: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
        fingerprint: typing.Optional[builtins.str] = None,
        partner_account_id: typing.Optional[builtins.str] = None,
        partner_type: typing.Optional[builtins.str] = None,
        sidewalk: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnPartnerAccount.SidewalkAccountInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        sidewalk_update: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnPartnerAccount.SidewalkUpdateAccountProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPartnerAccount``.

        :param account_linked: ``AWS::IoTWireless::PartnerAccount.AccountLinked``.
        :param fingerprint: ``AWS::IoTWireless::PartnerAccount.Fingerprint``.
        :param partner_account_id: The ID of the partner account to update.
        :param partner_type: ``AWS::IoTWireless::PartnerAccount.PartnerType``.
        :param sidewalk: The Sidewalk account credentials.
        :param sidewalk_update: ``AWS::IoTWireless::PartnerAccount.SidewalkUpdate``.
        :param tags: The tags are an array of key-value pairs to attach to the specified resource. Tags can have a minimum of 0 and a maximum of 50 items.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_iotwireless as iotwireless
            
            cfn_partner_account_props = iotwireless.CfnPartnerAccountProps(
                account_linked=False,
                fingerprint="fingerprint",
                partner_account_id="partnerAccountId",
                partner_type="partnerType",
                sidewalk=iotwireless.CfnPartnerAccount.SidewalkAccountInfoProperty(
                    app_server_private_key="appServerPrivateKey"
                ),
                sidewalk_update=iotwireless.CfnPartnerAccount.SidewalkUpdateAccountProperty(
                    app_server_private_key="appServerPrivateKey"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0134fa6a451b04e0c7892ec364f0aeed88594db85f4499f076f7082172c88b64)
            check_type(argname="argument account_linked", value=account_linked, expected_type=type_hints["account_linked"])
            check_type(argname="argument fingerprint", value=fingerprint, expected_type=type_hints["fingerprint"])
            check_type(argname="argument partner_account_id", value=partner_account_id, expected_type=type_hints["partner_account_id"])
            check_type(argname="argument partner_type", value=partner_type, expected_type=type_hints["partner_type"])
            check_type(argname="argument sidewalk", value=sidewalk, expected_type=type_hints["sidewalk"])
            check_type(argname="argument sidewalk_update", value=sidewalk_update, expected_type=type_hints["sidewalk_update"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if account_linked is not None:
            self._values["account_linked"] = account_linked
        if fingerprint is not None:
            self._values["fingerprint"] = fingerprint
        if partner_account_id is not None:
            self._values["partner_account_id"] = partner_account_id
        if partner_type is not None:
            self._values["partner_type"] = partner_type
        if sidewalk is not None:
            self._values["sidewalk"] = sidewalk
        if sidewalk_update is not None:
            self._values["sidewalk_update"] = sidewalk_update
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def account_linked(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
        '''``AWS::IoTWireless::PartnerAccount.AccountLinked``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-accountlinked
        '''
        result = self._values.get("account_linked")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

    @builtins.property
    def fingerprint(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTWireless::PartnerAccount.Fingerprint``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-fingerprint
        '''
        result = self._values.get("fingerprint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def partner_account_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the partner account to update.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-partneraccountid
        '''
        result = self._values.get("partner_account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def partner_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTWireless::PartnerAccount.PartnerType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-partnertype
        '''
        result = self._values.get("partner_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sidewalk(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnPartnerAccount.SidewalkAccountInfoProperty]]:
        '''The Sidewalk account credentials.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-sidewalk
        '''
        result = self._values.get("sidewalk")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnPartnerAccount.SidewalkAccountInfoProperty]], result)

    @builtins.property
    def sidewalk_update(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnPartnerAccount.SidewalkUpdateAccountProperty]]:
        '''``AWS::IoTWireless::PartnerAccount.SidewalkUpdate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-sidewalkupdate
        '''
        result = self._values.get("sidewalk_update")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnPartnerAccount.SidewalkUpdateAccountProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]]:
        '''The tags are an array of key-value pairs to attach to the specified resource.

        Tags can have a minimum of 0 and a maximum of 50 items.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-partneraccount.html#cfn-iotwireless-partneraccount-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPartnerAccountProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnServiceProfile(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-iotwireless.CfnServiceProfile",
):
    '''A CloudFormation ``AWS::IoTWireless::ServiceProfile``.

    Creates a new service profile.

    :cloudformationResource: AWS::IoTWireless::ServiceProfile
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_iotwireless as iotwireless
        
        cfn_service_profile = iotwireless.CfnServiceProfile(self, "MyCfnServiceProfile",
            lo_ra_wan=iotwireless.CfnServiceProfile.LoRaWANServiceProfileProperty(
                add_gw_metadata=False,
                channel_mask="channelMask",
                dev_status_req_freq=123,
                dl_bucket_size=123,
                dl_rate=123,
                dl_rate_policy="dlRatePolicy",
                dr_max=123,
                dr_min=123,
                hr_allowed=False,
                min_gw_diversity=123,
                nwk_geo_loc=False,
                pr_allowed=False,
                ra_allowed=False,
                report_dev_status_battery=False,
                report_dev_status_margin=False,
                target_per=123,
                ul_bucket_size=123,
                ul_rate=123,
                ul_rate_policy="ulRatePolicy"
            ),
            name="name",
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
        lo_ra_wan: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnServiceProfile.LoRaWANServiceProfileProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::IoTWireless::ServiceProfile``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param lo_ra_wan: LoRaWAN service profile object.
        :param name: The name of the new resource.
        :param tags: The tags are an array of key-value pairs to attach to the specified resource. Tags can have a minimum of 0 and a maximum of 50 items.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7dbd2107f56db404db84d056e6501ffc6e000bb87f7182a023832a1484ae229)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnServiceProfileProps(lo_ra_wan=lo_ra_wan, name=name, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02f0e00dafa7fc99f30699ab4ba046138def30ed247810ca72b4ec35158ef92a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4f2bdce7658589ce40b4c1f0bf84f034c4c77df7cc869b77cda2b67e03e3664f)
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
        '''The ARN of the service profile created.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the service profile created.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrLoRaWanChannelMask")
    def attr_lo_ra_wan_channel_mask(self) -> builtins.str:
        '''The ChannelMask value.

        :cloudformationAttribute: LoRaWAN.ChannelMask
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLoRaWanChannelMask"))

    @builtins.property
    @jsii.member(jsii_name="attrLoRaWanDevStatusReqFreq")
    def attr_lo_ra_wan_dev_status_req_freq(self) -> jsii.Number:
        '''The DevStatusReqFreq value.

        :cloudformationAttribute: LoRaWAN.DevStatusReqFreq
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrLoRaWanDevStatusReqFreq"))

    @builtins.property
    @jsii.member(jsii_name="attrLoRaWanDlBucketSize")
    def attr_lo_ra_wan_dl_bucket_size(self) -> jsii.Number:
        '''The DLBucketSize value.

        :cloudformationAttribute: LoRaWAN.DlBucketSize
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrLoRaWanDlBucketSize"))

    @builtins.property
    @jsii.member(jsii_name="attrLoRaWanDlRate")
    def attr_lo_ra_wan_dl_rate(self) -> jsii.Number:
        '''The DLRate value.

        :cloudformationAttribute: LoRaWAN.DlRate
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrLoRaWanDlRate"))

    @builtins.property
    @jsii.member(jsii_name="attrLoRaWanDlRatePolicy")
    def attr_lo_ra_wan_dl_rate_policy(self) -> builtins.str:
        '''The DLRatePolicy value.

        :cloudformationAttribute: LoRaWAN.DlRatePolicy
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLoRaWanDlRatePolicy"))

    @builtins.property
    @jsii.member(jsii_name="attrLoRaWanDrMax")
    def attr_lo_ra_wan_dr_max(self) -> jsii.Number:
        '''The DRMax value.

        :cloudformationAttribute: LoRaWAN.DrMax
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrLoRaWanDrMax"))

    @builtins.property
    @jsii.member(jsii_name="attrLoRaWanDrMin")
    def attr_lo_ra_wan_dr_min(self) -> jsii.Number:
        '''The DRMin value.

        :cloudformationAttribute: LoRaWAN.DrMin
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrLoRaWanDrMin"))

    @builtins.property
    @jsii.member(jsii_name="attrLoRaWanHrAllowed")
    def attr_lo_ra_wan_hr_allowed(self) -> _aws_cdk_core_f4b25747.IResolvable:
        '''The HRAllowed value that describes whether handover roaming is allowed.

        :cloudformationAttribute: LoRaWAN.HrAllowed
        '''
        return typing.cast(_aws_cdk_core_f4b25747.IResolvable, jsii.get(self, "attrLoRaWanHrAllowed"))

    @builtins.property
    @jsii.member(jsii_name="attrLoRaWanMinGwDiversity")
    def attr_lo_ra_wan_min_gw_diversity(self) -> jsii.Number:
        '''The MinGwDiversity value.

        :cloudformationAttribute: LoRaWAN.MinGwDiversity
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrLoRaWanMinGwDiversity"))

    @builtins.property
    @jsii.member(jsii_name="attrLoRaWanNwkGeoLoc")
    def attr_lo_ra_wan_nwk_geo_loc(self) -> _aws_cdk_core_f4b25747.IResolvable:
        '''The NwkGeoLoc value.

        :cloudformationAttribute: LoRaWAN.NwkGeoLoc
        '''
        return typing.cast(_aws_cdk_core_f4b25747.IResolvable, jsii.get(self, "attrLoRaWanNwkGeoLoc"))

    @builtins.property
    @jsii.member(jsii_name="attrLoRaWanPrAllowed")
    def attr_lo_ra_wan_pr_allowed(self) -> _aws_cdk_core_f4b25747.IResolvable:
        '''The PRAllowed value that describes whether passive roaming is allowed.

        :cloudformationAttribute: LoRaWAN.PrAllowed
        '''
        return typing.cast(_aws_cdk_core_f4b25747.IResolvable, jsii.get(self, "attrLoRaWanPrAllowed"))

    @builtins.property
    @jsii.member(jsii_name="attrLoRaWanRaAllowed")
    def attr_lo_ra_wan_ra_allowed(self) -> _aws_cdk_core_f4b25747.IResolvable:
        '''The RAAllowed value that describes whether roaming activation is allowed.

        :cloudformationAttribute: LoRaWAN.RaAllowed
        '''
        return typing.cast(_aws_cdk_core_f4b25747.IResolvable, jsii.get(self, "attrLoRaWanRaAllowed"))

    @builtins.property
    @jsii.member(jsii_name="attrLoRaWanReportDevStatusBattery")
    def attr_lo_ra_wan_report_dev_status_battery(
        self,
    ) -> _aws_cdk_core_f4b25747.IResolvable:
        '''The ReportDevStatusBattery value.

        :cloudformationAttribute: LoRaWAN.ReportDevStatusBattery
        '''
        return typing.cast(_aws_cdk_core_f4b25747.IResolvable, jsii.get(self, "attrLoRaWanReportDevStatusBattery"))

    @builtins.property
    @jsii.member(jsii_name="attrLoRaWanReportDevStatusMargin")
    def attr_lo_ra_wan_report_dev_status_margin(
        self,
    ) -> _aws_cdk_core_f4b25747.IResolvable:
        '''The ReportDevStatusMargin value.

        :cloudformationAttribute: LoRaWAN.ReportDevStatusMargin
        '''
        return typing.cast(_aws_cdk_core_f4b25747.IResolvable, jsii.get(self, "attrLoRaWanReportDevStatusMargin"))

    @builtins.property
    @jsii.member(jsii_name="attrLoRaWanResponse")
    def attr_lo_ra_wan_response(self) -> _aws_cdk_core_f4b25747.IResolvable:
        '''
        :cloudformationAttribute: LoRaWANResponse
        '''
        return typing.cast(_aws_cdk_core_f4b25747.IResolvable, jsii.get(self, "attrLoRaWanResponse"))

    @builtins.property
    @jsii.member(jsii_name="attrLoRaWanTargetPer")
    def attr_lo_ra_wan_target_per(self) -> jsii.Number:
        '''The TargetPer value.

        :cloudformationAttribute: LoRaWAN.TargetPer
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrLoRaWanTargetPer"))

    @builtins.property
    @jsii.member(jsii_name="attrLoRaWanUlBucketSize")
    def attr_lo_ra_wan_ul_bucket_size(self) -> jsii.Number:
        '''The UlBucketSize value.

        :cloudformationAttribute: LoRaWAN.UlBucketSize
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrLoRaWanUlBucketSize"))

    @builtins.property
    @jsii.member(jsii_name="attrLoRaWanUlRate")
    def attr_lo_ra_wan_ul_rate(self) -> jsii.Number:
        '''The ULRate value.

        :cloudformationAttribute: LoRaWAN.UlRate
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrLoRaWanUlRate"))

    @builtins.property
    @jsii.member(jsii_name="attrLoRaWanUlRatePolicy")
    def attr_lo_ra_wan_ul_rate_policy(self) -> builtins.str:
        '''The ULRatePolicy value.

        :cloudformationAttribute: LoRaWAN.UlRatePolicy
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLoRaWanUlRatePolicy"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _aws_cdk_core_f4b25747.TagManager:
        '''The tags are an array of key-value pairs to attach to the specified resource.

        Tags can have a minimum of 0 and a maximum of 50 items.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#cfn-iotwireless-serviceprofile-tags
        '''
        return typing.cast(_aws_cdk_core_f4b25747.TagManager, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="loRaWan")
    def lo_ra_wan(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnServiceProfile.LoRaWANServiceProfileProperty"]]:
        '''LoRaWAN service profile object.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#cfn-iotwireless-serviceprofile-lorawan
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnServiceProfile.LoRaWANServiceProfileProperty"]], jsii.get(self, "loRaWan"))

    @lo_ra_wan.setter
    def lo_ra_wan(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnServiceProfile.LoRaWANServiceProfileProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1018d5d0ec6563797cbbcb2c4caf64a35ebe16b38b14a32585a201d64b2223b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loRaWan", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the new resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#cfn-iotwireless-serviceprofile-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4b5c0ad26d176237f37fa4f10f8b549f2d9b05e89e5d24253ff9b6d1884ed7e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotwireless.CfnServiceProfile.LoRaWANServiceProfileProperty",
        jsii_struct_bases=[],
        name_mapping={
            "add_gw_metadata": "addGwMetadata",
            "channel_mask": "channelMask",
            "dev_status_req_freq": "devStatusReqFreq",
            "dl_bucket_size": "dlBucketSize",
            "dl_rate": "dlRate",
            "dl_rate_policy": "dlRatePolicy",
            "dr_max": "drMax",
            "dr_min": "drMin",
            "hr_allowed": "hrAllowed",
            "min_gw_diversity": "minGwDiversity",
            "nwk_geo_loc": "nwkGeoLoc",
            "pr_allowed": "prAllowed",
            "ra_allowed": "raAllowed",
            "report_dev_status_battery": "reportDevStatusBattery",
            "report_dev_status_margin": "reportDevStatusMargin",
            "target_per": "targetPer",
            "ul_bucket_size": "ulBucketSize",
            "ul_rate": "ulRate",
            "ul_rate_policy": "ulRatePolicy",
        },
    )
    class LoRaWANServiceProfileProperty:
        def __init__(
            self,
            *,
            add_gw_metadata: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            channel_mask: typing.Optional[builtins.str] = None,
            dev_status_req_freq: typing.Optional[jsii.Number] = None,
            dl_bucket_size: typing.Optional[jsii.Number] = None,
            dl_rate: typing.Optional[jsii.Number] = None,
            dl_rate_policy: typing.Optional[builtins.str] = None,
            dr_max: typing.Optional[jsii.Number] = None,
            dr_min: typing.Optional[jsii.Number] = None,
            hr_allowed: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            min_gw_diversity: typing.Optional[jsii.Number] = None,
            nwk_geo_loc: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            pr_allowed: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            ra_allowed: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            report_dev_status_battery: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            report_dev_status_margin: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            target_per: typing.Optional[jsii.Number] = None,
            ul_bucket_size: typing.Optional[jsii.Number] = None,
            ul_rate: typing.Optional[jsii.Number] = None,
            ul_rate_policy: typing.Optional[builtins.str] = None,
        ) -> None:
            '''LoRaWANServiceProfile object.

            :param add_gw_metadata: The AddGWMetaData value.
            :param channel_mask: The ChannelMask value. This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``
            :param dev_status_req_freq: The DevStatusReqFreq value. This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``
            :param dl_bucket_size: The DLBucketSize value. This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``
            :param dl_rate: The DLRate value. This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``
            :param dl_rate_policy: The DLRatePolicy value. This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``
            :param dr_max: The DRMax value. This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``
            :param dr_min: The DRMin value. This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``
            :param hr_allowed: The HRAllowed value that describes whether handover roaming is allowed. This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``
            :param min_gw_diversity: The MinGwDiversity value. This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``
            :param nwk_geo_loc: The NwkGeoLoc value. This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``
            :param pr_allowed: The PRAllowed value that describes whether passive roaming is allowed. This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``
            :param ra_allowed: The RAAllowed value that describes whether roaming activation is allowed.
            :param report_dev_status_battery: The ReportDevStatusBattery value. This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``
            :param report_dev_status_margin: The ReportDevStatusMargin value. This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``
            :param target_per: The TargetPer value. This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``
            :param ul_bucket_size: The UlBucketSize value. This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``
            :param ul_rate: The ULRate value. This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``
            :param ul_rate_policy: The ULRatePolicy value. This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_iotwireless as iotwireless
                
                lo_ra_wANService_profile_property = iotwireless.CfnServiceProfile.LoRaWANServiceProfileProperty(
                    add_gw_metadata=False,
                    channel_mask="channelMask",
                    dev_status_req_freq=123,
                    dl_bucket_size=123,
                    dl_rate=123,
                    dl_rate_policy="dlRatePolicy",
                    dr_max=123,
                    dr_min=123,
                    hr_allowed=False,
                    min_gw_diversity=123,
                    nwk_geo_loc=False,
                    pr_allowed=False,
                    ra_allowed=False,
                    report_dev_status_battery=False,
                    report_dev_status_margin=False,
                    target_per=123,
                    ul_bucket_size=123,
                    ul_rate=123,
                    ul_rate_policy="ulRatePolicy"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__33dce9396f76e7b3fc8db88e167d0eacc3f17c554287d779def7c57e33267d9b)
                check_type(argname="argument add_gw_metadata", value=add_gw_metadata, expected_type=type_hints["add_gw_metadata"])
                check_type(argname="argument channel_mask", value=channel_mask, expected_type=type_hints["channel_mask"])
                check_type(argname="argument dev_status_req_freq", value=dev_status_req_freq, expected_type=type_hints["dev_status_req_freq"])
                check_type(argname="argument dl_bucket_size", value=dl_bucket_size, expected_type=type_hints["dl_bucket_size"])
                check_type(argname="argument dl_rate", value=dl_rate, expected_type=type_hints["dl_rate"])
                check_type(argname="argument dl_rate_policy", value=dl_rate_policy, expected_type=type_hints["dl_rate_policy"])
                check_type(argname="argument dr_max", value=dr_max, expected_type=type_hints["dr_max"])
                check_type(argname="argument dr_min", value=dr_min, expected_type=type_hints["dr_min"])
                check_type(argname="argument hr_allowed", value=hr_allowed, expected_type=type_hints["hr_allowed"])
                check_type(argname="argument min_gw_diversity", value=min_gw_diversity, expected_type=type_hints["min_gw_diversity"])
                check_type(argname="argument nwk_geo_loc", value=nwk_geo_loc, expected_type=type_hints["nwk_geo_loc"])
                check_type(argname="argument pr_allowed", value=pr_allowed, expected_type=type_hints["pr_allowed"])
                check_type(argname="argument ra_allowed", value=ra_allowed, expected_type=type_hints["ra_allowed"])
                check_type(argname="argument report_dev_status_battery", value=report_dev_status_battery, expected_type=type_hints["report_dev_status_battery"])
                check_type(argname="argument report_dev_status_margin", value=report_dev_status_margin, expected_type=type_hints["report_dev_status_margin"])
                check_type(argname="argument target_per", value=target_per, expected_type=type_hints["target_per"])
                check_type(argname="argument ul_bucket_size", value=ul_bucket_size, expected_type=type_hints["ul_bucket_size"])
                check_type(argname="argument ul_rate", value=ul_rate, expected_type=type_hints["ul_rate"])
                check_type(argname="argument ul_rate_policy", value=ul_rate_policy, expected_type=type_hints["ul_rate_policy"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if add_gw_metadata is not None:
                self._values["add_gw_metadata"] = add_gw_metadata
            if channel_mask is not None:
                self._values["channel_mask"] = channel_mask
            if dev_status_req_freq is not None:
                self._values["dev_status_req_freq"] = dev_status_req_freq
            if dl_bucket_size is not None:
                self._values["dl_bucket_size"] = dl_bucket_size
            if dl_rate is not None:
                self._values["dl_rate"] = dl_rate
            if dl_rate_policy is not None:
                self._values["dl_rate_policy"] = dl_rate_policy
            if dr_max is not None:
                self._values["dr_max"] = dr_max
            if dr_min is not None:
                self._values["dr_min"] = dr_min
            if hr_allowed is not None:
                self._values["hr_allowed"] = hr_allowed
            if min_gw_diversity is not None:
                self._values["min_gw_diversity"] = min_gw_diversity
            if nwk_geo_loc is not None:
                self._values["nwk_geo_loc"] = nwk_geo_loc
            if pr_allowed is not None:
                self._values["pr_allowed"] = pr_allowed
            if ra_allowed is not None:
                self._values["ra_allowed"] = ra_allowed
            if report_dev_status_battery is not None:
                self._values["report_dev_status_battery"] = report_dev_status_battery
            if report_dev_status_margin is not None:
                self._values["report_dev_status_margin"] = report_dev_status_margin
            if target_per is not None:
                self._values["target_per"] = target_per
            if ul_bucket_size is not None:
                self._values["ul_bucket_size"] = ul_bucket_size
            if ul_rate is not None:
                self._values["ul_rate"] = ul_rate
            if ul_rate_policy is not None:
                self._values["ul_rate_policy"] = ul_rate_policy

        @builtins.property
        def add_gw_metadata(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''The AddGWMetaData value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-addgwmetadata
            '''
            result = self._values.get("add_gw_metadata")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def channel_mask(self) -> typing.Optional[builtins.str]:
            '''The ChannelMask value.

            This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-channelmask
            '''
            result = self._values.get("channel_mask")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def dev_status_req_freq(self) -> typing.Optional[jsii.Number]:
            '''The DevStatusReqFreq value.

            This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-devstatusreqfreq
            '''
            result = self._values.get("dev_status_req_freq")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def dl_bucket_size(self) -> typing.Optional[jsii.Number]:
            '''The DLBucketSize value.

            This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-dlbucketsize
            '''
            result = self._values.get("dl_bucket_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def dl_rate(self) -> typing.Optional[jsii.Number]:
            '''The DLRate value.

            This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-dlrate
            '''
            result = self._values.get("dl_rate")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def dl_rate_policy(self) -> typing.Optional[builtins.str]:
            '''The DLRatePolicy value.

            This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-dlratepolicy
            '''
            result = self._values.get("dl_rate_policy")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def dr_max(self) -> typing.Optional[jsii.Number]:
            '''The DRMax value.

            This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-drmax
            '''
            result = self._values.get("dr_max")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def dr_min(self) -> typing.Optional[jsii.Number]:
            '''The DRMin value.

            This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-drmin
            '''
            result = self._values.get("dr_min")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def hr_allowed(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''The HRAllowed value that describes whether handover roaming is allowed.

            This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-hrallowed
            '''
            result = self._values.get("hr_allowed")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def min_gw_diversity(self) -> typing.Optional[jsii.Number]:
            '''The MinGwDiversity value.

            This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-mingwdiversity
            '''
            result = self._values.get("min_gw_diversity")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def nwk_geo_loc(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''The NwkGeoLoc value.

            This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-nwkgeoloc
            '''
            result = self._values.get("nwk_geo_loc")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def pr_allowed(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''The PRAllowed value that describes whether passive roaming is allowed.

            This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-prallowed
            '''
            result = self._values.get("pr_allowed")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def ra_allowed(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''The RAAllowed value that describes whether roaming activation is allowed.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-raallowed
            '''
            result = self._values.get("ra_allowed")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def report_dev_status_battery(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''The ReportDevStatusBattery value.

            This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-reportdevstatusbattery
            '''
            result = self._values.get("report_dev_status_battery")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def report_dev_status_margin(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''The ReportDevStatusMargin value.

            This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-reportdevstatusmargin
            '''
            result = self._values.get("report_dev_status_margin")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def target_per(self) -> typing.Optional[jsii.Number]:
            '''The TargetPer value.

            This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-targetper
            '''
            result = self._values.get("target_per")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def ul_bucket_size(self) -> typing.Optional[jsii.Number]:
            '''The UlBucketSize value.

            This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-ulbucketsize
            '''
            result = self._values.get("ul_bucket_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def ul_rate(self) -> typing.Optional[jsii.Number]:
            '''The ULRate value.

            This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-ulrate
            '''
            result = self._values.get("ul_rate")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def ul_rate_policy(self) -> typing.Optional[builtins.str]:
            '''The ULRatePolicy value.

            This property is ``ReadOnly`` and can't be inputted for create. It's returned with ``Fn::GetAtt``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-serviceprofile-lorawanserviceprofile.html#cfn-iotwireless-serviceprofile-lorawanserviceprofile-ulratepolicy
            '''
            result = self._values.get("ul_rate_policy")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoRaWANServiceProfileProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-iotwireless.CfnServiceProfileProps",
    jsii_struct_bases=[],
    name_mapping={"lo_ra_wan": "loRaWan", "name": "name", "tags": "tags"},
)
class CfnServiceProfileProps:
    def __init__(
        self,
        *,
        lo_ra_wan: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnServiceProfile.LoRaWANServiceProfileProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnServiceProfile``.

        :param lo_ra_wan: LoRaWAN service profile object.
        :param name: The name of the new resource.
        :param tags: The tags are an array of key-value pairs to attach to the specified resource. Tags can have a minimum of 0 and a maximum of 50 items.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_iotwireless as iotwireless
            
            cfn_service_profile_props = iotwireless.CfnServiceProfileProps(
                lo_ra_wan=iotwireless.CfnServiceProfile.LoRaWANServiceProfileProperty(
                    add_gw_metadata=False,
                    channel_mask="channelMask",
                    dev_status_req_freq=123,
                    dl_bucket_size=123,
                    dl_rate=123,
                    dl_rate_policy="dlRatePolicy",
                    dr_max=123,
                    dr_min=123,
                    hr_allowed=False,
                    min_gw_diversity=123,
                    nwk_geo_loc=False,
                    pr_allowed=False,
                    ra_allowed=False,
                    report_dev_status_battery=False,
                    report_dev_status_margin=False,
                    target_per=123,
                    ul_bucket_size=123,
                    ul_rate=123,
                    ul_rate_policy="ulRatePolicy"
                ),
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7a73d9cd4af9e2bfcb9ba2833b981c2f200576b6a8d4e3c3e3186a0ddd358cc)
            check_type(argname="argument lo_ra_wan", value=lo_ra_wan, expected_type=type_hints["lo_ra_wan"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if lo_ra_wan is not None:
            self._values["lo_ra_wan"] = lo_ra_wan
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def lo_ra_wan(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnServiceProfile.LoRaWANServiceProfileProperty]]:
        '''LoRaWAN service profile object.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#cfn-iotwireless-serviceprofile-lorawan
        '''
        result = self._values.get("lo_ra_wan")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnServiceProfile.LoRaWANServiceProfileProperty]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the new resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#cfn-iotwireless-serviceprofile-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]]:
        '''The tags are an array of key-value pairs to attach to the specified resource.

        Tags can have a minimum of 0 and a maximum of 50 items.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-serviceprofile.html#cfn-iotwireless-serviceprofile-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServiceProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnTaskDefinition(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-iotwireless.CfnTaskDefinition",
):
    '''A CloudFormation ``AWS::IoTWireless::TaskDefinition``.

    Creates a gateway task definition.

    :cloudformationResource: AWS::IoTWireless::TaskDefinition
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_iotwireless as iotwireless
        
        cfn_task_definition = iotwireless.CfnTaskDefinition(self, "MyCfnTaskDefinition",
            auto_create_tasks=False,
        
            # the properties below are optional
            lo_ra_wan_update_gateway_task_entry=iotwireless.CfnTaskDefinition.LoRaWANUpdateGatewayTaskEntryProperty(
                current_version=iotwireless.CfnTaskDefinition.LoRaWANGatewayVersionProperty(
                    model="model",
                    package_version="packageVersion",
                    station="station"
                ),
                update_version=iotwireless.CfnTaskDefinition.LoRaWANGatewayVersionProperty(
                    model="model",
                    package_version="packageVersion",
                    station="station"
                )
            ),
            name="name",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            task_definition_type="taskDefinitionType",
            update=iotwireless.CfnTaskDefinition.UpdateWirelessGatewayTaskCreateProperty(
                lo_ra_wan=iotwireless.CfnTaskDefinition.LoRaWANUpdateGatewayTaskCreateProperty(
                    current_version=iotwireless.CfnTaskDefinition.LoRaWANGatewayVersionProperty(
                        model="model",
                        package_version="packageVersion",
                        station="station"
                    ),
                    sig_key_crc=123,
                    update_signature="updateSignature",
                    update_version=iotwireless.CfnTaskDefinition.LoRaWANGatewayVersionProperty(
                        model="model",
                        package_version="packageVersion",
                        station="station"
                    )
                ),
                update_data_role="updateDataRole",
                update_data_source="updateDataSource"
            )
        )
    '''

    def __init__(
        self,
        scope: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        auto_create_tasks: typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable],
        lo_ra_wan_update_gateway_task_entry: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnTaskDefinition.LoRaWANUpdateGatewayTaskEntryProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
        task_definition_type: typing.Optional[builtins.str] = None,
        update: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnTaskDefinition.UpdateWirelessGatewayTaskCreateProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::IoTWireless::TaskDefinition``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param auto_create_tasks: Whether to automatically create tasks using this task definition for all gateways with the specified current version. If ``false`` , the task must me created by calling ``CreateWirelessGatewayTask`` .
        :param lo_ra_wan_update_gateway_task_entry: ``AWS::IoTWireless::TaskDefinition.LoRaWANUpdateGatewayTaskEntry``.
        :param name: The name of the new resource.
        :param tags: The tags are an array of key-value pairs to attach to the specified resource. Tags can have a minimum of 0 and a maximum of 50 items.
        :param task_definition_type: ``AWS::IoTWireless::TaskDefinition.TaskDefinitionType``.
        :param update: Information about the gateways to update.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1a898decb0ee15fbffbe4ea6b9137b63ee1c9d0aa59ffa7d14c8d5794ebf1d5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTaskDefinitionProps(
            auto_create_tasks=auto_create_tasks,
            lo_ra_wan_update_gateway_task_entry=lo_ra_wan_update_gateway_task_entry,
            name=name,
            tags=tags,
            task_definition_type=task_definition_type,
            update=update,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e540a0ecd0c87a779951f5b7f64357528afe84527bbf88db7329d647c18abdd8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f48db4c9acdbc97be0ad7b9950c3283769d89909a1e71ecc16ede5bc678adfda)
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
        '''The Amazon Resource Name of the resource.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the new wireless gateway task definition.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _aws_cdk_core_f4b25747.TagManager:
        '''The tags are an array of key-value pairs to attach to the specified resource.

        Tags can have a minimum of 0 and a maximum of 50 items.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-tags
        '''
        return typing.cast(_aws_cdk_core_f4b25747.TagManager, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="autoCreateTasks")
    def auto_create_tasks(
        self,
    ) -> typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]:
        '''Whether to automatically create tasks using this task definition for all gateways with the specified current version.

        If ``false`` , the task must me created by calling ``CreateWirelessGatewayTask`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-autocreatetasks
        '''
        return typing.cast(typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable], jsii.get(self, "autoCreateTasks"))

    @auto_create_tasks.setter
    def auto_create_tasks(
        self,
        value: typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61710283d06049b3691d6878062e3108f69e4909c7f117b6f7ee119dd8749e38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoCreateTasks", value)

    @builtins.property
    @jsii.member(jsii_name="loRaWanUpdateGatewayTaskEntry")
    def lo_ra_wan_update_gateway_task_entry(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnTaskDefinition.LoRaWANUpdateGatewayTaskEntryProperty"]]:
        '''``AWS::IoTWireless::TaskDefinition.LoRaWANUpdateGatewayTaskEntry``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskentry
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnTaskDefinition.LoRaWANUpdateGatewayTaskEntryProperty"]], jsii.get(self, "loRaWanUpdateGatewayTaskEntry"))

    @lo_ra_wan_update_gateway_task_entry.setter
    def lo_ra_wan_update_gateway_task_entry(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnTaskDefinition.LoRaWANUpdateGatewayTaskEntryProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc46980d503af071f2a1c6e0f7ea9f9e6f2325b771988d6eab1fce8e1783edc3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loRaWanUpdateGatewayTaskEntry", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the new resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__344198b16445ad641747a7dd1b1641325ca58892eddbfefa3fb4f7aa0bd0b98d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="taskDefinitionType")
    def task_definition_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTWireless::TaskDefinition.TaskDefinitionType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-taskdefinitiontype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "taskDefinitionType"))

    @task_definition_type.setter
    def task_definition_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0a0dc21e3824a8118f7b83ee26668d51e90092cb16dede2d05ec87f4c03b88e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskDefinitionType", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnTaskDefinition.UpdateWirelessGatewayTaskCreateProperty"]]:
        '''Information about the gateways to update.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-update
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnTaskDefinition.UpdateWirelessGatewayTaskCreateProperty"]], jsii.get(self, "update"))

    @update.setter
    def update(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnTaskDefinition.UpdateWirelessGatewayTaskCreateProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04812ec7d3b3ff2eb351e1d6e6c1d54ce2b5fda69f6d848e8445c0e1c56632e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotwireless.CfnTaskDefinition.LoRaWANGatewayVersionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "model": "model",
            "package_version": "packageVersion",
            "station": "station",
        },
    )
    class LoRaWANGatewayVersionProperty:
        def __init__(
            self,
            *,
            model: typing.Optional[builtins.str] = None,
            package_version: typing.Optional[builtins.str] = None,
            station: typing.Optional[builtins.str] = None,
        ) -> None:
            '''LoRaWANGatewayVersion object.

            :param model: The model number of the wireless gateway.
            :param package_version: The version of the wireless gateway firmware.
            :param station: The basic station version of the wireless gateway.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawangatewayversion.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_iotwireless as iotwireless
                
                lo_ra_wANGateway_version_property = iotwireless.CfnTaskDefinition.LoRaWANGatewayVersionProperty(
                    model="model",
                    package_version="packageVersion",
                    station="station"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__78d4a261f6b892a4248e96f0d4ec1d748d653d0bf50c58fc3705018219a45da9)
                check_type(argname="argument model", value=model, expected_type=type_hints["model"])
                check_type(argname="argument package_version", value=package_version, expected_type=type_hints["package_version"])
                check_type(argname="argument station", value=station, expected_type=type_hints["station"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if model is not None:
                self._values["model"] = model
            if package_version is not None:
                self._values["package_version"] = package_version
            if station is not None:
                self._values["station"] = station

        @builtins.property
        def model(self) -> typing.Optional[builtins.str]:
            '''The model number of the wireless gateway.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawangatewayversion.html#cfn-iotwireless-taskdefinition-lorawangatewayversion-model
            '''
            result = self._values.get("model")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def package_version(self) -> typing.Optional[builtins.str]:
            '''The version of the wireless gateway firmware.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawangatewayversion.html#cfn-iotwireless-taskdefinition-lorawangatewayversion-packageversion
            '''
            result = self._values.get("package_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def station(self) -> typing.Optional[builtins.str]:
            '''The basic station version of the wireless gateway.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawangatewayversion.html#cfn-iotwireless-taskdefinition-lorawangatewayversion-station
            '''
            result = self._values.get("station")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoRaWANGatewayVersionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotwireless.CfnTaskDefinition.LoRaWANUpdateGatewayTaskCreateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "current_version": "currentVersion",
            "sig_key_crc": "sigKeyCrc",
            "update_signature": "updateSignature",
            "update_version": "updateVersion",
        },
    )
    class LoRaWANUpdateGatewayTaskCreateProperty:
        def __init__(
            self,
            *,
            current_version: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnTaskDefinition.LoRaWANGatewayVersionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sig_key_crc: typing.Optional[jsii.Number] = None,
            update_signature: typing.Optional[builtins.str] = None,
            update_version: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnTaskDefinition.LoRaWANGatewayVersionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The signature used to verify the update firmware.

            :param current_version: The version of the gateways that should receive the update.
            :param sig_key_crc: The CRC of the signature private key to check.
            :param update_signature: The signature used to verify the update firmware.
            :param update_version: The firmware version to update the gateway to.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_iotwireless as iotwireless
                
                lo_ra_wANUpdate_gateway_task_create_property = iotwireless.CfnTaskDefinition.LoRaWANUpdateGatewayTaskCreateProperty(
                    current_version=iotwireless.CfnTaskDefinition.LoRaWANGatewayVersionProperty(
                        model="model",
                        package_version="packageVersion",
                        station="station"
                    ),
                    sig_key_crc=123,
                    update_signature="updateSignature",
                    update_version=iotwireless.CfnTaskDefinition.LoRaWANGatewayVersionProperty(
                        model="model",
                        package_version="packageVersion",
                        station="station"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__67d12e61f380ff9154d4537ba69b22ace2544dd5f93588795880579f144fb67d)
                check_type(argname="argument current_version", value=current_version, expected_type=type_hints["current_version"])
                check_type(argname="argument sig_key_crc", value=sig_key_crc, expected_type=type_hints["sig_key_crc"])
                check_type(argname="argument update_signature", value=update_signature, expected_type=type_hints["update_signature"])
                check_type(argname="argument update_version", value=update_version, expected_type=type_hints["update_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if current_version is not None:
                self._values["current_version"] = current_version
            if sig_key_crc is not None:
                self._values["sig_key_crc"] = sig_key_crc
            if update_signature is not None:
                self._values["update_signature"] = update_signature
            if update_version is not None:
                self._values["update_version"] = update_version

        @builtins.property
        def current_version(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnTaskDefinition.LoRaWANGatewayVersionProperty"]]:
            '''The version of the gateways that should receive the update.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate-currentversion
            '''
            result = self._values.get("current_version")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnTaskDefinition.LoRaWANGatewayVersionProperty"]], result)

        @builtins.property
        def sig_key_crc(self) -> typing.Optional[jsii.Number]:
            '''The CRC of the signature private key to check.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate-sigkeycrc
            '''
            result = self._values.get("sig_key_crc")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def update_signature(self) -> typing.Optional[builtins.str]:
            '''The signature used to verify the update firmware.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate-updatesignature
            '''
            result = self._values.get("update_signature")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def update_version(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnTaskDefinition.LoRaWANGatewayVersionProperty"]]:
            '''The firmware version to update the gateway to.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskcreate-updateversion
            '''
            result = self._values.get("update_version")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnTaskDefinition.LoRaWANGatewayVersionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoRaWANUpdateGatewayTaskCreateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotwireless.CfnTaskDefinition.LoRaWANUpdateGatewayTaskEntryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "current_version": "currentVersion",
            "update_version": "updateVersion",
        },
    )
    class LoRaWANUpdateGatewayTaskEntryProperty:
        def __init__(
            self,
            *,
            current_version: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnTaskDefinition.LoRaWANGatewayVersionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            update_version: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnTaskDefinition.LoRaWANGatewayVersionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''LoRaWANUpdateGatewayTaskEntry object.

            :param current_version: The version of the gateways that should receive the update.
            :param update_version: The firmware version to update the gateway to.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskentry.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_iotwireless as iotwireless
                
                lo_ra_wANUpdate_gateway_task_entry_property = iotwireless.CfnTaskDefinition.LoRaWANUpdateGatewayTaskEntryProperty(
                    current_version=iotwireless.CfnTaskDefinition.LoRaWANGatewayVersionProperty(
                        model="model",
                        package_version="packageVersion",
                        station="station"
                    ),
                    update_version=iotwireless.CfnTaskDefinition.LoRaWANGatewayVersionProperty(
                        model="model",
                        package_version="packageVersion",
                        station="station"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__21dcf59b2bc153afbee45193a56ae699f588ca9b5558504487599e49f32dc7be)
                check_type(argname="argument current_version", value=current_version, expected_type=type_hints["current_version"])
                check_type(argname="argument update_version", value=update_version, expected_type=type_hints["update_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if current_version is not None:
                self._values["current_version"] = current_version
            if update_version is not None:
                self._values["update_version"] = update_version

        @builtins.property
        def current_version(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnTaskDefinition.LoRaWANGatewayVersionProperty"]]:
            '''The version of the gateways that should receive the update.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskentry.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskentry-currentversion
            '''
            result = self._values.get("current_version")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnTaskDefinition.LoRaWANGatewayVersionProperty"]], result)

        @builtins.property
        def update_version(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnTaskDefinition.LoRaWANGatewayVersionProperty"]]:
            '''The firmware version to update the gateway to.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-lorawanupdategatewaytaskentry.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskentry-updateversion
            '''
            result = self._values.get("update_version")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnTaskDefinition.LoRaWANGatewayVersionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoRaWANUpdateGatewayTaskEntryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotwireless.CfnTaskDefinition.UpdateWirelessGatewayTaskCreateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "lo_ra_wan": "loRaWan",
            "update_data_role": "updateDataRole",
            "update_data_source": "updateDataSource",
        },
    )
    class UpdateWirelessGatewayTaskCreateProperty:
        def __init__(
            self,
            *,
            lo_ra_wan: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnTaskDefinition.LoRaWANUpdateGatewayTaskCreateProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            update_data_role: typing.Optional[builtins.str] = None,
            update_data_source: typing.Optional[builtins.str] = None,
        ) -> None:
            '''UpdateWirelessGatewayTaskCreate object.

            :param lo_ra_wan: The properties that relate to the LoRaWAN wireless gateway.
            :param update_data_role: The IAM role used to read data from the S3 bucket.
            :param update_data_source: The link to the S3 bucket.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_iotwireless as iotwireless
                
                update_wireless_gateway_task_create_property = iotwireless.CfnTaskDefinition.UpdateWirelessGatewayTaskCreateProperty(
                    lo_ra_wan=iotwireless.CfnTaskDefinition.LoRaWANUpdateGatewayTaskCreateProperty(
                        current_version=iotwireless.CfnTaskDefinition.LoRaWANGatewayVersionProperty(
                            model="model",
                            package_version="packageVersion",
                            station="station"
                        ),
                        sig_key_crc=123,
                        update_signature="updateSignature",
                        update_version=iotwireless.CfnTaskDefinition.LoRaWANGatewayVersionProperty(
                            model="model",
                            package_version="packageVersion",
                            station="station"
                        )
                    ),
                    update_data_role="updateDataRole",
                    update_data_source="updateDataSource"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__72082ec5a22edd46f8332768162eabcff23292f62cf7ccba54980752c3b19a8f)
                check_type(argname="argument lo_ra_wan", value=lo_ra_wan, expected_type=type_hints["lo_ra_wan"])
                check_type(argname="argument update_data_role", value=update_data_role, expected_type=type_hints["update_data_role"])
                check_type(argname="argument update_data_source", value=update_data_source, expected_type=type_hints["update_data_source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if lo_ra_wan is not None:
                self._values["lo_ra_wan"] = lo_ra_wan
            if update_data_role is not None:
                self._values["update_data_role"] = update_data_role
            if update_data_source is not None:
                self._values["update_data_source"] = update_data_source

        @builtins.property
        def lo_ra_wan(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnTaskDefinition.LoRaWANUpdateGatewayTaskCreateProperty"]]:
            '''The properties that relate to the LoRaWAN wireless gateway.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate.html#cfn-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate-lorawan
            '''
            result = self._values.get("lo_ra_wan")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnTaskDefinition.LoRaWANUpdateGatewayTaskCreateProperty"]], result)

        @builtins.property
        def update_data_role(self) -> typing.Optional[builtins.str]:
            '''The IAM role used to read data from the S3 bucket.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate.html#cfn-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate-updatedatarole
            '''
            result = self._values.get("update_data_role")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def update_data_source(self) -> typing.Optional[builtins.str]:
            '''The link to the S3 bucket.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate.html#cfn-iotwireless-taskdefinition-updatewirelessgatewaytaskcreate-updatedatasource
            '''
            result = self._values.get("update_data_source")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UpdateWirelessGatewayTaskCreateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-iotwireless.CfnTaskDefinitionProps",
    jsii_struct_bases=[],
    name_mapping={
        "auto_create_tasks": "autoCreateTasks",
        "lo_ra_wan_update_gateway_task_entry": "loRaWanUpdateGatewayTaskEntry",
        "name": "name",
        "tags": "tags",
        "task_definition_type": "taskDefinitionType",
        "update": "update",
    },
)
class CfnTaskDefinitionProps:
    def __init__(
        self,
        *,
        auto_create_tasks: typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable],
        lo_ra_wan_update_gateway_task_entry: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnTaskDefinition.LoRaWANUpdateGatewayTaskEntryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
        task_definition_type: typing.Optional[builtins.str] = None,
        update: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnTaskDefinition.UpdateWirelessGatewayTaskCreateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnTaskDefinition``.

        :param auto_create_tasks: Whether to automatically create tasks using this task definition for all gateways with the specified current version. If ``false`` , the task must me created by calling ``CreateWirelessGatewayTask`` .
        :param lo_ra_wan_update_gateway_task_entry: ``AWS::IoTWireless::TaskDefinition.LoRaWANUpdateGatewayTaskEntry``.
        :param name: The name of the new resource.
        :param tags: The tags are an array of key-value pairs to attach to the specified resource. Tags can have a minimum of 0 and a maximum of 50 items.
        :param task_definition_type: ``AWS::IoTWireless::TaskDefinition.TaskDefinitionType``.
        :param update: Information about the gateways to update.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_iotwireless as iotwireless
            
            cfn_task_definition_props = iotwireless.CfnTaskDefinitionProps(
                auto_create_tasks=False,
            
                # the properties below are optional
                lo_ra_wan_update_gateway_task_entry=iotwireless.CfnTaskDefinition.LoRaWANUpdateGatewayTaskEntryProperty(
                    current_version=iotwireless.CfnTaskDefinition.LoRaWANGatewayVersionProperty(
                        model="model",
                        package_version="packageVersion",
                        station="station"
                    ),
                    update_version=iotwireless.CfnTaskDefinition.LoRaWANGatewayVersionProperty(
                        model="model",
                        package_version="packageVersion",
                        station="station"
                    )
                ),
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                task_definition_type="taskDefinitionType",
                update=iotwireless.CfnTaskDefinition.UpdateWirelessGatewayTaskCreateProperty(
                    lo_ra_wan=iotwireless.CfnTaskDefinition.LoRaWANUpdateGatewayTaskCreateProperty(
                        current_version=iotwireless.CfnTaskDefinition.LoRaWANGatewayVersionProperty(
                            model="model",
                            package_version="packageVersion",
                            station="station"
                        ),
                        sig_key_crc=123,
                        update_signature="updateSignature",
                        update_version=iotwireless.CfnTaskDefinition.LoRaWANGatewayVersionProperty(
                            model="model",
                            package_version="packageVersion",
                            station="station"
                        )
                    ),
                    update_data_role="updateDataRole",
                    update_data_source="updateDataSource"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a42881aba1e0d388e940986d57a2df4c63a4c3e1e107c7869f4290f43ba5596d)
            check_type(argname="argument auto_create_tasks", value=auto_create_tasks, expected_type=type_hints["auto_create_tasks"])
            check_type(argname="argument lo_ra_wan_update_gateway_task_entry", value=lo_ra_wan_update_gateway_task_entry, expected_type=type_hints["lo_ra_wan_update_gateway_task_entry"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument task_definition_type", value=task_definition_type, expected_type=type_hints["task_definition_type"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "auto_create_tasks": auto_create_tasks,
        }
        if lo_ra_wan_update_gateway_task_entry is not None:
            self._values["lo_ra_wan_update_gateway_task_entry"] = lo_ra_wan_update_gateway_task_entry
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags
        if task_definition_type is not None:
            self._values["task_definition_type"] = task_definition_type
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def auto_create_tasks(
        self,
    ) -> typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]:
        '''Whether to automatically create tasks using this task definition for all gateways with the specified current version.

        If ``false`` , the task must me created by calling ``CreateWirelessGatewayTask`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-autocreatetasks
        '''
        result = self._values.get("auto_create_tasks")
        assert result is not None, "Required property 'auto_create_tasks' is missing"
        return typing.cast(typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable], result)

    @builtins.property
    def lo_ra_wan_update_gateway_task_entry(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnTaskDefinition.LoRaWANUpdateGatewayTaskEntryProperty]]:
        '''``AWS::IoTWireless::TaskDefinition.LoRaWANUpdateGatewayTaskEntry``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-lorawanupdategatewaytaskentry
        '''
        result = self._values.get("lo_ra_wan_update_gateway_task_entry")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnTaskDefinition.LoRaWANUpdateGatewayTaskEntryProperty]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the new resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]]:
        '''The tags are an array of key-value pairs to attach to the specified resource.

        Tags can have a minimum of 0 and a maximum of 50 items.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]], result)

    @builtins.property
    def task_definition_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTWireless::TaskDefinition.TaskDefinitionType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-taskdefinitiontype
        '''
        result = self._values.get("task_definition_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnTaskDefinition.UpdateWirelessGatewayTaskCreateProperty]]:
        '''Information about the gateways to update.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-taskdefinition.html#cfn-iotwireless-taskdefinition-update
        '''
        result = self._values.get("update")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnTaskDefinition.UpdateWirelessGatewayTaskCreateProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTaskDefinitionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnWirelessDevice(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-iotwireless.CfnWirelessDevice",
):
    '''A CloudFormation ``AWS::IoTWireless::WirelessDevice``.

    Provisions a wireless device.

    :cloudformationResource: AWS::IoTWireless::WirelessDevice
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_iotwireless as iotwireless
        
        cfn_wireless_device = iotwireless.CfnWirelessDevice(self, "MyCfnWirelessDevice",
            destination_name="destinationName",
            type="type",
        
            # the properties below are optional
            description="description",
            last_uplink_received_at="lastUplinkReceivedAt",
            lo_ra_wan=iotwireless.CfnWirelessDevice.LoRaWANDeviceProperty(
                abp_v10_x=iotwireless.CfnWirelessDevice.AbpV10xProperty(
                    dev_addr="devAddr",
                    session_keys=iotwireless.CfnWirelessDevice.SessionKeysAbpV10xProperty(
                        app_sKey="appSKey",
                        nwk_sKey="nwkSKey"
                    )
                ),
                abp_v11=iotwireless.CfnWirelessDevice.AbpV11Property(
                    dev_addr="devAddr",
                    session_keys=iotwireless.CfnWirelessDevice.SessionKeysAbpV11Property(
                        app_sKey="appSKey",
                        f_nwk_sInt_key="fNwkSIntKey",
                        nwk_sEnc_key="nwkSEncKey",
                        s_nwk_sInt_key="sNwkSIntKey"
                    )
                ),
                dev_eui="devEui",
                device_profile_id="deviceProfileId",
                otaa_v10_x=iotwireless.CfnWirelessDevice.OtaaV10xProperty(
                    app_eui="appEui",
                    app_key="appKey"
                ),
                otaa_v11=iotwireless.CfnWirelessDevice.OtaaV11Property(
                    app_key="appKey",
                    join_eui="joinEui",
                    nwk_key="nwkKey"
                ),
                service_profile_id="serviceProfileId"
            ),
            name="name",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            thing_arn="thingArn"
        )
    '''

    def __init__(
        self,
        scope: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        destination_name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        last_uplink_received_at: typing.Optional[builtins.str] = None,
        lo_ra_wan: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnWirelessDevice.LoRaWANDeviceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
        thing_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::IoTWireless::WirelessDevice``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param destination_name: The name of the destination to assign to the new wireless device. Can have only have alphanumeric, - (hyphen) and _ (underscore) characters and it can't have any spaces.
        :param type: The wireless device type.
        :param description: The description of the new resource. Maximum length is 2048.
        :param last_uplink_received_at: The date and time when the most recent uplink was received.
        :param lo_ra_wan: The device configuration information to use to create the wireless device. Must be at least one of OtaaV10x, OtaaV11, AbpV11, or AbpV10x.
        :param name: The name of the new resource.
        :param tags: The tags are an array of key-value pairs to attach to the specified resource. Tags can have a minimum of 0 and a maximum of 50 items.
        :param thing_arn: The ARN of the thing to associate with the wireless device.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2498b50cdcf80e13c7919648027ad8436c24e0c64a692cf90619497c8f4ffcd6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnWirelessDeviceProps(
            destination_name=destination_name,
            type=type,
            description=description,
            last_uplink_received_at=last_uplink_received_at,
            lo_ra_wan=lo_ra_wan,
            name=name,
            tags=tags,
            thing_arn=thing_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b5f575ef0dc4cf624fecf0acc5b30b3c4e1c3d9662bafc0aadeacef5ad751c3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b297ed62dd177f9b47ff1277a279d19962680c2999f0df7276e1f61f16c9a4d4)
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
        '''The ARN of the wireless device created.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the wireless device created.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrThingName")
    def attr_thing_name(self) -> builtins.str:
        '''The name of the thing associated with the wireless device.

        The value is empty if a thing isn't associated with the device.

        :cloudformationAttribute: ThingName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrThingName"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _aws_cdk_core_f4b25747.TagManager:
        '''The tags are an array of key-value pairs to attach to the specified resource.

        Tags can have a minimum of 0 and a maximum of 50 items.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-tags
        '''
        return typing.cast(_aws_cdk_core_f4b25747.TagManager, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="destinationName")
    def destination_name(self) -> builtins.str:
        '''The name of the destination to assign to the new wireless device.

        Can have only have alphanumeric, - (hyphen) and _ (underscore) characters and it can't have any spaces.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-destinationname
        '''
        return typing.cast(builtins.str, jsii.get(self, "destinationName"))

    @destination_name.setter
    def destination_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00ba3f47e8dcef98e11c660c384c4b2a7c149aa09074e99eabd9275a1868992a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationName", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The wireless device type.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-type
        '''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__050d401141307e8c7ead438df2bd58d8bf5d154625cea5a162e7e6a9017e3669)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the new resource.

        Maximum length is 2048.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cccb359e115f4909697886eb6450f59fc406b1d353adfe95a57f6dd63afe32c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="lastUplinkReceivedAt")
    def last_uplink_received_at(self) -> typing.Optional[builtins.str]:
        '''The date and time when the most recent uplink was received.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-lastuplinkreceivedat
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lastUplinkReceivedAt"))

    @last_uplink_received_at.setter
    def last_uplink_received_at(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57665aba99e886a54639b1411ecf712ff706d3ddf8afa21ae38f8f78557bf2b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lastUplinkReceivedAt", value)

    @builtins.property
    @jsii.member(jsii_name="loRaWan")
    def lo_ra_wan(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnWirelessDevice.LoRaWANDeviceProperty"]]:
        '''The device configuration information to use to create the wireless device.

        Must be at least one of OtaaV10x, OtaaV11, AbpV11, or AbpV10x.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-lorawan
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnWirelessDevice.LoRaWANDeviceProperty"]], jsii.get(self, "loRaWan"))

    @lo_ra_wan.setter
    def lo_ra_wan(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnWirelessDevice.LoRaWANDeviceProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35ecf775c88d2eb74c4b3344ba6232ca231e8ac24daeb03d664cbc6d40b11d80)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loRaWan", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the new resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2e9b78a64a1ec87c985426e49b4b36681a523fdc37870df62f12dcbed230a01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="thingArn")
    def thing_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the thing to associate with the wireless device.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-thingarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thingArn"))

    @thing_arn.setter
    def thing_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87d4e579c6fa422ba32251ac7877fe7e935f33e3c9bf2f8d258c5b421c85c8c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thingArn", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotwireless.CfnWirelessDevice.AbpV10xProperty",
        jsii_struct_bases=[],
        name_mapping={"dev_addr": "devAddr", "session_keys": "sessionKeys"},
    )
    class AbpV10xProperty:
        def __init__(
            self,
            *,
            dev_addr: builtins.str,
            session_keys: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnWirelessDevice.SessionKeysAbpV10xProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''ABP device object for LoRaWAN specification v1.0.x.

            :param dev_addr: The DevAddr value.
            :param session_keys: Session keys for ABP v1.0.x.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv10x.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_iotwireless as iotwireless
                
                abp_v10x_property = iotwireless.CfnWirelessDevice.AbpV10xProperty(
                    dev_addr="devAddr",
                    session_keys=iotwireless.CfnWirelessDevice.SessionKeysAbpV10xProperty(
                        app_sKey="appSKey",
                        nwk_sKey="nwkSKey"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4d38550f49273904c8ee61210f3208e42c0b4df5a17b9315741fb4134c4f9f03)
                check_type(argname="argument dev_addr", value=dev_addr, expected_type=type_hints["dev_addr"])
                check_type(argname="argument session_keys", value=session_keys, expected_type=type_hints["session_keys"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "dev_addr": dev_addr,
                "session_keys": session_keys,
            }

        @builtins.property
        def dev_addr(self) -> builtins.str:
            '''The DevAddr value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv10x.html#cfn-iotwireless-wirelessdevice-abpv10x-devaddr
            '''
            result = self._values.get("dev_addr")
            assert result is not None, "Required property 'dev_addr' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def session_keys(
            self,
        ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnWirelessDevice.SessionKeysAbpV10xProperty"]:
            '''Session keys for ABP v1.0.x.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv10x.html#cfn-iotwireless-wirelessdevice-abpv10x-sessionkeys
            '''
            result = self._values.get("session_keys")
            assert result is not None, "Required property 'session_keys' is missing"
            return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnWirelessDevice.SessionKeysAbpV10xProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AbpV10xProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotwireless.CfnWirelessDevice.AbpV11Property",
        jsii_struct_bases=[],
        name_mapping={"dev_addr": "devAddr", "session_keys": "sessionKeys"},
    )
    class AbpV11Property:
        def __init__(
            self,
            *,
            dev_addr: builtins.str,
            session_keys: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnWirelessDevice.SessionKeysAbpV11Property", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''ABP device object for create APIs for v1.1.

            :param dev_addr: The DevAddr value.
            :param session_keys: Session keys for ABP v1.1.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv11.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_iotwireless as iotwireless
                
                abp_v11_property = iotwireless.CfnWirelessDevice.AbpV11Property(
                    dev_addr="devAddr",
                    session_keys=iotwireless.CfnWirelessDevice.SessionKeysAbpV11Property(
                        app_sKey="appSKey",
                        f_nwk_sInt_key="fNwkSIntKey",
                        nwk_sEnc_key="nwkSEncKey",
                        s_nwk_sInt_key="sNwkSIntKey"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__aaf3ee7ceb3259cc7dcb668de5f7e5557789a9b4259a5c4f29a54495f7d63e32)
                check_type(argname="argument dev_addr", value=dev_addr, expected_type=type_hints["dev_addr"])
                check_type(argname="argument session_keys", value=session_keys, expected_type=type_hints["session_keys"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "dev_addr": dev_addr,
                "session_keys": session_keys,
            }

        @builtins.property
        def dev_addr(self) -> builtins.str:
            '''The DevAddr value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv11.html#cfn-iotwireless-wirelessdevice-abpv11-devaddr
            '''
            result = self._values.get("dev_addr")
            assert result is not None, "Required property 'dev_addr' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def session_keys(
            self,
        ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnWirelessDevice.SessionKeysAbpV11Property"]:
            '''Session keys for ABP v1.1.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-abpv11.html#cfn-iotwireless-wirelessdevice-abpv11-sessionkeys
            '''
            result = self._values.get("session_keys")
            assert result is not None, "Required property 'session_keys' is missing"
            return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnWirelessDevice.SessionKeysAbpV11Property"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AbpV11Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotwireless.CfnWirelessDevice.LoRaWANDeviceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "abp_v10_x": "abpV10X",
            "abp_v11": "abpV11",
            "dev_eui": "devEui",
            "device_profile_id": "deviceProfileId",
            "otaa_v10_x": "otaaV10X",
            "otaa_v11": "otaaV11",
            "service_profile_id": "serviceProfileId",
        },
    )
    class LoRaWANDeviceProperty:
        def __init__(
            self,
            *,
            abp_v10_x: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnWirelessDevice.AbpV10xProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            abp_v11: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnWirelessDevice.AbpV11Property", typing.Dict[builtins.str, typing.Any]]]] = None,
            dev_eui: typing.Optional[builtins.str] = None,
            device_profile_id: typing.Optional[builtins.str] = None,
            otaa_v10_x: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnWirelessDevice.OtaaV10xProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            otaa_v11: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnWirelessDevice.OtaaV11Property", typing.Dict[builtins.str, typing.Any]]]] = None,
            service_profile_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''LoRaWAN object for create functions.

            :param abp_v10_x: LoRaWAN object for create APIs.
            :param abp_v11: ABP device object for create APIs for v1.1.
            :param dev_eui: The DevEUI value.
            :param device_profile_id: The ID of the device profile for the new wireless device.
            :param otaa_v10_x: OTAA device object for create APIs for v1.0.x.
            :param otaa_v11: OTAA device object for v1.1 for create APIs.
            :param service_profile_id: The ID of the service profile.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_iotwireless as iotwireless
                
                lo_ra_wANDevice_property = iotwireless.CfnWirelessDevice.LoRaWANDeviceProperty(
                    abp_v10_x=iotwireless.CfnWirelessDevice.AbpV10xProperty(
                        dev_addr="devAddr",
                        session_keys=iotwireless.CfnWirelessDevice.SessionKeysAbpV10xProperty(
                            app_sKey="appSKey",
                            nwk_sKey="nwkSKey"
                        )
                    ),
                    abp_v11=iotwireless.CfnWirelessDevice.AbpV11Property(
                        dev_addr="devAddr",
                        session_keys=iotwireless.CfnWirelessDevice.SessionKeysAbpV11Property(
                            app_sKey="appSKey",
                            f_nwk_sInt_key="fNwkSIntKey",
                            nwk_sEnc_key="nwkSEncKey",
                            s_nwk_sInt_key="sNwkSIntKey"
                        )
                    ),
                    dev_eui="devEui",
                    device_profile_id="deviceProfileId",
                    otaa_v10_x=iotwireless.CfnWirelessDevice.OtaaV10xProperty(
                        app_eui="appEui",
                        app_key="appKey"
                    ),
                    otaa_v11=iotwireless.CfnWirelessDevice.OtaaV11Property(
                        app_key="appKey",
                        join_eui="joinEui",
                        nwk_key="nwkKey"
                    ),
                    service_profile_id="serviceProfileId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4b78ec2b6d6078b53cda50049b04e47266b3bc3db89298bf8dca91e21abc82c5)
                check_type(argname="argument abp_v10_x", value=abp_v10_x, expected_type=type_hints["abp_v10_x"])
                check_type(argname="argument abp_v11", value=abp_v11, expected_type=type_hints["abp_v11"])
                check_type(argname="argument dev_eui", value=dev_eui, expected_type=type_hints["dev_eui"])
                check_type(argname="argument device_profile_id", value=device_profile_id, expected_type=type_hints["device_profile_id"])
                check_type(argname="argument otaa_v10_x", value=otaa_v10_x, expected_type=type_hints["otaa_v10_x"])
                check_type(argname="argument otaa_v11", value=otaa_v11, expected_type=type_hints["otaa_v11"])
                check_type(argname="argument service_profile_id", value=service_profile_id, expected_type=type_hints["service_profile_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if abp_v10_x is not None:
                self._values["abp_v10_x"] = abp_v10_x
            if abp_v11 is not None:
                self._values["abp_v11"] = abp_v11
            if dev_eui is not None:
                self._values["dev_eui"] = dev_eui
            if device_profile_id is not None:
                self._values["device_profile_id"] = device_profile_id
            if otaa_v10_x is not None:
                self._values["otaa_v10_x"] = otaa_v10_x
            if otaa_v11 is not None:
                self._values["otaa_v11"] = otaa_v11
            if service_profile_id is not None:
                self._values["service_profile_id"] = service_profile_id

        @builtins.property
        def abp_v10_x(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnWirelessDevice.AbpV10xProperty"]]:
            '''LoRaWAN object for create APIs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-abpv10x
            '''
            result = self._values.get("abp_v10_x")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnWirelessDevice.AbpV10xProperty"]], result)

        @builtins.property
        def abp_v11(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnWirelessDevice.AbpV11Property"]]:
            '''ABP device object for create APIs for v1.1.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-abpv11
            '''
            result = self._values.get("abp_v11")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnWirelessDevice.AbpV11Property"]], result)

        @builtins.property
        def dev_eui(self) -> typing.Optional[builtins.str]:
            '''The DevEUI value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-deveui
            '''
            result = self._values.get("dev_eui")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def device_profile_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the device profile for the new wireless device.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-deviceprofileid
            '''
            result = self._values.get("device_profile_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def otaa_v10_x(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnWirelessDevice.OtaaV10xProperty"]]:
            '''OTAA device object for create APIs for v1.0.x.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-otaav10x
            '''
            result = self._values.get("otaa_v10_x")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnWirelessDevice.OtaaV10xProperty"]], result)

        @builtins.property
        def otaa_v11(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnWirelessDevice.OtaaV11Property"]]:
            '''OTAA device object for v1.1 for create APIs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-otaav11
            '''
            result = self._values.get("otaa_v11")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnWirelessDevice.OtaaV11Property"]], result)

        @builtins.property
        def service_profile_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the service profile.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-lorawandevice.html#cfn-iotwireless-wirelessdevice-lorawandevice-serviceprofileid
            '''
            result = self._values.get("service_profile_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoRaWANDeviceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotwireless.CfnWirelessDevice.OtaaV10xProperty",
        jsii_struct_bases=[],
        name_mapping={"app_eui": "appEui", "app_key": "appKey"},
    )
    class OtaaV10xProperty:
        def __init__(self, *, app_eui: builtins.str, app_key: builtins.str) -> None:
            '''OTAA device object for create APIs for v1.0.x.

            :param app_eui: The AppEUI value, with pattern of ``[a-fA-F0-9]{16}`` .
            :param app_key: The AppKey is a secret key, which you should handle in a similar way as you would an application password. You can protect the AppKey value by storing it in the AWS Secrets Manager and use the `secretsmanager <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-secretsmanager>`_ to reference this value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav10x.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_iotwireless as iotwireless
                
                otaa_v10x_property = iotwireless.CfnWirelessDevice.OtaaV10xProperty(
                    app_eui="appEui",
                    app_key="appKey"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a0f71a8ae506773c267541441910c6a924c4e20ae4017823a1f1320f051b2d69)
                check_type(argname="argument app_eui", value=app_eui, expected_type=type_hints["app_eui"])
                check_type(argname="argument app_key", value=app_key, expected_type=type_hints["app_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "app_eui": app_eui,
                "app_key": app_key,
            }

        @builtins.property
        def app_eui(self) -> builtins.str:
            '''The AppEUI value, with pattern of ``[a-fA-F0-9]{16}`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav10x.html#cfn-iotwireless-wirelessdevice-otaav10x-appeui
            '''
            result = self._values.get("app_eui")
            assert result is not None, "Required property 'app_eui' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def app_key(self) -> builtins.str:
            '''The AppKey is a secret key, which you should handle in a similar way as you would an application password.

            You can protect the AppKey value by storing it in the AWS Secrets Manager and use the `secretsmanager <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-secretsmanager>`_ to reference this value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav10x.html#cfn-iotwireless-wirelessdevice-otaav10x-appkey
            '''
            result = self._values.get("app_key")
            assert result is not None, "Required property 'app_key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OtaaV10xProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotwireless.CfnWirelessDevice.OtaaV11Property",
        jsii_struct_bases=[],
        name_mapping={"app_key": "appKey", "join_eui": "joinEui", "nwk_key": "nwkKey"},
    )
    class OtaaV11Property:
        def __init__(
            self,
            *,
            app_key: builtins.str,
            join_eui: builtins.str,
            nwk_key: builtins.str,
        ) -> None:
            '''OTAA device object for v1.1 for create APIs.

            :param app_key: The AppKey is a secret key, which you should handle in a similar way as you would an application password. You can protect the AppKey value by storing it in the AWS Secrets Manager and use the `secretsmanager <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-secretsmanager>`_ to reference this value.
            :param join_eui: The JoinEUI value.
            :param nwk_key: The NwkKey is a secret key, which you should handle in a similar way as you would an application password. You can protect the NwkKey value by storing it in the AWS Secrets Manager and use the `secretsmanager <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-secretsmanager>`_ to reference this value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav11.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_iotwireless as iotwireless
                
                otaa_v11_property = iotwireless.CfnWirelessDevice.OtaaV11Property(
                    app_key="appKey",
                    join_eui="joinEui",
                    nwk_key="nwkKey"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a333397b966e4f12f635f015fd9f6314f0900609dc3fee12f17ae9ff0c8656a3)
                check_type(argname="argument app_key", value=app_key, expected_type=type_hints["app_key"])
                check_type(argname="argument join_eui", value=join_eui, expected_type=type_hints["join_eui"])
                check_type(argname="argument nwk_key", value=nwk_key, expected_type=type_hints["nwk_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "app_key": app_key,
                "join_eui": join_eui,
                "nwk_key": nwk_key,
            }

        @builtins.property
        def app_key(self) -> builtins.str:
            '''The AppKey is a secret key, which you should handle in a similar way as you would an application password.

            You can protect the AppKey value by storing it in the AWS Secrets Manager and use the `secretsmanager <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-secretsmanager>`_ to reference this value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav11.html#cfn-iotwireless-wirelessdevice-otaav11-appkey
            '''
            result = self._values.get("app_key")
            assert result is not None, "Required property 'app_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def join_eui(self) -> builtins.str:
            '''The JoinEUI value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav11.html#cfn-iotwireless-wirelessdevice-otaav11-joineui
            '''
            result = self._values.get("join_eui")
            assert result is not None, "Required property 'join_eui' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def nwk_key(self) -> builtins.str:
            '''The NwkKey is a secret key, which you should handle in a similar way as you would an application password.

            You can protect the NwkKey value by storing it in the AWS Secrets Manager and use the `secretsmanager <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-secretsmanager>`_ to reference this value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-otaav11.html#cfn-iotwireless-wirelessdevice-otaav11-nwkkey
            '''
            result = self._values.get("nwk_key")
            assert result is not None, "Required property 'nwk_key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OtaaV11Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotwireless.CfnWirelessDevice.SessionKeysAbpV10xProperty",
        jsii_struct_bases=[],
        name_mapping={"app_s_key": "appSKey", "nwk_s_key": "nwkSKey"},
    )
    class SessionKeysAbpV10xProperty:
        def __init__(self, *, app_s_key: builtins.str, nwk_s_key: builtins.str) -> None:
            '''LoRaWAN object for create APIs.

            :param app_s_key: The AppSKey is a secret key, which you should handle in a similar way as you would an application password. You can protect the AppSKey value by storing it in the AWS Secrets Manager and use the `secretsmanager <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-secretsmanager>`_ to reference this value.
            :param nwk_s_key: The NwkSKey is a secret key, which you should handle in a similar way as you would an application password. You can protect the NwkSKey value by storing it in the AWS Secrets Manager and use the `secretsmanager <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-secretsmanager>`_ to reference this value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv10x.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_iotwireless as iotwireless
                
                session_keys_abp_v10x_property = iotwireless.CfnWirelessDevice.SessionKeysAbpV10xProperty(
                    app_sKey="appSKey",
                    nwk_sKey="nwkSKey"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__693d578f082eaee5b5cb0dea9e5158c79e26907b8729f4bbea847b376f17e5b7)
                check_type(argname="argument app_s_key", value=app_s_key, expected_type=type_hints["app_s_key"])
                check_type(argname="argument nwk_s_key", value=nwk_s_key, expected_type=type_hints["nwk_s_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "app_s_key": app_s_key,
                "nwk_s_key": nwk_s_key,
            }

        @builtins.property
        def app_s_key(self) -> builtins.str:
            '''The AppSKey is a secret key, which you should handle in a similar way as you would an application password.

            You can protect the AppSKey value by storing it in the AWS Secrets Manager and use the `secretsmanager <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-secretsmanager>`_ to reference this value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv10x.html#cfn-iotwireless-wirelessdevice-sessionkeysabpv10x-appskey
            '''
            result = self._values.get("app_s_key")
            assert result is not None, "Required property 'app_s_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def nwk_s_key(self) -> builtins.str:
            '''The NwkSKey is a secret key, which you should handle in a similar way as you would an application password.

            You can protect the NwkSKey value by storing it in the AWS Secrets Manager and use the `secretsmanager <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-secretsmanager>`_ to reference this value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv10x.html#cfn-iotwireless-wirelessdevice-sessionkeysabpv10x-nwkskey
            '''
            result = self._values.get("nwk_s_key")
            assert result is not None, "Required property 'nwk_s_key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SessionKeysAbpV10xProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotwireless.CfnWirelessDevice.SessionKeysAbpV11Property",
        jsii_struct_bases=[],
        name_mapping={
            "app_s_key": "appSKey",
            "f_nwk_s_int_key": "fNwkSIntKey",
            "nwk_s_enc_key": "nwkSEncKey",
            "s_nwk_s_int_key": "sNwkSIntKey",
        },
    )
    class SessionKeysAbpV11Property:
        def __init__(
            self,
            *,
            app_s_key: builtins.str,
            f_nwk_s_int_key: builtins.str,
            nwk_s_enc_key: builtins.str,
            s_nwk_s_int_key: builtins.str,
        ) -> None:
            '''Session keys for ABP v1.1.

            :param app_s_key: The AppSKey is a secret key, which you should handle in a similar way as you would an application password. You can protect the AppSKey value by storing it in the AWS Secrets Manager and use the `secretsmanager <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-secretsmanager>`_ to reference this value.
            :param f_nwk_s_int_key: The FNwkSIntKey is a secret key, which you should handle in a similar way as you would an application password. You can protect the FNwkSIntKey value by storing it in the AWS Secrets Manager and use the `secretsmanager <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-secretsmanager>`_ to reference this value.
            :param nwk_s_enc_key: The NwkSEncKey is a secret key, which you should handle in a similar way as you would an application password. You can protect the NwkSEncKey value by storing it in the AWS Secrets Manager and use the `secretsmanager <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-secretsmanager>`_ to reference this value.
            :param s_nwk_s_int_key: The SNwkSIntKey is a secret key, which you should handle in a similar way as you would an application password. You can protect the SNwkSIntKey value by storing it in the AWS Secrets Manager and use the `secretsmanager <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-secretsmanager>`_ to reference this value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_iotwireless as iotwireless
                
                session_keys_abp_v11_property = iotwireless.CfnWirelessDevice.SessionKeysAbpV11Property(
                    app_sKey="appSKey",
                    f_nwk_sInt_key="fNwkSIntKey",
                    nwk_sEnc_key="nwkSEncKey",
                    s_nwk_sInt_key="sNwkSIntKey"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__378afcb9d3baf5597fe62761a2fcdc90d7922a86151e3ff57497d7c9cb3221a1)
                check_type(argname="argument app_s_key", value=app_s_key, expected_type=type_hints["app_s_key"])
                check_type(argname="argument f_nwk_s_int_key", value=f_nwk_s_int_key, expected_type=type_hints["f_nwk_s_int_key"])
                check_type(argname="argument nwk_s_enc_key", value=nwk_s_enc_key, expected_type=type_hints["nwk_s_enc_key"])
                check_type(argname="argument s_nwk_s_int_key", value=s_nwk_s_int_key, expected_type=type_hints["s_nwk_s_int_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "app_s_key": app_s_key,
                "f_nwk_s_int_key": f_nwk_s_int_key,
                "nwk_s_enc_key": nwk_s_enc_key,
                "s_nwk_s_int_key": s_nwk_s_int_key,
            }

        @builtins.property
        def app_s_key(self) -> builtins.str:
            '''The AppSKey is a secret key, which you should handle in a similar way as you would an application password.

            You can protect the AppSKey value by storing it in the AWS Secrets Manager and use the `secretsmanager <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-secretsmanager>`_ to reference this value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11.html#cfn-iotwireless-wirelessdevice-sessionkeysabpv11-appskey
            '''
            result = self._values.get("app_s_key")
            assert result is not None, "Required property 'app_s_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def f_nwk_s_int_key(self) -> builtins.str:
            '''The FNwkSIntKey is a secret key, which you should handle in a similar way as you would an application password.

            You can protect the FNwkSIntKey value by storing it in the AWS Secrets Manager and use the `secretsmanager <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-secretsmanager>`_ to reference this value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11.html#cfn-iotwireless-wirelessdevice-sessionkeysabpv11-fnwksintkey
            '''
            result = self._values.get("f_nwk_s_int_key")
            assert result is not None, "Required property 'f_nwk_s_int_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def nwk_s_enc_key(self) -> builtins.str:
            '''The NwkSEncKey is a secret key, which you should handle in a similar way as you would an application password.

            You can protect the NwkSEncKey value by storing it in the AWS Secrets Manager and use the `secretsmanager <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-secretsmanager>`_ to reference this value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11.html#cfn-iotwireless-wirelessdevice-sessionkeysabpv11-nwksenckey
            '''
            result = self._values.get("nwk_s_enc_key")
            assert result is not None, "Required property 'nwk_s_enc_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s_nwk_s_int_key(self) -> builtins.str:
            '''The SNwkSIntKey is a secret key, which you should handle in a similar way as you would an application password.

            You can protect the SNwkSIntKey value by storing it in the AWS Secrets Manager and use the `secretsmanager <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-secretsmanager>`_ to reference this value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv11.html#cfn-iotwireless-wirelessdevice-sessionkeysabpv11-snwksintkey
            '''
            result = self._values.get("s_nwk_s_int_key")
            assert result is not None, "Required property 's_nwk_s_int_key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SessionKeysAbpV11Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-iotwireless.CfnWirelessDeviceProps",
    jsii_struct_bases=[],
    name_mapping={
        "destination_name": "destinationName",
        "type": "type",
        "description": "description",
        "last_uplink_received_at": "lastUplinkReceivedAt",
        "lo_ra_wan": "loRaWan",
        "name": "name",
        "tags": "tags",
        "thing_arn": "thingArn",
    },
)
class CfnWirelessDeviceProps:
    def __init__(
        self,
        *,
        destination_name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        last_uplink_received_at: typing.Optional[builtins.str] = None,
        lo_ra_wan: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnWirelessDevice.LoRaWANDeviceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
        thing_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnWirelessDevice``.

        :param destination_name: The name of the destination to assign to the new wireless device. Can have only have alphanumeric, - (hyphen) and _ (underscore) characters and it can't have any spaces.
        :param type: The wireless device type.
        :param description: The description of the new resource. Maximum length is 2048.
        :param last_uplink_received_at: The date and time when the most recent uplink was received.
        :param lo_ra_wan: The device configuration information to use to create the wireless device. Must be at least one of OtaaV10x, OtaaV11, AbpV11, or AbpV10x.
        :param name: The name of the new resource.
        :param tags: The tags are an array of key-value pairs to attach to the specified resource. Tags can have a minimum of 0 and a maximum of 50 items.
        :param thing_arn: The ARN of the thing to associate with the wireless device.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_iotwireless as iotwireless
            
            cfn_wireless_device_props = iotwireless.CfnWirelessDeviceProps(
                destination_name="destinationName",
                type="type",
            
                # the properties below are optional
                description="description",
                last_uplink_received_at="lastUplinkReceivedAt",
                lo_ra_wan=iotwireless.CfnWirelessDevice.LoRaWANDeviceProperty(
                    abp_v10_x=iotwireless.CfnWirelessDevice.AbpV10xProperty(
                        dev_addr="devAddr",
                        session_keys=iotwireless.CfnWirelessDevice.SessionKeysAbpV10xProperty(
                            app_sKey="appSKey",
                            nwk_sKey="nwkSKey"
                        )
                    ),
                    abp_v11=iotwireless.CfnWirelessDevice.AbpV11Property(
                        dev_addr="devAddr",
                        session_keys=iotwireless.CfnWirelessDevice.SessionKeysAbpV11Property(
                            app_sKey="appSKey",
                            f_nwk_sInt_key="fNwkSIntKey",
                            nwk_sEnc_key="nwkSEncKey",
                            s_nwk_sInt_key="sNwkSIntKey"
                        )
                    ),
                    dev_eui="devEui",
                    device_profile_id="deviceProfileId",
                    otaa_v10_x=iotwireless.CfnWirelessDevice.OtaaV10xProperty(
                        app_eui="appEui",
                        app_key="appKey"
                    ),
                    otaa_v11=iotwireless.CfnWirelessDevice.OtaaV11Property(
                        app_key="appKey",
                        join_eui="joinEui",
                        nwk_key="nwkKey"
                    ),
                    service_profile_id="serviceProfileId"
                ),
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                thing_arn="thingArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82e04df14f0377fc270cbe3177e2f24bbf0bfda173dfe89eff85b6feadecca8d)
            check_type(argname="argument destination_name", value=destination_name, expected_type=type_hints["destination_name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument last_uplink_received_at", value=last_uplink_received_at, expected_type=type_hints["last_uplink_received_at"])
            check_type(argname="argument lo_ra_wan", value=lo_ra_wan, expected_type=type_hints["lo_ra_wan"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument thing_arn", value=thing_arn, expected_type=type_hints["thing_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination_name": destination_name,
            "type": type,
        }
        if description is not None:
            self._values["description"] = description
        if last_uplink_received_at is not None:
            self._values["last_uplink_received_at"] = last_uplink_received_at
        if lo_ra_wan is not None:
            self._values["lo_ra_wan"] = lo_ra_wan
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags
        if thing_arn is not None:
            self._values["thing_arn"] = thing_arn

    @builtins.property
    def destination_name(self) -> builtins.str:
        '''The name of the destination to assign to the new wireless device.

        Can have only have alphanumeric, - (hyphen) and _ (underscore) characters and it can't have any spaces.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-destinationname
        '''
        result = self._values.get("destination_name")
        assert result is not None, "Required property 'destination_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The wireless device type.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the new resource.

        Maximum length is 2048.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def last_uplink_received_at(self) -> typing.Optional[builtins.str]:
        '''The date and time when the most recent uplink was received.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-lastuplinkreceivedat
        '''
        result = self._values.get("last_uplink_received_at")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lo_ra_wan(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnWirelessDevice.LoRaWANDeviceProperty]]:
        '''The device configuration information to use to create the wireless device.

        Must be at least one of OtaaV10x, OtaaV11, AbpV11, or AbpV10x.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-lorawan
        '''
        result = self._values.get("lo_ra_wan")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnWirelessDevice.LoRaWANDeviceProperty]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the new resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]]:
        '''The tags are an array of key-value pairs to attach to the specified resource.

        Tags can have a minimum of 0 and a maximum of 50 items.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]], result)

    @builtins.property
    def thing_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the thing to associate with the wireless device.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html#cfn-iotwireless-wirelessdevice-thingarn
        '''
        result = self._values.get("thing_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWirelessDeviceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnWirelessGateway(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-iotwireless.CfnWirelessGateway",
):
    '''A CloudFormation ``AWS::IoTWireless::WirelessGateway``.

    Provisions a wireless gateway.

    :cloudformationResource: AWS::IoTWireless::WirelessGateway
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_iotwireless as iotwireless
        
        cfn_wireless_gateway = iotwireless.CfnWirelessGateway(self, "MyCfnWirelessGateway",
            lo_ra_wan=iotwireless.CfnWirelessGateway.LoRaWANGatewayProperty(
                gateway_eui="gatewayEui",
                rf_region="rfRegion"
            ),
        
            # the properties below are optional
            description="description",
            last_uplink_received_at="lastUplinkReceivedAt",
            name="name",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            thing_arn="thingArn",
            thing_name="thingName"
        )
    '''

    def __init__(
        self,
        scope: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        lo_ra_wan: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnWirelessGateway.LoRaWANGatewayProperty", typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        last_uplink_received_at: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
        thing_arn: typing.Optional[builtins.str] = None,
        thing_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::IoTWireless::WirelessGateway``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param lo_ra_wan: The gateway configuration information to use to create the wireless gateway.
        :param description: The description of the new resource. The maximum length is 2048 characters.
        :param last_uplink_received_at: The date and time when the most recent uplink was received.
        :param name: The name of the new resource.
        :param tags: The tags are an array of key-value pairs to attach to the specified resource. Tags can have a minimum of 0 and a maximum of 50 items.
        :param thing_arn: The ARN of the thing to associate with the wireless gateway.
        :param thing_name: ``AWS::IoTWireless::WirelessGateway.ThingName``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a89c4b5de62c743b993367fa1c205bc1c752e37b8621fecdddfadd9745e7cd3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnWirelessGatewayProps(
            lo_ra_wan=lo_ra_wan,
            description=description,
            last_uplink_received_at=last_uplink_received_at,
            name=name,
            tags=tags,
            thing_arn=thing_arn,
            thing_name=thing_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07dae05bacc1b48e3a5f09635792cc5536249734a54e6fd363ffd3adcb5f5fbd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0c2495120ba7aee15d44de3ebad8c502141cea2a0f35fd83f3453e038e44aa0a)
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
        '''The ARN of the wireless gateway created.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the wireless gateway created.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _aws_cdk_core_f4b25747.TagManager:
        '''The tags are an array of key-value pairs to attach to the specified resource.

        Tags can have a minimum of 0 and a maximum of 50 items.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-tags
        '''
        return typing.cast(_aws_cdk_core_f4b25747.TagManager, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="loRaWan")
    def lo_ra_wan(
        self,
    ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnWirelessGateway.LoRaWANGatewayProperty"]:
        '''The gateway configuration information to use to create the wireless gateway.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-lorawan
        '''
        return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnWirelessGateway.LoRaWANGatewayProperty"], jsii.get(self, "loRaWan"))

    @lo_ra_wan.setter
    def lo_ra_wan(
        self,
        value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnWirelessGateway.LoRaWANGatewayProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97f73752e7eb94263226cdcbd4b4b090598eedd2493d6fb0f90aaaf27a5f13dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loRaWan", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the new resource.

        The maximum length is 2048 characters.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7307bc5853df9c6f89bb2a273fc61e71e90262e0840060fe9cbd3de583ab782b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="lastUplinkReceivedAt")
    def last_uplink_received_at(self) -> typing.Optional[builtins.str]:
        '''The date and time when the most recent uplink was received.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-lastuplinkreceivedat
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lastUplinkReceivedAt"))

    @last_uplink_received_at.setter
    def last_uplink_received_at(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97f97073dc5ee2c04af738a298813d0961792f853fad84d73d2a70ccc26cb51e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lastUplinkReceivedAt", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the new resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7d788a768fa1121cb651f157751bcea3746163332e857fefeef850f2c59fdee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="thingArn")
    def thing_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the thing to associate with the wireless gateway.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-thingarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thingArn"))

    @thing_arn.setter
    def thing_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24529e4f39a4d1d88aa00af84e16bbe41ecf62bd192bbb4724528ed323e3eb84)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thingArn", value)

    @builtins.property
    @jsii.member(jsii_name="thingName")
    def thing_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTWireless::WirelessGateway.ThingName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-thingname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thingName"))

    @thing_name.setter
    def thing_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30f1d8a14839748583f9cb5e88ce35c3cb139b3838df7df8cc4ea5ce16324d32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thingName", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotwireless.CfnWirelessGateway.LoRaWANGatewayProperty",
        jsii_struct_bases=[],
        name_mapping={"gateway_eui": "gatewayEui", "rf_region": "rfRegion"},
    )
    class LoRaWANGatewayProperty:
        def __init__(
            self,
            *,
            gateway_eui: builtins.str,
            rf_region: builtins.str,
        ) -> None:
            '''LoRaWAN wireless gateway object.

            :param gateway_eui: The gateway's EUI value.
            :param rf_region: The frequency band (RFRegion) value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessgateway-lorawangateway.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_iotwireless as iotwireless
                
                lo_ra_wANGateway_property = iotwireless.CfnWirelessGateway.LoRaWANGatewayProperty(
                    gateway_eui="gatewayEui",
                    rf_region="rfRegion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__aa02e2b37976d1cc9825697c3d4bf4dfff25811d5b5cab49c1d3fa85c0b39d3d)
                check_type(argname="argument gateway_eui", value=gateway_eui, expected_type=type_hints["gateway_eui"])
                check_type(argname="argument rf_region", value=rf_region, expected_type=type_hints["rf_region"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "gateway_eui": gateway_eui,
                "rf_region": rf_region,
            }

        @builtins.property
        def gateway_eui(self) -> builtins.str:
            '''The gateway's EUI value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessgateway-lorawangateway.html#cfn-iotwireless-wirelessgateway-lorawangateway-gatewayeui
            '''
            result = self._values.get("gateway_eui")
            assert result is not None, "Required property 'gateway_eui' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def rf_region(self) -> builtins.str:
            '''The frequency band (RFRegion) value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotwireless-wirelessgateway-lorawangateway.html#cfn-iotwireless-wirelessgateway-lorawangateway-rfregion
            '''
            result = self._values.get("rf_region")
            assert result is not None, "Required property 'rf_region' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoRaWANGatewayProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-iotwireless.CfnWirelessGatewayProps",
    jsii_struct_bases=[],
    name_mapping={
        "lo_ra_wan": "loRaWan",
        "description": "description",
        "last_uplink_received_at": "lastUplinkReceivedAt",
        "name": "name",
        "tags": "tags",
        "thing_arn": "thingArn",
        "thing_name": "thingName",
    },
)
class CfnWirelessGatewayProps:
    def __init__(
        self,
        *,
        lo_ra_wan: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnWirelessGateway.LoRaWANGatewayProperty, typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        last_uplink_received_at: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
        thing_arn: typing.Optional[builtins.str] = None,
        thing_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnWirelessGateway``.

        :param lo_ra_wan: The gateway configuration information to use to create the wireless gateway.
        :param description: The description of the new resource. The maximum length is 2048 characters.
        :param last_uplink_received_at: The date and time when the most recent uplink was received.
        :param name: The name of the new resource.
        :param tags: The tags are an array of key-value pairs to attach to the specified resource. Tags can have a minimum of 0 and a maximum of 50 items.
        :param thing_arn: The ARN of the thing to associate with the wireless gateway.
        :param thing_name: ``AWS::IoTWireless::WirelessGateway.ThingName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_iotwireless as iotwireless
            
            cfn_wireless_gateway_props = iotwireless.CfnWirelessGatewayProps(
                lo_ra_wan=iotwireless.CfnWirelessGateway.LoRaWANGatewayProperty(
                    gateway_eui="gatewayEui",
                    rf_region="rfRegion"
                ),
            
                # the properties below are optional
                description="description",
                last_uplink_received_at="lastUplinkReceivedAt",
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                thing_arn="thingArn",
                thing_name="thingName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fcd953583aa54651f18e0c55e234398e5b33c25a61ff45400d2f92ea434ae58)
            check_type(argname="argument lo_ra_wan", value=lo_ra_wan, expected_type=type_hints["lo_ra_wan"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument last_uplink_received_at", value=last_uplink_received_at, expected_type=type_hints["last_uplink_received_at"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument thing_arn", value=thing_arn, expected_type=type_hints["thing_arn"])
            check_type(argname="argument thing_name", value=thing_name, expected_type=type_hints["thing_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "lo_ra_wan": lo_ra_wan,
        }
        if description is not None:
            self._values["description"] = description
        if last_uplink_received_at is not None:
            self._values["last_uplink_received_at"] = last_uplink_received_at
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags
        if thing_arn is not None:
            self._values["thing_arn"] = thing_arn
        if thing_name is not None:
            self._values["thing_name"] = thing_name

    @builtins.property
    def lo_ra_wan(
        self,
    ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnWirelessGateway.LoRaWANGatewayProperty]:
        '''The gateway configuration information to use to create the wireless gateway.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-lorawan
        '''
        result = self._values.get("lo_ra_wan")
        assert result is not None, "Required property 'lo_ra_wan' is missing"
        return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnWirelessGateway.LoRaWANGatewayProperty], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the new resource.

        The maximum length is 2048 characters.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def last_uplink_received_at(self) -> typing.Optional[builtins.str]:
        '''The date and time when the most recent uplink was received.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-lastuplinkreceivedat
        '''
        result = self._values.get("last_uplink_received_at")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the new resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]]:
        '''The tags are an array of key-value pairs to attach to the specified resource.

        Tags can have a minimum of 0 and a maximum of 50 items.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]], result)

    @builtins.property
    def thing_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the thing to associate with the wireless gateway.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-thingarn
        '''
        result = self._values.get("thing_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def thing_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTWireless::WirelessGateway.ThingName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessgateway.html#cfn-iotwireless-wirelessgateway-thingname
        '''
        result = self._values.get("thing_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWirelessGatewayProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDestination",
    "CfnDestinationProps",
    "CfnDeviceProfile",
    "CfnDeviceProfileProps",
    "CfnFuotaTask",
    "CfnFuotaTaskProps",
    "CfnMulticastGroup",
    "CfnMulticastGroupProps",
    "CfnNetworkAnalyzerConfiguration",
    "CfnNetworkAnalyzerConfigurationProps",
    "CfnPartnerAccount",
    "CfnPartnerAccountProps",
    "CfnServiceProfile",
    "CfnServiceProfileProps",
    "CfnTaskDefinition",
    "CfnTaskDefinitionProps",
    "CfnWirelessDevice",
    "CfnWirelessDeviceProps",
    "CfnWirelessGateway",
    "CfnWirelessGatewayProps",
]

publication.publish()

def _typecheckingstub__c07d5546eee9891c06c041a98e64d55f9258f40f6c57d8229496a1bbe14b62a3(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    expression: builtins.str,
    expression_type: builtins.str,
    name: builtins.str,
    role_arn: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0f588c8b63304988e3b3b2747e4fa527dd621202103e6556535d686f4f1d553(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8289c3ab4984a46f3dc227436cb9232bc83f5f487623f0e442617a0df9f9a887(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__391ef63f878229f7f3e7af4f145ad11cb958bcc169f0c50808d4771f48d370fe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3753e7d52d06779443eda5bcccb44a47dc2e29d425c7557181b183dcb245e37(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fc1f0622e35c3e0ca44862dbcaafd68711d012e0c949c61c60b43ecb966edb3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1d8c10f8c9db42b8dd5d0bbd7ab1686db99a868d4a1ac6e3f7fa917aa6d3c7f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a296168c930d693598e4578e8edca9fc5e36eb2bd8a7dbdc80986ca7327aee5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9070cb0529d6006b3d56cf59fedb7e85cd9879dd12ada9cec779f836ee530780(
    *,
    expression: builtins.str,
    expression_type: builtins.str,
    name: builtins.str,
    role_arn: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00e6fd505e7c19020d64d1f59d1e418008c69e6745daf7166e5689b3c7d4c1d0(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    lo_ra_wan: typing.Optional[typing.Union[typing.Union[CfnDeviceProfile.LoRaWANDeviceProfileProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable]] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d212c1cc213f0e1ec1e2426fbf8980588bad6cff13c5477b329031eca87e1be4(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__554aa51c6b28db8423c61a0fccd803fdde2a7747de576bcecb340af3eeef498b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1382ed615daabd4b75b523bc91cc1dcc3de85da4ee705a63ab1df96711868ad(
    value: typing.Optional[typing.Union[CfnDeviceProfile.LoRaWANDeviceProfileProperty, _aws_cdk_core_f4b25747.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0afe21458b494e68210528688ab3f8ee25530ebed85a849ad5f3787338cb54d3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4df874c71da347f86d91b106d8ff2c80ea04e8abd384f8aa3e3adc2c7e19d9d1(
    *,
    class_b_timeout: typing.Optional[jsii.Number] = None,
    class_c_timeout: typing.Optional[jsii.Number] = None,
    factory_preset_freqs_list: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[jsii.Number]]] = None,
    mac_version: typing.Optional[builtins.str] = None,
    max_duty_cycle: typing.Optional[jsii.Number] = None,
    max_eirp: typing.Optional[jsii.Number] = None,
    ping_slot_dr: typing.Optional[jsii.Number] = None,
    ping_slot_freq: typing.Optional[jsii.Number] = None,
    ping_slot_period: typing.Optional[jsii.Number] = None,
    reg_params_revision: typing.Optional[builtins.str] = None,
    rf_region: typing.Optional[builtins.str] = None,
    rx_data_rate2: typing.Optional[jsii.Number] = None,
    rx_delay1: typing.Optional[jsii.Number] = None,
    rx_dr_offset1: typing.Optional[jsii.Number] = None,
    rx_freq2: typing.Optional[jsii.Number] = None,
    supports32_bit_f_cnt: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    supports_class_b: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    supports_class_c: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    supports_join: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__786fff6434f78dd9f30b4cfe18f3ed2ed4c80556a2b98404510ae635247bea60(
    *,
    lo_ra_wan: typing.Optional[typing.Union[typing.Union[CfnDeviceProfile.LoRaWANDeviceProfileProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable]] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fac50800fa79fde1d0f1a7bfce65467532f94e2dd3e9500046e6714c9ee8990e(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    firmware_update_image: builtins.str,
    firmware_update_role: builtins.str,
    lo_ra_wan: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnFuotaTask.LoRaWANProperty, typing.Dict[builtins.str, typing.Any]]],
    associate_multicast_group: typing.Optional[builtins.str] = None,
    associate_wireless_device: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    disassociate_multicast_group: typing.Optional[builtins.str] = None,
    disassociate_wireless_device: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__574b4629294334955ce6611455e2967cdf368d8d573cf9e0967c46ed618cb602(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bc81f32f2986cf67b5338aeaba0d8357a04e4dd0383b3b0e850dc8ec9baec68(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b99a931b2d8ad5f6646c170e4eeab1c40b6594745f02910413d4a4f5f4de66a7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a13d972a00b2e05226cccf6f832174bb0318fc14f92e178a44ef297404714f6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1dfcb6d788444ab7fddf1d72a0fed6ee51ba0b594a4e005f7da26398eeb252b(
    value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnFuotaTask.LoRaWANProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3b31f9255759727056bf9c371484663111b2a25fcbc621806adbd08b23e9bf6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ef7ee0475718cd5e7cce1ab7bc2db177557a091137e157b1a31c93a252c6278(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2a29dcd7459b584c8f47ef33fbe5ac33c53b6f9499a6647962851ffc48e3044(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63dddc2cbfffcab1ce28810bc7fd476c21d6c3ffe89753f0339b3946d596c780(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b57451d39cf92c1c3968b85e86f24d3d5c84f59993bcc64472aae0afce9f40b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cb0945d4b06e6d9555be90c010b58e1188907319028ca761c8f40ab1bfd44ba(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7f394b2c3cada2f758424af2b04612603fd774011a3cf64273266119928877b(
    *,
    rf_region: builtins.str,
    start_time: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e35293df026c833950b6cca8691adb2956ae230656d925e366bac133d424834a(
    *,
    firmware_update_image: builtins.str,
    firmware_update_role: builtins.str,
    lo_ra_wan: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnFuotaTask.LoRaWANProperty, typing.Dict[builtins.str, typing.Any]]],
    associate_multicast_group: typing.Optional[builtins.str] = None,
    associate_wireless_device: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    disassociate_multicast_group: typing.Optional[builtins.str] = None,
    disassociate_wireless_device: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a2e05fa345b05f90f387c25508cdd51b56624ed2f49a6606328d2d548181820(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    lo_ra_wan: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnMulticastGroup.LoRaWANProperty, typing.Dict[builtins.str, typing.Any]]],
    associate_wireless_device: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    disassociate_wireless_device: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4de8527c39ab1d6e8c43a277cc2621cfd2749312f1e0694f9650adc9b23a2073(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0823deac008b9fb7f95e9bc1675655a06c6d4f388e8b0859225ad9b14a442741(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cbe8a4f8e06bb7a860cb0baab06842b8f4b0598afba3017867156d184004132(
    value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnMulticastGroup.LoRaWANProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__707cc48ddfdd5448a4a796d8f52b97fe9da0b1fc8b209a6091ca0e5382908174(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18801e24de5d350eb998f7a24278e5de6cba1d4979b3899774f51d95f04a32db(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__babf64259763222e9200372f8f9a0dc47f9344c566a0e18735c034109a5e4dca(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab82d1d3876064a7214b1df689f194e9045000c7650ab8ad9f395a4739628719(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be6c8762f813fbf9a7591812bd531240173637e378321fb3b31d14215401aeaf(
    *,
    dl_class: builtins.str,
    rf_region: builtins.str,
    number_of_devices_in_group: typing.Optional[jsii.Number] = None,
    number_of_devices_requested: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6520d54ed44ebc8cc25979431512f73387c8209299844ee263df28b92033bb1d(
    *,
    lo_ra_wan: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnMulticastGroup.LoRaWANProperty, typing.Dict[builtins.str, typing.Any]]],
    associate_wireless_device: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    disassociate_wireless_device: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d967395ceebc9ab2779b47d78fba79166b5164b9ddcf171e133a13c7e899d4d1(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    trace_content: typing.Any = None,
    wireless_devices: typing.Optional[typing.Sequence[builtins.str]] = None,
    wireless_gateways: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7bc22364251ed1bcc2143106adcf75e5da9af83909fb8dbb99b4aebfcb0ff1e(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa939ffc0ec5d1811a752ca54b711682aaa2cb478c3770f3c37aee0bf77d8809(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de7a3f4635556d9edd70ebfdc7ac76aae27772707d845e4abef3cce418b4c740(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8df36495c789634bd67810c6db00a288f2ba47fc6339669d0c775506dd31cb9a(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20758c77a313146e5260d9586cec253e25535329d4a39dcaf98051d9957e1c18(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aafaec887cd8114ccf9d608c5397bd1f127ebb95cabe2668eb2903348b478433(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5d18077851536aad976972dffe900741f397b7339e333381ce7c1dab2fd0a60(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62e528c8e83ed1e47d66e196d0f9b1d67bd658d26a7c43bc9a0e0c4e590aebbc(
    *,
    log_level: typing.Optional[builtins.str] = None,
    wireless_device_frame_info: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14b9c0811c4a82e27972c18d49cfc19d2dfeff1e5299795b35da2982117d441c(
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    trace_content: typing.Any = None,
    wireless_devices: typing.Optional[typing.Sequence[builtins.str]] = None,
    wireless_gateways: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70fa94c1bc06e6c68aa2fb8408642703cf7651fcca48eee0a681153c5361bfc4(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    account_linked: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    fingerprint: typing.Optional[builtins.str] = None,
    partner_account_id: typing.Optional[builtins.str] = None,
    partner_type: typing.Optional[builtins.str] = None,
    sidewalk: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnPartnerAccount.SidewalkAccountInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sidewalk_update: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnPartnerAccount.SidewalkUpdateAccountProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__361d87c6c60da6c1a65dbc96b9d6f09302f8fe6b2551bc7d5ed16242aa3a05e9(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0e6929d69455bc76d2614d96d62c6c2f5e7d298052b3cd99d5be6e9e056683e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54c3658dd86f8c293397ceebb41841106b95ea260fd61b6ab5f04f09f37e8a1f(
    value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1183306b1b10cd491c3bdbb0fcaa09113a705efd6407184bea12bd682f27f91a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__968d6c73746e0ec8da5bb8f0b9470adc72e1c8cf2241ecfa9a1bd3a22e393f57(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16046c75847d64ccb61aaf3f1e5226de8ac3ac2c7af34ee879fdbfcb85f07595(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be9da21e25b74972fc3cccb1a59fa7790e236e910c522f33402511663fc89542(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnPartnerAccount.SidewalkAccountInfoProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30de54314a9ba79d2acc51a5b90823a0c2b5ca7ce2eaa40df13553d911ec5a7b(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnPartnerAccount.SidewalkUpdateAccountProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b46e7e557b3d3afeee1d77a34fe5a132c0912080c061e0a95d82ab815def6b65(
    *,
    app_server_private_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b049fcd6c2dd99820d74621419ff2d298754483761f2e7a3c6d1c7201b7cb63d(
    *,
    amazon_id: typing.Optional[builtins.str] = None,
    arn: typing.Optional[builtins.str] = None,
    fingerprint: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb7cc79f47ef6e08577cb3eb6b56f8b6dd8e8a60703b4ab85fab0f10c4708237(
    *,
    app_server_private_key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0134fa6a451b04e0c7892ec364f0aeed88594db85f4499f076f7082172c88b64(
    *,
    account_linked: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    fingerprint: typing.Optional[builtins.str] = None,
    partner_account_id: typing.Optional[builtins.str] = None,
    partner_type: typing.Optional[builtins.str] = None,
    sidewalk: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnPartnerAccount.SidewalkAccountInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sidewalk_update: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnPartnerAccount.SidewalkUpdateAccountProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7dbd2107f56db404db84d056e6501ffc6e000bb87f7182a023832a1484ae229(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    lo_ra_wan: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnServiceProfile.LoRaWANServiceProfileProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02f0e00dafa7fc99f30699ab4ba046138def30ed247810ca72b4ec35158ef92a(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f2bdce7658589ce40b4c1f0bf84f034c4c77df7cc869b77cda2b67e03e3664f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1018d5d0ec6563797cbbcb2c4caf64a35ebe16b38b14a32585a201d64b2223b(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnServiceProfile.LoRaWANServiceProfileProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4b5c0ad26d176237f37fa4f10f8b549f2d9b05e89e5d24253ff9b6d1884ed7e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33dce9396f76e7b3fc8db88e167d0eacc3f17c554287d779def7c57e33267d9b(
    *,
    add_gw_metadata: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    channel_mask: typing.Optional[builtins.str] = None,
    dev_status_req_freq: typing.Optional[jsii.Number] = None,
    dl_bucket_size: typing.Optional[jsii.Number] = None,
    dl_rate: typing.Optional[jsii.Number] = None,
    dl_rate_policy: typing.Optional[builtins.str] = None,
    dr_max: typing.Optional[jsii.Number] = None,
    dr_min: typing.Optional[jsii.Number] = None,
    hr_allowed: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    min_gw_diversity: typing.Optional[jsii.Number] = None,
    nwk_geo_loc: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    pr_allowed: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    ra_allowed: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    report_dev_status_battery: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    report_dev_status_margin: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    target_per: typing.Optional[jsii.Number] = None,
    ul_bucket_size: typing.Optional[jsii.Number] = None,
    ul_rate: typing.Optional[jsii.Number] = None,
    ul_rate_policy: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7a73d9cd4af9e2bfcb9ba2833b981c2f200576b6a8d4e3c3e3186a0ddd358cc(
    *,
    lo_ra_wan: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnServiceProfile.LoRaWANServiceProfileProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1a898decb0ee15fbffbe4ea6b9137b63ee1c9d0aa59ffa7d14c8d5794ebf1d5(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    auto_create_tasks: typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable],
    lo_ra_wan_update_gateway_task_entry: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnTaskDefinition.LoRaWANUpdateGatewayTaskEntryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    task_definition_type: typing.Optional[builtins.str] = None,
    update: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnTaskDefinition.UpdateWirelessGatewayTaskCreateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e540a0ecd0c87a779951f5b7f64357528afe84527bbf88db7329d647c18abdd8(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f48db4c9acdbc97be0ad7b9950c3283769d89909a1e71ecc16ede5bc678adfda(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61710283d06049b3691d6878062e3108f69e4909c7f117b6f7ee119dd8749e38(
    value: typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc46980d503af071f2a1c6e0f7ea9f9e6f2325b771988d6eab1fce8e1783edc3(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnTaskDefinition.LoRaWANUpdateGatewayTaskEntryProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__344198b16445ad641747a7dd1b1641325ca58892eddbfefa3fb4f7aa0bd0b98d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0a0dc21e3824a8118f7b83ee26668d51e90092cb16dede2d05ec87f4c03b88e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04812ec7d3b3ff2eb351e1d6e6c1d54ce2b5fda69f6d848e8445c0e1c56632e0(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnTaskDefinition.UpdateWirelessGatewayTaskCreateProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78d4a261f6b892a4248e96f0d4ec1d748d653d0bf50c58fc3705018219a45da9(
    *,
    model: typing.Optional[builtins.str] = None,
    package_version: typing.Optional[builtins.str] = None,
    station: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67d12e61f380ff9154d4537ba69b22ace2544dd5f93588795880579f144fb67d(
    *,
    current_version: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnTaskDefinition.LoRaWANGatewayVersionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sig_key_crc: typing.Optional[jsii.Number] = None,
    update_signature: typing.Optional[builtins.str] = None,
    update_version: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnTaskDefinition.LoRaWANGatewayVersionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21dcf59b2bc153afbee45193a56ae699f588ca9b5558504487599e49f32dc7be(
    *,
    current_version: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnTaskDefinition.LoRaWANGatewayVersionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    update_version: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnTaskDefinition.LoRaWANGatewayVersionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72082ec5a22edd46f8332768162eabcff23292f62cf7ccba54980752c3b19a8f(
    *,
    lo_ra_wan: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnTaskDefinition.LoRaWANUpdateGatewayTaskCreateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    update_data_role: typing.Optional[builtins.str] = None,
    update_data_source: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a42881aba1e0d388e940986d57a2df4c63a4c3e1e107c7869f4290f43ba5596d(
    *,
    auto_create_tasks: typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable],
    lo_ra_wan_update_gateway_task_entry: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnTaskDefinition.LoRaWANUpdateGatewayTaskEntryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    task_definition_type: typing.Optional[builtins.str] = None,
    update: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnTaskDefinition.UpdateWirelessGatewayTaskCreateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2498b50cdcf80e13c7919648027ad8436c24e0c64a692cf90619497c8f4ffcd6(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    destination_name: builtins.str,
    type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    last_uplink_received_at: typing.Optional[builtins.str] = None,
    lo_ra_wan: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnWirelessDevice.LoRaWANDeviceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    thing_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b5f575ef0dc4cf624fecf0acc5b30b3c4e1c3d9662bafc0aadeacef5ad751c3(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b297ed62dd177f9b47ff1277a279d19962680c2999f0df7276e1f61f16c9a4d4(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00ba3f47e8dcef98e11c660c384c4b2a7c149aa09074e99eabd9275a1868992a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__050d401141307e8c7ead438df2bd58d8bf5d154625cea5a162e7e6a9017e3669(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cccb359e115f4909697886eb6450f59fc406b1d353adfe95a57f6dd63afe32c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57665aba99e886a54639b1411ecf712ff706d3ddf8afa21ae38f8f78557bf2b5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35ecf775c88d2eb74c4b3344ba6232ca231e8ac24daeb03d664cbc6d40b11d80(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnWirelessDevice.LoRaWANDeviceProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2e9b78a64a1ec87c985426e49b4b36681a523fdc37870df62f12dcbed230a01(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87d4e579c6fa422ba32251ac7877fe7e935f33e3c9bf2f8d258c5b421c85c8c0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d38550f49273904c8ee61210f3208e42c0b4df5a17b9315741fb4134c4f9f03(
    *,
    dev_addr: builtins.str,
    session_keys: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnWirelessDevice.SessionKeysAbpV10xProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aaf3ee7ceb3259cc7dcb668de5f7e5557789a9b4259a5c4f29a54495f7d63e32(
    *,
    dev_addr: builtins.str,
    session_keys: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnWirelessDevice.SessionKeysAbpV11Property, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b78ec2b6d6078b53cda50049b04e47266b3bc3db89298bf8dca91e21abc82c5(
    *,
    abp_v10_x: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnWirelessDevice.AbpV10xProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    abp_v11: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnWirelessDevice.AbpV11Property, typing.Dict[builtins.str, typing.Any]]]] = None,
    dev_eui: typing.Optional[builtins.str] = None,
    device_profile_id: typing.Optional[builtins.str] = None,
    otaa_v10_x: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnWirelessDevice.OtaaV10xProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    otaa_v11: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnWirelessDevice.OtaaV11Property, typing.Dict[builtins.str, typing.Any]]]] = None,
    service_profile_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0f71a8ae506773c267541441910c6a924c4e20ae4017823a1f1320f051b2d69(
    *,
    app_eui: builtins.str,
    app_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a333397b966e4f12f635f015fd9f6314f0900609dc3fee12f17ae9ff0c8656a3(
    *,
    app_key: builtins.str,
    join_eui: builtins.str,
    nwk_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__693d578f082eaee5b5cb0dea9e5158c79e26907b8729f4bbea847b376f17e5b7(
    *,
    app_s_key: builtins.str,
    nwk_s_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__378afcb9d3baf5597fe62761a2fcdc90d7922a86151e3ff57497d7c9cb3221a1(
    *,
    app_s_key: builtins.str,
    f_nwk_s_int_key: builtins.str,
    nwk_s_enc_key: builtins.str,
    s_nwk_s_int_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82e04df14f0377fc270cbe3177e2f24bbf0bfda173dfe89eff85b6feadecca8d(
    *,
    destination_name: builtins.str,
    type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    last_uplink_received_at: typing.Optional[builtins.str] = None,
    lo_ra_wan: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnWirelessDevice.LoRaWANDeviceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    thing_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a89c4b5de62c743b993367fa1c205bc1c752e37b8621fecdddfadd9745e7cd3(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    lo_ra_wan: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnWirelessGateway.LoRaWANGatewayProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    last_uplink_received_at: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    thing_arn: typing.Optional[builtins.str] = None,
    thing_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07dae05bacc1b48e3a5f09635792cc5536249734a54e6fd363ffd3adcb5f5fbd(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c2495120ba7aee15d44de3ebad8c502141cea2a0f35fd83f3453e038e44aa0a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97f73752e7eb94263226cdcbd4b4b090598eedd2493d6fb0f90aaaf27a5f13dc(
    value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnWirelessGateway.LoRaWANGatewayProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7307bc5853df9c6f89bb2a273fc61e71e90262e0840060fe9cbd3de583ab782b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97f97073dc5ee2c04af738a298813d0961792f853fad84d73d2a70ccc26cb51e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7d788a768fa1121cb651f157751bcea3746163332e857fefeef850f2c59fdee(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24529e4f39a4d1d88aa00af84e16bbe41ecf62bd192bbb4724528ed323e3eb84(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30f1d8a14839748583f9cb5e88ce35c3cb139b3838df7df8cc4ea5ce16324d32(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa02e2b37976d1cc9825697c3d4bf4dfff25811d5b5cab49c1d3fa85c0b39d3d(
    *,
    gateway_eui: builtins.str,
    rf_region: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fcd953583aa54651f18e0c55e234398e5b33c25a61ff45400d2f92ea434ae58(
    *,
    lo_ra_wan: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnWirelessGateway.LoRaWANGatewayProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    last_uplink_received_at: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    thing_arn: typing.Optional[builtins.str] = None,
    thing_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

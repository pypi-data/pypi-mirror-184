'''
# AWS::SSO Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_sso as sso
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for SSO construct libraries](https://constructs.dev/search?q=sso)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::SSO resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SSO.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::SSO](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SSO.html).

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
class CfnAssignment(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sso.CfnAssignment",
):
    '''A CloudFormation ``AWS::SSO::Assignment``.

    Assigns access to a Principal for a specified AWS account using a specified permission set.
    .. epigraph::

       The term *principal* here refers to a user or group that is defined in IAM Identity Center .

    :cloudformationResource: AWS::SSO::Assignment
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_sso as sso
        
        cfn_assignment = sso.CfnAssignment(self, "MyCfnAssignment",
            instance_arn="instanceArn",
            permission_set_arn="permissionSetArn",
            principal_id="principalId",
            principal_type="principalType",
            target_id="targetId",
            target_type="targetType"
        )
    '''

    def __init__(
        self,
        scope: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        instance_arn: builtins.str,
        permission_set_arn: builtins.str,
        principal_id: builtins.str,
        principal_type: builtins.str,
        target_id: builtins.str,
        target_type: builtins.str,
    ) -> None:
        '''Create a new ``AWS::SSO::Assignment``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html>`_ in the *AWS General Reference* .
        :param permission_set_arn: The ARN of the permission set.
        :param principal_id: An identifier for an object in IAM Identity Center, such as a user or group. PrincipalIds are GUIDs (For example, f81d4fae-7dec-11d0-a765-00a0c91e6bf6). For more information about PrincipalIds in IAM Identity Center, see the `IAM Identity Center Identity Store API Reference <https://docs.aws.amazon.com//singlesignon/latest/IdentityStoreAPIReference/welcome.html>`_ .
        :param principal_type: The entity type for which the assignment will be created.
        :param target_id: TargetID is an AWS account identifier, typically a 10-12 digit string (For example, 123456789012).
        :param target_type: The entity type for which the assignment will be created.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9583c2550c355b39916bdb43c9d364b996fab7f826903887b911aab9fe066751)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAssignmentProps(
            instance_arn=instance_arn,
            permission_set_arn=permission_set_arn,
            principal_id=principal_id,
            principal_type=principal_type,
            target_id=target_id,
            target_type=target_type,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f518667452efb368ade61d083684ad7f114f296189db531f40176aea58ecec14)
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
            type_hints = typing.get_type_hints(_typecheckingstub__500d2ae81864550232127f63fda39b595ca35b5ebbdc26aae3cac7f72938f4dd)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''The ARN of the IAM Identity Center instance under which the operation will be executed.

        For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html>`_ in the *AWS General Reference* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-instancearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d5cdd981dcf4bf948e4b5d57d3ef313f17e7978c210feccb60754b3380636f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceArn", value)

    @builtins.property
    @jsii.member(jsii_name="permissionSetArn")
    def permission_set_arn(self) -> builtins.str:
        '''The ARN of the permission set.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-permissionsetarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "permissionSetArn"))

    @permission_set_arn.setter
    def permission_set_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__369d567c64088cd44c984c91075d5826f6ea1f10ded5cc2f08ac967c66dd185b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissionSetArn", value)

    @builtins.property
    @jsii.member(jsii_name="principalId")
    def principal_id(self) -> builtins.str:
        '''An identifier for an object in IAM Identity Center, such as a user or group.

        PrincipalIds are GUIDs (For example, f81d4fae-7dec-11d0-a765-00a0c91e6bf6). For more information about PrincipalIds in IAM Identity Center, see the `IAM Identity Center Identity Store API Reference <https://docs.aws.amazon.com//singlesignon/latest/IdentityStoreAPIReference/welcome.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-principalid
        '''
        return typing.cast(builtins.str, jsii.get(self, "principalId"))

    @principal_id.setter
    def principal_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d78fef8f4b2a48de81e185d0edb82f6c4a7471be00428cd080c4eff958102bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "principalId", value)

    @builtins.property
    @jsii.member(jsii_name="principalType")
    def principal_type(self) -> builtins.str:
        '''The entity type for which the assignment will be created.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-principaltype
        '''
        return typing.cast(builtins.str, jsii.get(self, "principalType"))

    @principal_type.setter
    def principal_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3ec63d8083f159d4e9f9c662e7070231c3d577932d6444255843a9691837161)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "principalType", value)

    @builtins.property
    @jsii.member(jsii_name="targetId")
    def target_id(self) -> builtins.str:
        '''TargetID is an AWS account identifier, typically a 10-12 digit string (For example, 123456789012).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-targetid
        '''
        return typing.cast(builtins.str, jsii.get(self, "targetId"))

    @target_id.setter
    def target_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3b7ed7b671faae1d71292c1247c29e35ecb3e149564a196364fd29684a3cc78)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetId", value)

    @builtins.property
    @jsii.member(jsii_name="targetType")
    def target_type(self) -> builtins.str:
        '''The entity type for which the assignment will be created.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-targettype
        '''
        return typing.cast(builtins.str, jsii.get(self, "targetType"))

    @target_type.setter
    def target_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c62b78fc1f690b0fc535ce0b5f90eb5188fae02c9f21522014ea54c33773302)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetType", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sso.CfnAssignmentProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_arn": "instanceArn",
        "permission_set_arn": "permissionSetArn",
        "principal_id": "principalId",
        "principal_type": "principalType",
        "target_id": "targetId",
        "target_type": "targetType",
    },
)
class CfnAssignmentProps:
    def __init__(
        self,
        *,
        instance_arn: builtins.str,
        permission_set_arn: builtins.str,
        principal_id: builtins.str,
        principal_type: builtins.str,
        target_id: builtins.str,
        target_type: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnAssignment``.

        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html>`_ in the *AWS General Reference* .
        :param permission_set_arn: The ARN of the permission set.
        :param principal_id: An identifier for an object in IAM Identity Center, such as a user or group. PrincipalIds are GUIDs (For example, f81d4fae-7dec-11d0-a765-00a0c91e6bf6). For more information about PrincipalIds in IAM Identity Center, see the `IAM Identity Center Identity Store API Reference <https://docs.aws.amazon.com//singlesignon/latest/IdentityStoreAPIReference/welcome.html>`_ .
        :param principal_type: The entity type for which the assignment will be created.
        :param target_id: TargetID is an AWS account identifier, typically a 10-12 digit string (For example, 123456789012).
        :param target_type: The entity type for which the assignment will be created.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_sso as sso
            
            cfn_assignment_props = sso.CfnAssignmentProps(
                instance_arn="instanceArn",
                permission_set_arn="permissionSetArn",
                principal_id="principalId",
                principal_type="principalType",
                target_id="targetId",
                target_type="targetType"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a0fe0f0e6bbca20ac0efc0ff958d821f21e5d0d4b4fc2a49ca65e624cd45f88)
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
            check_type(argname="argument permission_set_arn", value=permission_set_arn, expected_type=type_hints["permission_set_arn"])
            check_type(argname="argument principal_id", value=principal_id, expected_type=type_hints["principal_id"])
            check_type(argname="argument principal_type", value=principal_type, expected_type=type_hints["principal_type"])
            check_type(argname="argument target_id", value=target_id, expected_type=type_hints["target_id"])
            check_type(argname="argument target_type", value=target_type, expected_type=type_hints["target_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_arn": instance_arn,
            "permission_set_arn": permission_set_arn,
            "principal_id": principal_id,
            "principal_type": principal_type,
            "target_id": target_id,
            "target_type": target_type,
        }

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The ARN of the IAM Identity Center instance under which the operation will be executed.

        For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html>`_ in the *AWS General Reference* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def permission_set_arn(self) -> builtins.str:
        '''The ARN of the permission set.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-permissionsetarn
        '''
        result = self._values.get("permission_set_arn")
        assert result is not None, "Required property 'permission_set_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def principal_id(self) -> builtins.str:
        '''An identifier for an object in IAM Identity Center, such as a user or group.

        PrincipalIds are GUIDs (For example, f81d4fae-7dec-11d0-a765-00a0c91e6bf6). For more information about PrincipalIds in IAM Identity Center, see the `IAM Identity Center Identity Store API Reference <https://docs.aws.amazon.com//singlesignon/latest/IdentityStoreAPIReference/welcome.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-principalid
        '''
        result = self._values.get("principal_id")
        assert result is not None, "Required property 'principal_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def principal_type(self) -> builtins.str:
        '''The entity type for which the assignment will be created.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-principaltype
        '''
        result = self._values.get("principal_type")
        assert result is not None, "Required property 'principal_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_id(self) -> builtins.str:
        '''TargetID is an AWS account identifier, typically a 10-12 digit string (For example, 123456789012).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-targetid
        '''
        result = self._values.get("target_id")
        assert result is not None, "Required property 'target_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_type(self) -> builtins.str:
        '''The entity type for which the assignment will be created.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-targettype
        '''
        result = self._values.get("target_type")
        assert result is not None, "Required property 'target_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAssignmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnInstanceAccessControlAttributeConfiguration(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sso.CfnInstanceAccessControlAttributeConfiguration",
):
    '''A CloudFormation ``AWS::SSO::InstanceAccessControlAttributeConfiguration``.

    Enables the attribute-based access control (ABAC) feature for the specified IAM Identity Center instance. You can also specify new attributes to add to your ABAC configuration during the enabling process. For more information about ABAC, see `Attribute-Based Access Control <https://docs.aws.amazon.com//singlesignon/latest/userguide/abac.html>`_ in the *IAM Identity Center User Guide* .
    .. epigraph::

       The ``InstanceAccessControlAttributeConfiguration`` property has been deprecated but is still supported for backwards compatibility purposes. We recommend that you use the ``AccessControlAttributes`` property instead.

    :cloudformationResource: AWS::SSO::InstanceAccessControlAttributeConfiguration
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_sso as sso
        
        cfn_instance_access_control_attribute_configuration = sso.CfnInstanceAccessControlAttributeConfiguration(self, "MyCfnInstanceAccessControlAttributeConfiguration",
            instance_arn="instanceArn",
        
            # the properties below are optional
            access_control_attributes=[sso.CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty(
                key="key",
                value=sso.CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeValueProperty(
                    source=["source"]
                )
            )]
        )
    '''

    def __init__(
        self,
        scope: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        instance_arn: builtins.str,
        access_control_attributes: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[typing.Union["CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty", typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable]]]] = None,
    ) -> None:
        '''Create a new ``AWS::SSO::InstanceAccessControlAttributeConfiguration``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation will be executed.
        :param access_control_attributes: Lists the attributes that are configured for ABAC in the specified IAM Identity Center instance.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86f8072315f2a7fa7058307331311dce99c06c1d2c210fee221e69e37c5b7e79)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnInstanceAccessControlAttributeConfigurationProps(
            instance_arn=instance_arn,
            access_control_attributes=access_control_attributes,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25a6cd1fedf8fe6e20ed0ee6a2c25bf567c5226f9e7b33fe0c1c9d6ca3f40292)
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
            type_hints = typing.get_type_hints(_typecheckingstub__beced262b5a95170e93c29e3a50c2f2fbcd5c5b95cd4a90be60b78083c4fdc01)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''The ARN of the IAM Identity Center instance under which the operation will be executed.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html#cfn-sso-instanceaccesscontrolattributeconfiguration-instancearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccfe8e729fb71bdd9f0239a159f75713a85f77b0470bfe8492c18163bd795711)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceArn", value)

    @builtins.property
    @jsii.member(jsii_name="accessControlAttributes")
    def access_control_attributes(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union["CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty", _aws_cdk_core_f4b25747.IResolvable]]]]:
        '''Lists the attributes that are configured for ABAC in the specified IAM Identity Center instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html#cfn-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattributes
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union["CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty", _aws_cdk_core_f4b25747.IResolvable]]]], jsii.get(self, "accessControlAttributes"))

    @access_control_attributes.setter
    def access_control_attributes(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union["CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty", _aws_cdk_core_f4b25747.IResolvable]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4f5b2ec55dc7091ab2bf1343cf84a27f8e708f4e9c1e757e1dd2ba351a2a368)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessControlAttributes", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sso.CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class AccessControlAttributeProperty:
        def __init__(
            self,
            *,
            key: builtins.str,
            value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeValueProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''These are IAM Identity Center identity store attributes that you can configure for use in attributes-based access control (ABAC).

            You can create permissions policies that determine who can access your AWS resources based upon the configured attribute values. When you enable ABAC and specify ``AccessControlAttributes`` , IAM Identity Center passes the attribute values of the authenticated user into IAM for use in policy evaluation.

            :param key: The name of the attribute associated with your identities in your identity source. This is used to map a specified attribute in your identity source with an attribute in IAM Identity Center .
            :param value: The value used for mapping a specified attribute to an identity source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sso as sso
                
                access_control_attribute_property = sso.CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty(
                    key="key",
                    value=sso.CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeValueProperty(
                        source=["source"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d176c0d6109001f5985ec36d4f688b1be5ea2f6adbbebccfa2747f5c66301d11)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''The name of the attribute associated with your identities in your identity source.

            This is used to map a specified attribute in your identity source with an attribute in IAM Identity Center .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute.html#cfn-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(
            self,
        ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeValueProperty"]:
            '''The value used for mapping a specified attribute to an identity source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute.html#cfn-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeValueProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AccessControlAttributeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sso.CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeValueProperty",
        jsii_struct_bases=[],
        name_mapping={"source": "source"},
    )
    class AccessControlAttributeValueProperty:
        def __init__(self, *, source: typing.Sequence[builtins.str]) -> None:
            '''The value used for mapping a specified attribute to an identity source.

            :param source: The identity source to use when mapping a specified attribute to IAM Identity Center .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattributevalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sso as sso
                
                access_control_attribute_value_property = sso.CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeValueProperty(
                    source=["source"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8c2d5dbdc9d2d6a9d1a4d6f93e9b67d2b1bae3aa5d796fa7574587be603c7d85)
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "source": source,
            }

        @builtins.property
        def source(self) -> typing.List[builtins.str]:
            '''The identity source to use when mapping a specified attribute to IAM Identity Center .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattributevalue.html#cfn-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattributevalue-source
            '''
            result = self._values.get("source")
            assert result is not None, "Required property 'source' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AccessControlAttributeValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sso.CfnInstanceAccessControlAttributeConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_arn": "instanceArn",
        "access_control_attributes": "accessControlAttributes",
    },
)
class CfnInstanceAccessControlAttributeConfigurationProps:
    def __init__(
        self,
        *,
        instance_arn: builtins.str,
        access_control_attributes: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[typing.Union[CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnInstanceAccessControlAttributeConfiguration``.

        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation will be executed.
        :param access_control_attributes: Lists the attributes that are configured for ABAC in the specified IAM Identity Center instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_sso as sso
            
            cfn_instance_access_control_attribute_configuration_props = sso.CfnInstanceAccessControlAttributeConfigurationProps(
                instance_arn="instanceArn",
            
                # the properties below are optional
                access_control_attributes=[sso.CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty(
                    key="key",
                    value=sso.CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeValueProperty(
                        source=["source"]
                    )
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97a5059d3e57502a0b2ab04d980fcca841a3657fd77abe791eb0cb6a3f72dbe9)
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
            check_type(argname="argument access_control_attributes", value=access_control_attributes, expected_type=type_hints["access_control_attributes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_arn": instance_arn,
        }
        if access_control_attributes is not None:
            self._values["access_control_attributes"] = access_control_attributes

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The ARN of the IAM Identity Center instance under which the operation will be executed.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html#cfn-sso-instanceaccesscontrolattributeconfiguration-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_control_attributes(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty, _aws_cdk_core_f4b25747.IResolvable]]]]:
        '''Lists the attributes that are configured for ABAC in the specified IAM Identity Center instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html#cfn-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattributes
        '''
        result = self._values.get("access_control_attributes")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty, _aws_cdk_core_f4b25747.IResolvable]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnInstanceAccessControlAttributeConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnPermissionSet(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sso.CfnPermissionSet",
):
    '''A CloudFormation ``AWS::SSO::PermissionSet``.

    Specifies a permission set within a specified IAM Identity Center instance.

    :cloudformationResource: AWS::SSO::PermissionSet
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_sso as sso
        
        # inline_policy: Any
        
        cfn_permission_set = sso.CfnPermissionSet(self, "MyCfnPermissionSet",
            instance_arn="instanceArn",
            name="name",
        
            # the properties below are optional
            customer_managed_policy_references=[sso.CfnPermissionSet.CustomerManagedPolicyReferenceProperty(
                name="name",
        
                # the properties below are optional
                path="path"
            )],
            description="description",
            inline_policy=inline_policy,
            managed_policies=["managedPolicies"],
            permissions_boundary=sso.CfnPermissionSet.PermissionsBoundaryProperty(
                customer_managed_policy_reference=sso.CfnPermissionSet.CustomerManagedPolicyReferenceProperty(
                    name="name",
        
                    # the properties below are optional
                    path="path"
                ),
                managed_policy_arn="managedPolicyArn"
            ),
            relay_state_type="relayStateType",
            session_duration="sessionDuration",
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
        instance_arn: builtins.str,
        name: builtins.str,
        customer_managed_policy_references: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnPermissionSet.CustomerManagedPolicyReferenceProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        inline_policy: typing.Any = None,
        managed_policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        permissions_boundary: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnPermissionSet.PermissionsBoundaryProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        relay_state_type: typing.Optional[builtins.str] = None,
        session_duration: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::SSO::PermissionSet``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html>`_ in the *AWS General Reference* .
        :param name: The name of the permission set.
        :param customer_managed_policy_references: Specifies the names and paths of the customer managed policies that you have attached to your permission set.
        :param description: The description of the ``PermissionSet`` .
        :param inline_policy: The inline policy that is attached to the permission set. .. epigraph:: For ``Length Constraints`` , if a valid ARN is provided for a permission set, it is possible for an empty inline policy to be returned.
        :param managed_policies: A structure that stores the details of the AWS managed policy.
        :param permissions_boundary: Specifies the configuration of the AWS managed or customer managed policy that you want to set as a permissions boundary. Specify either ``CustomerManagedPolicyReference`` to use the name and path of a customer managed policy, or ``ManagedPolicyArn`` to use the ARN of an AWS managed policy. A permissions boundary represents the maximum permissions that any policy can grant your role. For more information, see `Permissions boundaries for IAM entities <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`_ in the *IAM User Guide* . .. epigraph:: Policies used as permissions boundaries don't provide permissions. You must also attach an IAM policy to the role. To learn how the effective permissions for a role are evaluated, see `IAM JSON policy evaluation logic <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html>`_ in the *IAM User Guide* .
        :param relay_state_type: Used to redirect users within the application during the federation authentication process.
        :param session_duration: The length of time that the application user sessions are valid for in the ISO-8601 standard.
        :param tags: The tags to attach to the new ``PermissionSet`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__367b6705f06c7d6f14f3907264e13ee3268282a0b43167d8e2091acfbd3837b5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPermissionSetProps(
            instance_arn=instance_arn,
            name=name,
            customer_managed_policy_references=customer_managed_policy_references,
            description=description,
            inline_policy=inline_policy,
            managed_policies=managed_policies,
            permissions_boundary=permissions_boundary,
            relay_state_type=relay_state_type,
            session_duration=session_duration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3871a5f733bae8e2454777749d347a18a93e701637db3dfb54efbb8176d541f6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8a10a52adcecd17e07c26d1774311a036e56a2efe69455ece053f95e66902d43)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrPermissionSetArn")
    def attr_permission_set_arn(self) -> builtins.str:
        '''The permission set ARN of the permission set, such as ``arn:aws:sso:::permissionSet/ins-instanceid/ps-permissionsetid`` .

        :cloudformationAttribute: PermissionSetArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPermissionSetArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _aws_cdk_core_f4b25747.TagManager:
        '''The tags to attach to the new ``PermissionSet`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-tags
        '''
        return typing.cast(_aws_cdk_core_f4b25747.TagManager, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="inlinePolicy")
    def inline_policy(self) -> typing.Any:
        '''The inline policy that is attached to the permission set.

        .. epigraph::

           For ``Length Constraints`` , if a valid ARN is provided for a permission set, it is possible for an empty inline policy to be returned.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-inlinepolicy
        '''
        return typing.cast(typing.Any, jsii.get(self, "inlinePolicy"))

    @inline_policy.setter
    def inline_policy(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23c013124c5e5747626106f316f80ec05d28c0f2bb42aad0b4c0484ef23e64b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inlinePolicy", value)

    @builtins.property
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''The ARN of the IAM Identity Center instance under which the operation will be executed.

        For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html>`_ in the *AWS General Reference* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-instancearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e99cefdb623dfeaeca734e1b313fa9ad4c5ba2a597ee1a2c79db923a39ca049)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the permission set.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__366b74787a4ce6ef91dfcdc2dd34d5a6121f6d2d248625a10848c8caf3e78d7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="customerManagedPolicyReferences")
    def customer_managed_policy_references(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnPermissionSet.CustomerManagedPolicyReferenceProperty"]]]]:
        '''Specifies the names and paths of the customer managed policies that you have attached to your permission set.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-customermanagedpolicyreferences
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnPermissionSet.CustomerManagedPolicyReferenceProperty"]]]], jsii.get(self, "customerManagedPolicyReferences"))

    @customer_managed_policy_references.setter
    def customer_managed_policy_references(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnPermissionSet.CustomerManagedPolicyReferenceProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c34427b6577a11ebe9586a8617e7dad9365d27e6fff1e37697502159f99bbe9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customerManagedPolicyReferences", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the ``PermissionSet`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__078985bd33bba614ff1cd57df92e6938fc83b6b4b65e16a4a4ed93ff2ac46a60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="managedPolicies")
    def managed_policies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A structure that stores the details of the AWS managed policy.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-managedpolicies
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "managedPolicies"))

    @managed_policies.setter
    def managed_policies(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e890f2651d96ddbf9135f831069f2d442f58ebd595ff9799441d64fb760e3bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedPolicies", value)

    @builtins.property
    @jsii.member(jsii_name="permissionsBoundary")
    def permissions_boundary(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnPermissionSet.PermissionsBoundaryProperty"]]:
        '''Specifies the configuration of the AWS managed or customer managed policy that you want to set as a permissions boundary.

        Specify either ``CustomerManagedPolicyReference`` to use the name and path of a customer managed policy, or ``ManagedPolicyArn`` to use the ARN of an AWS managed policy. A permissions boundary represents the maximum permissions that any policy can grant your role. For more information, see `Permissions boundaries for IAM entities <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`_ in the *IAM User Guide* .
        .. epigraph::

           Policies used as permissions boundaries don't provide permissions. You must also attach an IAM policy to the role. To learn how the effective permissions for a role are evaluated, see `IAM JSON policy evaluation logic <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html>`_ in the *IAM User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-permissionsboundary
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnPermissionSet.PermissionsBoundaryProperty"]], jsii.get(self, "permissionsBoundary"))

    @permissions_boundary.setter
    def permissions_boundary(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnPermissionSet.PermissionsBoundaryProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8c1049eea884b5607637074fdbe49a5614eb01ff62a8576786864c2d6cdad5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissionsBoundary", value)

    @builtins.property
    @jsii.member(jsii_name="relayStateType")
    def relay_state_type(self) -> typing.Optional[builtins.str]:
        '''Used to redirect users within the application during the federation authentication process.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-relaystatetype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "relayStateType"))

    @relay_state_type.setter
    def relay_state_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ace8e8388627a59ce1fac9185c7e2fa8db58b570297ce75b7b2cd1e599e0fec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "relayStateType", value)

    @builtins.property
    @jsii.member(jsii_name="sessionDuration")
    def session_duration(self) -> typing.Optional[builtins.str]:
        '''The length of time that the application user sessions are valid for in the ISO-8601 standard.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-sessionduration
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sessionDuration"))

    @session_duration.setter
    def session_duration(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1ce65fd9bd737f24bf4ec4f88b675c7c24498189e6f19074551e8ed0d49ea0f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionDuration", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sso.CfnPermissionSet.CustomerManagedPolicyReferenceProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "path": "path"},
    )
    class CustomerManagedPolicyReferenceProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            path: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the name and path of a customer managed policy.

            You must have an IAM policy that matches the name and path in each AWS account where you want to deploy your permission set.

            :param name: The name of the IAM policy that you have configured in each account where you want to deploy your permission set.
            :param path: The path to the IAM policy that you have configured in each account where you want to deploy your permission set. The default is ``/`` . For more information, see `Friendly names and paths <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-friendly-names>`_ in the *IAM User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-permissionset-customermanagedpolicyreference.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sso as sso
                
                customer_managed_policy_reference_property = sso.CfnPermissionSet.CustomerManagedPolicyReferenceProperty(
                    name="name",
                
                    # the properties below are optional
                    path="path"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ab5012337ba132ecbded8e31a31cd1f327045bf9c2ea2aa6d4e4815a7d58c60f)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }
            if path is not None:
                self._values["path"] = path

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the IAM policy that you have configured in each account where you want to deploy your permission set.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-permissionset-customermanagedpolicyreference.html#cfn-sso-permissionset-customermanagedpolicyreference-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def path(self) -> typing.Optional[builtins.str]:
            '''The path to the IAM policy that you have configured in each account where you want to deploy your permission set.

            The default is ``/`` . For more information, see `Friendly names and paths <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-friendly-names>`_ in the *IAM User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-permissionset-customermanagedpolicyreference.html#cfn-sso-permissionset-customermanagedpolicyreference-path
            '''
            result = self._values.get("path")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomerManagedPolicyReferenceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sso.CfnPermissionSet.PermissionsBoundaryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "customer_managed_policy_reference": "customerManagedPolicyReference",
            "managed_policy_arn": "managedPolicyArn",
        },
    )
    class PermissionsBoundaryProperty:
        def __init__(
            self,
            *,
            customer_managed_policy_reference: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnPermissionSet.CustomerManagedPolicyReferenceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            managed_policy_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the configuration of the AWS managed or customer managed policy that you want to set as a permissions boundary.

            Specify either ``CustomerManagedPolicyReference`` to use the name and path of a customer managed policy, or ``ManagedPolicyArn`` to use the ARN of an AWS managed policy. A permissions boundary represents the maximum permissions that any policy can grant your role. For more information, see `Permissions boundaries for IAM entities <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`_ in the *IAM User Guide* .
            .. epigraph::

               Policies used as permissions boundaries don't provide permissions. You must also attach an IAM policy to the role. To learn how the effective permissions for a role are evaluated, see `IAM JSON policy evaluation logic <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html>`_ in the *IAM User Guide* .

            :param customer_managed_policy_reference: Specifies the name and path of a customer managed policy. You must have an IAM policy that matches the name and path in each AWS account where you want to deploy your permission set.
            :param managed_policy_arn: The AWS managed policy ARN that you want to attach to a permission set as a permissions boundary.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-permissionset-permissionsboundary.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_sso as sso
                
                permissions_boundary_property = sso.CfnPermissionSet.PermissionsBoundaryProperty(
                    customer_managed_policy_reference=sso.CfnPermissionSet.CustomerManagedPolicyReferenceProperty(
                        name="name",
                
                        # the properties below are optional
                        path="path"
                    ),
                    managed_policy_arn="managedPolicyArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6d5cab04a8b70e19536ec7d554c9fdb29780e290977ce4fa715e9ee7eae31dd9)
                check_type(argname="argument customer_managed_policy_reference", value=customer_managed_policy_reference, expected_type=type_hints["customer_managed_policy_reference"])
                check_type(argname="argument managed_policy_arn", value=managed_policy_arn, expected_type=type_hints["managed_policy_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if customer_managed_policy_reference is not None:
                self._values["customer_managed_policy_reference"] = customer_managed_policy_reference
            if managed_policy_arn is not None:
                self._values["managed_policy_arn"] = managed_policy_arn

        @builtins.property
        def customer_managed_policy_reference(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnPermissionSet.CustomerManagedPolicyReferenceProperty"]]:
            '''Specifies the name and path of a customer managed policy.

            You must have an IAM policy that matches the name and path in each AWS account where you want to deploy your permission set.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-permissionset-permissionsboundary.html#cfn-sso-permissionset-permissionsboundary-customermanagedpolicyreference
            '''
            result = self._values.get("customer_managed_policy_reference")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnPermissionSet.CustomerManagedPolicyReferenceProperty"]], result)

        @builtins.property
        def managed_policy_arn(self) -> typing.Optional[builtins.str]:
            '''The AWS managed policy ARN that you want to attach to a permission set as a permissions boundary.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-permissionset-permissionsboundary.html#cfn-sso-permissionset-permissionsboundary-managedpolicyarn
            '''
            result = self._values.get("managed_policy_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PermissionsBoundaryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sso.CfnPermissionSetProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_arn": "instanceArn",
        "name": "name",
        "customer_managed_policy_references": "customerManagedPolicyReferences",
        "description": "description",
        "inline_policy": "inlinePolicy",
        "managed_policies": "managedPolicies",
        "permissions_boundary": "permissionsBoundary",
        "relay_state_type": "relayStateType",
        "session_duration": "sessionDuration",
        "tags": "tags",
    },
)
class CfnPermissionSetProps:
    def __init__(
        self,
        *,
        instance_arn: builtins.str,
        name: builtins.str,
        customer_managed_policy_references: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnPermissionSet.CustomerManagedPolicyReferenceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        inline_policy: typing.Any = None,
        managed_policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        permissions_boundary: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnPermissionSet.PermissionsBoundaryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        relay_state_type: typing.Optional[builtins.str] = None,
        session_duration: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPermissionSet``.

        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html>`_ in the *AWS General Reference* .
        :param name: The name of the permission set.
        :param customer_managed_policy_references: Specifies the names and paths of the customer managed policies that you have attached to your permission set.
        :param description: The description of the ``PermissionSet`` .
        :param inline_policy: The inline policy that is attached to the permission set. .. epigraph:: For ``Length Constraints`` , if a valid ARN is provided for a permission set, it is possible for an empty inline policy to be returned.
        :param managed_policies: A structure that stores the details of the AWS managed policy.
        :param permissions_boundary: Specifies the configuration of the AWS managed or customer managed policy that you want to set as a permissions boundary. Specify either ``CustomerManagedPolicyReference`` to use the name and path of a customer managed policy, or ``ManagedPolicyArn`` to use the ARN of an AWS managed policy. A permissions boundary represents the maximum permissions that any policy can grant your role. For more information, see `Permissions boundaries for IAM entities <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`_ in the *IAM User Guide* . .. epigraph:: Policies used as permissions boundaries don't provide permissions. You must also attach an IAM policy to the role. To learn how the effective permissions for a role are evaluated, see `IAM JSON policy evaluation logic <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html>`_ in the *IAM User Guide* .
        :param relay_state_type: Used to redirect users within the application during the federation authentication process.
        :param session_duration: The length of time that the application user sessions are valid for in the ISO-8601 standard.
        :param tags: The tags to attach to the new ``PermissionSet`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_sso as sso
            
            # inline_policy: Any
            
            cfn_permission_set_props = sso.CfnPermissionSetProps(
                instance_arn="instanceArn",
                name="name",
            
                # the properties below are optional
                customer_managed_policy_references=[sso.CfnPermissionSet.CustomerManagedPolicyReferenceProperty(
                    name="name",
            
                    # the properties below are optional
                    path="path"
                )],
                description="description",
                inline_policy=inline_policy,
                managed_policies=["managedPolicies"],
                permissions_boundary=sso.CfnPermissionSet.PermissionsBoundaryProperty(
                    customer_managed_policy_reference=sso.CfnPermissionSet.CustomerManagedPolicyReferenceProperty(
                        name="name",
            
                        # the properties below are optional
                        path="path"
                    ),
                    managed_policy_arn="managedPolicyArn"
                ),
                relay_state_type="relayStateType",
                session_duration="sessionDuration",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b28a9062c54fe2c4ea63a0488f1e72717c268189b5edaa29b477b3d1d49f0b6)
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument customer_managed_policy_references", value=customer_managed_policy_references, expected_type=type_hints["customer_managed_policy_references"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument inline_policy", value=inline_policy, expected_type=type_hints["inline_policy"])
            check_type(argname="argument managed_policies", value=managed_policies, expected_type=type_hints["managed_policies"])
            check_type(argname="argument permissions_boundary", value=permissions_boundary, expected_type=type_hints["permissions_boundary"])
            check_type(argname="argument relay_state_type", value=relay_state_type, expected_type=type_hints["relay_state_type"])
            check_type(argname="argument session_duration", value=session_duration, expected_type=type_hints["session_duration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_arn": instance_arn,
            "name": name,
        }
        if customer_managed_policy_references is not None:
            self._values["customer_managed_policy_references"] = customer_managed_policy_references
        if description is not None:
            self._values["description"] = description
        if inline_policy is not None:
            self._values["inline_policy"] = inline_policy
        if managed_policies is not None:
            self._values["managed_policies"] = managed_policies
        if permissions_boundary is not None:
            self._values["permissions_boundary"] = permissions_boundary
        if relay_state_type is not None:
            self._values["relay_state_type"] = relay_state_type
        if session_duration is not None:
            self._values["session_duration"] = session_duration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The ARN of the IAM Identity Center instance under which the operation will be executed.

        For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html>`_ in the *AWS General Reference* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the permission set.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def customer_managed_policy_references(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnPermissionSet.CustomerManagedPolicyReferenceProperty]]]]:
        '''Specifies the names and paths of the customer managed policies that you have attached to your permission set.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-customermanagedpolicyreferences
        '''
        result = self._values.get("customer_managed_policy_references")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnPermissionSet.CustomerManagedPolicyReferenceProperty]]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the ``PermissionSet`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def inline_policy(self) -> typing.Any:
        '''The inline policy that is attached to the permission set.

        .. epigraph::

           For ``Length Constraints`` , if a valid ARN is provided for a permission set, it is possible for an empty inline policy to be returned.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-inlinepolicy
        '''
        result = self._values.get("inline_policy")
        return typing.cast(typing.Any, result)

    @builtins.property
    def managed_policies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A structure that stores the details of the AWS managed policy.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-managedpolicies
        '''
        result = self._values.get("managed_policies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def permissions_boundary(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnPermissionSet.PermissionsBoundaryProperty]]:
        '''Specifies the configuration of the AWS managed or customer managed policy that you want to set as a permissions boundary.

        Specify either ``CustomerManagedPolicyReference`` to use the name and path of a customer managed policy, or ``ManagedPolicyArn`` to use the ARN of an AWS managed policy. A permissions boundary represents the maximum permissions that any policy can grant your role. For more information, see `Permissions boundaries for IAM entities <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`_ in the *IAM User Guide* .
        .. epigraph::

           Policies used as permissions boundaries don't provide permissions. You must also attach an IAM policy to the role. To learn how the effective permissions for a role are evaluated, see `IAM JSON policy evaluation logic <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html>`_ in the *IAM User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-permissionsboundary
        '''
        result = self._values.get("permissions_boundary")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnPermissionSet.PermissionsBoundaryProperty]], result)

    @builtins.property
    def relay_state_type(self) -> typing.Optional[builtins.str]:
        '''Used to redirect users within the application during the federation authentication process.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-relaystatetype
        '''
        result = self._values.get("relay_state_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def session_duration(self) -> typing.Optional[builtins.str]:
        '''The length of time that the application user sessions are valid for in the ISO-8601 standard.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-sessionduration
        '''
        result = self._values.get("session_duration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]]:
        '''The tags to attach to the new ``PermissionSet`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPermissionSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAssignment",
    "CfnAssignmentProps",
    "CfnInstanceAccessControlAttributeConfiguration",
    "CfnInstanceAccessControlAttributeConfigurationProps",
    "CfnPermissionSet",
    "CfnPermissionSetProps",
]

publication.publish()

def _typecheckingstub__9583c2550c355b39916bdb43c9d364b996fab7f826903887b911aab9fe066751(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    instance_arn: builtins.str,
    permission_set_arn: builtins.str,
    principal_id: builtins.str,
    principal_type: builtins.str,
    target_id: builtins.str,
    target_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f518667452efb368ade61d083684ad7f114f296189db531f40176aea58ecec14(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__500d2ae81864550232127f63fda39b595ca35b5ebbdc26aae3cac7f72938f4dd(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d5cdd981dcf4bf948e4b5d57d3ef313f17e7978c210feccb60754b3380636f8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__369d567c64088cd44c984c91075d5826f6ea1f10ded5cc2f08ac967c66dd185b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d78fef8f4b2a48de81e185d0edb82f6c4a7471be00428cd080c4eff958102bc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3ec63d8083f159d4e9f9c662e7070231c3d577932d6444255843a9691837161(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3b7ed7b671faae1d71292c1247c29e35ecb3e149564a196364fd29684a3cc78(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c62b78fc1f690b0fc535ce0b5f90eb5188fae02c9f21522014ea54c33773302(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a0fe0f0e6bbca20ac0efc0ff958d821f21e5d0d4b4fc2a49ca65e624cd45f88(
    *,
    instance_arn: builtins.str,
    permission_set_arn: builtins.str,
    principal_id: builtins.str,
    principal_type: builtins.str,
    target_id: builtins.str,
    target_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86f8072315f2a7fa7058307331311dce99c06c1d2c210fee221e69e37c5b7e79(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    instance_arn: builtins.str,
    access_control_attributes: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[typing.Union[CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25a6cd1fedf8fe6e20ed0ee6a2c25bf567c5226f9e7b33fe0c1c9d6ca3f40292(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__beced262b5a95170e93c29e3a50c2f2fbcd5c5b95cd4a90be60b78083c4fdc01(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccfe8e729fb71bdd9f0239a159f75713a85f77b0470bfe8492c18163bd795711(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4f5b2ec55dc7091ab2bf1343cf84a27f8e708f4e9c1e757e1dd2ba351a2a368(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty, _aws_cdk_core_f4b25747.IResolvable]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d176c0d6109001f5985ec36d4f688b1be5ea2f6adbbebccfa2747f5c66301d11(
    *,
    key: builtins.str,
    value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeValueProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c2d5dbdc9d2d6a9d1a4d6f93e9b67d2b1bae3aa5d796fa7574587be603c7d85(
    *,
    source: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97a5059d3e57502a0b2ab04d980fcca841a3657fd77abe791eb0cb6a3f72dbe9(
    *,
    instance_arn: builtins.str,
    access_control_attributes: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[typing.Union[CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__367b6705f06c7d6f14f3907264e13ee3268282a0b43167d8e2091acfbd3837b5(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    instance_arn: builtins.str,
    name: builtins.str,
    customer_managed_policy_references: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnPermissionSet.CustomerManagedPolicyReferenceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    inline_policy: typing.Any = None,
    managed_policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    permissions_boundary: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnPermissionSet.PermissionsBoundaryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    relay_state_type: typing.Optional[builtins.str] = None,
    session_duration: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3871a5f733bae8e2454777749d347a18a93e701637db3dfb54efbb8176d541f6(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a10a52adcecd17e07c26d1774311a036e56a2efe69455ece053f95e66902d43(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23c013124c5e5747626106f316f80ec05d28c0f2bb42aad0b4c0484ef23e64b0(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e99cefdb623dfeaeca734e1b313fa9ad4c5ba2a597ee1a2c79db923a39ca049(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__366b74787a4ce6ef91dfcdc2dd34d5a6121f6d2d248625a10848c8caf3e78d7b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c34427b6577a11ebe9586a8617e7dad9365d27e6fff1e37697502159f99bbe9(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnPermissionSet.CustomerManagedPolicyReferenceProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__078985bd33bba614ff1cd57df92e6938fc83b6b4b65e16a4a4ed93ff2ac46a60(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e890f2651d96ddbf9135f831069f2d442f58ebd595ff9799441d64fb760e3bb(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8c1049eea884b5607637074fdbe49a5614eb01ff62a8576786864c2d6cdad5c(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnPermissionSet.PermissionsBoundaryProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ace8e8388627a59ce1fac9185c7e2fa8db58b570297ce75b7b2cd1e599e0fec(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1ce65fd9bd737f24bf4ec4f88b675c7c24498189e6f19074551e8ed0d49ea0f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab5012337ba132ecbded8e31a31cd1f327045bf9c2ea2aa6d4e4815a7d58c60f(
    *,
    name: builtins.str,
    path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d5cab04a8b70e19536ec7d554c9fdb29780e290977ce4fa715e9ee7eae31dd9(
    *,
    customer_managed_policy_reference: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnPermissionSet.CustomerManagedPolicyReferenceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    managed_policy_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b28a9062c54fe2c4ea63a0488f1e72717c268189b5edaa29b477b3d1d49f0b6(
    *,
    instance_arn: builtins.str,
    name: builtins.str,
    customer_managed_policy_references: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnPermissionSet.CustomerManagedPolicyReferenceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    inline_policy: typing.Any = None,
    managed_policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    permissions_boundary: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnPermissionSet.PermissionsBoundaryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    relay_state_type: typing.Optional[builtins.str] = None,
    session_duration: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

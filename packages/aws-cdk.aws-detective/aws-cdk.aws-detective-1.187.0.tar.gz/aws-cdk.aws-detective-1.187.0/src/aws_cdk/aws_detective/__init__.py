'''
# AWS::Detective Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_detective as detective
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Detective construct libraries](https://constructs.dev/search?q=detective)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Detective resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Detective.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Detective](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Detective.html).

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
class CfnGraph(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-detective.CfnGraph",
):
    '''A CloudFormation ``AWS::Detective::Graph``.

    The ``AWS::Detective::Graph`` resource is an Amazon Detective resource type that creates a Detective behavior graph. The requesting account becomes the administrator account for the behavior graph.

    :cloudformationResource: AWS::Detective::Graph
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-graph.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_detective as detective
        
        cfn_graph = detective.CfnGraph(self, "MyCfnGraph",
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
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Detective::Graph``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param tags: The tag values to assign to the new behavior graph.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2886b9466b00433e31fa1a7a45c115ef247062e785363131f94b5bb9f09b9000)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGraphProps(tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cb7b43e7492619c5052f56b4f12c5ae5600d42255247af6a5fb5836af2dff23)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2b79cc69cacae00693d3e7aa3fc4aebb78e89e65a933421f32508dd12d18716b)
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
        '''The ARN of the new behavior graph.

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
        '''The tag values to assign to the new behavior graph.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-graph.html#cfn-detective-graph-tags
        '''
        return typing.cast(_aws_cdk_core_f4b25747.TagManager, jsii.get(self, "tags"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-detective.CfnGraphProps",
    jsii_struct_bases=[],
    name_mapping={"tags": "tags"},
)
class CfnGraphProps:
    def __init__(
        self,
        *,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnGraph``.

        :param tags: The tag values to assign to the new behavior graph.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-graph.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_detective as detective
            
            cfn_graph_props = detective.CfnGraphProps(
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1ef959eb0f0cf4b7b3817d48e2a296d287ef70b8ac75fd17b7496b97dc911d2)
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]]:
        '''The tag values to assign to the new behavior graph.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-graph.html#cfn-detective-graph-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGraphProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnMemberInvitation(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-detective.CfnMemberInvitation",
):
    '''A CloudFormation ``AWS::Detective::MemberInvitation``.

    The ``AWS::Detective::MemberInvitation`` resource is an Amazon Detective resource type that creates an invitation to join a Detective behavior graph. The administrator account can choose whether to send an email notification of the invitation to the root user email address of the AWS account.

    :cloudformationResource: AWS::Detective::MemberInvitation
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-memberinvitation.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_detective as detective
        
        cfn_member_invitation = detective.CfnMemberInvitation(self, "MyCfnMemberInvitation",
            graph_arn="graphArn",
            member_email_address="memberEmailAddress",
            member_id="memberId",
        
            # the properties below are optional
            disable_email_notification=False,
            message="message"
        )
    '''

    def __init__(
        self,
        scope: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        graph_arn: builtins.str,
        member_email_address: builtins.str,
        member_id: builtins.str,
        disable_email_notification: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
        message: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Detective::MemberInvitation``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param graph_arn: The ARN of the behavior graph to invite the account to contribute data to.
        :param member_email_address: The root user email address of the invited account. If the email address provided is not the root user email address for the provided account, the invitation creation fails.
        :param member_id: The AWS account identifier of the invited account.
        :param disable_email_notification: Whether to send an invitation email to the member account. If set to true, the member account does not receive an invitation email.
        :param message: Customized text to include in the invitation email message.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f34773afc753f246427e74dd39d52c9744e953488def1e307b7a9b9b8dbbb909)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMemberInvitationProps(
            graph_arn=graph_arn,
            member_email_address=member_email_address,
            member_id=member_id,
            disable_email_notification=disable_email_notification,
            message=message,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0dbadd5ca4cddc83d9ac18fa954ddd5633851a1c319832597703539deb5b41ea)
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
            type_hints = typing.get_type_hints(_typecheckingstub__37b5f9ec8618f85034a299d4307af3eb58f2c7cafb59c95f481fdb04db349ebc)
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
    @jsii.member(jsii_name="graphArn")
    def graph_arn(self) -> builtins.str:
        '''The ARN of the behavior graph to invite the account to contribute data to.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-memberinvitation.html#cfn-detective-memberinvitation-grapharn
        '''
        return typing.cast(builtins.str, jsii.get(self, "graphArn"))

    @graph_arn.setter
    def graph_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__333c0ede7ed917df7f730d8d03120e35914eab6fbe4bc9ca383c750c667c46e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "graphArn", value)

    @builtins.property
    @jsii.member(jsii_name="memberEmailAddress")
    def member_email_address(self) -> builtins.str:
        '''The root user email address of the invited account.

        If the email address provided is not the root user email address for the provided account, the invitation creation fails.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-memberinvitation.html#cfn-detective-memberinvitation-memberemailaddress
        '''
        return typing.cast(builtins.str, jsii.get(self, "memberEmailAddress"))

    @member_email_address.setter
    def member_email_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e85e65a5a0865431771f9b6c60247e7b21cc876ead738a858a70184ebaafbb35)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memberEmailAddress", value)

    @builtins.property
    @jsii.member(jsii_name="memberId")
    def member_id(self) -> builtins.str:
        '''The AWS account identifier of the invited account.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-memberinvitation.html#cfn-detective-memberinvitation-memberid
        '''
        return typing.cast(builtins.str, jsii.get(self, "memberId"))

    @member_id.setter
    def member_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34b733e4d9ef7c57b76e7fb4f6826856cdf5f58ae9712e9a5fe311f5a44e8bbf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memberId", value)

    @builtins.property
    @jsii.member(jsii_name="disableEmailNotification")
    def disable_email_notification(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
        '''Whether to send an invitation email to the member account.

        If set to true, the member account does not receive an invitation email.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-memberinvitation.html#cfn-detective-memberinvitation-disableemailnotification
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], jsii.get(self, "disableEmailNotification"))

    @disable_email_notification.setter
    def disable_email_notification(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa99d9da780a21f1727bc136a4e8098094788066873e8aa0d0ce38ea9752a3fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableEmailNotification", value)

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> typing.Optional[builtins.str]:
        '''Customized text to include in the invitation email message.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-memberinvitation.html#cfn-detective-memberinvitation-message
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "message"))

    @message.setter
    def message(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f72382561788c79b114abbbca21e1fc4a6fa4b81910c9d03de3f0d992f8030f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "message", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-detective.CfnMemberInvitationProps",
    jsii_struct_bases=[],
    name_mapping={
        "graph_arn": "graphArn",
        "member_email_address": "memberEmailAddress",
        "member_id": "memberId",
        "disable_email_notification": "disableEmailNotification",
        "message": "message",
    },
)
class CfnMemberInvitationProps:
    def __init__(
        self,
        *,
        graph_arn: builtins.str,
        member_email_address: builtins.str,
        member_id: builtins.str,
        disable_email_notification: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
        message: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnMemberInvitation``.

        :param graph_arn: The ARN of the behavior graph to invite the account to contribute data to.
        :param member_email_address: The root user email address of the invited account. If the email address provided is not the root user email address for the provided account, the invitation creation fails.
        :param member_id: The AWS account identifier of the invited account.
        :param disable_email_notification: Whether to send an invitation email to the member account. If set to true, the member account does not receive an invitation email.
        :param message: Customized text to include in the invitation email message.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-memberinvitation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_detective as detective
            
            cfn_member_invitation_props = detective.CfnMemberInvitationProps(
                graph_arn="graphArn",
                member_email_address="memberEmailAddress",
                member_id="memberId",
            
                # the properties below are optional
                disable_email_notification=False,
                message="message"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46b098540a12971802d998b153c6b3cf538da9c9c7b104989d1a2866a9fc7eae)
            check_type(argname="argument graph_arn", value=graph_arn, expected_type=type_hints["graph_arn"])
            check_type(argname="argument member_email_address", value=member_email_address, expected_type=type_hints["member_email_address"])
            check_type(argname="argument member_id", value=member_id, expected_type=type_hints["member_id"])
            check_type(argname="argument disable_email_notification", value=disable_email_notification, expected_type=type_hints["disable_email_notification"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "graph_arn": graph_arn,
            "member_email_address": member_email_address,
            "member_id": member_id,
        }
        if disable_email_notification is not None:
            self._values["disable_email_notification"] = disable_email_notification
        if message is not None:
            self._values["message"] = message

    @builtins.property
    def graph_arn(self) -> builtins.str:
        '''The ARN of the behavior graph to invite the account to contribute data to.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-memberinvitation.html#cfn-detective-memberinvitation-grapharn
        '''
        result = self._values.get("graph_arn")
        assert result is not None, "Required property 'graph_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def member_email_address(self) -> builtins.str:
        '''The root user email address of the invited account.

        If the email address provided is not the root user email address for the provided account, the invitation creation fails.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-memberinvitation.html#cfn-detective-memberinvitation-memberemailaddress
        '''
        result = self._values.get("member_email_address")
        assert result is not None, "Required property 'member_email_address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def member_id(self) -> builtins.str:
        '''The AWS account identifier of the invited account.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-memberinvitation.html#cfn-detective-memberinvitation-memberid
        '''
        result = self._values.get("member_id")
        assert result is not None, "Required property 'member_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disable_email_notification(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
        '''Whether to send an invitation email to the member account.

        If set to true, the member account does not receive an invitation email.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-memberinvitation.html#cfn-detective-memberinvitation-disableemailnotification
        '''
        result = self._values.get("disable_email_notification")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

    @builtins.property
    def message(self) -> typing.Optional[builtins.str]:
        '''Customized text to include in the invitation email message.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-detective-memberinvitation.html#cfn-detective-memberinvitation-message
        '''
        result = self._values.get("message")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMemberInvitationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnGraph",
    "CfnGraphProps",
    "CfnMemberInvitation",
    "CfnMemberInvitationProps",
]

publication.publish()

def _typecheckingstub__2886b9466b00433e31fa1a7a45c115ef247062e785363131f94b5bb9f09b9000(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cb7b43e7492619c5052f56b4f12c5ae5600d42255247af6a5fb5836af2dff23(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b79cc69cacae00693d3e7aa3fc4aebb78e89e65a933421f32508dd12d18716b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1ef959eb0f0cf4b7b3817d48e2a296d287ef70b8ac75fd17b7496b97dc911d2(
    *,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f34773afc753f246427e74dd39d52c9744e953488def1e307b7a9b9b8dbbb909(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    graph_arn: builtins.str,
    member_email_address: builtins.str,
    member_id: builtins.str,
    disable_email_notification: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    message: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0dbadd5ca4cddc83d9ac18fa954ddd5633851a1c319832597703539deb5b41ea(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37b5f9ec8618f85034a299d4307af3eb58f2c7cafb59c95f481fdb04db349ebc(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__333c0ede7ed917df7f730d8d03120e35914eab6fbe4bc9ca383c750c667c46e3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e85e65a5a0865431771f9b6c60247e7b21cc876ead738a858a70184ebaafbb35(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34b733e4d9ef7c57b76e7fb4f6826856cdf5f58ae9712e9a5fe311f5a44e8bbf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa99d9da780a21f1727bc136a4e8098094788066873e8aa0d0ce38ea9752a3fd(
    value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f72382561788c79b114abbbca21e1fc4a6fa4b81910c9d03de3f0d992f8030f2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46b098540a12971802d998b153c6b3cf538da9c9c7b104989d1a2866a9fc7eae(
    *,
    graph_arn: builtins.str,
    member_email_address: builtins.str,
    member_id: builtins.str,
    disable_email_notification: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    message: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

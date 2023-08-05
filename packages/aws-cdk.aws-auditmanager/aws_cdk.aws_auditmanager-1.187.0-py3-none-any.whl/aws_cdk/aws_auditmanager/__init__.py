'''
# AWS::AuditManager Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_auditmanager as auditmanager
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for AuditManager construct libraries](https://constructs.dev/search?q=auditmanager)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::AuditManager resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AuditManager.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::AuditManager](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AuditManager.html).

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
class CfnAssessment(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-auditmanager.CfnAssessment",
):
    '''A CloudFormation ``AWS::AuditManager::Assessment``.

    The ``AWS::AuditManager::Assessment`` resource is an Audit Manager resource type that defines the scope of audit evidence collected by Audit Manager . An Audit Manager assessment is an implementation of an Audit Manager framework.

    :cloudformationResource: AWS::AuditManager::Assessment
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_auditmanager as auditmanager
        
        cfn_assessment = auditmanager.CfnAssessment(self, "MyCfnAssessment",
            assessment_reports_destination=auditmanager.CfnAssessment.AssessmentReportsDestinationProperty(
                destination="destination",
                destination_type="destinationType"
            ),
            aws_account=auditmanager.CfnAssessment.AWSAccountProperty(
                email_address="emailAddress",
                id="id",
                name="name"
            ),
            description="description",
            framework_id="frameworkId",
            name="name",
            roles=[auditmanager.CfnAssessment.RoleProperty(
                role_arn="roleArn",
                role_type="roleType"
            )],
            scope=auditmanager.CfnAssessment.ScopeProperty(
                aws_accounts=[auditmanager.CfnAssessment.AWSAccountProperty(
                    email_address="emailAddress",
                    id="id",
                    name="name"
                )],
                aws_services=[auditmanager.CfnAssessment.AWSServiceProperty(
                    service_name="serviceName"
                )]
            ),
            status="status",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope_: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        assessment_reports_destination: typing.Optional[typing.Union[typing.Union["CfnAssessment.AssessmentReportsDestinationProperty", typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable]] = None,
        aws_account: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnAssessment.AWSAccountProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        framework_id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        roles: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnAssessment.RoleProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        scope: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnAssessment.ScopeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::AuditManager::Assessment``.

        :param scope_: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param assessment_reports_destination: The destination that evidence reports are stored in for the assessment.
        :param aws_account: The AWS account that's associated with the assessment.
        :param description: The description of the assessment.
        :param framework_id: The unique identifier for the framework.
        :param name: The name of the assessment.
        :param roles: The roles that are associated with the assessment.
        :param scope: The wrapper of AWS accounts and services that are in scope for the assessment.
        :param status: The overall status of the assessment. When you create a new assessment, the initial ``Status`` value is always ``ACTIVE`` . When you create an assessment, even if you specify the value as ``INACTIVE`` , the value overrides to ``ACTIVE`` . After you create an assessment, you can change the value of the ``Status`` property at any time. For example, when you want to stop collecting evidence for your assessment, you can change the assessment status to ``INACTIVE`` .
        :param tags: The tags that are associated with the assessment.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cbec5f94cb27af7d767480475f02eea2214c9cf8a1a106e604c0cd5a64e22d0)
            check_type(argname="argument scope_", value=scope_, expected_type=type_hints["scope_"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAssessmentProps(
            assessment_reports_destination=assessment_reports_destination,
            aws_account=aws_account,
            description=description,
            framework_id=framework_id,
            name=name,
            roles=roles,
            scope=scope,
            status=status,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope_, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c01fc692d7642b8bd4eb77f0c1fe13cda389aeb5397fad8d96f6e3aa0367a76b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d9f50096a2d62cdcc76a206593f520d7eb602970764a1af453b226f383c37a0e)
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
        '''The Amazon Resource Name (ARN) of the assessment.

        For example, ``arn:aws:auditmanager:us-east-1:123456789012:assessment/111A1A1A-22B2-33C3-DDD4-55E5E5E555E5`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAssessmentId")
    def attr_assessment_id(self) -> builtins.str:
        '''The unique identifier for the assessment.

        For example, ``111A1A1A-22B2-33C3-DDD4-55E5E5E555E5`` .

        :cloudformationAttribute: AssessmentId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssessmentId"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> _aws_cdk_core_f4b25747.IResolvable:
        '''The time when the assessment was created.

        For example, ``1607582033.373`` .

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(_aws_cdk_core_f4b25747.IResolvable, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrDelegations")
    def attr_delegations(self) -> _aws_cdk_core_f4b25747.IResolvable:
        '''The delegations that are associated with the assessment.

        :cloudformationAttribute: Delegations
        '''
        return typing.cast(_aws_cdk_core_f4b25747.IResolvable, jsii.get(self, "attrDelegations"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _aws_cdk_core_f4b25747.TagManager:
        '''The tags that are associated with the assessment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html#cfn-auditmanager-assessment-tags
        '''
        return typing.cast(_aws_cdk_core_f4b25747.TagManager, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="assessmentReportsDestination")
    def assessment_reports_destination(
        self,
    ) -> typing.Optional[typing.Union["CfnAssessment.AssessmentReportsDestinationProperty", _aws_cdk_core_f4b25747.IResolvable]]:
        '''The destination that evidence reports are stored in for the assessment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html#cfn-auditmanager-assessment-assessmentreportsdestination
        '''
        return typing.cast(typing.Optional[typing.Union["CfnAssessment.AssessmentReportsDestinationProperty", _aws_cdk_core_f4b25747.IResolvable]], jsii.get(self, "assessmentReportsDestination"))

    @assessment_reports_destination.setter
    def assessment_reports_destination(
        self,
        value: typing.Optional[typing.Union["CfnAssessment.AssessmentReportsDestinationProperty", _aws_cdk_core_f4b25747.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0783353de4276fdd03e3c1415ad7119c8b39a645366b6e9d5472ce5506bf49b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assessmentReportsDestination", value)

    @builtins.property
    @jsii.member(jsii_name="awsAccount")
    def aws_account(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnAssessment.AWSAccountProperty"]]:
        '''The AWS account that's associated with the assessment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html#cfn-auditmanager-assessment-awsaccount
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnAssessment.AWSAccountProperty"]], jsii.get(self, "awsAccount"))

    @aws_account.setter
    def aws_account(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnAssessment.AWSAccountProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d6f8e81b80c4e1429dd46110f922c3fb414e5bf048f4b9f119f76e64feeb99c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsAccount", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the assessment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html#cfn-auditmanager-assessment-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7acb8d17f86a181ea1c7517be2fec0f2cc69d3621df802ab1808ada7d3191f6b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="frameworkId")
    def framework_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier for the framework.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html#cfn-auditmanager-assessment-frameworkid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "frameworkId"))

    @framework_id.setter
    def framework_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46b572a7917710345cc31c0d4ac779c8590b30bdba64ac173f9fa070b9d24727)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frameworkId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the assessment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html#cfn-auditmanager-assessment-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1510d2ac32f1d88d24da0b5b8d531b15c676a1ac6d9f0c3526772d4e285b2cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="roles")
    def roles(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnAssessment.RoleProperty"]]]]:
        '''The roles that are associated with the assessment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html#cfn-auditmanager-assessment-roles
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnAssessment.RoleProperty"]]]], jsii.get(self, "roles"))

    @roles.setter
    def roles(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnAssessment.RoleProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d32ae91a19f76c79ea9da11468f52f2e1ff205e1140816ce79450790aeadf67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roles", value)

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnAssessment.ScopeProperty"]]:
        '''The wrapper of AWS accounts and services that are in scope for the assessment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html#cfn-auditmanager-assessment-scope
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnAssessment.ScopeProperty"]], jsii.get(self, "scope"))

    @scope.setter
    def scope(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnAssessment.ScopeProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf246d80a0a0799715fd5ccffcd5f8ac7ecac9cd3a4515933f3a98fc0435b5b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scope", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''The overall status of the assessment.

        When you create a new assessment, the initial ``Status`` value is always ``ACTIVE`` . When you create an assessment, even if you specify the value as ``INACTIVE`` , the value overrides to ``ACTIVE`` .

        After you create an assessment, you can change the value of the ``Status`` property at any time. For example, when you want to stop collecting evidence for your assessment, you can change the assessment status to ``INACTIVE`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html#cfn-auditmanager-assessment-status
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2f2d0f7dac5551e470c4702b32c04965a2e8737a193a25a6a7268612874c2cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-auditmanager.CfnAssessment.AWSAccountProperty",
        jsii_struct_bases=[],
        name_mapping={"email_address": "emailAddress", "id": "id", "name": "name"},
    )
    class AWSAccountProperty:
        def __init__(
            self,
            *,
            email_address: typing.Optional[builtins.str] = None,
            id: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``AWSAccount`` property type specifies the wrapper of the AWS account details, such as account ID, email address, and so on.

            :param email_address: The email address that's associated with the AWS account .
            :param id: The identifier for the AWS account .
            :param name: The name of the AWS account .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-awsaccount.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_auditmanager as auditmanager
                
                a_wSAccount_property = auditmanager.CfnAssessment.AWSAccountProperty(
                    email_address="emailAddress",
                    id="id",
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d9aed61a5f374bce8f12c197f14929f0bf94be8ba4eac2122d145f42c542c6ed)
                check_type(argname="argument email_address", value=email_address, expected_type=type_hints["email_address"])
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if email_address is not None:
                self._values["email_address"] = email_address
            if id is not None:
                self._values["id"] = id
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def email_address(self) -> typing.Optional[builtins.str]:
            '''The email address that's associated with the AWS account .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-awsaccount.html#cfn-auditmanager-assessment-awsaccount-emailaddress
            '''
            result = self._values.get("email_address")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def id(self) -> typing.Optional[builtins.str]:
            '''The identifier for the AWS account .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-awsaccount.html#cfn-auditmanager-assessment-awsaccount-id
            '''
            result = self._values.get("id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the AWS account .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-awsaccount.html#cfn-auditmanager-assessment-awsaccount-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AWSAccountProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-auditmanager.CfnAssessment.AWSServiceProperty",
        jsii_struct_bases=[],
        name_mapping={"service_name": "serviceName"},
    )
    class AWSServiceProperty:
        def __init__(
            self,
            *,
            service_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``AWSService`` property type specifies an AWS service such as Amazon S3 , AWS CloudTrail , and so on.

            :param service_name: The name of the AWS service .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-awsservice.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_auditmanager as auditmanager
                
                a_wSService_property = auditmanager.CfnAssessment.AWSServiceProperty(
                    service_name="serviceName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4617b7e4c7d3c348c57843b408a5495a7323c72a5b3f7b464e44f6de1bd9f266)
                check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if service_name is not None:
                self._values["service_name"] = service_name

        @builtins.property
        def service_name(self) -> typing.Optional[builtins.str]:
            '''The name of the AWS service .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-awsservice.html#cfn-auditmanager-assessment-awsservice-servicename
            '''
            result = self._values.get("service_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AWSServiceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-auditmanager.CfnAssessment.AssessmentReportsDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination": "destination",
            "destination_type": "destinationType",
        },
    )
    class AssessmentReportsDestinationProperty:
        def __init__(
            self,
            *,
            destination: typing.Optional[builtins.str] = None,
            destination_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``AssessmentReportsDestination`` property type specifies the location in which AWS Audit Manager saves assessment reports for the given assessment.

            :param destination: The destination of the assessment report.
            :param destination_type: The destination type, such as Amazon S3.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-assessmentreportsdestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_auditmanager as auditmanager
                
                assessment_reports_destination_property = auditmanager.CfnAssessment.AssessmentReportsDestinationProperty(
                    destination="destination",
                    destination_type="destinationType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a69274af50f32f481ca8d85c2c0701c6320eb63e460dcf0d204562de662ed51c)
                check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
                check_type(argname="argument destination_type", value=destination_type, expected_type=type_hints["destination_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if destination is not None:
                self._values["destination"] = destination
            if destination_type is not None:
                self._values["destination_type"] = destination_type

        @builtins.property
        def destination(self) -> typing.Optional[builtins.str]:
            '''The destination of the assessment report.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-assessmentreportsdestination.html#cfn-auditmanager-assessment-assessmentreportsdestination-destination
            '''
            result = self._values.get("destination")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def destination_type(self) -> typing.Optional[builtins.str]:
            '''The destination type, such as Amazon S3.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-assessmentreportsdestination.html#cfn-auditmanager-assessment-assessmentreportsdestination-destinationtype
            '''
            result = self._values.get("destination_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AssessmentReportsDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-auditmanager.CfnAssessment.DelegationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "assessment_id": "assessmentId",
            "assessment_name": "assessmentName",
            "comment": "comment",
            "control_set_id": "controlSetId",
            "created_by": "createdBy",
            "creation_time": "creationTime",
            "id": "id",
            "last_updated": "lastUpdated",
            "role_arn": "roleArn",
            "role_type": "roleType",
            "status": "status",
        },
    )
    class DelegationProperty:
        def __init__(
            self,
            *,
            assessment_id: typing.Optional[builtins.str] = None,
            assessment_name: typing.Optional[builtins.str] = None,
            comment: typing.Optional[builtins.str] = None,
            control_set_id: typing.Optional[builtins.str] = None,
            created_by: typing.Optional[builtins.str] = None,
            creation_time: typing.Optional[jsii.Number] = None,
            id: typing.Optional[builtins.str] = None,
            last_updated: typing.Optional[jsii.Number] = None,
            role_arn: typing.Optional[builtins.str] = None,
            role_type: typing.Optional[builtins.str] = None,
            status: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``Delegation`` property type specifies the assignment of a control set to a delegate for review.

            :param assessment_id: The identifier for the assessment that's associated with the delegation.
            :param assessment_name: The name of the assessment that's associated with the delegation.
            :param comment: The comment that's related to the delegation.
            :param control_set_id: The identifier for the control set that's associated with the delegation.
            :param created_by: The IAM user or role that created the delegation. *Minimum* : ``1`` *Maximum* : ``100`` *Pattern* : ``^[a-zA-Z0-9-_()\\\\[\\\\]\\\\s]+$``
            :param creation_time: Specifies when the delegation was created.
            :param id: The unique identifier for the delegation.
            :param last_updated: Specifies when the delegation was last updated.
            :param role_arn: The Amazon Resource Name (ARN) of the IAM role.
            :param role_type: The type of customer persona. .. epigraph:: In ``CreateAssessment`` , ``roleType`` can only be ``PROCESS_OWNER`` . In ``UpdateSettings`` , ``roleType`` can only be ``PROCESS_OWNER`` . In ``BatchCreateDelegationByAssessment`` , ``roleType`` can only be ``RESOURCE_OWNER`` .
            :param status: The status of the delegation.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-delegation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_auditmanager as auditmanager
                
                delegation_property = auditmanager.CfnAssessment.DelegationProperty(
                    assessment_id="assessmentId",
                    assessment_name="assessmentName",
                    comment="comment",
                    control_set_id="controlSetId",
                    created_by="createdBy",
                    creation_time=123,
                    id="id",
                    last_updated=123,
                    role_arn="roleArn",
                    role_type="roleType",
                    status="status"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dfade4609059e73a348a1df3e438ab29f804d77f6164cd45f937b2c79b77b095)
                check_type(argname="argument assessment_id", value=assessment_id, expected_type=type_hints["assessment_id"])
                check_type(argname="argument assessment_name", value=assessment_name, expected_type=type_hints["assessment_name"])
                check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
                check_type(argname="argument control_set_id", value=control_set_id, expected_type=type_hints["control_set_id"])
                check_type(argname="argument created_by", value=created_by, expected_type=type_hints["created_by"])
                check_type(argname="argument creation_time", value=creation_time, expected_type=type_hints["creation_time"])
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument last_updated", value=last_updated, expected_type=type_hints["last_updated"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument role_type", value=role_type, expected_type=type_hints["role_type"])
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if assessment_id is not None:
                self._values["assessment_id"] = assessment_id
            if assessment_name is not None:
                self._values["assessment_name"] = assessment_name
            if comment is not None:
                self._values["comment"] = comment
            if control_set_id is not None:
                self._values["control_set_id"] = control_set_id
            if created_by is not None:
                self._values["created_by"] = created_by
            if creation_time is not None:
                self._values["creation_time"] = creation_time
            if id is not None:
                self._values["id"] = id
            if last_updated is not None:
                self._values["last_updated"] = last_updated
            if role_arn is not None:
                self._values["role_arn"] = role_arn
            if role_type is not None:
                self._values["role_type"] = role_type
            if status is not None:
                self._values["status"] = status

        @builtins.property
        def assessment_id(self) -> typing.Optional[builtins.str]:
            '''The identifier for the assessment that's associated with the delegation.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-delegation.html#cfn-auditmanager-assessment-delegation-assessmentid
            '''
            result = self._values.get("assessment_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def assessment_name(self) -> typing.Optional[builtins.str]:
            '''The name of the assessment that's associated with the delegation.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-delegation.html#cfn-auditmanager-assessment-delegation-assessmentname
            '''
            result = self._values.get("assessment_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def comment(self) -> typing.Optional[builtins.str]:
            '''The comment that's related to the delegation.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-delegation.html#cfn-auditmanager-assessment-delegation-comment
            '''
            result = self._values.get("comment")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def control_set_id(self) -> typing.Optional[builtins.str]:
            '''The identifier for the control set that's associated with the delegation.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-delegation.html#cfn-auditmanager-assessment-delegation-controlsetid
            '''
            result = self._values.get("control_set_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def created_by(self) -> typing.Optional[builtins.str]:
            '''The IAM user or role that created the delegation.

            *Minimum* : ``1``

            *Maximum* : ``100``

            *Pattern* : ``^[a-zA-Z0-9-_()\\\\[\\\\]\\\\s]+$``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-delegation.html#cfn-auditmanager-assessment-delegation-createdby
            '''
            result = self._values.get("created_by")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def creation_time(self) -> typing.Optional[jsii.Number]:
            '''Specifies when the delegation was created.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-delegation.html#cfn-auditmanager-assessment-delegation-creationtime
            '''
            result = self._values.get("creation_time")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def id(self) -> typing.Optional[builtins.str]:
            '''The unique identifier for the delegation.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-delegation.html#cfn-auditmanager-assessment-delegation-id
            '''
            result = self._values.get("id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def last_updated(self) -> typing.Optional[jsii.Number]:
            '''Specifies when the delegation was last updated.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-delegation.html#cfn-auditmanager-assessment-delegation-lastupdated
            '''
            result = self._values.get("last_updated")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def role_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the IAM role.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-delegation.html#cfn-auditmanager-assessment-delegation-rolearn
            '''
            result = self._values.get("role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def role_type(self) -> typing.Optional[builtins.str]:
            '''The type of customer persona.

            .. epigraph::

               In ``CreateAssessment`` , ``roleType`` can only be ``PROCESS_OWNER`` .

               In ``UpdateSettings`` , ``roleType`` can only be ``PROCESS_OWNER`` .

               In ``BatchCreateDelegationByAssessment`` , ``roleType`` can only be ``RESOURCE_OWNER`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-delegation.html#cfn-auditmanager-assessment-delegation-roletype
            '''
            result = self._values.get("role_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            '''The status of the delegation.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-delegation.html#cfn-auditmanager-assessment-delegation-status
            '''
            result = self._values.get("status")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DelegationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-auditmanager.CfnAssessment.RoleProperty",
        jsii_struct_bases=[],
        name_mapping={"role_arn": "roleArn", "role_type": "roleType"},
    )
    class RoleProperty:
        def __init__(
            self,
            *,
            role_arn: typing.Optional[builtins.str] = None,
            role_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``Role`` property type specifies the wrapper that contains AWS Audit Manager role information, such as the role type and IAM Amazon Resource Name (ARN).

            :param role_arn: The Amazon Resource Name (ARN) of the IAM role.
            :param role_type: The type of customer persona. .. epigraph:: In ``CreateAssessment`` , ``roleType`` can only be ``PROCESS_OWNER`` . In ``UpdateSettings`` , ``roleType`` can only be ``PROCESS_OWNER`` . In ``BatchCreateDelegationByAssessment`` , ``roleType`` can only be ``RESOURCE_OWNER`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-role.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_auditmanager as auditmanager
                
                role_property = auditmanager.CfnAssessment.RoleProperty(
                    role_arn="roleArn",
                    role_type="roleType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ee778eb6e25ad346c9f2a61e5946a178e5812d70bf2d26241a50ae02dbafa43f)
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument role_type", value=role_type, expected_type=type_hints["role_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if role_arn is not None:
                self._values["role_arn"] = role_arn
            if role_type is not None:
                self._values["role_type"] = role_type

        @builtins.property
        def role_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the IAM role.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-role.html#cfn-auditmanager-assessment-role-rolearn
            '''
            result = self._values.get("role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def role_type(self) -> typing.Optional[builtins.str]:
            '''The type of customer persona.

            .. epigraph::

               In ``CreateAssessment`` , ``roleType`` can only be ``PROCESS_OWNER`` .

               In ``UpdateSettings`` , ``roleType`` can only be ``PROCESS_OWNER`` .

               In ``BatchCreateDelegationByAssessment`` , ``roleType`` can only be ``RESOURCE_OWNER`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-role.html#cfn-auditmanager-assessment-role-roletype
            '''
            result = self._values.get("role_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RoleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-auditmanager.CfnAssessment.ScopeProperty",
        jsii_struct_bases=[],
        name_mapping={"aws_accounts": "awsAccounts", "aws_services": "awsServices"},
    )
    class ScopeProperty:
        def __init__(
            self,
            *,
            aws_accounts: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnAssessment.AWSAccountProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            aws_services: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnAssessment.AWSServiceProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The ``Scope`` property type specifies the wrapper that contains the AWS accounts and services that are in scope for the assessment.

            :param aws_accounts: The AWS accounts that are included in the scope of the assessment.
            :param aws_services: The AWS services that are included in the scope of the assessment.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-scope.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_auditmanager as auditmanager
                
                scope_property = auditmanager.CfnAssessment.ScopeProperty(
                    aws_accounts=[auditmanager.CfnAssessment.AWSAccountProperty(
                        email_address="emailAddress",
                        id="id",
                        name="name"
                    )],
                    aws_services=[auditmanager.CfnAssessment.AWSServiceProperty(
                        service_name="serviceName"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e4b546ead3aac459b6d04e263fc6839004e005941d77c6ad18d7632dbcca39b0)
                check_type(argname="argument aws_accounts", value=aws_accounts, expected_type=type_hints["aws_accounts"])
                check_type(argname="argument aws_services", value=aws_services, expected_type=type_hints["aws_services"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if aws_accounts is not None:
                self._values["aws_accounts"] = aws_accounts
            if aws_services is not None:
                self._values["aws_services"] = aws_services

        @builtins.property
        def aws_accounts(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnAssessment.AWSAccountProperty"]]]]:
            '''The AWS accounts that are included in the scope of the assessment.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-scope.html#cfn-auditmanager-assessment-scope-awsaccounts
            '''
            result = self._values.get("aws_accounts")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnAssessment.AWSAccountProperty"]]]], result)

        @builtins.property
        def aws_services(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnAssessment.AWSServiceProperty"]]]]:
            '''The AWS services that are included in the scope of the assessment.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-auditmanager-assessment-scope.html#cfn-auditmanager-assessment-scope-awsservices
            '''
            result = self._values.get("aws_services")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnAssessment.AWSServiceProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScopeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-auditmanager.CfnAssessmentProps",
    jsii_struct_bases=[],
    name_mapping={
        "assessment_reports_destination": "assessmentReportsDestination",
        "aws_account": "awsAccount",
        "description": "description",
        "framework_id": "frameworkId",
        "name": "name",
        "roles": "roles",
        "scope": "scope",
        "status": "status",
        "tags": "tags",
    },
)
class CfnAssessmentProps:
    def __init__(
        self,
        *,
        assessment_reports_destination: typing.Optional[typing.Union[typing.Union[CfnAssessment.AssessmentReportsDestinationProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable]] = None,
        aws_account: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnAssessment.AWSAccountProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        framework_id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        roles: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnAssessment.RoleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        scope: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnAssessment.ScopeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAssessment``.

        :param assessment_reports_destination: The destination that evidence reports are stored in for the assessment.
        :param aws_account: The AWS account that's associated with the assessment.
        :param description: The description of the assessment.
        :param framework_id: The unique identifier for the framework.
        :param name: The name of the assessment.
        :param roles: The roles that are associated with the assessment.
        :param scope: The wrapper of AWS accounts and services that are in scope for the assessment.
        :param status: The overall status of the assessment. When you create a new assessment, the initial ``Status`` value is always ``ACTIVE`` . When you create an assessment, even if you specify the value as ``INACTIVE`` , the value overrides to ``ACTIVE`` . After you create an assessment, you can change the value of the ``Status`` property at any time. For example, when you want to stop collecting evidence for your assessment, you can change the assessment status to ``INACTIVE`` .
        :param tags: The tags that are associated with the assessment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_auditmanager as auditmanager
            
            cfn_assessment_props = auditmanager.CfnAssessmentProps(
                assessment_reports_destination=auditmanager.CfnAssessment.AssessmentReportsDestinationProperty(
                    destination="destination",
                    destination_type="destinationType"
                ),
                aws_account=auditmanager.CfnAssessment.AWSAccountProperty(
                    email_address="emailAddress",
                    id="id",
                    name="name"
                ),
                description="description",
                framework_id="frameworkId",
                name="name",
                roles=[auditmanager.CfnAssessment.RoleProperty(
                    role_arn="roleArn",
                    role_type="roleType"
                )],
                scope=auditmanager.CfnAssessment.ScopeProperty(
                    aws_accounts=[auditmanager.CfnAssessment.AWSAccountProperty(
                        email_address="emailAddress",
                        id="id",
                        name="name"
                    )],
                    aws_services=[auditmanager.CfnAssessment.AWSServiceProperty(
                        service_name="serviceName"
                    )]
                ),
                status="status",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__329c7e2f1cf73cccdedc3263e67b9ccda6e0059d58c8433d23efa340bd99e637)
            check_type(argname="argument assessment_reports_destination", value=assessment_reports_destination, expected_type=type_hints["assessment_reports_destination"])
            check_type(argname="argument aws_account", value=aws_account, expected_type=type_hints["aws_account"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument framework_id", value=framework_id, expected_type=type_hints["framework_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument roles", value=roles, expected_type=type_hints["roles"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if assessment_reports_destination is not None:
            self._values["assessment_reports_destination"] = assessment_reports_destination
        if aws_account is not None:
            self._values["aws_account"] = aws_account
        if description is not None:
            self._values["description"] = description
        if framework_id is not None:
            self._values["framework_id"] = framework_id
        if name is not None:
            self._values["name"] = name
        if roles is not None:
            self._values["roles"] = roles
        if scope is not None:
            self._values["scope"] = scope
        if status is not None:
            self._values["status"] = status
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def assessment_reports_destination(
        self,
    ) -> typing.Optional[typing.Union[CfnAssessment.AssessmentReportsDestinationProperty, _aws_cdk_core_f4b25747.IResolvable]]:
        '''The destination that evidence reports are stored in for the assessment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html#cfn-auditmanager-assessment-assessmentreportsdestination
        '''
        result = self._values.get("assessment_reports_destination")
        return typing.cast(typing.Optional[typing.Union[CfnAssessment.AssessmentReportsDestinationProperty, _aws_cdk_core_f4b25747.IResolvable]], result)

    @builtins.property
    def aws_account(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnAssessment.AWSAccountProperty]]:
        '''The AWS account that's associated with the assessment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html#cfn-auditmanager-assessment-awsaccount
        '''
        result = self._values.get("aws_account")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnAssessment.AWSAccountProperty]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the assessment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html#cfn-auditmanager-assessment-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def framework_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier for the framework.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html#cfn-auditmanager-assessment-frameworkid
        '''
        result = self._values.get("framework_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the assessment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html#cfn-auditmanager-assessment-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def roles(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnAssessment.RoleProperty]]]]:
        '''The roles that are associated with the assessment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html#cfn-auditmanager-assessment-roles
        '''
        result = self._values.get("roles")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnAssessment.RoleProperty]]]], result)

    @builtins.property
    def scope(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnAssessment.ScopeProperty]]:
        '''The wrapper of AWS accounts and services that are in scope for the assessment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html#cfn-auditmanager-assessment-scope
        '''
        result = self._values.get("scope")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnAssessment.ScopeProperty]], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''The overall status of the assessment.

        When you create a new assessment, the initial ``Status`` value is always ``ACTIVE`` . When you create an assessment, even if you specify the value as ``INACTIVE`` , the value overrides to ``ACTIVE`` .

        After you create an assessment, you can change the value of the ``Status`` property at any time. For example, when you want to stop collecting evidence for your assessment, you can change the assessment status to ``INACTIVE`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html#cfn-auditmanager-assessment-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]]:
        '''The tags that are associated with the assessment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-auditmanager-assessment.html#cfn-auditmanager-assessment-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAssessmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAssessment",
    "CfnAssessmentProps",
]

publication.publish()

def _typecheckingstub__2cbec5f94cb27af7d767480475f02eea2214c9cf8a1a106e604c0cd5a64e22d0(
    scope_: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    assessment_reports_destination: typing.Optional[typing.Union[typing.Union[CfnAssessment.AssessmentReportsDestinationProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable]] = None,
    aws_account: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnAssessment.AWSAccountProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    framework_id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    roles: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnAssessment.RoleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    scope: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnAssessment.ScopeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    status: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c01fc692d7642b8bd4eb77f0c1fe13cda389aeb5397fad8d96f6e3aa0367a76b(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9f50096a2d62cdcc76a206593f520d7eb602970764a1af453b226f383c37a0e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0783353de4276fdd03e3c1415ad7119c8b39a645366b6e9d5472ce5506bf49b(
    value: typing.Optional[typing.Union[CfnAssessment.AssessmentReportsDestinationProperty, _aws_cdk_core_f4b25747.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d6f8e81b80c4e1429dd46110f922c3fb414e5bf048f4b9f119f76e64feeb99c(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnAssessment.AWSAccountProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7acb8d17f86a181ea1c7517be2fec0f2cc69d3621df802ab1808ada7d3191f6b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46b572a7917710345cc31c0d4ac779c8590b30bdba64ac173f9fa070b9d24727(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1510d2ac32f1d88d24da0b5b8d531b15c676a1ac6d9f0c3526772d4e285b2cf(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d32ae91a19f76c79ea9da11468f52f2e1ff205e1140816ce79450790aeadf67(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnAssessment.RoleProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf246d80a0a0799715fd5ccffcd5f8ac7ecac9cd3a4515933f3a98fc0435b5b0(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnAssessment.ScopeProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2f2d0f7dac5551e470c4702b32c04965a2e8737a193a25a6a7268612874c2cf(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9aed61a5f374bce8f12c197f14929f0bf94be8ba4eac2122d145f42c542c6ed(
    *,
    email_address: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4617b7e4c7d3c348c57843b408a5495a7323c72a5b3f7b464e44f6de1bd9f266(
    *,
    service_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a69274af50f32f481ca8d85c2c0701c6320eb63e460dcf0d204562de662ed51c(
    *,
    destination: typing.Optional[builtins.str] = None,
    destination_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfade4609059e73a348a1df3e438ab29f804d77f6164cd45f937b2c79b77b095(
    *,
    assessment_id: typing.Optional[builtins.str] = None,
    assessment_name: typing.Optional[builtins.str] = None,
    comment: typing.Optional[builtins.str] = None,
    control_set_id: typing.Optional[builtins.str] = None,
    created_by: typing.Optional[builtins.str] = None,
    creation_time: typing.Optional[jsii.Number] = None,
    id: typing.Optional[builtins.str] = None,
    last_updated: typing.Optional[jsii.Number] = None,
    role_arn: typing.Optional[builtins.str] = None,
    role_type: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee778eb6e25ad346c9f2a61e5946a178e5812d70bf2d26241a50ae02dbafa43f(
    *,
    role_arn: typing.Optional[builtins.str] = None,
    role_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4b546ead3aac459b6d04e263fc6839004e005941d77c6ad18d7632dbcca39b0(
    *,
    aws_accounts: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnAssessment.AWSAccountProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    aws_services: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnAssessment.AWSServiceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__329c7e2f1cf73cccdedc3263e67b9ccda6e0059d58c8433d23efa340bd99e637(
    *,
    assessment_reports_destination: typing.Optional[typing.Union[typing.Union[CfnAssessment.AssessmentReportsDestinationProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable]] = None,
    aws_account: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnAssessment.AWSAccountProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    framework_id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    roles: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnAssessment.RoleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    scope: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnAssessment.ScopeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    status: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

'''
# AWS Config Construct Library

<!--BEGIN STABILITY BANNER-->---


Features                                                                               | Stability
---------------------------------------------------------------------------------------|------------
CFN Resources                                                                          | ![Stable](https://img.shields.io/badge/stable-success.svg?style=for-the-badge)
Higher level constructs for Config Rules                                               | ![Stable](https://img.shields.io/badge/stable-success.svg?style=for-the-badge)
Higher level constructs for initial set-up (delivery channel & configuration recorder) | ![Not Implemented](https://img.shields.io/badge/not--implemented-black.svg?style=for-the-badge)

> **CFN Resources:** All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always
> stable and safe to use.

<!-- -->

> **Stable:** Higher level constructs in this module that are marked stable will not undergo any
> breaking changes. They will strictly follow the [Semantic Versioning](https://semver.org/) model.

---
<!--END STABILITY BANNER-->

[AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) provides a detailed view of the configuration of AWS resources in your AWS account.
This includes how the resources are related to one another and how they were configured in the
past so that you can see how the configurations and relationships change over time.

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

## Initial Setup

Before using the constructs provided in this module, you need to set up AWS Config
in the region in which it will be used. This setup includes the one-time creation of the
following resources per region:

* `ConfigurationRecorder`: Configure which resources will be recorded for config changes.
* `DeliveryChannel`: Configure where to store the recorded data.

The following guides provide the steps for getting started with AWS Config:

* [Using the AWS Console](https://docs.aws.amazon.com/config/latest/developerguide/gs-console.html)
* [Using the AWS CLI](https://docs.aws.amazon.com/config/latest/developerguide/gs-cli.html)

## Rules

AWS Config can evaluate the configuration settings of your AWS resources by creating AWS Config rules,
which represent your ideal configuration settings.

See [Evaluating Resources with AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html) to learn more about AWS Config rules.

### AWS Managed Rules

AWS Config provides AWS managed rules, which are predefined, customizable rules that AWS Config
uses to evaluate whether your AWS resources comply with common best practices.

For example, you could create a managed rule that checks whether active access keys are rotated
within the number of days specified.

```python
# https://docs.aws.amazon.com/config/latest/developerguide/access-keys-rotated.html
config.ManagedRule(self, "AccessKeysRotated",
    identifier=config.ManagedRuleIdentifiers.ACCESS_KEYS_ROTATED,
    input_parameters={
        "max_access_key_age": 60
    },

    # default is 24 hours
    maximum_execution_frequency=config.MaximumExecutionFrequency.TWELVE_HOURS
)
```

Identifiers for AWS managed rules are available through static constants in the `ManagedRuleIdentifiers` class.
You can find supported input parameters in the [List of AWS Config Managed Rules](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html).

The following higher level constructs for AWS managed rules are available.

#### Access Key rotation

Checks whether your active access keys are rotated within the number of days specified.

```python
# compliant if access keys have been rotated within the last 90 days
config.AccessKeysRotated(self, "AccessKeyRotated")
```

#### CloudFormation Stack drift detection

Checks whether your CloudFormation stack's actual configuration differs, or has drifted,
from it's expected configuration.

```python
# compliant if stack's status is 'IN_SYNC'
# non-compliant if the stack's drift status is 'DRIFTED'
config.CloudFormationStackDriftDetectionCheck(self, "Drift",
    own_stack_only=True
)
```

#### CloudFormation Stack notifications

Checks whether your CloudFormation stacks are sending event notifications to a SNS topic.

```python
# topics to which CloudFormation stacks may send event notifications
topic1 = sns.Topic(self, "AllowedTopic1")
topic2 = sns.Topic(self, "AllowedTopic2")

# non-compliant if CloudFormation stack does not send notifications to 'topic1' or 'topic2'
config.CloudFormationStackNotificationCheck(self, "NotificationCheck",
    topics=[topic1, topic2]
)
```

### Custom rules

You can develop custom rules and add them to AWS Config. You associate each custom rule with an
AWS Lambda function, which contains the logic that evaluates whether your AWS resources comply
with the rule.

### Triggers

AWS Lambda executes functions in response to events that are published by AWS Services.
The function for a custom Config rule receives an event that is published by AWS Config,
and is responsible for evaluating the compliance of the rule.

Evaluations can be triggered by configuration changes, periodically, or both.
To create a custom rule, define a `CustomRule` and specify the Lambda Function
to run and the trigger types.

```python
# eval_compliance_fn: lambda.Function


config.CustomRule(self, "CustomRule",
    lambda_function=eval_compliance_fn,
    configuration_changes=True,
    periodic=True,

    # default is 24 hours
    maximum_execution_frequency=config.MaximumExecutionFrequency.SIX_HOURS
)
```

When the trigger for a rule occurs, the Lambda function is invoked by publishing an event.
See [example events for AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules_example-events.html)

The AWS documentation has examples of Lambda functions for evaluations that are
[triggered by configuration changes](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules_nodejs-sample.html#event-based-example-rule) and [triggered periodically](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules_nodejs-sample.html#periodic-example-rule)

### Scope

By default rules are triggered by changes to all [resources](https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html#supported-resources).

Use the `RuleScope` APIs (`fromResource()`, `fromResources()` or `fromTag()`) to restrict
the scope of both managed and custom rules:

```python
# eval_compliance_fn: lambda.Function
ssh_rule = config.ManagedRule(self, "SSH",
    identifier=config.ManagedRuleIdentifiers.EC2_SECURITY_GROUPS_INCOMING_SSH_DISABLED,
    rule_scope=config.RuleScope.from_resource(config.ResourceType.EC2_SECURITY_GROUP, "sg-1234567890abcdefgh")
)
custom_rule = config.CustomRule(self, "Lambda",
    lambda_function=eval_compliance_fn,
    configuration_changes=True,
    rule_scope=config.RuleScope.from_resources([config.ResourceType.CLOUDFORMATION_STACK, config.ResourceType.S3_BUCKET])
)

tag_rule = config.CustomRule(self, "CostCenterTagRule",
    lambda_function=eval_compliance_fn,
    configuration_changes=True,
    rule_scope=config.RuleScope.from_tag("Cost Center", "MyApp")
)
```

### Events

You can define Amazon EventBridge event rules which trigger when a compliance check fails
or when a rule is re-evaluated.

Use the `onComplianceChange()` APIs to trigger an EventBridge event when a compliance check
of your AWS Config Rule fails:

```python
# Topic to which compliance notification events will be published
compliance_topic = sns.Topic(self, "ComplianceTopic")

rule = config.CloudFormationStackDriftDetectionCheck(self, "Drift")
rule.on_compliance_change("TopicEvent",
    target=targets.SnsTopic(compliance_topic)
)
```

Use the `onReEvaluationStatus()` status to trigger an EventBridge event when an AWS Config
rule is re-evaluated.

```python
# Topic to which re-evaluation notification events will be published
re_evaluation_topic = sns.Topic(self, "ComplianceTopic")

rule = config.CloudFormationStackDriftDetectionCheck(self, "Drift")
rule.on_re_evaluation_status("ReEvaluationEvent",
    target=targets.SnsTopic(re_evaluation_topic)
)
```

### Example

The following example creates a custom rule that evaluates whether EC2 instances are compliant.
Compliance events are published to an SNS topic.

```python
# Lambda function containing logic that evaluates compliance with the rule.
eval_compliance_fn = lambda_.Function(self, "CustomFunction",
    code=lambda_.AssetCode.from_inline("exports.handler = (event) => console.log(event);"),
    handler="index.handler",
    runtime=lambda_.Runtime.NODEJS_14_X
)

# A custom rule that runs on configuration changes of EC2 instances
custom_rule = config.CustomRule(self, "Custom",
    configuration_changes=True,
    lambda_function=eval_compliance_fn,
    rule_scope=config.RuleScope.from_resource(config.ResourceType.EC2_INSTANCE)
)

# A rule to detect stack drifts
drift_rule = config.CloudFormationStackDriftDetectionCheck(self, "Drift")

# Topic to which compliance notification events will be published
compliance_topic = sns.Topic(self, "ComplianceTopic")

# Send notification on compliance change events
drift_rule.on_compliance_change("ComplianceChange",
    target=targets.SnsTopic(compliance_topic)
)
```
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

import aws_cdk.aws_events as _aws_cdk_aws_events_efcdfa54
import aws_cdk.aws_iam as _aws_cdk_aws_iam_940a1ce0
import aws_cdk.aws_lambda as _aws_cdk_aws_lambda_5443dbc3
import aws_cdk.aws_sns as _aws_cdk_aws_sns_889c7272
import aws_cdk.core as _aws_cdk_core_f4b25747
import constructs as _constructs_77d1e7e8


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnAggregationAuthorization(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-config.CfnAggregationAuthorization",
):
    '''A CloudFormation ``AWS::Config::AggregationAuthorization``.

    An object that represents the authorizations granted to aggregator accounts and regions.

    :cloudformationResource: AWS::Config::AggregationAuthorization
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-aggregationauthorization.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_config as config
        
        cfn_aggregation_authorization = config.CfnAggregationAuthorization(self, "MyCfnAggregationAuthorization",
            authorized_account_id="authorizedAccountId",
            authorized_aws_region="authorizedAwsRegion",
        
            # the properties below are optional
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
        authorized_account_id: builtins.str,
        authorized_aws_region: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Config::AggregationAuthorization``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param authorized_account_id: The 12-digit account ID of the account authorized to aggregate data.
        :param authorized_aws_region: The region authorized to collect aggregated data.
        :param tags: An array of tag object.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6a9d2dc813e1cf84217e5ea4c0bc4b35be477685bea184f0a0cc41ab6c4ac50)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAggregationAuthorizationProps(
            authorized_account_id=authorized_account_id,
            authorized_aws_region=authorized_aws_region,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8afed4d6cd342dbe2306a18e89730c831d4b6a76ca932077a372a0c240df633)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5f78841ee5e3698cfaf5ca0f7e4d6a43ff3e28cf72163941bdabde5bce232319)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAggregationAuthorizationArn")
    def attr_aggregation_authorization_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the aggregation object.

        :cloudformationAttribute: AggregationAuthorizationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAggregationAuthorizationArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _aws_cdk_core_f4b25747.TagManager:
        '''An array of tag object.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-aggregationauthorization.html#cfn-config-aggregationauthorization-tags
        '''
        return typing.cast(_aws_cdk_core_f4b25747.TagManager, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="authorizedAccountId")
    def authorized_account_id(self) -> builtins.str:
        '''The 12-digit account ID of the account authorized to aggregate data.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-aggregationauthorization.html#cfn-config-aggregationauthorization-authorizedaccountid
        '''
        return typing.cast(builtins.str, jsii.get(self, "authorizedAccountId"))

    @authorized_account_id.setter
    def authorized_account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6165e139d37da90d977b8ce17e308014c131b9ef327c8be5e2384dd97522c38b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizedAccountId", value)

    @builtins.property
    @jsii.member(jsii_name="authorizedAwsRegion")
    def authorized_aws_region(self) -> builtins.str:
        '''The region authorized to collect aggregated data.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-aggregationauthorization.html#cfn-config-aggregationauthorization-authorizedawsregion
        '''
        return typing.cast(builtins.str, jsii.get(self, "authorizedAwsRegion"))

    @authorized_aws_region.setter
    def authorized_aws_region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8dfd97ed4e91f2adb8693639da0cd45e3bab81e435ce21279f07b7bcecba462f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizedAwsRegion", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-config.CfnAggregationAuthorizationProps",
    jsii_struct_bases=[],
    name_mapping={
        "authorized_account_id": "authorizedAccountId",
        "authorized_aws_region": "authorizedAwsRegion",
        "tags": "tags",
    },
)
class CfnAggregationAuthorizationProps:
    def __init__(
        self,
        *,
        authorized_account_id: builtins.str,
        authorized_aws_region: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAggregationAuthorization``.

        :param authorized_account_id: The 12-digit account ID of the account authorized to aggregate data.
        :param authorized_aws_region: The region authorized to collect aggregated data.
        :param tags: An array of tag object.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-aggregationauthorization.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_config as config
            
            cfn_aggregation_authorization_props = config.CfnAggregationAuthorizationProps(
                authorized_account_id="authorizedAccountId",
                authorized_aws_region="authorizedAwsRegion",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01bd187f12935f617e2d9e75fe5baa997581bb7b03471eb5a5c84722e70a2763)
            check_type(argname="argument authorized_account_id", value=authorized_account_id, expected_type=type_hints["authorized_account_id"])
            check_type(argname="argument authorized_aws_region", value=authorized_aws_region, expected_type=type_hints["authorized_aws_region"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "authorized_account_id": authorized_account_id,
            "authorized_aws_region": authorized_aws_region,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def authorized_account_id(self) -> builtins.str:
        '''The 12-digit account ID of the account authorized to aggregate data.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-aggregationauthorization.html#cfn-config-aggregationauthorization-authorizedaccountid
        '''
        result = self._values.get("authorized_account_id")
        assert result is not None, "Required property 'authorized_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authorized_aws_region(self) -> builtins.str:
        '''The region authorized to collect aggregated data.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-aggregationauthorization.html#cfn-config-aggregationauthorization-authorizedawsregion
        '''
        result = self._values.get("authorized_aws_region")
        assert result is not None, "Required property 'authorized_aws_region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]]:
        '''An array of tag object.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-aggregationauthorization.html#cfn-config-aggregationauthorization-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAggregationAuthorizationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnConfigRule(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-config.CfnConfigRule",
):
    '''A CloudFormation ``AWS::Config::ConfigRule``.

    Adds or updates an AWS Config rule to evaluate if your AWS resources comply with your desired configurations. For information on how many AWS Config rules you can have per account, see `*Service Limits* <https://docs.aws.amazon.com/config/latest/developerguide/configlimits.html>`_ in the *AWS Config Developer Guide* .

    There are two types of rules: *AWS Config Managed Rules* and *AWS Config Custom Rules* . You can use the ``ConfigRule`` resource to create both AWS Config Managed Rules and AWS Config Custom Rules.

    AWS Config Managed Rules are predefined, customizable rules created by AWS Config . For a list of managed rules, see `List of AWS Config Managed Rules <https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html>`_ . If you are adding an AWS Config managed rule, you must specify the rule's identifier for the ``SourceIdentifier`` key.

    AWS Config Custom Rules are rules that you create from scratch. There are two ways to create AWS Config custom rules: with Lambda functions ( `AWS Lambda Developer Guide <https://docs.aws.amazon.com/config/latest/developerguide/gettingstarted-concepts.html#gettingstarted-concepts-function>`_ ) and with Guard ( `Guard GitHub Repository <https://docs.aws.amazon.com/https://github.com/aws-cloudformation/cloudformation-guard>`_ ), a policy-as-code language. AWS Config custom rules created with AWS Lambda are called *AWS Config Custom Lambda Rules* and AWS Config custom rules created with Guard are called *AWS Config Custom Policy Rules* .

    If you are adding a new AWS Config Custom Lambda rule, you first need to create an AWS Lambda function that the rule invokes to evaluate your resources. When you use the ``ConfigRule`` resource to add a Custom Lambda rule to AWS Config , you must specify the Amazon Resource Name (ARN) that AWS Lambda assigns to the function. You specify the ARN in the ``SourceIdentifier`` key. This key is part of the ``Source`` object, which is part of the ``ConfigRule`` object.

    For any new AWS Config rule that you add, specify the ``ConfigRuleName`` in the ``ConfigRule`` object. Do not specify the ``ConfigRuleArn`` or the ``ConfigRuleId`` . These values are generated by AWS Config for new rules.

    If you are updating a rule that you added previously, you can specify the rule by ``ConfigRuleName`` , ``ConfigRuleId`` , or ``ConfigRuleArn`` in the ``ConfigRule`` data type that you use in this request.

    For more information about developing and using AWS Config rules, see `Evaluating Resources with AWS Config Rules <https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html>`_ in the *AWS Config Developer Guide* .

    :cloudformationResource: AWS::Config::ConfigRule
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_config as config
        
        # input_parameters: Any
        
        cfn_config_rule = config.CfnConfigRule(self, "MyCfnConfigRule",
            source=config.CfnConfigRule.SourceProperty(
                owner="owner",
        
                # the properties below are optional
                custom_policy_details=config.CfnConfigRule.CustomPolicyDetailsProperty(
                    enable_debug_log_delivery=False,
                    policy_runtime="policyRuntime",
                    policy_text="policyText"
                ),
                source_details=[config.CfnConfigRule.SourceDetailProperty(
                    event_source="eventSource",
                    message_type="messageType",
        
                    # the properties below are optional
                    maximum_execution_frequency="maximumExecutionFrequency"
                )],
                source_identifier="sourceIdentifier"
            ),
        
            # the properties below are optional
            config_rule_name="configRuleName",
            description="description",
            input_parameters=input_parameters,
            maximum_execution_frequency="maximumExecutionFrequency",
            scope=config.CfnConfigRule.ScopeProperty(
                compliance_resource_id="complianceResourceId",
                compliance_resource_types=["complianceResourceTypes"],
                tag_key="tagKey",
                tag_value="tagValue"
            )
        )
    '''

    def __init__(
        self,
        scope_: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        source: typing.Union[typing.Union["CfnConfigRule.SourceProperty", typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable],
        config_rule_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        input_parameters: typing.Any = None,
        maximum_execution_frequency: typing.Optional[builtins.str] = None,
        scope: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnConfigRule.ScopeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Config::ConfigRule``.

        :param scope_: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param source: Provides the rule owner ( ``AWS`` for managed rules, ``CUSTOM_POLICY`` for Custom Policy rules, and ``CUSTOM_LAMBDA`` for Custom Lambda rules), the rule identifier, and the notifications that cause the function to evaluate your AWS resources.
        :param config_rule_name: A name for the AWS Config rule. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the rule name. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ .
        :param description: The description that you provide for the AWS Config rule.
        :param input_parameters: A string, in JSON format, that is passed to the AWS Config rule Lambda function.
        :param maximum_execution_frequency: The maximum frequency with which AWS Config runs evaluations for a rule. You can specify a value for ``MaximumExecutionFrequency`` when: - You are using an AWS managed rule that is triggered at a periodic frequency. - Your custom rule is triggered when AWS Config delivers the configuration snapshot. For more information, see `ConfigSnapshotDeliveryProperties <https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigSnapshotDeliveryProperties.html>`_ . .. epigraph:: By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.
        :param scope: Defines which resources can trigger an evaluation for the rule. The scope can include one or more resource types, a combination of one resource type and one resource ID, or a combination of a tag key and value. Specify a scope to constrain the resources that can trigger an evaluation for the rule. If you do not specify a scope, evaluations are triggered when any resource in the recording group changes. .. epigraph:: The scope can be empty.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b715dcb856de03e35118dac99b95e0217359c82cd030ec60042b90a19d3bbc3a)
            check_type(argname="argument scope_", value=scope_, expected_type=type_hints["scope_"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConfigRuleProps(
            source=source,
            config_rule_name=config_rule_name,
            description=description,
            input_parameters=input_parameters,
            maximum_execution_frequency=maximum_execution_frequency,
            scope=scope,
        )

        jsii.create(self.__class__, self, [scope_, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db2ccae574ac49665b735a58c56db60bfa86b499e650cbcdecfb089215620ca2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7937dfba02be731188c8748c596044bc2ee041ee6bf28ba1d46cb31a9bf5be88)
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
        '''The Amazon Resource Name (ARN) of the AWS Config rule, such as ``arn:aws:config:us-east-1:123456789012:config-rule/config-rule-a1bzhi`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrComplianceType")
    def attr_compliance_type(self) -> builtins.str:
        '''The compliance status of an AWS Config rule, such as ``COMPLIANT`` or ``NON_COMPLIANT`` .

        :cloudformationAttribute: Compliance.Type
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrComplianceType"))

    @builtins.property
    @jsii.member(jsii_name="attrConfigRuleId")
    def attr_config_rule_id(self) -> builtins.str:
        '''The ID of the AWS Config rule, such as ``config-rule-a1bzhi`` .

        :cloudformationAttribute: ConfigRuleId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConfigRuleId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="inputParameters")
    def input_parameters(self) -> typing.Any:
        '''A string, in JSON format, that is passed to the AWS Config rule Lambda function.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-inputparameters
        '''
        return typing.cast(typing.Any, jsii.get(self, "inputParameters"))

    @input_parameters.setter
    def input_parameters(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff040958078577219ea682de08dc9553e8d44daaa83242e6449ad3ee96a79523)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inputParameters", value)

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(
        self,
    ) -> typing.Union["CfnConfigRule.SourceProperty", _aws_cdk_core_f4b25747.IResolvable]:
        '''Provides the rule owner ( ``AWS`` for managed rules, ``CUSTOM_POLICY`` for Custom Policy rules, and ``CUSTOM_LAMBDA`` for Custom Lambda rules), the rule identifier, and the notifications that cause the function to evaluate your AWS resources.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-source
        '''
        return typing.cast(typing.Union["CfnConfigRule.SourceProperty", _aws_cdk_core_f4b25747.IResolvable], jsii.get(self, "source"))

    @source.setter
    def source(
        self,
        value: typing.Union["CfnConfigRule.SourceProperty", _aws_cdk_core_f4b25747.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0f68afb3b699133231ecbc84b9f921b9c3e1f70d9b9d355dc56beb936194643)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)

    @builtins.property
    @jsii.member(jsii_name="configRuleName")
    def config_rule_name(self) -> typing.Optional[builtins.str]:
        '''A name for the AWS Config rule.

        If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the rule name. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-configrulename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configRuleName"))

    @config_rule_name.setter
    def config_rule_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3758f13125433c373ef1fbbb714d3e990846b51bf97bdb59b5d43302b0978d21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configRuleName", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description that you provide for the AWS Config rule.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a73645d403a17ec49d8dfd0648eacbfab6c11243826612648ecde0051791e9d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="maximumExecutionFrequency")
    def maximum_execution_frequency(self) -> typing.Optional[builtins.str]:
        '''The maximum frequency with which AWS Config runs evaluations for a rule.

        You can specify a value for ``MaximumExecutionFrequency`` when:

        - You are using an AWS managed rule that is triggered at a periodic frequency.
        - Your custom rule is triggered when AWS Config delivers the configuration snapshot. For more information, see `ConfigSnapshotDeliveryProperties <https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigSnapshotDeliveryProperties.html>`_ .

        .. epigraph::

           By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-maximumexecutionfrequency
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maximumExecutionFrequency"))

    @maximum_execution_frequency.setter
    def maximum_execution_frequency(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d64d9703cd2c88f8c39b9debc7cf183956e8e1c29221cdc7067713cbd5f0f07d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumExecutionFrequency", value)

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnConfigRule.ScopeProperty"]]:
        '''Defines which resources can trigger an evaluation for the rule.

        The scope can include one or more resource types, a combination of one resource type and one resource ID, or a combination of a tag key and value. Specify a scope to constrain the resources that can trigger an evaluation for the rule. If you do not specify a scope, evaluations are triggered when any resource in the recording group changes.
        .. epigraph::

           The scope can be empty.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-scope
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnConfigRule.ScopeProperty"]], jsii.get(self, "scope"))

    @scope.setter
    def scope(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnConfigRule.ScopeProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5356ac2e6f88f0e5e1f7b165b7bf50408cf67e439b9dacf51ed3ef3210504e87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scope", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-config.CfnConfigRule.CustomPolicyDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enable_debug_log_delivery": "enableDebugLogDelivery",
            "policy_runtime": "policyRuntime",
            "policy_text": "policyText",
        },
    )
    class CustomPolicyDetailsProperty:
        def __init__(
            self,
            *,
            enable_debug_log_delivery: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            policy_runtime: typing.Optional[builtins.str] = None,
            policy_text: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides the runtime system, policy definition, and whether debug logging enabled.

            You can specify the following CustomPolicyDetails parameter values only for AWS Config Custom Policy rules.

            :param enable_debug_log_delivery: The boolean expression for enabling debug logging for your AWS Config Custom Policy rule. The default value is ``false`` .
            :param policy_runtime: The runtime system for your AWS Config Custom Policy rule. Guard is a policy-as-code language that allows you to write policies that are enforced by AWS Config Custom Policy rules. For more information about Guard, see the `Guard GitHub Repository <https://docs.aws.amazon.com/https://github.com/aws-cloudformation/cloudformation-guard>`_ .
            :param policy_text: The policy definition containing the logic for your AWS Config Custom Policy rule.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-custompolicydetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_config as config
                
                custom_policy_details_property = config.CfnConfigRule.CustomPolicyDetailsProperty(
                    enable_debug_log_delivery=False,
                    policy_runtime="policyRuntime",
                    policy_text="policyText"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__06ebb7d82eb683640594e4fa806c53b9ee50c6cd4cd5ddf00d173ab257688cdd)
                check_type(argname="argument enable_debug_log_delivery", value=enable_debug_log_delivery, expected_type=type_hints["enable_debug_log_delivery"])
                check_type(argname="argument policy_runtime", value=policy_runtime, expected_type=type_hints["policy_runtime"])
                check_type(argname="argument policy_text", value=policy_text, expected_type=type_hints["policy_text"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enable_debug_log_delivery is not None:
                self._values["enable_debug_log_delivery"] = enable_debug_log_delivery
            if policy_runtime is not None:
                self._values["policy_runtime"] = policy_runtime
            if policy_text is not None:
                self._values["policy_text"] = policy_text

        @builtins.property
        def enable_debug_log_delivery(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''The boolean expression for enabling debug logging for your AWS Config Custom Policy rule.

            The default value is ``false`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-custompolicydetails.html#cfn-config-configrule-custompolicydetails-enabledebuglogdelivery
            '''
            result = self._values.get("enable_debug_log_delivery")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def policy_runtime(self) -> typing.Optional[builtins.str]:
            '''The runtime system for your AWS Config Custom Policy rule.

            Guard is a policy-as-code language that allows you to write policies that are enforced by AWS Config Custom Policy rules. For more information about Guard, see the `Guard GitHub Repository <https://docs.aws.amazon.com/https://github.com/aws-cloudformation/cloudformation-guard>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-custompolicydetails.html#cfn-config-configrule-custompolicydetails-policyruntime
            '''
            result = self._values.get("policy_runtime")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def policy_text(self) -> typing.Optional[builtins.str]:
            '''The policy definition containing the logic for your AWS Config Custom Policy rule.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-custompolicydetails.html#cfn-config-configrule-custompolicydetails-policytext
            '''
            result = self._values.get("policy_text")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomPolicyDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-config.CfnConfigRule.ScopeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "compliance_resource_id": "complianceResourceId",
            "compliance_resource_types": "complianceResourceTypes",
            "tag_key": "tagKey",
            "tag_value": "tagValue",
        },
    )
    class ScopeProperty:
        def __init__(
            self,
            *,
            compliance_resource_id: typing.Optional[builtins.str] = None,
            compliance_resource_types: typing.Optional[typing.Sequence[builtins.str]] = None,
            tag_key: typing.Optional[builtins.str] = None,
            tag_value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines which resources trigger an evaluation for an AWS Config rule.

            The scope can include one or more resource types, a combination of a tag key and value, or a combination of one resource type and one resource ID. Specify a scope to constrain which resources trigger an evaluation for a rule. Otherwise, evaluations for the rule are triggered when any resource in your recording group changes in configuration.

            :param compliance_resource_id: The ID of the only AWS resource that you want to trigger an evaluation for the rule. If you specify a resource ID, you must specify one resource type for ``ComplianceResourceTypes`` .
            :param compliance_resource_types: The resource types of only those AWS resources that you want to trigger an evaluation for the rule. You can only specify one type if you also specify a resource ID for ``ComplianceResourceId`` .
            :param tag_key: The tag key that is applied to only those AWS resources that you want to trigger an evaluation for the rule.
            :param tag_value: The tag value applied to only those AWS resources that you want to trigger an evaluation for the rule. If you specify a value for ``TagValue`` , you must also specify a value for ``TagKey`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-scope.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_config as config
                
                scope_property = config.CfnConfigRule.ScopeProperty(
                    compliance_resource_id="complianceResourceId",
                    compliance_resource_types=["complianceResourceTypes"],
                    tag_key="tagKey",
                    tag_value="tagValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a3f871ed3e31c85d7e5e120d04b6284671d677ef54d9f11ccb3c9e359c42b2d0)
                check_type(argname="argument compliance_resource_id", value=compliance_resource_id, expected_type=type_hints["compliance_resource_id"])
                check_type(argname="argument compliance_resource_types", value=compliance_resource_types, expected_type=type_hints["compliance_resource_types"])
                check_type(argname="argument tag_key", value=tag_key, expected_type=type_hints["tag_key"])
                check_type(argname="argument tag_value", value=tag_value, expected_type=type_hints["tag_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if compliance_resource_id is not None:
                self._values["compliance_resource_id"] = compliance_resource_id
            if compliance_resource_types is not None:
                self._values["compliance_resource_types"] = compliance_resource_types
            if tag_key is not None:
                self._values["tag_key"] = tag_key
            if tag_value is not None:
                self._values["tag_value"] = tag_value

        @builtins.property
        def compliance_resource_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the only AWS resource that you want to trigger an evaluation for the rule.

            If you specify a resource ID, you must specify one resource type for ``ComplianceResourceTypes`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-scope.html#cfn-config-configrule-scope-complianceresourceid
            '''
            result = self._values.get("compliance_resource_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def compliance_resource_types(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''The resource types of only those AWS resources that you want to trigger an evaluation for the rule.

            You can only specify one type if you also specify a resource ID for ``ComplianceResourceId`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-scope.html#cfn-config-configrule-scope-complianceresourcetypes
            '''
            result = self._values.get("compliance_resource_types")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def tag_key(self) -> typing.Optional[builtins.str]:
            '''The tag key that is applied to only those AWS resources that you want to trigger an evaluation for the rule.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-scope.html#cfn-config-configrule-scope-tagkey
            '''
            result = self._values.get("tag_key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tag_value(self) -> typing.Optional[builtins.str]:
            '''The tag value applied to only those AWS resources that you want to trigger an evaluation for the rule.

            If you specify a value for ``TagValue`` , you must also specify a value for ``TagKey`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-scope.html#cfn-config-configrule-scope-tagvalue
            '''
            result = self._values.get("tag_value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScopeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-config.CfnConfigRule.SourceDetailProperty",
        jsii_struct_bases=[],
        name_mapping={
            "event_source": "eventSource",
            "message_type": "messageType",
            "maximum_execution_frequency": "maximumExecutionFrequency",
        },
    )
    class SourceDetailProperty:
        def __init__(
            self,
            *,
            event_source: builtins.str,
            message_type: builtins.str,
            maximum_execution_frequency: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides the source and the message types that trigger AWS Config to evaluate your AWS resources against a rule.

            It also provides the frequency with which you want AWS Config to run evaluations for the rule if the trigger type is periodic. You can specify the parameter values for ``SourceDetail`` only for custom rules.

            :param event_source: The source of the event, such as an AWS service, that triggers AWS Config to evaluate your AWS resources.
            :param message_type: The type of notification that triggers AWS Config to run an evaluation for a rule. You can specify the following notification types: - ``ConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config delivers a configuration item as a result of a resource change. - ``OversizedConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config delivers an oversized configuration item. AWS Config may generate this notification type when a resource changes and the notification exceeds the maximum size allowed by Amazon SNS. - ``ScheduledNotification`` - Triggers a periodic evaluation at the frequency specified for ``MaximumExecutionFrequency`` . - ``ConfigurationSnapshotDeliveryCompleted`` - Triggers a periodic evaluation when AWS Config delivers a configuration snapshot. If you want your custom rule to be triggered by configuration changes, specify two SourceDetail objects, one for ``ConfigurationItemChangeNotification`` and one for ``OversizedConfigurationItemChangeNotification`` .
            :param maximum_execution_frequency: The frequency at which you want AWS Config to run evaluations for a custom rule with a periodic trigger. If you specify a value for ``MaximumExecutionFrequency`` , then ``MessageType`` must use the ``ScheduledNotification`` value. .. epigraph:: By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter. Based on the valid value you choose, AWS Config runs evaluations once for each valid value. For example, if you choose ``Three_Hours`` , AWS Config runs evaluations once every three hours. In this case, ``Three_Hours`` is the frequency of this rule.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source-sourcedetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_config as config
                
                source_detail_property = config.CfnConfigRule.SourceDetailProperty(
                    event_source="eventSource",
                    message_type="messageType",
                
                    # the properties below are optional
                    maximum_execution_frequency="maximumExecutionFrequency"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2797e199072ce461a39d33ff9e62230185747dda75b6e5facbd285c3b0c5edf9)
                check_type(argname="argument event_source", value=event_source, expected_type=type_hints["event_source"])
                check_type(argname="argument message_type", value=message_type, expected_type=type_hints["message_type"])
                check_type(argname="argument maximum_execution_frequency", value=maximum_execution_frequency, expected_type=type_hints["maximum_execution_frequency"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "event_source": event_source,
                "message_type": message_type,
            }
            if maximum_execution_frequency is not None:
                self._values["maximum_execution_frequency"] = maximum_execution_frequency

        @builtins.property
        def event_source(self) -> builtins.str:
            '''The source of the event, such as an AWS service, that triggers AWS Config to evaluate your AWS resources.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source-sourcedetails.html#cfn-config-configrule-source-sourcedetail-eventsource
            '''
            result = self._values.get("event_source")
            assert result is not None, "Required property 'event_source' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def message_type(self) -> builtins.str:
            '''The type of notification that triggers AWS Config to run an evaluation for a rule.

            You can specify the following notification types:

            - ``ConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config delivers a configuration item as a result of a resource change.
            - ``OversizedConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config delivers an oversized configuration item. AWS Config may generate this notification type when a resource changes and the notification exceeds the maximum size allowed by Amazon SNS.
            - ``ScheduledNotification`` - Triggers a periodic evaluation at the frequency specified for ``MaximumExecutionFrequency`` .
            - ``ConfigurationSnapshotDeliveryCompleted`` - Triggers a periodic evaluation when AWS Config delivers a configuration snapshot.

            If you want your custom rule to be triggered by configuration changes, specify two SourceDetail objects, one for ``ConfigurationItemChangeNotification`` and one for ``OversizedConfigurationItemChangeNotification`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source-sourcedetails.html#cfn-config-configrule-source-sourcedetail-messagetype
            '''
            result = self._values.get("message_type")
            assert result is not None, "Required property 'message_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def maximum_execution_frequency(self) -> typing.Optional[builtins.str]:
            '''The frequency at which you want AWS Config to run evaluations for a custom rule with a periodic trigger.

            If you specify a value for ``MaximumExecutionFrequency`` , then ``MessageType`` must use the ``ScheduledNotification`` value.
            .. epigraph::

               By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.

               Based on the valid value you choose, AWS Config runs evaluations once for each valid value. For example, if you choose ``Three_Hours`` , AWS Config runs evaluations once every three hours. In this case, ``Three_Hours`` is the frequency of this rule.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source-sourcedetails.html#cfn-config-configrule-sourcedetail-maximumexecutionfrequency
            '''
            result = self._values.get("maximum_execution_frequency")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceDetailProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-config.CfnConfigRule.SourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "owner": "owner",
            "custom_policy_details": "customPolicyDetails",
            "source_details": "sourceDetails",
            "source_identifier": "sourceIdentifier",
        },
    )
    class SourceProperty:
        def __init__(
            self,
            *,
            owner: builtins.str,
            custom_policy_details: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnConfigRule.CustomPolicyDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            source_details: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnConfigRule.SourceDetailProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            source_identifier: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides the CustomPolicyDetails, the rule owner ( ``AWS`` for managed rules, ``CUSTOM_POLICY`` for Custom Policy rules, and ``CUSTOM_LAMBDA`` for Custom Lambda rules), the rule identifier, and the events that cause the evaluation of your AWS resources.

            :param owner: Indicates whether AWS or the customer owns and manages the AWS Config rule. AWS Config Managed Rules are predefined rules owned by AWS . For more information, see `AWS Config Managed Rules <https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html>`_ in the *AWS Config developer guide* . AWS Config Custom Rules are rules that you can develop either with Guard ( ``CUSTOM_POLICY`` ) or AWS Lambda ( ``CUSTOM_LAMBDA`` ). For more information, see `AWS Config Custom Rules <https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules.html>`_ in the *AWS Config developer guide* .
            :param custom_policy_details: Provides the runtime system, policy definition, and whether debug logging is enabled. Required when owner is set to ``CUSTOM_POLICY`` .
            :param source_details: Provides the source and the message types that cause AWS Config to evaluate your AWS resources against a rule. It also provides the frequency with which you want AWS Config to run evaluations for the rule if the trigger type is periodic. If the owner is set to ``CUSTOM_POLICY`` , the only acceptable values for the AWS Config rule trigger message type are ``ConfigurationItemChangeNotification`` and ``OversizedConfigurationItemChangeNotification`` .
            :param source_identifier: For AWS Config Managed rules, a predefined identifier from a list. For example, ``IAM_PASSWORD_POLICY`` is a managed rule. To reference a managed rule, see `List of AWS Config Managed Rules <https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html>`_ . For AWS Config Custom Lambda rules, the identifier is the Amazon Resource Name (ARN) of the rule's AWS Lambda function, such as ``arn:aws:lambda:us-east-2:123456789012:function:custom_rule_name`` . For AWS Config Custom Policy rules, this field will be ignored.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_config as config
                
                source_property = config.CfnConfigRule.SourceProperty(
                    owner="owner",
                
                    # the properties below are optional
                    custom_policy_details=config.CfnConfigRule.CustomPolicyDetailsProperty(
                        enable_debug_log_delivery=False,
                        policy_runtime="policyRuntime",
                        policy_text="policyText"
                    ),
                    source_details=[config.CfnConfigRule.SourceDetailProperty(
                        event_source="eventSource",
                        message_type="messageType",
                
                        # the properties below are optional
                        maximum_execution_frequency="maximumExecutionFrequency"
                    )],
                    source_identifier="sourceIdentifier"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__acb56d8b83fc364cb5dd698ef9028c60fb41d21514ce088402ea83dad69a45e5)
                check_type(argname="argument owner", value=owner, expected_type=type_hints["owner"])
                check_type(argname="argument custom_policy_details", value=custom_policy_details, expected_type=type_hints["custom_policy_details"])
                check_type(argname="argument source_details", value=source_details, expected_type=type_hints["source_details"])
                check_type(argname="argument source_identifier", value=source_identifier, expected_type=type_hints["source_identifier"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "owner": owner,
            }
            if custom_policy_details is not None:
                self._values["custom_policy_details"] = custom_policy_details
            if source_details is not None:
                self._values["source_details"] = source_details
            if source_identifier is not None:
                self._values["source_identifier"] = source_identifier

        @builtins.property
        def owner(self) -> builtins.str:
            '''Indicates whether AWS or the customer owns and manages the AWS Config rule.

            AWS Config Managed Rules are predefined rules owned by AWS . For more information, see `AWS Config Managed Rules <https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html>`_ in the *AWS Config developer guide* .

            AWS Config Custom Rules are rules that you can develop either with Guard ( ``CUSTOM_POLICY`` ) or AWS Lambda ( ``CUSTOM_LAMBDA`` ). For more information, see `AWS Config Custom Rules <https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules.html>`_ in the *AWS Config developer guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source.html#cfn-config-configrule-source-owner
            '''
            result = self._values.get("owner")
            assert result is not None, "Required property 'owner' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def custom_policy_details(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnConfigRule.CustomPolicyDetailsProperty"]]:
            '''Provides the runtime system, policy definition, and whether debug logging is enabled.

            Required when owner is set to ``CUSTOM_POLICY`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source.html#cfn-config-configrule-source-custompolicydetails
            '''
            result = self._values.get("custom_policy_details")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnConfigRule.CustomPolicyDetailsProperty"]], result)

        @builtins.property
        def source_details(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnConfigRule.SourceDetailProperty"]]]]:
            '''Provides the source and the message types that cause AWS Config to evaluate your AWS resources against a rule.

            It also provides the frequency with which you want AWS Config to run evaluations for the rule if the trigger type is periodic.

            If the owner is set to ``CUSTOM_POLICY`` , the only acceptable values for the AWS Config rule trigger message type are ``ConfigurationItemChangeNotification`` and ``OversizedConfigurationItemChangeNotification`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source.html#cfn-config-configrule-source-sourcedetails
            '''
            result = self._values.get("source_details")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnConfigRule.SourceDetailProperty"]]]], result)

        @builtins.property
        def source_identifier(self) -> typing.Optional[builtins.str]:
            '''For AWS Config Managed rules, a predefined identifier from a list.

            For example, ``IAM_PASSWORD_POLICY`` is a managed rule. To reference a managed rule, see `List of AWS Config Managed Rules <https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html>`_ .

            For AWS Config Custom Lambda rules, the identifier is the Amazon Resource Name (ARN) of the rule's AWS Lambda function, such as ``arn:aws:lambda:us-east-2:123456789012:function:custom_rule_name`` .

            For AWS Config Custom Policy rules, this field will be ignored.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source.html#cfn-config-configrule-source-sourceidentifier
            '''
            result = self._values.get("source_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-config.CfnConfigRuleProps",
    jsii_struct_bases=[],
    name_mapping={
        "source": "source",
        "config_rule_name": "configRuleName",
        "description": "description",
        "input_parameters": "inputParameters",
        "maximum_execution_frequency": "maximumExecutionFrequency",
        "scope": "scope",
    },
)
class CfnConfigRuleProps:
    def __init__(
        self,
        *,
        source: typing.Union[typing.Union[CfnConfigRule.SourceProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable],
        config_rule_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        input_parameters: typing.Any = None,
        maximum_execution_frequency: typing.Optional[builtins.str] = None,
        scope: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnConfigRule.ScopeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnConfigRule``.

        :param source: Provides the rule owner ( ``AWS`` for managed rules, ``CUSTOM_POLICY`` for Custom Policy rules, and ``CUSTOM_LAMBDA`` for Custom Lambda rules), the rule identifier, and the notifications that cause the function to evaluate your AWS resources.
        :param config_rule_name: A name for the AWS Config rule. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the rule name. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ .
        :param description: The description that you provide for the AWS Config rule.
        :param input_parameters: A string, in JSON format, that is passed to the AWS Config rule Lambda function.
        :param maximum_execution_frequency: The maximum frequency with which AWS Config runs evaluations for a rule. You can specify a value for ``MaximumExecutionFrequency`` when: - You are using an AWS managed rule that is triggered at a periodic frequency. - Your custom rule is triggered when AWS Config delivers the configuration snapshot. For more information, see `ConfigSnapshotDeliveryProperties <https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigSnapshotDeliveryProperties.html>`_ . .. epigraph:: By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.
        :param scope: Defines which resources can trigger an evaluation for the rule. The scope can include one or more resource types, a combination of one resource type and one resource ID, or a combination of a tag key and value. Specify a scope to constrain the resources that can trigger an evaluation for the rule. If you do not specify a scope, evaluations are triggered when any resource in the recording group changes. .. epigraph:: The scope can be empty.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_config as config
            
            # input_parameters: Any
            
            cfn_config_rule_props = config.CfnConfigRuleProps(
                source=config.CfnConfigRule.SourceProperty(
                    owner="owner",
            
                    # the properties below are optional
                    custom_policy_details=config.CfnConfigRule.CustomPolicyDetailsProperty(
                        enable_debug_log_delivery=False,
                        policy_runtime="policyRuntime",
                        policy_text="policyText"
                    ),
                    source_details=[config.CfnConfigRule.SourceDetailProperty(
                        event_source="eventSource",
                        message_type="messageType",
            
                        # the properties below are optional
                        maximum_execution_frequency="maximumExecutionFrequency"
                    )],
                    source_identifier="sourceIdentifier"
                ),
            
                # the properties below are optional
                config_rule_name="configRuleName",
                description="description",
                input_parameters=input_parameters,
                maximum_execution_frequency="maximumExecutionFrequency",
                scope=config.CfnConfigRule.ScopeProperty(
                    compliance_resource_id="complianceResourceId",
                    compliance_resource_types=["complianceResourceTypes"],
                    tag_key="tagKey",
                    tag_value="tagValue"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b65c6f4c78dffa21e21051386073637fda26a165240c20fb82dd516c4946490)
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument config_rule_name", value=config_rule_name, expected_type=type_hints["config_rule_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument input_parameters", value=input_parameters, expected_type=type_hints["input_parameters"])
            check_type(argname="argument maximum_execution_frequency", value=maximum_execution_frequency, expected_type=type_hints["maximum_execution_frequency"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "source": source,
        }
        if config_rule_name is not None:
            self._values["config_rule_name"] = config_rule_name
        if description is not None:
            self._values["description"] = description
        if input_parameters is not None:
            self._values["input_parameters"] = input_parameters
        if maximum_execution_frequency is not None:
            self._values["maximum_execution_frequency"] = maximum_execution_frequency
        if scope is not None:
            self._values["scope"] = scope

    @builtins.property
    def source(
        self,
    ) -> typing.Union[CfnConfigRule.SourceProperty, _aws_cdk_core_f4b25747.IResolvable]:
        '''Provides the rule owner ( ``AWS`` for managed rules, ``CUSTOM_POLICY`` for Custom Policy rules, and ``CUSTOM_LAMBDA`` for Custom Lambda rules), the rule identifier, and the notifications that cause the function to evaluate your AWS resources.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-source
        '''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(typing.Union[CfnConfigRule.SourceProperty, _aws_cdk_core_f4b25747.IResolvable], result)

    @builtins.property
    def config_rule_name(self) -> typing.Optional[builtins.str]:
        '''A name for the AWS Config rule.

        If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the rule name. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-configrulename
        '''
        result = self._values.get("config_rule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description that you provide for the AWS Config rule.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def input_parameters(self) -> typing.Any:
        '''A string, in JSON format, that is passed to the AWS Config rule Lambda function.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-inputparameters
        '''
        result = self._values.get("input_parameters")
        return typing.cast(typing.Any, result)

    @builtins.property
    def maximum_execution_frequency(self) -> typing.Optional[builtins.str]:
        '''The maximum frequency with which AWS Config runs evaluations for a rule.

        You can specify a value for ``MaximumExecutionFrequency`` when:

        - You are using an AWS managed rule that is triggered at a periodic frequency.
        - Your custom rule is triggered when AWS Config delivers the configuration snapshot. For more information, see `ConfigSnapshotDeliveryProperties <https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigSnapshotDeliveryProperties.html>`_ .

        .. epigraph::

           By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-maximumexecutionfrequency
        '''
        result = self._values.get("maximum_execution_frequency")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scope(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnConfigRule.ScopeProperty]]:
        '''Defines which resources can trigger an evaluation for the rule.

        The scope can include one or more resource types, a combination of one resource type and one resource ID, or a combination of a tag key and value. Specify a scope to constrain the resources that can trigger an evaluation for the rule. If you do not specify a scope, evaluations are triggered when any resource in the recording group changes.
        .. epigraph::

           The scope can be empty.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-scope
        '''
        result = self._values.get("scope")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnConfigRule.ScopeProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConfigRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnConfigurationAggregator(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-config.CfnConfigurationAggregator",
):
    '''A CloudFormation ``AWS::Config::ConfigurationAggregator``.

    The details about the configuration aggregator, including information about source accounts, regions, and metadata of the aggregator.

    :cloudformationResource: AWS::Config::ConfigurationAggregator
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationaggregator.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_config as config
        
        cfn_configuration_aggregator = config.CfnConfigurationAggregator(self, "MyCfnConfigurationAggregator",
            account_aggregation_sources=[config.CfnConfigurationAggregator.AccountAggregationSourceProperty(
                account_ids=["accountIds"],
        
                # the properties below are optional
                all_aws_regions=False,
                aws_regions=["awsRegions"]
            )],
            configuration_aggregator_name="configurationAggregatorName",
            organization_aggregation_source=config.CfnConfigurationAggregator.OrganizationAggregationSourceProperty(
                role_arn="roleArn",
        
                # the properties below are optional
                all_aws_regions=False,
                aws_regions=["awsRegions"]
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
        account_aggregation_sources: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnConfigurationAggregator.AccountAggregationSourceProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        configuration_aggregator_name: typing.Optional[builtins.str] = None,
        organization_aggregation_source: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnConfigurationAggregator.OrganizationAggregationSourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Config::ConfigurationAggregator``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param account_aggregation_sources: Provides a list of source accounts and regions to be aggregated.
        :param configuration_aggregator_name: The name of the aggregator.
        :param organization_aggregation_source: Provides an organization and list of regions to be aggregated.
        :param tags: An array of tag object.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25d65699ab65b867983329a04b0d91d9c7377e7e8ecf97c6a93a9af62b80c24a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConfigurationAggregatorProps(
            account_aggregation_sources=account_aggregation_sources,
            configuration_aggregator_name=configuration_aggregator_name,
            organization_aggregation_source=organization_aggregation_source,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__082ab66bb975c2363e25b7556f992d975af557f7130ef2e4117dda6aa2d63ec7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6f4f5a5bf3cbad30bbf119c1aafe52cf1f9254a12aa417f41ae14b11a9f1fb81)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrConfigurationAggregatorArn")
    def attr_configuration_aggregator_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the aggregator.

        :cloudformationAttribute: ConfigurationAggregatorArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConfigurationAggregatorArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _aws_cdk_core_f4b25747.TagManager:
        '''An array of tag object.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationaggregator.html#cfn-config-configurationaggregator-tags
        '''
        return typing.cast(_aws_cdk_core_f4b25747.TagManager, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="accountAggregationSources")
    def account_aggregation_sources(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnConfigurationAggregator.AccountAggregationSourceProperty"]]]]:
        '''Provides a list of source accounts and regions to be aggregated.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationaggregator.html#cfn-config-configurationaggregator-accountaggregationsources
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnConfigurationAggregator.AccountAggregationSourceProperty"]]]], jsii.get(self, "accountAggregationSources"))

    @account_aggregation_sources.setter
    def account_aggregation_sources(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnConfigurationAggregator.AccountAggregationSourceProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e75c62528f4ad029fddbeff3ed3636efa81228c3c20898b2700b68439d06c794)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountAggregationSources", value)

    @builtins.property
    @jsii.member(jsii_name="configurationAggregatorName")
    def configuration_aggregator_name(self) -> typing.Optional[builtins.str]:
        '''The name of the aggregator.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationaggregator.html#cfn-config-configurationaggregator-configurationaggregatorname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configurationAggregatorName"))

    @configuration_aggregator_name.setter
    def configuration_aggregator_name(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efabd439525114d765db310ecae400a923c8682659664af91c7ef89071465597)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurationAggregatorName", value)

    @builtins.property
    @jsii.member(jsii_name="organizationAggregationSource")
    def organization_aggregation_source(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnConfigurationAggregator.OrganizationAggregationSourceProperty"]]:
        '''Provides an organization and list of regions to be aggregated.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationaggregator.html#cfn-config-configurationaggregator-organizationaggregationsource
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnConfigurationAggregator.OrganizationAggregationSourceProperty"]], jsii.get(self, "organizationAggregationSource"))

    @organization_aggregation_source.setter
    def organization_aggregation_source(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnConfigurationAggregator.OrganizationAggregationSourceProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0afda739d86bd65f4de026a74441c31d72849a5a610e030860b8116599f3fb5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organizationAggregationSource", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-config.CfnConfigurationAggregator.AccountAggregationSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "account_ids": "accountIds",
            "all_aws_regions": "allAwsRegions",
            "aws_regions": "awsRegions",
        },
    )
    class AccountAggregationSourceProperty:
        def __init__(
            self,
            *,
            account_ids: typing.Sequence[builtins.str],
            all_aws_regions: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''A collection of accounts and regions.

            :param account_ids: The 12-digit account ID of the account being aggregated.
            :param all_aws_regions: If true, aggregate existing AWS Config regions and future regions.
            :param aws_regions: The source regions being aggregated.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-accountaggregationsource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_config as config
                
                account_aggregation_source_property = config.CfnConfigurationAggregator.AccountAggregationSourceProperty(
                    account_ids=["accountIds"],
                
                    # the properties below are optional
                    all_aws_regions=False,
                    aws_regions=["awsRegions"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8ce2db2e204bf98d1b52629954f9ab5f5c97e9d90d92da09ef813f9c0edb7ebb)
                check_type(argname="argument account_ids", value=account_ids, expected_type=type_hints["account_ids"])
                check_type(argname="argument all_aws_regions", value=all_aws_regions, expected_type=type_hints["all_aws_regions"])
                check_type(argname="argument aws_regions", value=aws_regions, expected_type=type_hints["aws_regions"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "account_ids": account_ids,
            }
            if all_aws_regions is not None:
                self._values["all_aws_regions"] = all_aws_regions
            if aws_regions is not None:
                self._values["aws_regions"] = aws_regions

        @builtins.property
        def account_ids(self) -> typing.List[builtins.str]:
            '''The 12-digit account ID of the account being aggregated.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-accountaggregationsource.html#cfn-config-configurationaggregator-accountaggregationsource-accountids
            '''
            result = self._values.get("account_ids")
            assert result is not None, "Required property 'account_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def all_aws_regions(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''If true, aggregate existing AWS Config regions and future regions.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-accountaggregationsource.html#cfn-config-configurationaggregator-accountaggregationsource-allawsregions
            '''
            result = self._values.get("all_aws_regions")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def aws_regions(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The source regions being aggregated.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-accountaggregationsource.html#cfn-config-configurationaggregator-accountaggregationsource-awsregions
            '''
            result = self._values.get("aws_regions")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AccountAggregationSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-config.CfnConfigurationAggregator.OrganizationAggregationSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "role_arn": "roleArn",
            "all_aws_regions": "allAwsRegions",
            "aws_regions": "awsRegions",
        },
    )
    class OrganizationAggregationSourceProperty:
        def __init__(
            self,
            *,
            role_arn: builtins.str,
            all_aws_regions: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''This object contains regions to set up the aggregator and an IAM role to retrieve organization details.

            :param role_arn: ARN of the IAM role used to retrieve AWS Organizations details associated with the aggregator account.
            :param all_aws_regions: If true, aggregate existing AWS Config regions and future regions.
            :param aws_regions: The source regions being aggregated.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-organizationaggregationsource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_config as config
                
                organization_aggregation_source_property = config.CfnConfigurationAggregator.OrganizationAggregationSourceProperty(
                    role_arn="roleArn",
                
                    # the properties below are optional
                    all_aws_regions=False,
                    aws_regions=["awsRegions"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__54ac6abb32014e25f820d49ee5da1db68a05c9d687343325ef4ec98072169b61)
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument all_aws_regions", value=all_aws_regions, expected_type=type_hints["all_aws_regions"])
                check_type(argname="argument aws_regions", value=aws_regions, expected_type=type_hints["aws_regions"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "role_arn": role_arn,
            }
            if all_aws_regions is not None:
                self._values["all_aws_regions"] = all_aws_regions
            if aws_regions is not None:
                self._values["aws_regions"] = aws_regions

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''ARN of the IAM role used to retrieve AWS Organizations details associated with the aggregator account.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-organizationaggregationsource.html#cfn-config-configurationaggregator-organizationaggregationsource-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def all_aws_regions(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''If true, aggregate existing AWS Config regions and future regions.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-organizationaggregationsource.html#cfn-config-configurationaggregator-organizationaggregationsource-allawsregions
            '''
            result = self._values.get("all_aws_regions")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def aws_regions(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The source regions being aggregated.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-organizationaggregationsource.html#cfn-config-configurationaggregator-organizationaggregationsource-awsregions
            '''
            result = self._values.get("aws_regions")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OrganizationAggregationSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-config.CfnConfigurationAggregatorProps",
    jsii_struct_bases=[],
    name_mapping={
        "account_aggregation_sources": "accountAggregationSources",
        "configuration_aggregator_name": "configurationAggregatorName",
        "organization_aggregation_source": "organizationAggregationSource",
        "tags": "tags",
    },
)
class CfnConfigurationAggregatorProps:
    def __init__(
        self,
        *,
        account_aggregation_sources: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnConfigurationAggregator.AccountAggregationSourceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        configuration_aggregator_name: typing.Optional[builtins.str] = None,
        organization_aggregation_source: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnConfigurationAggregator.OrganizationAggregationSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnConfigurationAggregator``.

        :param account_aggregation_sources: Provides a list of source accounts and regions to be aggregated.
        :param configuration_aggregator_name: The name of the aggregator.
        :param organization_aggregation_source: Provides an organization and list of regions to be aggregated.
        :param tags: An array of tag object.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationaggregator.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_config as config
            
            cfn_configuration_aggregator_props = config.CfnConfigurationAggregatorProps(
                account_aggregation_sources=[config.CfnConfigurationAggregator.AccountAggregationSourceProperty(
                    account_ids=["accountIds"],
            
                    # the properties below are optional
                    all_aws_regions=False,
                    aws_regions=["awsRegions"]
                )],
                configuration_aggregator_name="configurationAggregatorName",
                organization_aggregation_source=config.CfnConfigurationAggregator.OrganizationAggregationSourceProperty(
                    role_arn="roleArn",
            
                    # the properties below are optional
                    all_aws_regions=False,
                    aws_regions=["awsRegions"]
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00843dd48d11cd13753b312a22e8e672e6fd05192603e46c90ffc0e969121443)
            check_type(argname="argument account_aggregation_sources", value=account_aggregation_sources, expected_type=type_hints["account_aggregation_sources"])
            check_type(argname="argument configuration_aggregator_name", value=configuration_aggregator_name, expected_type=type_hints["configuration_aggregator_name"])
            check_type(argname="argument organization_aggregation_source", value=organization_aggregation_source, expected_type=type_hints["organization_aggregation_source"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if account_aggregation_sources is not None:
            self._values["account_aggregation_sources"] = account_aggregation_sources
        if configuration_aggregator_name is not None:
            self._values["configuration_aggregator_name"] = configuration_aggregator_name
        if organization_aggregation_source is not None:
            self._values["organization_aggregation_source"] = organization_aggregation_source
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def account_aggregation_sources(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnConfigurationAggregator.AccountAggregationSourceProperty]]]]:
        '''Provides a list of source accounts and regions to be aggregated.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationaggregator.html#cfn-config-configurationaggregator-accountaggregationsources
        '''
        result = self._values.get("account_aggregation_sources")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnConfigurationAggregator.AccountAggregationSourceProperty]]]], result)

    @builtins.property
    def configuration_aggregator_name(self) -> typing.Optional[builtins.str]:
        '''The name of the aggregator.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationaggregator.html#cfn-config-configurationaggregator-configurationaggregatorname
        '''
        result = self._values.get("configuration_aggregator_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def organization_aggregation_source(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnConfigurationAggregator.OrganizationAggregationSourceProperty]]:
        '''Provides an organization and list of regions to be aggregated.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationaggregator.html#cfn-config-configurationaggregator-organizationaggregationsource
        '''
        result = self._values.get("organization_aggregation_source")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnConfigurationAggregator.OrganizationAggregationSourceProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]]:
        '''An array of tag object.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationaggregator.html#cfn-config-configurationaggregator-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConfigurationAggregatorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnConfigurationRecorder(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-config.CfnConfigurationRecorder",
):
    '''A CloudFormation ``AWS::Config::ConfigurationRecorder``.

    The AWS::Config::ConfigurationRecorder resource describes the AWS resource types for which AWS Config records configuration changes. The configuration recorder stores the configurations of the supported resources in your account as configuration items.
    .. epigraph::

       To enable AWS Config , you must create a configuration recorder and a delivery channel. AWS Config uses the delivery channel to deliver the configuration changes to your Amazon S3 bucket or Amazon SNS topic. For more information, see `AWS::Config::DeliveryChannel <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html>`_ .

    AWS CloudFormation starts the recorder as soon as the delivery channel is available.

    To stop the recorder and delete it, delete the configuration recorder from your stack. To stop the recorder without deleting it, call the `StopConfigurationRecorder <https://docs.aws.amazon.com/config/latest/APIReference/API_StopConfigurationRecorder.html>`_ action of the AWS Config API directly.

    For more information, see `Configuration Recorder <https://docs.aws.amazon.com/config/latest/developerguide/config-concepts.html#config-recorder>`_ in the AWS Config Developer Guide.

    :cloudformationResource: AWS::Config::ConfigurationRecorder
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationrecorder.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_config as config
        
        cfn_configuration_recorder = config.CfnConfigurationRecorder(self, "MyCfnConfigurationRecorder",
            role_arn="roleArn",
        
            # the properties below are optional
            name="name",
            recording_group=config.CfnConfigurationRecorder.RecordingGroupProperty(
                all_supported=False,
                include_global_resource_types=False,
                resource_types=["resourceTypes"]
            )
        )
    '''

    def __init__(
        self,
        scope: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        role_arn: builtins.str,
        name: typing.Optional[builtins.str] = None,
        recording_group: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnConfigurationRecorder.RecordingGroupProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Config::ConfigurationRecorder``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param role_arn: The Amazon Resource Name (ARN) of the IAM (IAM) role that is used to make read or write requests to the delivery channel that you specify and to get configuration details for supported AWS resources. For more information, see `Permissions for the IAM Role Assigned <https://docs.aws.amazon.com/config/latest/developerguide/iamrole-permissions.html>`_ to AWS Config in the AWS Config Developer Guide.
        :param name: A name for the configuration recorder. If you don't specify a name, AWS CloudFormation CloudFormation generates a unique physical ID and uses that ID for the configuration recorder name. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ . .. epigraph:: After you create a configuration recorder, you cannot rename it. If you don't want a name that AWS CloudFormation generates, specify a value for this property. Updates are not supported.
        :param recording_group: Indicates whether to record configurations for all supported resources or for a list of resource types. The resource types that you list must be supported by AWS Config .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5532e7605ebcf4129b4b1bebab2aa17aef32722b46fd205d4f12d12f94f27a10)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConfigurationRecorderProps(
            role_arn=role_arn, name=name, recording_group=recording_group
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f69f7390ca248e9f9e0a7cbf22d8438d3c1f271da3643fbc76d44ef4e419021f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__16f03b1cbae4a38781613771e4362b1938da0a82c0b81e04e47e6c1e7725dcd4)
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
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM (IAM) role that is used to make read or write requests to the delivery channel that you specify and to get configuration details for supported AWS resources.

        For more information, see `Permissions for the IAM Role Assigned <https://docs.aws.amazon.com/config/latest/developerguide/iamrole-permissions.html>`_ to AWS Config in the AWS Config Developer Guide.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationrecorder.html#cfn-config-configurationrecorder-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c325dc0dd3b3ee7e0baa17a07fecbe4fd908a5d89488b64eb7ce7fc909be1ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''A name for the configuration recorder.

        If you don't specify a name, AWS CloudFormation CloudFormation generates a unique physical ID and uses that ID for the configuration recorder name. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ .
        .. epigraph::

           After you create a configuration recorder, you cannot rename it. If you don't want a name that AWS CloudFormation generates, specify a value for this property.

        Updates are not supported.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationrecorder.html#cfn-config-configurationrecorder-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80bb9afa0c20fd9088664b082f366aa41647e32a01232ae00deffea238d53be7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="recordingGroup")
    def recording_group(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnConfigurationRecorder.RecordingGroupProperty"]]:
        '''Indicates whether to record configurations for all supported resources or for a list of resource types.

        The resource types that you list must be supported by AWS Config .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationrecorder.html#cfn-config-configurationrecorder-recordinggroup
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnConfigurationRecorder.RecordingGroupProperty"]], jsii.get(self, "recordingGroup"))

    @recording_group.setter
    def recording_group(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnConfigurationRecorder.RecordingGroupProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9018fa3a443fd91e5137c6613c147e9456d9475f934d02fc188272b54ce6df62)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordingGroup", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-config.CfnConfigurationRecorder.RecordingGroupProperty",
        jsii_struct_bases=[],
        name_mapping={
            "all_supported": "allSupported",
            "include_global_resource_types": "includeGlobalResourceTypes",
            "resource_types": "resourceTypes",
        },
    )
    class RecordingGroupProperty:
        def __init__(
            self,
            *,
            all_supported: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            include_global_resource_types: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            resource_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Specifies which AWS resource types AWS Config records for configuration changes.

            In the recording group, you specify whether you want to record all supported resource types or only specific types of resources.

            By default, AWS Config records the configuration changes for all supported types of *regional resources* that AWS Config discovers in the region in which it is running. Regional resources are tied to a region and can be used only in that region. Examples of regional resources are EC2 instances and EBS volumes.

            You can also have AWS Config record supported types of *global resources* . Global resources are not tied to a specific region and can be used in all regions. The global resource types that AWS Config supports include IAM users, groups, roles, and customer managed policies.
            .. epigraph::

               Global resource types onboarded to AWS Config recording after February 2022 will only be recorded in the service's home region for the commercial partition and AWS GovCloud (US) West for the GovCloud partition. You can view the Configuration Items for these new global resource types only in their home region and AWS GovCloud (US) West.

               Supported global resource types onboarded before February 2022 such as ``AWS::IAM::Group`` , ``AWS::IAM::Policy`` , ``AWS::IAM::Role`` , ``AWS::IAM::User`` remain unchanged, and they will continue to deliver Configuration Items in all supported regions in AWS Config . The change will only affect new global resource types onboarded after February 2022.

               To record global resource types onboarded after February 2022, enable All Supported Resource Types in the home region of the global resource type you want to record.

            If you don't want AWS Config to record all resources, you can specify which types of resources it will record with the ``resourceTypes`` parameter.

            For a list of supported resource types, see `Supported Resource Types <https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html#supported-resources>`_ .

            For more information and a table of the Home Regions for Global Resource Types Onboarded after February 2022, see `Selecting Which Resources AWS Config Records <https://docs.aws.amazon.com/config/latest/developerguide/select-resources.html>`_ .

            :param all_supported: Specifies whether AWS Config records configuration changes for every supported type of regional resource. If you set this option to ``true`` , when AWS Config adds support for a new type of regional resource, it starts recording resources of that type automatically. If you set this option to ``true`` , you cannot enumerate a list of ``resourceTypes`` .
            :param include_global_resource_types: Specifies whether AWS Config includes all supported types of global resources (for example, IAM resources) with the resources that it records. Before you can set this option to ``true`` , you must set the ``AllSupported`` option to ``true`` . If you set this option to ``true`` , when AWS Config adds support for a new type of global resource, it starts recording resources of that type automatically. The configuration details for any global resource are the same in all regions. To prevent duplicate configuration items, you should consider customizing AWS Config in only one region to record global resources.
            :param resource_types: A comma-separated list that specifies the types of AWS resources for which AWS Config records configuration changes (for example, ``AWS::EC2::Instance`` or ``AWS::CloudTrail::Trail`` ). To record all configuration changes, you must set the ``AllSupported`` option to ``false`` . If you set this option to ``true`` , when AWS Config adds support for a new type of resource, it will not record resources of that type unless you manually add that type to your recording group. For a list of valid ``resourceTypes`` values, see the *resourceType Value* column in `Supported AWS Resource Types <https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html#supported-resources>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordinggroup.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_config as config
                
                recording_group_property = config.CfnConfigurationRecorder.RecordingGroupProperty(
                    all_supported=False,
                    include_global_resource_types=False,
                    resource_types=["resourceTypes"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8ad79dedcd0640bedf2de2b275b03fcb48bd1d8f729c854c64c81a5b23ecf7cc)
                check_type(argname="argument all_supported", value=all_supported, expected_type=type_hints["all_supported"])
                check_type(argname="argument include_global_resource_types", value=include_global_resource_types, expected_type=type_hints["include_global_resource_types"])
                check_type(argname="argument resource_types", value=resource_types, expected_type=type_hints["resource_types"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if all_supported is not None:
                self._values["all_supported"] = all_supported
            if include_global_resource_types is not None:
                self._values["include_global_resource_types"] = include_global_resource_types
            if resource_types is not None:
                self._values["resource_types"] = resource_types

        @builtins.property
        def all_supported(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''Specifies whether AWS Config records configuration changes for every supported type of regional resource.

            If you set this option to ``true`` , when AWS Config adds support for a new type of regional resource, it starts recording resources of that type automatically.

            If you set this option to ``true`` , you cannot enumerate a list of ``resourceTypes`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordinggroup.html#cfn-config-configurationrecorder-recordinggroup-allsupported
            '''
            result = self._values.get("all_supported")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def include_global_resource_types(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''Specifies whether AWS Config includes all supported types of global resources (for example, IAM resources) with the resources that it records.

            Before you can set this option to ``true`` , you must set the ``AllSupported`` option to ``true`` .

            If you set this option to ``true`` , when AWS Config adds support for a new type of global resource, it starts recording resources of that type automatically.

            The configuration details for any global resource are the same in all regions. To prevent duplicate configuration items, you should consider customizing AWS Config in only one region to record global resources.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordinggroup.html#cfn-config-configurationrecorder-recordinggroup-includeglobalresourcetypes
            '''
            result = self._values.get("include_global_resource_types")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def resource_types(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A comma-separated list that specifies the types of AWS resources for which AWS Config records configuration changes (for example, ``AWS::EC2::Instance`` or ``AWS::CloudTrail::Trail`` ).

            To record all configuration changes, you must set the ``AllSupported`` option to ``false`` .

            If you set this option to ``true`` , when AWS Config adds support for a new type of resource, it will not record resources of that type unless you manually add that type to your recording group.

            For a list of valid ``resourceTypes`` values, see the *resourceType Value* column in `Supported AWS Resource Types <https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html#supported-resources>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordinggroup.html#cfn-config-configurationrecorder-recordinggroup-resourcetypes
            '''
            result = self._values.get("resource_types")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RecordingGroupProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-config.CfnConfigurationRecorderProps",
    jsii_struct_bases=[],
    name_mapping={
        "role_arn": "roleArn",
        "name": "name",
        "recording_group": "recordingGroup",
    },
)
class CfnConfigurationRecorderProps:
    def __init__(
        self,
        *,
        role_arn: builtins.str,
        name: typing.Optional[builtins.str] = None,
        recording_group: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnConfigurationRecorder.RecordingGroupProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnConfigurationRecorder``.

        :param role_arn: The Amazon Resource Name (ARN) of the IAM (IAM) role that is used to make read or write requests to the delivery channel that you specify and to get configuration details for supported AWS resources. For more information, see `Permissions for the IAM Role Assigned <https://docs.aws.amazon.com/config/latest/developerguide/iamrole-permissions.html>`_ to AWS Config in the AWS Config Developer Guide.
        :param name: A name for the configuration recorder. If you don't specify a name, AWS CloudFormation CloudFormation generates a unique physical ID and uses that ID for the configuration recorder name. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ . .. epigraph:: After you create a configuration recorder, you cannot rename it. If you don't want a name that AWS CloudFormation generates, specify a value for this property. Updates are not supported.
        :param recording_group: Indicates whether to record configurations for all supported resources or for a list of resource types. The resource types that you list must be supported by AWS Config .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationrecorder.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_config as config
            
            cfn_configuration_recorder_props = config.CfnConfigurationRecorderProps(
                role_arn="roleArn",
            
                # the properties below are optional
                name="name",
                recording_group=config.CfnConfigurationRecorder.RecordingGroupProperty(
                    all_supported=False,
                    include_global_resource_types=False,
                    resource_types=["resourceTypes"]
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19b40216b605775542336c66e586acbda5bedfeb6e8b98925bc745b3572387f4)
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument recording_group", value=recording_group, expected_type=type_hints["recording_group"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "role_arn": role_arn,
        }
        if name is not None:
            self._values["name"] = name
        if recording_group is not None:
            self._values["recording_group"] = recording_group

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM (IAM) role that is used to make read or write requests to the delivery channel that you specify and to get configuration details for supported AWS resources.

        For more information, see `Permissions for the IAM Role Assigned <https://docs.aws.amazon.com/config/latest/developerguide/iamrole-permissions.html>`_ to AWS Config in the AWS Config Developer Guide.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationrecorder.html#cfn-config-configurationrecorder-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''A name for the configuration recorder.

        If you don't specify a name, AWS CloudFormation CloudFormation generates a unique physical ID and uses that ID for the configuration recorder name. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ .
        .. epigraph::

           After you create a configuration recorder, you cannot rename it. If you don't want a name that AWS CloudFormation generates, specify a value for this property.

        Updates are not supported.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationrecorder.html#cfn-config-configurationrecorder-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def recording_group(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnConfigurationRecorder.RecordingGroupProperty]]:
        '''Indicates whether to record configurations for all supported resources or for a list of resource types.

        The resource types that you list must be supported by AWS Config .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationrecorder.html#cfn-config-configurationrecorder-recordinggroup
        '''
        result = self._values.get("recording_group")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnConfigurationRecorder.RecordingGroupProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConfigurationRecorderProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnConformancePack(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-config.CfnConformancePack",
):
    '''A CloudFormation ``AWS::Config::ConformancePack``.

    A conformance pack is a collection of AWS Config rules and remediation actions that can be easily deployed in an account and a region. ConformancePack creates a service linked role in your account. The service linked role is created only when the role does not exist in your account.

    :cloudformationResource: AWS::Config::ConformancePack
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-conformancepack.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_config as config
        
        # template_ssm_document_details: Any
        
        cfn_conformance_pack = config.CfnConformancePack(self, "MyCfnConformancePack",
            conformance_pack_name="conformancePackName",
        
            # the properties below are optional
            conformance_pack_input_parameters=[config.CfnConformancePack.ConformancePackInputParameterProperty(
                parameter_name="parameterName",
                parameter_value="parameterValue"
            )],
            delivery_s3_bucket="deliveryS3Bucket",
            delivery_s3_key_prefix="deliveryS3KeyPrefix",
            template_body="templateBody",
            template_s3_uri="templateS3Uri",
            template_ssm_document_details=template_ssm_document_details
        )
    '''

    def __init__(
        self,
        scope: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        conformance_pack_name: builtins.str,
        conformance_pack_input_parameters: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnConformancePack.ConformancePackInputParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        delivery_s3_bucket: typing.Optional[builtins.str] = None,
        delivery_s3_key_prefix: typing.Optional[builtins.str] = None,
        template_body: typing.Optional[builtins.str] = None,
        template_s3_uri: typing.Optional[builtins.str] = None,
        template_ssm_document_details: typing.Any = None,
    ) -> None:
        '''Create a new ``AWS::Config::ConformancePack``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param conformance_pack_name: Name of the conformance pack you want to create.
        :param conformance_pack_input_parameters: A list of ConformancePackInputParameter objects.
        :param delivery_s3_bucket: The name of the Amazon S3 bucket where AWS Config stores conformance pack templates.
        :param delivery_s3_key_prefix: The prefix for the Amazon S3 bucket.
        :param template_body: A string containing full conformance pack template body. Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. .. epigraph:: You can only use a YAML template with two resource types: config rule ( ``AWS::Config::ConfigRule`` ) and a remediation action ( ``AWS::Config::RemediationConfiguration`` ).
        :param template_s3_uri: Location of file containing the template body (s3://bucketname/prefix). The uri must point to the conformance pack template (max size: 300 KB) that is located in an Amazon S3 bucket. .. epigraph:: You must have access to read Amazon S3 bucket.
        :param template_ssm_document_details: ``AWS::Config::ConformancePack.TemplateSSMDocumentDetails``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6123f219e2006e6a835f6ff0683647eacebb11ad3246ef196c585a6e0b7221d7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConformancePackProps(
            conformance_pack_name=conformance_pack_name,
            conformance_pack_input_parameters=conformance_pack_input_parameters,
            delivery_s3_bucket=delivery_s3_bucket,
            delivery_s3_key_prefix=delivery_s3_key_prefix,
            template_body=template_body,
            template_s3_uri=template_s3_uri,
            template_ssm_document_details=template_ssm_document_details,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__888b7dbfec248b6535edbfb026169c7701b67e1dbef47ac19de92c5c15323757)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d3a33574e4d15eccc668be41d6ad70d886ad847ce4bc8bb387634dedddab853a)
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
    @jsii.member(jsii_name="conformancePackName")
    def conformance_pack_name(self) -> builtins.str:
        '''Name of the conformance pack you want to create.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-conformancepack.html#cfn-config-conformancepack-conformancepackname
        '''
        return typing.cast(builtins.str, jsii.get(self, "conformancePackName"))

    @conformance_pack_name.setter
    def conformance_pack_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88170d0f3f5c995c8cdf88fbb01b283638631a5ea2e29181b3cca25f0789d55a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "conformancePackName", value)

    @builtins.property
    @jsii.member(jsii_name="templateSsmDocumentDetails")
    def template_ssm_document_details(self) -> typing.Any:
        '''``AWS::Config::ConformancePack.TemplateSSMDocumentDetails``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-conformancepack.html#cfn-config-conformancepack-templatessmdocumentdetails
        '''
        return typing.cast(typing.Any, jsii.get(self, "templateSsmDocumentDetails"))

    @template_ssm_document_details.setter
    def template_ssm_document_details(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f7ac7e9540b1644014ffbeba63453ae38c2df19bdf2b3941330f6d9cabd32f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateSsmDocumentDetails", value)

    @builtins.property
    @jsii.member(jsii_name="conformancePackInputParameters")
    def conformance_pack_input_parameters(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnConformancePack.ConformancePackInputParameterProperty"]]]]:
        '''A list of ConformancePackInputParameter objects.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-conformancepack.html#cfn-config-conformancepack-conformancepackinputparameters
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnConformancePack.ConformancePackInputParameterProperty"]]]], jsii.get(self, "conformancePackInputParameters"))

    @conformance_pack_input_parameters.setter
    def conformance_pack_input_parameters(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnConformancePack.ConformancePackInputParameterProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bcaed2e029220ea94c7a5e93f52cf47324fcc86342f75dd0efca5b6c13ad20c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "conformancePackInputParameters", value)

    @builtins.property
    @jsii.member(jsii_name="deliveryS3Bucket")
    def delivery_s3_bucket(self) -> typing.Optional[builtins.str]:
        '''The name of the Amazon S3 bucket where AWS Config stores conformance pack templates.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-conformancepack.html#cfn-config-conformancepack-deliverys3bucket
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deliveryS3Bucket"))

    @delivery_s3_bucket.setter
    def delivery_s3_bucket(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd383f517904444571092513732623fcb488cd27f51875edfa0d0d9103be8f8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deliveryS3Bucket", value)

    @builtins.property
    @jsii.member(jsii_name="deliveryS3KeyPrefix")
    def delivery_s3_key_prefix(self) -> typing.Optional[builtins.str]:
        '''The prefix for the Amazon S3 bucket.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-conformancepack.html#cfn-config-conformancepack-deliverys3keyprefix
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deliveryS3KeyPrefix"))

    @delivery_s3_key_prefix.setter
    def delivery_s3_key_prefix(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__265056adaa136193224fb5d95b0845856d6eb3c469b59d22f8451ce84a314153)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deliveryS3KeyPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="templateBody")
    def template_body(self) -> typing.Optional[builtins.str]:
        '''A string containing full conformance pack template body.

        Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes.
        .. epigraph::

           You can only use a YAML template with two resource types: config rule ( ``AWS::Config::ConfigRule`` ) and a remediation action ( ``AWS::Config::RemediationConfiguration`` ).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-conformancepack.html#cfn-config-conformancepack-templatebody
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateBody"))

    @template_body.setter
    def template_body(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12dfd58bc90197bddd9eaa402abb3fc01d3d97e625d35c9e658564dc58190b02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateBody", value)

    @builtins.property
    @jsii.member(jsii_name="templateS3Uri")
    def template_s3_uri(self) -> typing.Optional[builtins.str]:
        '''Location of file containing the template body (s3://bucketname/prefix).

        The uri must point to the conformance pack template (max size: 300 KB) that is located in an Amazon S3 bucket.
        .. epigraph::

           You must have access to read Amazon S3 bucket.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-conformancepack.html#cfn-config-conformancepack-templates3uri
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateS3Uri"))

    @template_s3_uri.setter
    def template_s3_uri(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a19e9cf2f941cf7f00deea78e516e49cc26eab7b78191d5b950054eba7e4e08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateS3Uri", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-config.CfnConformancePack.ConformancePackInputParameterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "parameter_name": "parameterName",
            "parameter_value": "parameterValue",
        },
    )
    class ConformancePackInputParameterProperty:
        def __init__(
            self,
            *,
            parameter_name: builtins.str,
            parameter_value: builtins.str,
        ) -> None:
            '''Input parameters in the form of key-value pairs for the conformance pack, both of which you define.

            Keys can have a maximum character length of 255 characters, and values can have a maximum length of 4096 characters.

            :param parameter_name: One part of a key-value pair.
            :param parameter_value: Another part of the key-value pair.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-conformancepack-conformancepackinputparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_config as config
                
                conformance_pack_input_parameter_property = config.CfnConformancePack.ConformancePackInputParameterProperty(
                    parameter_name="parameterName",
                    parameter_value="parameterValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6c4bcb70dd1952e4df06b1fbed9981a1eb9f543f8ad4ecdbaf0de8f0fd504f40)
                check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
                check_type(argname="argument parameter_value", value=parameter_value, expected_type=type_hints["parameter_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "parameter_name": parameter_name,
                "parameter_value": parameter_value,
            }

        @builtins.property
        def parameter_name(self) -> builtins.str:
            '''One part of a key-value pair.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-conformancepack-conformancepackinputparameter.html#cfn-config-conformancepack-conformancepackinputparameter-parametername
            '''
            result = self._values.get("parameter_name")
            assert result is not None, "Required property 'parameter_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def parameter_value(self) -> builtins.str:
            '''Another part of the key-value pair.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-conformancepack-conformancepackinputparameter.html#cfn-config-conformancepack-conformancepackinputparameter-parametervalue
            '''
            result = self._values.get("parameter_value")
            assert result is not None, "Required property 'parameter_value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConformancePackInputParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-config.CfnConformancePack.TemplateSSMDocumentDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "document_name": "documentName",
            "document_version": "documentVersion",
        },
    )
    class TemplateSSMDocumentDetailsProperty:
        def __init__(
            self,
            *,
            document_name: typing.Optional[builtins.str] = None,
            document_version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''This API allows you to create a conformance pack template with an AWS Systems Manager document (SSM document).

            To deploy a conformance pack using an SSM document, first create an SSM document with conformance pack content, and then provide the ``DocumentName`` in the `PutConformancePack API <https://docs.aws.amazon.com/config/latest/APIReference/API_PutConformancePack.html>`_ . You can also provide the ``DocumentVersion`` .

            The ``TemplateSSMDocumentDetails`` object contains the name of the SSM document and the version of the SSM document.

            :param document_name: The name or Amazon Resource Name (ARN) of the SSM document to use to create a conformance pack. If you use the document name, AWS Config checks only your account and AWS Region for the SSM document. If you want to use an SSM document from another Region or account, you must provide the ARN.
            :param document_version: The version of the SSM document to use to create a conformance pack. By default, AWS Config uses the latest version. .. epigraph:: This field is optional.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-conformancepack-templatessmdocumentdetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_config as config
                
                template_sSMDocument_details_property = config.CfnConformancePack.TemplateSSMDocumentDetailsProperty(
                    document_name="documentName",
                    document_version="documentVersion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3c05dff23f0e3f4b96f068c119fa148dc0e3196da539a8ba7ba201e4438f6f1a)
                check_type(argname="argument document_name", value=document_name, expected_type=type_hints["document_name"])
                check_type(argname="argument document_version", value=document_version, expected_type=type_hints["document_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if document_name is not None:
                self._values["document_name"] = document_name
            if document_version is not None:
                self._values["document_version"] = document_version

        @builtins.property
        def document_name(self) -> typing.Optional[builtins.str]:
            '''The name or Amazon Resource Name (ARN) of the SSM document to use to create a conformance pack.

            If you use the document name, AWS Config checks only your account and AWS Region for the SSM document. If you want to use an SSM document from another Region or account, you must provide the ARN.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-conformancepack-templatessmdocumentdetails.html#cfn-config-conformancepack-templatessmdocumentdetails-documentname
            '''
            result = self._values.get("document_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def document_version(self) -> typing.Optional[builtins.str]:
            '''The version of the SSM document to use to create a conformance pack.

            By default, AWS Config uses the latest version.
            .. epigraph::

               This field is optional.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-conformancepack-templatessmdocumentdetails.html#cfn-config-conformancepack-templatessmdocumentdetails-documentversion
            '''
            result = self._values.get("document_version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TemplateSSMDocumentDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-config.CfnConformancePackProps",
    jsii_struct_bases=[],
    name_mapping={
        "conformance_pack_name": "conformancePackName",
        "conformance_pack_input_parameters": "conformancePackInputParameters",
        "delivery_s3_bucket": "deliveryS3Bucket",
        "delivery_s3_key_prefix": "deliveryS3KeyPrefix",
        "template_body": "templateBody",
        "template_s3_uri": "templateS3Uri",
        "template_ssm_document_details": "templateSsmDocumentDetails",
    },
)
class CfnConformancePackProps:
    def __init__(
        self,
        *,
        conformance_pack_name: builtins.str,
        conformance_pack_input_parameters: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnConformancePack.ConformancePackInputParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        delivery_s3_bucket: typing.Optional[builtins.str] = None,
        delivery_s3_key_prefix: typing.Optional[builtins.str] = None,
        template_body: typing.Optional[builtins.str] = None,
        template_s3_uri: typing.Optional[builtins.str] = None,
        template_ssm_document_details: typing.Any = None,
    ) -> None:
        '''Properties for defining a ``CfnConformancePack``.

        :param conformance_pack_name: Name of the conformance pack you want to create.
        :param conformance_pack_input_parameters: A list of ConformancePackInputParameter objects.
        :param delivery_s3_bucket: The name of the Amazon S3 bucket where AWS Config stores conformance pack templates.
        :param delivery_s3_key_prefix: The prefix for the Amazon S3 bucket.
        :param template_body: A string containing full conformance pack template body. Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. .. epigraph:: You can only use a YAML template with two resource types: config rule ( ``AWS::Config::ConfigRule`` ) and a remediation action ( ``AWS::Config::RemediationConfiguration`` ).
        :param template_s3_uri: Location of file containing the template body (s3://bucketname/prefix). The uri must point to the conformance pack template (max size: 300 KB) that is located in an Amazon S3 bucket. .. epigraph:: You must have access to read Amazon S3 bucket.
        :param template_ssm_document_details: ``AWS::Config::ConformancePack.TemplateSSMDocumentDetails``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-conformancepack.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_config as config
            
            # template_ssm_document_details: Any
            
            cfn_conformance_pack_props = config.CfnConformancePackProps(
                conformance_pack_name="conformancePackName",
            
                # the properties below are optional
                conformance_pack_input_parameters=[config.CfnConformancePack.ConformancePackInputParameterProperty(
                    parameter_name="parameterName",
                    parameter_value="parameterValue"
                )],
                delivery_s3_bucket="deliveryS3Bucket",
                delivery_s3_key_prefix="deliveryS3KeyPrefix",
                template_body="templateBody",
                template_s3_uri="templateS3Uri",
                template_ssm_document_details=template_ssm_document_details
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c468477deaceeaedd7116aee03f37a7ce2e3183150dae370e43ffd361961133)
            check_type(argname="argument conformance_pack_name", value=conformance_pack_name, expected_type=type_hints["conformance_pack_name"])
            check_type(argname="argument conformance_pack_input_parameters", value=conformance_pack_input_parameters, expected_type=type_hints["conformance_pack_input_parameters"])
            check_type(argname="argument delivery_s3_bucket", value=delivery_s3_bucket, expected_type=type_hints["delivery_s3_bucket"])
            check_type(argname="argument delivery_s3_key_prefix", value=delivery_s3_key_prefix, expected_type=type_hints["delivery_s3_key_prefix"])
            check_type(argname="argument template_body", value=template_body, expected_type=type_hints["template_body"])
            check_type(argname="argument template_s3_uri", value=template_s3_uri, expected_type=type_hints["template_s3_uri"])
            check_type(argname="argument template_ssm_document_details", value=template_ssm_document_details, expected_type=type_hints["template_ssm_document_details"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "conformance_pack_name": conformance_pack_name,
        }
        if conformance_pack_input_parameters is not None:
            self._values["conformance_pack_input_parameters"] = conformance_pack_input_parameters
        if delivery_s3_bucket is not None:
            self._values["delivery_s3_bucket"] = delivery_s3_bucket
        if delivery_s3_key_prefix is not None:
            self._values["delivery_s3_key_prefix"] = delivery_s3_key_prefix
        if template_body is not None:
            self._values["template_body"] = template_body
        if template_s3_uri is not None:
            self._values["template_s3_uri"] = template_s3_uri
        if template_ssm_document_details is not None:
            self._values["template_ssm_document_details"] = template_ssm_document_details

    @builtins.property
    def conformance_pack_name(self) -> builtins.str:
        '''Name of the conformance pack you want to create.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-conformancepack.html#cfn-config-conformancepack-conformancepackname
        '''
        result = self._values.get("conformance_pack_name")
        assert result is not None, "Required property 'conformance_pack_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def conformance_pack_input_parameters(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnConformancePack.ConformancePackInputParameterProperty]]]]:
        '''A list of ConformancePackInputParameter objects.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-conformancepack.html#cfn-config-conformancepack-conformancepackinputparameters
        '''
        result = self._values.get("conformance_pack_input_parameters")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnConformancePack.ConformancePackInputParameterProperty]]]], result)

    @builtins.property
    def delivery_s3_bucket(self) -> typing.Optional[builtins.str]:
        '''The name of the Amazon S3 bucket where AWS Config stores conformance pack templates.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-conformancepack.html#cfn-config-conformancepack-deliverys3bucket
        '''
        result = self._values.get("delivery_s3_bucket")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delivery_s3_key_prefix(self) -> typing.Optional[builtins.str]:
        '''The prefix for the Amazon S3 bucket.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-conformancepack.html#cfn-config-conformancepack-deliverys3keyprefix
        '''
        result = self._values.get("delivery_s3_key_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def template_body(self) -> typing.Optional[builtins.str]:
        '''A string containing full conformance pack template body.

        Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes.
        .. epigraph::

           You can only use a YAML template with two resource types: config rule ( ``AWS::Config::ConfigRule`` ) and a remediation action ( ``AWS::Config::RemediationConfiguration`` ).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-conformancepack.html#cfn-config-conformancepack-templatebody
        '''
        result = self._values.get("template_body")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def template_s3_uri(self) -> typing.Optional[builtins.str]:
        '''Location of file containing the template body (s3://bucketname/prefix).

        The uri must point to the conformance pack template (max size: 300 KB) that is located in an Amazon S3 bucket.
        .. epigraph::

           You must have access to read Amazon S3 bucket.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-conformancepack.html#cfn-config-conformancepack-templates3uri
        '''
        result = self._values.get("template_s3_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def template_ssm_document_details(self) -> typing.Any:
        '''``AWS::Config::ConformancePack.TemplateSSMDocumentDetails``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-conformancepack.html#cfn-config-conformancepack-templatessmdocumentdetails
        '''
        result = self._values.get("template_ssm_document_details")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConformancePackProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnDeliveryChannel(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-config.CfnDeliveryChannel",
):
    '''A CloudFormation ``AWS::Config::DeliveryChannel``.

    Specifies a delivery channel object to deliver configuration information to an Amazon S3 bucket and Amazon SNS topic.

    Before you can create a delivery channel, you must create a configuration recorder. You can use this action to change the Amazon S3 bucket or an Amazon SNS topic of the existing delivery channel. To change the Amazon S3 bucket or an Amazon SNS topic, call this action and specify the changed values for the S3 bucket and the SNS topic. If you specify a different value for either the S3 bucket or the SNS topic, this action will keep the existing value for the parameter that is not changed.
    .. epigraph::

       In the China (Beijing) Region, when you call this action, the Amazon S3 bucket must also be in the China (Beijing) Region. In all the other regions, AWS Config supports cross-region and cross-account delivery channels.

    You can have only one delivery channel per region per AWS account, and the delivery channel is required to use AWS Config .
    .. epigraph::

       AWS Config does not support the delivery channel to an Amazon S3 bucket bucket where object lock is enabled. For more information, see `How S3 Object Lock works <https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-overview.html>`_ .

    When you create the delivery channel, you can specify; how often AWS Config delivers configuration snapshots to your Amazon S3 bucket (for example, 24 hours), the S3 bucket to which AWS Config sends configuration snapshots and configuration history files, and the Amazon SNS topic to which AWS Config sends notifications about configuration changes, such as updated resources, AWS Config rule evaluations, and when AWS Config delivers the configuration snapshot to your S3 bucket. For more information, see `Deliver Configuration Items <https://docs.aws.amazon.com/config/latest/developerguide/how-does-config-work.html#delivery-channel>`_ in the AWS Config Developer Guide.
    .. epigraph::

       To enable AWS Config , you must create a configuration recorder and a delivery channel. If you want to create the resources separately, you must create a configuration recorder before you can create a delivery channel. AWS Config uses the configuration recorder to capture configuration changes to your resources. For more information, see `AWS::Config::ConfigurationRecorder <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationrecorder.html>`_ .

    For more information, see `Managing the Delivery Channel <https://docs.aws.amazon.com/config/latest/developerguide/manage-delivery-channel.html>`_ in the AWS Config Developer Guide.

    :cloudformationResource: AWS::Config::DeliveryChannel
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_config as config
        
        cfn_delivery_channel = config.CfnDeliveryChannel(self, "MyCfnDeliveryChannel",
            s3_bucket_name="s3BucketName",
        
            # the properties below are optional
            config_snapshot_delivery_properties=config.CfnDeliveryChannel.ConfigSnapshotDeliveryPropertiesProperty(
                delivery_frequency="deliveryFrequency"
            ),
            name="name",
            s3_key_prefix="s3KeyPrefix",
            s3_kms_key_arn="s3KmsKeyArn",
            sns_topic_arn="snsTopicArn"
        )
    '''

    def __init__(
        self,
        scope: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        s3_bucket_name: builtins.str,
        config_snapshot_delivery_properties: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDeliveryChannel.ConfigSnapshotDeliveryPropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        s3_key_prefix: typing.Optional[builtins.str] = None,
        s3_kms_key_arn: typing.Optional[builtins.str] = None,
        sns_topic_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Config::DeliveryChannel``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param s3_bucket_name: The name of the Amazon S3 bucket to which AWS Config delivers configuration snapshots and configuration history files. If you specify a bucket that belongs to another AWS account , that bucket must have policies that grant access permissions to AWS Config . For more information, see `Permissions for the Amazon S3 Bucket <https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-policy.html>`_ in the *AWS Config Developer Guide* .
        :param config_snapshot_delivery_properties: The options for how often AWS Config delivers configuration snapshots to the Amazon S3 bucket.
        :param name: A name for the delivery channel. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the delivery channel name. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ . Updates are not supported. To change the name, you must run two separate updates. In the first update, delete this resource, and then recreate it with a new name in the second update.
        :param s3_key_prefix: The prefix for the specified Amazon S3 bucket.
        :param s3_kms_key_arn: The Amazon Resource Name (ARN) of the AWS Key Management Service ( AWS KMS ) AWS KMS key (KMS key) used to encrypt objects delivered by AWS Config . Must belong to the same Region as the destination S3 bucket.
        :param sns_topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic to which AWS Config sends notifications about configuration changes. If you choose a topic from another account, the topic must have policies that grant access permissions to AWS Config . For more information, see `Permissions for the Amazon SNS Topic <https://docs.aws.amazon.com/config/latest/developerguide/sns-topic-policy.html>`_ in the *AWS Config Developer Guide* .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8503fca266122c009084fee38132ec508c1ee988de9b01ba62411d1ae9dfe16d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDeliveryChannelProps(
            s3_bucket_name=s3_bucket_name,
            config_snapshot_delivery_properties=config_snapshot_delivery_properties,
            name=name,
            s3_key_prefix=s3_key_prefix,
            s3_kms_key_arn=s3_kms_key_arn,
            sns_topic_arn=sns_topic_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bc784826c9be5853c9d29de9a4c1161ea4e8e938a31566fa616bc92ccbed8fe)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6a43f11103336b602266a7d05b2954a590113fe185f1b9af4d33f4f23ebabc02)
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
    @jsii.member(jsii_name="s3BucketName")
    def s3_bucket_name(self) -> builtins.str:
        '''The name of the Amazon S3 bucket to which AWS Config delivers configuration snapshots and configuration history files.

        If you specify a bucket that belongs to another AWS account , that bucket must have policies that grant access permissions to AWS Config . For more information, see `Permissions for the Amazon S3 Bucket <https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-policy.html>`_ in the *AWS Config Developer Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-s3bucketname
        '''
        return typing.cast(builtins.str, jsii.get(self, "s3BucketName"))

    @s3_bucket_name.setter
    def s3_bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f490e7999afdc9d4cca032ea5e9c6ab33bc3e954c19f65ea41f23bd3b4155aeb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3BucketName", value)

    @builtins.property
    @jsii.member(jsii_name="configSnapshotDeliveryProperties")
    def config_snapshot_delivery_properties(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDeliveryChannel.ConfigSnapshotDeliveryPropertiesProperty"]]:
        '''The options for how often AWS Config delivers configuration snapshots to the Amazon S3 bucket.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-configsnapshotdeliveryproperties
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDeliveryChannel.ConfigSnapshotDeliveryPropertiesProperty"]], jsii.get(self, "configSnapshotDeliveryProperties"))

    @config_snapshot_delivery_properties.setter
    def config_snapshot_delivery_properties(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDeliveryChannel.ConfigSnapshotDeliveryPropertiesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__689eb2e0300c97079b93eb02a656ac27b9541852f3429108ff47c0c67a535938)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configSnapshotDeliveryProperties", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''A name for the delivery channel.

        If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the delivery channel name. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ .

        Updates are not supported. To change the name, you must run two separate updates. In the first update, delete this resource, and then recreate it with a new name in the second update.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ac8b13595a2aa4848daadda34a1e07813ca0a12e4252017cff58b25fe04df24)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="s3KeyPrefix")
    def s3_key_prefix(self) -> typing.Optional[builtins.str]:
        '''The prefix for the specified Amazon S3 bucket.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-s3keyprefix
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3KeyPrefix"))

    @s3_key_prefix.setter
    def s3_key_prefix(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0f7c0158b61d88c369b351f47c2ead21485eaa959b849e60fae2be2f6c90718)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3KeyPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="s3KmsKeyArn")
    def s3_kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the AWS Key Management Service ( AWS KMS ) AWS KMS key (KMS key) used to encrypt objects delivered by AWS Config .

        Must belong to the same Region as the destination S3 bucket.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-s3kmskeyarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3KmsKeyArn"))

    @s3_kms_key_arn.setter
    def s3_kms_key_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc5e1cbfac10a9e52d0144d5ec59962b2ccb87bb83eb1880da5045abc6d56e4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3KmsKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="snsTopicArn")
    def sns_topic_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the Amazon SNS topic to which AWS Config sends notifications about configuration changes.

        If you choose a topic from another account, the topic must have policies that grant access permissions to AWS Config . For more information, see `Permissions for the Amazon SNS Topic <https://docs.aws.amazon.com/config/latest/developerguide/sns-topic-policy.html>`_ in the *AWS Config Developer Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-snstopicarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snsTopicArn"))

    @sns_topic_arn.setter
    def sns_topic_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f33d70a9ba07df1effc7044f94ba092c7c42e6b5e3bead29d4b3e34b032230a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snsTopicArn", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-config.CfnDeliveryChannel.ConfigSnapshotDeliveryPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"delivery_frequency": "deliveryFrequency"},
    )
    class ConfigSnapshotDeliveryPropertiesProperty:
        def __init__(
            self,
            *,
            delivery_frequency: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides options for how often AWS Config delivers configuration snapshots to the Amazon S3 bucket in your delivery channel.

            .. epigraph::

               If you want to create a rule that triggers evaluations for your resources when AWS Config delivers the configuration snapshot, see the following:

            The frequency for a rule that triggers evaluations for your resources when AWS Config delivers the configuration snapshot is set by one of two values, depending on which is less frequent:

            - The value for the ``deliveryFrequency`` parameter within the delivery channel configuration, which sets how often AWS Config delivers configuration snapshots. This value also sets how often AWS Config invokes evaluations for AWS Config rules.
            - The value for the ``MaximumExecutionFrequency`` parameter, which sets the maximum frequency with which AWS Config invokes evaluations for the rule. For more information, see `ConfigRule <https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigRule.html>`_ .

            If the ``deliveryFrequency`` value is less frequent than the ``MaximumExecutionFrequency`` value for a rule, AWS Config invokes the rule only as often as the ``deliveryFrequency`` value.

            - For example, you want your rule to run evaluations when AWS Config delivers the configuration snapshot.
            - You specify the ``MaximumExecutionFrequency`` value for ``Six_Hours`` .
            - You then specify the delivery channel ``deliveryFrequency`` value for ``TwentyFour_Hours`` .
            - Because the value for ``deliveryFrequency`` is less frequent than ``MaximumExecutionFrequency`` , AWS Config invokes evaluations for the rule every 24 hours.

            You should set the ``MaximumExecutionFrequency`` value to be at least as frequent as the ``deliveryFrequency`` value. You can view the ``deliveryFrequency`` value by using the ``DescribeDeliveryChannnels`` action.

            To update the ``deliveryFrequency`` with which AWS Config delivers your configuration snapshots, use the ``PutDeliveryChannel`` action.

            :param delivery_frequency: The frequency with which AWS Config delivers configuration snapshots.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-deliverychannel-configsnapshotdeliveryproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_config as config
                
                config_snapshot_delivery_properties_property = config.CfnDeliveryChannel.ConfigSnapshotDeliveryPropertiesProperty(
                    delivery_frequency="deliveryFrequency"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5efc3c228622d3e345810794f186238d4f1c0cd7a9c6ac447802f3557a5ec86a)
                check_type(argname="argument delivery_frequency", value=delivery_frequency, expected_type=type_hints["delivery_frequency"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if delivery_frequency is not None:
                self._values["delivery_frequency"] = delivery_frequency

        @builtins.property
        def delivery_frequency(self) -> typing.Optional[builtins.str]:
            '''The frequency with which AWS Config delivers configuration snapshots.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-deliverychannel-configsnapshotdeliveryproperties.html#cfn-config-deliverychannel-configsnapshotdeliveryproperties-deliveryfrequency
            '''
            result = self._values.get("delivery_frequency")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfigSnapshotDeliveryPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-config.CfnDeliveryChannelProps",
    jsii_struct_bases=[],
    name_mapping={
        "s3_bucket_name": "s3BucketName",
        "config_snapshot_delivery_properties": "configSnapshotDeliveryProperties",
        "name": "name",
        "s3_key_prefix": "s3KeyPrefix",
        "s3_kms_key_arn": "s3KmsKeyArn",
        "sns_topic_arn": "snsTopicArn",
    },
)
class CfnDeliveryChannelProps:
    def __init__(
        self,
        *,
        s3_bucket_name: builtins.str,
        config_snapshot_delivery_properties: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDeliveryChannel.ConfigSnapshotDeliveryPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        s3_key_prefix: typing.Optional[builtins.str] = None,
        s3_kms_key_arn: typing.Optional[builtins.str] = None,
        sns_topic_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnDeliveryChannel``.

        :param s3_bucket_name: The name of the Amazon S3 bucket to which AWS Config delivers configuration snapshots and configuration history files. If you specify a bucket that belongs to another AWS account , that bucket must have policies that grant access permissions to AWS Config . For more information, see `Permissions for the Amazon S3 Bucket <https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-policy.html>`_ in the *AWS Config Developer Guide* .
        :param config_snapshot_delivery_properties: The options for how often AWS Config delivers configuration snapshots to the Amazon S3 bucket.
        :param name: A name for the delivery channel. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the delivery channel name. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ . Updates are not supported. To change the name, you must run two separate updates. In the first update, delete this resource, and then recreate it with a new name in the second update.
        :param s3_key_prefix: The prefix for the specified Amazon S3 bucket.
        :param s3_kms_key_arn: The Amazon Resource Name (ARN) of the AWS Key Management Service ( AWS KMS ) AWS KMS key (KMS key) used to encrypt objects delivered by AWS Config . Must belong to the same Region as the destination S3 bucket.
        :param sns_topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic to which AWS Config sends notifications about configuration changes. If you choose a topic from another account, the topic must have policies that grant access permissions to AWS Config . For more information, see `Permissions for the Amazon SNS Topic <https://docs.aws.amazon.com/config/latest/developerguide/sns-topic-policy.html>`_ in the *AWS Config Developer Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_config as config
            
            cfn_delivery_channel_props = config.CfnDeliveryChannelProps(
                s3_bucket_name="s3BucketName",
            
                # the properties below are optional
                config_snapshot_delivery_properties=config.CfnDeliveryChannel.ConfigSnapshotDeliveryPropertiesProperty(
                    delivery_frequency="deliveryFrequency"
                ),
                name="name",
                s3_key_prefix="s3KeyPrefix",
                s3_kms_key_arn="s3KmsKeyArn",
                sns_topic_arn="snsTopicArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__392b246527bdbb83ef04a19cc7335fcd146d88170a6ac469c5966c386c829c3e)
            check_type(argname="argument s3_bucket_name", value=s3_bucket_name, expected_type=type_hints["s3_bucket_name"])
            check_type(argname="argument config_snapshot_delivery_properties", value=config_snapshot_delivery_properties, expected_type=type_hints["config_snapshot_delivery_properties"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument s3_key_prefix", value=s3_key_prefix, expected_type=type_hints["s3_key_prefix"])
            check_type(argname="argument s3_kms_key_arn", value=s3_kms_key_arn, expected_type=type_hints["s3_kms_key_arn"])
            check_type(argname="argument sns_topic_arn", value=sns_topic_arn, expected_type=type_hints["sns_topic_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "s3_bucket_name": s3_bucket_name,
        }
        if config_snapshot_delivery_properties is not None:
            self._values["config_snapshot_delivery_properties"] = config_snapshot_delivery_properties
        if name is not None:
            self._values["name"] = name
        if s3_key_prefix is not None:
            self._values["s3_key_prefix"] = s3_key_prefix
        if s3_kms_key_arn is not None:
            self._values["s3_kms_key_arn"] = s3_kms_key_arn
        if sns_topic_arn is not None:
            self._values["sns_topic_arn"] = sns_topic_arn

    @builtins.property
    def s3_bucket_name(self) -> builtins.str:
        '''The name of the Amazon S3 bucket to which AWS Config delivers configuration snapshots and configuration history files.

        If you specify a bucket that belongs to another AWS account , that bucket must have policies that grant access permissions to AWS Config . For more information, see `Permissions for the Amazon S3 Bucket <https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-policy.html>`_ in the *AWS Config Developer Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-s3bucketname
        '''
        result = self._values.get("s3_bucket_name")
        assert result is not None, "Required property 's3_bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def config_snapshot_delivery_properties(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnDeliveryChannel.ConfigSnapshotDeliveryPropertiesProperty]]:
        '''The options for how often AWS Config delivers configuration snapshots to the Amazon S3 bucket.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-configsnapshotdeliveryproperties
        '''
        result = self._values.get("config_snapshot_delivery_properties")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnDeliveryChannel.ConfigSnapshotDeliveryPropertiesProperty]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''A name for the delivery channel.

        If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the delivery channel name. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ .

        Updates are not supported. To change the name, you must run two separate updates. In the first update, delete this resource, and then recreate it with a new name in the second update.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_key_prefix(self) -> typing.Optional[builtins.str]:
        '''The prefix for the specified Amazon S3 bucket.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-s3keyprefix
        '''
        result = self._values.get("s3_key_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the AWS Key Management Service ( AWS KMS ) AWS KMS key (KMS key) used to encrypt objects delivered by AWS Config .

        Must belong to the same Region as the destination S3 bucket.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-s3kmskeyarn
        '''
        result = self._values.get("s3_kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sns_topic_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the Amazon SNS topic to which AWS Config sends notifications about configuration changes.

        If you choose a topic from another account, the topic must have policies that grant access permissions to AWS Config . For more information, see `Permissions for the Amazon SNS Topic <https://docs.aws.amazon.com/config/latest/developerguide/sns-topic-policy.html>`_ in the *AWS Config Developer Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-snstopicarn
        '''
        result = self._values.get("sns_topic_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDeliveryChannelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnOrganizationConfigRule(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-config.CfnOrganizationConfigRule",
):
    '''A CloudFormation ``AWS::Config::OrganizationConfigRule``.

    Adds or updates an AWS Config rule for your entire organization to evaluate if your AWS resources comply with your desired configurations. For information on how many organization AWS Config rules you can have per account, see `*Service Limits* <https://docs.aws.amazon.com/config/latest/developerguide/configlimits.html>`_ in the *AWS Config Developer Guide* .

    Only a management account and a delegated administrator can create or update an organization AWS Config rule. When calling the ``OrganizationConfigRule`` resource with a delegated administrator, you must ensure AWS Organizations ``ListDelegatedAdministrator`` permissions are added. An organization can have up to 3 delegated administrators.

    The ``OrganizationConfigRule`` resource enables organization service access through the ``EnableAWSServiceAccess`` action and creates a service-linked role ``AWSServiceRoleForConfigMultiAccountSetup`` in the management or delegated administrator account of your organization. The service-linked role is created only when the role does not exist in the caller account. AWS Config verifies the existence of role with ``GetRole`` action.

    To use the ``OrganizationConfigRule`` resource with delegated administrator, register a delegated administrator by calling AWS Organization ``register-delegated-administrator`` for ``config-multiaccountsetup.amazonaws.com`` .

    There are two types of rules: *AWS Config Managed Rules* and *AWS Config Custom Rules* . You can use ``PutOrganizationConfigRule`` to create both AWS Config Managed Rules and AWS Config Custom Rules.

    AWS Config Managed Rules are predefined, customizable rules created by AWS Config . For a list of managed rules, see `List of AWS Config Managed Rules <https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html>`_ . If you are adding an AWS Config managed rule, you must specify the rule's identifier for the ``RuleIdentifier`` key.

    AWS Config Custom Rules are rules that you create from scratch. There are two ways to create AWS Config custom rules: with Lambda functions ( `AWS Lambda Developer Guide <https://docs.aws.amazon.com/config/latest/developerguide/gettingstarted-concepts.html#gettingstarted-concepts-function>`_ ) and with Guard ( `Guard GitHub Repository <https://docs.aws.amazon.com/https://github.com/aws-cloudformation/cloudformation-guard>`_ ), a policy-as-code language. AWS Config custom rules created with AWS Lambda are called *AWS Config Custom Lambda Rules* and AWS Config custom rules created with Guard are called *AWS Config Custom Policy Rules* .

    If you are adding a new AWS Config Custom Lambda rule, you first need to create an AWS Lambda function in the management account or a delegated administrator that the rule invokes to evaluate your resources. You also need to create an IAM role in the managed account that can be assumed by the Lambda function. When you use ``PutOrganizationConfigRule`` to add a Custom Lambda rule to AWS Config , you must specify the Amazon Resource Name (ARN) that AWS Lambda assigns to the function.

    :cloudformationResource: AWS::Config::OrganizationConfigRule
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconfigrule.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_config as config
        
        cfn_organization_config_rule = config.CfnOrganizationConfigRule(self, "MyCfnOrganizationConfigRule",
            organization_config_rule_name="organizationConfigRuleName",
        
            # the properties below are optional
            excluded_accounts=["excludedAccounts"],
            organization_custom_code_rule_metadata=config.CfnOrganizationConfigRule.OrganizationCustomCodeRuleMetadataProperty(
                code_text="codeText",
                runtime="runtime",
        
                # the properties below are optional
                debug_log_delivery_accounts=["debugLogDeliveryAccounts"],
                description="description",
                input_parameters="inputParameters",
                maximum_execution_frequency="maximumExecutionFrequency",
                organization_config_rule_trigger_types=["organizationConfigRuleTriggerTypes"],
                resource_id_scope="resourceIdScope",
                resource_types_scope=["resourceTypesScope"],
                tag_key_scope="tagKeyScope",
                tag_value_scope="tagValueScope"
            ),
            organization_custom_rule_metadata=config.CfnOrganizationConfigRule.OrganizationCustomRuleMetadataProperty(
                lambda_function_arn="lambdaFunctionArn",
                organization_config_rule_trigger_types=["organizationConfigRuleTriggerTypes"],
        
                # the properties below are optional
                description="description",
                input_parameters="inputParameters",
                maximum_execution_frequency="maximumExecutionFrequency",
                resource_id_scope="resourceIdScope",
                resource_types_scope=["resourceTypesScope"],
                tag_key_scope="tagKeyScope",
                tag_value_scope="tagValueScope"
            ),
            organization_managed_rule_metadata=config.CfnOrganizationConfigRule.OrganizationManagedRuleMetadataProperty(
                rule_identifier="ruleIdentifier",
        
                # the properties below are optional
                description="description",
                input_parameters="inputParameters",
                maximum_execution_frequency="maximumExecutionFrequency",
                resource_id_scope="resourceIdScope",
                resource_types_scope=["resourceTypesScope"],
                tag_key_scope="tagKeyScope",
                tag_value_scope="tagValueScope"
            )
        )
    '''

    def __init__(
        self,
        scope: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        organization_config_rule_name: builtins.str,
        excluded_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
        organization_custom_code_rule_metadata: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnOrganizationConfigRule.OrganizationCustomCodeRuleMetadataProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        organization_custom_rule_metadata: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnOrganizationConfigRule.OrganizationCustomRuleMetadataProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        organization_managed_rule_metadata: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnOrganizationConfigRule.OrganizationManagedRuleMetadataProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Config::OrganizationConfigRule``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param organization_config_rule_name: The name that you assign to organization AWS Config rule.
        :param excluded_accounts: A comma-separated list of accounts excluded from organization AWS Config rule.
        :param organization_custom_code_rule_metadata: ``AWS::Config::OrganizationConfigRule.OrganizationCustomCodeRuleMetadata``.
        :param organization_custom_rule_metadata: An ``OrganizationCustomRuleMetadata`` object.
        :param organization_managed_rule_metadata: An ``OrganizationManagedRuleMetadata`` object.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b506ccb21501386876d39b6e43f781e00d82c1099fe12489a841614124a07b31)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnOrganizationConfigRuleProps(
            organization_config_rule_name=organization_config_rule_name,
            excluded_accounts=excluded_accounts,
            organization_custom_code_rule_metadata=organization_custom_code_rule_metadata,
            organization_custom_rule_metadata=organization_custom_rule_metadata,
            organization_managed_rule_metadata=organization_managed_rule_metadata,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ba0b3f14f6bec4f7c9423983d8ee7e9a71bcc3daacc82bdc266d120665fa322)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e71116763d0720f599a45f1b95994a44efe53f2e2160d46a8ff64af4dafc4f58)
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
    @jsii.member(jsii_name="organizationConfigRuleName")
    def organization_config_rule_name(self) -> builtins.str:
        '''The name that you assign to organization AWS Config rule.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconfigrule.html#cfn-config-organizationconfigrule-organizationconfigrulename
        '''
        return typing.cast(builtins.str, jsii.get(self, "organizationConfigRuleName"))

    @organization_config_rule_name.setter
    def organization_config_rule_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bfda5455a4e9f7bbd5923d65f203601c239bb91eaec45d7f2ef40afa6791f22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organizationConfigRuleName", value)

    @builtins.property
    @jsii.member(jsii_name="excludedAccounts")
    def excluded_accounts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A comma-separated list of accounts excluded from organization AWS Config rule.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconfigrule.html#cfn-config-organizationconfigrule-excludedaccounts
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "excludedAccounts"))

    @excluded_accounts.setter
    def excluded_accounts(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64ab5433e3c3beda5112bb6c8c191059903bd15b035478578849f10a4864980f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludedAccounts", value)

    @builtins.property
    @jsii.member(jsii_name="organizationCustomCodeRuleMetadata")
    def organization_custom_code_rule_metadata(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnOrganizationConfigRule.OrganizationCustomCodeRuleMetadataProperty"]]:
        '''``AWS::Config::OrganizationConfigRule.OrganizationCustomCodeRuleMetadata``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconfigrule.html#cfn-config-organizationconfigrule-organizationcustomcoderulemetadata
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnOrganizationConfigRule.OrganizationCustomCodeRuleMetadataProperty"]], jsii.get(self, "organizationCustomCodeRuleMetadata"))

    @organization_custom_code_rule_metadata.setter
    def organization_custom_code_rule_metadata(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnOrganizationConfigRule.OrganizationCustomCodeRuleMetadataProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a74a2f44949dfd73daca0ecea240366a679d927adcec03d325ebd8c4dfad5636)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organizationCustomCodeRuleMetadata", value)

    @builtins.property
    @jsii.member(jsii_name="organizationCustomRuleMetadata")
    def organization_custom_rule_metadata(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnOrganizationConfigRule.OrganizationCustomRuleMetadataProperty"]]:
        '''An ``OrganizationCustomRuleMetadata`` object.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconfigrule.html#cfn-config-organizationconfigrule-organizationcustomrulemetadata
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnOrganizationConfigRule.OrganizationCustomRuleMetadataProperty"]], jsii.get(self, "organizationCustomRuleMetadata"))

    @organization_custom_rule_metadata.setter
    def organization_custom_rule_metadata(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnOrganizationConfigRule.OrganizationCustomRuleMetadataProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae9a661088177a704fbfd22fa22ee971adafd61fa5566245dead965a0aea23ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organizationCustomRuleMetadata", value)

    @builtins.property
    @jsii.member(jsii_name="organizationManagedRuleMetadata")
    def organization_managed_rule_metadata(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnOrganizationConfigRule.OrganizationManagedRuleMetadataProperty"]]:
        '''An ``OrganizationManagedRuleMetadata`` object.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconfigrule.html#cfn-config-organizationconfigrule-organizationmanagedrulemetadata
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnOrganizationConfigRule.OrganizationManagedRuleMetadataProperty"]], jsii.get(self, "organizationManagedRuleMetadata"))

    @organization_managed_rule_metadata.setter
    def organization_managed_rule_metadata(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnOrganizationConfigRule.OrganizationManagedRuleMetadataProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7723ef40d27fd1460f2ad024f5f6cd4701fe13b73fb4ce0b89e0a520aa5a004)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organizationManagedRuleMetadata", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-config.CfnOrganizationConfigRule.OrganizationCustomCodeRuleMetadataProperty",
        jsii_struct_bases=[],
        name_mapping={
            "code_text": "codeText",
            "runtime": "runtime",
            "debug_log_delivery_accounts": "debugLogDeliveryAccounts",
            "description": "description",
            "input_parameters": "inputParameters",
            "maximum_execution_frequency": "maximumExecutionFrequency",
            "organization_config_rule_trigger_types": "organizationConfigRuleTriggerTypes",
            "resource_id_scope": "resourceIdScope",
            "resource_types_scope": "resourceTypesScope",
            "tag_key_scope": "tagKeyScope",
            "tag_value_scope": "tagValueScope",
        },
    )
    class OrganizationCustomCodeRuleMetadataProperty:
        def __init__(
            self,
            *,
            code_text: builtins.str,
            runtime: builtins.str,
            debug_log_delivery_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
            description: typing.Optional[builtins.str] = None,
            input_parameters: typing.Optional[builtins.str] = None,
            maximum_execution_frequency: typing.Optional[builtins.str] = None,
            organization_config_rule_trigger_types: typing.Optional[typing.Sequence[builtins.str]] = None,
            resource_id_scope: typing.Optional[builtins.str] = None,
            resource_types_scope: typing.Optional[typing.Sequence[builtins.str]] = None,
            tag_key_scope: typing.Optional[builtins.str] = None,
            tag_value_scope: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param code_text: ``CfnOrganizationConfigRule.OrganizationCustomCodeRuleMetadataProperty.CodeText``.
            :param runtime: ``CfnOrganizationConfigRule.OrganizationCustomCodeRuleMetadataProperty.Runtime``.
            :param debug_log_delivery_accounts: ``CfnOrganizationConfigRule.OrganizationCustomCodeRuleMetadataProperty.DebugLogDeliveryAccounts``.
            :param description: ``CfnOrganizationConfigRule.OrganizationCustomCodeRuleMetadataProperty.Description``.
            :param input_parameters: ``CfnOrganizationConfigRule.OrganizationCustomCodeRuleMetadataProperty.InputParameters``.
            :param maximum_execution_frequency: ``CfnOrganizationConfigRule.OrganizationCustomCodeRuleMetadataProperty.MaximumExecutionFrequency``.
            :param organization_config_rule_trigger_types: ``CfnOrganizationConfigRule.OrganizationCustomCodeRuleMetadataProperty.OrganizationConfigRuleTriggerTypes``.
            :param resource_id_scope: ``CfnOrganizationConfigRule.OrganizationCustomCodeRuleMetadataProperty.ResourceIdScope``.
            :param resource_types_scope: ``CfnOrganizationConfigRule.OrganizationCustomCodeRuleMetadataProperty.ResourceTypesScope``.
            :param tag_key_scope: ``CfnOrganizationConfigRule.OrganizationCustomCodeRuleMetadataProperty.TagKeyScope``.
            :param tag_value_scope: ``CfnOrganizationConfigRule.OrganizationCustomCodeRuleMetadataProperty.TagValueScope``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomcoderulemetadata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_config as config
                
                organization_custom_code_rule_metadata_property = config.CfnOrganizationConfigRule.OrganizationCustomCodeRuleMetadataProperty(
                    code_text="codeText",
                    runtime="runtime",
                
                    # the properties below are optional
                    debug_log_delivery_accounts=["debugLogDeliveryAccounts"],
                    description="description",
                    input_parameters="inputParameters",
                    maximum_execution_frequency="maximumExecutionFrequency",
                    organization_config_rule_trigger_types=["organizationConfigRuleTriggerTypes"],
                    resource_id_scope="resourceIdScope",
                    resource_types_scope=["resourceTypesScope"],
                    tag_key_scope="tagKeyScope",
                    tag_value_scope="tagValueScope"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e3494b5976e8b7148e429811e24136c4203b079234017740bed1ab618ac03fdc)
                check_type(argname="argument code_text", value=code_text, expected_type=type_hints["code_text"])
                check_type(argname="argument runtime", value=runtime, expected_type=type_hints["runtime"])
                check_type(argname="argument debug_log_delivery_accounts", value=debug_log_delivery_accounts, expected_type=type_hints["debug_log_delivery_accounts"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument input_parameters", value=input_parameters, expected_type=type_hints["input_parameters"])
                check_type(argname="argument maximum_execution_frequency", value=maximum_execution_frequency, expected_type=type_hints["maximum_execution_frequency"])
                check_type(argname="argument organization_config_rule_trigger_types", value=organization_config_rule_trigger_types, expected_type=type_hints["organization_config_rule_trigger_types"])
                check_type(argname="argument resource_id_scope", value=resource_id_scope, expected_type=type_hints["resource_id_scope"])
                check_type(argname="argument resource_types_scope", value=resource_types_scope, expected_type=type_hints["resource_types_scope"])
                check_type(argname="argument tag_key_scope", value=tag_key_scope, expected_type=type_hints["tag_key_scope"])
                check_type(argname="argument tag_value_scope", value=tag_value_scope, expected_type=type_hints["tag_value_scope"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "code_text": code_text,
                "runtime": runtime,
            }
            if debug_log_delivery_accounts is not None:
                self._values["debug_log_delivery_accounts"] = debug_log_delivery_accounts
            if description is not None:
                self._values["description"] = description
            if input_parameters is not None:
                self._values["input_parameters"] = input_parameters
            if maximum_execution_frequency is not None:
                self._values["maximum_execution_frequency"] = maximum_execution_frequency
            if organization_config_rule_trigger_types is not None:
                self._values["organization_config_rule_trigger_types"] = organization_config_rule_trigger_types
            if resource_id_scope is not None:
                self._values["resource_id_scope"] = resource_id_scope
            if resource_types_scope is not None:
                self._values["resource_types_scope"] = resource_types_scope
            if tag_key_scope is not None:
                self._values["tag_key_scope"] = tag_key_scope
            if tag_value_scope is not None:
                self._values["tag_value_scope"] = tag_value_scope

        @builtins.property
        def code_text(self) -> builtins.str:
            '''``CfnOrganizationConfigRule.OrganizationCustomCodeRuleMetadataProperty.CodeText``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomcoderulemetadata.html#cfn-config-organizationconfigrule-organizationcustomcoderulemetadata-codetext
            '''
            result = self._values.get("code_text")
            assert result is not None, "Required property 'code_text' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def runtime(self) -> builtins.str:
            '''``CfnOrganizationConfigRule.OrganizationCustomCodeRuleMetadataProperty.Runtime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomcoderulemetadata.html#cfn-config-organizationconfigrule-organizationcustomcoderulemetadata-runtime
            '''
            result = self._values.get("runtime")
            assert result is not None, "Required property 'runtime' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def debug_log_delivery_accounts(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnOrganizationConfigRule.OrganizationCustomCodeRuleMetadataProperty.DebugLogDeliveryAccounts``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomcoderulemetadata.html#cfn-config-organizationconfigrule-organizationcustomcoderulemetadata-debuglogdeliveryaccounts
            '''
            result = self._values.get("debug_log_delivery_accounts")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''``CfnOrganizationConfigRule.OrganizationCustomCodeRuleMetadataProperty.Description``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomcoderulemetadata.html#cfn-config-organizationconfigrule-organizationcustomcoderulemetadata-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def input_parameters(self) -> typing.Optional[builtins.str]:
            '''``CfnOrganizationConfigRule.OrganizationCustomCodeRuleMetadataProperty.InputParameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomcoderulemetadata.html#cfn-config-organizationconfigrule-organizationcustomcoderulemetadata-inputparameters
            '''
            result = self._values.get("input_parameters")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def maximum_execution_frequency(self) -> typing.Optional[builtins.str]:
            '''``CfnOrganizationConfigRule.OrganizationCustomCodeRuleMetadataProperty.MaximumExecutionFrequency``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomcoderulemetadata.html#cfn-config-organizationconfigrule-organizationcustomcoderulemetadata-maximumexecutionfrequency
            '''
            result = self._values.get("maximum_execution_frequency")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def organization_config_rule_trigger_types(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnOrganizationConfigRule.OrganizationCustomCodeRuleMetadataProperty.OrganizationConfigRuleTriggerTypes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomcoderulemetadata.html#cfn-config-organizationconfigrule-organizationcustomcoderulemetadata-organizationconfigruletriggertypes
            '''
            result = self._values.get("organization_config_rule_trigger_types")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def resource_id_scope(self) -> typing.Optional[builtins.str]:
            '''``CfnOrganizationConfigRule.OrganizationCustomCodeRuleMetadataProperty.ResourceIdScope``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomcoderulemetadata.html#cfn-config-organizationconfigrule-organizationcustomcoderulemetadata-resourceidscope
            '''
            result = self._values.get("resource_id_scope")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def resource_types_scope(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnOrganizationConfigRule.OrganizationCustomCodeRuleMetadataProperty.ResourceTypesScope``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomcoderulemetadata.html#cfn-config-organizationconfigrule-organizationcustomcoderulemetadata-resourcetypesscope
            '''
            result = self._values.get("resource_types_scope")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def tag_key_scope(self) -> typing.Optional[builtins.str]:
            '''``CfnOrganizationConfigRule.OrganizationCustomCodeRuleMetadataProperty.TagKeyScope``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomcoderulemetadata.html#cfn-config-organizationconfigrule-organizationcustomcoderulemetadata-tagkeyscope
            '''
            result = self._values.get("tag_key_scope")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tag_value_scope(self) -> typing.Optional[builtins.str]:
            '''``CfnOrganizationConfigRule.OrganizationCustomCodeRuleMetadataProperty.TagValueScope``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomcoderulemetadata.html#cfn-config-organizationconfigrule-organizationcustomcoderulemetadata-tagvaluescope
            '''
            result = self._values.get("tag_value_scope")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OrganizationCustomCodeRuleMetadataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-config.CfnOrganizationConfigRule.OrganizationCustomRuleMetadataProperty",
        jsii_struct_bases=[],
        name_mapping={
            "lambda_function_arn": "lambdaFunctionArn",
            "organization_config_rule_trigger_types": "organizationConfigRuleTriggerTypes",
            "description": "description",
            "input_parameters": "inputParameters",
            "maximum_execution_frequency": "maximumExecutionFrequency",
            "resource_id_scope": "resourceIdScope",
            "resource_types_scope": "resourceTypesScope",
            "tag_key_scope": "tagKeyScope",
            "tag_value_scope": "tagValueScope",
        },
    )
    class OrganizationCustomRuleMetadataProperty:
        def __init__(
            self,
            *,
            lambda_function_arn: builtins.str,
            organization_config_rule_trigger_types: typing.Sequence[builtins.str],
            description: typing.Optional[builtins.str] = None,
            input_parameters: typing.Optional[builtins.str] = None,
            maximum_execution_frequency: typing.Optional[builtins.str] = None,
            resource_id_scope: typing.Optional[builtins.str] = None,
            resource_types_scope: typing.Optional[typing.Sequence[builtins.str]] = None,
            tag_key_scope: typing.Optional[builtins.str] = None,
            tag_value_scope: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An object that specifies organization custom rule metadata such as resource type, resource ID of AWS resource, Lambda function ARN, and organization trigger types that trigger AWS Config to evaluate your AWS resources against a rule.

            It also provides the frequency with which you want AWS Config to run evaluations for the rule if the trigger type is periodic.

            :param lambda_function_arn: The lambda function ARN.
            :param organization_config_rule_trigger_types: The type of notification that triggers AWS Config to run an evaluation for a rule. You can specify the following notification types: - ``ConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config delivers a configuration item as a result of a resource change. - ``OversizedConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config delivers an oversized configuration item. AWS Config may generate this notification type when a resource changes and the notification exceeds the maximum size allowed by Amazon SNS. - ``ScheduledNotification`` - Triggers a periodic evaluation at the frequency specified for ``MaximumExecutionFrequency`` .
            :param description: The description that you provide for your organization AWS Config rule.
            :param input_parameters: A string, in JSON format, that is passed to your organization AWS Config rule Lambda function.
            :param maximum_execution_frequency: The maximum frequency with which AWS Config runs evaluations for a rule. Your custom rule is triggered when AWS Config delivers the configuration snapshot. For more information, see ``ConfigSnapshotDeliveryProperties`` . .. epigraph:: By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.
            :param resource_id_scope: The ID of the AWS resource that was evaluated.
            :param resource_types_scope: The type of the AWS resource that was evaluated.
            :param tag_key_scope: One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.
            :param tag_value_scope: The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomrulemetadata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_config as config
                
                organization_custom_rule_metadata_property = config.CfnOrganizationConfigRule.OrganizationCustomRuleMetadataProperty(
                    lambda_function_arn="lambdaFunctionArn",
                    organization_config_rule_trigger_types=["organizationConfigRuleTriggerTypes"],
                
                    # the properties below are optional
                    description="description",
                    input_parameters="inputParameters",
                    maximum_execution_frequency="maximumExecutionFrequency",
                    resource_id_scope="resourceIdScope",
                    resource_types_scope=["resourceTypesScope"],
                    tag_key_scope="tagKeyScope",
                    tag_value_scope="tagValueScope"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__308812e33051b64d99844c3dee8eb71c0acdd33b6559d539f7c0e6d850b09000)
                check_type(argname="argument lambda_function_arn", value=lambda_function_arn, expected_type=type_hints["lambda_function_arn"])
                check_type(argname="argument organization_config_rule_trigger_types", value=organization_config_rule_trigger_types, expected_type=type_hints["organization_config_rule_trigger_types"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument input_parameters", value=input_parameters, expected_type=type_hints["input_parameters"])
                check_type(argname="argument maximum_execution_frequency", value=maximum_execution_frequency, expected_type=type_hints["maximum_execution_frequency"])
                check_type(argname="argument resource_id_scope", value=resource_id_scope, expected_type=type_hints["resource_id_scope"])
                check_type(argname="argument resource_types_scope", value=resource_types_scope, expected_type=type_hints["resource_types_scope"])
                check_type(argname="argument tag_key_scope", value=tag_key_scope, expected_type=type_hints["tag_key_scope"])
                check_type(argname="argument tag_value_scope", value=tag_value_scope, expected_type=type_hints["tag_value_scope"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "lambda_function_arn": lambda_function_arn,
                "organization_config_rule_trigger_types": organization_config_rule_trigger_types,
            }
            if description is not None:
                self._values["description"] = description
            if input_parameters is not None:
                self._values["input_parameters"] = input_parameters
            if maximum_execution_frequency is not None:
                self._values["maximum_execution_frequency"] = maximum_execution_frequency
            if resource_id_scope is not None:
                self._values["resource_id_scope"] = resource_id_scope
            if resource_types_scope is not None:
                self._values["resource_types_scope"] = resource_types_scope
            if tag_key_scope is not None:
                self._values["tag_key_scope"] = tag_key_scope
            if tag_value_scope is not None:
                self._values["tag_value_scope"] = tag_value_scope

        @builtins.property
        def lambda_function_arn(self) -> builtins.str:
            '''The lambda function ARN.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomrulemetadata.html#cfn-config-organizationconfigrule-organizationcustomrulemetadata-lambdafunctionarn
            '''
            result = self._values.get("lambda_function_arn")
            assert result is not None, "Required property 'lambda_function_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def organization_config_rule_trigger_types(self) -> typing.List[builtins.str]:
            '''The type of notification that triggers AWS Config to run an evaluation for a rule.

            You can specify the following notification types:

            - ``ConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config delivers a configuration item as a result of a resource change.
            - ``OversizedConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config delivers an oversized configuration item. AWS Config may generate this notification type when a resource changes and the notification exceeds the maximum size allowed by Amazon SNS.
            - ``ScheduledNotification`` - Triggers a periodic evaluation at the frequency specified for ``MaximumExecutionFrequency`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomrulemetadata.html#cfn-config-organizationconfigrule-organizationcustomrulemetadata-organizationconfigruletriggertypes
            '''
            result = self._values.get("organization_config_rule_trigger_types")
            assert result is not None, "Required property 'organization_config_rule_trigger_types' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The description that you provide for your organization AWS Config rule.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomrulemetadata.html#cfn-config-organizationconfigrule-organizationcustomrulemetadata-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def input_parameters(self) -> typing.Optional[builtins.str]:
            '''A string, in JSON format, that is passed to your organization AWS Config rule Lambda function.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomrulemetadata.html#cfn-config-organizationconfigrule-organizationcustomrulemetadata-inputparameters
            '''
            result = self._values.get("input_parameters")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def maximum_execution_frequency(self) -> typing.Optional[builtins.str]:
            '''The maximum frequency with which AWS Config runs evaluations for a rule.

            Your custom rule is triggered when AWS Config delivers the configuration snapshot. For more information, see ``ConfigSnapshotDeliveryProperties`` .
            .. epigraph::

               By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomrulemetadata.html#cfn-config-organizationconfigrule-organizationcustomrulemetadata-maximumexecutionfrequency
            '''
            result = self._values.get("maximum_execution_frequency")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def resource_id_scope(self) -> typing.Optional[builtins.str]:
            '''The ID of the AWS resource that was evaluated.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomrulemetadata.html#cfn-config-organizationconfigrule-organizationcustomrulemetadata-resourceidscope
            '''
            result = self._values.get("resource_id_scope")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def resource_types_scope(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The type of the AWS resource that was evaluated.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomrulemetadata.html#cfn-config-organizationconfigrule-organizationcustomrulemetadata-resourcetypesscope
            '''
            result = self._values.get("resource_types_scope")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def tag_key_scope(self) -> typing.Optional[builtins.str]:
            '''One part of a key-value pair that make up a tag.

            A key is a general label that acts like a category for more specific tag values.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomrulemetadata.html#cfn-config-organizationconfigrule-organizationcustomrulemetadata-tagkeyscope
            '''
            result = self._values.get("tag_key_scope")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tag_value_scope(self) -> typing.Optional[builtins.str]:
            '''The optional part of a key-value pair that make up a tag.

            A value acts as a descriptor within a tag category (key).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomrulemetadata.html#cfn-config-organizationconfigrule-organizationcustomrulemetadata-tagvaluescope
            '''
            result = self._values.get("tag_value_scope")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OrganizationCustomRuleMetadataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-config.CfnOrganizationConfigRule.OrganizationManagedRuleMetadataProperty",
        jsii_struct_bases=[],
        name_mapping={
            "rule_identifier": "ruleIdentifier",
            "description": "description",
            "input_parameters": "inputParameters",
            "maximum_execution_frequency": "maximumExecutionFrequency",
            "resource_id_scope": "resourceIdScope",
            "resource_types_scope": "resourceTypesScope",
            "tag_key_scope": "tagKeyScope",
            "tag_value_scope": "tagValueScope",
        },
    )
    class OrganizationManagedRuleMetadataProperty:
        def __init__(
            self,
            *,
            rule_identifier: builtins.str,
            description: typing.Optional[builtins.str] = None,
            input_parameters: typing.Optional[builtins.str] = None,
            maximum_execution_frequency: typing.Optional[builtins.str] = None,
            resource_id_scope: typing.Optional[builtins.str] = None,
            resource_types_scope: typing.Optional[typing.Sequence[builtins.str]] = None,
            tag_key_scope: typing.Optional[builtins.str] = None,
            tag_value_scope: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An object that specifies organization managed rule metadata such as resource type and ID of AWS resource along with the rule identifier.

            It also provides the frequency with which you want AWS Config to run evaluations for the rule if the trigger type is periodic.

            :param rule_identifier: For organization config managed rules, a predefined identifier from a list. For example, ``IAM_PASSWORD_POLICY`` is a managed rule. To reference a managed rule, see `Using AWS Config managed rules <https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html>`_ .
            :param description: The description that you provide for your organization AWS Config rule.
            :param input_parameters: A string, in JSON format, that is passed to your organization AWS Config rule Lambda function.
            :param maximum_execution_frequency: The maximum frequency with which AWS Config runs evaluations for a rule. This is for an AWS Config managed rule that is triggered at a periodic frequency. .. epigraph:: By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.
            :param resource_id_scope: The ID of the AWS resource that was evaluated.
            :param resource_types_scope: The type of the AWS resource that was evaluated.
            :param tag_key_scope: One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.
            :param tag_value_scope: The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationmanagedrulemetadata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_config as config
                
                organization_managed_rule_metadata_property = config.CfnOrganizationConfigRule.OrganizationManagedRuleMetadataProperty(
                    rule_identifier="ruleIdentifier",
                
                    # the properties below are optional
                    description="description",
                    input_parameters="inputParameters",
                    maximum_execution_frequency="maximumExecutionFrequency",
                    resource_id_scope="resourceIdScope",
                    resource_types_scope=["resourceTypesScope"],
                    tag_key_scope="tagKeyScope",
                    tag_value_scope="tagValueScope"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e79946dfc98a295f8d1ebb2e640427202599da5a200569f35457e9f2dfbbd0d1)
                check_type(argname="argument rule_identifier", value=rule_identifier, expected_type=type_hints["rule_identifier"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument input_parameters", value=input_parameters, expected_type=type_hints["input_parameters"])
                check_type(argname="argument maximum_execution_frequency", value=maximum_execution_frequency, expected_type=type_hints["maximum_execution_frequency"])
                check_type(argname="argument resource_id_scope", value=resource_id_scope, expected_type=type_hints["resource_id_scope"])
                check_type(argname="argument resource_types_scope", value=resource_types_scope, expected_type=type_hints["resource_types_scope"])
                check_type(argname="argument tag_key_scope", value=tag_key_scope, expected_type=type_hints["tag_key_scope"])
                check_type(argname="argument tag_value_scope", value=tag_value_scope, expected_type=type_hints["tag_value_scope"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "rule_identifier": rule_identifier,
            }
            if description is not None:
                self._values["description"] = description
            if input_parameters is not None:
                self._values["input_parameters"] = input_parameters
            if maximum_execution_frequency is not None:
                self._values["maximum_execution_frequency"] = maximum_execution_frequency
            if resource_id_scope is not None:
                self._values["resource_id_scope"] = resource_id_scope
            if resource_types_scope is not None:
                self._values["resource_types_scope"] = resource_types_scope
            if tag_key_scope is not None:
                self._values["tag_key_scope"] = tag_key_scope
            if tag_value_scope is not None:
                self._values["tag_value_scope"] = tag_value_scope

        @builtins.property
        def rule_identifier(self) -> builtins.str:
            '''For organization config managed rules, a predefined identifier from a list.

            For example, ``IAM_PASSWORD_POLICY`` is a managed rule. To reference a managed rule, see `Using AWS Config managed rules <https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationmanagedrulemetadata.html#cfn-config-organizationconfigrule-organizationmanagedrulemetadata-ruleidentifier
            '''
            result = self._values.get("rule_identifier")
            assert result is not None, "Required property 'rule_identifier' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The description that you provide for your organization AWS Config rule.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationmanagedrulemetadata.html#cfn-config-organizationconfigrule-organizationmanagedrulemetadata-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def input_parameters(self) -> typing.Optional[builtins.str]:
            '''A string, in JSON format, that is passed to your organization AWS Config rule Lambda function.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationmanagedrulemetadata.html#cfn-config-organizationconfigrule-organizationmanagedrulemetadata-inputparameters
            '''
            result = self._values.get("input_parameters")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def maximum_execution_frequency(self) -> typing.Optional[builtins.str]:
            '''The maximum frequency with which AWS Config runs evaluations for a rule.

            This is for an AWS Config managed rule that is triggered at a periodic frequency.
            .. epigraph::

               By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationmanagedrulemetadata.html#cfn-config-organizationconfigrule-organizationmanagedrulemetadata-maximumexecutionfrequency
            '''
            result = self._values.get("maximum_execution_frequency")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def resource_id_scope(self) -> typing.Optional[builtins.str]:
            '''The ID of the AWS resource that was evaluated.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationmanagedrulemetadata.html#cfn-config-organizationconfigrule-organizationmanagedrulemetadata-resourceidscope
            '''
            result = self._values.get("resource_id_scope")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def resource_types_scope(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The type of the AWS resource that was evaluated.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationmanagedrulemetadata.html#cfn-config-organizationconfigrule-organizationmanagedrulemetadata-resourcetypesscope
            '''
            result = self._values.get("resource_types_scope")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def tag_key_scope(self) -> typing.Optional[builtins.str]:
            '''One part of a key-value pair that make up a tag.

            A key is a general label that acts like a category for more specific tag values.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationmanagedrulemetadata.html#cfn-config-organizationconfigrule-organizationmanagedrulemetadata-tagkeyscope
            '''
            result = self._values.get("tag_key_scope")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tag_value_scope(self) -> typing.Optional[builtins.str]:
            '''The optional part of a key-value pair that make up a tag.

            A value acts as a descriptor within a tag category (key).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationmanagedrulemetadata.html#cfn-config-organizationconfigrule-organizationmanagedrulemetadata-tagvaluescope
            '''
            result = self._values.get("tag_value_scope")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OrganizationManagedRuleMetadataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-config.CfnOrganizationConfigRuleProps",
    jsii_struct_bases=[],
    name_mapping={
        "organization_config_rule_name": "organizationConfigRuleName",
        "excluded_accounts": "excludedAccounts",
        "organization_custom_code_rule_metadata": "organizationCustomCodeRuleMetadata",
        "organization_custom_rule_metadata": "organizationCustomRuleMetadata",
        "organization_managed_rule_metadata": "organizationManagedRuleMetadata",
    },
)
class CfnOrganizationConfigRuleProps:
    def __init__(
        self,
        *,
        organization_config_rule_name: builtins.str,
        excluded_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
        organization_custom_code_rule_metadata: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnOrganizationConfigRule.OrganizationCustomCodeRuleMetadataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        organization_custom_rule_metadata: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnOrganizationConfigRule.OrganizationCustomRuleMetadataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        organization_managed_rule_metadata: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnOrganizationConfigRule.OrganizationManagedRuleMetadataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnOrganizationConfigRule``.

        :param organization_config_rule_name: The name that you assign to organization AWS Config rule.
        :param excluded_accounts: A comma-separated list of accounts excluded from organization AWS Config rule.
        :param organization_custom_code_rule_metadata: ``AWS::Config::OrganizationConfigRule.OrganizationCustomCodeRuleMetadata``.
        :param organization_custom_rule_metadata: An ``OrganizationCustomRuleMetadata`` object.
        :param organization_managed_rule_metadata: An ``OrganizationManagedRuleMetadata`` object.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconfigrule.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_config as config
            
            cfn_organization_config_rule_props = config.CfnOrganizationConfigRuleProps(
                organization_config_rule_name="organizationConfigRuleName",
            
                # the properties below are optional
                excluded_accounts=["excludedAccounts"],
                organization_custom_code_rule_metadata=config.CfnOrganizationConfigRule.OrganizationCustomCodeRuleMetadataProperty(
                    code_text="codeText",
                    runtime="runtime",
            
                    # the properties below are optional
                    debug_log_delivery_accounts=["debugLogDeliveryAccounts"],
                    description="description",
                    input_parameters="inputParameters",
                    maximum_execution_frequency="maximumExecutionFrequency",
                    organization_config_rule_trigger_types=["organizationConfigRuleTriggerTypes"],
                    resource_id_scope="resourceIdScope",
                    resource_types_scope=["resourceTypesScope"],
                    tag_key_scope="tagKeyScope",
                    tag_value_scope="tagValueScope"
                ),
                organization_custom_rule_metadata=config.CfnOrganizationConfigRule.OrganizationCustomRuleMetadataProperty(
                    lambda_function_arn="lambdaFunctionArn",
                    organization_config_rule_trigger_types=["organizationConfigRuleTriggerTypes"],
            
                    # the properties below are optional
                    description="description",
                    input_parameters="inputParameters",
                    maximum_execution_frequency="maximumExecutionFrequency",
                    resource_id_scope="resourceIdScope",
                    resource_types_scope=["resourceTypesScope"],
                    tag_key_scope="tagKeyScope",
                    tag_value_scope="tagValueScope"
                ),
                organization_managed_rule_metadata=config.CfnOrganizationConfigRule.OrganizationManagedRuleMetadataProperty(
                    rule_identifier="ruleIdentifier",
            
                    # the properties below are optional
                    description="description",
                    input_parameters="inputParameters",
                    maximum_execution_frequency="maximumExecutionFrequency",
                    resource_id_scope="resourceIdScope",
                    resource_types_scope=["resourceTypesScope"],
                    tag_key_scope="tagKeyScope",
                    tag_value_scope="tagValueScope"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__678289097a98bc5fd4dd4585f454bf87d496198b265fc462c28d48ee4ab656be)
            check_type(argname="argument organization_config_rule_name", value=organization_config_rule_name, expected_type=type_hints["organization_config_rule_name"])
            check_type(argname="argument excluded_accounts", value=excluded_accounts, expected_type=type_hints["excluded_accounts"])
            check_type(argname="argument organization_custom_code_rule_metadata", value=organization_custom_code_rule_metadata, expected_type=type_hints["organization_custom_code_rule_metadata"])
            check_type(argname="argument organization_custom_rule_metadata", value=organization_custom_rule_metadata, expected_type=type_hints["organization_custom_rule_metadata"])
            check_type(argname="argument organization_managed_rule_metadata", value=organization_managed_rule_metadata, expected_type=type_hints["organization_managed_rule_metadata"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "organization_config_rule_name": organization_config_rule_name,
        }
        if excluded_accounts is not None:
            self._values["excluded_accounts"] = excluded_accounts
        if organization_custom_code_rule_metadata is not None:
            self._values["organization_custom_code_rule_metadata"] = organization_custom_code_rule_metadata
        if organization_custom_rule_metadata is not None:
            self._values["organization_custom_rule_metadata"] = organization_custom_rule_metadata
        if organization_managed_rule_metadata is not None:
            self._values["organization_managed_rule_metadata"] = organization_managed_rule_metadata

    @builtins.property
    def organization_config_rule_name(self) -> builtins.str:
        '''The name that you assign to organization AWS Config rule.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconfigrule.html#cfn-config-organizationconfigrule-organizationconfigrulename
        '''
        result = self._values.get("organization_config_rule_name")
        assert result is not None, "Required property 'organization_config_rule_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def excluded_accounts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A comma-separated list of accounts excluded from organization AWS Config rule.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconfigrule.html#cfn-config-organizationconfigrule-excludedaccounts
        '''
        result = self._values.get("excluded_accounts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def organization_custom_code_rule_metadata(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnOrganizationConfigRule.OrganizationCustomCodeRuleMetadataProperty]]:
        '''``AWS::Config::OrganizationConfigRule.OrganizationCustomCodeRuleMetadata``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconfigrule.html#cfn-config-organizationconfigrule-organizationcustomcoderulemetadata
        '''
        result = self._values.get("organization_custom_code_rule_metadata")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnOrganizationConfigRule.OrganizationCustomCodeRuleMetadataProperty]], result)

    @builtins.property
    def organization_custom_rule_metadata(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnOrganizationConfigRule.OrganizationCustomRuleMetadataProperty]]:
        '''An ``OrganizationCustomRuleMetadata`` object.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconfigrule.html#cfn-config-organizationconfigrule-organizationcustomrulemetadata
        '''
        result = self._values.get("organization_custom_rule_metadata")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnOrganizationConfigRule.OrganizationCustomRuleMetadataProperty]], result)

    @builtins.property
    def organization_managed_rule_metadata(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnOrganizationConfigRule.OrganizationManagedRuleMetadataProperty]]:
        '''An ``OrganizationManagedRuleMetadata`` object.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconfigrule.html#cfn-config-organizationconfigrule-organizationmanagedrulemetadata
        '''
        result = self._values.get("organization_managed_rule_metadata")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnOrganizationConfigRule.OrganizationManagedRuleMetadataProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnOrganizationConfigRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnOrganizationConformancePack(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-config.CfnOrganizationConformancePack",
):
    '''A CloudFormation ``AWS::Config::OrganizationConformancePack``.

    OrganizationConformancePack deploys conformance packs across member accounts in an AWS Organizations . OrganizationConformancePack enables organization service access for ``config-multiaccountsetup.amazonaws.com`` through the ``EnableAWSServiceAccess`` action and creates a service linked role in the master account of your organization. The service linked role is created only when the role does not exist in the master account.

    :cloudformationResource: AWS::Config::OrganizationConformancePack
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconformancepack.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_config as config
        
        cfn_organization_conformance_pack = config.CfnOrganizationConformancePack(self, "MyCfnOrganizationConformancePack",
            organization_conformance_pack_name="organizationConformancePackName",
        
            # the properties below are optional
            conformance_pack_input_parameters=[config.CfnOrganizationConformancePack.ConformancePackInputParameterProperty(
                parameter_name="parameterName",
                parameter_value="parameterValue"
            )],
            delivery_s3_bucket="deliveryS3Bucket",
            delivery_s3_key_prefix="deliveryS3KeyPrefix",
            excluded_accounts=["excludedAccounts"],
            template_body="templateBody",
            template_s3_uri="templateS3Uri"
        )
    '''

    def __init__(
        self,
        scope: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        organization_conformance_pack_name: builtins.str,
        conformance_pack_input_parameters: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnOrganizationConformancePack.ConformancePackInputParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        delivery_s3_bucket: typing.Optional[builtins.str] = None,
        delivery_s3_key_prefix: typing.Optional[builtins.str] = None,
        excluded_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
        template_body: typing.Optional[builtins.str] = None,
        template_s3_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Config::OrganizationConformancePack``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param organization_conformance_pack_name: The name you assign to an organization conformance pack.
        :param conformance_pack_input_parameters: A list of ``ConformancePackInputParameter`` objects.
        :param delivery_s3_bucket: The name of the Amazon S3 bucket where AWS Config stores conformance pack templates. .. epigraph:: This field is optional.
        :param delivery_s3_key_prefix: Any folder structure you want to add to an Amazon S3 bucket. .. epigraph:: This field is optional.
        :param excluded_accounts: A comma-separated list of accounts excluded from organization conformance pack.
        :param template_body: A string containing full conformance pack template body. Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes.
        :param template_s3_uri: Location of file containing the template body. The uri must point to the conformance pack template (max size: 300 KB).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a20f40efb5e871fc8f570b7e47343feda5af1c82dcf16660322bbc1929af56fc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnOrganizationConformancePackProps(
            organization_conformance_pack_name=organization_conformance_pack_name,
            conformance_pack_input_parameters=conformance_pack_input_parameters,
            delivery_s3_bucket=delivery_s3_bucket,
            delivery_s3_key_prefix=delivery_s3_key_prefix,
            excluded_accounts=excluded_accounts,
            template_body=template_body,
            template_s3_uri=template_s3_uri,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec620aaebbb43409be1fb8c242500cdaf4d5fe84f9f9103149cc6d40f7e74f64)
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
            type_hints = typing.get_type_hints(_typecheckingstub__65e0cc8d709757676f671cc3ab583ec52226ee513475123bb9ebd135e84c99e4)
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
    @jsii.member(jsii_name="organizationConformancePackName")
    def organization_conformance_pack_name(self) -> builtins.str:
        '''The name you assign to an organization conformance pack.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconformancepack.html#cfn-config-organizationconformancepack-organizationconformancepackname
        '''
        return typing.cast(builtins.str, jsii.get(self, "organizationConformancePackName"))

    @organization_conformance_pack_name.setter
    def organization_conformance_pack_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49099c5f413b09e4f288f5f65b8a302539b394e49f6f66cf333a2bc366198925)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organizationConformancePackName", value)

    @builtins.property
    @jsii.member(jsii_name="conformancePackInputParameters")
    def conformance_pack_input_parameters(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnOrganizationConformancePack.ConformancePackInputParameterProperty"]]]]:
        '''A list of ``ConformancePackInputParameter`` objects.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconformancepack.html#cfn-config-organizationconformancepack-conformancepackinputparameters
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnOrganizationConformancePack.ConformancePackInputParameterProperty"]]]], jsii.get(self, "conformancePackInputParameters"))

    @conformance_pack_input_parameters.setter
    def conformance_pack_input_parameters(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnOrganizationConformancePack.ConformancePackInputParameterProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed61238dacbaf3ee81b4eb66e0c4e5463b440d527c0a49508f6bb727085a027b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "conformancePackInputParameters", value)

    @builtins.property
    @jsii.member(jsii_name="deliveryS3Bucket")
    def delivery_s3_bucket(self) -> typing.Optional[builtins.str]:
        '''The name of the Amazon S3 bucket where AWS Config stores conformance pack templates.

        .. epigraph::

           This field is optional.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconformancepack.html#cfn-config-organizationconformancepack-deliverys3bucket
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deliveryS3Bucket"))

    @delivery_s3_bucket.setter
    def delivery_s3_bucket(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ac2f9f7af6cb6f06d82e385c8a81e34b8bd33767c25438e84f1d5dc32dc87e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deliveryS3Bucket", value)

    @builtins.property
    @jsii.member(jsii_name="deliveryS3KeyPrefix")
    def delivery_s3_key_prefix(self) -> typing.Optional[builtins.str]:
        '''Any folder structure you want to add to an Amazon S3 bucket.

        .. epigraph::

           This field is optional.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconformancepack.html#cfn-config-organizationconformancepack-deliverys3keyprefix
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deliveryS3KeyPrefix"))

    @delivery_s3_key_prefix.setter
    def delivery_s3_key_prefix(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa1237f2530d411b7d64104f3dc05f74340af362e962ba815c47e514777d0fd4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deliveryS3KeyPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="excludedAccounts")
    def excluded_accounts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A comma-separated list of accounts excluded from organization conformance pack.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconformancepack.html#cfn-config-organizationconformancepack-excludedaccounts
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "excludedAccounts"))

    @excluded_accounts.setter
    def excluded_accounts(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5554551cb66433e495447665360dc3688c586078b58d25f50576191704de2f7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludedAccounts", value)

    @builtins.property
    @jsii.member(jsii_name="templateBody")
    def template_body(self) -> typing.Optional[builtins.str]:
        '''A string containing full conformance pack template body.

        Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconformancepack.html#cfn-config-organizationconformancepack-templatebody
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateBody"))

    @template_body.setter
    def template_body(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f451cc2185147be3141c333f8fc24963f28818a46d1ed633a5fe992f403e84cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateBody", value)

    @builtins.property
    @jsii.member(jsii_name="templateS3Uri")
    def template_s3_uri(self) -> typing.Optional[builtins.str]:
        '''Location of file containing the template body.

        The uri must point to the conformance pack template (max size: 300 KB).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconformancepack.html#cfn-config-organizationconformancepack-templates3uri
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateS3Uri"))

    @template_s3_uri.setter
    def template_s3_uri(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee958e76ffd91e1fdb984f5dae41c4dbfa49ca4650f7871ccba671617438c48a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateS3Uri", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-config.CfnOrganizationConformancePack.ConformancePackInputParameterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "parameter_name": "parameterName",
            "parameter_value": "parameterValue",
        },
    )
    class ConformancePackInputParameterProperty:
        def __init__(
            self,
            *,
            parameter_name: builtins.str,
            parameter_value: builtins.str,
        ) -> None:
            '''Input parameters in the form of key-value pairs for the conformance pack, both of which you define.

            Keys can have a maximum character length of 255 characters, and values can have a maximum length of 4096 characters.

            :param parameter_name: One part of a key-value pair.
            :param parameter_value: One part of a key-value pair.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconformancepack-conformancepackinputparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_config as config
                
                conformance_pack_input_parameter_property = config.CfnOrganizationConformancePack.ConformancePackInputParameterProperty(
                    parameter_name="parameterName",
                    parameter_value="parameterValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__027e7f88a548e59cba26c51fbc136bbeeaee12184468f557b66f758a54333e37)
                check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
                check_type(argname="argument parameter_value", value=parameter_value, expected_type=type_hints["parameter_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "parameter_name": parameter_name,
                "parameter_value": parameter_value,
            }

        @builtins.property
        def parameter_name(self) -> builtins.str:
            '''One part of a key-value pair.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconformancepack-conformancepackinputparameter.html#cfn-config-organizationconformancepack-conformancepackinputparameter-parametername
            '''
            result = self._values.get("parameter_name")
            assert result is not None, "Required property 'parameter_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def parameter_value(self) -> builtins.str:
            '''One part of a key-value pair.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconformancepack-conformancepackinputparameter.html#cfn-config-organizationconformancepack-conformancepackinputparameter-parametervalue
            '''
            result = self._values.get("parameter_value")
            assert result is not None, "Required property 'parameter_value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConformancePackInputParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-config.CfnOrganizationConformancePackProps",
    jsii_struct_bases=[],
    name_mapping={
        "organization_conformance_pack_name": "organizationConformancePackName",
        "conformance_pack_input_parameters": "conformancePackInputParameters",
        "delivery_s3_bucket": "deliveryS3Bucket",
        "delivery_s3_key_prefix": "deliveryS3KeyPrefix",
        "excluded_accounts": "excludedAccounts",
        "template_body": "templateBody",
        "template_s3_uri": "templateS3Uri",
    },
)
class CfnOrganizationConformancePackProps:
    def __init__(
        self,
        *,
        organization_conformance_pack_name: builtins.str,
        conformance_pack_input_parameters: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnOrganizationConformancePack.ConformancePackInputParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        delivery_s3_bucket: typing.Optional[builtins.str] = None,
        delivery_s3_key_prefix: typing.Optional[builtins.str] = None,
        excluded_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
        template_body: typing.Optional[builtins.str] = None,
        template_s3_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnOrganizationConformancePack``.

        :param organization_conformance_pack_name: The name you assign to an organization conformance pack.
        :param conformance_pack_input_parameters: A list of ``ConformancePackInputParameter`` objects.
        :param delivery_s3_bucket: The name of the Amazon S3 bucket where AWS Config stores conformance pack templates. .. epigraph:: This field is optional.
        :param delivery_s3_key_prefix: Any folder structure you want to add to an Amazon S3 bucket. .. epigraph:: This field is optional.
        :param excluded_accounts: A comma-separated list of accounts excluded from organization conformance pack.
        :param template_body: A string containing full conformance pack template body. Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes.
        :param template_s3_uri: Location of file containing the template body. The uri must point to the conformance pack template (max size: 300 KB).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconformancepack.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_config as config
            
            cfn_organization_conformance_pack_props = config.CfnOrganizationConformancePackProps(
                organization_conformance_pack_name="organizationConformancePackName",
            
                # the properties below are optional
                conformance_pack_input_parameters=[config.CfnOrganizationConformancePack.ConformancePackInputParameterProperty(
                    parameter_name="parameterName",
                    parameter_value="parameterValue"
                )],
                delivery_s3_bucket="deliveryS3Bucket",
                delivery_s3_key_prefix="deliveryS3KeyPrefix",
                excluded_accounts=["excludedAccounts"],
                template_body="templateBody",
                template_s3_uri="templateS3Uri"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc1f3f9375583d7bc0bee4f0fe74824e5a8406e73b4f8cb426aaa96327cb6c43)
            check_type(argname="argument organization_conformance_pack_name", value=organization_conformance_pack_name, expected_type=type_hints["organization_conformance_pack_name"])
            check_type(argname="argument conformance_pack_input_parameters", value=conformance_pack_input_parameters, expected_type=type_hints["conformance_pack_input_parameters"])
            check_type(argname="argument delivery_s3_bucket", value=delivery_s3_bucket, expected_type=type_hints["delivery_s3_bucket"])
            check_type(argname="argument delivery_s3_key_prefix", value=delivery_s3_key_prefix, expected_type=type_hints["delivery_s3_key_prefix"])
            check_type(argname="argument excluded_accounts", value=excluded_accounts, expected_type=type_hints["excluded_accounts"])
            check_type(argname="argument template_body", value=template_body, expected_type=type_hints["template_body"])
            check_type(argname="argument template_s3_uri", value=template_s3_uri, expected_type=type_hints["template_s3_uri"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "organization_conformance_pack_name": organization_conformance_pack_name,
        }
        if conformance_pack_input_parameters is not None:
            self._values["conformance_pack_input_parameters"] = conformance_pack_input_parameters
        if delivery_s3_bucket is not None:
            self._values["delivery_s3_bucket"] = delivery_s3_bucket
        if delivery_s3_key_prefix is not None:
            self._values["delivery_s3_key_prefix"] = delivery_s3_key_prefix
        if excluded_accounts is not None:
            self._values["excluded_accounts"] = excluded_accounts
        if template_body is not None:
            self._values["template_body"] = template_body
        if template_s3_uri is not None:
            self._values["template_s3_uri"] = template_s3_uri

    @builtins.property
    def organization_conformance_pack_name(self) -> builtins.str:
        '''The name you assign to an organization conformance pack.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconformancepack.html#cfn-config-organizationconformancepack-organizationconformancepackname
        '''
        result = self._values.get("organization_conformance_pack_name")
        assert result is not None, "Required property 'organization_conformance_pack_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def conformance_pack_input_parameters(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnOrganizationConformancePack.ConformancePackInputParameterProperty]]]]:
        '''A list of ``ConformancePackInputParameter`` objects.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconformancepack.html#cfn-config-organizationconformancepack-conformancepackinputparameters
        '''
        result = self._values.get("conformance_pack_input_parameters")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnOrganizationConformancePack.ConformancePackInputParameterProperty]]]], result)

    @builtins.property
    def delivery_s3_bucket(self) -> typing.Optional[builtins.str]:
        '''The name of the Amazon S3 bucket where AWS Config stores conformance pack templates.

        .. epigraph::

           This field is optional.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconformancepack.html#cfn-config-organizationconformancepack-deliverys3bucket
        '''
        result = self._values.get("delivery_s3_bucket")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delivery_s3_key_prefix(self) -> typing.Optional[builtins.str]:
        '''Any folder structure you want to add to an Amazon S3 bucket.

        .. epigraph::

           This field is optional.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconformancepack.html#cfn-config-organizationconformancepack-deliverys3keyprefix
        '''
        result = self._values.get("delivery_s3_key_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def excluded_accounts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A comma-separated list of accounts excluded from organization conformance pack.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconformancepack.html#cfn-config-organizationconformancepack-excludedaccounts
        '''
        result = self._values.get("excluded_accounts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def template_body(self) -> typing.Optional[builtins.str]:
        '''A string containing full conformance pack template body.

        Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconformancepack.html#cfn-config-organizationconformancepack-templatebody
        '''
        result = self._values.get("template_body")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def template_s3_uri(self) -> typing.Optional[builtins.str]:
        '''Location of file containing the template body.

        The uri must point to the conformance pack template (max size: 300 KB).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconformancepack.html#cfn-config-organizationconformancepack-templates3uri
        '''
        result = self._values.get("template_s3_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnOrganizationConformancePackProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnRemediationConfiguration(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-config.CfnRemediationConfiguration",
):
    '''A CloudFormation ``AWS::Config::RemediationConfiguration``.

    An object that represents the details about the remediation configuration that includes the remediation action, parameters, and data to execute the action.

    :cloudformationResource: AWS::Config::RemediationConfiguration
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_config as config
        
        # parameters: Any
        
        cfn_remediation_configuration = config.CfnRemediationConfiguration(self, "MyCfnRemediationConfiguration",
            config_rule_name="configRuleName",
            target_id="targetId",
            target_type="targetType",
        
            # the properties below are optional
            automatic=False,
            execution_controls=config.CfnRemediationConfiguration.ExecutionControlsProperty(
                ssm_controls=config.CfnRemediationConfiguration.SsmControlsProperty(
                    concurrent_execution_rate_percentage=123,
                    error_percentage=123
                )
            ),
            maximum_automatic_attempts=123,
            parameters=parameters,
            resource_type="resourceType",
            retry_attempt_seconds=123,
            target_version="targetVersion"
        )
    '''

    def __init__(
        self,
        scope: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        config_rule_name: builtins.str,
        target_id: builtins.str,
        target_type: builtins.str,
        automatic: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
        execution_controls: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnRemediationConfiguration.ExecutionControlsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        maximum_automatic_attempts: typing.Optional[jsii.Number] = None,
        parameters: typing.Any = None,
        resource_type: typing.Optional[builtins.str] = None,
        retry_attempt_seconds: typing.Optional[jsii.Number] = None,
        target_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Config::RemediationConfiguration``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param config_rule_name: The name of the AWS Config rule.
        :param target_id: Target ID is the name of the public document.
        :param target_type: The type of the target. Target executes remediation. For example, SSM document.
        :param automatic: The remediation is triggered automatically.
        :param execution_controls: An ExecutionControls object.
        :param maximum_automatic_attempts: The maximum number of failed attempts for auto-remediation. If you do not select a number, the default is 5. For example, if you specify MaximumAutomaticAttempts as 5 with RetryAttemptSeconds as 50 seconds, AWS Config will put a RemediationException on your behalf for the failing resource after the 5th failed attempt within 50 seconds.
        :param parameters: An object of the RemediationParameterValue. For more information, see `RemediationParameterValue <https://docs.aws.amazon.com/config/latest/APIReference/API_RemediationParameterValue.html>`_ . .. epigraph:: The type is a map of strings to RemediationParameterValue.
        :param resource_type: The type of a resource.
        :param retry_attempt_seconds: Maximum time in seconds that AWS Config runs auto-remediation. If you do not select a number, the default is 60 seconds. For example, if you specify RetryAttemptSeconds as 50 seconds and MaximumAutomaticAttempts as 5, AWS Config will run auto-remediations 5 times within 50 seconds before throwing an exception.
        :param target_version: Version of the target. For example, version of the SSM document. .. epigraph:: If you make backward incompatible changes to the SSM document, you must call PutRemediationConfiguration API again to ensure the remediations can run.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df0ccb3e35c03afdc1847c752a5de3041146631d00089e64af9de6b06eecf7ae)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRemediationConfigurationProps(
            config_rule_name=config_rule_name,
            target_id=target_id,
            target_type=target_type,
            automatic=automatic,
            execution_controls=execution_controls,
            maximum_automatic_attempts=maximum_automatic_attempts,
            parameters=parameters,
            resource_type=resource_type,
            retry_attempt_seconds=retry_attempt_seconds,
            target_version=target_version,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f81e93550632ccea0f3cc031871e34d6ae49c64e3e98341134b138fdefa15b3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6aa049392202cee3880b6f72810e36cc2cac2dac921aa8e1f92e8ef63a900a6e)
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
    @jsii.member(jsii_name="configRuleName")
    def config_rule_name(self) -> builtins.str:
        '''The name of the AWS Config rule.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html#cfn-config-remediationconfiguration-configrulename
        '''
        return typing.cast(builtins.str, jsii.get(self, "configRuleName"))

    @config_rule_name.setter
    def config_rule_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5af04272b48cd7e8b55ce538f839ef249541a1e185e4c8c29d4819f3748a74a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configRuleName", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Any:
        '''An object of the RemediationParameterValue. For more information, see `RemediationParameterValue <https://docs.aws.amazon.com/config/latest/APIReference/API_RemediationParameterValue.html>`_ .

        .. epigraph::

           The type is a map of strings to RemediationParameterValue.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html#cfn-config-remediationconfiguration-parameters
        '''
        return typing.cast(typing.Any, jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__937ce6cdc0f4e244de040031b10c797897279212ffa86c44b65e43d6bba6a959)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="targetId")
    def target_id(self) -> builtins.str:
        '''Target ID is the name of the public document.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html#cfn-config-remediationconfiguration-targetid
        '''
        return typing.cast(builtins.str, jsii.get(self, "targetId"))

    @target_id.setter
    def target_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9abd361ef93db21187e2406af69fcdeb8b2bcc704fd30a5f06e1fc7b43ebdd87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetId", value)

    @builtins.property
    @jsii.member(jsii_name="targetType")
    def target_type(self) -> builtins.str:
        '''The type of the target.

        Target executes remediation. For example, SSM document.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html#cfn-config-remediationconfiguration-targettype
        '''
        return typing.cast(builtins.str, jsii.get(self, "targetType"))

    @target_type.setter
    def target_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__605c486b3be45b77078729b7b5c7af7aaa8c43c04b212dd24e5ba34746979538)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetType", value)

    @builtins.property
    @jsii.member(jsii_name="automatic")
    def automatic(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
        '''The remediation is triggered automatically.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html#cfn-config-remediationconfiguration-automatic
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], jsii.get(self, "automatic"))

    @automatic.setter
    def automatic(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cb72646ea2b338cd5c4dcd2e4b371b93052a2b9ab41df141b7c916fdb848c48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "automatic", value)

    @builtins.property
    @jsii.member(jsii_name="executionControls")
    def execution_controls(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnRemediationConfiguration.ExecutionControlsProperty"]]:
        '''An ExecutionControls object.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html#cfn-config-remediationconfiguration-executioncontrols
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnRemediationConfiguration.ExecutionControlsProperty"]], jsii.get(self, "executionControls"))

    @execution_controls.setter
    def execution_controls(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnRemediationConfiguration.ExecutionControlsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69ad26cf90d5e215439c878b91392c31afbb645473739f1e510d084d4c07b138)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionControls", value)

    @builtins.property
    @jsii.member(jsii_name="maximumAutomaticAttempts")
    def maximum_automatic_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of failed attempts for auto-remediation. If you do not select a number, the default is 5.

        For example, if you specify MaximumAutomaticAttempts as 5 with RetryAttemptSeconds as 50 seconds, AWS Config will put a RemediationException on your behalf for the failing resource after the 5th failed attempt within 50 seconds.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html#cfn-config-remediationconfiguration-maximumautomaticattempts
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumAutomaticAttempts"))

    @maximum_automatic_attempts.setter
    def maximum_automatic_attempts(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__871b74d77a62585e6372043a5354b60922edc42517633ef103f29420390c3e1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumAutomaticAttempts", value)

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> typing.Optional[builtins.str]:
        '''The type of a resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html#cfn-config-remediationconfiguration-resourcetype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceType"))

    @resource_type.setter
    def resource_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__285192de933460de2bc196dc50c36f9a5a49be4c6d36607bf9ee5b864e8c5169)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceType", value)

    @builtins.property
    @jsii.member(jsii_name="retryAttemptSeconds")
    def retry_attempt_seconds(self) -> typing.Optional[jsii.Number]:
        '''Maximum time in seconds that AWS Config runs auto-remediation.

        If you do not select a number, the default is 60 seconds.

        For example, if you specify RetryAttemptSeconds as 50 seconds and MaximumAutomaticAttempts as 5, AWS Config will run auto-remediations 5 times within 50 seconds before throwing an exception.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html#cfn-config-remediationconfiguration-retryattemptseconds
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retryAttemptSeconds"))

    @retry_attempt_seconds.setter
    def retry_attempt_seconds(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e3a13ceabde1da7aeeaa50c9d33011fdf74a9a11d6551b018ed1ee77d2ebbea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retryAttemptSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="targetVersion")
    def target_version(self) -> typing.Optional[builtins.str]:
        '''Version of the target. For example, version of the SSM document.

        .. epigraph::

           If you make backward incompatible changes to the SSM document, you must call PutRemediationConfiguration API again to ensure the remediations can run.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html#cfn-config-remediationconfiguration-targetversion
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetVersion"))

    @target_version.setter
    def target_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c2a0ae324ebf289f497742e67467025ebef8c2d7a9bda0a954b769bacf06bae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetVersion", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-config.CfnRemediationConfiguration.ExecutionControlsProperty",
        jsii_struct_bases=[],
        name_mapping={"ssm_controls": "ssmControls"},
    )
    class ExecutionControlsProperty:
        def __init__(
            self,
            *,
            ssm_controls: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnRemediationConfiguration.SsmControlsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''An ExecutionControls object.

            :param ssm_controls: A SsmControls object.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-executioncontrols.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_config as config
                
                execution_controls_property = config.CfnRemediationConfiguration.ExecutionControlsProperty(
                    ssm_controls=config.CfnRemediationConfiguration.SsmControlsProperty(
                        concurrent_execution_rate_percentage=123,
                        error_percentage=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5c9bb63bd99bf40767252006448a4291646686c562f79c794a67340a30b63052)
                check_type(argname="argument ssm_controls", value=ssm_controls, expected_type=type_hints["ssm_controls"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ssm_controls is not None:
                self._values["ssm_controls"] = ssm_controls

        @builtins.property
        def ssm_controls(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnRemediationConfiguration.SsmControlsProperty"]]:
            '''A SsmControls object.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-executioncontrols.html#cfn-config-remediationconfiguration-executioncontrols-ssmcontrols
            '''
            result = self._values.get("ssm_controls")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnRemediationConfiguration.SsmControlsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExecutionControlsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-config.CfnRemediationConfiguration.RemediationParameterValueProperty",
        jsii_struct_bases=[],
        name_mapping={
            "resource_value": "resourceValue",
            "static_value": "staticValue",
        },
    )
    class RemediationParameterValueProperty:
        def __init__(
            self,
            *,
            resource_value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnRemediationConfiguration.ResourceValueProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            static_value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnRemediationConfiguration.StaticValueProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The value is either a dynamic (resource) value or a static value.

            You must select either a dynamic value or a static value.

            :param resource_value: The value is dynamic and changes at run-time.
            :param static_value: The value is static and does not change at run-time.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-remediationparametervalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_config as config
                
                remediation_parameter_value_property = config.CfnRemediationConfiguration.RemediationParameterValueProperty(
                    resource_value=config.CfnRemediationConfiguration.ResourceValueProperty(
                        value="value"
                    ),
                    static_value=config.CfnRemediationConfiguration.StaticValueProperty(
                        values=["values"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__281701a7180e3f34d6f80b43e9fe65c8cf3b67e9223960717b8236bf0a03ab17)
                check_type(argname="argument resource_value", value=resource_value, expected_type=type_hints["resource_value"])
                check_type(argname="argument static_value", value=static_value, expected_type=type_hints["static_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if resource_value is not None:
                self._values["resource_value"] = resource_value
            if static_value is not None:
                self._values["static_value"] = static_value

        @builtins.property
        def resource_value(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnRemediationConfiguration.ResourceValueProperty"]]:
            '''The value is dynamic and changes at run-time.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-remediationparametervalue.html#cfn-config-remediationconfiguration-remediationparametervalue-resourcevalue
            '''
            result = self._values.get("resource_value")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnRemediationConfiguration.ResourceValueProperty"]], result)

        @builtins.property
        def static_value(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnRemediationConfiguration.StaticValueProperty"]]:
            '''The value is static and does not change at run-time.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-remediationparametervalue.html#cfn-config-remediationconfiguration-remediationparametervalue-staticvalue
            '''
            result = self._values.get("static_value")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnRemediationConfiguration.StaticValueProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RemediationParameterValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-config.CfnRemediationConfiguration.ResourceValueProperty",
        jsii_struct_bases=[],
        name_mapping={"value": "value"},
    )
    class ResourceValueProperty:
        def __init__(self, *, value: typing.Optional[builtins.str] = None) -> None:
            '''The dynamic value of the resource.

            :param value: The value is a resource ID.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-resourcevalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_config as config
                
                resource_value_property = config.CfnRemediationConfiguration.ResourceValueProperty(
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e560ba9bb903158fb8112b331d35478a124e7f5d17144bd54f9d0b8ad7241112)
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The value is a resource ID.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-resourcevalue.html#cfn-config-remediationconfiguration-resourcevalue-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-config.CfnRemediationConfiguration.SsmControlsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "concurrent_execution_rate_percentage": "concurrentExecutionRatePercentage",
            "error_percentage": "errorPercentage",
        },
    )
    class SsmControlsProperty:
        def __init__(
            self,
            *,
            concurrent_execution_rate_percentage: typing.Optional[jsii.Number] = None,
            error_percentage: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''AWS Systems Manager (SSM) specific remediation controls.

            :param concurrent_execution_rate_percentage: The maximum percentage of remediation actions allowed to run in parallel on the non-compliant resources for that specific rule. You can specify a percentage, such as 10%. The default value is 10.
            :param error_percentage: The percentage of errors that are allowed before SSM stops running automations on non-compliant resources for that specific rule. You can specify a percentage of errors, for example 10%. If you do not specifiy a percentage, the default is 50%. For example, if you set the ErrorPercentage to 40% for 10 non-compliant resources, then SSM stops running the automations when the fifth error is received.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-ssmcontrols.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_config as config
                
                ssm_controls_property = config.CfnRemediationConfiguration.SsmControlsProperty(
                    concurrent_execution_rate_percentage=123,
                    error_percentage=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9f1a4bf4f23bb3618339e4dffbd663e4253f8b970a4c30ccaaf4b6150a74ba7a)
                check_type(argname="argument concurrent_execution_rate_percentage", value=concurrent_execution_rate_percentage, expected_type=type_hints["concurrent_execution_rate_percentage"])
                check_type(argname="argument error_percentage", value=error_percentage, expected_type=type_hints["error_percentage"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if concurrent_execution_rate_percentage is not None:
                self._values["concurrent_execution_rate_percentage"] = concurrent_execution_rate_percentage
            if error_percentage is not None:
                self._values["error_percentage"] = error_percentage

        @builtins.property
        def concurrent_execution_rate_percentage(self) -> typing.Optional[jsii.Number]:
            '''The maximum percentage of remediation actions allowed to run in parallel on the non-compliant resources for that specific rule.

            You can specify a percentage, such as 10%. The default value is 10.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-ssmcontrols.html#cfn-config-remediationconfiguration-ssmcontrols-concurrentexecutionratepercentage
            '''
            result = self._values.get("concurrent_execution_rate_percentage")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def error_percentage(self) -> typing.Optional[jsii.Number]:
            '''The percentage of errors that are allowed before SSM stops running automations on non-compliant resources for that specific rule.

            You can specify a percentage of errors, for example 10%. If you do not specifiy a percentage, the default is 50%. For example, if you set the ErrorPercentage to 40% for 10 non-compliant resources, then SSM stops running the automations when the fifth error is received.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-ssmcontrols.html#cfn-config-remediationconfiguration-ssmcontrols-errorpercentage
            '''
            result = self._values.get("error_percentage")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SsmControlsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-config.CfnRemediationConfiguration.StaticValueProperty",
        jsii_struct_bases=[],
        name_mapping={"values": "values"},
    )
    class StaticValueProperty:
        def __init__(
            self,
            *,
            values: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The static value of the resource.

            :param values: A list of values. For example, the ARN of the assumed role.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-staticvalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_config as config
                
                static_value_property = config.CfnRemediationConfiguration.StaticValueProperty(
                    values=["values"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4d830098cbcf8a4aa85f63e59547d214cdd736b8c0740e7d4039642b2e1ad460)
                check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if values is not None:
                self._values["values"] = values

        @builtins.property
        def values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of values.

            For example, the ARN of the assumed role.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-staticvalue.html#cfn-config-remediationconfiguration-staticvalue-values
            '''
            result = self._values.get("values")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StaticValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-config.CfnRemediationConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "config_rule_name": "configRuleName",
        "target_id": "targetId",
        "target_type": "targetType",
        "automatic": "automatic",
        "execution_controls": "executionControls",
        "maximum_automatic_attempts": "maximumAutomaticAttempts",
        "parameters": "parameters",
        "resource_type": "resourceType",
        "retry_attempt_seconds": "retryAttemptSeconds",
        "target_version": "targetVersion",
    },
)
class CfnRemediationConfigurationProps:
    def __init__(
        self,
        *,
        config_rule_name: builtins.str,
        target_id: builtins.str,
        target_type: builtins.str,
        automatic: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
        execution_controls: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnRemediationConfiguration.ExecutionControlsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        maximum_automatic_attempts: typing.Optional[jsii.Number] = None,
        parameters: typing.Any = None,
        resource_type: typing.Optional[builtins.str] = None,
        retry_attempt_seconds: typing.Optional[jsii.Number] = None,
        target_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnRemediationConfiguration``.

        :param config_rule_name: The name of the AWS Config rule.
        :param target_id: Target ID is the name of the public document.
        :param target_type: The type of the target. Target executes remediation. For example, SSM document.
        :param automatic: The remediation is triggered automatically.
        :param execution_controls: An ExecutionControls object.
        :param maximum_automatic_attempts: The maximum number of failed attempts for auto-remediation. If you do not select a number, the default is 5. For example, if you specify MaximumAutomaticAttempts as 5 with RetryAttemptSeconds as 50 seconds, AWS Config will put a RemediationException on your behalf for the failing resource after the 5th failed attempt within 50 seconds.
        :param parameters: An object of the RemediationParameterValue. For more information, see `RemediationParameterValue <https://docs.aws.amazon.com/config/latest/APIReference/API_RemediationParameterValue.html>`_ . .. epigraph:: The type is a map of strings to RemediationParameterValue.
        :param resource_type: The type of a resource.
        :param retry_attempt_seconds: Maximum time in seconds that AWS Config runs auto-remediation. If you do not select a number, the default is 60 seconds. For example, if you specify RetryAttemptSeconds as 50 seconds and MaximumAutomaticAttempts as 5, AWS Config will run auto-remediations 5 times within 50 seconds before throwing an exception.
        :param target_version: Version of the target. For example, version of the SSM document. .. epigraph:: If you make backward incompatible changes to the SSM document, you must call PutRemediationConfiguration API again to ensure the remediations can run.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_config as config
            
            # parameters: Any
            
            cfn_remediation_configuration_props = config.CfnRemediationConfigurationProps(
                config_rule_name="configRuleName",
                target_id="targetId",
                target_type="targetType",
            
                # the properties below are optional
                automatic=False,
                execution_controls=config.CfnRemediationConfiguration.ExecutionControlsProperty(
                    ssm_controls=config.CfnRemediationConfiguration.SsmControlsProperty(
                        concurrent_execution_rate_percentage=123,
                        error_percentage=123
                    )
                ),
                maximum_automatic_attempts=123,
                parameters=parameters,
                resource_type="resourceType",
                retry_attempt_seconds=123,
                target_version="targetVersion"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e76eab5e10174eda1264da2000216cbde6cc9219074242d28450210ec1afeef4)
            check_type(argname="argument config_rule_name", value=config_rule_name, expected_type=type_hints["config_rule_name"])
            check_type(argname="argument target_id", value=target_id, expected_type=type_hints["target_id"])
            check_type(argname="argument target_type", value=target_type, expected_type=type_hints["target_type"])
            check_type(argname="argument automatic", value=automatic, expected_type=type_hints["automatic"])
            check_type(argname="argument execution_controls", value=execution_controls, expected_type=type_hints["execution_controls"])
            check_type(argname="argument maximum_automatic_attempts", value=maximum_automatic_attempts, expected_type=type_hints["maximum_automatic_attempts"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
            check_type(argname="argument retry_attempt_seconds", value=retry_attempt_seconds, expected_type=type_hints["retry_attempt_seconds"])
            check_type(argname="argument target_version", value=target_version, expected_type=type_hints["target_version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "config_rule_name": config_rule_name,
            "target_id": target_id,
            "target_type": target_type,
        }
        if automatic is not None:
            self._values["automatic"] = automatic
        if execution_controls is not None:
            self._values["execution_controls"] = execution_controls
        if maximum_automatic_attempts is not None:
            self._values["maximum_automatic_attempts"] = maximum_automatic_attempts
        if parameters is not None:
            self._values["parameters"] = parameters
        if resource_type is not None:
            self._values["resource_type"] = resource_type
        if retry_attempt_seconds is not None:
            self._values["retry_attempt_seconds"] = retry_attempt_seconds
        if target_version is not None:
            self._values["target_version"] = target_version

    @builtins.property
    def config_rule_name(self) -> builtins.str:
        '''The name of the AWS Config rule.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html#cfn-config-remediationconfiguration-configrulename
        '''
        result = self._values.get("config_rule_name")
        assert result is not None, "Required property 'config_rule_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_id(self) -> builtins.str:
        '''Target ID is the name of the public document.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html#cfn-config-remediationconfiguration-targetid
        '''
        result = self._values.get("target_id")
        assert result is not None, "Required property 'target_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_type(self) -> builtins.str:
        '''The type of the target.

        Target executes remediation. For example, SSM document.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html#cfn-config-remediationconfiguration-targettype
        '''
        result = self._values.get("target_type")
        assert result is not None, "Required property 'target_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def automatic(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
        '''The remediation is triggered automatically.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html#cfn-config-remediationconfiguration-automatic
        '''
        result = self._values.get("automatic")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

    @builtins.property
    def execution_controls(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnRemediationConfiguration.ExecutionControlsProperty]]:
        '''An ExecutionControls object.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html#cfn-config-remediationconfiguration-executioncontrols
        '''
        result = self._values.get("execution_controls")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnRemediationConfiguration.ExecutionControlsProperty]], result)

    @builtins.property
    def maximum_automatic_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of failed attempts for auto-remediation. If you do not select a number, the default is 5.

        For example, if you specify MaximumAutomaticAttempts as 5 with RetryAttemptSeconds as 50 seconds, AWS Config will put a RemediationException on your behalf for the failing resource after the 5th failed attempt within 50 seconds.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html#cfn-config-remediationconfiguration-maximumautomaticattempts
        '''
        result = self._values.get("maximum_automatic_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def parameters(self) -> typing.Any:
        '''An object of the RemediationParameterValue. For more information, see `RemediationParameterValue <https://docs.aws.amazon.com/config/latest/APIReference/API_RemediationParameterValue.html>`_ .

        .. epigraph::

           The type is a map of strings to RemediationParameterValue.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html#cfn-config-remediationconfiguration-parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Any, result)

    @builtins.property
    def resource_type(self) -> typing.Optional[builtins.str]:
        '''The type of a resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html#cfn-config-remediationconfiguration-resourcetype
        '''
        result = self._values.get("resource_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retry_attempt_seconds(self) -> typing.Optional[jsii.Number]:
        '''Maximum time in seconds that AWS Config runs auto-remediation.

        If you do not select a number, the default is 60 seconds.

        For example, if you specify RetryAttemptSeconds as 50 seconds and MaximumAutomaticAttempts as 5, AWS Config will run auto-remediations 5 times within 50 seconds before throwing an exception.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html#cfn-config-remediationconfiguration-retryattemptseconds
        '''
        result = self._values.get("retry_attempt_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def target_version(self) -> typing.Optional[builtins.str]:
        '''Version of the target. For example, version of the SSM document.

        .. epigraph::

           If you make backward incompatible changes to the SSM document, you must call PutRemediationConfiguration API again to ensure the remediations can run.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html#cfn-config-remediationconfiguration-targetversion
        '''
        result = self._values.get("target_version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRemediationConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnStoredQuery(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-config.CfnStoredQuery",
):
    '''A CloudFormation ``AWS::Config::StoredQuery``.

    Provides the details of a stored query.

    :cloudformationResource: AWS::Config::StoredQuery
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-storedquery.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_config as config
        
        cfn_stored_query = config.CfnStoredQuery(self, "MyCfnStoredQuery",
            query_expression="queryExpression",
            query_name="queryName",
        
            # the properties below are optional
            query_description="queryDescription",
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
        query_expression: builtins.str,
        query_name: builtins.str,
        query_description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Config::StoredQuery``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param query_expression: The expression of the query. For example, ``SELECT resourceId, resourceType, supplementaryConfiguration.BucketVersioningConfiguration.status WHERE resourceType = 'AWS::S3::Bucket' AND supplementaryConfiguration.BucketVersioningConfiguration.status = 'Off'.``
        :param query_name: The name of the query.
        :param query_description: A unique description for the query.
        :param tags: An array of key-value pairs to apply to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bed95671ca6fdaace458fd531821ca6f617f7389c7c8d1780cf04bbcaef087e6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnStoredQueryProps(
            query_expression=query_expression,
            query_name=query_name,
            query_description=query_description,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c62229555e9a810b0a31ef9d721ad0f5497942327b87db8913eb5520aa7d819e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__77874ee40e947f394072b8d96c480283ee8ff5da8ba31ed7507fcdd5bfd69c54)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrQueryArn")
    def attr_query_arn(self) -> builtins.str:
        '''Amazon Resource Name (ARN) of the query.

        For example, arn:partition:service:region:account-id:resource-type/resource-name/resource-id.

        :cloudformationAttribute: QueryArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrQueryArn"))

    @builtins.property
    @jsii.member(jsii_name="attrQueryId")
    def attr_query_id(self) -> builtins.str:
        '''The ID of the query.

        :cloudformationAttribute: QueryId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrQueryId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _aws_cdk_core_f4b25747.TagManager:
        '''An array of key-value pairs to apply to this resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-storedquery.html#cfn-config-storedquery-tags
        '''
        return typing.cast(_aws_cdk_core_f4b25747.TagManager, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="queryExpression")
    def query_expression(self) -> builtins.str:
        '''The expression of the query.

        For example, ``SELECT resourceId, resourceType, supplementaryConfiguration.BucketVersioningConfiguration.status WHERE resourceType = 'AWS::S3::Bucket' AND supplementaryConfiguration.BucketVersioningConfiguration.status = 'Off'.``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-storedquery.html#cfn-config-storedquery-queryexpression
        '''
        return typing.cast(builtins.str, jsii.get(self, "queryExpression"))

    @query_expression.setter
    def query_expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__749cfd407c6f57d5a88c1f73901f65cea002c9e0c7809dbaa028ae54c656865b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryExpression", value)

    @builtins.property
    @jsii.member(jsii_name="queryName")
    def query_name(self) -> builtins.str:
        '''The name of the query.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-storedquery.html#cfn-config-storedquery-queryname
        '''
        return typing.cast(builtins.str, jsii.get(self, "queryName"))

    @query_name.setter
    def query_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__726cb093f586df14a3cbaa4a8ead19eadb4662844d460e2954752bbf0fd0d924)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryName", value)

    @builtins.property
    @jsii.member(jsii_name="queryDescription")
    def query_description(self) -> typing.Optional[builtins.str]:
        '''A unique description for the query.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-storedquery.html#cfn-config-storedquery-querydescription
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryDescription"))

    @query_description.setter
    def query_description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43a2a66de066398f31cfe3d0d336eb0b8a9e7957ca4291a357bce806d5d05610)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryDescription", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-config.CfnStoredQueryProps",
    jsii_struct_bases=[],
    name_mapping={
        "query_expression": "queryExpression",
        "query_name": "queryName",
        "query_description": "queryDescription",
        "tags": "tags",
    },
)
class CfnStoredQueryProps:
    def __init__(
        self,
        *,
        query_expression: builtins.str,
        query_name: builtins.str,
        query_description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnStoredQuery``.

        :param query_expression: The expression of the query. For example, ``SELECT resourceId, resourceType, supplementaryConfiguration.BucketVersioningConfiguration.status WHERE resourceType = 'AWS::S3::Bucket' AND supplementaryConfiguration.BucketVersioningConfiguration.status = 'Off'.``
        :param query_name: The name of the query.
        :param query_description: A unique description for the query.
        :param tags: An array of key-value pairs to apply to this resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-storedquery.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_config as config
            
            cfn_stored_query_props = config.CfnStoredQueryProps(
                query_expression="queryExpression",
                query_name="queryName",
            
                # the properties below are optional
                query_description="queryDescription",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9154d511891bb2cc1103c89588295e98d82eeafe7a0c5efe8a2ceda52ae648e7)
            check_type(argname="argument query_expression", value=query_expression, expected_type=type_hints["query_expression"])
            check_type(argname="argument query_name", value=query_name, expected_type=type_hints["query_name"])
            check_type(argname="argument query_description", value=query_description, expected_type=type_hints["query_description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "query_expression": query_expression,
            "query_name": query_name,
        }
        if query_description is not None:
            self._values["query_description"] = query_description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def query_expression(self) -> builtins.str:
        '''The expression of the query.

        For example, ``SELECT resourceId, resourceType, supplementaryConfiguration.BucketVersioningConfiguration.status WHERE resourceType = 'AWS::S3::Bucket' AND supplementaryConfiguration.BucketVersioningConfiguration.status = 'Off'.``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-storedquery.html#cfn-config-storedquery-queryexpression
        '''
        result = self._values.get("query_expression")
        assert result is not None, "Required property 'query_expression' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def query_name(self) -> builtins.str:
        '''The name of the query.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-storedquery.html#cfn-config-storedquery-queryname
        '''
        result = self._values.get("query_name")
        assert result is not None, "Required property 'query_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def query_description(self) -> typing.Optional[builtins.str]:
        '''A unique description for the query.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-storedquery.html#cfn-config-storedquery-querydescription
        '''
        result = self._values.get("query_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]]:
        '''An array of key-value pairs to apply to this resource.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-storedquery.html#cfn-config-storedquery-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStoredQueryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="@aws-cdk/aws-config.IRule")
class IRule(_aws_cdk_core_f4b25747.IResource, typing_extensions.Protocol):
    '''Interface representing an AWS Config rule.'''

    @builtins.property
    @jsii.member(jsii_name="configRuleName")
    def config_rule_name(self) -> builtins.str:
        '''The name of the rule.

        :attribute: true
        '''
        ...

    @jsii.member(jsii_name="onComplianceChange")
    def on_compliance_change(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_aws_cdk_aws_events_efcdfa54.EventPattern, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[_aws_cdk_aws_events_efcdfa54.IRuleTarget] = None,
    ) -> _aws_cdk_aws_events_efcdfa54.Rule:
        '''Defines a EventBridge event rule which triggers for rule compliance events.

        :param id: -
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        ...

    @jsii.member(jsii_name="onEvent")
    def on_event(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_aws_cdk_aws_events_efcdfa54.EventPattern, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[_aws_cdk_aws_events_efcdfa54.IRuleTarget] = None,
    ) -> _aws_cdk_aws_events_efcdfa54.Rule:
        '''Defines an EventBridge event rule which triggers for rule events.

        Use
        ``rule.addEventPattern(pattern)`` to specify a filter.

        :param id: -
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        ...

    @jsii.member(jsii_name="onReEvaluationStatus")
    def on_re_evaluation_status(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_aws_cdk_aws_events_efcdfa54.EventPattern, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[_aws_cdk_aws_events_efcdfa54.IRuleTarget] = None,
    ) -> _aws_cdk_aws_events_efcdfa54.Rule:
        '''Defines a EventBridge event rule which triggers for rule re-evaluation status events.

        :param id: -
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        ...


class _IRuleProxy(
    jsii.proxy_for(_aws_cdk_core_f4b25747.IResource), # type: ignore[misc]
):
    '''Interface representing an AWS Config rule.'''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-config.IRule"

    @builtins.property
    @jsii.member(jsii_name="configRuleName")
    def config_rule_name(self) -> builtins.str:
        '''The name of the rule.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "configRuleName"))

    @jsii.member(jsii_name="onComplianceChange")
    def on_compliance_change(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_aws_cdk_aws_events_efcdfa54.EventPattern, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[_aws_cdk_aws_events_efcdfa54.IRuleTarget] = None,
    ) -> _aws_cdk_aws_events_efcdfa54.Rule:
        '''Defines a EventBridge event rule which triggers for rule compliance events.

        :param id: -
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e2ef8a1a04bb9f7791ace4e0f281292b7b42fd2f28453ec5572478286c23994)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _aws_cdk_aws_events_efcdfa54.OnEventOptions(
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
            target=target,
        )

        return typing.cast(_aws_cdk_aws_events_efcdfa54.Rule, jsii.invoke(self, "onComplianceChange", [id, options]))

    @jsii.member(jsii_name="onEvent")
    def on_event(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_aws_cdk_aws_events_efcdfa54.EventPattern, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[_aws_cdk_aws_events_efcdfa54.IRuleTarget] = None,
    ) -> _aws_cdk_aws_events_efcdfa54.Rule:
        '''Defines an EventBridge event rule which triggers for rule events.

        Use
        ``rule.addEventPattern(pattern)`` to specify a filter.

        :param id: -
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__576370f225a870a0cc4811380c4eabef037a05f2601206885795f104f94bd2fa)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _aws_cdk_aws_events_efcdfa54.OnEventOptions(
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
            target=target,
        )

        return typing.cast(_aws_cdk_aws_events_efcdfa54.Rule, jsii.invoke(self, "onEvent", [id, options]))

    @jsii.member(jsii_name="onReEvaluationStatus")
    def on_re_evaluation_status(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_aws_cdk_aws_events_efcdfa54.EventPattern, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[_aws_cdk_aws_events_efcdfa54.IRuleTarget] = None,
    ) -> _aws_cdk_aws_events_efcdfa54.Rule:
        '''Defines a EventBridge event rule which triggers for rule re-evaluation status events.

        :param id: -
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3de891820673c0218415a0ed7d1fc22835f389d276e993acc45ffc336aa06aac)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _aws_cdk_aws_events_efcdfa54.OnEventOptions(
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
            target=target,
        )

        return typing.cast(_aws_cdk_aws_events_efcdfa54.Rule, jsii.invoke(self, "onReEvaluationStatus", [id, options]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRule).__jsii_proxy_class__ = lambda : _IRuleProxy


@jsii.implements(IRule)
class ManagedRule(
    _aws_cdk_core_f4b25747.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-config.ManagedRule",
):
    '''A new managed rule.

    :resource: AWS::Config::ConfigRule
    :exampleMetadata: infused

    Example::

        # https://docs.aws.amazon.com/config/latest/developerguide/access-keys-rotated.html
        config.ManagedRule(self, "AccessKeysRotated",
            identifier=config.ManagedRuleIdentifiers.ACCESS_KEYS_ROTATED,
            input_parameters={
                "max_access_key_age": 60
            },
        
            # default is 24 hours
            maximum_execution_frequency=config.MaximumExecutionFrequency.TWELVE_HOURS
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        identifier: builtins.str,
        config_rule_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        maximum_execution_frequency: typing.Optional["MaximumExecutionFrequency"] = None,
        rule_scope: typing.Optional["RuleScope"] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param identifier: The identifier of the AWS managed rule.
        :param config_rule_name: A name for the AWS Config rule. Default: - CloudFormation generated name
        :param description: A description about this AWS Config rule. Default: - No description
        :param input_parameters: Input parameter values that are passed to the AWS Config rule. Default: - No input parameters
        :param maximum_execution_frequency: The maximum frequency at which the AWS Config rule runs evaluations. Default: MaximumExecutionFrequency.TWENTY_FOUR_HOURS
        :param rule_scope: Defines which resources trigger an evaluation for an AWS Config rule. Default: - evaluations for the rule are triggered when any resource in the recording group changes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__beb7233dcde14af055dfba051306a71fe86357693e267f2c540e81b863f1b54a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ManagedRuleProps(
            identifier=identifier,
            config_rule_name=config_rule_name,
            description=description,
            input_parameters=input_parameters,
            maximum_execution_frequency=maximum_execution_frequency,
            rule_scope=rule_scope,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromConfigRuleName")
    @builtins.classmethod
    def from_config_rule_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        config_rule_name: builtins.str,
    ) -> IRule:
        '''Imports an existing rule.

        :param scope: -
        :param id: -
        :param config_rule_name: the name of the rule.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e552b5124862de104ba5f6ed449ae86b76651764caa3d146db229aec6dfe1bb1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument config_rule_name", value=config_rule_name, expected_type=type_hints["config_rule_name"])
        return typing.cast(IRule, jsii.sinvoke(cls, "fromConfigRuleName", [scope, id, config_rule_name]))

    @jsii.member(jsii_name="onComplianceChange")
    def on_compliance_change(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_aws_cdk_aws_events_efcdfa54.EventPattern, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[_aws_cdk_aws_events_efcdfa54.IRuleTarget] = None,
    ) -> _aws_cdk_aws_events_efcdfa54.Rule:
        '''Defines an EventBridge event rule which triggers for rule compliance events.

        :param id: -
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43163b798774fd8cea5b4f2ca4f8d3e25000552eba3360cf963727ad3e600880)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _aws_cdk_aws_events_efcdfa54.OnEventOptions(
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
            target=target,
        )

        return typing.cast(_aws_cdk_aws_events_efcdfa54.Rule, jsii.invoke(self, "onComplianceChange", [id, options]))

    @jsii.member(jsii_name="onEvent")
    def on_event(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_aws_cdk_aws_events_efcdfa54.EventPattern, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[_aws_cdk_aws_events_efcdfa54.IRuleTarget] = None,
    ) -> _aws_cdk_aws_events_efcdfa54.Rule:
        '''Defines an EventBridge event rule which triggers for rule events.

        Use
        ``rule.addEventPattern(pattern)`` to specify a filter.

        :param id: -
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9e32d950364ffb20c68ea94f8efd7ddc6a7d61f9f2c2d8ba52f97ff600e8776)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _aws_cdk_aws_events_efcdfa54.OnEventOptions(
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
            target=target,
        )

        return typing.cast(_aws_cdk_aws_events_efcdfa54.Rule, jsii.invoke(self, "onEvent", [id, options]))

    @jsii.member(jsii_name="onReEvaluationStatus")
    def on_re_evaluation_status(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_aws_cdk_aws_events_efcdfa54.EventPattern, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[_aws_cdk_aws_events_efcdfa54.IRuleTarget] = None,
    ) -> _aws_cdk_aws_events_efcdfa54.Rule:
        '''Defines an EventBridge event rule which triggers for rule re-evaluation status events.

        :param id: -
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a73bc9b5ffc0291341ab1444151356eb4dbc32b663275a57ad775b20f4d2ef0)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _aws_cdk_aws_events_efcdfa54.OnEventOptions(
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
            target=target,
        )

        return typing.cast(_aws_cdk_aws_events_efcdfa54.Rule, jsii.invoke(self, "onReEvaluationStatus", [id, options]))

    @builtins.property
    @jsii.member(jsii_name="configRuleArn")
    def config_rule_arn(self) -> builtins.str:
        '''The arn of the rule.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "configRuleArn"))

    @builtins.property
    @jsii.member(jsii_name="configRuleComplianceType")
    def config_rule_compliance_type(self) -> builtins.str:
        '''The compliance status of the rule.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "configRuleComplianceType"))

    @builtins.property
    @jsii.member(jsii_name="configRuleId")
    def config_rule_id(self) -> builtins.str:
        '''The id of the rule.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "configRuleId"))

    @builtins.property
    @jsii.member(jsii_name="configRuleName")
    def config_rule_name(self) -> builtins.str:
        '''The name of the rule.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "configRuleName"))

    @builtins.property
    @jsii.member(jsii_name="isCustomWithChanges")
    def _is_custom_with_changes(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "isCustomWithChanges"))

    @_is_custom_with_changes.setter
    def _is_custom_with_changes(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2f20c670458b15ce78f700dcb4d585b9d6b62be820e131913dde2b1a218f836)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isCustomWithChanges", value)

    @builtins.property
    @jsii.member(jsii_name="isManaged")
    def _is_managed(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "isManaged"))

    @_is_managed.setter
    def _is_managed(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9125ecd42861d285e4c2b6421f67f5e127f89ed0f26458982f5b0ebc9a8678e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isManaged", value)

    @builtins.property
    @jsii.member(jsii_name="ruleScope")
    def _rule_scope(self) -> typing.Optional["RuleScope"]:
        return typing.cast(typing.Optional["RuleScope"], jsii.get(self, "ruleScope"))

    @_rule_scope.setter
    def _rule_scope(self, value: typing.Optional["RuleScope"]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7065b8018e00f1c5ccacdbd0d149628eaf3073e0d8d54062d0bbba5729e385ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleScope", value)


class ManagedRuleIdentifiers(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-config.ManagedRuleIdentifiers",
):
    '''Managed rules that are supported by AWS Config.

    :see: https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html
    :exampleMetadata: infused

    Example::

        # https://docs.aws.amazon.com/config/latest/developerguide/access-keys-rotated.html
        config.ManagedRule(self, "AccessKeysRotated",
            identifier=config.ManagedRuleIdentifiers.ACCESS_KEYS_ROTATED,
            input_parameters={
                "max_access_key_age": 60
            },
        
            # default is 24 hours
            maximum_execution_frequency=config.MaximumExecutionFrequency.TWELVE_HOURS
        )
    '''

    @jsii.python.classproperty
    @jsii.member(jsii_name="ACCESS_KEYS_ROTATED")
    def ACCESS_KEYS_ROTATED(cls) -> builtins.str:
        '''Checks whether the active access keys are rotated within the number of days specified in maxAccessKeyAge.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/access-keys-rotated.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ACCESS_KEYS_ROTATED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ACCOUNT_PART_OF_ORGANIZATIONS")
    def ACCOUNT_PART_OF_ORGANIZATIONS(cls) -> builtins.str:
        '''Checks whether AWS account is part of AWS Organizations.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/account-part-of-organizations.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ACCOUNT_PART_OF_ORGANIZATIONS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ACM_CERTIFICATE_EXPIRATION_CHECK")
    def ACM_CERTIFICATE_EXPIRATION_CHECK(cls) -> builtins.str:
        '''Checks whether ACM Certificates in your account are marked for expiration within the specified number of days.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/acm-certificate-expiration-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ACM_CERTIFICATE_EXPIRATION_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ALB_HTTP_DROP_INVALID_HEADER_ENABLED")
    def ALB_HTTP_DROP_INVALID_HEADER_ENABLED(cls) -> builtins.str:
        '''Checks if rule evaluates Application Load Balancers (ALBs) to ensure they are configured to drop http headers.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/alb-http-drop-invalid-header-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ALB_HTTP_DROP_INVALID_HEADER_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ALB_HTTP_TO_HTTPS_REDIRECTION_CHECK")
    def ALB_HTTP_TO_HTTPS_REDIRECTION_CHECK(cls) -> builtins.str:
        '''Checks whether HTTP to HTTPS redirection is configured on all HTTP listeners of Application Load Balancer.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/alb-http-to-https-redirection-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ALB_HTTP_TO_HTTPS_REDIRECTION_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ALB_WAF_ENABLED")
    def ALB_WAF_ENABLED(cls) -> builtins.str:
        '''Checks if Web Application Firewall (WAF) is enabled on Application Load Balancers (ALBs).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/alb-waf-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ALB_WAF_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="API_GW_CACHE_ENABLED_AND_ENCRYPTED")
    def API_GW_CACHE_ENABLED_AND_ENCRYPTED(cls) -> builtins.str:
        '''Checks that all methods in Amazon API Gateway stages have caching enabled and encrypted.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/api-gw-cache-enabled-and-encrypted.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "API_GW_CACHE_ENABLED_AND_ENCRYPTED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="API_GW_ENDPOINT_TYPE_CHECK")
    def API_GW_ENDPOINT_TYPE_CHECK(cls) -> builtins.str:
        '''Checks that Amazon API Gateway APIs are of the type specified in the rule parameter endpointConfigurationType.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/api-gw-endpoint-type-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "API_GW_ENDPOINT_TYPE_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="API_GW_EXECUTION_LOGGING_ENABLED")
    def API_GW_EXECUTION_LOGGING_ENABLED(cls) -> builtins.str:
        '''Checks that all methods in Amazon API Gateway stage has logging enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/api-gw-execution-logging-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "API_GW_EXECUTION_LOGGING_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="APPROVED_AMIS_BY_ID")
    def APPROVED_AMIS_BY_ID(cls) -> builtins.str:
        '''Checks whether running instances are using specified AMIs.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/approved-amis-by-id.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "APPROVED_AMIS_BY_ID"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="APPROVED_AMIS_BY_TAG")
    def APPROVED_AMIS_BY_TAG(cls) -> builtins.str:
        '''Checks whether running instances are using specified AMIs.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/approved-amis-by-tag.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "APPROVED_AMIS_BY_TAG"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AUTOSCALING_GROUP_ELB_HEALTHCHECK_REQUIRED")
    def AUTOSCALING_GROUP_ELB_HEALTHCHECK_REQUIRED(cls) -> builtins.str:
        '''Checks whether your Auto Scaling groups that are associated with a load balancer are using Elastic Load Balancing health checks.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/autoscaling-group-elb-healthcheck-required.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "AUTOSCALING_GROUP_ELB_HEALTHCHECK_REQUIRED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_TRAIL_CLOUD_WATCH_LOGS_ENABLED")
    def CLOUD_TRAIL_CLOUD_WATCH_LOGS_ENABLED(cls) -> builtins.str:
        '''Checks whether AWS CloudTrail trails are configured to send logs to Amazon CloudWatch Logs.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cloud-trail-cloud-watch-logs-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUD_TRAIL_CLOUD_WATCH_LOGS_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_TRAIL_ENABLED")
    def CLOUD_TRAIL_ENABLED(cls) -> builtins.str:
        '''Checks whether AWS CloudTrail is enabled in your AWS account.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cloudtrail-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUD_TRAIL_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_TRAIL_ENCRYPTION_ENABLED")
    def CLOUD_TRAIL_ENCRYPTION_ENABLED(cls) -> builtins.str:
        '''Checks whether AWS CloudTrail is configured to use the server side encryption (SSE) AWS Key Management Service (AWS KMS) customer master key (CMK) encryption.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cloud-trail-encryption-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUD_TRAIL_ENCRYPTION_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_TRAIL_LOG_FILE_VALIDATION_ENABLED")
    def CLOUD_TRAIL_LOG_FILE_VALIDATION_ENABLED(cls) -> builtins.str:
        '''Checks whether AWS CloudTrail creates a signed digest file with logs.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cloud-trail-log-file-validation-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUD_TRAIL_LOG_FILE_VALIDATION_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDFORMATION_STACK_DRIFT_DETECTION_CHECK")
    def CLOUDFORMATION_STACK_DRIFT_DETECTION_CHECK(cls) -> builtins.str:
        '''Checks whether an AWS CloudFormation stack's actual configuration differs, or has drifted, from it's expected configuration.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cloudformation-stack-drift-detection-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUDFORMATION_STACK_DRIFT_DETECTION_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDFORMATION_STACK_NOTIFICATION_CHECK")
    def CLOUDFORMATION_STACK_NOTIFICATION_CHECK(cls) -> builtins.str:
        '''Checks whether your CloudFormation stacks are sending event notifications to an SNS topic.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cloudformation-stack-notification-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUDFORMATION_STACK_NOTIFICATION_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDFRONT_DEFAULT_ROOT_OBJECT_CONFIGURED")
    def CLOUDFRONT_DEFAULT_ROOT_OBJECT_CONFIGURED(cls) -> builtins.str:
        '''Checks if an Amazon CloudFront distribution is configured to return a specific object that is the default root object.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cloudfront-default-root-object-configured.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUDFRONT_DEFAULT_ROOT_OBJECT_CONFIGURED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDFRONT_ORIGIN_ACCESS_IDENTITY_ENABLED")
    def CLOUDFRONT_ORIGIN_ACCESS_IDENTITY_ENABLED(cls) -> builtins.str:
        '''Checks that Amazon CloudFront distribution with Amazon S3 Origin type has Origin Access Identity (OAI) configured.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cloudfront-origin-access-identity-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUDFRONT_ORIGIN_ACCESS_IDENTITY_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDFRONT_ORIGIN_FAILOVER_ENABLED")
    def CLOUDFRONT_ORIGIN_FAILOVER_ENABLED(cls) -> builtins.str:
        '''Checks whether an origin group is configured for the distribution of at least 2 origins in the origin group for Amazon CloudFront.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cloudfront-origin-failover-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUDFRONT_ORIGIN_FAILOVER_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDFRONT_SNI_ENABLED")
    def CLOUDFRONT_SNI_ENABLED(cls) -> builtins.str:
        '''Checks if Amazon CloudFront distributions are using a custom SSL certificate and are configured to use SNI to serve HTTPS requests.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cloudfront-sni-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUDFRONT_SNI_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDFRONT_VIEWER_POLICY_HTTPS")
    def CLOUDFRONT_VIEWER_POLICY_HTTPS(cls) -> builtins.str:
        '''Checks whether your Amazon CloudFront distributions use HTTPS (directly or via a redirection).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cloudfront-viewer-policy-https.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUDFRONT_VIEWER_POLICY_HTTPS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDTRAIL_MULTI_REGION_ENABLED")
    def CLOUDTRAIL_MULTI_REGION_ENABLED(cls) -> builtins.str:
        '''Checks that there is at least one multi-region AWS CloudTrail.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/multi-region-cloudtrail-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUDTRAIL_MULTI_REGION_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDTRAIL_S3_DATAEVENTS_ENABLED")
    def CLOUDTRAIL_S3_DATAEVENTS_ENABLED(cls) -> builtins.str:
        '''Checks whether at least one AWS CloudTrail trail is logging Amazon S3 data events for all S3 buckets.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cloudtrail-s3-dataevents-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUDTRAIL_S3_DATAEVENTS_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDTRAIL_SECURITY_TRAIL_ENABLED")
    def CLOUDTRAIL_SECURITY_TRAIL_ENABLED(cls) -> builtins.str:
        '''Checks that there is at least one AWS CloudTrail trail defined with security best practices.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cloudtrail-security-trail-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUDTRAIL_SECURITY_TRAIL_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDWATCH_ALARM_ACTION_CHECK")
    def CLOUDWATCH_ALARM_ACTION_CHECK(cls) -> builtins.str:
        '''Checks whether CloudWatch alarms have at least one alarm action, one INSUFFICIENT_DATA action, or one OK action enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cloudwatch-alarm-action-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUDWATCH_ALARM_ACTION_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDWATCH_ALARM_RESOURCE_CHECK")
    def CLOUDWATCH_ALARM_RESOURCE_CHECK(cls) -> builtins.str:
        '''Checks whether the specified resource type has a CloudWatch alarm for the specified metric.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cloudwatch-alarm-resource-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUDWATCH_ALARM_RESOURCE_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDWATCH_ALARM_SETTINGS_CHECK")
    def CLOUDWATCH_ALARM_SETTINGS_CHECK(cls) -> builtins.str:
        '''Checks whether CloudWatch alarms with the given metric name have the specified settings.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cloudwatch-alarm-settings-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUDWATCH_ALARM_SETTINGS_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDWATCH_LOG_GROUP_ENCRYPTED")
    def CLOUDWATCH_LOG_GROUP_ENCRYPTED(cls) -> builtins.str:
        '''Checks whether a log group in Amazon CloudWatch Logs is encrypted with a AWS Key Management Service (KMS) managed Customer Master Keys (CMK).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cloudwatch-log-group-encrypted.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUDWATCH_LOG_GROUP_ENCRYPTED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CMK_BACKING_KEY_ROTATION_ENABLED")
    def CMK_BACKING_KEY_ROTATION_ENABLED(cls) -> builtins.str:
        '''Checks that key rotation is enabled for each key and matches to the key ID of the customer created customer master key (CMK).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cmk-backing-key-rotation-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CMK_BACKING_KEY_ROTATION_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CODEBUILD_PROJECT_ENVVAR_AWSCRED_CHECK")
    def CODEBUILD_PROJECT_ENVVAR_AWSCRED_CHECK(cls) -> builtins.str:
        '''Checks whether the project contains environment variables AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/codebuild-project-envvar-awscred-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CODEBUILD_PROJECT_ENVVAR_AWSCRED_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CODEBUILD_PROJECT_SOURCE_REPO_URL_CHECK")
    def CODEBUILD_PROJECT_SOURCE_REPO_URL_CHECK(cls) -> builtins.str:
        '''Checks whether the GitHub or Bitbucket source repository URL contains either personal access tokens or user name and password.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/codebuild-project-source-repo-url-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CODEBUILD_PROJECT_SOURCE_REPO_URL_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CODEPIPELINE_DEPLOYMENT_COUNT_CHECK")
    def CODEPIPELINE_DEPLOYMENT_COUNT_CHECK(cls) -> builtins.str:
        '''Checks whether the first deployment stage of the AWS CodePipeline performs more than one deployment.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/codepipeline-deployment-count-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CODEPIPELINE_DEPLOYMENT_COUNT_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CODEPIPELINE_REGION_FANOUT_CHECK")
    def CODEPIPELINE_REGION_FANOUT_CHECK(cls) -> builtins.str:
        '''Checks whether each stage in the AWS CodePipeline deploys to more than N times the number of the regions the AWS CodePipeline has deployed in all the previous combined stages, where N is the region fanout number.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/codepipeline-region-fanout-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CODEPIPELINE_REGION_FANOUT_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CW_LOGGROUP_RETENTION_PERIOD_CHECK")
    def CW_LOGGROUP_RETENTION_PERIOD_CHECK(cls) -> builtins.str:
        '''Checks whether Amazon CloudWatch LogGroup retention period is set to specific number of days.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cw-loggroup-retention-period-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CW_LOGGROUP_RETENTION_PERIOD_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DAX_ENCRYPTION_ENABLED")
    def DAX_ENCRYPTION_ENABLED(cls) -> builtins.str:
        '''Checks that DynamoDB Accelerator (DAX) clusters are encrypted.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/dax-encryption-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "DAX_ENCRYPTION_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DMS_REPLICATION_NOT_PUBLIC")
    def DMS_REPLICATION_NOT_PUBLIC(cls) -> builtins.str:
        '''Checks whether AWS Database Migration Service replication instances are public.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/dms-replication-not-public.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "DMS_REPLICATION_NOT_PUBLIC"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DYNAMODB_AUTOSCALING_ENABLED")
    def DYNAMODB_AUTOSCALING_ENABLED(cls) -> builtins.str:
        '''Checks whether Auto Scaling or On-Demand is enabled on your DynamoDB tables and/or global secondary indexes.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/dynamodb-autoscaling-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "DYNAMODB_AUTOSCALING_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DYNAMODB_IN_BACKUP_PLAN")
    def DYNAMODB_IN_BACKUP_PLAN(cls) -> builtins.str:
        '''Checks whether Amazon DynamoDB table is present in AWS Backup plans.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/dynamodb-in-backup-plan.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "DYNAMODB_IN_BACKUP_PLAN"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DYNAMODB_PITR_ENABLED")
    def DYNAMODB_PITR_ENABLED(cls) -> builtins.str:
        '''Checks that point in time recovery (PITR) is enabled for Amazon DynamoDB tables.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/dynamodb-pitr-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "DYNAMODB_PITR_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DYNAMODB_TABLE_ENCRYPTED_KMS")
    def DYNAMODB_TABLE_ENCRYPTED_KMS(cls) -> builtins.str:
        '''Checks whether Amazon DynamoDB table is encrypted with AWS Key Management Service (KMS).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/dynamodb-table-encrypted-kms.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "DYNAMODB_TABLE_ENCRYPTED_KMS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DYNAMODB_TABLE_ENCRYPTION_ENABLED")
    def DYNAMODB_TABLE_ENCRYPTION_ENABLED(cls) -> builtins.str:
        '''Checks whether the Amazon DynamoDB tables are encrypted and checks their status.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/dynamodb-table-encryption-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "DYNAMODB_TABLE_ENCRYPTION_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DYNAMODB_THROUGHPUT_LIMIT_CHECK")
    def DYNAMODB_THROUGHPUT_LIMIT_CHECK(cls) -> builtins.str:
        '''Checks whether provisioned DynamoDB throughput is approaching the maximum limit for your account.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/dynamodb-throughput-limit-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "DYNAMODB_THROUGHPUT_LIMIT_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EBS_ENCRYPTED_VOLUMES")
    def EBS_ENCRYPTED_VOLUMES(cls) -> builtins.str:
        '''Checks whether the EBS volumes that are in an attached state are encrypted.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/encrypted-volumes.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EBS_ENCRYPTED_VOLUMES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EBS_IN_BACKUP_PLAN")
    def EBS_IN_BACKUP_PLAN(cls) -> builtins.str:
        '''Checks if Amazon Elastic Block Store (Amazon EBS) volumes are added in backup plans of AWS Backup.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ebs-in-backup-plan.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EBS_IN_BACKUP_PLAN"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EBS_OPTIMIZED_INSTANCE")
    def EBS_OPTIMIZED_INSTANCE(cls) -> builtins.str:
        '''Checks whether EBS optimization is enabled for your EC2 instances that can be EBS-optimized.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ebs-optimized-instance.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EBS_OPTIMIZED_INSTANCE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EBS_SNAPSHOT_PUBLIC_RESTORABLE_CHECK")
    def EBS_SNAPSHOT_PUBLIC_RESTORABLE_CHECK(cls) -> builtins.str:
        '''Checks whether Amazon Elastic Block Store snapshots are not publicly restorable.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ebs-snapshot-public-restorable-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EBS_SNAPSHOT_PUBLIC_RESTORABLE_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_DESIRED_INSTANCE_TENANCY")
    def EC2_DESIRED_INSTANCE_TENANCY(cls) -> builtins.str:
        '''Checks instances for specified tenancy.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/desired-instance-tenancy.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_DESIRED_INSTANCE_TENANCY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_DESIRED_INSTANCE_TYPE")
    def EC2_DESIRED_INSTANCE_TYPE(cls) -> builtins.str:
        '''Checks whether your EC2 instances are of the specified instance types.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/desired-instance-type.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_DESIRED_INSTANCE_TYPE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_EBS_ENCRYPTION_BY_DEFAULT")
    def EC2_EBS_ENCRYPTION_BY_DEFAULT(cls) -> builtins.str:
        '''Check that Amazon Elastic Block Store (EBS) encryption is enabled by default.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-ebs-encryption-by-default.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_EBS_ENCRYPTION_BY_DEFAULT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_IMDSV2_CHECK")
    def EC2_IMDSV2_CHECK(cls) -> builtins.str:
        '''Checks whether your Amazon Elastic Compute Cloud (Amazon EC2) instance metadata version is configured with Instance Metadata Service Version 2 (IMDSv2).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-imdsv2-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_IMDSV2_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_INSTANCE_DETAILED_MONITORING_ENABLED")
    def EC2_INSTANCE_DETAILED_MONITORING_ENABLED(cls) -> builtins.str:
        '''Checks whether detailed monitoring is enabled for EC2 instances.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-instance-detailed-monitoring-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_INSTANCE_DETAILED_MONITORING_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_INSTANCE_MANAGED_BY_SSM")
    def EC2_INSTANCE_MANAGED_BY_SSM(cls) -> builtins.str:
        '''Checks whether the Amazon EC2 instances in your account are managed by AWS Systems Manager.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-instance-managed-by-systems-manager.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_INSTANCE_MANAGED_BY_SSM"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_INSTANCE_NO_PUBLIC_IP")
    def EC2_INSTANCE_NO_PUBLIC_IP(cls) -> builtins.str:
        '''Checks whether Amazon Elastic Compute Cloud (Amazon EC2) instances have a public IP association.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-instance-no-public-ip.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_INSTANCE_NO_PUBLIC_IP"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_INSTANCE_PROFILE_ATTACHED")
    def EC2_INSTANCE_PROFILE_ATTACHED(cls) -> builtins.str:
        '''Checks if an Amazon Elastic Compute Cloud (Amazon EC2) instance has an Identity and Access Management (IAM) profile attached to it.

        This rule is NON_COMPLIANT if no IAM profile is
        attached to the Amazon EC2 instance.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-instance-profile-attached.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_INSTANCE_PROFILE_ATTACHED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_INSTANCES_IN_VPC")
    def EC2_INSTANCES_IN_VPC(cls) -> builtins.str:
        '''Checks whether your EC2 instances belong to a virtual private cloud (VPC).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-instances-in-vpc.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_INSTANCES_IN_VPC"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_MANAGED_INSTANCE_APPLICATIONS_BLOCKED")
    def EC2_MANAGED_INSTANCE_APPLICATIONS_BLOCKED(cls) -> builtins.str:
        '''Checks that none of the specified applications are installed on the instance.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-managedinstance-applications-blacklisted.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_MANAGED_INSTANCE_APPLICATIONS_BLOCKED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_MANAGED_INSTANCE_APPLICATIONS_REQUIRED")
    def EC2_MANAGED_INSTANCE_APPLICATIONS_REQUIRED(cls) -> builtins.str:
        '''Checks whether all of the specified applications are installed on the instance.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-managedinstance-applications-required.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_MANAGED_INSTANCE_APPLICATIONS_REQUIRED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_MANAGED_INSTANCE_ASSOCIATION_COMPLIANCE_STATUS_CHECK")
    def EC2_MANAGED_INSTANCE_ASSOCIATION_COMPLIANCE_STATUS_CHECK(cls) -> builtins.str:
        '''Checks whether the compliance status of AWS Systems Manager association compliance is COMPLIANT or NON_COMPLIANT after the association execution on the instance.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-managedinstance-association-compliance-status-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_MANAGED_INSTANCE_ASSOCIATION_COMPLIANCE_STATUS_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_MANAGED_INSTANCE_INVENTORY_BLOCKED")
    def EC2_MANAGED_INSTANCE_INVENTORY_BLOCKED(cls) -> builtins.str:
        '''Checks whether instances managed by AWS Systems Manager are configured to collect blocked inventory types.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-managedinstance-inventory-blacklisted.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_MANAGED_INSTANCE_INVENTORY_BLOCKED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_MANAGED_INSTANCE_PATCH_COMPLIANCE_STATUS_CHECK")
    def EC2_MANAGED_INSTANCE_PATCH_COMPLIANCE_STATUS_CHECK(cls) -> builtins.str:
        '''Checks whether the compliance status of the Amazon EC2 Systems Manager patch compliance is COMPLIANT or NON_COMPLIANT after the patch installation on the instance.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-managedinstance-patch-compliance-status-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_MANAGED_INSTANCE_PATCH_COMPLIANCE_STATUS_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_MANAGED_INSTANCE_PLATFORM_CHECK")
    def EC2_MANAGED_INSTANCE_PLATFORM_CHECK(cls) -> builtins.str:
        '''Checks whether EC2 managed instances have the desired configurations.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-managedinstance-platform-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_MANAGED_INSTANCE_PLATFORM_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_SECURITY_GROUP_ATTACHED_TO_ENI")
    def EC2_SECURITY_GROUP_ATTACHED_TO_ENI(cls) -> builtins.str:
        '''Checks that security groups are attached to Amazon Elastic Compute Cloud (Amazon EC2) instances or to an elastic network interface.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-security-group-attached-to-eni.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_SECURITY_GROUP_ATTACHED_TO_ENI"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_SECURITY_GROUPS_INCOMING_SSH_DISABLED")
    def EC2_SECURITY_GROUPS_INCOMING_SSH_DISABLED(cls) -> builtins.str:
        '''Checks whether the incoming SSH traffic for the security groups is accessible.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/restricted-ssh.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_SECURITY_GROUPS_INCOMING_SSH_DISABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_SECURITY_GROUPS_RESTRICTED_INCOMING_TRAFFIC")
    def EC2_SECURITY_GROUPS_RESTRICTED_INCOMING_TRAFFIC(cls) -> builtins.str:
        '''Checks whether the security groups in use do not allow unrestricted incoming TCP traffic to the specified ports.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/restricted-common-ports.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_SECURITY_GROUPS_RESTRICTED_INCOMING_TRAFFIC"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_STOPPED_INSTANCE")
    def EC2_STOPPED_INSTANCE(cls) -> builtins.str:
        '''Checks whether there are instances stopped for more than the allowed number of days.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-stopped-instance.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_STOPPED_INSTANCE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_VOLUME_INUSE_CHECK")
    def EC2_VOLUME_INUSE_CHECK(cls) -> builtins.str:
        '''Checks whether EBS volumes are attached to EC2 instances.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-volume-inuse-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_VOLUME_INUSE_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EFS_ENCRYPTED_CHECK")
    def EFS_ENCRYPTED_CHECK(cls) -> builtins.str:
        '''hecks whether Amazon Elastic File System (Amazon EFS) is configured to encrypt the file data using AWS Key Management Service (AWS KMS).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/efs-encrypted-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EFS_ENCRYPTED_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EFS_IN_BACKUP_PLAN")
    def EFS_IN_BACKUP_PLAN(cls) -> builtins.str:
        '''Checks whether Amazon Elastic File System (Amazon EFS) file systems are added in the backup plans of AWS Backup.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/efs-in-backup-plan.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EFS_IN_BACKUP_PLAN"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EIP_ATTACHED")
    def EIP_ATTACHED(cls) -> builtins.str:
        '''Checks whether all Elastic IP addresses that are allocated to a VPC are attached to EC2 instances or in-use elastic network interfaces (ENIs).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/eip-attached.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EIP_ATTACHED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EKS_ENDPOINT_NO_PUBLIC_ACCESS")
    def EKS_ENDPOINT_NO_PUBLIC_ACCESS(cls) -> builtins.str:
        '''Checks whether Amazon Elastic Kubernetes Service (Amazon EKS) endpoint is not publicly accessible.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/eks-endpoint-no-public-access.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EKS_ENDPOINT_NO_PUBLIC_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EKS_SECRETS_ENCRYPTED")
    def EKS_SECRETS_ENCRYPTED(cls) -> builtins.str:
        '''Checks whether Amazon Elastic Kubernetes Service clusters are configured to have Kubernetes secrets encrypted using AWS Key Management Service (KMS) keys.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/eks-secrets-encrypted.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EKS_SECRETS_ENCRYPTED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTICACHE_REDIS_CLUSTER_AUTOMATIC_BACKUP_CHECK")
    def ELASTICACHE_REDIS_CLUSTER_AUTOMATIC_BACKUP_CHECK(cls) -> builtins.str:
        '''Check if the Amazon ElastiCache Redis clusters have automatic backup turned on.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/elasticache-redis-cluster-automatic-backup-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ELASTICACHE_REDIS_CLUSTER_AUTOMATIC_BACKUP_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTICSEARCH_ENCRYPTED_AT_REST")
    def ELASTICSEARCH_ENCRYPTED_AT_REST(cls) -> builtins.str:
        '''Checks whether Amazon Elasticsearch Service (Amazon ES) domains have encryption at rest configuration enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/elasticsearch-encrypted-at-rest.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ELASTICSEARCH_ENCRYPTED_AT_REST"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTICSEARCH_IN_VPC_ONLY")
    def ELASTICSEARCH_IN_VPC_ONLY(cls) -> builtins.str:
        '''Checks whether Amazon Elasticsearch Service (Amazon ES) domains are in Amazon Virtual Private Cloud (Amazon VPC).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/elasticsearch-in-vpc-only.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ELASTICSEARCH_IN_VPC_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTICSEARCH_NODE_TO_NODE_ENCRYPTION_CHECK")
    def ELASTICSEARCH_NODE_TO_NODE_ENCRYPTION_CHECK(cls) -> builtins.str:
        '''Check that Amazon ElasticSearch Service nodes are encrypted end to end.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/elasticsearch-node-to-node-encryption-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ELASTICSEARCH_NODE_TO_NODE_ENCRYPTION_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELB_ACM_CERTIFICATE_REQUIRED")
    def ELB_ACM_CERTIFICATE_REQUIRED(cls) -> builtins.str:
        '''Checks whether the Classic Load Balancers use SSL certificates provided by AWS Certificate Manager.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/elb-acm-certificate-required.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ELB_ACM_CERTIFICATE_REQUIRED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELB_CROSS_ZONE_LOAD_BALANCING_ENABLED")
    def ELB_CROSS_ZONE_LOAD_BALANCING_ENABLED(cls) -> builtins.str:
        '''Checks if cross-zone load balancing is enabled for the Classic Load Balancers (CLBs).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/elb-cross-zone-load-balancing-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ELB_CROSS_ZONE_LOAD_BALANCING_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELB_CUSTOM_SECURITY_POLICY_SSL_CHECK")
    def ELB_CUSTOM_SECURITY_POLICY_SSL_CHECK(cls) -> builtins.str:
        '''Checks whether your Classic Load Balancer SSL listeners are using a custom policy.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/elb-custom-security-policy-ssl-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ELB_CUSTOM_SECURITY_POLICY_SSL_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELB_DELETION_PROTECTION_ENABLED")
    def ELB_DELETION_PROTECTION_ENABLED(cls) -> builtins.str:
        '''Checks whether Elastic Load Balancing has deletion protection enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/elb-deletion-protection-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ELB_DELETION_PROTECTION_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELB_LOGGING_ENABLED")
    def ELB_LOGGING_ENABLED(cls) -> builtins.str:
        '''Checks whether the Application Load Balancer and the Classic Load Balancer have logging enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/elb-logging-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ELB_LOGGING_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELB_PREDEFINED_SECURITY_POLICY_SSL_CHECK")
    def ELB_PREDEFINED_SECURITY_POLICY_SSL_CHECK(cls) -> builtins.str:
        '''Checks whether your Classic Load Balancer SSL listeners are using a predefined policy.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/elb-predefined-security-policy-ssl-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ELB_PREDEFINED_SECURITY_POLICY_SSL_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELB_TLS_HTTPS_LISTENERS_ONLY")
    def ELB_TLS_HTTPS_LISTENERS_ONLY(cls) -> builtins.str:
        '''Checks whether your Classic Load Balancer is configured with SSL or HTTPS listeners.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/elb-tls-https-listeners-only.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ELB_TLS_HTTPS_LISTENERS_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EMR_KERBEROS_ENABLED")
    def EMR_KERBEROS_ENABLED(cls) -> builtins.str:
        '''Checks that Amazon EMR clusters have Kerberos enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/emr-kerberos-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EMR_KERBEROS_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EMR_MASTER_NO_PUBLIC_IP")
    def EMR_MASTER_NO_PUBLIC_IP(cls) -> builtins.str:
        '''Checks whether Amazon Elastic MapReduce (EMR) clusters' master nodes have public IPs.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/emr-master-no-public-ip.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EMR_MASTER_NO_PUBLIC_IP"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="FMS_SECURITY_GROUP_AUDIT_POLICY_CHECK")
    def FMS_SECURITY_GROUP_AUDIT_POLICY_CHECK(cls) -> builtins.str:
        '''Checks whether the security groups associated inScope resources are compliant with the master security groups at each rule level based on allowSecurityGroup and denySecurityGroup flag.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/fms-security-group-audit-policy-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "FMS_SECURITY_GROUP_AUDIT_POLICY_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="FMS_SECURITY_GROUP_CONTENT_CHECK")
    def FMS_SECURITY_GROUP_CONTENT_CHECK(cls) -> builtins.str:
        '''Checks whether AWS Firewall Manager created security groups content is the same as the master security groups.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/fms-security-group-content-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "FMS_SECURITY_GROUP_CONTENT_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="FMS_SECURITY_GROUP_RESOURCE_ASSOCIATION_CHECK")
    def FMS_SECURITY_GROUP_RESOURCE_ASSOCIATION_CHECK(cls) -> builtins.str:
        '''Checks whether Amazon EC2 or an elastic network interface is associated with AWS Firewall Manager security groups.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/fms-security-group-resource-association-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "FMS_SECURITY_GROUP_RESOURCE_ASSOCIATION_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="FMS_SHIELD_RESOURCE_POLICY_CHECK")
    def FMS_SHIELD_RESOURCE_POLICY_CHECK(cls) -> builtins.str:
        '''Checks whether an Application Load Balancer, Amazon CloudFront distributions, Elastic Load Balancer or Elastic IP has AWS Shield protection.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/fms-shield-resource-policy-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "FMS_SHIELD_RESOURCE_POLICY_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="FMS_WEBACL_RESOURCE_POLICY_CHECK")
    def FMS_WEBACL_RESOURCE_POLICY_CHECK(cls) -> builtins.str:
        '''Checks whether the web ACL is associated with an Application Load Balancer, API Gateway stage, or Amazon CloudFront distributions.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/fms-webacl-resource-policy-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "FMS_WEBACL_RESOURCE_POLICY_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="FMS_WEBACL_RULEGROUP_ASSOCIATION_CHECK")
    def FMS_WEBACL_RULEGROUP_ASSOCIATION_CHECK(cls) -> builtins.str:
        '''Checks that the rule groups associate with the web ACL at the correct priority.

        The correct priority is decided by the rank of the rule groups in the ruleGroups parameter.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/fms-webacl-rulegroup-association-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "FMS_WEBACL_RULEGROUP_ASSOCIATION_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="GUARDDUTY_ENABLED_CENTRALIZED")
    def GUARDDUTY_ENABLED_CENTRALIZED(cls) -> builtins.str:
        '''Checks whether Amazon GuardDuty is enabled in your AWS account and region.

        If you provide an AWS account for centralization,
        the rule evaluates the Amazon GuardDuty results in the centralized account.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/guardduty-enabled-centralized.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "GUARDDUTY_ENABLED_CENTRALIZED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="GUARDDUTY_NON_ARCHIVED_FINDINGS")
    def GUARDDUTY_NON_ARCHIVED_FINDINGS(cls) -> builtins.str:
        '''Checks whether the Amazon GuardDuty has findings that are non archived.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/guardduty-non-archived-findings.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "GUARDDUTY_NON_ARCHIVED_FINDINGS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_CUSTOMER_POLICY_BLOCKED_KMS_ACTIONS")
    def IAM_CUSTOMER_POLICY_BLOCKED_KMS_ACTIONS(cls) -> builtins.str:
        '''Checks that the managed AWS Identity and Access Management policies that you create do not allow blocked actions on all AWS AWS KMS keys.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/iam-customer-policy-blocked-kms-actions.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "IAM_CUSTOMER_POLICY_BLOCKED_KMS_ACTIONS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_GROUP_HAS_USERS_CHECK")
    def IAM_GROUP_HAS_USERS_CHECK(cls) -> builtins.str:
        '''Checks whether IAM groups have at least one IAM user.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/iam-group-has-users-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "IAM_GROUP_HAS_USERS_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_INLINE_POLICY_BLOCKED_KMS_ACTIONS")
    def IAM_INLINE_POLICY_BLOCKED_KMS_ACTIONS(cls) -> builtins.str:
        '''Checks that the inline policies attached to your AWS Identity and Access Management users, roles, and groups do not allow blocked actions on all AWS Key Management Service keys.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/iam-inline-policy-blocked-kms-actions.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "IAM_INLINE_POLICY_BLOCKED_KMS_ACTIONS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_NO_INLINE_POLICY_CHECK")
    def IAM_NO_INLINE_POLICY_CHECK(cls) -> builtins.str:
        '''Checks that inline policy feature is not in use.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/iam-no-inline-policy-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "IAM_NO_INLINE_POLICY_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_PASSWORD_POLICY")
    def IAM_PASSWORD_POLICY(cls) -> builtins.str:
        '''Checks whether the account password policy for IAM users meets the specified requirements indicated in the parameters.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/iam-password-policy.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "IAM_PASSWORD_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_POLICY_BLOCKED_CHECK")
    def IAM_POLICY_BLOCKED_CHECK(cls) -> builtins.str:
        '''Checks whether for each IAM resource, a policy ARN in the input parameter is attached to the IAM resource.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/iam-policy-blacklisted-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "IAM_POLICY_BLOCKED_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_POLICY_IN_USE")
    def IAM_POLICY_IN_USE(cls) -> builtins.str:
        '''Checks whether the IAM policy ARN is attached to an IAM user, or an IAM group with one or more IAM users, or an IAM role with one or more trusted entity.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/iam-policy-in-use.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "IAM_POLICY_IN_USE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_POLICY_NO_STATEMENTS_WITH_ADMIN_ACCESS")
    def IAM_POLICY_NO_STATEMENTS_WITH_ADMIN_ACCESS(cls) -> builtins.str:
        '''Checks the IAM policies that you create for Allow statements that grant permissions to all actions on all resources.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/iam-policy-no-statements-with-admin-access.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "IAM_POLICY_NO_STATEMENTS_WITH_ADMIN_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_ROLE_MANAGED_POLICY_CHECK")
    def IAM_ROLE_MANAGED_POLICY_CHECK(cls) -> builtins.str:
        '''Checks that AWS Identity and Access Management (IAM) policies in a list of policies are attached to all AWS roles.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/iam-role-managed-policy-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "IAM_ROLE_MANAGED_POLICY_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_ROOT_ACCESS_KEY_CHECK")
    def IAM_ROOT_ACCESS_KEY_CHECK(cls) -> builtins.str:
        '''Checks whether the root user access key is available.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/iam-root-access-key-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "IAM_ROOT_ACCESS_KEY_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_USER_GROUP_MEMBERSHIP_CHECK")
    def IAM_USER_GROUP_MEMBERSHIP_CHECK(cls) -> builtins.str:
        '''Checks whether IAM users are members of at least one IAM group.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/iam-user-group-membership-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "IAM_USER_GROUP_MEMBERSHIP_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_USER_MFA_ENABLED")
    def IAM_USER_MFA_ENABLED(cls) -> builtins.str:
        '''Checks whether the AWS Identity and Access Management users have multi-factor authentication (MFA) enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/iam-user-mfa-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "IAM_USER_MFA_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_USER_NO_POLICIES_CHECK")
    def IAM_USER_NO_POLICIES_CHECK(cls) -> builtins.str:
        '''Checks that none of your IAM users have policies attached.

        IAM users must inherit permissions from IAM groups or roles.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/iam-user-no-policies-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "IAM_USER_NO_POLICIES_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_USER_UNUSED_CREDENTIALS_CHECK")
    def IAM_USER_UNUSED_CREDENTIALS_CHECK(cls) -> builtins.str:
        '''Checks whether your AWS Identity and Access Management (IAM) users have passwords or active access keys that have not been used within the specified number of days you provided.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/iam-user-unused-credentials-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "IAM_USER_UNUSED_CREDENTIALS_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="INTERNET_GATEWAY_AUTHORIZED_VPC_ONLY")
    def INTERNET_GATEWAY_AUTHORIZED_VPC_ONLY(cls) -> builtins.str:
        '''Checks that Internet gateways (IGWs) are only attached to an authorized Amazon Virtual Private Cloud (VPCs).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/internet-gateway-authorized-vpc-only.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "INTERNET_GATEWAY_AUTHORIZED_VPC_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="KMS_CMK_NOT_SCHEDULED_FOR_DELETION")
    def KMS_CMK_NOT_SCHEDULED_FOR_DELETION(cls) -> builtins.str:
        '''Checks whether customer master keys (CMKs) are not scheduled for deletion in AWS Key Management Service (KMS).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/kms-cmk-not-scheduled-for-deletion.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "KMS_CMK_NOT_SCHEDULED_FOR_DELETION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LAMBDA_CONCURRENCY_CHECK")
    def LAMBDA_CONCURRENCY_CHECK(cls) -> builtins.str:
        '''Checks whether the AWS Lambda function is configured with function-level concurrent execution limit.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/lambda-concurrency-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "LAMBDA_CONCURRENCY_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LAMBDA_DLQ_CHECK")
    def LAMBDA_DLQ_CHECK(cls) -> builtins.str:
        '''Checks whether an AWS Lambda function is configured with a dead-letter queue.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/lambda-dlq-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "LAMBDA_DLQ_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LAMBDA_FUNCTION_PUBLIC_ACCESS_PROHIBITED")
    def LAMBDA_FUNCTION_PUBLIC_ACCESS_PROHIBITED(cls) -> builtins.str:
        '''Checks whether the AWS Lambda function policy attached to the Lambda resource prohibits public access.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/lambda-function-public-access-prohibited.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "LAMBDA_FUNCTION_PUBLIC_ACCESS_PROHIBITED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LAMBDA_FUNCTION_SETTINGS_CHECK")
    def LAMBDA_FUNCTION_SETTINGS_CHECK(cls) -> builtins.str:
        '''Checks that the lambda function settings for runtime, role, timeout, and memory size match the expected values.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/lambda-function-settings-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "LAMBDA_FUNCTION_SETTINGS_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LAMBDA_INSIDE_VPC")
    def LAMBDA_INSIDE_VPC(cls) -> builtins.str:
        '''Checks whether an AWS Lambda function is in an Amazon Virtual Private Cloud.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/lambda-inside-vpc.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "LAMBDA_INSIDE_VPC"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="MFA_ENABLED_FOR_IAM_CONSOLE_ACCESS")
    def MFA_ENABLED_FOR_IAM_CONSOLE_ACCESS(cls) -> builtins.str:
        '''Checks whether AWS Multi-Factor Authentication (MFA) is enabled for all IAM users that use a console password.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/mfa-enabled-for-iam-console-access.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "MFA_ENABLED_FOR_IAM_CONSOLE_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_CLUSTER_DELETION_PROTECTION_ENABLED")
    def RDS_CLUSTER_DELETION_PROTECTION_ENABLED(cls) -> builtins.str:
        '''Checks if an Amazon Relational Database Service (Amazon RDS) cluster has deletion protection enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/rds-cluster-deletion-protection-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "RDS_CLUSTER_DELETION_PROTECTION_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_DB_INSTANCE_BACKUP_ENABLED")
    def RDS_DB_INSTANCE_BACKUP_ENABLED(cls) -> builtins.str:
        '''Checks whether RDS DB instances have backups enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/db-instance-backup-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "RDS_DB_INSTANCE_BACKUP_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_ENHANCED_MONITORING_ENABLED")
    def RDS_ENHANCED_MONITORING_ENABLED(cls) -> builtins.str:
        '''Checks whether enhanced monitoring is enabled for Amazon Relational Database Service (Amazon RDS) instances.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/rds-enhanced-monitoring-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "RDS_ENHANCED_MONITORING_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_IN_BACKUP_PLAN")
    def RDS_IN_BACKUP_PLAN(cls) -> builtins.str:
        '''Checks whether Amazon RDS database is present in back plans of AWS Backup.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/rds-in-backup-plan.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "RDS_IN_BACKUP_PLAN"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_INSTANCE_DELETION_PROTECTION_ENABLED")
    def RDS_INSTANCE_DELETION_PROTECTION_ENABLED(cls) -> builtins.str:
        '''Checks if an Amazon Relational Database Service (Amazon RDS) instance has deletion protection enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/rds-instance-deletion-protection-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "RDS_INSTANCE_DELETION_PROTECTION_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_INSTANCE_IAM_AUTHENTICATION_ENABLED")
    def RDS_INSTANCE_IAM_AUTHENTICATION_ENABLED(cls) -> builtins.str:
        '''Checks if an Amazon RDS instance has AWS Identity and Access Management (IAM) authentication enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/rds-instance-iam-authentication-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "RDS_INSTANCE_IAM_AUTHENTICATION_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_INSTANCE_PUBLIC_ACCESS_CHECK")
    def RDS_INSTANCE_PUBLIC_ACCESS_CHECK(cls) -> builtins.str:
        '''Check whether the Amazon Relational Database Service instances are not publicly accessible.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/rds-instance-public-access-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "RDS_INSTANCE_PUBLIC_ACCESS_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_LOGGING_ENABLED")
    def RDS_LOGGING_ENABLED(cls) -> builtins.str:
        '''Checks that respective logs of Amazon Relational Database Service (Amazon RDS) are enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/rds-logging-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "RDS_LOGGING_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_MULTI_AZ_SUPPORT")
    def RDS_MULTI_AZ_SUPPORT(cls) -> builtins.str:
        '''Checks whether high availability is enabled for your RDS DB instances.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/rds-multi-az-support.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "RDS_MULTI_AZ_SUPPORT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_SNAPSHOT_ENCRYPTED")
    def RDS_SNAPSHOT_ENCRYPTED(cls) -> builtins.str:
        '''Checks whether Amazon Relational Database Service (Amazon RDS) DB snapshots are encrypted.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/rds-snapshot-encrypted.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "RDS_SNAPSHOT_ENCRYPTED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_SNAPSHOTS_PUBLIC_PROHIBITED")
    def RDS_SNAPSHOTS_PUBLIC_PROHIBITED(cls) -> builtins.str:
        '''Checks if Amazon Relational Database Service (Amazon RDS) snapshots are public.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/rds-snapshots-public-prohibited.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "RDS_SNAPSHOTS_PUBLIC_PROHIBITED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_STORAGE_ENCRYPTED")
    def RDS_STORAGE_ENCRYPTED(cls) -> builtins.str:
        '''Checks whether storage encryption is enabled for your RDS DB instances.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/rds-storage-encrypted.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "RDS_STORAGE_ENCRYPTED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="REDSHIFT_BACKUP_ENABLED")
    def REDSHIFT_BACKUP_ENABLED(cls) -> builtins.str:
        '''Checks that Amazon Redshift automated snapshots are enabled for clusters.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/redshift-backup-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "REDSHIFT_BACKUP_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="REDSHIFT_CLUSTER_CONFIGURATION_CHECK")
    def REDSHIFT_CLUSTER_CONFIGURATION_CHECK(cls) -> builtins.str:
        '''Checks whether Amazon Redshift clusters have the specified settings.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/redshift-cluster-configuration-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "REDSHIFT_CLUSTER_CONFIGURATION_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="REDSHIFT_CLUSTER_MAINTENANCE_SETTINGS_CHECK")
    def REDSHIFT_CLUSTER_MAINTENANCE_SETTINGS_CHECK(cls) -> builtins.str:
        '''Checks whether Amazon Redshift clusters have the specified maintenance settings.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/redshift-cluster-maintenancesettings-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "REDSHIFT_CLUSTER_MAINTENANCE_SETTINGS_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="REDSHIFT_CLUSTER_PUBLIC_ACCESS_CHECK")
    def REDSHIFT_CLUSTER_PUBLIC_ACCESS_CHECK(cls) -> builtins.str:
        '''Checks whether Amazon Redshift clusters are not publicly accessible.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/redshift-cluster-public-access-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "REDSHIFT_CLUSTER_PUBLIC_ACCESS_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="REDSHIFT_REQUIRE_TLS_SSL")
    def REDSHIFT_REQUIRE_TLS_SSL(cls) -> builtins.str:
        '''Checks whether Amazon Redshift clusters require TLS/SSL encryption to connect to SQL clients.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/redshift-require-tls-ssl.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "REDSHIFT_REQUIRE_TLS_SSL"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="REQUIRED_TAGS")
    def REQUIRED_TAGS(cls) -> builtins.str:
        '''Checks whether your resources have the tags that you specify.

        For example, you can check whether your Amazon EC2 instances have the CostCenter tag.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/required-tags.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "REQUIRED_TAGS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ROOT_ACCOUNT_HARDWARE_MFA_ENABLED")
    def ROOT_ACCOUNT_HARDWARE_MFA_ENABLED(cls) -> builtins.str:
        '''Checks whether your AWS account is enabled to use multi-factor authentication (MFA) hardware device to sign in with root credentials.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/root-account-hardware-mfa-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ROOT_ACCOUNT_HARDWARE_MFA_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ROOT_ACCOUNT_MFA_ENABLED")
    def ROOT_ACCOUNT_MFA_ENABLED(cls) -> builtins.str:
        '''Checks whether users of your AWS account require a multi-factor authentication (MFA) device to sign in with root credentials.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/root-account-mfa-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ROOT_ACCOUNT_MFA_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3_ACCOUNT_LEVEL_PUBLIC_ACCESS_BLOCKS")
    def S3_ACCOUNT_LEVEL_PUBLIC_ACCESS_BLOCKS(cls) -> builtins.str:
        '''Checks whether the required public access block settings are configured from account level.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/s3-account-level-public-access-blocks.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "S3_ACCOUNT_LEVEL_PUBLIC_ACCESS_BLOCKS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3_BUCKET_BLOCKED_ACTIONS_PROHIBITED")
    def S3_BUCKET_BLOCKED_ACTIONS_PROHIBITED(cls) -> builtins.str:
        '''Checks that the Amazon Simple Storage Service bucket policy does not allow blocked bucket-level and object-level actions on resources in the bucket for principals from other AWS accounts.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-blacklisted-actions-prohibited.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "S3_BUCKET_BLOCKED_ACTIONS_PROHIBITED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3_BUCKET_DEFAULT_LOCK_ENABLED")
    def S3_BUCKET_DEFAULT_LOCK_ENABLED(cls) -> builtins.str:
        '''Checks whether Amazon Simple Storage Service (Amazon S3) bucket has lock enabled, by default.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-default-lock-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "S3_BUCKET_DEFAULT_LOCK_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3_BUCKET_LEVEL_PUBLIC_ACCESS_PROHIBITED")
    def S3_BUCKET_LEVEL_PUBLIC_ACCESS_PROHIBITED(cls) -> builtins.str:
        '''Checks if Amazon Simple Storage Service (Amazon S3) buckets are publicly accessible.

        This rule is
        NON_COMPLIANT if an Amazon S3 bucket is not listed in the excludedPublicBuckets parameter and bucket level
        settings are public.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-level-public-access-prohibited.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "S3_BUCKET_LEVEL_PUBLIC_ACCESS_PROHIBITED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3_BUCKET_LOGGING_ENABLED")
    def S3_BUCKET_LOGGING_ENABLED(cls) -> builtins.str:
        '''Checks whether logging is enabled for your S3 buckets.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-logging-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "S3_BUCKET_LOGGING_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3_BUCKET_POLICY_GRANTEE_CHECK")
    def S3_BUCKET_POLICY_GRANTEE_CHECK(cls) -> builtins.str:
        '''Checks that the access granted by the Amazon S3 bucket is restricted by any of the AWS principals, federated users, service principals, IP addresses, or VPCs that you provide.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-policy-grantee-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "S3_BUCKET_POLICY_GRANTEE_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3_BUCKET_POLICY_NOT_MORE_PERMISSIVE")
    def S3_BUCKET_POLICY_NOT_MORE_PERMISSIVE(cls) -> builtins.str:
        '''Verifies that your Amazon Simple Storage Service bucket policies do not allow other inter-account permissions than the control Amazon S3 bucket policy provided.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-policy-not-more-permissive.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "S3_BUCKET_POLICY_NOT_MORE_PERMISSIVE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3_BUCKET_PUBLIC_READ_PROHIBITED")
    def S3_BUCKET_PUBLIC_READ_PROHIBITED(cls) -> builtins.str:
        '''Checks that your Amazon S3 buckets do not allow public read access.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-public-read-prohibited.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "S3_BUCKET_PUBLIC_READ_PROHIBITED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3_BUCKET_PUBLIC_WRITE_PROHIBITED")
    def S3_BUCKET_PUBLIC_WRITE_PROHIBITED(cls) -> builtins.str:
        '''Checks that your Amazon S3 buckets do not allow public write access.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-public-write-prohibited.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "S3_BUCKET_PUBLIC_WRITE_PROHIBITED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3_BUCKET_REPLICATION_ENABLED")
    def S3_BUCKET_REPLICATION_ENABLED(cls) -> builtins.str:
        '''Checks whether S3 buckets have cross-region replication enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-replication-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "S3_BUCKET_REPLICATION_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3_BUCKET_SERVER_SIDE_ENCRYPTION_ENABLED")
    def S3_BUCKET_SERVER_SIDE_ENCRYPTION_ENABLED(cls) -> builtins.str:
        '''Checks that your Amazon S3 bucket either has Amazon S3 default encryption enabled or that the S3 bucket policy explicitly denies put-object requests without server side encryption that uses AES-256 or AWS Key Management Service.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-server-side-encryption-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "S3_BUCKET_SERVER_SIDE_ENCRYPTION_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3_BUCKET_SSL_REQUESTS_ONLY")
    def S3_BUCKET_SSL_REQUESTS_ONLY(cls) -> builtins.str:
        '''Checks whether S3 buckets have policies that require requests to use Secure Socket Layer (SSL).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-ssl-requests-only.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "S3_BUCKET_SSL_REQUESTS_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3_BUCKET_VERSIONING_ENABLED")
    def S3_BUCKET_VERSIONING_ENABLED(cls) -> builtins.str:
        '''Checks whether versioning is enabled for your S3 buckets.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-versioning-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "S3_BUCKET_VERSIONING_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3_DEFAULT_ENCRYPTION_KMS")
    def S3_DEFAULT_ENCRYPTION_KMS(cls) -> builtins.str:
        '''Checks whether the Amazon Simple Storage Service (Amazon S3) buckets are encrypted with AWS Key Management Service (AWS KMS).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/s3-default-encryption-kms.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "S3_DEFAULT_ENCRYPTION_KMS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SAGEMAKER_ENDPOINT_CONFIGURATION_KMS_KEY_CONFIGURED")
    def SAGEMAKER_ENDPOINT_CONFIGURATION_KMS_KEY_CONFIGURED(cls) -> builtins.str:
        '''Checks whether AWS Key Management Service (KMS) key is configured for an Amazon SageMaker endpoint configuration.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/sagemaker-endpoint-configuration-kms-key-configured.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "SAGEMAKER_ENDPOINT_CONFIGURATION_KMS_KEY_CONFIGURED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SAGEMAKER_NOTEBOOK_INSTANCE_KMS_KEY_CONFIGURED")
    def SAGEMAKER_NOTEBOOK_INSTANCE_KMS_KEY_CONFIGURED(cls) -> builtins.str:
        '''Check whether an AWS Key Management Service (KMS) key is configured for SageMaker notebook instance.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/sagemaker-notebook-instance-kms-key-configured.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "SAGEMAKER_NOTEBOOK_INSTANCE_KMS_KEY_CONFIGURED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SAGEMAKER_NOTEBOOK_NO_DIRECT_INTERNET_ACCESS")
    def SAGEMAKER_NOTEBOOK_NO_DIRECT_INTERNET_ACCESS(cls) -> builtins.str:
        '''Checks whether direct internet access is disabled for an Amazon SageMaker notebook instance.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/sagemaker-notebook-no-direct-internet-access.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "SAGEMAKER_NOTEBOOK_NO_DIRECT_INTERNET_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SECRETSMANAGER_ROTATION_ENABLED_CHECK")
    def SECRETSMANAGER_ROTATION_ENABLED_CHECK(cls) -> builtins.str:
        '''Checks whether AWS Secrets Manager secret has rotation enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/secretsmanager-rotation-enabled-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "SECRETSMANAGER_ROTATION_ENABLED_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SECRETSMANAGER_SCHEDULED_ROTATION_SUCCESS_CHECK")
    def SECRETSMANAGER_SCHEDULED_ROTATION_SUCCESS_CHECK(cls) -> builtins.str:
        '''Checks whether AWS Secrets Manager secret rotation has rotated successfully as per the rotation schedule.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/secretsmanager-scheduled-rotation-success-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "SECRETSMANAGER_SCHEDULED_ROTATION_SUCCESS_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SECURITYHUB_ENABLED")
    def SECURITYHUB_ENABLED(cls) -> builtins.str:
        '''Checks that AWS Security Hub is enabled for an AWS account.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/securityhub-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "SECURITYHUB_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SERVICE_VPC_ENDPOINT_ENABLED")
    def SERVICE_VPC_ENDPOINT_ENABLED(cls) -> builtins.str:
        '''Checks whether Service Endpoint for the service provided in rule parameter is created for each Amazon VPC.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/service-vpc-endpoint-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "SERVICE_VPC_ENDPOINT_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SHIELD_ADVANCED_ENABLED_AUTO_RENEW")
    def SHIELD_ADVANCED_ENABLED_AUTO_RENEW(cls) -> builtins.str:
        '''Checks whether EBS volumes are attached to EC2 instances.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/shield-advanced-enabled-autorenew.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "SHIELD_ADVANCED_ENABLED_AUTO_RENEW"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SHIELD_DRT_ACCESS")
    def SHIELD_DRT_ACCESS(cls) -> builtins.str:
        '''Verify that DDoS response team (DRT) can access AWS account.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/shield-drt-access.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "SHIELD_DRT_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SNS_ENCRYPTED_KMS")
    def SNS_ENCRYPTED_KMS(cls) -> builtins.str:
        '''Checks whether Amazon SNS topic is encrypted with AWS Key Management Service (AWS KMS).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/sns-encrypted-kms.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "SNS_ENCRYPTED_KMS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="VPC_DEFAULT_SECURITY_GROUP_CLOSED")
    def VPC_DEFAULT_SECURITY_GROUP_CLOSED(cls) -> builtins.str:
        '''Checks that the default security group of any Amazon Virtual Private Cloud (VPC) does not allow inbound or outbound traffic.

        The rule returns NOT_APPLICABLE if the security group
        is not default.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/vpc-default-security-group-closed.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "VPC_DEFAULT_SECURITY_GROUP_CLOSED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="VPC_FLOW_LOGS_ENABLED")
    def VPC_FLOW_LOGS_ENABLED(cls) -> builtins.str:
        '''Checks whether Amazon Virtual Private Cloud flow logs are found and enabled for Amazon VPC.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/vpc-flow-logs-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "VPC_FLOW_LOGS_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="VPC_SG_OPEN_ONLY_TO_AUTHORIZED_PORTS")
    def VPC_SG_OPEN_ONLY_TO_AUTHORIZED_PORTS(cls) -> builtins.str:
        '''Checks whether the security group with 0.0.0.0/0 of any Amazon Virtual Private Cloud (Amazon VPC) allows only specific inbound TCP or UDP traffic.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/vpc-sg-open-only-to-authorized-ports.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "VPC_SG_OPEN_ONLY_TO_AUTHORIZED_PORTS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="VPC_VPN_2_TUNNELS_UP")
    def VPC_VPN_2_TUNNELS_UP(cls) -> builtins.str:
        '''Checks that both AWS Virtual Private Network tunnels provided by AWS Site-to-Site VPN are in UP status.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/vpc-vpn-2-tunnels-up.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "VPC_VPN_2_TUNNELS_UP"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="WAF_CLASSIC_LOGGING_ENABLED")
    def WAF_CLASSIC_LOGGING_ENABLED(cls) -> builtins.str:
        '''Checks if logging is enabled on AWS Web Application Firewall (WAF) classic global web ACLs.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/waf-classic-logging-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "WAF_CLASSIC_LOGGING_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="WAFV2_LOGGING_ENABLED")
    def WAFV2_LOGGING_ENABLED(cls) -> builtins.str:
        '''Checks whether logging is enabled on AWS Web Application Firewall (WAFV2) regional and global web access control list (ACLs).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/wafv2-logging-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "WAFV2_LOGGING_ENABLED"))


@jsii.enum(jsii_type="@aws-cdk/aws-config.MaximumExecutionFrequency")
class MaximumExecutionFrequency(enum.Enum):
    '''The maximum frequency at which the AWS Config rule runs evaluations.

    :exampleMetadata: infused

    Example::

        # https://docs.aws.amazon.com/config/latest/developerguide/access-keys-rotated.html
        config.ManagedRule(self, "AccessKeysRotated",
            identifier=config.ManagedRuleIdentifiers.ACCESS_KEYS_ROTATED,
            input_parameters={
                "max_access_key_age": 60
            },
        
            # default is 24 hours
            maximum_execution_frequency=config.MaximumExecutionFrequency.TWELVE_HOURS
        )
    '''

    ONE_HOUR = "ONE_HOUR"
    '''1 hour.'''
    THREE_HOURS = "THREE_HOURS"
    '''3 hours.'''
    SIX_HOURS = "SIX_HOURS"
    '''6 hours.'''
    TWELVE_HOURS = "TWELVE_HOURS"
    '''12 hours.'''
    TWENTY_FOUR_HOURS = "TWENTY_FOUR_HOURS"
    '''24 hours.'''


class ResourceType(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-config.ResourceType",
):
    '''Resources types that are supported by AWS Config.

    :see: https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html
    :exampleMetadata: infused

    Example::

        # eval_compliance_fn: lambda.Function
        ssh_rule = config.ManagedRule(self, "SSH",
            identifier=config.ManagedRuleIdentifiers.EC2_SECURITY_GROUPS_INCOMING_SSH_DISABLED,
            rule_scope=config.RuleScope.from_resource(config.ResourceType.EC2_SECURITY_GROUP, "sg-1234567890abcdefgh")
        )
        custom_rule = config.CustomRule(self, "Lambda",
            lambda_function=eval_compliance_fn,
            configuration_changes=True,
            rule_scope=config.RuleScope.from_resources([config.ResourceType.CLOUDFORMATION_STACK, config.ResourceType.S3_BUCKET])
        )
        
        tag_rule = config.CustomRule(self, "CostCenterTagRule",
            lambda_function=eval_compliance_fn,
            configuration_changes=True,
            rule_scope=config.RuleScope.from_tag("Cost Center", "MyApp")
        )
    '''

    @jsii.member(jsii_name="of")
    @builtins.classmethod
    def of(cls, type: builtins.str) -> "ResourceType":
        '''A custom resource type to support future cases.

        :param type: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db687db6a42e76118e2e021d6e57901854f5fb1e4ae269ae67f500d34a94f7d6)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        return typing.cast("ResourceType", jsii.sinvoke(cls, "of", [type]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ACM_CERTIFICATE")
    def ACM_CERTIFICATE(cls) -> "ResourceType":
        '''AWS Certificate manager certificate.'''
        return typing.cast("ResourceType", jsii.sget(cls, "ACM_CERTIFICATE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="APIGATEWAY_REST_API")
    def APIGATEWAY_REST_API(cls) -> "ResourceType":
        '''API Gateway REST API.'''
        return typing.cast("ResourceType", jsii.sget(cls, "APIGATEWAY_REST_API"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="APIGATEWAY_STAGE")
    def APIGATEWAY_STAGE(cls) -> "ResourceType":
        '''API Gateway Stage.'''
        return typing.cast("ResourceType", jsii.sget(cls, "APIGATEWAY_STAGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="APIGATEWAYV2_API")
    def APIGATEWAYV2_API(cls) -> "ResourceType":
        '''API Gatewayv2 API.'''
        return typing.cast("ResourceType", jsii.sget(cls, "APIGATEWAYV2_API"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="APIGATEWAYV2_STAGE")
    def APIGATEWAYV2_STAGE(cls) -> "ResourceType":
        '''API Gatewayv2 Stage.'''
        return typing.cast("ResourceType", jsii.sget(cls, "APIGATEWAYV2_STAGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AUTO_SCALING_GROUP")
    def AUTO_SCALING_GROUP(cls) -> "ResourceType":
        '''AWS Auto Scaling group.'''
        return typing.cast("ResourceType", jsii.sget(cls, "AUTO_SCALING_GROUP"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AUTO_SCALING_LAUNCH_CONFIGURATION")
    def AUTO_SCALING_LAUNCH_CONFIGURATION(cls) -> "ResourceType":
        '''AWS Auto Scaling launch configuration.'''
        return typing.cast("ResourceType", jsii.sget(cls, "AUTO_SCALING_LAUNCH_CONFIGURATION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AUTO_SCALING_POLICY")
    def AUTO_SCALING_POLICY(cls) -> "ResourceType":
        '''AWS Auto Scaling policy.'''
        return typing.cast("ResourceType", jsii.sget(cls, "AUTO_SCALING_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AUTO_SCALING_SCHEDULED_ACTION")
    def AUTO_SCALING_SCHEDULED_ACTION(cls) -> "ResourceType":
        '''AWS Auto Scaling scheduled action.'''
        return typing.cast("ResourceType", jsii.sget(cls, "AUTO_SCALING_SCHEDULED_ACTION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDFORMATION_STACK")
    def CLOUDFORMATION_STACK(cls) -> "ResourceType":
        '''AWS CloudFormation stack.'''
        return typing.cast("ResourceType", jsii.sget(cls, "CLOUDFORMATION_STACK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDFRONT_DISTRIBUTION")
    def CLOUDFRONT_DISTRIBUTION(cls) -> "ResourceType":
        '''Amazon CloudFront Distribution.'''
        return typing.cast("ResourceType", jsii.sget(cls, "CLOUDFRONT_DISTRIBUTION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDFRONT_STREAMING_DISTRIBUTION")
    def CLOUDFRONT_STREAMING_DISTRIBUTION(cls) -> "ResourceType":
        '''Amazon CloudFront streaming distribution.'''
        return typing.cast("ResourceType", jsii.sget(cls, "CLOUDFRONT_STREAMING_DISTRIBUTION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDTRAIL_TRAIL")
    def CLOUDTRAIL_TRAIL(cls) -> "ResourceType":
        '''AWS CloudTrail trail.'''
        return typing.cast("ResourceType", jsii.sget(cls, "CLOUDTRAIL_TRAIL"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDWATCH_ALARM")
    def CLOUDWATCH_ALARM(cls) -> "ResourceType":
        '''Amazon CloudWatch Alarm.'''
        return typing.cast("ResourceType", jsii.sget(cls, "CLOUDWATCH_ALARM"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CODEBUILD_PROJECT")
    def CODEBUILD_PROJECT(cls) -> "ResourceType":
        '''AWS CodeBuild project.'''
        return typing.cast("ResourceType", jsii.sget(cls, "CODEBUILD_PROJECT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CODEPIPELINE_PIPELINE")
    def CODEPIPELINE_PIPELINE(cls) -> "ResourceType":
        '''AWS CodePipeline pipeline.'''
        return typing.cast("ResourceType", jsii.sget(cls, "CODEPIPELINE_PIPELINE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DYNAMODB_TABLE")
    def DYNAMODB_TABLE(cls) -> "ResourceType":
        '''Amazon DynamoDB Table.'''
        return typing.cast("ResourceType", jsii.sget(cls, "DYNAMODB_TABLE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EBS_VOLUME")
    def EBS_VOLUME(cls) -> "ResourceType":
        '''Elastic Block Store (EBS) volume.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EBS_VOLUME"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_CUSTOMER_GATEWAY")
    def EC2_CUSTOMER_GATEWAY(cls) -> "ResourceType":
        '''Amazon EC2 customer gateway.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_CUSTOMER_GATEWAY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_EGRESS_ONLY_INTERNET_GATEWAY")
    def EC2_EGRESS_ONLY_INTERNET_GATEWAY(cls) -> "ResourceType":
        '''EC2 Egress only internet gateway.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_EGRESS_ONLY_INTERNET_GATEWAY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_EIP")
    def EC2_EIP(cls) -> "ResourceType":
        '''EC2 Elastic IP.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_EIP"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_FLOW_LOG")
    def EC2_FLOW_LOG(cls) -> "ResourceType":
        '''EC2 flow log.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_FLOW_LOG"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_HOST")
    def EC2_HOST(cls) -> "ResourceType":
        '''EC2 host.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_HOST"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_INSTANCE")
    def EC2_INSTANCE(cls) -> "ResourceType":
        '''EC2 instance.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_INSTANCE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_INTERNET_GATEWAY")
    def EC2_INTERNET_GATEWAY(cls) -> "ResourceType":
        '''Amazon EC2 internet gateway.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_INTERNET_GATEWAY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_NAT_GATEWAY")
    def EC2_NAT_GATEWAY(cls) -> "ResourceType":
        '''EC2 NAT gateway.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_NAT_GATEWAY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_NETWORK_ACL")
    def EC2_NETWORK_ACL(cls) -> "ResourceType":
        '''Amazon EC2 network ACL.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_NETWORK_ACL"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_ROUTE_TABLE")
    def EC2_ROUTE_TABLE(cls) -> "ResourceType":
        '''Amazon EC2 route table.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_ROUTE_TABLE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_SECURITY_GROUP")
    def EC2_SECURITY_GROUP(cls) -> "ResourceType":
        '''EC2 security group.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_SECURITY_GROUP"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_SUBNET")
    def EC2_SUBNET(cls) -> "ResourceType":
        '''Amazon EC2 subnet table.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_SUBNET"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_VPC")
    def EC2_VPC(cls) -> "ResourceType":
        '''Amazon EC2 VPC.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_VPC"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_VPC_ENDPOINT")
    def EC2_VPC_ENDPOINT(cls) -> "ResourceType":
        '''EC2 VPC endpoint.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_VPC_ENDPOINT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_VPC_ENDPOINT_SERVICE")
    def EC2_VPC_ENDPOINT_SERVICE(cls) -> "ResourceType":
        '''EC2 VPC endpoint service.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_VPC_ENDPOINT_SERVICE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_VPC_PEERING_CONNECTION")
    def EC2_VPC_PEERING_CONNECTION(cls) -> "ResourceType":
        '''EC2 VPC peering connection.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_VPC_PEERING_CONNECTION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_VPN_CONNECTION")
    def EC2_VPN_CONNECTION(cls) -> "ResourceType":
        '''Amazon EC2 VPN connection.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_VPN_CONNECTION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_VPN_GATEWAY")
    def EC2_VPN_GATEWAY(cls) -> "ResourceType":
        '''Amazon EC2 VPN gateway.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_VPN_GATEWAY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTIC_BEANSTALK_APPLICATION")
    def ELASTIC_BEANSTALK_APPLICATION(cls) -> "ResourceType":
        '''AWS Elastic Beanstalk (EB) application.'''
        return typing.cast("ResourceType", jsii.sget(cls, "ELASTIC_BEANSTALK_APPLICATION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTIC_BEANSTALK_APPLICATION_VERSION")
    def ELASTIC_BEANSTALK_APPLICATION_VERSION(cls) -> "ResourceType":
        '''AWS Elastic Beanstalk (EB) application version.'''
        return typing.cast("ResourceType", jsii.sget(cls, "ELASTIC_BEANSTALK_APPLICATION_VERSION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTIC_BEANSTALK_ENVIRONMENT")
    def ELASTIC_BEANSTALK_ENVIRONMENT(cls) -> "ResourceType":
        '''AWS Elastic Beanstalk (EB) environment.'''
        return typing.cast("ResourceType", jsii.sget(cls, "ELASTIC_BEANSTALK_ENVIRONMENT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTICSEARCH_DOMAIN")
    def ELASTICSEARCH_DOMAIN(cls) -> "ResourceType":
        '''Amazon ElasticSearch domain.'''
        return typing.cast("ResourceType", jsii.sget(cls, "ELASTICSEARCH_DOMAIN"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELB_LOAD_BALANCER")
    def ELB_LOAD_BALANCER(cls) -> "ResourceType":
        '''AWS ELB classic load balancer.'''
        return typing.cast("ResourceType", jsii.sget(cls, "ELB_LOAD_BALANCER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELBV2_LOAD_BALANCER")
    def ELBV2_LOAD_BALANCER(cls) -> "ResourceType":
        '''AWS ELBv2 network load balancer or AWS ELBv2 application load balancer.'''
        return typing.cast("ResourceType", jsii.sget(cls, "ELBV2_LOAD_BALANCER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_GROUP")
    def IAM_GROUP(cls) -> "ResourceType":
        '''AWS IAM group.'''
        return typing.cast("ResourceType", jsii.sget(cls, "IAM_GROUP"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_POLICY")
    def IAM_POLICY(cls) -> "ResourceType":
        '''AWS IAM policy.'''
        return typing.cast("ResourceType", jsii.sget(cls, "IAM_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_ROLE")
    def IAM_ROLE(cls) -> "ResourceType":
        '''AWS IAM role.'''
        return typing.cast("ResourceType", jsii.sget(cls, "IAM_ROLE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_USER")
    def IAM_USER(cls) -> "ResourceType":
        '''AWS IAM user.'''
        return typing.cast("ResourceType", jsii.sget(cls, "IAM_USER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="KMS_KEY")
    def KMS_KEY(cls) -> "ResourceType":
        '''AWS KMS Key.'''
        return typing.cast("ResourceType", jsii.sget(cls, "KMS_KEY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LAMBDA_FUNCTION")
    def LAMBDA_FUNCTION(cls) -> "ResourceType":
        '''AWS Lambda function.'''
        return typing.cast("ResourceType", jsii.sget(cls, "LAMBDA_FUNCTION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="QLDB_LEDGER")
    def QLDB_LEDGER(cls) -> "ResourceType":
        '''Amazon QLDB ledger.'''
        return typing.cast("ResourceType", jsii.sget(cls, "QLDB_LEDGER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_DB_CLUSTER")
    def RDS_DB_CLUSTER(cls) -> "ResourceType":
        '''Amazon RDS database cluster.'''
        return typing.cast("ResourceType", jsii.sget(cls, "RDS_DB_CLUSTER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_DB_CLUSTER_SNAPSHOT")
    def RDS_DB_CLUSTER_SNAPSHOT(cls) -> "ResourceType":
        '''Amazon RDS database cluster snapshot.'''
        return typing.cast("ResourceType", jsii.sget(cls, "RDS_DB_CLUSTER_SNAPSHOT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_DB_INSTANCE")
    def RDS_DB_INSTANCE(cls) -> "ResourceType":
        '''Amazon RDS database instance.'''
        return typing.cast("ResourceType", jsii.sget(cls, "RDS_DB_INSTANCE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_DB_SECURITY_GROUP")
    def RDS_DB_SECURITY_GROUP(cls) -> "ResourceType":
        '''Amazon RDS database security group.'''
        return typing.cast("ResourceType", jsii.sget(cls, "RDS_DB_SECURITY_GROUP"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_DB_SNAPSHOT")
    def RDS_DB_SNAPSHOT(cls) -> "ResourceType":
        '''Amazon RDS database snapshot.'''
        return typing.cast("ResourceType", jsii.sget(cls, "RDS_DB_SNAPSHOT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_DB_SUBNET_GROUP")
    def RDS_DB_SUBNET_GROUP(cls) -> "ResourceType":
        '''Amazon RDS database subnet group.'''
        return typing.cast("ResourceType", jsii.sget(cls, "RDS_DB_SUBNET_GROUP"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_EVENT_SUBSCRIPTION")
    def RDS_EVENT_SUBSCRIPTION(cls) -> "ResourceType":
        '''Amazon RDS event subscription.'''
        return typing.cast("ResourceType", jsii.sget(cls, "RDS_EVENT_SUBSCRIPTION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="REDSHIFT_CLUSTER")
    def REDSHIFT_CLUSTER(cls) -> "ResourceType":
        '''Amazon Redshift cluster.'''
        return typing.cast("ResourceType", jsii.sget(cls, "REDSHIFT_CLUSTER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="REDSHIFT_CLUSTER_PARAMETER_GROUP")
    def REDSHIFT_CLUSTER_PARAMETER_GROUP(cls) -> "ResourceType":
        '''Amazon Redshift cluster parameter group.'''
        return typing.cast("ResourceType", jsii.sget(cls, "REDSHIFT_CLUSTER_PARAMETER_GROUP"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="REDSHIFT_CLUSTER_SECURITY_GROUP")
    def REDSHIFT_CLUSTER_SECURITY_GROUP(cls) -> "ResourceType":
        '''Amazon Redshift cluster security group.'''
        return typing.cast("ResourceType", jsii.sget(cls, "REDSHIFT_CLUSTER_SECURITY_GROUP"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="REDSHIFT_CLUSTER_SNAPSHOT")
    def REDSHIFT_CLUSTER_SNAPSHOT(cls) -> "ResourceType":
        '''Amazon Redshift cluster snapshot.'''
        return typing.cast("ResourceType", jsii.sget(cls, "REDSHIFT_CLUSTER_SNAPSHOT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="REDSHIFT_CLUSTER_SUBNET_GROUP")
    def REDSHIFT_CLUSTER_SUBNET_GROUP(cls) -> "ResourceType":
        '''Amazon Redshift cluster subnet group.'''
        return typing.cast("ResourceType", jsii.sget(cls, "REDSHIFT_CLUSTER_SUBNET_GROUP"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="REDSHIFT_EVENT_SUBSCRIPTION")
    def REDSHIFT_EVENT_SUBSCRIPTION(cls) -> "ResourceType":
        '''Amazon Redshift event subscription.'''
        return typing.cast("ResourceType", jsii.sget(cls, "REDSHIFT_EVENT_SUBSCRIPTION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3_ACCOUNT_PUBLIC_ACCESS_BLOCK")
    def S3_ACCOUNT_PUBLIC_ACCESS_BLOCK(cls) -> "ResourceType":
        '''Amazon S3 account public access block.'''
        return typing.cast("ResourceType", jsii.sget(cls, "S3_ACCOUNT_PUBLIC_ACCESS_BLOCK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3_BUCKET")
    def S3_BUCKET(cls) -> "ResourceType":
        '''Amazon S3 bucket.'''
        return typing.cast("ResourceType", jsii.sget(cls, "S3_BUCKET"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SECRETS_MANAGER_SECRET")
    def SECRETS_MANAGER_SECRET(cls) -> "ResourceType":
        '''AWS Secrets Manager secret.'''
        return typing.cast("ResourceType", jsii.sget(cls, "SECRETS_MANAGER_SECRET"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SERVICE_CATALOG_CLOUDFORMATION_PRODUCT")
    def SERVICE_CATALOG_CLOUDFORMATION_PRODUCT(cls) -> "ResourceType":
        '''AWS Service Catalog CloudFormation product.'''
        return typing.cast("ResourceType", jsii.sget(cls, "SERVICE_CATALOG_CLOUDFORMATION_PRODUCT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SERVICE_CATALOG_CLOUDFORMATION_PROVISIONED_PRODUCT")
    def SERVICE_CATALOG_CLOUDFORMATION_PROVISIONED_PRODUCT(cls) -> "ResourceType":
        '''AWS Service Catalog CloudFormation provisioned product.'''
        return typing.cast("ResourceType", jsii.sget(cls, "SERVICE_CATALOG_CLOUDFORMATION_PROVISIONED_PRODUCT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SERVICE_CATALOG_PORTFOLIO")
    def SERVICE_CATALOG_PORTFOLIO(cls) -> "ResourceType":
        '''AWS Service Catalog portfolio.'''
        return typing.cast("ResourceType", jsii.sget(cls, "SERVICE_CATALOG_PORTFOLIO"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SHIELD_PROTECTION")
    def SHIELD_PROTECTION(cls) -> "ResourceType":
        '''AWS Shield protection.'''
        return typing.cast("ResourceType", jsii.sget(cls, "SHIELD_PROTECTION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SHIELD_REGIONAL_PROTECTION")
    def SHIELD_REGIONAL_PROTECTION(cls) -> "ResourceType":
        '''AWS Shield regional protection.'''
        return typing.cast("ResourceType", jsii.sget(cls, "SHIELD_REGIONAL_PROTECTION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SNS_TOPIC")
    def SNS_TOPIC(cls) -> "ResourceType":
        '''Amazon SNS topic.'''
        return typing.cast("ResourceType", jsii.sget(cls, "SNS_TOPIC"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SQS_QUEUE")
    def SQS_QUEUE(cls) -> "ResourceType":
        '''Amazon SQS queue.'''
        return typing.cast("ResourceType", jsii.sget(cls, "SQS_QUEUE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYSTEMS_MANAGER_ASSOCIATION_COMPLIANCE")
    def SYSTEMS_MANAGER_ASSOCIATION_COMPLIANCE(cls) -> "ResourceType":
        '''AWS Systems Manager association compliance.'''
        return typing.cast("ResourceType", jsii.sget(cls, "SYSTEMS_MANAGER_ASSOCIATION_COMPLIANCE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYSTEMS_MANAGER_FILE_DATA")
    def SYSTEMS_MANAGER_FILE_DATA(cls) -> "ResourceType":
        '''AWS Systems Manager file data.'''
        return typing.cast("ResourceType", jsii.sget(cls, "SYSTEMS_MANAGER_FILE_DATA"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYSTEMS_MANAGER_MANAGED_INSTANCE_INVENTORY")
    def SYSTEMS_MANAGER_MANAGED_INSTANCE_INVENTORY(cls) -> "ResourceType":
        '''AWS Systems Manager managed instance inventory.'''
        return typing.cast("ResourceType", jsii.sget(cls, "SYSTEMS_MANAGER_MANAGED_INSTANCE_INVENTORY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYSTEMS_MANAGER_PATCH_COMPLIANCE")
    def SYSTEMS_MANAGER_PATCH_COMPLIANCE(cls) -> "ResourceType":
        '''AWS Systems Manager patch compliance.'''
        return typing.cast("ResourceType", jsii.sget(cls, "SYSTEMS_MANAGER_PATCH_COMPLIANCE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="WAF_RATE_BASED_RULE")
    def WAF_RATE_BASED_RULE(cls) -> "ResourceType":
        '''AWS WAF rate based rule.'''
        return typing.cast("ResourceType", jsii.sget(cls, "WAF_RATE_BASED_RULE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="WAF_REGIONAL_RATE_BASED_RULE")
    def WAF_REGIONAL_RATE_BASED_RULE(cls) -> "ResourceType":
        '''AWS WAF regional rate based rule.'''
        return typing.cast("ResourceType", jsii.sget(cls, "WAF_REGIONAL_RATE_BASED_RULE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="WAF_REGIONAL_RULE")
    def WAF_REGIONAL_RULE(cls) -> "ResourceType":
        '''AWS WAF regional rule.'''
        return typing.cast("ResourceType", jsii.sget(cls, "WAF_REGIONAL_RULE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="WAF_REGIONAL_RULE_GROUP")
    def WAF_REGIONAL_RULE_GROUP(cls) -> "ResourceType":
        '''AWS WAF regional rule group.'''
        return typing.cast("ResourceType", jsii.sget(cls, "WAF_REGIONAL_RULE_GROUP"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="WAF_REGIONAL_WEB_ACL")
    def WAF_REGIONAL_WEB_ACL(cls) -> "ResourceType":
        '''AWS WAF web ACL.'''
        return typing.cast("ResourceType", jsii.sget(cls, "WAF_REGIONAL_WEB_ACL"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="WAF_RULE")
    def WAF_RULE(cls) -> "ResourceType":
        '''AWS WAF rule.'''
        return typing.cast("ResourceType", jsii.sget(cls, "WAF_RULE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="WAF_RULE_GROUP")
    def WAF_RULE_GROUP(cls) -> "ResourceType":
        '''AWS WAF rule group.'''
        return typing.cast("ResourceType", jsii.sget(cls, "WAF_RULE_GROUP"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="WAF_WEB_ACL")
    def WAF_WEB_ACL(cls) -> "ResourceType":
        '''AWS WAF web ACL.'''
        return typing.cast("ResourceType", jsii.sget(cls, "WAF_WEB_ACL"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="WAFV2_MANAGED_RULE_SET")
    def WAFV2_MANAGED_RULE_SET(cls) -> "ResourceType":
        '''AWS WAFv2 managed rule set.'''
        return typing.cast("ResourceType", jsii.sget(cls, "WAFV2_MANAGED_RULE_SET"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="WAFV2_RULE_GROUP")
    def WAFV2_RULE_GROUP(cls) -> "ResourceType":
        '''AWS WAFv2 rule group.'''
        return typing.cast("ResourceType", jsii.sget(cls, "WAFV2_RULE_GROUP"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="WAFV2_WEB_ACL")
    def WAFV2_WEB_ACL(cls) -> "ResourceType":
        '''AWS WAFv2 web ACL.'''
        return typing.cast("ResourceType", jsii.sget(cls, "WAFV2_WEB_ACL"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="XRAY_ENCRYPTION_CONFIGURATION")
    def XRAY_ENCRYPTION_CONFIGURATION(cls) -> "ResourceType":
        '''AWS X-Ray encryption configuration.'''
        return typing.cast("ResourceType", jsii.sget(cls, "XRAY_ENCRYPTION_CONFIGURATION"))

    @builtins.property
    @jsii.member(jsii_name="complianceResourceType")
    def compliance_resource_type(self) -> builtins.str:
        '''Valid value of resource type.'''
        return typing.cast(builtins.str, jsii.get(self, "complianceResourceType"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-config.RuleProps",
    jsii_struct_bases=[],
    name_mapping={
        "config_rule_name": "configRuleName",
        "description": "description",
        "input_parameters": "inputParameters",
        "maximum_execution_frequency": "maximumExecutionFrequency",
        "rule_scope": "ruleScope",
    },
)
class RuleProps:
    def __init__(
        self,
        *,
        config_rule_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
        rule_scope: typing.Optional["RuleScope"] = None,
    ) -> None:
        '''Construction properties for a new rule.

        :param config_rule_name: A name for the AWS Config rule. Default: - CloudFormation generated name
        :param description: A description about this AWS Config rule. Default: - No description
        :param input_parameters: Input parameter values that are passed to the AWS Config rule. Default: - No input parameters
        :param maximum_execution_frequency: The maximum frequency at which the AWS Config rule runs evaluations. Default: MaximumExecutionFrequency.TWENTY_FOUR_HOURS
        :param rule_scope: Defines which resources trigger an evaluation for an AWS Config rule. Default: - evaluations for the rule are triggered when any resource in the recording group changes.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_config as config
            
            # input_parameters: Any
            # rule_scope: config.RuleScope
            
            rule_props = config.RuleProps(
                config_rule_name="configRuleName",
                description="description",
                input_parameters={
                    "input_parameters_key": input_parameters
                },
                maximum_execution_frequency=config.MaximumExecutionFrequency.ONE_HOUR,
                rule_scope=rule_scope
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1eb734ae9fa747b5a43ec647ab46db612926a3fb07a8693cf4152d7f092a895a)
            check_type(argname="argument config_rule_name", value=config_rule_name, expected_type=type_hints["config_rule_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument input_parameters", value=input_parameters, expected_type=type_hints["input_parameters"])
            check_type(argname="argument maximum_execution_frequency", value=maximum_execution_frequency, expected_type=type_hints["maximum_execution_frequency"])
            check_type(argname="argument rule_scope", value=rule_scope, expected_type=type_hints["rule_scope"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if config_rule_name is not None:
            self._values["config_rule_name"] = config_rule_name
        if description is not None:
            self._values["description"] = description
        if input_parameters is not None:
            self._values["input_parameters"] = input_parameters
        if maximum_execution_frequency is not None:
            self._values["maximum_execution_frequency"] = maximum_execution_frequency
        if rule_scope is not None:
            self._values["rule_scope"] = rule_scope

    @builtins.property
    def config_rule_name(self) -> typing.Optional[builtins.str]:
        '''A name for the AWS Config rule.

        :default: - CloudFormation generated name
        '''
        result = self._values.get("config_rule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description about this AWS Config rule.

        :default: - No description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def input_parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Input parameter values that are passed to the AWS Config rule.

        :default: - No input parameters
        '''
        result = self._values.get("input_parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def maximum_execution_frequency(self) -> typing.Optional[MaximumExecutionFrequency]:
        '''The maximum frequency at which the AWS Config rule runs evaluations.

        :default: MaximumExecutionFrequency.TWENTY_FOUR_HOURS
        '''
        result = self._values.get("maximum_execution_frequency")
        return typing.cast(typing.Optional[MaximumExecutionFrequency], result)

    @builtins.property
    def rule_scope(self) -> typing.Optional["RuleScope"]:
        '''Defines which resources trigger an evaluation for an AWS Config rule.

        :default: - evaluations for the rule are triggered when any resource in the recording group changes.
        '''
        result = self._values.get("rule_scope")
        return typing.cast(typing.Optional["RuleScope"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RuleScope(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-config.RuleScope"):
    '''Determines which resources trigger an evaluation of an AWS Config rule.

    :exampleMetadata: infused

    Example::

        # eval_compliance_fn: lambda.Function
        ssh_rule = config.ManagedRule(self, "SSH",
            identifier=config.ManagedRuleIdentifiers.EC2_SECURITY_GROUPS_INCOMING_SSH_DISABLED,
            rule_scope=config.RuleScope.from_resource(config.ResourceType.EC2_SECURITY_GROUP, "sg-1234567890abcdefgh")
        )
        custom_rule = config.CustomRule(self, "Lambda",
            lambda_function=eval_compliance_fn,
            configuration_changes=True,
            rule_scope=config.RuleScope.from_resources([config.ResourceType.CLOUDFORMATION_STACK, config.ResourceType.S3_BUCKET])
        )
        
        tag_rule = config.CustomRule(self, "CostCenterTagRule",
            lambda_function=eval_compliance_fn,
            configuration_changes=True,
            rule_scope=config.RuleScope.from_tag("Cost Center", "MyApp")
        )
    '''

    @jsii.member(jsii_name="fromResource")
    @builtins.classmethod
    def from_resource(
        cls,
        resource_type: ResourceType,
        resource_id: typing.Optional[builtins.str] = None,
    ) -> "RuleScope":
        '''restricts scope of changes to a specific resource type or resource identifier.

        :param resource_type: -
        :param resource_id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38acf6b71126be6e2db421239e9babdd7462f42529ef7bc257f9fa610a56fc28)
            check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
            check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
        return typing.cast("RuleScope", jsii.sinvoke(cls, "fromResource", [resource_type, resource_id]))

    @jsii.member(jsii_name="fromResources")
    @builtins.classmethod
    def from_resources(
        cls,
        resource_types: typing.Sequence[ResourceType],
    ) -> "RuleScope":
        '''restricts scope of changes to specific resource types.

        :param resource_types: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2696024e628939ed8f328e89e342d436fb2013b56f930ea22a6fd5ca180ad1f1)
            check_type(argname="argument resource_types", value=resource_types, expected_type=type_hints["resource_types"])
        return typing.cast("RuleScope", jsii.sinvoke(cls, "fromResources", [resource_types]))

    @jsii.member(jsii_name="fromTag")
    @builtins.classmethod
    def from_tag(
        cls,
        key: builtins.str,
        value: typing.Optional[builtins.str] = None,
    ) -> "RuleScope":
        '''restricts scope of changes to a specific tag.

        :param key: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57c51734c4ad182dafcb7de6caf0313b81055e8eed34201f631c6536e565cf82)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("RuleScope", jsii.sinvoke(cls, "fromTag", [key, value]))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> typing.Optional[builtins.str]:
        '''tag key applied to resources that will trigger evaluation of a rule.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "key"))

    @builtins.property
    @jsii.member(jsii_name="resourceId")
    def resource_id(self) -> typing.Optional[builtins.str]:
        '''ID of the only AWS resource that will trigger evaluation of a rule.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceId"))

    @builtins.property
    @jsii.member(jsii_name="resourceTypes")
    def resource_types(self) -> typing.Optional[typing.List[ResourceType]]:
        '''Resource types that will trigger evaluation of a rule.'''
        return typing.cast(typing.Optional[typing.List[ResourceType]], jsii.get(self, "resourceTypes"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> typing.Optional[builtins.str]:
        '''tag value applied to resources that will trigger evaluation of a rule.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "value"))


class AccessKeysRotated(
    ManagedRule,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-config.AccessKeysRotated",
):
    '''Checks whether the active access keys are rotated within the number of days specified in ``maxAge``.

    :see: https://docs.aws.amazon.com/config/latest/developerguide/access-keys-rotated.html
    :resource: AWS::Config::ConfigRule
    :exampleMetadata: infused

    Example::

        # compliant if access keys have been rotated within the last 90 days
        config.AccessKeysRotated(self, "AccessKeyRotated")
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        max_age: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
        config_rule_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
        rule_scope: typing.Optional[RuleScope] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param max_age: The maximum number of days within which the access keys must be rotated. Default: Duration.days(90)
        :param config_rule_name: A name for the AWS Config rule. Default: - CloudFormation generated name
        :param description: A description about this AWS Config rule. Default: - No description
        :param input_parameters: Input parameter values that are passed to the AWS Config rule. Default: - No input parameters
        :param maximum_execution_frequency: The maximum frequency at which the AWS Config rule runs evaluations. Default: MaximumExecutionFrequency.TWENTY_FOUR_HOURS
        :param rule_scope: Defines which resources trigger an evaluation for an AWS Config rule. Default: - evaluations for the rule are triggered when any resource in the recording group changes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d49a760448522c6803de30b2dcd450ab9ed427fbc0536ea5a08d26cb910421a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = AccessKeysRotatedProps(
            max_age=max_age,
            config_rule_name=config_rule_name,
            description=description,
            input_parameters=input_parameters,
            maximum_execution_frequency=maximum_execution_frequency,
            rule_scope=rule_scope,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@aws-cdk/aws-config.AccessKeysRotatedProps",
    jsii_struct_bases=[RuleProps],
    name_mapping={
        "config_rule_name": "configRuleName",
        "description": "description",
        "input_parameters": "inputParameters",
        "maximum_execution_frequency": "maximumExecutionFrequency",
        "rule_scope": "ruleScope",
        "max_age": "maxAge",
    },
)
class AccessKeysRotatedProps(RuleProps):
    def __init__(
        self,
        *,
        config_rule_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
        rule_scope: typing.Optional[RuleScope] = None,
        max_age: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
    ) -> None:
        '''Construction properties for a AccessKeysRotated.

        :param config_rule_name: A name for the AWS Config rule. Default: - CloudFormation generated name
        :param description: A description about this AWS Config rule. Default: - No description
        :param input_parameters: Input parameter values that are passed to the AWS Config rule. Default: - No input parameters
        :param maximum_execution_frequency: The maximum frequency at which the AWS Config rule runs evaluations. Default: MaximumExecutionFrequency.TWENTY_FOUR_HOURS
        :param rule_scope: Defines which resources trigger an evaluation for an AWS Config rule. Default: - evaluations for the rule are triggered when any resource in the recording group changes.
        :param max_age: The maximum number of days within which the access keys must be rotated. Default: Duration.days(90)

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_config as config
            import aws_cdk.core as cdk
            
            # input_parameters: Any
            # rule_scope: config.RuleScope
            
            access_keys_rotated_props = config.AccessKeysRotatedProps(
                config_rule_name="configRuleName",
                description="description",
                input_parameters={
                    "input_parameters_key": input_parameters
                },
                max_age=cdk.Duration.minutes(30),
                maximum_execution_frequency=config.MaximumExecutionFrequency.ONE_HOUR,
                rule_scope=rule_scope
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__110381818ee33aac9a13be24c45e46644cf89f78d758658859b149b9f88fcd9d)
            check_type(argname="argument config_rule_name", value=config_rule_name, expected_type=type_hints["config_rule_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument input_parameters", value=input_parameters, expected_type=type_hints["input_parameters"])
            check_type(argname="argument maximum_execution_frequency", value=maximum_execution_frequency, expected_type=type_hints["maximum_execution_frequency"])
            check_type(argname="argument rule_scope", value=rule_scope, expected_type=type_hints["rule_scope"])
            check_type(argname="argument max_age", value=max_age, expected_type=type_hints["max_age"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if config_rule_name is not None:
            self._values["config_rule_name"] = config_rule_name
        if description is not None:
            self._values["description"] = description
        if input_parameters is not None:
            self._values["input_parameters"] = input_parameters
        if maximum_execution_frequency is not None:
            self._values["maximum_execution_frequency"] = maximum_execution_frequency
        if rule_scope is not None:
            self._values["rule_scope"] = rule_scope
        if max_age is not None:
            self._values["max_age"] = max_age

    @builtins.property
    def config_rule_name(self) -> typing.Optional[builtins.str]:
        '''A name for the AWS Config rule.

        :default: - CloudFormation generated name
        '''
        result = self._values.get("config_rule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description about this AWS Config rule.

        :default: - No description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def input_parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Input parameter values that are passed to the AWS Config rule.

        :default: - No input parameters
        '''
        result = self._values.get("input_parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def maximum_execution_frequency(self) -> typing.Optional[MaximumExecutionFrequency]:
        '''The maximum frequency at which the AWS Config rule runs evaluations.

        :default: MaximumExecutionFrequency.TWENTY_FOUR_HOURS
        '''
        result = self._values.get("maximum_execution_frequency")
        return typing.cast(typing.Optional[MaximumExecutionFrequency], result)

    @builtins.property
    def rule_scope(self) -> typing.Optional[RuleScope]:
        '''Defines which resources trigger an evaluation for an AWS Config rule.

        :default: - evaluations for the rule are triggered when any resource in the recording group changes.
        '''
        result = self._values.get("rule_scope")
        return typing.cast(typing.Optional[RuleScope], result)

    @builtins.property
    def max_age(self) -> typing.Optional[_aws_cdk_core_f4b25747.Duration]:
        '''The maximum number of days within which the access keys must be rotated.

        :default: Duration.days(90)
        '''
        result = self._values.get("max_age")
        return typing.cast(typing.Optional[_aws_cdk_core_f4b25747.Duration], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessKeysRotatedProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudFormationStackDriftDetectionCheck(
    ManagedRule,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-config.CloudFormationStackDriftDetectionCheck",
):
    '''Checks whether your CloudFormation stacks' actual configuration differs, or has drifted, from its expected configuration.

    :see: https://docs.aws.amazon.com/config/latest/developerguide/cloudformation-stack-drift-detection-check.html
    :resource: AWS::Config::ConfigRule
    :exampleMetadata: infused

    Example::

        # Topic to which compliance notification events will be published
        compliance_topic = sns.Topic(self, "ComplianceTopic")
        
        rule = config.CloudFormationStackDriftDetectionCheck(self, "Drift")
        rule.on_compliance_change("TopicEvent",
            target=targets.SnsTopic(compliance_topic)
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        own_stack_only: typing.Optional[builtins.bool] = None,
        role: typing.Optional[_aws_cdk_aws_iam_940a1ce0.IRole] = None,
        config_rule_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
        rule_scope: typing.Optional[RuleScope] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param own_stack_only: Whether to check only the stack where this rule is deployed. Default: false
        :param role: The IAM role to use for this rule. It must have permissions to detect drift for AWS CloudFormation stacks. Ensure to attach ``config.amazonaws.com`` trusted permissions and ``ReadOnlyAccess`` policy permissions. For specific policy permissions, refer to https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html. Default: - A role will be created
        :param config_rule_name: A name for the AWS Config rule. Default: - CloudFormation generated name
        :param description: A description about this AWS Config rule. Default: - No description
        :param input_parameters: Input parameter values that are passed to the AWS Config rule. Default: - No input parameters
        :param maximum_execution_frequency: The maximum frequency at which the AWS Config rule runs evaluations. Default: MaximumExecutionFrequency.TWENTY_FOUR_HOURS
        :param rule_scope: Defines which resources trigger an evaluation for an AWS Config rule. Default: - evaluations for the rule are triggered when any resource in the recording group changes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56104c799461baed787cd2925d18f3a5b835f10fcf3b90ca147268f5c4fd5dac)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CloudFormationStackDriftDetectionCheckProps(
            own_stack_only=own_stack_only,
            role=role,
            config_rule_name=config_rule_name,
            description=description,
            input_parameters=input_parameters,
            maximum_execution_frequency=maximum_execution_frequency,
            rule_scope=rule_scope,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@aws-cdk/aws-config.CloudFormationStackDriftDetectionCheckProps",
    jsii_struct_bases=[RuleProps],
    name_mapping={
        "config_rule_name": "configRuleName",
        "description": "description",
        "input_parameters": "inputParameters",
        "maximum_execution_frequency": "maximumExecutionFrequency",
        "rule_scope": "ruleScope",
        "own_stack_only": "ownStackOnly",
        "role": "role",
    },
)
class CloudFormationStackDriftDetectionCheckProps(RuleProps):
    def __init__(
        self,
        *,
        config_rule_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
        rule_scope: typing.Optional[RuleScope] = None,
        own_stack_only: typing.Optional[builtins.bool] = None,
        role: typing.Optional[_aws_cdk_aws_iam_940a1ce0.IRole] = None,
    ) -> None:
        '''Construction properties for a CloudFormationStackDriftDetectionCheck.

        :param config_rule_name: A name for the AWS Config rule. Default: - CloudFormation generated name
        :param description: A description about this AWS Config rule. Default: - No description
        :param input_parameters: Input parameter values that are passed to the AWS Config rule. Default: - No input parameters
        :param maximum_execution_frequency: The maximum frequency at which the AWS Config rule runs evaluations. Default: MaximumExecutionFrequency.TWENTY_FOUR_HOURS
        :param rule_scope: Defines which resources trigger an evaluation for an AWS Config rule. Default: - evaluations for the rule are triggered when any resource in the recording group changes.
        :param own_stack_only: Whether to check only the stack where this rule is deployed. Default: false
        :param role: The IAM role to use for this rule. It must have permissions to detect drift for AWS CloudFormation stacks. Ensure to attach ``config.amazonaws.com`` trusted permissions and ``ReadOnlyAccess`` policy permissions. For specific policy permissions, refer to https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html. Default: - A role will be created

        :exampleMetadata: infused

        Example::

            # compliant if stack's status is 'IN_SYNC'
            # non-compliant if the stack's drift status is 'DRIFTED'
            config.CloudFormationStackDriftDetectionCheck(self, "Drift",
                own_stack_only=True
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ec5db3cf27da842ae7b04c0e7f299129e58954e79f505a26626d856e777953d)
            check_type(argname="argument config_rule_name", value=config_rule_name, expected_type=type_hints["config_rule_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument input_parameters", value=input_parameters, expected_type=type_hints["input_parameters"])
            check_type(argname="argument maximum_execution_frequency", value=maximum_execution_frequency, expected_type=type_hints["maximum_execution_frequency"])
            check_type(argname="argument rule_scope", value=rule_scope, expected_type=type_hints["rule_scope"])
            check_type(argname="argument own_stack_only", value=own_stack_only, expected_type=type_hints["own_stack_only"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if config_rule_name is not None:
            self._values["config_rule_name"] = config_rule_name
        if description is not None:
            self._values["description"] = description
        if input_parameters is not None:
            self._values["input_parameters"] = input_parameters
        if maximum_execution_frequency is not None:
            self._values["maximum_execution_frequency"] = maximum_execution_frequency
        if rule_scope is not None:
            self._values["rule_scope"] = rule_scope
        if own_stack_only is not None:
            self._values["own_stack_only"] = own_stack_only
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def config_rule_name(self) -> typing.Optional[builtins.str]:
        '''A name for the AWS Config rule.

        :default: - CloudFormation generated name
        '''
        result = self._values.get("config_rule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description about this AWS Config rule.

        :default: - No description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def input_parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Input parameter values that are passed to the AWS Config rule.

        :default: - No input parameters
        '''
        result = self._values.get("input_parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def maximum_execution_frequency(self) -> typing.Optional[MaximumExecutionFrequency]:
        '''The maximum frequency at which the AWS Config rule runs evaluations.

        :default: MaximumExecutionFrequency.TWENTY_FOUR_HOURS
        '''
        result = self._values.get("maximum_execution_frequency")
        return typing.cast(typing.Optional[MaximumExecutionFrequency], result)

    @builtins.property
    def rule_scope(self) -> typing.Optional[RuleScope]:
        '''Defines which resources trigger an evaluation for an AWS Config rule.

        :default: - evaluations for the rule are triggered when any resource in the recording group changes.
        '''
        result = self._values.get("rule_scope")
        return typing.cast(typing.Optional[RuleScope], result)

    @builtins.property
    def own_stack_only(self) -> typing.Optional[builtins.bool]:
        '''Whether to check only the stack where this rule is deployed.

        :default: false
        '''
        result = self._values.get("own_stack_only")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def role(self) -> typing.Optional[_aws_cdk_aws_iam_940a1ce0.IRole]:
        '''The IAM role to use for this rule.

        It must have permissions to detect drift
        for AWS CloudFormation stacks. Ensure to attach ``config.amazonaws.com`` trusted
        permissions and ``ReadOnlyAccess`` policy permissions. For specific policy permissions,
        refer to https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html.

        :default: - A role will be created
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_aws_cdk_aws_iam_940a1ce0.IRole], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudFormationStackDriftDetectionCheckProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudFormationStackNotificationCheck(
    ManagedRule,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-config.CloudFormationStackNotificationCheck",
):
    '''Checks whether your CloudFormation stacks are sending event notifications to a SNS topic.

    Optionally checks whether specified SNS topics are used.

    :see: https://docs.aws.amazon.com/config/latest/developerguide/cloudformation-stack-notification-check.html
    :resource: AWS::Config::ConfigRule
    :exampleMetadata: infused

    Example::

        # topics to which CloudFormation stacks may send event notifications
        topic1 = sns.Topic(self, "AllowedTopic1")
        topic2 = sns.Topic(self, "AllowedTopic2")
        
        # non-compliant if CloudFormation stack does not send notifications to 'topic1' or 'topic2'
        config.CloudFormationStackNotificationCheck(self, "NotificationCheck",
            topics=[topic1, topic2]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        topics: typing.Optional[typing.Sequence[_aws_cdk_aws_sns_889c7272.ITopic]] = None,
        config_rule_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
        rule_scope: typing.Optional[RuleScope] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param topics: A list of allowed topics. At most 5 topics. Default: - No topics.
        :param config_rule_name: A name for the AWS Config rule. Default: - CloudFormation generated name
        :param description: A description about this AWS Config rule. Default: - No description
        :param input_parameters: Input parameter values that are passed to the AWS Config rule. Default: - No input parameters
        :param maximum_execution_frequency: The maximum frequency at which the AWS Config rule runs evaluations. Default: MaximumExecutionFrequency.TWENTY_FOUR_HOURS
        :param rule_scope: Defines which resources trigger an evaluation for an AWS Config rule. Default: - evaluations for the rule are triggered when any resource in the recording group changes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__893553c8bd0d925f3ddc6db39e56ccd8dcdd58609837e4f9603f4eca6bc0710f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CloudFormationStackNotificationCheckProps(
            topics=topics,
            config_rule_name=config_rule_name,
            description=description,
            input_parameters=input_parameters,
            maximum_execution_frequency=maximum_execution_frequency,
            rule_scope=rule_scope,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@aws-cdk/aws-config.CloudFormationStackNotificationCheckProps",
    jsii_struct_bases=[RuleProps],
    name_mapping={
        "config_rule_name": "configRuleName",
        "description": "description",
        "input_parameters": "inputParameters",
        "maximum_execution_frequency": "maximumExecutionFrequency",
        "rule_scope": "ruleScope",
        "topics": "topics",
    },
)
class CloudFormationStackNotificationCheckProps(RuleProps):
    def __init__(
        self,
        *,
        config_rule_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
        rule_scope: typing.Optional[RuleScope] = None,
        topics: typing.Optional[typing.Sequence[_aws_cdk_aws_sns_889c7272.ITopic]] = None,
    ) -> None:
        '''Construction properties for a CloudFormationStackNotificationCheck.

        :param config_rule_name: A name for the AWS Config rule. Default: - CloudFormation generated name
        :param description: A description about this AWS Config rule. Default: - No description
        :param input_parameters: Input parameter values that are passed to the AWS Config rule. Default: - No input parameters
        :param maximum_execution_frequency: The maximum frequency at which the AWS Config rule runs evaluations. Default: MaximumExecutionFrequency.TWENTY_FOUR_HOURS
        :param rule_scope: Defines which resources trigger an evaluation for an AWS Config rule. Default: - evaluations for the rule are triggered when any resource in the recording group changes.
        :param topics: A list of allowed topics. At most 5 topics. Default: - No topics.

        :exampleMetadata: infused

        Example::

            # topics to which CloudFormation stacks may send event notifications
            topic1 = sns.Topic(self, "AllowedTopic1")
            topic2 = sns.Topic(self, "AllowedTopic2")
            
            # non-compliant if CloudFormation stack does not send notifications to 'topic1' or 'topic2'
            config.CloudFormationStackNotificationCheck(self, "NotificationCheck",
                topics=[topic1, topic2]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bfc41ded906165c8d587958aa47c05624a8923f15a45d1cf04030b4ffa6bcb8)
            check_type(argname="argument config_rule_name", value=config_rule_name, expected_type=type_hints["config_rule_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument input_parameters", value=input_parameters, expected_type=type_hints["input_parameters"])
            check_type(argname="argument maximum_execution_frequency", value=maximum_execution_frequency, expected_type=type_hints["maximum_execution_frequency"])
            check_type(argname="argument rule_scope", value=rule_scope, expected_type=type_hints["rule_scope"])
            check_type(argname="argument topics", value=topics, expected_type=type_hints["topics"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if config_rule_name is not None:
            self._values["config_rule_name"] = config_rule_name
        if description is not None:
            self._values["description"] = description
        if input_parameters is not None:
            self._values["input_parameters"] = input_parameters
        if maximum_execution_frequency is not None:
            self._values["maximum_execution_frequency"] = maximum_execution_frequency
        if rule_scope is not None:
            self._values["rule_scope"] = rule_scope
        if topics is not None:
            self._values["topics"] = topics

    @builtins.property
    def config_rule_name(self) -> typing.Optional[builtins.str]:
        '''A name for the AWS Config rule.

        :default: - CloudFormation generated name
        '''
        result = self._values.get("config_rule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description about this AWS Config rule.

        :default: - No description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def input_parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Input parameter values that are passed to the AWS Config rule.

        :default: - No input parameters
        '''
        result = self._values.get("input_parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def maximum_execution_frequency(self) -> typing.Optional[MaximumExecutionFrequency]:
        '''The maximum frequency at which the AWS Config rule runs evaluations.

        :default: MaximumExecutionFrequency.TWENTY_FOUR_HOURS
        '''
        result = self._values.get("maximum_execution_frequency")
        return typing.cast(typing.Optional[MaximumExecutionFrequency], result)

    @builtins.property
    def rule_scope(self) -> typing.Optional[RuleScope]:
        '''Defines which resources trigger an evaluation for an AWS Config rule.

        :default: - evaluations for the rule are triggered when any resource in the recording group changes.
        '''
        result = self._values.get("rule_scope")
        return typing.cast(typing.Optional[RuleScope], result)

    @builtins.property
    def topics(self) -> typing.Optional[typing.List[_aws_cdk_aws_sns_889c7272.ITopic]]:
        '''A list of allowed topics.

        At most 5 topics.

        :default: - No topics.
        '''
        result = self._values.get("topics")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_aws_sns_889c7272.ITopic]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudFormationStackNotificationCheckProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IRule)
class CustomRule(
    _aws_cdk_core_f4b25747.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-config.CustomRule",
):
    '''A new custom rule.

    :resource: AWS::Config::ConfigRule
    :exampleMetadata: infused

    Example::

        # Lambda function containing logic that evaluates compliance with the rule.
        eval_compliance_fn = lambda_.Function(self, "CustomFunction",
            code=lambda_.AssetCode.from_inline("exports.handler = (event) => console.log(event);"),
            handler="index.handler",
            runtime=lambda_.Runtime.NODEJS_14_X
        )
        
        # A custom rule that runs on configuration changes of EC2 instances
        custom_rule = config.CustomRule(self, "Custom",
            configuration_changes=True,
            lambda_function=eval_compliance_fn,
            rule_scope=config.RuleScope.from_resource(config.ResourceType.EC2_INSTANCE)
        )
        
        # A rule to detect stack drifts
        drift_rule = config.CloudFormationStackDriftDetectionCheck(self, "Drift")
        
        # Topic to which compliance notification events will be published
        compliance_topic = sns.Topic(self, "ComplianceTopic")
        
        # Send notification on compliance change events
        drift_rule.on_compliance_change("ComplianceChange",
            target=targets.SnsTopic(compliance_topic)
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        lambda_function: _aws_cdk_aws_lambda_5443dbc3.IFunction,
        configuration_changes: typing.Optional[builtins.bool] = None,
        periodic: typing.Optional[builtins.bool] = None,
        config_rule_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
        rule_scope: typing.Optional[RuleScope] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param lambda_function: The Lambda function to run.
        :param configuration_changes: Whether to run the rule on configuration changes. Default: false
        :param periodic: Whether to run the rule on a fixed frequency. Default: false
        :param config_rule_name: A name for the AWS Config rule. Default: - CloudFormation generated name
        :param description: A description about this AWS Config rule. Default: - No description
        :param input_parameters: Input parameter values that are passed to the AWS Config rule. Default: - No input parameters
        :param maximum_execution_frequency: The maximum frequency at which the AWS Config rule runs evaluations. Default: MaximumExecutionFrequency.TWENTY_FOUR_HOURS
        :param rule_scope: Defines which resources trigger an evaluation for an AWS Config rule. Default: - evaluations for the rule are triggered when any resource in the recording group changes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fefbcb451627baeca7df97e860fdcd28d644e5917c08a5ba02e320e9ba8ab076)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CustomRuleProps(
            lambda_function=lambda_function,
            configuration_changes=configuration_changes,
            periodic=periodic,
            config_rule_name=config_rule_name,
            description=description,
            input_parameters=input_parameters,
            maximum_execution_frequency=maximum_execution_frequency,
            rule_scope=rule_scope,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromConfigRuleName")
    @builtins.classmethod
    def from_config_rule_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        config_rule_name: builtins.str,
    ) -> IRule:
        '''Imports an existing rule.

        :param scope: -
        :param id: -
        :param config_rule_name: the name of the rule.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41f23c6abdf80a81de31e9143dd051ed924c5cac8b2b927c30e19c48881d1f0b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument config_rule_name", value=config_rule_name, expected_type=type_hints["config_rule_name"])
        return typing.cast(IRule, jsii.sinvoke(cls, "fromConfigRuleName", [scope, id, config_rule_name]))

    @jsii.member(jsii_name="onComplianceChange")
    def on_compliance_change(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_aws_cdk_aws_events_efcdfa54.EventPattern, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[_aws_cdk_aws_events_efcdfa54.IRuleTarget] = None,
    ) -> _aws_cdk_aws_events_efcdfa54.Rule:
        '''Defines an EventBridge event rule which triggers for rule compliance events.

        :param id: -
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33890b0042eb3061675d88c7fef5896069cfe0db429fb2e284fb2f64236b01ab)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _aws_cdk_aws_events_efcdfa54.OnEventOptions(
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
            target=target,
        )

        return typing.cast(_aws_cdk_aws_events_efcdfa54.Rule, jsii.invoke(self, "onComplianceChange", [id, options]))

    @jsii.member(jsii_name="onEvent")
    def on_event(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_aws_cdk_aws_events_efcdfa54.EventPattern, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[_aws_cdk_aws_events_efcdfa54.IRuleTarget] = None,
    ) -> _aws_cdk_aws_events_efcdfa54.Rule:
        '''Defines an EventBridge event rule which triggers for rule events.

        Use
        ``rule.addEventPattern(pattern)`` to specify a filter.

        :param id: -
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f78558801c57a29946ae502612db9239b081d1adcddf8c1a3f5309df5a94af2)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _aws_cdk_aws_events_efcdfa54.OnEventOptions(
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
            target=target,
        )

        return typing.cast(_aws_cdk_aws_events_efcdfa54.Rule, jsii.invoke(self, "onEvent", [id, options]))

    @jsii.member(jsii_name="onReEvaluationStatus")
    def on_re_evaluation_status(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_aws_cdk_aws_events_efcdfa54.EventPattern, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[_aws_cdk_aws_events_efcdfa54.IRuleTarget] = None,
    ) -> _aws_cdk_aws_events_efcdfa54.Rule:
        '''Defines an EventBridge event rule which triggers for rule re-evaluation status events.

        :param id: -
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07b7f6c542aa9138489d9d4f6762a34af78d103cdab0527b6bc7250351b7a76e)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _aws_cdk_aws_events_efcdfa54.OnEventOptions(
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
            target=target,
        )

        return typing.cast(_aws_cdk_aws_events_efcdfa54.Rule, jsii.invoke(self, "onReEvaluationStatus", [id, options]))

    @builtins.property
    @jsii.member(jsii_name="configRuleArn")
    def config_rule_arn(self) -> builtins.str:
        '''The arn of the rule.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "configRuleArn"))

    @builtins.property
    @jsii.member(jsii_name="configRuleComplianceType")
    def config_rule_compliance_type(self) -> builtins.str:
        '''The compliance status of the rule.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "configRuleComplianceType"))

    @builtins.property
    @jsii.member(jsii_name="configRuleId")
    def config_rule_id(self) -> builtins.str:
        '''The id of the rule.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "configRuleId"))

    @builtins.property
    @jsii.member(jsii_name="configRuleName")
    def config_rule_name(self) -> builtins.str:
        '''The name of the rule.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "configRuleName"))

    @builtins.property
    @jsii.member(jsii_name="isCustomWithChanges")
    def _is_custom_with_changes(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "isCustomWithChanges"))

    @_is_custom_with_changes.setter
    def _is_custom_with_changes(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0dfb2b453bc3a9748fc10ac4aeaaab883bb1b8c50304ccbbb0fd74b6990ae0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isCustomWithChanges", value)

    @builtins.property
    @jsii.member(jsii_name="isManaged")
    def _is_managed(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "isManaged"))

    @_is_managed.setter
    def _is_managed(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69bfb50702eaeee8b588ec7a0bf8660ef1defed02d163bc9cb6e1dfd046eb8d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isManaged", value)

    @builtins.property
    @jsii.member(jsii_name="ruleScope")
    def _rule_scope(self) -> typing.Optional[RuleScope]:
        return typing.cast(typing.Optional[RuleScope], jsii.get(self, "ruleScope"))

    @_rule_scope.setter
    def _rule_scope(self, value: typing.Optional[RuleScope]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc8ec6e11f15eb8246f61611f9a28a4f439ce0eeeae26c891035ba7c4a01ae08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleScope", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-config.CustomRuleProps",
    jsii_struct_bases=[RuleProps],
    name_mapping={
        "config_rule_name": "configRuleName",
        "description": "description",
        "input_parameters": "inputParameters",
        "maximum_execution_frequency": "maximumExecutionFrequency",
        "rule_scope": "ruleScope",
        "lambda_function": "lambdaFunction",
        "configuration_changes": "configurationChanges",
        "periodic": "periodic",
    },
)
class CustomRuleProps(RuleProps):
    def __init__(
        self,
        *,
        config_rule_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
        rule_scope: typing.Optional[RuleScope] = None,
        lambda_function: _aws_cdk_aws_lambda_5443dbc3.IFunction,
        configuration_changes: typing.Optional[builtins.bool] = None,
        periodic: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Construction properties for a CustomRule.

        :param config_rule_name: A name for the AWS Config rule. Default: - CloudFormation generated name
        :param description: A description about this AWS Config rule. Default: - No description
        :param input_parameters: Input parameter values that are passed to the AWS Config rule. Default: - No input parameters
        :param maximum_execution_frequency: The maximum frequency at which the AWS Config rule runs evaluations. Default: MaximumExecutionFrequency.TWENTY_FOUR_HOURS
        :param rule_scope: Defines which resources trigger an evaluation for an AWS Config rule. Default: - evaluations for the rule are triggered when any resource in the recording group changes.
        :param lambda_function: The Lambda function to run.
        :param configuration_changes: Whether to run the rule on configuration changes. Default: false
        :param periodic: Whether to run the rule on a fixed frequency. Default: false

        :exampleMetadata: infused

        Example::

            # Lambda function containing logic that evaluates compliance with the rule.
            eval_compliance_fn = lambda_.Function(self, "CustomFunction",
                code=lambda_.AssetCode.from_inline("exports.handler = (event) => console.log(event);"),
                handler="index.handler",
                runtime=lambda_.Runtime.NODEJS_14_X
            )
            
            # A custom rule that runs on configuration changes of EC2 instances
            custom_rule = config.CustomRule(self, "Custom",
                configuration_changes=True,
                lambda_function=eval_compliance_fn,
                rule_scope=config.RuleScope.from_resource(config.ResourceType.EC2_INSTANCE)
            )
            
            # A rule to detect stack drifts
            drift_rule = config.CloudFormationStackDriftDetectionCheck(self, "Drift")
            
            # Topic to which compliance notification events will be published
            compliance_topic = sns.Topic(self, "ComplianceTopic")
            
            # Send notification on compliance change events
            drift_rule.on_compliance_change("ComplianceChange",
                target=targets.SnsTopic(compliance_topic)
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f87c4ec243baed6d93c1df2ef1de1d5cc9217be3c7aa768471056fcf43cc8c8)
            check_type(argname="argument config_rule_name", value=config_rule_name, expected_type=type_hints["config_rule_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument input_parameters", value=input_parameters, expected_type=type_hints["input_parameters"])
            check_type(argname="argument maximum_execution_frequency", value=maximum_execution_frequency, expected_type=type_hints["maximum_execution_frequency"])
            check_type(argname="argument rule_scope", value=rule_scope, expected_type=type_hints["rule_scope"])
            check_type(argname="argument lambda_function", value=lambda_function, expected_type=type_hints["lambda_function"])
            check_type(argname="argument configuration_changes", value=configuration_changes, expected_type=type_hints["configuration_changes"])
            check_type(argname="argument periodic", value=periodic, expected_type=type_hints["periodic"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "lambda_function": lambda_function,
        }
        if config_rule_name is not None:
            self._values["config_rule_name"] = config_rule_name
        if description is not None:
            self._values["description"] = description
        if input_parameters is not None:
            self._values["input_parameters"] = input_parameters
        if maximum_execution_frequency is not None:
            self._values["maximum_execution_frequency"] = maximum_execution_frequency
        if rule_scope is not None:
            self._values["rule_scope"] = rule_scope
        if configuration_changes is not None:
            self._values["configuration_changes"] = configuration_changes
        if periodic is not None:
            self._values["periodic"] = periodic

    @builtins.property
    def config_rule_name(self) -> typing.Optional[builtins.str]:
        '''A name for the AWS Config rule.

        :default: - CloudFormation generated name
        '''
        result = self._values.get("config_rule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description about this AWS Config rule.

        :default: - No description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def input_parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Input parameter values that are passed to the AWS Config rule.

        :default: - No input parameters
        '''
        result = self._values.get("input_parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def maximum_execution_frequency(self) -> typing.Optional[MaximumExecutionFrequency]:
        '''The maximum frequency at which the AWS Config rule runs evaluations.

        :default: MaximumExecutionFrequency.TWENTY_FOUR_HOURS
        '''
        result = self._values.get("maximum_execution_frequency")
        return typing.cast(typing.Optional[MaximumExecutionFrequency], result)

    @builtins.property
    def rule_scope(self) -> typing.Optional[RuleScope]:
        '''Defines which resources trigger an evaluation for an AWS Config rule.

        :default: - evaluations for the rule are triggered when any resource in the recording group changes.
        '''
        result = self._values.get("rule_scope")
        return typing.cast(typing.Optional[RuleScope], result)

    @builtins.property
    def lambda_function(self) -> _aws_cdk_aws_lambda_5443dbc3.IFunction:
        '''The Lambda function to run.'''
        result = self._values.get("lambda_function")
        assert result is not None, "Required property 'lambda_function' is missing"
        return typing.cast(_aws_cdk_aws_lambda_5443dbc3.IFunction, result)

    @builtins.property
    def configuration_changes(self) -> typing.Optional[builtins.bool]:
        '''Whether to run the rule on configuration changes.

        :default: false
        '''
        result = self._values.get("configuration_changes")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def periodic(self) -> typing.Optional[builtins.bool]:
        '''Whether to run the rule on a fixed frequency.

        :default: false
        '''
        result = self._values.get("periodic")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CustomRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-config.ManagedRuleProps",
    jsii_struct_bases=[RuleProps],
    name_mapping={
        "config_rule_name": "configRuleName",
        "description": "description",
        "input_parameters": "inputParameters",
        "maximum_execution_frequency": "maximumExecutionFrequency",
        "rule_scope": "ruleScope",
        "identifier": "identifier",
    },
)
class ManagedRuleProps(RuleProps):
    def __init__(
        self,
        *,
        config_rule_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
        rule_scope: typing.Optional[RuleScope] = None,
        identifier: builtins.str,
    ) -> None:
        '''Construction properties for a ManagedRule.

        :param config_rule_name: A name for the AWS Config rule. Default: - CloudFormation generated name
        :param description: A description about this AWS Config rule. Default: - No description
        :param input_parameters: Input parameter values that are passed to the AWS Config rule. Default: - No input parameters
        :param maximum_execution_frequency: The maximum frequency at which the AWS Config rule runs evaluations. Default: MaximumExecutionFrequency.TWENTY_FOUR_HOURS
        :param rule_scope: Defines which resources trigger an evaluation for an AWS Config rule. Default: - evaluations for the rule are triggered when any resource in the recording group changes.
        :param identifier: The identifier of the AWS managed rule.

        :exampleMetadata: infused

        Example::

            # https://docs.aws.amazon.com/config/latest/developerguide/access-keys-rotated.html
            config.ManagedRule(self, "AccessKeysRotated",
                identifier=config.ManagedRuleIdentifiers.ACCESS_KEYS_ROTATED,
                input_parameters={
                    "max_access_key_age": 60
                },
            
                # default is 24 hours
                maximum_execution_frequency=config.MaximumExecutionFrequency.TWELVE_HOURS
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d6b3b9e342ceb3ab4ee19b736a9c2a4f43858829db3d59474bd2ac245edf9bf)
            check_type(argname="argument config_rule_name", value=config_rule_name, expected_type=type_hints["config_rule_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument input_parameters", value=input_parameters, expected_type=type_hints["input_parameters"])
            check_type(argname="argument maximum_execution_frequency", value=maximum_execution_frequency, expected_type=type_hints["maximum_execution_frequency"])
            check_type(argname="argument rule_scope", value=rule_scope, expected_type=type_hints["rule_scope"])
            check_type(argname="argument identifier", value=identifier, expected_type=type_hints["identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "identifier": identifier,
        }
        if config_rule_name is not None:
            self._values["config_rule_name"] = config_rule_name
        if description is not None:
            self._values["description"] = description
        if input_parameters is not None:
            self._values["input_parameters"] = input_parameters
        if maximum_execution_frequency is not None:
            self._values["maximum_execution_frequency"] = maximum_execution_frequency
        if rule_scope is not None:
            self._values["rule_scope"] = rule_scope

    @builtins.property
    def config_rule_name(self) -> typing.Optional[builtins.str]:
        '''A name for the AWS Config rule.

        :default: - CloudFormation generated name
        '''
        result = self._values.get("config_rule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description about this AWS Config rule.

        :default: - No description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def input_parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Input parameter values that are passed to the AWS Config rule.

        :default: - No input parameters
        '''
        result = self._values.get("input_parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def maximum_execution_frequency(self) -> typing.Optional[MaximumExecutionFrequency]:
        '''The maximum frequency at which the AWS Config rule runs evaluations.

        :default: MaximumExecutionFrequency.TWENTY_FOUR_HOURS
        '''
        result = self._values.get("maximum_execution_frequency")
        return typing.cast(typing.Optional[MaximumExecutionFrequency], result)

    @builtins.property
    def rule_scope(self) -> typing.Optional[RuleScope]:
        '''Defines which resources trigger an evaluation for an AWS Config rule.

        :default: - evaluations for the rule are triggered when any resource in the recording group changes.
        '''
        result = self._values.get("rule_scope")
        return typing.cast(typing.Optional[RuleScope], result)

    @builtins.property
    def identifier(self) -> builtins.str:
        '''The identifier of the AWS managed rule.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html
        '''
        result = self._values.get("identifier")
        assert result is not None, "Required property 'identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AccessKeysRotated",
    "AccessKeysRotatedProps",
    "CfnAggregationAuthorization",
    "CfnAggregationAuthorizationProps",
    "CfnConfigRule",
    "CfnConfigRuleProps",
    "CfnConfigurationAggregator",
    "CfnConfigurationAggregatorProps",
    "CfnConfigurationRecorder",
    "CfnConfigurationRecorderProps",
    "CfnConformancePack",
    "CfnConformancePackProps",
    "CfnDeliveryChannel",
    "CfnDeliveryChannelProps",
    "CfnOrganizationConfigRule",
    "CfnOrganizationConfigRuleProps",
    "CfnOrganizationConformancePack",
    "CfnOrganizationConformancePackProps",
    "CfnRemediationConfiguration",
    "CfnRemediationConfigurationProps",
    "CfnStoredQuery",
    "CfnStoredQueryProps",
    "CloudFormationStackDriftDetectionCheck",
    "CloudFormationStackDriftDetectionCheckProps",
    "CloudFormationStackNotificationCheck",
    "CloudFormationStackNotificationCheckProps",
    "CustomRule",
    "CustomRuleProps",
    "IRule",
    "ManagedRule",
    "ManagedRuleIdentifiers",
    "ManagedRuleProps",
    "MaximumExecutionFrequency",
    "ResourceType",
    "RuleProps",
    "RuleScope",
]

publication.publish()

def _typecheckingstub__d6a9d2dc813e1cf84217e5ea4c0bc4b35be477685bea184f0a0cc41ab6c4ac50(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    authorized_account_id: builtins.str,
    authorized_aws_region: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8afed4d6cd342dbe2306a18e89730c831d4b6a76ca932077a372a0c240df633(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f78841ee5e3698cfaf5ca0f7e4d6a43ff3e28cf72163941bdabde5bce232319(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6165e139d37da90d977b8ce17e308014c131b9ef327c8be5e2384dd97522c38b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dfd97ed4e91f2adb8693639da0cd45e3bab81e435ce21279f07b7bcecba462f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01bd187f12935f617e2d9e75fe5baa997581bb7b03471eb5a5c84722e70a2763(
    *,
    authorized_account_id: builtins.str,
    authorized_aws_region: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b715dcb856de03e35118dac99b95e0217359c82cd030ec60042b90a19d3bbc3a(
    scope_: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    source: typing.Union[typing.Union[CfnConfigRule.SourceProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable],
    config_rule_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    input_parameters: typing.Any = None,
    maximum_execution_frequency: typing.Optional[builtins.str] = None,
    scope: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnConfigRule.ScopeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db2ccae574ac49665b735a58c56db60bfa86b499e650cbcdecfb089215620ca2(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7937dfba02be731188c8748c596044bc2ee041ee6bf28ba1d46cb31a9bf5be88(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff040958078577219ea682de08dc9553e8d44daaa83242e6449ad3ee96a79523(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0f68afb3b699133231ecbc84b9f921b9c3e1f70d9b9d355dc56beb936194643(
    value: typing.Union[CfnConfigRule.SourceProperty, _aws_cdk_core_f4b25747.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3758f13125433c373ef1fbbb714d3e990846b51bf97bdb59b5d43302b0978d21(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a73645d403a17ec49d8dfd0648eacbfab6c11243826612648ecde0051791e9d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d64d9703cd2c88f8c39b9debc7cf183956e8e1c29221cdc7067713cbd5f0f07d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5356ac2e6f88f0e5e1f7b165b7bf50408cf67e439b9dacf51ed3ef3210504e87(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnConfigRule.ScopeProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06ebb7d82eb683640594e4fa806c53b9ee50c6cd4cd5ddf00d173ab257688cdd(
    *,
    enable_debug_log_delivery: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    policy_runtime: typing.Optional[builtins.str] = None,
    policy_text: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3f871ed3e31c85d7e5e120d04b6284671d677ef54d9f11ccb3c9e359c42b2d0(
    *,
    compliance_resource_id: typing.Optional[builtins.str] = None,
    compliance_resource_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    tag_key: typing.Optional[builtins.str] = None,
    tag_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2797e199072ce461a39d33ff9e62230185747dda75b6e5facbd285c3b0c5edf9(
    *,
    event_source: builtins.str,
    message_type: builtins.str,
    maximum_execution_frequency: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acb56d8b83fc364cb5dd698ef9028c60fb41d21514ce088402ea83dad69a45e5(
    *,
    owner: builtins.str,
    custom_policy_details: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnConfigRule.CustomPolicyDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    source_details: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnConfigRule.SourceDetailProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    source_identifier: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b65c6f4c78dffa21e21051386073637fda26a165240c20fb82dd516c4946490(
    *,
    source: typing.Union[typing.Union[CfnConfigRule.SourceProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable],
    config_rule_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    input_parameters: typing.Any = None,
    maximum_execution_frequency: typing.Optional[builtins.str] = None,
    scope: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnConfigRule.ScopeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25d65699ab65b867983329a04b0d91d9c7377e7e8ecf97c6a93a9af62b80c24a(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    account_aggregation_sources: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnConfigurationAggregator.AccountAggregationSourceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    configuration_aggregator_name: typing.Optional[builtins.str] = None,
    organization_aggregation_source: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnConfigurationAggregator.OrganizationAggregationSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__082ab66bb975c2363e25b7556f992d975af557f7130ef2e4117dda6aa2d63ec7(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f4f5a5bf3cbad30bbf119c1aafe52cf1f9254a12aa417f41ae14b11a9f1fb81(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e75c62528f4ad029fddbeff3ed3636efa81228c3c20898b2700b68439d06c794(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnConfigurationAggregator.AccountAggregationSourceProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efabd439525114d765db310ecae400a923c8682659664af91c7ef89071465597(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0afda739d86bd65f4de026a74441c31d72849a5a610e030860b8116599f3fb5f(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnConfigurationAggregator.OrganizationAggregationSourceProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ce2db2e204bf98d1b52629954f9ab5f5c97e9d90d92da09ef813f9c0edb7ebb(
    *,
    account_ids: typing.Sequence[builtins.str],
    all_aws_regions: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54ac6abb32014e25f820d49ee5da1db68a05c9d687343325ef4ec98072169b61(
    *,
    role_arn: builtins.str,
    all_aws_regions: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00843dd48d11cd13753b312a22e8e672e6fd05192603e46c90ffc0e969121443(
    *,
    account_aggregation_sources: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnConfigurationAggregator.AccountAggregationSourceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    configuration_aggregator_name: typing.Optional[builtins.str] = None,
    organization_aggregation_source: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnConfigurationAggregator.OrganizationAggregationSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5532e7605ebcf4129b4b1bebab2aa17aef32722b46fd205d4f12d12f94f27a10(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    role_arn: builtins.str,
    name: typing.Optional[builtins.str] = None,
    recording_group: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnConfigurationRecorder.RecordingGroupProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f69f7390ca248e9f9e0a7cbf22d8438d3c1f271da3643fbc76d44ef4e419021f(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16f03b1cbae4a38781613771e4362b1938da0a82c0b81e04e47e6c1e7725dcd4(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c325dc0dd3b3ee7e0baa17a07fecbe4fd908a5d89488b64eb7ce7fc909be1ad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80bb9afa0c20fd9088664b082f366aa41647e32a01232ae00deffea238d53be7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9018fa3a443fd91e5137c6613c147e9456d9475f934d02fc188272b54ce6df62(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnConfigurationRecorder.RecordingGroupProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ad79dedcd0640bedf2de2b275b03fcb48bd1d8f729c854c64c81a5b23ecf7cc(
    *,
    all_supported: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    include_global_resource_types: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    resource_types: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19b40216b605775542336c66e586acbda5bedfeb6e8b98925bc745b3572387f4(
    *,
    role_arn: builtins.str,
    name: typing.Optional[builtins.str] = None,
    recording_group: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnConfigurationRecorder.RecordingGroupProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6123f219e2006e6a835f6ff0683647eacebb11ad3246ef196c585a6e0b7221d7(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    conformance_pack_name: builtins.str,
    conformance_pack_input_parameters: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnConformancePack.ConformancePackInputParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    delivery_s3_bucket: typing.Optional[builtins.str] = None,
    delivery_s3_key_prefix: typing.Optional[builtins.str] = None,
    template_body: typing.Optional[builtins.str] = None,
    template_s3_uri: typing.Optional[builtins.str] = None,
    template_ssm_document_details: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__888b7dbfec248b6535edbfb026169c7701b67e1dbef47ac19de92c5c15323757(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3a33574e4d15eccc668be41d6ad70d886ad847ce4bc8bb387634dedddab853a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88170d0f3f5c995c8cdf88fbb01b283638631a5ea2e29181b3cca25f0789d55a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f7ac7e9540b1644014ffbeba63453ae38c2df19bdf2b3941330f6d9cabd32f7(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bcaed2e029220ea94c7a5e93f52cf47324fcc86342f75dd0efca5b6c13ad20c(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnConformancePack.ConformancePackInputParameterProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd383f517904444571092513732623fcb488cd27f51875edfa0d0d9103be8f8e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__265056adaa136193224fb5d95b0845856d6eb3c469b59d22f8451ce84a314153(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12dfd58bc90197bddd9eaa402abb3fc01d3d97e625d35c9e658564dc58190b02(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a19e9cf2f941cf7f00deea78e516e49cc26eab7b78191d5b950054eba7e4e08(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c4bcb70dd1952e4df06b1fbed9981a1eb9f543f8ad4ecdbaf0de8f0fd504f40(
    *,
    parameter_name: builtins.str,
    parameter_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c05dff23f0e3f4b96f068c119fa148dc0e3196da539a8ba7ba201e4438f6f1a(
    *,
    document_name: typing.Optional[builtins.str] = None,
    document_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c468477deaceeaedd7116aee03f37a7ce2e3183150dae370e43ffd361961133(
    *,
    conformance_pack_name: builtins.str,
    conformance_pack_input_parameters: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnConformancePack.ConformancePackInputParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    delivery_s3_bucket: typing.Optional[builtins.str] = None,
    delivery_s3_key_prefix: typing.Optional[builtins.str] = None,
    template_body: typing.Optional[builtins.str] = None,
    template_s3_uri: typing.Optional[builtins.str] = None,
    template_ssm_document_details: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8503fca266122c009084fee38132ec508c1ee988de9b01ba62411d1ae9dfe16d(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    s3_bucket_name: builtins.str,
    config_snapshot_delivery_properties: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDeliveryChannel.ConfigSnapshotDeliveryPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    s3_key_prefix: typing.Optional[builtins.str] = None,
    s3_kms_key_arn: typing.Optional[builtins.str] = None,
    sns_topic_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bc784826c9be5853c9d29de9a4c1161ea4e8e938a31566fa616bc92ccbed8fe(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a43f11103336b602266a7d05b2954a590113fe185f1b9af4d33f4f23ebabc02(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f490e7999afdc9d4cca032ea5e9c6ab33bc3e954c19f65ea41f23bd3b4155aeb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__689eb2e0300c97079b93eb02a656ac27b9541852f3429108ff47c0c67a535938(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnDeliveryChannel.ConfigSnapshotDeliveryPropertiesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ac8b13595a2aa4848daadda34a1e07813ca0a12e4252017cff58b25fe04df24(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0f7c0158b61d88c369b351f47c2ead21485eaa959b849e60fae2be2f6c90718(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc5e1cbfac10a9e52d0144d5ec59962b2ccb87bb83eb1880da5045abc6d56e4e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f33d70a9ba07df1effc7044f94ba092c7c42e6b5e3bead29d4b3e34b032230a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5efc3c228622d3e345810794f186238d4f1c0cd7a9c6ac447802f3557a5ec86a(
    *,
    delivery_frequency: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__392b246527bdbb83ef04a19cc7335fcd146d88170a6ac469c5966c386c829c3e(
    *,
    s3_bucket_name: builtins.str,
    config_snapshot_delivery_properties: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDeliveryChannel.ConfigSnapshotDeliveryPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    s3_key_prefix: typing.Optional[builtins.str] = None,
    s3_kms_key_arn: typing.Optional[builtins.str] = None,
    sns_topic_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b506ccb21501386876d39b6e43f781e00d82c1099fe12489a841614124a07b31(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    organization_config_rule_name: builtins.str,
    excluded_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
    organization_custom_code_rule_metadata: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnOrganizationConfigRule.OrganizationCustomCodeRuleMetadataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    organization_custom_rule_metadata: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnOrganizationConfigRule.OrganizationCustomRuleMetadataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    organization_managed_rule_metadata: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnOrganizationConfigRule.OrganizationManagedRuleMetadataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ba0b3f14f6bec4f7c9423983d8ee7e9a71bcc3daacc82bdc266d120665fa322(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e71116763d0720f599a45f1b95994a44efe53f2e2160d46a8ff64af4dafc4f58(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bfda5455a4e9f7bbd5923d65f203601c239bb91eaec45d7f2ef40afa6791f22(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64ab5433e3c3beda5112bb6c8c191059903bd15b035478578849f10a4864980f(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a74a2f44949dfd73daca0ecea240366a679d927adcec03d325ebd8c4dfad5636(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnOrganizationConfigRule.OrganizationCustomCodeRuleMetadataProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae9a661088177a704fbfd22fa22ee971adafd61fa5566245dead965a0aea23ba(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnOrganizationConfigRule.OrganizationCustomRuleMetadataProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7723ef40d27fd1460f2ad024f5f6cd4701fe13b73fb4ce0b89e0a520aa5a004(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnOrganizationConfigRule.OrganizationManagedRuleMetadataProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3494b5976e8b7148e429811e24136c4203b079234017740bed1ab618ac03fdc(
    *,
    code_text: builtins.str,
    runtime: builtins.str,
    debug_log_delivery_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
    description: typing.Optional[builtins.str] = None,
    input_parameters: typing.Optional[builtins.str] = None,
    maximum_execution_frequency: typing.Optional[builtins.str] = None,
    organization_config_rule_trigger_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    resource_id_scope: typing.Optional[builtins.str] = None,
    resource_types_scope: typing.Optional[typing.Sequence[builtins.str]] = None,
    tag_key_scope: typing.Optional[builtins.str] = None,
    tag_value_scope: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__308812e33051b64d99844c3dee8eb71c0acdd33b6559d539f7c0e6d850b09000(
    *,
    lambda_function_arn: builtins.str,
    organization_config_rule_trigger_types: typing.Sequence[builtins.str],
    description: typing.Optional[builtins.str] = None,
    input_parameters: typing.Optional[builtins.str] = None,
    maximum_execution_frequency: typing.Optional[builtins.str] = None,
    resource_id_scope: typing.Optional[builtins.str] = None,
    resource_types_scope: typing.Optional[typing.Sequence[builtins.str]] = None,
    tag_key_scope: typing.Optional[builtins.str] = None,
    tag_value_scope: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e79946dfc98a295f8d1ebb2e640427202599da5a200569f35457e9f2dfbbd0d1(
    *,
    rule_identifier: builtins.str,
    description: typing.Optional[builtins.str] = None,
    input_parameters: typing.Optional[builtins.str] = None,
    maximum_execution_frequency: typing.Optional[builtins.str] = None,
    resource_id_scope: typing.Optional[builtins.str] = None,
    resource_types_scope: typing.Optional[typing.Sequence[builtins.str]] = None,
    tag_key_scope: typing.Optional[builtins.str] = None,
    tag_value_scope: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__678289097a98bc5fd4dd4585f454bf87d496198b265fc462c28d48ee4ab656be(
    *,
    organization_config_rule_name: builtins.str,
    excluded_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
    organization_custom_code_rule_metadata: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnOrganizationConfigRule.OrganizationCustomCodeRuleMetadataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    organization_custom_rule_metadata: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnOrganizationConfigRule.OrganizationCustomRuleMetadataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    organization_managed_rule_metadata: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnOrganizationConfigRule.OrganizationManagedRuleMetadataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a20f40efb5e871fc8f570b7e47343feda5af1c82dcf16660322bbc1929af56fc(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    organization_conformance_pack_name: builtins.str,
    conformance_pack_input_parameters: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnOrganizationConformancePack.ConformancePackInputParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    delivery_s3_bucket: typing.Optional[builtins.str] = None,
    delivery_s3_key_prefix: typing.Optional[builtins.str] = None,
    excluded_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
    template_body: typing.Optional[builtins.str] = None,
    template_s3_uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec620aaebbb43409be1fb8c242500cdaf4d5fe84f9f9103149cc6d40f7e74f64(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65e0cc8d709757676f671cc3ab583ec52226ee513475123bb9ebd135e84c99e4(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49099c5f413b09e4f288f5f65b8a302539b394e49f6f66cf333a2bc366198925(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed61238dacbaf3ee81b4eb66e0c4e5463b440d527c0a49508f6bb727085a027b(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnOrganizationConformancePack.ConformancePackInputParameterProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ac2f9f7af6cb6f06d82e385c8a81e34b8bd33767c25438e84f1d5dc32dc87e8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa1237f2530d411b7d64104f3dc05f74340af362e962ba815c47e514777d0fd4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5554551cb66433e495447665360dc3688c586078b58d25f50576191704de2f7c(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f451cc2185147be3141c333f8fc24963f28818a46d1ed633a5fe992f403e84cd(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee958e76ffd91e1fdb984f5dae41c4dbfa49ca4650f7871ccba671617438c48a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__027e7f88a548e59cba26c51fbc136bbeeaee12184468f557b66f758a54333e37(
    *,
    parameter_name: builtins.str,
    parameter_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc1f3f9375583d7bc0bee4f0fe74824e5a8406e73b4f8cb426aaa96327cb6c43(
    *,
    organization_conformance_pack_name: builtins.str,
    conformance_pack_input_parameters: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnOrganizationConformancePack.ConformancePackInputParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    delivery_s3_bucket: typing.Optional[builtins.str] = None,
    delivery_s3_key_prefix: typing.Optional[builtins.str] = None,
    excluded_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
    template_body: typing.Optional[builtins.str] = None,
    template_s3_uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df0ccb3e35c03afdc1847c752a5de3041146631d00089e64af9de6b06eecf7ae(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    config_rule_name: builtins.str,
    target_id: builtins.str,
    target_type: builtins.str,
    automatic: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    execution_controls: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnRemediationConfiguration.ExecutionControlsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    maximum_automatic_attempts: typing.Optional[jsii.Number] = None,
    parameters: typing.Any = None,
    resource_type: typing.Optional[builtins.str] = None,
    retry_attempt_seconds: typing.Optional[jsii.Number] = None,
    target_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f81e93550632ccea0f3cc031871e34d6ae49c64e3e98341134b138fdefa15b3(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6aa049392202cee3880b6f72810e36cc2cac2dac921aa8e1f92e8ef63a900a6e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5af04272b48cd7e8b55ce538f839ef249541a1e185e4c8c29d4819f3748a74a5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__937ce6cdc0f4e244de040031b10c797897279212ffa86c44b65e43d6bba6a959(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9abd361ef93db21187e2406af69fcdeb8b2bcc704fd30a5f06e1fc7b43ebdd87(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__605c486b3be45b77078729b7b5c7af7aaa8c43c04b212dd24e5ba34746979538(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cb72646ea2b338cd5c4dcd2e4b371b93052a2b9ab41df141b7c916fdb848c48(
    value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69ad26cf90d5e215439c878b91392c31afbb645473739f1e510d084d4c07b138(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnRemediationConfiguration.ExecutionControlsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__871b74d77a62585e6372043a5354b60922edc42517633ef103f29420390c3e1b(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__285192de933460de2bc196dc50c36f9a5a49be4c6d36607bf9ee5b864e8c5169(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e3a13ceabde1da7aeeaa50c9d33011fdf74a9a11d6551b018ed1ee77d2ebbea(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c2a0ae324ebf289f497742e67467025ebef8c2d7a9bda0a954b769bacf06bae(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c9bb63bd99bf40767252006448a4291646686c562f79c794a67340a30b63052(
    *,
    ssm_controls: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnRemediationConfiguration.SsmControlsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__281701a7180e3f34d6f80b43e9fe65c8cf3b67e9223960717b8236bf0a03ab17(
    *,
    resource_value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnRemediationConfiguration.ResourceValueProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    static_value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnRemediationConfiguration.StaticValueProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e560ba9bb903158fb8112b331d35478a124e7f5d17144bd54f9d0b8ad7241112(
    *,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f1a4bf4f23bb3618339e4dffbd663e4253f8b970a4c30ccaaf4b6150a74ba7a(
    *,
    concurrent_execution_rate_percentage: typing.Optional[jsii.Number] = None,
    error_percentage: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d830098cbcf8a4aa85f63e59547d214cdd736b8c0740e7d4039642b2e1ad460(
    *,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e76eab5e10174eda1264da2000216cbde6cc9219074242d28450210ec1afeef4(
    *,
    config_rule_name: builtins.str,
    target_id: builtins.str,
    target_type: builtins.str,
    automatic: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    execution_controls: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnRemediationConfiguration.ExecutionControlsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    maximum_automatic_attempts: typing.Optional[jsii.Number] = None,
    parameters: typing.Any = None,
    resource_type: typing.Optional[builtins.str] = None,
    retry_attempt_seconds: typing.Optional[jsii.Number] = None,
    target_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bed95671ca6fdaace458fd531821ca6f617f7389c7c8d1780cf04bbcaef087e6(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    query_expression: builtins.str,
    query_name: builtins.str,
    query_description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c62229555e9a810b0a31ef9d721ad0f5497942327b87db8913eb5520aa7d819e(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77874ee40e947f394072b8d96c480283ee8ff5da8ba31ed7507fcdd5bfd69c54(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__749cfd407c6f57d5a88c1f73901f65cea002c9e0c7809dbaa028ae54c656865b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__726cb093f586df14a3cbaa4a8ead19eadb4662844d460e2954752bbf0fd0d924(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43a2a66de066398f31cfe3d0d336eb0b8a9e7957ca4291a357bce806d5d05610(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9154d511891bb2cc1103c89588295e98d82eeafe7a0c5efe8a2ceda52ae648e7(
    *,
    query_expression: builtins.str,
    query_name: builtins.str,
    query_description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e2ef8a1a04bb9f7791ace4e0f281292b7b42fd2f28453ec5572478286c23994(
    id: builtins.str,
    *,
    description: typing.Optional[builtins.str] = None,
    event_pattern: typing.Optional[typing.Union[_aws_cdk_aws_events_efcdfa54.EventPattern, typing.Dict[builtins.str, typing.Any]]] = None,
    rule_name: typing.Optional[builtins.str] = None,
    target: typing.Optional[_aws_cdk_aws_events_efcdfa54.IRuleTarget] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__576370f225a870a0cc4811380c4eabef037a05f2601206885795f104f94bd2fa(
    id: builtins.str,
    *,
    description: typing.Optional[builtins.str] = None,
    event_pattern: typing.Optional[typing.Union[_aws_cdk_aws_events_efcdfa54.EventPattern, typing.Dict[builtins.str, typing.Any]]] = None,
    rule_name: typing.Optional[builtins.str] = None,
    target: typing.Optional[_aws_cdk_aws_events_efcdfa54.IRuleTarget] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3de891820673c0218415a0ed7d1fc22835f389d276e993acc45ffc336aa06aac(
    id: builtins.str,
    *,
    description: typing.Optional[builtins.str] = None,
    event_pattern: typing.Optional[typing.Union[_aws_cdk_aws_events_efcdfa54.EventPattern, typing.Dict[builtins.str, typing.Any]]] = None,
    rule_name: typing.Optional[builtins.str] = None,
    target: typing.Optional[_aws_cdk_aws_events_efcdfa54.IRuleTarget] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__beb7233dcde14af055dfba051306a71fe86357693e267f2c540e81b863f1b54a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    identifier: builtins.str,
    config_rule_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
    rule_scope: typing.Optional[RuleScope] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e552b5124862de104ba5f6ed449ae86b76651764caa3d146db229aec6dfe1bb1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    config_rule_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43163b798774fd8cea5b4f2ca4f8d3e25000552eba3360cf963727ad3e600880(
    id: builtins.str,
    *,
    description: typing.Optional[builtins.str] = None,
    event_pattern: typing.Optional[typing.Union[_aws_cdk_aws_events_efcdfa54.EventPattern, typing.Dict[builtins.str, typing.Any]]] = None,
    rule_name: typing.Optional[builtins.str] = None,
    target: typing.Optional[_aws_cdk_aws_events_efcdfa54.IRuleTarget] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9e32d950364ffb20c68ea94f8efd7ddc6a7d61f9f2c2d8ba52f97ff600e8776(
    id: builtins.str,
    *,
    description: typing.Optional[builtins.str] = None,
    event_pattern: typing.Optional[typing.Union[_aws_cdk_aws_events_efcdfa54.EventPattern, typing.Dict[builtins.str, typing.Any]]] = None,
    rule_name: typing.Optional[builtins.str] = None,
    target: typing.Optional[_aws_cdk_aws_events_efcdfa54.IRuleTarget] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a73bc9b5ffc0291341ab1444151356eb4dbc32b663275a57ad775b20f4d2ef0(
    id: builtins.str,
    *,
    description: typing.Optional[builtins.str] = None,
    event_pattern: typing.Optional[typing.Union[_aws_cdk_aws_events_efcdfa54.EventPattern, typing.Dict[builtins.str, typing.Any]]] = None,
    rule_name: typing.Optional[builtins.str] = None,
    target: typing.Optional[_aws_cdk_aws_events_efcdfa54.IRuleTarget] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2f20c670458b15ce78f700dcb4d585b9d6b62be820e131913dde2b1a218f836(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9125ecd42861d285e4c2b6421f67f5e127f89ed0f26458982f5b0ebc9a8678e(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7065b8018e00f1c5ccacdbd0d149628eaf3073e0d8d54062d0bbba5729e385ec(
    value: typing.Optional[RuleScope],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db687db6a42e76118e2e021d6e57901854f5fb1e4ae269ae67f500d34a94f7d6(
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1eb734ae9fa747b5a43ec647ab46db612926a3fb07a8693cf4152d7f092a895a(
    *,
    config_rule_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
    rule_scope: typing.Optional[RuleScope] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38acf6b71126be6e2db421239e9babdd7462f42529ef7bc257f9fa610a56fc28(
    resource_type: ResourceType,
    resource_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2696024e628939ed8f328e89e342d436fb2013b56f930ea22a6fd5ca180ad1f1(
    resource_types: typing.Sequence[ResourceType],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57c51734c4ad182dafcb7de6caf0313b81055e8eed34201f631c6536e565cf82(
    key: builtins.str,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d49a760448522c6803de30b2dcd450ab9ed427fbc0536ea5a08d26cb910421a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    max_age: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
    config_rule_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
    rule_scope: typing.Optional[RuleScope] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__110381818ee33aac9a13be24c45e46644cf89f78d758658859b149b9f88fcd9d(
    *,
    config_rule_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
    rule_scope: typing.Optional[RuleScope] = None,
    max_age: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56104c799461baed787cd2925d18f3a5b835f10fcf3b90ca147268f5c4fd5dac(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    own_stack_only: typing.Optional[builtins.bool] = None,
    role: typing.Optional[_aws_cdk_aws_iam_940a1ce0.IRole] = None,
    config_rule_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
    rule_scope: typing.Optional[RuleScope] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ec5db3cf27da842ae7b04c0e7f299129e58954e79f505a26626d856e777953d(
    *,
    config_rule_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
    rule_scope: typing.Optional[RuleScope] = None,
    own_stack_only: typing.Optional[builtins.bool] = None,
    role: typing.Optional[_aws_cdk_aws_iam_940a1ce0.IRole] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__893553c8bd0d925f3ddc6db39e56ccd8dcdd58609837e4f9603f4eca6bc0710f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    topics: typing.Optional[typing.Sequence[_aws_cdk_aws_sns_889c7272.ITopic]] = None,
    config_rule_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
    rule_scope: typing.Optional[RuleScope] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bfc41ded906165c8d587958aa47c05624a8923f15a45d1cf04030b4ffa6bcb8(
    *,
    config_rule_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
    rule_scope: typing.Optional[RuleScope] = None,
    topics: typing.Optional[typing.Sequence[_aws_cdk_aws_sns_889c7272.ITopic]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fefbcb451627baeca7df97e860fdcd28d644e5917c08a5ba02e320e9ba8ab076(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    lambda_function: _aws_cdk_aws_lambda_5443dbc3.IFunction,
    configuration_changes: typing.Optional[builtins.bool] = None,
    periodic: typing.Optional[builtins.bool] = None,
    config_rule_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
    rule_scope: typing.Optional[RuleScope] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41f23c6abdf80a81de31e9143dd051ed924c5cac8b2b927c30e19c48881d1f0b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    config_rule_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33890b0042eb3061675d88c7fef5896069cfe0db429fb2e284fb2f64236b01ab(
    id: builtins.str,
    *,
    description: typing.Optional[builtins.str] = None,
    event_pattern: typing.Optional[typing.Union[_aws_cdk_aws_events_efcdfa54.EventPattern, typing.Dict[builtins.str, typing.Any]]] = None,
    rule_name: typing.Optional[builtins.str] = None,
    target: typing.Optional[_aws_cdk_aws_events_efcdfa54.IRuleTarget] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f78558801c57a29946ae502612db9239b081d1adcddf8c1a3f5309df5a94af2(
    id: builtins.str,
    *,
    description: typing.Optional[builtins.str] = None,
    event_pattern: typing.Optional[typing.Union[_aws_cdk_aws_events_efcdfa54.EventPattern, typing.Dict[builtins.str, typing.Any]]] = None,
    rule_name: typing.Optional[builtins.str] = None,
    target: typing.Optional[_aws_cdk_aws_events_efcdfa54.IRuleTarget] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07b7f6c542aa9138489d9d4f6762a34af78d103cdab0527b6bc7250351b7a76e(
    id: builtins.str,
    *,
    description: typing.Optional[builtins.str] = None,
    event_pattern: typing.Optional[typing.Union[_aws_cdk_aws_events_efcdfa54.EventPattern, typing.Dict[builtins.str, typing.Any]]] = None,
    rule_name: typing.Optional[builtins.str] = None,
    target: typing.Optional[_aws_cdk_aws_events_efcdfa54.IRuleTarget] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0dfb2b453bc3a9748fc10ac4aeaaab883bb1b8c50304ccbbb0fd74b6990ae0a(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69bfb50702eaeee8b588ec7a0bf8660ef1defed02d163bc9cb6e1dfd046eb8d3(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc8ec6e11f15eb8246f61611f9a28a4f439ce0eeeae26c891035ba7c4a01ae08(
    value: typing.Optional[RuleScope],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f87c4ec243baed6d93c1df2ef1de1d5cc9217be3c7aa768471056fcf43cc8c8(
    *,
    config_rule_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
    rule_scope: typing.Optional[RuleScope] = None,
    lambda_function: _aws_cdk_aws_lambda_5443dbc3.IFunction,
    configuration_changes: typing.Optional[builtins.bool] = None,
    periodic: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d6b3b9e342ceb3ab4ee19b736a9c2a4f43858829db3d59474bd2ac245edf9bf(
    *,
    config_rule_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
    rule_scope: typing.Optional[RuleScope] = None,
    identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

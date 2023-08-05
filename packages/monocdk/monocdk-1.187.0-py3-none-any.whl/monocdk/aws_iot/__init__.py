'''
# AWS IoT Construct Library

AWS IoT Core lets you connect billions of IoT devices and route trillions of
messages to AWS services without managing infrastructure.

## Installation

Install the module:

```console
$ npm i @aws-cdk/aws-iot
```

Import it into your code:

```python
import monocdk as iot
import monocdk as actions
```

## `TopicRule`

Create a topic rule that give your devices the ability to interact with AWS services.
You can create a topic rule with an action that invoke the Lambda action as following:

```python
func = lambda_.Function(self, "MyFunction",
    runtime=lambda_.Runtime.NODEJS_14_X,
    handler="index.handler",
    code=lambda_.Code.from_inline("""
            exports.handler = (event) => {
              console.log("It is test for lambda action of AWS IoT Rule.", event);
            };""")
)

iot.TopicRule(self, "TopicRule",
    topic_rule_name="MyTopicRule",  # optional
    description="invokes the lambda function",  # optional
    sql=iot.IotSql.from_string_as_ver20160323("SELECT topic(2) as device_id, timestamp() as timestamp FROM 'device/+/data'"),
    actions=[actions.LambdaFunctionAction(func)]
)
```

Or, you can add an action after constructing the `TopicRule` instance as following:

```python
# func: lambda.Function


topic_rule = iot.TopicRule(self, "TopicRule",
    sql=iot.IotSql.from_string_as_ver20160323("SELECT topic(2) as device_id, timestamp() as timestamp FROM 'device/+/data'")
)
topic_rule.add_action(actions.LambdaFunctionAction(func))
```

You can also supply `errorAction` as following,
and the IoT Rule will trigger it if a rule's action is unable to perform:

```python
import monocdk as logs


log_group = logs.LogGroup(self, "MyLogGroup")

iot.TopicRule(self, "TopicRule",
    sql=iot.IotSql.from_string_as_ver20160323("SELECT topic(2) as device_id, timestamp() as timestamp FROM 'device/+/data'"),
    error_action=actions.CloudWatchLogsAction(log_group)
)
```

If you wanna make the topic rule disable, add property `enabled: false` as following:

```python
iot.TopicRule(self, "TopicRule",
    sql=iot.IotSql.from_string_as_ver20160323("SELECT topic(2) as device_id, timestamp() as timestamp FROM 'device/+/data'"),
    enabled=False
)
```

See also [@aws-cdk/aws-iot-actions](https://docs.aws.amazon.com/cdk/api/latest/docs/aws-iot-actions-readme.html) for other actions.
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

from .._jsii import *

import constructs as _constructs_77d1e7e8
from .. import (
    CfnResource as _CfnResource_e0a482dc,
    CfnTag as _CfnTag_95fbdc29,
    Construct as _Construct_e78e779f,
    IInspectable as _IInspectable_82c04a63,
    IResolvable as _IResolvable_a771d0ef,
    IResource as _IResource_8c1dbbbd,
    Resource as _Resource_abff4495,
    TagManager as _TagManager_0b7ab120,
    TreeInspector as _TreeInspector_1cd1894e,
)


@jsii.data_type(
    jsii_type="monocdk.aws_iot.ActionConfig",
    jsii_struct_bases=[],
    name_mapping={"configuration": "configuration"},
)
class ActionConfig:
    def __init__(
        self,
        *,
        configuration: typing.Union["CfnTopicRule.ActionProperty", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''(experimental) Properties for an topic rule action.

        :param configuration: (experimental) The configuration for this action.

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_iot as iot
            
            action_config = iot.ActionConfig(
                configuration=iot.CfnTopicRule.ActionProperty(
                    cloudwatch_alarm=iot.CfnTopicRule.CloudwatchAlarmActionProperty(
                        alarm_name="alarmName",
                        role_arn="roleArn",
                        state_reason="stateReason",
                        state_value="stateValue"
                    ),
                    cloudwatch_logs=iot.CfnTopicRule.CloudwatchLogsActionProperty(
                        log_group_name="logGroupName",
                        role_arn="roleArn"
                    ),
                    cloudwatch_metric=iot.CfnTopicRule.CloudwatchMetricActionProperty(
                        metric_name="metricName",
                        metric_namespace="metricNamespace",
                        metric_unit="metricUnit",
                        metric_value="metricValue",
                        role_arn="roleArn",
            
                        # the properties below are optional
                        metric_timestamp="metricTimestamp"
                    ),
                    dynamo_db=iot.CfnTopicRule.DynamoDBActionProperty(
                        hash_key_field="hashKeyField",
                        hash_key_value="hashKeyValue",
                        role_arn="roleArn",
                        table_name="tableName",
            
                        # the properties below are optional
                        hash_key_type="hashKeyType",
                        payload_field="payloadField",
                        range_key_field="rangeKeyField",
                        range_key_type="rangeKeyType",
                        range_key_value="rangeKeyValue"
                    ),
                    dynamo_dBv2=iot.CfnTopicRule.DynamoDBv2ActionProperty(
                        put_item=iot.CfnTopicRule.PutItemInputProperty(
                            table_name="tableName"
                        ),
                        role_arn="roleArn"
                    ),
                    elasticsearch=iot.CfnTopicRule.ElasticsearchActionProperty(
                        endpoint="endpoint",
                        id="id",
                        index="index",
                        role_arn="roleArn",
                        type="type"
                    ),
                    firehose=iot.CfnTopicRule.FirehoseActionProperty(
                        delivery_stream_name="deliveryStreamName",
                        role_arn="roleArn",
            
                        # the properties below are optional
                        batch_mode=False,
                        separator="separator"
                    ),
                    http=iot.CfnTopicRule.HttpActionProperty(
                        url="url",
            
                        # the properties below are optional
                        auth=iot.CfnTopicRule.HttpAuthorizationProperty(
                            sigv4=iot.CfnTopicRule.SigV4AuthorizationProperty(
                                role_arn="roleArn",
                                service_name="serviceName",
                                signing_region="signingRegion"
                            )
                        ),
                        confirmation_url="confirmationUrl",
                        headers=[iot.CfnTopicRule.HttpActionHeaderProperty(
                            key="key",
                            value="value"
                        )]
                    ),
                    iot_analytics=iot.CfnTopicRule.IotAnalyticsActionProperty(
                        channel_name="channelName",
                        role_arn="roleArn",
            
                        # the properties below are optional
                        batch_mode=False
                    ),
                    iot_events=iot.CfnTopicRule.IotEventsActionProperty(
                        input_name="inputName",
                        role_arn="roleArn",
            
                        # the properties below are optional
                        batch_mode=False,
                        message_id="messageId"
                    ),
                    iot_site_wise=iot.CfnTopicRule.IotSiteWiseActionProperty(
                        put_asset_property_value_entries=[iot.CfnTopicRule.PutAssetPropertyValueEntryProperty(
                            property_values=[iot.CfnTopicRule.AssetPropertyValueProperty(
                                timestamp=iot.CfnTopicRule.AssetPropertyTimestampProperty(
                                    time_in_seconds="timeInSeconds",
            
                                    # the properties below are optional
                                    offset_in_nanos="offsetInNanos"
                                ),
                                value=iot.CfnTopicRule.AssetPropertyVariantProperty(
                                    boolean_value="booleanValue",
                                    double_value="doubleValue",
                                    integer_value="integerValue",
                                    string_value="stringValue"
                                ),
            
                                # the properties below are optional
                                quality="quality"
                            )],
            
                            # the properties below are optional
                            asset_id="assetId",
                            entry_id="entryId",
                            property_alias="propertyAlias",
                            property_id="propertyId"
                        )],
                        role_arn="roleArn"
                    ),
                    kafka=iot.CfnTopicRule.KafkaActionProperty(
                        client_properties={
                            "client_properties_key": "clientProperties"
                        },
                        destination_arn="destinationArn",
                        topic="topic",
            
                        # the properties below are optional
                        key="key",
                        partition="partition"
                    ),
                    kinesis=iot.CfnTopicRule.KinesisActionProperty(
                        role_arn="roleArn",
                        stream_name="streamName",
            
                        # the properties below are optional
                        partition_key="partitionKey"
                    ),
                    lambda_=iot.CfnTopicRule.LambdaActionProperty(
                        function_arn="functionArn"
                    ),
                    location=iot.CfnTopicRule.LocationActionProperty(
                        device_id="deviceId",
                        latitude="latitude",
                        longitude="longitude",
                        role_arn="roleArn",
                        tracker_name="trackerName",
            
                        # the properties below are optional
                        timestamp=Date()
                    ),
                    open_search=iot.CfnTopicRule.OpenSearchActionProperty(
                        endpoint="endpoint",
                        id="id",
                        index="index",
                        role_arn="roleArn",
                        type="type"
                    ),
                    republish=iot.CfnTopicRule.RepublishActionProperty(
                        role_arn="roleArn",
                        topic="topic",
            
                        # the properties below are optional
                        headers=iot.CfnTopicRule.RepublishActionHeadersProperty(
                            content_type="contentType",
                            correlation_data="correlationData",
                            message_expiry="messageExpiry",
                            payload_format_indicator="payloadFormatIndicator",
                            response_topic="responseTopic",
                            user_properties=[iot.CfnTopicRule.UserPropertyProperty(
                                key="key",
                                value="value"
                            )]
                        ),
                        qos=123
                    ),
                    s3=iot.CfnTopicRule.S3ActionProperty(
                        bucket_name="bucketName",
                        key="key",
                        role_arn="roleArn",
            
                        # the properties below are optional
                        canned_acl="cannedAcl"
                    ),
                    sns=iot.CfnTopicRule.SnsActionProperty(
                        role_arn="roleArn",
                        target_arn="targetArn",
            
                        # the properties below are optional
                        message_format="messageFormat"
                    ),
                    sqs=iot.CfnTopicRule.SqsActionProperty(
                        queue_url="queueUrl",
                        role_arn="roleArn",
            
                        # the properties below are optional
                        use_base64=False
                    ),
                    step_functions=iot.CfnTopicRule.StepFunctionsActionProperty(
                        role_arn="roleArn",
                        state_machine_name="stateMachineName",
            
                        # the properties below are optional
                        execution_name_prefix="executionNamePrefix"
                    ),
                    timestream=iot.CfnTopicRule.TimestreamActionProperty(
                        database_name="databaseName",
                        dimensions=[iot.CfnTopicRule.TimestreamDimensionProperty(
                            name="name",
                            value="value"
                        )],
                        role_arn="roleArn",
                        table_name="tableName",
            
                        # the properties below are optional
                        timestamp=iot.CfnTopicRule.TimestreamTimestampProperty(
                            unit="unit",
                            value="value"
                        )
                    )
                )
            )
        '''
        if isinstance(configuration, dict):
            configuration = CfnTopicRule.ActionProperty(**configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__917322bf96f684171fc47212b367dde8956db396e5a79655c238a3ab2480da71)
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "configuration": configuration,
        }

    @builtins.property
    def configuration(self) -> "CfnTopicRule.ActionProperty":
        '''(experimental) The configuration for this action.

        :stability: experimental
        '''
        result = self._values.get("configuration")
        assert result is not None, "Required property 'configuration' is missing"
        return typing.cast("CfnTopicRule.ActionProperty", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ActionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnAccountAuditConfiguration(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iot.CfnAccountAuditConfiguration",
):
    '''A CloudFormation ``AWS::IoT::AccountAuditConfiguration``.

    Use the ``AWS::IoT::AccountAuditConfiguration`` resource to configure or reconfigure the Device Defender audit settings for your account. Settings include how audit notifications are sent and which audit checks are enabled or disabled. For API reference, see `UpdateAccountAuditConfiguration <https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateAccountAuditConfiguration.html>`_ and for detailed information on all available audit checks, see `Audit checks <https://docs.aws.amazon.com/iot/latest/developerguide/device-defender-audit-checks.html>`_ .

    :cloudformationResource: AWS::IoT::AccountAuditConfiguration
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-accountauditconfiguration.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_iot as iot
        
        cfn_account_audit_configuration = iot.CfnAccountAuditConfiguration(self, "MyCfnAccountAuditConfiguration",
            account_id="accountId",
            audit_check_configurations=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationsProperty(
                authenticated_cognito_role_overly_permissive_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                    enabled=False
                ),
                ca_certificate_expiring_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                    enabled=False
                ),
                ca_certificate_key_quality_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                    enabled=False
                ),
                conflicting_client_ids_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                    enabled=False
                ),
                device_certificate_expiring_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                    enabled=False
                ),
                device_certificate_key_quality_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                    enabled=False
                ),
                device_certificate_shared_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                    enabled=False
                ),
                intermediate_ca_revoked_for_active_device_certificates_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                    enabled=False
                ),
                iot_policy_overly_permissive_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                    enabled=False
                ),
                io_tPolicy_potential_mis_configuration_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                    enabled=False
                ),
                iot_role_alias_allows_access_to_unused_services_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                    enabled=False
                ),
                iot_role_alias_overly_permissive_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                    enabled=False
                ),
                logging_disabled_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                    enabled=False
                ),
                revoked_ca_certificate_still_active_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                    enabled=False
                ),
                revoked_device_certificate_still_active_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                    enabled=False
                ),
                unauthenticated_cognito_role_overly_permissive_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                    enabled=False
                )
            ),
            role_arn="roleArn",
        
            # the properties below are optional
            audit_notification_target_configurations=iot.CfnAccountAuditConfiguration.AuditNotificationTargetConfigurationsProperty(
                sns=iot.CfnAccountAuditConfiguration.AuditNotificationTargetProperty(
                    enabled=False,
                    role_arn="roleArn",
                    target_arn="targetArn"
                )
            )
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        account_id: builtins.str,
        audit_check_configurations: typing.Union[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationsProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
        role_arn: builtins.str,
        audit_notification_target_configurations: typing.Optional[typing.Union[typing.Union["CfnAccountAuditConfiguration.AuditNotificationTargetConfigurationsProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    ) -> None:
        '''Create a new ``AWS::IoT::AccountAuditConfiguration``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param account_id: The ID of the account. You can use the expression ``!Sub "${AWS::AccountId}"`` to use your account ID.
        :param audit_check_configurations: Specifies which audit checks are enabled and disabled for this account. Some data collection might start immediately when certain checks are enabled. When a check is disabled, any data collected so far in relation to the check is deleted. To disable a check, set the value of the ``Enabled:`` key to ``false`` . If an enabled check is removed from the template, it will also be disabled. You can't disable a check if it's used by any scheduled audit. You must delete the check from the scheduled audit or delete the scheduled audit itself to disable the check. For more information on avialbe auidt checks see `AWS::IoT::AccountAuditConfiguration AuditCheckConfigurations <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html>`_
        :param role_arn: The Amazon Resource Name (ARN) of the role that grants permission to AWS IoT to access information about your devices, policies, certificates, and other items as required when performing an audit.
        :param audit_notification_target_configurations: Information about the targets to which audit notifications are sent.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7735d9e6d93dc1a72b84f19f68fb84c0e33d0dfe59ed396a1399db9ce831a9dd)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAccountAuditConfigurationProps(
            account_id=account_id,
            audit_check_configurations=audit_check_configurations,
            role_arn=role_arn,
            audit_notification_target_configurations=audit_notification_target_configurations,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b8b50dbd80fd95746de6c96a6dfbfae5bee9ad27502bc87c56e1b56c7c1de9c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b7d9e06c0b372fecc936f2c7b04b4599158dd256118c6e766cecfb09a0d56c7a)
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
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        '''The ID of the account.

        You can use the expression ``!Sub "${AWS::AccountId}"`` to use your account ID.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-accountauditconfiguration.html#cfn-iot-accountauditconfiguration-accountid
        '''
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1df43efb3aa9a16d25a96f2305c8cc02e51f52f86b6d954e524590fa054b4f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="auditCheckConfigurations")
    def audit_check_configurations(
        self,
    ) -> typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationsProperty", _IResolvable_a771d0ef]:
        '''Specifies which audit checks are enabled and disabled for this account.

        Some data collection might start immediately when certain checks are enabled. When a check is disabled, any data collected so far in relation to the check is deleted. To disable a check, set the value of the ``Enabled:`` key to ``false`` .

        If an enabled check is removed from the template, it will also be disabled.

        You can't disable a check if it's used by any scheduled audit. You must delete the check from the scheduled audit or delete the scheduled audit itself to disable the check.

        For more information on avialbe auidt checks see `AWS::IoT::AccountAuditConfiguration AuditCheckConfigurations <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html>`_

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-accountauditconfiguration.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations
        '''
        return typing.cast(typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationsProperty", _IResolvable_a771d0ef], jsii.get(self, "auditCheckConfigurations"))

    @audit_check_configurations.setter
    def audit_check_configurations(
        self,
        value: typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationsProperty", _IResolvable_a771d0ef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78dc0e43a4e743f05c4e07629dc49380fa5ea79f96e8250fef5f8b01a8821da1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "auditCheckConfigurations", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the role that grants permission to AWS IoT to access information about your devices, policies, certificates, and other items as required when performing an audit.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-accountauditconfiguration.html#cfn-iot-accountauditconfiguration-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e5018125dbd21a9e8fda914b0cf8f7bb617e37b81d4f77092635de2ed725ea9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="auditNotificationTargetConfigurations")
    def audit_notification_target_configurations(
        self,
    ) -> typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditNotificationTargetConfigurationsProperty", _IResolvable_a771d0ef]]:
        '''Information about the targets to which audit notifications are sent.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-accountauditconfiguration.html#cfn-iot-accountauditconfiguration-auditnotificationtargetconfigurations
        '''
        return typing.cast(typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditNotificationTargetConfigurationsProperty", _IResolvable_a771d0ef]], jsii.get(self, "auditNotificationTargetConfigurations"))

    @audit_notification_target_configurations.setter
    def audit_notification_target_configurations(
        self,
        value: typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditNotificationTargetConfigurationsProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1099f85e532c40d2797fc0d72f60d910f5fb880c11ac1d145aa00cbe26ca3fb7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "auditNotificationTargetConfigurations", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled"},
    )
    class AuditCheckConfigurationProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''Which audit checks are enabled and disabled for this account.

            :param enabled: True if this audit check is enabled for this account.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                audit_check_configuration_property = iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                    enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7cdd76f4f5d6394b1c753a44de5552be456bfb670513bbbad85c6a7f46623ca3)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''True if this audit check is enabled for this account.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfiguration.html#cfn-iot-accountauditconfiguration-auditcheckconfiguration-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuditCheckConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnAccountAuditConfiguration.AuditCheckConfigurationsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "authenticated_cognito_role_overly_permissive_check": "authenticatedCognitoRoleOverlyPermissiveCheck",
            "ca_certificate_expiring_check": "caCertificateExpiringCheck",
            "ca_certificate_key_quality_check": "caCertificateKeyQualityCheck",
            "conflicting_client_ids_check": "conflictingClientIdsCheck",
            "device_certificate_expiring_check": "deviceCertificateExpiringCheck",
            "device_certificate_key_quality_check": "deviceCertificateKeyQualityCheck",
            "device_certificate_shared_check": "deviceCertificateSharedCheck",
            "intermediate_ca_revoked_for_active_device_certificates_check": "intermediateCaRevokedForActiveDeviceCertificatesCheck",
            "iot_policy_overly_permissive_check": "iotPolicyOverlyPermissiveCheck",
            "io_t_policy_potential_mis_configuration_check": "ioTPolicyPotentialMisConfigurationCheck",
            "iot_role_alias_allows_access_to_unused_services_check": "iotRoleAliasAllowsAccessToUnusedServicesCheck",
            "iot_role_alias_overly_permissive_check": "iotRoleAliasOverlyPermissiveCheck",
            "logging_disabled_check": "loggingDisabledCheck",
            "revoked_ca_certificate_still_active_check": "revokedCaCertificateStillActiveCheck",
            "revoked_device_certificate_still_active_check": "revokedDeviceCertificateStillActiveCheck",
            "unauthenticated_cognito_role_overly_permissive_check": "unauthenticatedCognitoRoleOverlyPermissiveCheck",
        },
    )
    class AuditCheckConfigurationsProperty:
        def __init__(
            self,
            *,
            authenticated_cognito_role_overly_permissive_check: typing.Optional[typing.Union[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            ca_certificate_expiring_check: typing.Optional[typing.Union[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            ca_certificate_key_quality_check: typing.Optional[typing.Union[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            conflicting_client_ids_check: typing.Optional[typing.Union[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            device_certificate_expiring_check: typing.Optional[typing.Union[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            device_certificate_key_quality_check: typing.Optional[typing.Union[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            device_certificate_shared_check: typing.Optional[typing.Union[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            intermediate_ca_revoked_for_active_device_certificates_check: typing.Optional[typing.Union[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            iot_policy_overly_permissive_check: typing.Optional[typing.Union[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            io_t_policy_potential_mis_configuration_check: typing.Optional[typing.Union[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            iot_role_alias_allows_access_to_unused_services_check: typing.Optional[typing.Union[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            iot_role_alias_overly_permissive_check: typing.Optional[typing.Union[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            logging_disabled_check: typing.Optional[typing.Union[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            revoked_ca_certificate_still_active_check: typing.Optional[typing.Union[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            revoked_device_certificate_still_active_check: typing.Optional[typing.Union[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            unauthenticated_cognito_role_overly_permissive_check: typing.Optional[typing.Union[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''The types of audit checks that can be performed.

            :param authenticated_cognito_role_overly_permissive_check: Checks the permissiveness of an authenticated Amazon Cognito identity pool role. For this check, AWS IoT Device Defender audits all Amazon Cognito identity pools that have been used to connect to the AWS IoT message broker during the 31 days before the audit is performed.
            :param ca_certificate_expiring_check: Checks if a CA certificate is expiring. This check applies to CA certificates expiring within 30 days or that have expired.
            :param ca_certificate_key_quality_check: Checks the quality of the CA certificate key. The quality checks if the key is in a valid format, not expired, and if the key meets a minimum required size. This check applies to CA certificates that are ``ACTIVE`` or ``PENDING_TRANSFER`` .
            :param conflicting_client_ids_check: Checks if multiple devices connect using the same client ID.
            :param device_certificate_expiring_check: Checks if a device certificate is expiring. This check applies to device certificates expiring within 30 days or that have expired.
            :param device_certificate_key_quality_check: Checks the quality of the device certificate key. The quality checks if the key is in a valid format, not expired, signed by a registered certificate authority, and if the key meets a minimum required size.
            :param device_certificate_shared_check: Checks if multiple concurrent connections use the same X.509 certificate to authenticate with AWS IoT .
            :param intermediate_ca_revoked_for_active_device_certificates_check: ``CfnAccountAuditConfiguration.AuditCheckConfigurationsProperty.IntermediateCaRevokedForActiveDeviceCertificatesCheck``.
            :param iot_policy_overly_permissive_check: Checks the permissiveness of a policy attached to an authenticated Amazon Cognito identity pool role.
            :param io_t_policy_potential_mis_configuration_check: ``CfnAccountAuditConfiguration.AuditCheckConfigurationsProperty.IoTPolicyPotentialMisConfigurationCheck``.
            :param iot_role_alias_allows_access_to_unused_services_check: Checks if a role alias has access to services that haven't been used for the AWS IoT device in the last year.
            :param iot_role_alias_overly_permissive_check: Checks if the temporary credentials provided by AWS IoT role aliases are overly permissive.
            :param logging_disabled_check: Checks if AWS IoT logs are disabled.
            :param revoked_ca_certificate_still_active_check: Checks if a revoked CA certificate is still active.
            :param revoked_device_certificate_still_active_check: Checks if a revoked device certificate is still active.
            :param unauthenticated_cognito_role_overly_permissive_check: Checks if policy attached to an unauthenticated Amazon Cognito identity pool role is too permissive.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                audit_check_configurations_property = iot.CfnAccountAuditConfiguration.AuditCheckConfigurationsProperty(
                    authenticated_cognito_role_overly_permissive_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    ca_certificate_expiring_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    ca_certificate_key_quality_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    conflicting_client_ids_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    device_certificate_expiring_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    device_certificate_key_quality_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    device_certificate_shared_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    intermediate_ca_revoked_for_active_device_certificates_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    iot_policy_overly_permissive_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    io_tPolicy_potential_mis_configuration_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    iot_role_alias_allows_access_to_unused_services_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    iot_role_alias_overly_permissive_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    logging_disabled_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    revoked_ca_certificate_still_active_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    revoked_device_certificate_still_active_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    unauthenticated_cognito_role_overly_permissive_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__51c2e37ebbdc3f43373070b2ecda9ebaa07b63f6d481c66f9b00b0d6be5c4b47)
                check_type(argname="argument authenticated_cognito_role_overly_permissive_check", value=authenticated_cognito_role_overly_permissive_check, expected_type=type_hints["authenticated_cognito_role_overly_permissive_check"])
                check_type(argname="argument ca_certificate_expiring_check", value=ca_certificate_expiring_check, expected_type=type_hints["ca_certificate_expiring_check"])
                check_type(argname="argument ca_certificate_key_quality_check", value=ca_certificate_key_quality_check, expected_type=type_hints["ca_certificate_key_quality_check"])
                check_type(argname="argument conflicting_client_ids_check", value=conflicting_client_ids_check, expected_type=type_hints["conflicting_client_ids_check"])
                check_type(argname="argument device_certificate_expiring_check", value=device_certificate_expiring_check, expected_type=type_hints["device_certificate_expiring_check"])
                check_type(argname="argument device_certificate_key_quality_check", value=device_certificate_key_quality_check, expected_type=type_hints["device_certificate_key_quality_check"])
                check_type(argname="argument device_certificate_shared_check", value=device_certificate_shared_check, expected_type=type_hints["device_certificate_shared_check"])
                check_type(argname="argument intermediate_ca_revoked_for_active_device_certificates_check", value=intermediate_ca_revoked_for_active_device_certificates_check, expected_type=type_hints["intermediate_ca_revoked_for_active_device_certificates_check"])
                check_type(argname="argument iot_policy_overly_permissive_check", value=iot_policy_overly_permissive_check, expected_type=type_hints["iot_policy_overly_permissive_check"])
                check_type(argname="argument io_t_policy_potential_mis_configuration_check", value=io_t_policy_potential_mis_configuration_check, expected_type=type_hints["io_t_policy_potential_mis_configuration_check"])
                check_type(argname="argument iot_role_alias_allows_access_to_unused_services_check", value=iot_role_alias_allows_access_to_unused_services_check, expected_type=type_hints["iot_role_alias_allows_access_to_unused_services_check"])
                check_type(argname="argument iot_role_alias_overly_permissive_check", value=iot_role_alias_overly_permissive_check, expected_type=type_hints["iot_role_alias_overly_permissive_check"])
                check_type(argname="argument logging_disabled_check", value=logging_disabled_check, expected_type=type_hints["logging_disabled_check"])
                check_type(argname="argument revoked_ca_certificate_still_active_check", value=revoked_ca_certificate_still_active_check, expected_type=type_hints["revoked_ca_certificate_still_active_check"])
                check_type(argname="argument revoked_device_certificate_still_active_check", value=revoked_device_certificate_still_active_check, expected_type=type_hints["revoked_device_certificate_still_active_check"])
                check_type(argname="argument unauthenticated_cognito_role_overly_permissive_check", value=unauthenticated_cognito_role_overly_permissive_check, expected_type=type_hints["unauthenticated_cognito_role_overly_permissive_check"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if authenticated_cognito_role_overly_permissive_check is not None:
                self._values["authenticated_cognito_role_overly_permissive_check"] = authenticated_cognito_role_overly_permissive_check
            if ca_certificate_expiring_check is not None:
                self._values["ca_certificate_expiring_check"] = ca_certificate_expiring_check
            if ca_certificate_key_quality_check is not None:
                self._values["ca_certificate_key_quality_check"] = ca_certificate_key_quality_check
            if conflicting_client_ids_check is not None:
                self._values["conflicting_client_ids_check"] = conflicting_client_ids_check
            if device_certificate_expiring_check is not None:
                self._values["device_certificate_expiring_check"] = device_certificate_expiring_check
            if device_certificate_key_quality_check is not None:
                self._values["device_certificate_key_quality_check"] = device_certificate_key_quality_check
            if device_certificate_shared_check is not None:
                self._values["device_certificate_shared_check"] = device_certificate_shared_check
            if intermediate_ca_revoked_for_active_device_certificates_check is not None:
                self._values["intermediate_ca_revoked_for_active_device_certificates_check"] = intermediate_ca_revoked_for_active_device_certificates_check
            if iot_policy_overly_permissive_check is not None:
                self._values["iot_policy_overly_permissive_check"] = iot_policy_overly_permissive_check
            if io_t_policy_potential_mis_configuration_check is not None:
                self._values["io_t_policy_potential_mis_configuration_check"] = io_t_policy_potential_mis_configuration_check
            if iot_role_alias_allows_access_to_unused_services_check is not None:
                self._values["iot_role_alias_allows_access_to_unused_services_check"] = iot_role_alias_allows_access_to_unused_services_check
            if iot_role_alias_overly_permissive_check is not None:
                self._values["iot_role_alias_overly_permissive_check"] = iot_role_alias_overly_permissive_check
            if logging_disabled_check is not None:
                self._values["logging_disabled_check"] = logging_disabled_check
            if revoked_ca_certificate_still_active_check is not None:
                self._values["revoked_ca_certificate_still_active_check"] = revoked_ca_certificate_still_active_check
            if revoked_device_certificate_still_active_check is not None:
                self._values["revoked_device_certificate_still_active_check"] = revoked_device_certificate_still_active_check
            if unauthenticated_cognito_role_overly_permissive_check is not None:
                self._values["unauthenticated_cognito_role_overly_permissive_check"] = unauthenticated_cognito_role_overly_permissive_check

        @builtins.property
        def authenticated_cognito_role_overly_permissive_check(
            self,
        ) -> typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_a771d0ef]]:
            '''Checks the permissiveness of an authenticated Amazon Cognito identity pool role.

            For this check, AWS IoT Device Defender audits all Amazon Cognito identity pools that have been used to connect to the AWS IoT message broker during the 31 days before the audit is performed.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-authenticatedcognitoroleoverlypermissivecheck
            '''
            result = self._values.get("authenticated_cognito_role_overly_permissive_check")
            return typing.cast(typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def ca_certificate_expiring_check(
            self,
        ) -> typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_a771d0ef]]:
            '''Checks if a CA certificate is expiring.

            This check applies to CA certificates expiring within 30 days or that have expired.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-cacertificateexpiringcheck
            '''
            result = self._values.get("ca_certificate_expiring_check")
            return typing.cast(typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def ca_certificate_key_quality_check(
            self,
        ) -> typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_a771d0ef]]:
            '''Checks the quality of the CA certificate key.

            The quality checks if the key is in a valid format, not expired, and if the key meets a minimum required size. This check applies to CA certificates that are ``ACTIVE`` or ``PENDING_TRANSFER`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-cacertificatekeyqualitycheck
            '''
            result = self._values.get("ca_certificate_key_quality_check")
            return typing.cast(typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def conflicting_client_ids_check(
            self,
        ) -> typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_a771d0ef]]:
            '''Checks if multiple devices connect using the same client ID.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-conflictingclientidscheck
            '''
            result = self._values.get("conflicting_client_ids_check")
            return typing.cast(typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def device_certificate_expiring_check(
            self,
        ) -> typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_a771d0ef]]:
            '''Checks if a device certificate is expiring.

            This check applies to device certificates expiring within 30 days or that have expired.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-devicecertificateexpiringcheck
            '''
            result = self._values.get("device_certificate_expiring_check")
            return typing.cast(typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def device_certificate_key_quality_check(
            self,
        ) -> typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_a771d0ef]]:
            '''Checks the quality of the device certificate key.

            The quality checks if the key is in a valid format, not expired, signed by a registered certificate authority, and if the key meets a minimum required size.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-devicecertificatekeyqualitycheck
            '''
            result = self._values.get("device_certificate_key_quality_check")
            return typing.cast(typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def device_certificate_shared_check(
            self,
        ) -> typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_a771d0ef]]:
            '''Checks if multiple concurrent connections use the same X.509 certificate to authenticate with AWS IoT .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-devicecertificatesharedcheck
            '''
            result = self._values.get("device_certificate_shared_check")
            return typing.cast(typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def intermediate_ca_revoked_for_active_device_certificates_check(
            self,
        ) -> typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_a771d0ef]]:
            '''``CfnAccountAuditConfiguration.AuditCheckConfigurationsProperty.IntermediateCaRevokedForActiveDeviceCertificatesCheck``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-intermediatecarevokedforactivedevicecertificatescheck
            '''
            result = self._values.get("intermediate_ca_revoked_for_active_device_certificates_check")
            return typing.cast(typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def iot_policy_overly_permissive_check(
            self,
        ) -> typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_a771d0ef]]:
            '''Checks the permissiveness of a policy attached to an authenticated Amazon Cognito identity pool role.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-iotpolicyoverlypermissivecheck
            '''
            result = self._values.get("iot_policy_overly_permissive_check")
            return typing.cast(typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def io_t_policy_potential_mis_configuration_check(
            self,
        ) -> typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_a771d0ef]]:
            '''``CfnAccountAuditConfiguration.AuditCheckConfigurationsProperty.IoTPolicyPotentialMisConfigurationCheck``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-iotpolicypotentialmisconfigurationcheck
            '''
            result = self._values.get("io_t_policy_potential_mis_configuration_check")
            return typing.cast(typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def iot_role_alias_allows_access_to_unused_services_check(
            self,
        ) -> typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_a771d0ef]]:
            '''Checks if a role alias has access to services that haven't been used for the AWS IoT device in the last year.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-iotrolealiasallowsaccesstounusedservicescheck
            '''
            result = self._values.get("iot_role_alias_allows_access_to_unused_services_check")
            return typing.cast(typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def iot_role_alias_overly_permissive_check(
            self,
        ) -> typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_a771d0ef]]:
            '''Checks if the temporary credentials provided by AWS IoT role aliases are overly permissive.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-iotrolealiasoverlypermissivecheck
            '''
            result = self._values.get("iot_role_alias_overly_permissive_check")
            return typing.cast(typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def logging_disabled_check(
            self,
        ) -> typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_a771d0ef]]:
            '''Checks if AWS IoT logs are disabled.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-loggingdisabledcheck
            '''
            result = self._values.get("logging_disabled_check")
            return typing.cast(typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def revoked_ca_certificate_still_active_check(
            self,
        ) -> typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_a771d0ef]]:
            '''Checks if a revoked CA certificate is still active.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-revokedcacertificatestillactivecheck
            '''
            result = self._values.get("revoked_ca_certificate_still_active_check")
            return typing.cast(typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def revoked_device_certificate_still_active_check(
            self,
        ) -> typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_a771d0ef]]:
            '''Checks if a revoked device certificate is still active.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-revokeddevicecertificatestillactivecheck
            '''
            result = self._values.get("revoked_device_certificate_still_active_check")
            return typing.cast(typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def unauthenticated_cognito_role_overly_permissive_check(
            self,
        ) -> typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_a771d0ef]]:
            '''Checks if policy attached to an unauthenticated Amazon Cognito identity pool role is too permissive.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations-unauthenticatedcognitoroleoverlypermissivecheck
            '''
            result = self._values.get("unauthenticated_cognito_role_overly_permissive_check")
            return typing.cast(typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditCheckConfigurationProperty", _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuditCheckConfigurationsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnAccountAuditConfiguration.AuditNotificationTargetConfigurationsProperty",
        jsii_struct_bases=[],
        name_mapping={"sns": "sns"},
    )
    class AuditNotificationTargetConfigurationsProperty:
        def __init__(
            self,
            *,
            sns: typing.Optional[typing.Union[typing.Union["CfnAccountAuditConfiguration.AuditNotificationTargetProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''The configuration of the audit notification target.

            :param sns: The ``Sns`` notification target.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditnotificationtargetconfigurations.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                audit_notification_target_configurations_property = iot.CfnAccountAuditConfiguration.AuditNotificationTargetConfigurationsProperty(
                    sns=iot.CfnAccountAuditConfiguration.AuditNotificationTargetProperty(
                        enabled=False,
                        role_arn="roleArn",
                        target_arn="targetArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c705c85ad2da0d61407a058eab9f5441ae03ae0c66aee7af95c2c1056660062d)
                check_type(argname="argument sns", value=sns, expected_type=type_hints["sns"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if sns is not None:
                self._values["sns"] = sns

        @builtins.property
        def sns(
            self,
        ) -> typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditNotificationTargetProperty", _IResolvable_a771d0ef]]:
            '''The ``Sns`` notification target.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditnotificationtargetconfigurations.html#cfn-iot-accountauditconfiguration-auditnotificationtargetconfigurations-sns
            '''
            result = self._values.get("sns")
            return typing.cast(typing.Optional[typing.Union["CfnAccountAuditConfiguration.AuditNotificationTargetProperty", _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuditNotificationTargetConfigurationsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnAccountAuditConfiguration.AuditNotificationTargetProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enabled": "enabled",
            "role_arn": "roleArn",
            "target_arn": "targetArn",
        },
    )
    class AuditNotificationTargetProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            role_arn: typing.Optional[builtins.str] = None,
            target_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Information about the targets to which audit notifications are sent.

            :param enabled: True if notifications to the target are enabled.
            :param role_arn: The ARN of the role that grants permission to send notifications to the target.
            :param target_arn: The ARN of the target (SNS topic) to which audit notifications are sent.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditnotificationtarget.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                audit_notification_target_property = iot.CfnAccountAuditConfiguration.AuditNotificationTargetProperty(
                    enabled=False,
                    role_arn="roleArn",
                    target_arn="targetArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b39bf997a93d6f0434a608e80932d99b1a895bb1959ce6398e21bb3087a2f93d)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument target_arn", value=target_arn, expected_type=type_hints["target_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled
            if role_arn is not None:
                self._values["role_arn"] = role_arn
            if target_arn is not None:
                self._values["target_arn"] = target_arn

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''True if notifications to the target are enabled.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditnotificationtarget.html#cfn-iot-accountauditconfiguration-auditnotificationtarget-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def role_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the role that grants permission to send notifications to the target.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditnotificationtarget.html#cfn-iot-accountauditconfiguration-auditnotificationtarget-rolearn
            '''
            result = self._values.get("role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the target (SNS topic) to which audit notifications are sent.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditnotificationtarget.html#cfn-iot-accountauditconfiguration-auditnotificationtarget-targetarn
            '''
            result = self._values.get("target_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuditNotificationTargetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_iot.CfnAccountAuditConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "account_id": "accountId",
        "audit_check_configurations": "auditCheckConfigurations",
        "role_arn": "roleArn",
        "audit_notification_target_configurations": "auditNotificationTargetConfigurations",
    },
)
class CfnAccountAuditConfigurationProps:
    def __init__(
        self,
        *,
        account_id: builtins.str,
        audit_check_configurations: typing.Union[typing.Union[CfnAccountAuditConfiguration.AuditCheckConfigurationsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
        role_arn: builtins.str,
        audit_notification_target_configurations: typing.Optional[typing.Union[typing.Union[CfnAccountAuditConfiguration.AuditNotificationTargetConfigurationsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAccountAuditConfiguration``.

        :param account_id: The ID of the account. You can use the expression ``!Sub "${AWS::AccountId}"`` to use your account ID.
        :param audit_check_configurations: Specifies which audit checks are enabled and disabled for this account. Some data collection might start immediately when certain checks are enabled. When a check is disabled, any data collected so far in relation to the check is deleted. To disable a check, set the value of the ``Enabled:`` key to ``false`` . If an enabled check is removed from the template, it will also be disabled. You can't disable a check if it's used by any scheduled audit. You must delete the check from the scheduled audit or delete the scheduled audit itself to disable the check. For more information on avialbe auidt checks see `AWS::IoT::AccountAuditConfiguration AuditCheckConfigurations <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html>`_
        :param role_arn: The Amazon Resource Name (ARN) of the role that grants permission to AWS IoT to access information about your devices, policies, certificates, and other items as required when performing an audit.
        :param audit_notification_target_configurations: Information about the targets to which audit notifications are sent.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-accountauditconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_iot as iot
            
            cfn_account_audit_configuration_props = iot.CfnAccountAuditConfigurationProps(
                account_id="accountId",
                audit_check_configurations=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationsProperty(
                    authenticated_cognito_role_overly_permissive_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    ca_certificate_expiring_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    ca_certificate_key_quality_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    conflicting_client_ids_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    device_certificate_expiring_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    device_certificate_key_quality_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    device_certificate_shared_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    intermediate_ca_revoked_for_active_device_certificates_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    iot_policy_overly_permissive_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    io_tPolicy_potential_mis_configuration_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    iot_role_alias_allows_access_to_unused_services_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    iot_role_alias_overly_permissive_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    logging_disabled_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    revoked_ca_certificate_still_active_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    revoked_device_certificate_still_active_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    ),
                    unauthenticated_cognito_role_overly_permissive_check=iot.CfnAccountAuditConfiguration.AuditCheckConfigurationProperty(
                        enabled=False
                    )
                ),
                role_arn="roleArn",
            
                # the properties below are optional
                audit_notification_target_configurations=iot.CfnAccountAuditConfiguration.AuditNotificationTargetConfigurationsProperty(
                    sns=iot.CfnAccountAuditConfiguration.AuditNotificationTargetProperty(
                        enabled=False,
                        role_arn="roleArn",
                        target_arn="targetArn"
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe4d039eb2fde6efe1379ffa426a8799a2e9611fa326ceb114c58a89078b1560)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument audit_check_configurations", value=audit_check_configurations, expected_type=type_hints["audit_check_configurations"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument audit_notification_target_configurations", value=audit_notification_target_configurations, expected_type=type_hints["audit_notification_target_configurations"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_id": account_id,
            "audit_check_configurations": audit_check_configurations,
            "role_arn": role_arn,
        }
        if audit_notification_target_configurations is not None:
            self._values["audit_notification_target_configurations"] = audit_notification_target_configurations

    @builtins.property
    def account_id(self) -> builtins.str:
        '''The ID of the account.

        You can use the expression ``!Sub "${AWS::AccountId}"`` to use your account ID.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-accountauditconfiguration.html#cfn-iot-accountauditconfiguration-accountid
        '''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def audit_check_configurations(
        self,
    ) -> typing.Union[CfnAccountAuditConfiguration.AuditCheckConfigurationsProperty, _IResolvable_a771d0ef]:
        '''Specifies which audit checks are enabled and disabled for this account.

        Some data collection might start immediately when certain checks are enabled. When a check is disabled, any data collected so far in relation to the check is deleted. To disable a check, set the value of the ``Enabled:`` key to ``false`` .

        If an enabled check is removed from the template, it will also be disabled.

        You can't disable a check if it's used by any scheduled audit. You must delete the check from the scheduled audit or delete the scheduled audit itself to disable the check.

        For more information on avialbe auidt checks see `AWS::IoT::AccountAuditConfiguration AuditCheckConfigurations <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-accountauditconfiguration-auditcheckconfigurations.html>`_

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-accountauditconfiguration.html#cfn-iot-accountauditconfiguration-auditcheckconfigurations
        '''
        result = self._values.get("audit_check_configurations")
        assert result is not None, "Required property 'audit_check_configurations' is missing"
        return typing.cast(typing.Union[CfnAccountAuditConfiguration.AuditCheckConfigurationsProperty, _IResolvable_a771d0ef], result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the role that grants permission to AWS IoT to access information about your devices, policies, certificates, and other items as required when performing an audit.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-accountauditconfiguration.html#cfn-iot-accountauditconfiguration-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def audit_notification_target_configurations(
        self,
    ) -> typing.Optional[typing.Union[CfnAccountAuditConfiguration.AuditNotificationTargetConfigurationsProperty, _IResolvable_a771d0ef]]:
        '''Information about the targets to which audit notifications are sent.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-accountauditconfiguration.html#cfn-iot-accountauditconfiguration-auditnotificationtargetconfigurations
        '''
        result = self._values.get("audit_notification_target_configurations")
        return typing.cast(typing.Optional[typing.Union[CfnAccountAuditConfiguration.AuditNotificationTargetConfigurationsProperty, _IResolvable_a771d0ef]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAccountAuditConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnAuthorizer(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iot.CfnAuthorizer",
):
    '''A CloudFormation ``AWS::IoT::Authorizer``.

    Specifies an authorizer.

    :cloudformationResource: AWS::IoT::Authorizer
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_iot as iot
        
        cfn_authorizer = iot.CfnAuthorizer(self, "MyCfnAuthorizer",
            authorizer_function_arn="authorizerFunctionArn",
        
            # the properties below are optional
            authorizer_name="authorizerName",
            enable_caching_for_http=False,
            signing_disabled=False,
            status="status",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            token_key_name="tokenKeyName",
            token_signing_public_keys={
                "token_signing_public_keys_key": "tokenSigningPublicKeys"
            }
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        authorizer_function_arn: builtins.str,
        authorizer_name: typing.Optional[builtins.str] = None,
        enable_caching_for_http: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        signing_disabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
        token_key_name: typing.Optional[builtins.str] = None,
        token_signing_public_keys: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, builtins.str]]] = None,
    ) -> None:
        '''Create a new ``AWS::IoT::Authorizer``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param authorizer_function_arn: The authorizer's Lambda function ARN.
        :param authorizer_name: The authorizer name.
        :param enable_caching_for_http: ``AWS::IoT::Authorizer.EnableCachingForHttp``.
        :param signing_disabled: Specifies whether AWS IoT validates the token signature in an authorization request.
        :param status: The status of the authorizer. Valid values: ``ACTIVE`` | ``INACTIVE``
        :param tags: Metadata which can be used to manage the custom authorizer. .. epigraph:: For URI Request parameters use format: ...key1=value1&key2=value2... For the CLI command-line parameter use format: &&tags "key1=value1&key2=value2..." For the cli-input-json file use format: "tags": "key1=value1&key2=value2..."
        :param token_key_name: The key used to extract the token from the HTTP headers.
        :param token_signing_public_keys: The public keys used to validate the token signature returned by your custom authentication service.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb3d4475a2c47548b973752777c9b0cff14761d68b55e59b674d8ecd1e3b0534)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAuthorizerProps(
            authorizer_function_arn=authorizer_function_arn,
            authorizer_name=authorizer_name,
            enable_caching_for_http=enable_caching_for_http,
            signing_disabled=signing_disabled,
            status=status,
            tags=tags,
            token_key_name=token_key_name,
            token_signing_public_keys=token_signing_public_keys,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__393265a5c60fa3d96cacb06aaf67fea5b69fa5962102f55facae0247e4627fe2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__87153c2db95e8d2a428c654b27c0032207c40ada471606a006d46dd5e925a7db)
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
        '''The Amazon Resource Name (ARN) of the authorizer.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''Metadata which can be used to manage the custom authorizer.

        .. epigraph::

           For URI Request parameters use format: ...key1=value1&key2=value2...

           For the CLI command-line parameter use format: &&tags "key1=value1&key2=value2..."

           For the cli-input-json file use format: "tags": "key1=value1&key2=value2..."

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html#cfn-iot-authorizer-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="authorizerFunctionArn")
    def authorizer_function_arn(self) -> builtins.str:
        '''The authorizer's Lambda function ARN.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html#cfn-iot-authorizer-authorizerfunctionarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "authorizerFunctionArn"))

    @authorizer_function_arn.setter
    def authorizer_function_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ddf58b6dd2822aa9ef7f673d2429759b7ec9f126bf87a5d2ab871493e908fea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizerFunctionArn", value)

    @builtins.property
    @jsii.member(jsii_name="authorizerName")
    def authorizer_name(self) -> typing.Optional[builtins.str]:
        '''The authorizer name.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html#cfn-iot-authorizer-authorizername
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authorizerName"))

    @authorizer_name.setter
    def authorizer_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37ef5ea4d3ab384464cbd4b3dd894b559abe2b73e7edbe814c0bb3c4b5470108)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizerName", value)

    @builtins.property
    @jsii.member(jsii_name="enableCachingForHttp")
    def enable_caching_for_http(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''``AWS::IoT::Authorizer.EnableCachingForHttp``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html#cfn-iot-authorizer-enablecachingforhttp
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], jsii.get(self, "enableCachingForHttp"))

    @enable_caching_for_http.setter
    def enable_caching_for_http(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52b0810482d8bfca9db2d7ded06a9e7da766b6ec01a3b569a63c1ba8cf408c6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableCachingForHttp", value)

    @builtins.property
    @jsii.member(jsii_name="signingDisabled")
    def signing_disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''Specifies whether AWS IoT validates the token signature in an authorization request.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html#cfn-iot-authorizer-signingdisabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], jsii.get(self, "signingDisabled"))

    @signing_disabled.setter
    def signing_disabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9816cdb1250cc33b96cda68deb60d284d5a26fb35ab7439e4231ccb53df0fdce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signingDisabled", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''The status of the authorizer.

        Valid values: ``ACTIVE`` | ``INACTIVE``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html#cfn-iot-authorizer-status
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ae846646e7f76534ec709919af00314c49f1a20ff74b5d6c0dea4176f0e612d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="tokenKeyName")
    def token_key_name(self) -> typing.Optional[builtins.str]:
        '''The key used to extract the token from the HTTP headers.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html#cfn-iot-authorizer-tokenkeyname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenKeyName"))

    @token_key_name.setter
    def token_key_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4d22e3fb78176f8fb41cf67e1a83fc5bca67e2ff61d03f7b1e7c4ebab2c2e7a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenKeyName", value)

    @builtins.property
    @jsii.member(jsii_name="tokenSigningPublicKeys")
    def token_signing_public_keys(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, builtins.str]]]:
        '''The public keys used to validate the token signature returned by your custom authentication service.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html#cfn-iot-authorizer-tokensigningpublickeys
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "tokenSigningPublicKeys"))

    @token_signing_public_keys.setter
    def token_signing_public_keys(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a92430672f5805744463426fe7335e7a42edee162ca7eba2a4b3a49922f88f17)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenSigningPublicKeys", value)


@jsii.data_type(
    jsii_type="monocdk.aws_iot.CfnAuthorizerProps",
    jsii_struct_bases=[],
    name_mapping={
        "authorizer_function_arn": "authorizerFunctionArn",
        "authorizer_name": "authorizerName",
        "enable_caching_for_http": "enableCachingForHttp",
        "signing_disabled": "signingDisabled",
        "status": "status",
        "tags": "tags",
        "token_key_name": "tokenKeyName",
        "token_signing_public_keys": "tokenSigningPublicKeys",
    },
)
class CfnAuthorizerProps:
    def __init__(
        self,
        *,
        authorizer_function_arn: builtins.str,
        authorizer_name: typing.Optional[builtins.str] = None,
        enable_caching_for_http: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        signing_disabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
        token_key_name: typing.Optional[builtins.str] = None,
        token_signing_public_keys: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, builtins.str]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAuthorizer``.

        :param authorizer_function_arn: The authorizer's Lambda function ARN.
        :param authorizer_name: The authorizer name.
        :param enable_caching_for_http: ``AWS::IoT::Authorizer.EnableCachingForHttp``.
        :param signing_disabled: Specifies whether AWS IoT validates the token signature in an authorization request.
        :param status: The status of the authorizer. Valid values: ``ACTIVE`` | ``INACTIVE``
        :param tags: Metadata which can be used to manage the custom authorizer. .. epigraph:: For URI Request parameters use format: ...key1=value1&key2=value2... For the CLI command-line parameter use format: &&tags "key1=value1&key2=value2..." For the cli-input-json file use format: "tags": "key1=value1&key2=value2..."
        :param token_key_name: The key used to extract the token from the HTTP headers.
        :param token_signing_public_keys: The public keys used to validate the token signature returned by your custom authentication service.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_iot as iot
            
            cfn_authorizer_props = iot.CfnAuthorizerProps(
                authorizer_function_arn="authorizerFunctionArn",
            
                # the properties below are optional
                authorizer_name="authorizerName",
                enable_caching_for_http=False,
                signing_disabled=False,
                status="status",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                token_key_name="tokenKeyName",
                token_signing_public_keys={
                    "token_signing_public_keys_key": "tokenSigningPublicKeys"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__622515a7aaf08f5fc240a31ae650f399d7cf0608bdc8c8030f2508bf611883f5)
            check_type(argname="argument authorizer_function_arn", value=authorizer_function_arn, expected_type=type_hints["authorizer_function_arn"])
            check_type(argname="argument authorizer_name", value=authorizer_name, expected_type=type_hints["authorizer_name"])
            check_type(argname="argument enable_caching_for_http", value=enable_caching_for_http, expected_type=type_hints["enable_caching_for_http"])
            check_type(argname="argument signing_disabled", value=signing_disabled, expected_type=type_hints["signing_disabled"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument token_key_name", value=token_key_name, expected_type=type_hints["token_key_name"])
            check_type(argname="argument token_signing_public_keys", value=token_signing_public_keys, expected_type=type_hints["token_signing_public_keys"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "authorizer_function_arn": authorizer_function_arn,
        }
        if authorizer_name is not None:
            self._values["authorizer_name"] = authorizer_name
        if enable_caching_for_http is not None:
            self._values["enable_caching_for_http"] = enable_caching_for_http
        if signing_disabled is not None:
            self._values["signing_disabled"] = signing_disabled
        if status is not None:
            self._values["status"] = status
        if tags is not None:
            self._values["tags"] = tags
        if token_key_name is not None:
            self._values["token_key_name"] = token_key_name
        if token_signing_public_keys is not None:
            self._values["token_signing_public_keys"] = token_signing_public_keys

    @builtins.property
    def authorizer_function_arn(self) -> builtins.str:
        '''The authorizer's Lambda function ARN.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html#cfn-iot-authorizer-authorizerfunctionarn
        '''
        result = self._values.get("authorizer_function_arn")
        assert result is not None, "Required property 'authorizer_function_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authorizer_name(self) -> typing.Optional[builtins.str]:
        '''The authorizer name.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html#cfn-iot-authorizer-authorizername
        '''
        result = self._values.get("authorizer_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_caching_for_http(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''``AWS::IoT::Authorizer.EnableCachingForHttp``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html#cfn-iot-authorizer-enablecachingforhttp
        '''
        result = self._values.get("enable_caching_for_http")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

    @builtins.property
    def signing_disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''Specifies whether AWS IoT validates the token signature in an authorization request.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html#cfn-iot-authorizer-signingdisabled
        '''
        result = self._values.get("signing_disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''The status of the authorizer.

        Valid values: ``ACTIVE`` | ``INACTIVE``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html#cfn-iot-authorizer-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''Metadata which can be used to manage the custom authorizer.

        .. epigraph::

           For URI Request parameters use format: ...key1=value1&key2=value2...

           For the CLI command-line parameter use format: &&tags "key1=value1&key2=value2..."

           For the cli-input-json file use format: "tags": "key1=value1&key2=value2..."

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html#cfn-iot-authorizer-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    @builtins.property
    def token_key_name(self) -> typing.Optional[builtins.str]:
        '''The key used to extract the token from the HTTP headers.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html#cfn-iot-authorizer-tokenkeyname
        '''
        result = self._values.get("token_key_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token_signing_public_keys(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, builtins.str]]]:
        '''The public keys used to validate the token signature returned by your custom authentication service.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-authorizer.html#cfn-iot-authorizer-tokensigningpublickeys
        '''
        result = self._values.get("token_signing_public_keys")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, builtins.str]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAuthorizerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnCACertificate(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iot.CfnCACertificate",
):
    '''A CloudFormation ``AWS::IoT::CACertificate``.

    Specifies a CA certificate.

    :cloudformationResource: AWS::IoT::CACertificate
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_iot as iot
        
        cfn_cACertificate = iot.CfnCACertificate(self, "MyCfnCACertificate",
            ca_certificate_pem="caCertificatePem",
            status="status",
        
            # the properties below are optional
            auto_registration_status="autoRegistrationStatus",
            certificate_mode="certificateMode",
            registration_config=iot.CfnCACertificate.RegistrationConfigProperty(
                role_arn="roleArn",
                template_body="templateBody",
                template_name="templateName"
            ),
            remove_auto_registration=False,
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            verification_certificate_pem="verificationCertificatePem"
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        ca_certificate_pem: builtins.str,
        status: builtins.str,
        auto_registration_status: typing.Optional[builtins.str] = None,
        certificate_mode: typing.Optional[builtins.str] = None,
        registration_config: typing.Optional[typing.Union[typing.Union["CfnCACertificate.RegistrationConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        remove_auto_registration: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
        verification_certificate_pem: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::IoT::CACertificate``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param ca_certificate_pem: The certificate data in PEM format.
        :param status: The status of the CA certificate. Valid values are "ACTIVE" and "INACTIVE".
        :param auto_registration_status: Whether the CA certificate is configured for auto registration of device certificates. Valid values are "ENABLE" and "DISABLE".
        :param certificate_mode: The mode of the CA. All the device certificates that are registered using this CA will be registered in the same mode as the CA. For more information about certificate mode for device certificates, see `certificate mode <https://docs.aws.amazon.com//iot/latest/apireference/API_CertificateDescription.html#iot-Type-CertificateDescription-certificateMode>`_ . Valid values are "DEFAULT" and "SNI_ONLY".
        :param registration_config: Information about the registration configuration.
        :param remove_auto_registration: If true, removes auto registration.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param verification_certificate_pem: The private key verification certificate.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5df10346f5adc6dc276c52d395ea544195453293830dc65db55e15eec8ce3d97)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCACertificateProps(
            ca_certificate_pem=ca_certificate_pem,
            status=status,
            auto_registration_status=auto_registration_status,
            certificate_mode=certificate_mode,
            registration_config=registration_config,
            remove_auto_registration=remove_auto_registration,
            tags=tags,
            verification_certificate_pem=verification_certificate_pem,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2954d0f735960aedcf41f245b79c96ba6a195d28e45d455ebe8bf4a37ec5c8d9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3f88ebd33a08489c9d2aa7d0f11215e1159c40adaa24e2243529e6ca1e0a6522)
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
        '''Returns the Amazon Resource Name (ARN) for the instance profile. For example:.

        ``{ "Fn::GetAtt": ["MyCACertificate", "Arn"] }``

        A value similar to the following is returned:

        ``arn:aws:iot:us-east-1:123456789012:cacert/a6be6b84559801927e35a8f901fae08b5971d78d1562e29504ff9663b276a5f5``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The CA certificate ID.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html#cfn-iot-cacertificate-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="caCertificatePem")
    def ca_certificate_pem(self) -> builtins.str:
        '''The certificate data in PEM format.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html#cfn-iot-cacertificate-cacertificatepem
        '''
        return typing.cast(builtins.str, jsii.get(self, "caCertificatePem"))

    @ca_certificate_pem.setter
    def ca_certificate_pem(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07b24e8d3d99c28b3387bbad28620bfad12c47dda99fd97998117e22bde62d68)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caCertificatePem", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        '''The status of the CA certificate.

        Valid values are "ACTIVE" and "INACTIVE".

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html#cfn-iot-cacertificate-status
        '''
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35f6753340d6a65c1a34e9f7b99f2fea9a1a4bc1ab1b2fddea5f5ad848547021)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="autoRegistrationStatus")
    def auto_registration_status(self) -> typing.Optional[builtins.str]:
        '''Whether the CA certificate is configured for auto registration of device certificates.

        Valid values are "ENABLE" and "DISABLE".

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html#cfn-iot-cacertificate-autoregistrationstatus
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoRegistrationStatus"))

    @auto_registration_status.setter
    def auto_registration_status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0909ccca1dcf081687443f2b1131f47dd47159ba891348f4274c1d6527c207ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoRegistrationStatus", value)

    @builtins.property
    @jsii.member(jsii_name="certificateMode")
    def certificate_mode(self) -> typing.Optional[builtins.str]:
        '''The mode of the CA.

        All the device certificates that are registered using this CA will be registered in the same mode as the CA. For more information about certificate mode for device certificates, see `certificate mode <https://docs.aws.amazon.com//iot/latest/apireference/API_CertificateDescription.html#iot-Type-CertificateDescription-certificateMode>`_ .

        Valid values are "DEFAULT" and "SNI_ONLY".

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html#cfn-iot-cacertificate-certificatemode
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateMode"))

    @certificate_mode.setter
    def certificate_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5f97aedfa05b70d0f9c1bad07469f863220ecaeffd6862ba43ebad37c8c6d82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateMode", value)

    @builtins.property
    @jsii.member(jsii_name="registrationConfig")
    def registration_config(
        self,
    ) -> typing.Optional[typing.Union["CfnCACertificate.RegistrationConfigProperty", _IResolvable_a771d0ef]]:
        '''Information about the registration configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html#cfn-iot-cacertificate-registrationconfig
        '''
        return typing.cast(typing.Optional[typing.Union["CfnCACertificate.RegistrationConfigProperty", _IResolvable_a771d0ef]], jsii.get(self, "registrationConfig"))

    @registration_config.setter
    def registration_config(
        self,
        value: typing.Optional[typing.Union["CfnCACertificate.RegistrationConfigProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fdeb2d3dfd572ecb5655073a143af21a819a63a8766bc9e6753a6f50c800cb6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "registrationConfig", value)

    @builtins.property
    @jsii.member(jsii_name="removeAutoRegistration")
    def remove_auto_registration(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''If true, removes auto registration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html#cfn-iot-cacertificate-removeautoregistration
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], jsii.get(self, "removeAutoRegistration"))

    @remove_auto_registration.setter
    def remove_auto_registration(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2254fab851774a14895a29dfcc6b6930886ac15b9f5d11dcb2d78c43bb2d62ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "removeAutoRegistration", value)

    @builtins.property
    @jsii.member(jsii_name="verificationCertificatePem")
    def verification_certificate_pem(self) -> typing.Optional[builtins.str]:
        '''The private key verification certificate.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html#cfn-iot-cacertificate-verificationcertificatepem
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "verificationCertificatePem"))

    @verification_certificate_pem.setter
    def verification_certificate_pem(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d875df1b83d04338ef80f8897b314945159ddd0846b5b1bb02bb38e38798053)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "verificationCertificatePem", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnCACertificate.RegistrationConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "role_arn": "roleArn",
            "template_body": "templateBody",
            "template_name": "templateName",
        },
    )
    class RegistrationConfigProperty:
        def __init__(
            self,
            *,
            role_arn: typing.Optional[builtins.str] = None,
            template_body: typing.Optional[builtins.str] = None,
            template_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The registration configuration.

            :param role_arn: The ARN of the role.
            :param template_body: The template body.
            :param template_name: The name of the provisioning template.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-cacertificate-registrationconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                registration_config_property = iot.CfnCACertificate.RegistrationConfigProperty(
                    role_arn="roleArn",
                    template_body="templateBody",
                    template_name="templateName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__46c70e01b06ea5f8172ce27ae017b96ca7c083ff55ea1cca833cb379c8c9bcec)
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument template_body", value=template_body, expected_type=type_hints["template_body"])
                check_type(argname="argument template_name", value=template_name, expected_type=type_hints["template_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if role_arn is not None:
                self._values["role_arn"] = role_arn
            if template_body is not None:
                self._values["template_body"] = template_body
            if template_name is not None:
                self._values["template_name"] = template_name

        @builtins.property
        def role_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the role.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-cacertificate-registrationconfig.html#cfn-iot-cacertificate-registrationconfig-rolearn
            '''
            result = self._values.get("role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def template_body(self) -> typing.Optional[builtins.str]:
            '''The template body.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-cacertificate-registrationconfig.html#cfn-iot-cacertificate-registrationconfig-templatebody
            '''
            result = self._values.get("template_body")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def template_name(self) -> typing.Optional[builtins.str]:
            '''The name of the provisioning template.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-cacertificate-registrationconfig.html#cfn-iot-cacertificate-registrationconfig-templatename
            '''
            result = self._values.get("template_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RegistrationConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_iot.CfnCACertificateProps",
    jsii_struct_bases=[],
    name_mapping={
        "ca_certificate_pem": "caCertificatePem",
        "status": "status",
        "auto_registration_status": "autoRegistrationStatus",
        "certificate_mode": "certificateMode",
        "registration_config": "registrationConfig",
        "remove_auto_registration": "removeAutoRegistration",
        "tags": "tags",
        "verification_certificate_pem": "verificationCertificatePem",
    },
)
class CfnCACertificateProps:
    def __init__(
        self,
        *,
        ca_certificate_pem: builtins.str,
        status: builtins.str,
        auto_registration_status: typing.Optional[builtins.str] = None,
        certificate_mode: typing.Optional[builtins.str] = None,
        registration_config: typing.Optional[typing.Union[typing.Union[CfnCACertificate.RegistrationConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        remove_auto_registration: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
        verification_certificate_pem: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnCACertificate``.

        :param ca_certificate_pem: The certificate data in PEM format.
        :param status: The status of the CA certificate. Valid values are "ACTIVE" and "INACTIVE".
        :param auto_registration_status: Whether the CA certificate is configured for auto registration of device certificates. Valid values are "ENABLE" and "DISABLE".
        :param certificate_mode: The mode of the CA. All the device certificates that are registered using this CA will be registered in the same mode as the CA. For more information about certificate mode for device certificates, see `certificate mode <https://docs.aws.amazon.com//iot/latest/apireference/API_CertificateDescription.html#iot-Type-CertificateDescription-certificateMode>`_ . Valid values are "DEFAULT" and "SNI_ONLY".
        :param registration_config: Information about the registration configuration.
        :param remove_auto_registration: If true, removes auto registration.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param verification_certificate_pem: The private key verification certificate.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_iot as iot
            
            cfn_cACertificate_props = iot.CfnCACertificateProps(
                ca_certificate_pem="caCertificatePem",
                status="status",
            
                # the properties below are optional
                auto_registration_status="autoRegistrationStatus",
                certificate_mode="certificateMode",
                registration_config=iot.CfnCACertificate.RegistrationConfigProperty(
                    role_arn="roleArn",
                    template_body="templateBody",
                    template_name="templateName"
                ),
                remove_auto_registration=False,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                verification_certificate_pem="verificationCertificatePem"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3794474e144684ec752cf7d043907532c3c2793028dbcbaeeecdc73ed155167)
            check_type(argname="argument ca_certificate_pem", value=ca_certificate_pem, expected_type=type_hints["ca_certificate_pem"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument auto_registration_status", value=auto_registration_status, expected_type=type_hints["auto_registration_status"])
            check_type(argname="argument certificate_mode", value=certificate_mode, expected_type=type_hints["certificate_mode"])
            check_type(argname="argument registration_config", value=registration_config, expected_type=type_hints["registration_config"])
            check_type(argname="argument remove_auto_registration", value=remove_auto_registration, expected_type=type_hints["remove_auto_registration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument verification_certificate_pem", value=verification_certificate_pem, expected_type=type_hints["verification_certificate_pem"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ca_certificate_pem": ca_certificate_pem,
            "status": status,
        }
        if auto_registration_status is not None:
            self._values["auto_registration_status"] = auto_registration_status
        if certificate_mode is not None:
            self._values["certificate_mode"] = certificate_mode
        if registration_config is not None:
            self._values["registration_config"] = registration_config
        if remove_auto_registration is not None:
            self._values["remove_auto_registration"] = remove_auto_registration
        if tags is not None:
            self._values["tags"] = tags
        if verification_certificate_pem is not None:
            self._values["verification_certificate_pem"] = verification_certificate_pem

    @builtins.property
    def ca_certificate_pem(self) -> builtins.str:
        '''The certificate data in PEM format.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html#cfn-iot-cacertificate-cacertificatepem
        '''
        result = self._values.get("ca_certificate_pem")
        assert result is not None, "Required property 'ca_certificate_pem' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def status(self) -> builtins.str:
        '''The status of the CA certificate.

        Valid values are "ACTIVE" and "INACTIVE".

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html#cfn-iot-cacertificate-status
        '''
        result = self._values.get("status")
        assert result is not None, "Required property 'status' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_registration_status(self) -> typing.Optional[builtins.str]:
        '''Whether the CA certificate is configured for auto registration of device certificates.

        Valid values are "ENABLE" and "DISABLE".

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html#cfn-iot-cacertificate-autoregistrationstatus
        '''
        result = self._values.get("auto_registration_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_mode(self) -> typing.Optional[builtins.str]:
        '''The mode of the CA.

        All the device certificates that are registered using this CA will be registered in the same mode as the CA. For more information about certificate mode for device certificates, see `certificate mode <https://docs.aws.amazon.com//iot/latest/apireference/API_CertificateDescription.html#iot-Type-CertificateDescription-certificateMode>`_ .

        Valid values are "DEFAULT" and "SNI_ONLY".

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html#cfn-iot-cacertificate-certificatemode
        '''
        result = self._values.get("certificate_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def registration_config(
        self,
    ) -> typing.Optional[typing.Union[CfnCACertificate.RegistrationConfigProperty, _IResolvable_a771d0ef]]:
        '''Information about the registration configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html#cfn-iot-cacertificate-registrationconfig
        '''
        result = self._values.get("registration_config")
        return typing.cast(typing.Optional[typing.Union[CfnCACertificate.RegistrationConfigProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def remove_auto_registration(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''If true, removes auto registration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html#cfn-iot-cacertificate-removeautoregistration
        '''
        result = self._values.get("remove_auto_registration")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html#cfn-iot-cacertificate-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    @builtins.property
    def verification_certificate_pem(self) -> typing.Optional[builtins.str]:
        '''The private key verification certificate.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-cacertificate.html#cfn-iot-cacertificate-verificationcertificatepem
        '''
        result = self._values.get("verification_certificate_pem")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCACertificateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnCertificate(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iot.CfnCertificate",
):
    '''A CloudFormation ``AWS::IoT::Certificate``.

    Use the ``AWS::IoT::Certificate`` resource to declare an AWS IoT X.509 certificate. For information about working with X.509 certificates, see `X.509 Client Certificates <https://docs.aws.amazon.com/iot/latest/developerguide/x509-client-certs.html>`_ in the *AWS IoT Developer Guide* .

    :cloudformationResource: AWS::IoT::Certificate
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-certificate.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_iot as iot
        
        cfn_certificate = iot.CfnCertificate(self, "MyCfnCertificate",
            status="status",
        
            # the properties below are optional
            ca_certificate_pem="caCertificatePem",
            certificate_mode="certificateMode",
            certificate_pem="certificatePem",
            certificate_signing_request="certificateSigningRequest"
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        status: builtins.str,
        ca_certificate_pem: typing.Optional[builtins.str] = None,
        certificate_mode: typing.Optional[builtins.str] = None,
        certificate_pem: typing.Optional[builtins.str] = None,
        certificate_signing_request: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::IoT::Certificate``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param status: The status of the certificate. Valid values are ACTIVE, INACTIVE, REVOKED, PENDING_TRANSFER, and PENDING_ACTIVATION. The status value REGISTER_INACTIVE is deprecated and should not be used.
        :param ca_certificate_pem: The CA certificate used to sign the device certificate being registered, not available when CertificateMode is SNI_ONLY.
        :param certificate_mode: Specifies which mode of certificate registration to use with this resource. Valid options are DEFAULT with CaCertificatePem and CertificatePem, SNI_ONLY with CertificatePem, and Default with CertificateSigningRequest. ``DEFAULT`` : A certificate in ``DEFAULT`` mode is either generated by AWS IoT Core or registered with an issuer certificate authority (CA). Devices with certificates in ``DEFAULT`` mode aren't required to send the Server Name Indication (SNI) extension when connecting to AWS IoT Core . However, to use features such as custom domains and VPC endpoints, we recommend that you use the SNI extension when connecting to AWS IoT Core . ``SNI_ONLY`` : A certificate in ``SNI_ONLY`` mode is registered without an issuer CA. Devices with certificates in ``SNI_ONLY`` mode must send the SNI extension when connecting to AWS IoT Core .
        :param certificate_pem: The certificate data in PEM format. Requires SNI_ONLY for the certificate mode or the accompanying CACertificatePem for registration.
        :param certificate_signing_request: The certificate signing request (CSR).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e9f9930a9ef23dbbc0c80120852a3d3d7eaed14500fb832a34a7850a5fa02ec)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCertificateProps(
            status=status,
            ca_certificate_pem=ca_certificate_pem,
            certificate_mode=certificate_mode,
            certificate_pem=certificate_pem,
            certificate_signing_request=certificate_signing_request,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc96b621eef02c335b00a479741d80fe785601c347561199d6c92c3d4a0f0c26)
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
            type_hints = typing.get_type_hints(_typecheckingstub__56cd44293d14f49ccc9499874a0feac053f4743a00822272b08c8a9f8f03abb1)
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
        '''Returns the Amazon Resource Name (ARN) for the instance profile. For example:.

        ``{ "Fn::GetAtt": ["MyCertificate", "Arn"] }``

        A value similar to the following is returned:

        ``arn:aws:iot:ap-southeast-2:123456789012:cert/a1234567b89c012d3e4fg567hij8k9l01mno1p23q45678901rs234567890t1u2``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The certificate ID.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        '''The status of the certificate.

        Valid values are ACTIVE, INACTIVE, REVOKED, PENDING_TRANSFER, and PENDING_ACTIVATION.

        The status value REGISTER_INACTIVE is deprecated and should not be used.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-certificate.html#cfn-iot-certificate-status
        '''
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c3ec031d0f8d34534c9490f6838104426047a5873f836979214c1e0e817bfb5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="caCertificatePem")
    def ca_certificate_pem(self) -> typing.Optional[builtins.str]:
        '''The CA certificate used to sign the device certificate being registered, not available when CertificateMode is SNI_ONLY.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-certificate.html#cfn-iot-certificate-cacertificatepem
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "caCertificatePem"))

    @ca_certificate_pem.setter
    def ca_certificate_pem(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98d65aabc08896681c643a46b414185be01155fbbbdc53face2ff76c620c5099)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caCertificatePem", value)

    @builtins.property
    @jsii.member(jsii_name="certificateMode")
    def certificate_mode(self) -> typing.Optional[builtins.str]:
        '''Specifies which mode of certificate registration to use with this resource.

        Valid options are DEFAULT with CaCertificatePem and CertificatePem, SNI_ONLY with CertificatePem, and Default with CertificateSigningRequest.

        ``DEFAULT`` : A certificate in ``DEFAULT`` mode is either generated by AWS IoT Core or registered with an issuer certificate authority (CA). Devices with certificates in ``DEFAULT`` mode aren't required to send the Server Name Indication (SNI) extension when connecting to AWS IoT Core . However, to use features such as custom domains and VPC endpoints, we recommend that you use the SNI extension when connecting to AWS IoT Core .

        ``SNI_ONLY`` : A certificate in ``SNI_ONLY`` mode is registered without an issuer CA. Devices with certificates in ``SNI_ONLY`` mode must send the SNI extension when connecting to AWS IoT Core .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-certificate.html#cfn-iot-certificate-certificatemode
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateMode"))

    @certificate_mode.setter
    def certificate_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ac27a55c4f19acffeda86e297ef5f3902d0451c81cf4311a4f3b90ee00c7024)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateMode", value)

    @builtins.property
    @jsii.member(jsii_name="certificatePem")
    def certificate_pem(self) -> typing.Optional[builtins.str]:
        '''The certificate data in PEM format.

        Requires SNI_ONLY for the certificate mode or the accompanying CACertificatePem for registration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-certificate.html#cfn-iot-certificate-certificatepem
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificatePem"))

    @certificate_pem.setter
    def certificate_pem(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9427cb91627083d5c604783fb2fdd96813bce8273bc0b4cf7211f279ca5e15c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificatePem", value)

    @builtins.property
    @jsii.member(jsii_name="certificateSigningRequest")
    def certificate_signing_request(self) -> typing.Optional[builtins.str]:
        '''The certificate signing request (CSR).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-certificate.html#cfn-iot-certificate-certificatesigningrequest
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateSigningRequest"))

    @certificate_signing_request.setter
    def certificate_signing_request(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f751fb1b3c832b2ae9513cd80fbc3a592ac05a48f50d11e4e4d28f6bce1872b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateSigningRequest", value)


@jsii.data_type(
    jsii_type="monocdk.aws_iot.CfnCertificateProps",
    jsii_struct_bases=[],
    name_mapping={
        "status": "status",
        "ca_certificate_pem": "caCertificatePem",
        "certificate_mode": "certificateMode",
        "certificate_pem": "certificatePem",
        "certificate_signing_request": "certificateSigningRequest",
    },
)
class CfnCertificateProps:
    def __init__(
        self,
        *,
        status: builtins.str,
        ca_certificate_pem: typing.Optional[builtins.str] = None,
        certificate_mode: typing.Optional[builtins.str] = None,
        certificate_pem: typing.Optional[builtins.str] = None,
        certificate_signing_request: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnCertificate``.

        :param status: The status of the certificate. Valid values are ACTIVE, INACTIVE, REVOKED, PENDING_TRANSFER, and PENDING_ACTIVATION. The status value REGISTER_INACTIVE is deprecated and should not be used.
        :param ca_certificate_pem: The CA certificate used to sign the device certificate being registered, not available when CertificateMode is SNI_ONLY.
        :param certificate_mode: Specifies which mode of certificate registration to use with this resource. Valid options are DEFAULT with CaCertificatePem and CertificatePem, SNI_ONLY with CertificatePem, and Default with CertificateSigningRequest. ``DEFAULT`` : A certificate in ``DEFAULT`` mode is either generated by AWS IoT Core or registered with an issuer certificate authority (CA). Devices with certificates in ``DEFAULT`` mode aren't required to send the Server Name Indication (SNI) extension when connecting to AWS IoT Core . However, to use features such as custom domains and VPC endpoints, we recommend that you use the SNI extension when connecting to AWS IoT Core . ``SNI_ONLY`` : A certificate in ``SNI_ONLY`` mode is registered without an issuer CA. Devices with certificates in ``SNI_ONLY`` mode must send the SNI extension when connecting to AWS IoT Core .
        :param certificate_pem: The certificate data in PEM format. Requires SNI_ONLY for the certificate mode or the accompanying CACertificatePem for registration.
        :param certificate_signing_request: The certificate signing request (CSR).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-certificate.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_iot as iot
            
            cfn_certificate_props = iot.CfnCertificateProps(
                status="status",
            
                # the properties below are optional
                ca_certificate_pem="caCertificatePem",
                certificate_mode="certificateMode",
                certificate_pem="certificatePem",
                certificate_signing_request="certificateSigningRequest"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16f767e9b8ce74a2e27d508dfe51e4bf1d3cfb255b49b1f480bc2a0d8c643f33)
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument ca_certificate_pem", value=ca_certificate_pem, expected_type=type_hints["ca_certificate_pem"])
            check_type(argname="argument certificate_mode", value=certificate_mode, expected_type=type_hints["certificate_mode"])
            check_type(argname="argument certificate_pem", value=certificate_pem, expected_type=type_hints["certificate_pem"])
            check_type(argname="argument certificate_signing_request", value=certificate_signing_request, expected_type=type_hints["certificate_signing_request"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "status": status,
        }
        if ca_certificate_pem is not None:
            self._values["ca_certificate_pem"] = ca_certificate_pem
        if certificate_mode is not None:
            self._values["certificate_mode"] = certificate_mode
        if certificate_pem is not None:
            self._values["certificate_pem"] = certificate_pem
        if certificate_signing_request is not None:
            self._values["certificate_signing_request"] = certificate_signing_request

    @builtins.property
    def status(self) -> builtins.str:
        '''The status of the certificate.

        Valid values are ACTIVE, INACTIVE, REVOKED, PENDING_TRANSFER, and PENDING_ACTIVATION.

        The status value REGISTER_INACTIVE is deprecated and should not be used.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-certificate.html#cfn-iot-certificate-status
        '''
        result = self._values.get("status")
        assert result is not None, "Required property 'status' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ca_certificate_pem(self) -> typing.Optional[builtins.str]:
        '''The CA certificate used to sign the device certificate being registered, not available when CertificateMode is SNI_ONLY.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-certificate.html#cfn-iot-certificate-cacertificatepem
        '''
        result = self._values.get("ca_certificate_pem")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_mode(self) -> typing.Optional[builtins.str]:
        '''Specifies which mode of certificate registration to use with this resource.

        Valid options are DEFAULT with CaCertificatePem and CertificatePem, SNI_ONLY with CertificatePem, and Default with CertificateSigningRequest.

        ``DEFAULT`` : A certificate in ``DEFAULT`` mode is either generated by AWS IoT Core or registered with an issuer certificate authority (CA). Devices with certificates in ``DEFAULT`` mode aren't required to send the Server Name Indication (SNI) extension when connecting to AWS IoT Core . However, to use features such as custom domains and VPC endpoints, we recommend that you use the SNI extension when connecting to AWS IoT Core .

        ``SNI_ONLY`` : A certificate in ``SNI_ONLY`` mode is registered without an issuer CA. Devices with certificates in ``SNI_ONLY`` mode must send the SNI extension when connecting to AWS IoT Core .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-certificate.html#cfn-iot-certificate-certificatemode
        '''
        result = self._values.get("certificate_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_pem(self) -> typing.Optional[builtins.str]:
        '''The certificate data in PEM format.

        Requires SNI_ONLY for the certificate mode or the accompanying CACertificatePem for registration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-certificate.html#cfn-iot-certificate-certificatepem
        '''
        result = self._values.get("certificate_pem")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_signing_request(self) -> typing.Optional[builtins.str]:
        '''The certificate signing request (CSR).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-certificate.html#cfn-iot-certificate-certificatesigningrequest
        '''
        result = self._values.get("certificate_signing_request")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCertificateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnCustomMetric(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iot.CfnCustomMetric",
):
    '''A CloudFormation ``AWS::IoT::CustomMetric``.

    Use the ``AWS::IoT::CustomMetric`` resource to define a custom metric published by your devices to Device Defender. For API reference, see `CreateCustomMetric <https://docs.aws.amazon.com/iot/latest/apireference/API_CreateCustomMetric.html>`_ and for general information, see `Custom metrics <https://docs.aws.amazon.com/iot/latest/developerguide/dd-detect-custom-metrics.html>`_ .

    :cloudformationResource: AWS::IoT::CustomMetric
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-custommetric.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_iot as iot
        
        cfn_custom_metric = iot.CfnCustomMetric(self, "MyCfnCustomMetric",
            metric_type="metricType",
        
            # the properties below are optional
            display_name="displayName",
            metric_name="metricName",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        metric_type: builtins.str,
        display_name: typing.Optional[builtins.str] = None,
        metric_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::IoT::CustomMetric``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param metric_type: The type of the custom metric. Types include ``string-list`` , ``ip-address-list`` , ``number-list`` , and ``number`` . .. epigraph:: The type ``number`` only takes a single metric value as an input, but when you submit the metrics value in the DeviceMetrics report, you must pass it as an array with a single value.
        :param display_name: The friendly name in the console for the custom metric. This name doesn't have to be unique. Don't use this name as the metric identifier in the device metric report. You can update the friendly name after you define it.
        :param metric_name: The name of the custom metric. This will be used in the metric report submitted from the device/thing. The name can't begin with ``aws:`` . You can’t change the name after you define it.
        :param tags: Metadata that can be used to manage the custom metric.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ea99b45b7f4b56d3965922a562b9ad71ff1af6ad29be5d45c88d8debae4deb6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCustomMetricProps(
            metric_type=metric_type,
            display_name=display_name,
            metric_name=metric_name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f569eb8d969344bcec4d01cb0b2775e98604ae5a5f85f4ffc0a5642c5f39fc06)
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
            type_hints = typing.get_type_hints(_typecheckingstub__18fc78138538df0f68c3687920dc04a2e8b5626aa90bd1fcce08d903c519a136)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrMetricArn")
    def attr_metric_arn(self) -> builtins.str:
        '''The Amazon Resource Number (ARN) of the custom metric;

        for example, ``arn: *aws-partition* :iot: *region* : *accountId* :custommetric/ *metricName*`` .

        :cloudformationAttribute: MetricArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMetricArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''Metadata that can be used to manage the custom metric.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-custommetric.html#cfn-iot-custommetric-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="metricType")
    def metric_type(self) -> builtins.str:
        '''The type of the custom metric. Types include ``string-list`` , ``ip-address-list`` , ``number-list`` , and ``number`` .

        .. epigraph::

           The type ``number`` only takes a single metric value as an input, but when you submit the metrics value in the DeviceMetrics report, you must pass it as an array with a single value.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-custommetric.html#cfn-iot-custommetric-metrictype
        '''
        return typing.cast(builtins.str, jsii.get(self, "metricType"))

    @metric_type.setter
    def metric_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52cf83af158df69ae1246e2607320bd9bef859fba73ad0d6703c9d4d039f621e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricType", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The friendly name in the console for the custom metric.

        This name doesn't have to be unique. Don't use this name as the metric identifier in the device metric report. You can update the friendly name after you define it.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-custommetric.html#cfn-iot-custommetric-displayname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0932a4b138ed9513bfaccdd46b9debcb30c9dffb4a8f0baaaac56cafb0795e40)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> typing.Optional[builtins.str]:
        '''The name of the custom metric.

        This will be used in the metric report submitted from the device/thing. The name can't begin with ``aws:`` . You can’t change the name after you define it.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-custommetric.html#cfn-iot-custommetric-metricname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricName"))

    @metric_name.setter
    def metric_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6ce0019127a4adfdec183be6e19c979df1164122220af4f789c14159654dc10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricName", value)


@jsii.data_type(
    jsii_type="monocdk.aws_iot.CfnCustomMetricProps",
    jsii_struct_bases=[],
    name_mapping={
        "metric_type": "metricType",
        "display_name": "displayName",
        "metric_name": "metricName",
        "tags": "tags",
    },
)
class CfnCustomMetricProps:
    def __init__(
        self,
        *,
        metric_type: builtins.str,
        display_name: typing.Optional[builtins.str] = None,
        metric_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCustomMetric``.

        :param metric_type: The type of the custom metric. Types include ``string-list`` , ``ip-address-list`` , ``number-list`` , and ``number`` . .. epigraph:: The type ``number`` only takes a single metric value as an input, but when you submit the metrics value in the DeviceMetrics report, you must pass it as an array with a single value.
        :param display_name: The friendly name in the console for the custom metric. This name doesn't have to be unique. Don't use this name as the metric identifier in the device metric report. You can update the friendly name after you define it.
        :param metric_name: The name of the custom metric. This will be used in the metric report submitted from the device/thing. The name can't begin with ``aws:`` . You can’t change the name after you define it.
        :param tags: Metadata that can be used to manage the custom metric.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-custommetric.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_iot as iot
            
            cfn_custom_metric_props = iot.CfnCustomMetricProps(
                metric_type="metricType",
            
                # the properties below are optional
                display_name="displayName",
                metric_name="metricName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb4d6cbddb71e9e4cd4bd3f81a22d7fcd9a82141828d5d7d2ef317843439dca0)
            check_type(argname="argument metric_type", value=metric_type, expected_type=type_hints["metric_type"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metric_type": metric_type,
        }
        if display_name is not None:
            self._values["display_name"] = display_name
        if metric_name is not None:
            self._values["metric_name"] = metric_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def metric_type(self) -> builtins.str:
        '''The type of the custom metric. Types include ``string-list`` , ``ip-address-list`` , ``number-list`` , and ``number`` .

        .. epigraph::

           The type ``number`` only takes a single metric value as an input, but when you submit the metrics value in the DeviceMetrics report, you must pass it as an array with a single value.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-custommetric.html#cfn-iot-custommetric-metrictype
        '''
        result = self._values.get("metric_type")
        assert result is not None, "Required property 'metric_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The friendly name in the console for the custom metric.

        This name doesn't have to be unique. Don't use this name as the metric identifier in the device metric report. You can update the friendly name after you define it.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-custommetric.html#cfn-iot-custommetric-displayname
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metric_name(self) -> typing.Optional[builtins.str]:
        '''The name of the custom metric.

        This will be used in the metric report submitted from the device/thing. The name can't begin with ``aws:`` . You can’t change the name after you define it.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-custommetric.html#cfn-iot-custommetric-metricname
        '''
        result = self._values.get("metric_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''Metadata that can be used to manage the custom metric.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-custommetric.html#cfn-iot-custommetric-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCustomMetricProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnDimension(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iot.CfnDimension",
):
    '''A CloudFormation ``AWS::IoT::Dimension``.

    Use the ``AWS::IoT::Dimension`` to limit the scope of a metric used in a security profile for AWS IoT Device Defender . For example, using a ``TOPIC_FILTER`` dimension, you can narrow down the scope of the metric to only MQTT topics where the name matches the pattern specified in the dimension. For API reference, see `CreateDimension <https://docs.aws.amazon.com/iot/latest/apireference/API_CreateDimension.html>`_ and for general information, see `Scoping metrics in security profiles using dimensions <https://docs.aws.amazon.com/iot/latest/developerguide/scoping-security-behavior.html>`_ .

    :cloudformationResource: AWS::IoT::Dimension
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-dimension.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_iot as iot
        
        cfn_dimension = iot.CfnDimension(self, "MyCfnDimension",
            string_values=["stringValues"],
            type="type",
        
            # the properties below are optional
            name="name",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        string_values: typing.Sequence[builtins.str],
        type: builtins.str,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::IoT::Dimension``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param string_values: Specifies the value or list of values for the dimension. For ``TOPIC_FILTER`` dimensions, this is a pattern used to match the MQTT topic (for example, "admin/#").
        :param type: Specifies the type of dimension. Supported types: ``TOPIC_FILTER.``
        :param name: A unique identifier for the dimension.
        :param tags: Metadata that can be used to manage the dimension.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06cf84da0cf82ce58aef400445e90ce286914282b92497e27bc27c69be795834)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDimensionProps(
            string_values=string_values, type=type, name=name, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c25a23adb0e23c44f82ad046f58d62744b1b141804301e90c514f4af28693af0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__33ea8897257f3f21768f39fe1a097709c45600ec87e3d67741d9510433ce1a0f)
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
        '''The Amazon Resource Name (ARN) of the dimension.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''Metadata that can be used to manage the dimension.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-dimension.html#cfn-iot-dimension-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="stringValues")
    def string_values(self) -> typing.List[builtins.str]:
        '''Specifies the value or list of values for the dimension.

        For ``TOPIC_FILTER`` dimensions, this is a pattern used to match the MQTT topic (for example, "admin/#").

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-dimension.html#cfn-iot-dimension-stringvalues
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "stringValues"))

    @string_values.setter
    def string_values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c087f199ff4686daadad3cc62a699572c85b7257381085a3e302cbc6d3d28145)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stringValues", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''Specifies the type of dimension.

        Supported types: ``TOPIC_FILTER.``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-dimension.html#cfn-iot-dimension-type
        '''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbe1bf77dbcf6fa1a7326d35cffb405a6f5d9b361a01766b98cfc7965970ffc1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''A unique identifier for the dimension.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-dimension.html#cfn-iot-dimension-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__726401c262fbc85fa8a1847cfdcdf3513dc239b04f530b6cdbaa51a0827644a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="monocdk.aws_iot.CfnDimensionProps",
    jsii_struct_bases=[],
    name_mapping={
        "string_values": "stringValues",
        "type": "type",
        "name": "name",
        "tags": "tags",
    },
)
class CfnDimensionProps:
    def __init__(
        self,
        *,
        string_values: typing.Sequence[builtins.str],
        type: builtins.str,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDimension``.

        :param string_values: Specifies the value or list of values for the dimension. For ``TOPIC_FILTER`` dimensions, this is a pattern used to match the MQTT topic (for example, "admin/#").
        :param type: Specifies the type of dimension. Supported types: ``TOPIC_FILTER.``
        :param name: A unique identifier for the dimension.
        :param tags: Metadata that can be used to manage the dimension.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-dimension.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_iot as iot
            
            cfn_dimension_props = iot.CfnDimensionProps(
                string_values=["stringValues"],
                type="type",
            
                # the properties below are optional
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35ce00723e902f0b46065ca937def6947b708a0431cf4d5729f5fb988ed12309)
            check_type(argname="argument string_values", value=string_values, expected_type=type_hints["string_values"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "string_values": string_values,
            "type": type,
        }
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def string_values(self) -> typing.List[builtins.str]:
        '''Specifies the value or list of values for the dimension.

        For ``TOPIC_FILTER`` dimensions, this is a pattern used to match the MQTT topic (for example, "admin/#").

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-dimension.html#cfn-iot-dimension-stringvalues
        '''
        result = self._values.get("string_values")
        assert result is not None, "Required property 'string_values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Specifies the type of dimension.

        Supported types: ``TOPIC_FILTER.``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-dimension.html#cfn-iot-dimension-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''A unique identifier for the dimension.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-dimension.html#cfn-iot-dimension-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''Metadata that can be used to manage the dimension.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-dimension.html#cfn-iot-dimension-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDimensionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnDomainConfiguration(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iot.CfnDomainConfiguration",
):
    '''A CloudFormation ``AWS::IoT::DomainConfiguration``.

    Specifies a domain configuration.

    :cloudformationResource: AWS::IoT::DomainConfiguration
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_iot as iot
        
        cfn_domain_configuration = iot.CfnDomainConfiguration(self, "MyCfnDomainConfiguration",
            authorizer_config=iot.CfnDomainConfiguration.AuthorizerConfigProperty(
                allow_authorizer_override=False,
                default_authorizer_name="defaultAuthorizerName"
            ),
            domain_configuration_name="domainConfigurationName",
            domain_configuration_status="domainConfigurationStatus",
            domain_name="domainName",
            server_certificate_arns=["serverCertificateArns"],
            service_type="serviceType",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            validation_certificate_arn="validationCertificateArn"
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        authorizer_config: typing.Optional[typing.Union[typing.Union["CfnDomainConfiguration.AuthorizerConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        domain_configuration_name: typing.Optional[builtins.str] = None,
        domain_configuration_status: typing.Optional[builtins.str] = None,
        domain_name: typing.Optional[builtins.str] = None,
        server_certificate_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        service_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
        validation_certificate_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::IoT::DomainConfiguration``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param authorizer_config: An object that specifies the authorization service for a domain.
        :param domain_configuration_name: The name of the domain configuration. This value must be unique to a region.
        :param domain_configuration_status: The status to which the domain configuration should be updated. Valid values: ``ENABLED`` | ``DISABLED``
        :param domain_name: The name of the domain.
        :param server_certificate_arns: The ARNs of the certificates that AWS IoT passes to the device during the TLS handshake. Currently you can specify only one certificate ARN. This value is not required for AWS -managed domains.
        :param service_type: The type of service delivered by the endpoint. .. epigraph:: AWS IoT Core currently supports only the ``DATA`` service type.
        :param tags: Metadata which can be used to manage the domain configuration. .. epigraph:: For URI Request parameters use format: ...key1=value1&key2=value2... For the CLI command-line parameter use format: &&tags "key1=value1&key2=value2..." For the cli-input-json file use format: "tags": "key1=value1&key2=value2..."
        :param validation_certificate_arn: The certificate used to validate the server certificate and prove domain name ownership. This certificate must be signed by a public certificate authority. This value is not required for AWS -managed domains.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4f77b2d0d9579ebb455828dc3cede63a5e9e426f72891eb5acf208c94094670)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDomainConfigurationProps(
            authorizer_config=authorizer_config,
            domain_configuration_name=domain_configuration_name,
            domain_configuration_status=domain_configuration_status,
            domain_name=domain_name,
            server_certificate_arns=server_certificate_arns,
            service_type=service_type,
            tags=tags,
            validation_certificate_arn=validation_certificate_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34424cba98d5fd002279af60091cebece661a02a2e54b47c3eba5b7a5dacaeaa)
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
            type_hints = typing.get_type_hints(_typecheckingstub__07fcd6f026b661c3afb848e58ae51d238faf4b3a1300829c3bc024ac176fc30a)
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
        '''The Amazon Resource Name (ARN) of the domain configuration.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainType")
    def attr_domain_type(self) -> builtins.str:
        '''The type of service delivered by the domain.

        :cloudformationAttribute: DomainType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainType"))

    @builtins.property
    @jsii.member(jsii_name="attrServerCertificates")
    def attr_server_certificates(self) -> _IResolvable_a771d0ef:
        '''The ARNs of the certificates that AWS IoT passes to the device during the TLS handshake.

        Currently you can specify only one certificate ARN. This value is not required for AWS -managed domains.

        :cloudformationAttribute: ServerCertificates
        '''
        return typing.cast(_IResolvable_a771d0ef, jsii.get(self, "attrServerCertificates"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''Metadata which can be used to manage the domain configuration.

        .. epigraph::

           For URI Request parameters use format: ...key1=value1&key2=value2...

           For the CLI command-line parameter use format: &&tags "key1=value1&key2=value2..."

           For the cli-input-json file use format: "tags": "key1=value1&key2=value2..."

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html#cfn-iot-domainconfiguration-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="authorizerConfig")
    def authorizer_config(
        self,
    ) -> typing.Optional[typing.Union["CfnDomainConfiguration.AuthorizerConfigProperty", _IResolvable_a771d0ef]]:
        '''An object that specifies the authorization service for a domain.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html#cfn-iot-domainconfiguration-authorizerconfig
        '''
        return typing.cast(typing.Optional[typing.Union["CfnDomainConfiguration.AuthorizerConfigProperty", _IResolvable_a771d0ef]], jsii.get(self, "authorizerConfig"))

    @authorizer_config.setter
    def authorizer_config(
        self,
        value: typing.Optional[typing.Union["CfnDomainConfiguration.AuthorizerConfigProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07a2dc93550cbb719e30317479efbaf401d6aa9e4eba1935f757a30cb5b1afbc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizerConfig", value)

    @builtins.property
    @jsii.member(jsii_name="domainConfigurationName")
    def domain_configuration_name(self) -> typing.Optional[builtins.str]:
        '''The name of the domain configuration.

        This value must be unique to a region.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html#cfn-iot-domainconfiguration-domainconfigurationname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainConfigurationName"))

    @domain_configuration_name.setter
    def domain_configuration_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecdc2464d6dc7099fc1ac686164ade1ef8263473dd0c70cb18cff7ef3ab38923)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainConfigurationName", value)

    @builtins.property
    @jsii.member(jsii_name="domainConfigurationStatus")
    def domain_configuration_status(self) -> typing.Optional[builtins.str]:
        '''The status to which the domain configuration should be updated.

        Valid values: ``ENABLED`` | ``DISABLED``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html#cfn-iot-domainconfiguration-domainconfigurationstatus
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainConfigurationStatus"))

    @domain_configuration_status.setter
    def domain_configuration_status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6062d91a52a6e2f058bb8256a4994bec069946dad4e76a471846a8204c1019b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainConfigurationStatus", value)

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> typing.Optional[builtins.str]:
        '''The name of the domain.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html#cfn-iot-domainconfiguration-domainname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f138275dee3bc63e590defd3487ad6f8b6085c1702af336923fe0aa9d9cb248)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="serverCertificateArns")
    def server_certificate_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The ARNs of the certificates that AWS IoT passes to the device during the TLS handshake.

        Currently you can specify only one certificate ARN. This value is not required for AWS -managed domains.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html#cfn-iot-domainconfiguration-servercertificatearns
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "serverCertificateArns"))

    @server_certificate_arns.setter
    def server_certificate_arns(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fcbea10657987047afcf50b0f211e74045a25f552d465fc9a5e7ad20eebd1969)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverCertificateArns", value)

    @builtins.property
    @jsii.member(jsii_name="serviceType")
    def service_type(self) -> typing.Optional[builtins.str]:
        '''The type of service delivered by the endpoint.

        .. epigraph::

           AWS IoT Core currently supports only the ``DATA`` service type.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html#cfn-iot-domainconfiguration-servicetype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceType"))

    @service_type.setter
    def service_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89a2a17569b2ea82a87615d93e454e41d3a84e5f951b37939309842676fbaaa4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceType", value)

    @builtins.property
    @jsii.member(jsii_name="validationCertificateArn")
    def validation_certificate_arn(self) -> typing.Optional[builtins.str]:
        '''The certificate used to validate the server certificate and prove domain name ownership.

        This certificate must be signed by a public certificate authority. This value is not required for AWS -managed domains.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html#cfn-iot-domainconfiguration-validationcertificatearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "validationCertificateArn"))

    @validation_certificate_arn.setter
    def validation_certificate_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b55e1c672780e2e7b9130eb08180bbc14d2d64b47fd5cc880e9fdcff204d7cc3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "validationCertificateArn", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnDomainConfiguration.AuthorizerConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "allow_authorizer_override": "allowAuthorizerOverride",
            "default_authorizer_name": "defaultAuthorizerName",
        },
    )
    class AuthorizerConfigProperty:
        def __init__(
            self,
            *,
            allow_authorizer_override: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            default_authorizer_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An object that specifies the authorization service for a domain.

            :param allow_authorizer_override: A Boolean that specifies whether the domain configuration's authorization service can be overridden.
            :param default_authorizer_name: The name of the authorization service for a domain configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-domainconfiguration-authorizerconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                authorizer_config_property = iot.CfnDomainConfiguration.AuthorizerConfigProperty(
                    allow_authorizer_override=False,
                    default_authorizer_name="defaultAuthorizerName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a314a31439fda332ad90d8941379d5aa35f6979ccdd689ec7da0a1c8273b0b88)
                check_type(argname="argument allow_authorizer_override", value=allow_authorizer_override, expected_type=type_hints["allow_authorizer_override"])
                check_type(argname="argument default_authorizer_name", value=default_authorizer_name, expected_type=type_hints["default_authorizer_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if allow_authorizer_override is not None:
                self._values["allow_authorizer_override"] = allow_authorizer_override
            if default_authorizer_name is not None:
                self._values["default_authorizer_name"] = default_authorizer_name

        @builtins.property
        def allow_authorizer_override(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''A Boolean that specifies whether the domain configuration's authorization service can be overridden.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-domainconfiguration-authorizerconfig.html#cfn-iot-domainconfiguration-authorizerconfig-allowauthorizeroverride
            '''
            result = self._values.get("allow_authorizer_override")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def default_authorizer_name(self) -> typing.Optional[builtins.str]:
            '''The name of the authorization service for a domain configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-domainconfiguration-authorizerconfig.html#cfn-iot-domainconfiguration-authorizerconfig-defaultauthorizername
            '''
            result = self._values.get("default_authorizer_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthorizerConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnDomainConfiguration.ServerCertificateSummaryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "server_certificate_arn": "serverCertificateArn",
            "server_certificate_status": "serverCertificateStatus",
            "server_certificate_status_detail": "serverCertificateStatusDetail",
        },
    )
    class ServerCertificateSummaryProperty:
        def __init__(
            self,
            *,
            server_certificate_arn: typing.Optional[builtins.str] = None,
            server_certificate_status: typing.Optional[builtins.str] = None,
            server_certificate_status_detail: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An object that contains information about a server certificate.

            :param server_certificate_arn: The ARN of the server certificate.
            :param server_certificate_status: The status of the server certificate.
            :param server_certificate_status_detail: Details that explain the status of the server certificate.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-domainconfiguration-servercertificatesummary.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                server_certificate_summary_property = iot.CfnDomainConfiguration.ServerCertificateSummaryProperty(
                    server_certificate_arn="serverCertificateArn",
                    server_certificate_status="serverCertificateStatus",
                    server_certificate_status_detail="serverCertificateStatusDetail"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a5998b48e54d6ca703ebea656a326aec99045f8a75952682ec6d44a4acbfd566)
                check_type(argname="argument server_certificate_arn", value=server_certificate_arn, expected_type=type_hints["server_certificate_arn"])
                check_type(argname="argument server_certificate_status", value=server_certificate_status, expected_type=type_hints["server_certificate_status"])
                check_type(argname="argument server_certificate_status_detail", value=server_certificate_status_detail, expected_type=type_hints["server_certificate_status_detail"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if server_certificate_arn is not None:
                self._values["server_certificate_arn"] = server_certificate_arn
            if server_certificate_status is not None:
                self._values["server_certificate_status"] = server_certificate_status
            if server_certificate_status_detail is not None:
                self._values["server_certificate_status_detail"] = server_certificate_status_detail

        @builtins.property
        def server_certificate_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the server certificate.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-domainconfiguration-servercertificatesummary.html#cfn-iot-domainconfiguration-servercertificatesummary-servercertificatearn
            '''
            result = self._values.get("server_certificate_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def server_certificate_status(self) -> typing.Optional[builtins.str]:
            '''The status of the server certificate.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-domainconfiguration-servercertificatesummary.html#cfn-iot-domainconfiguration-servercertificatesummary-servercertificatestatus
            '''
            result = self._values.get("server_certificate_status")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def server_certificate_status_detail(self) -> typing.Optional[builtins.str]:
            '''Details that explain the status of the server certificate.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-domainconfiguration-servercertificatesummary.html#cfn-iot-domainconfiguration-servercertificatesummary-servercertificatestatusdetail
            '''
            result = self._values.get("server_certificate_status_detail")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServerCertificateSummaryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_iot.CfnDomainConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "authorizer_config": "authorizerConfig",
        "domain_configuration_name": "domainConfigurationName",
        "domain_configuration_status": "domainConfigurationStatus",
        "domain_name": "domainName",
        "server_certificate_arns": "serverCertificateArns",
        "service_type": "serviceType",
        "tags": "tags",
        "validation_certificate_arn": "validationCertificateArn",
    },
)
class CfnDomainConfigurationProps:
    def __init__(
        self,
        *,
        authorizer_config: typing.Optional[typing.Union[typing.Union[CfnDomainConfiguration.AuthorizerConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        domain_configuration_name: typing.Optional[builtins.str] = None,
        domain_configuration_status: typing.Optional[builtins.str] = None,
        domain_name: typing.Optional[builtins.str] = None,
        server_certificate_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        service_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
        validation_certificate_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnDomainConfiguration``.

        :param authorizer_config: An object that specifies the authorization service for a domain.
        :param domain_configuration_name: The name of the domain configuration. This value must be unique to a region.
        :param domain_configuration_status: The status to which the domain configuration should be updated. Valid values: ``ENABLED`` | ``DISABLED``
        :param domain_name: The name of the domain.
        :param server_certificate_arns: The ARNs of the certificates that AWS IoT passes to the device during the TLS handshake. Currently you can specify only one certificate ARN. This value is not required for AWS -managed domains.
        :param service_type: The type of service delivered by the endpoint. .. epigraph:: AWS IoT Core currently supports only the ``DATA`` service type.
        :param tags: Metadata which can be used to manage the domain configuration. .. epigraph:: For URI Request parameters use format: ...key1=value1&key2=value2... For the CLI command-line parameter use format: &&tags "key1=value1&key2=value2..." For the cli-input-json file use format: "tags": "key1=value1&key2=value2..."
        :param validation_certificate_arn: The certificate used to validate the server certificate and prove domain name ownership. This certificate must be signed by a public certificate authority. This value is not required for AWS -managed domains.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_iot as iot
            
            cfn_domain_configuration_props = iot.CfnDomainConfigurationProps(
                authorizer_config=iot.CfnDomainConfiguration.AuthorizerConfigProperty(
                    allow_authorizer_override=False,
                    default_authorizer_name="defaultAuthorizerName"
                ),
                domain_configuration_name="domainConfigurationName",
                domain_configuration_status="domainConfigurationStatus",
                domain_name="domainName",
                server_certificate_arns=["serverCertificateArns"],
                service_type="serviceType",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                validation_certificate_arn="validationCertificateArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9791be0b7126c5317bb6533c36262b9258afd7e1638de38299ba4e4db3f0d75)
            check_type(argname="argument authorizer_config", value=authorizer_config, expected_type=type_hints["authorizer_config"])
            check_type(argname="argument domain_configuration_name", value=domain_configuration_name, expected_type=type_hints["domain_configuration_name"])
            check_type(argname="argument domain_configuration_status", value=domain_configuration_status, expected_type=type_hints["domain_configuration_status"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument server_certificate_arns", value=server_certificate_arns, expected_type=type_hints["server_certificate_arns"])
            check_type(argname="argument service_type", value=service_type, expected_type=type_hints["service_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument validation_certificate_arn", value=validation_certificate_arn, expected_type=type_hints["validation_certificate_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if authorizer_config is not None:
            self._values["authorizer_config"] = authorizer_config
        if domain_configuration_name is not None:
            self._values["domain_configuration_name"] = domain_configuration_name
        if domain_configuration_status is not None:
            self._values["domain_configuration_status"] = domain_configuration_status
        if domain_name is not None:
            self._values["domain_name"] = domain_name
        if server_certificate_arns is not None:
            self._values["server_certificate_arns"] = server_certificate_arns
        if service_type is not None:
            self._values["service_type"] = service_type
        if tags is not None:
            self._values["tags"] = tags
        if validation_certificate_arn is not None:
            self._values["validation_certificate_arn"] = validation_certificate_arn

    @builtins.property
    def authorizer_config(
        self,
    ) -> typing.Optional[typing.Union[CfnDomainConfiguration.AuthorizerConfigProperty, _IResolvable_a771d0ef]]:
        '''An object that specifies the authorization service for a domain.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html#cfn-iot-domainconfiguration-authorizerconfig
        '''
        result = self._values.get("authorizer_config")
        return typing.cast(typing.Optional[typing.Union[CfnDomainConfiguration.AuthorizerConfigProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def domain_configuration_name(self) -> typing.Optional[builtins.str]:
        '''The name of the domain configuration.

        This value must be unique to a region.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html#cfn-iot-domainconfiguration-domainconfigurationname
        '''
        result = self._values.get("domain_configuration_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain_configuration_status(self) -> typing.Optional[builtins.str]:
        '''The status to which the domain configuration should be updated.

        Valid values: ``ENABLED`` | ``DISABLED``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html#cfn-iot-domainconfiguration-domainconfigurationstatus
        '''
        result = self._values.get("domain_configuration_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain_name(self) -> typing.Optional[builtins.str]:
        '''The name of the domain.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html#cfn-iot-domainconfiguration-domainname
        '''
        result = self._values.get("domain_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_certificate_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The ARNs of the certificates that AWS IoT passes to the device during the TLS handshake.

        Currently you can specify only one certificate ARN. This value is not required for AWS -managed domains.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html#cfn-iot-domainconfiguration-servercertificatearns
        '''
        result = self._values.get("server_certificate_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def service_type(self) -> typing.Optional[builtins.str]:
        '''The type of service delivered by the endpoint.

        .. epigraph::

           AWS IoT Core currently supports only the ``DATA`` service type.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html#cfn-iot-domainconfiguration-servicetype
        '''
        result = self._values.get("service_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''Metadata which can be used to manage the domain configuration.

        .. epigraph::

           For URI Request parameters use format: ...key1=value1&key2=value2...

           For the CLI command-line parameter use format: &&tags "key1=value1&key2=value2..."

           For the cli-input-json file use format: "tags": "key1=value1&key2=value2..."

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html#cfn-iot-domainconfiguration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    @builtins.property
    def validation_certificate_arn(self) -> typing.Optional[builtins.str]:
        '''The certificate used to validate the server certificate and prove domain name ownership.

        This certificate must be signed by a public certificate authority. This value is not required for AWS -managed domains.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-domainconfiguration.html#cfn-iot-domainconfiguration-validationcertificatearn
        '''
        result = self._values.get("validation_certificate_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDomainConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnFleetMetric(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iot.CfnFleetMetric",
):
    '''A CloudFormation ``AWS::IoT::FleetMetric``.

    Use the ``AWS::IoT::FleetMetric`` resource to declare a fleet metric.

    :cloudformationResource: AWS::IoT::FleetMetric
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_iot as iot
        
        cfn_fleet_metric = iot.CfnFleetMetric(self, "MyCfnFleetMetric",
            metric_name="metricName",
        
            # the properties below are optional
            aggregation_field="aggregationField",
            aggregation_type=iot.CfnFleetMetric.AggregationTypeProperty(
                name="name",
                values=["values"]
            ),
            description="description",
            index_name="indexName",
            period=123,
            query_string="queryString",
            query_version="queryVersion",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            unit="unit"
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        metric_name: builtins.str,
        aggregation_field: typing.Optional[builtins.str] = None,
        aggregation_type: typing.Optional[typing.Union[typing.Union["CfnFleetMetric.AggregationTypeProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        description: typing.Optional[builtins.str] = None,
        index_name: typing.Optional[builtins.str] = None,
        period: typing.Optional[jsii.Number] = None,
        query_string: typing.Optional[builtins.str] = None,
        query_version: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
        unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::IoT::FleetMetric``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param metric_name: The name of the fleet metric to create.
        :param aggregation_field: The field to aggregate.
        :param aggregation_type: The type of the aggregation query.
        :param description: The fleet metric description.
        :param index_name: The name of the index to search.
        :param period: The time in seconds between fleet metric emissions. Range [60(1 min), 86400(1 day)] and must be multiple of 60.
        :param query_string: The search query string.
        :param query_version: The query version.
        :param tags: Metadata which can be used to manage the fleet metric.
        :param unit: Used to support unit transformation such as milliseconds to seconds. Must be a unit supported by CW metric. Default to null.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ad7e60f88b12c0a66362e3e5f6010339fff15ed323c0cc55f68167135b10788)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFleetMetricProps(
            metric_name=metric_name,
            aggregation_field=aggregation_field,
            aggregation_type=aggregation_type,
            description=description,
            index_name=index_name,
            period=period,
            query_string=query_string,
            query_version=query_version,
            tags=tags,
            unit=unit,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5fd8d0171814851db4c44c37a7cce6b5112c531f2a57b44b2b0725ecdc1aad6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9dcfaf66d471bdea96f603e58143c22b32b0d0dbe6aa413418a339677e02144c)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationDate")
    def attr_creation_date(self) -> _IResolvable_a771d0ef:
        '''The time the fleet metric was created.

        :cloudformationAttribute: CreationDate
        '''
        return typing.cast(_IResolvable_a771d0ef, jsii.get(self, "attrCreationDate"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModifiedDate")
    def attr_last_modified_date(self) -> _IResolvable_a771d0ef:
        '''The time the fleet metric was last modified.

        :cloudformationAttribute: LastModifiedDate
        '''
        return typing.cast(_IResolvable_a771d0ef, jsii.get(self, "attrLastModifiedDate"))

    @builtins.property
    @jsii.member(jsii_name="attrMetricArn")
    def attr_metric_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the fleet metric.

        :cloudformationAttribute: MetricArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMetricArn"))

    @builtins.property
    @jsii.member(jsii_name="attrVersion")
    def attr_version(self) -> _IResolvable_a771d0ef:
        '''The fleet metric version.

        :cloudformationAttribute: Version
        '''
        return typing.cast(_IResolvable_a771d0ef, jsii.get(self, "attrVersion"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''Metadata which can be used to manage the fleet metric.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> builtins.str:
        '''The name of the fleet metric to create.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-metricname
        '''
        return typing.cast(builtins.str, jsii.get(self, "metricName"))

    @metric_name.setter
    def metric_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c2acbeff787ff877313a4ec2b95574d5a80949dd269a985b73d741b3c3192af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricName", value)

    @builtins.property
    @jsii.member(jsii_name="aggregationField")
    def aggregation_field(self) -> typing.Optional[builtins.str]:
        '''The field to aggregate.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-aggregationfield
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aggregationField"))

    @aggregation_field.setter
    def aggregation_field(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bb211b4b5a3eadbe0f3fb4e0370e939c47a91571a3f01c506b69752c96140e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aggregationField", value)

    @builtins.property
    @jsii.member(jsii_name="aggregationType")
    def aggregation_type(
        self,
    ) -> typing.Optional[typing.Union["CfnFleetMetric.AggregationTypeProperty", _IResolvable_a771d0ef]]:
        '''The type of the aggregation query.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-aggregationtype
        '''
        return typing.cast(typing.Optional[typing.Union["CfnFleetMetric.AggregationTypeProperty", _IResolvable_a771d0ef]], jsii.get(self, "aggregationType"))

    @aggregation_type.setter
    def aggregation_type(
        self,
        value: typing.Optional[typing.Union["CfnFleetMetric.AggregationTypeProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13472d3409b3845c68e55be14fcfe88a7e42fb4a57e4df346da4c2046a1b594f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aggregationType", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The fleet metric description.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11466b926632a4d4bebd6f7a6062d9e2d4e16acc6d4259a5533c3a286abb8595)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="indexName")
    def index_name(self) -> typing.Optional[builtins.str]:
        '''The name of the index to search.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-indexname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "indexName"))

    @index_name.setter
    def index_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__874b92f83a08a65e8cc0d4dbe5bfb269348a7620899708b590194410ca10a5ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "indexName", value)

    @builtins.property
    @jsii.member(jsii_name="period")
    def period(self) -> typing.Optional[jsii.Number]:
        '''The time in seconds between fleet metric emissions.

        Range [60(1 min), 86400(1 day)] and must be multiple of 60.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-period
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "period"))

    @period.setter
    def period(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__974d067c0c4aaabbb36191bcb265cdaa6d9b88edd52d590299a61217391f4075)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "period", value)

    @builtins.property
    @jsii.member(jsii_name="queryString")
    def query_string(self) -> typing.Optional[builtins.str]:
        '''The search query string.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-querystring
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryString"))

    @query_string.setter
    def query_string(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22a291e38e3fca078dbafcd8da2d1d570e3347e1484b5b65a4de3539555f7d61)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryString", value)

    @builtins.property
    @jsii.member(jsii_name="queryVersion")
    def query_version(self) -> typing.Optional[builtins.str]:
        '''The query version.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-queryversion
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryVersion"))

    @query_version.setter
    def query_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e957fe630fd8a4b4978a61b8230963d24324584aadc323d51dd4a1fb10b4012b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryVersion", value)

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> typing.Optional[builtins.str]:
        '''Used to support unit transformation such as milliseconds to seconds.

        Must be a unit supported by CW metric. Default to null.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-unit
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec8c2b0c7f95ad810c55a87aaddd01070aa123237f8c594e93d1d0109dd2331e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnFleetMetric.AggregationTypeProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "values": "values"},
    )
    class AggregationTypeProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            values: typing.Sequence[builtins.str],
        ) -> None:
            '''The type of aggregation queries.

            :param name: The name of the aggregation type.
            :param values: A list of the values of aggregation types.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-fleetmetric-aggregationtype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                aggregation_type_property = iot.CfnFleetMetric.AggregationTypeProperty(
                    name="name",
                    values=["values"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f65e968ba2f22b03f2813acc234863e0e6865868c95bdf069bb4471b58f584d6)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "values": values,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the aggregation type.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-fleetmetric-aggregationtype.html#cfn-iot-fleetmetric-aggregationtype-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def values(self) -> typing.List[builtins.str]:
            '''A list of the values of aggregation types.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-fleetmetric-aggregationtype.html#cfn-iot-fleetmetric-aggregationtype-values
            '''
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AggregationTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_iot.CfnFleetMetricProps",
    jsii_struct_bases=[],
    name_mapping={
        "metric_name": "metricName",
        "aggregation_field": "aggregationField",
        "aggregation_type": "aggregationType",
        "description": "description",
        "index_name": "indexName",
        "period": "period",
        "query_string": "queryString",
        "query_version": "queryVersion",
        "tags": "tags",
        "unit": "unit",
    },
)
class CfnFleetMetricProps:
    def __init__(
        self,
        *,
        metric_name: builtins.str,
        aggregation_field: typing.Optional[builtins.str] = None,
        aggregation_type: typing.Optional[typing.Union[typing.Union[CfnFleetMetric.AggregationTypeProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        description: typing.Optional[builtins.str] = None,
        index_name: typing.Optional[builtins.str] = None,
        period: typing.Optional[jsii.Number] = None,
        query_string: typing.Optional[builtins.str] = None,
        query_version: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
        unit: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnFleetMetric``.

        :param metric_name: The name of the fleet metric to create.
        :param aggregation_field: The field to aggregate.
        :param aggregation_type: The type of the aggregation query.
        :param description: The fleet metric description.
        :param index_name: The name of the index to search.
        :param period: The time in seconds between fleet metric emissions. Range [60(1 min), 86400(1 day)] and must be multiple of 60.
        :param query_string: The search query string.
        :param query_version: The query version.
        :param tags: Metadata which can be used to manage the fleet metric.
        :param unit: Used to support unit transformation such as milliseconds to seconds. Must be a unit supported by CW metric. Default to null.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_iot as iot
            
            cfn_fleet_metric_props = iot.CfnFleetMetricProps(
                metric_name="metricName",
            
                # the properties below are optional
                aggregation_field="aggregationField",
                aggregation_type=iot.CfnFleetMetric.AggregationTypeProperty(
                    name="name",
                    values=["values"]
                ),
                description="description",
                index_name="indexName",
                period=123,
                query_string="queryString",
                query_version="queryVersion",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                unit="unit"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f08a9cea47193eddb52faffb25f0135e360e21c0359b67cfe87ac3255e5ee2a)
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
            check_type(argname="argument aggregation_field", value=aggregation_field, expected_type=type_hints["aggregation_field"])
            check_type(argname="argument aggregation_type", value=aggregation_type, expected_type=type_hints["aggregation_type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument index_name", value=index_name, expected_type=type_hints["index_name"])
            check_type(argname="argument period", value=period, expected_type=type_hints["period"])
            check_type(argname="argument query_string", value=query_string, expected_type=type_hints["query_string"])
            check_type(argname="argument query_version", value=query_version, expected_type=type_hints["query_version"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metric_name": metric_name,
        }
        if aggregation_field is not None:
            self._values["aggregation_field"] = aggregation_field
        if aggregation_type is not None:
            self._values["aggregation_type"] = aggregation_type
        if description is not None:
            self._values["description"] = description
        if index_name is not None:
            self._values["index_name"] = index_name
        if period is not None:
            self._values["period"] = period
        if query_string is not None:
            self._values["query_string"] = query_string
        if query_version is not None:
            self._values["query_version"] = query_version
        if tags is not None:
            self._values["tags"] = tags
        if unit is not None:
            self._values["unit"] = unit

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''The name of the fleet metric to create.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-metricname
        '''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aggregation_field(self) -> typing.Optional[builtins.str]:
        '''The field to aggregate.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-aggregationfield
        '''
        result = self._values.get("aggregation_field")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aggregation_type(
        self,
    ) -> typing.Optional[typing.Union[CfnFleetMetric.AggregationTypeProperty, _IResolvable_a771d0ef]]:
        '''The type of the aggregation query.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-aggregationtype
        '''
        result = self._values.get("aggregation_type")
        return typing.cast(typing.Optional[typing.Union[CfnFleetMetric.AggregationTypeProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The fleet metric description.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def index_name(self) -> typing.Optional[builtins.str]:
        '''The name of the index to search.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-indexname
        '''
        result = self._values.get("index_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def period(self) -> typing.Optional[jsii.Number]:
        '''The time in seconds between fleet metric emissions.

        Range [60(1 min), 86400(1 day)] and must be multiple of 60.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-period
        '''
        result = self._values.get("period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def query_string(self) -> typing.Optional[builtins.str]:
        '''The search query string.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-querystring
        '''
        result = self._values.get("query_string")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def query_version(self) -> typing.Optional[builtins.str]:
        '''The query version.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-queryversion
        '''
        result = self._values.get("query_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''Metadata which can be used to manage the fleet metric.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    @builtins.property
    def unit(self) -> typing.Optional[builtins.str]:
        '''Used to support unit transformation such as milliseconds to seconds.

        Must be a unit supported by CW metric. Default to null.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-fleetmetric.html#cfn-iot-fleetmetric-unit
        '''
        result = self._values.get("unit")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFleetMetricProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnJobTemplate(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iot.CfnJobTemplate",
):
    '''A CloudFormation ``AWS::IoT::JobTemplate``.

    Represents a job template.

    :cloudformationResource: AWS::IoT::JobTemplate
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_iot as iot
        
        # abort_config: Any
        # job_executions_rollout_config: Any
        # presigned_url_config: Any
        # timeout_config: Any
        
        cfn_job_template = iot.CfnJobTemplate(self, "MyCfnJobTemplate",
            description="description",
            job_template_id="jobTemplateId",
        
            # the properties below are optional
            abort_config=abort_config,
            document="document",
            document_source="documentSource",
            job_arn="jobArn",
            job_executions_rollout_config=job_executions_rollout_config,
            presigned_url_config=presigned_url_config,
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            timeout_config=timeout_config
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        description: builtins.str,
        job_template_id: builtins.str,
        abort_config: typing.Any = None,
        document: typing.Optional[builtins.str] = None,
        document_source: typing.Optional[builtins.str] = None,
        job_arn: typing.Optional[builtins.str] = None,
        job_executions_rollout_config: typing.Any = None,
        presigned_url_config: typing.Any = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
        timeout_config: typing.Any = None,
    ) -> None:
        '''Create a new ``AWS::IoT::JobTemplate``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param description: A description of the job template.
        :param job_template_id: A unique identifier for the job template. We recommend using a UUID. Alpha-numeric characters, "-", and "_" are valid for use here.
        :param abort_config: The criteria that determine when and how a job abort takes place.
        :param document: The job document. Required if you don't specify a value for ``documentSource`` .
        :param document_source: An S3 link to the job document to use in the template. Required if you don't specify a value for ``document`` . .. epigraph:: If the job document resides in an S3 bucket, you must use a placeholder link when specifying the document. The placeholder link is of the following form: ``${aws:iot:s3-presigned-url:https://s3.amazonaws.com/ *bucket* / *key* }`` where *bucket* is your bucket name and *key* is the object in the bucket to which you are linking.
        :param job_arn: The ARN of the job to use as the basis for the job template.
        :param job_executions_rollout_config: Allows you to create a staged rollout of a job.
        :param presigned_url_config: Configuration for pre-signed S3 URLs.
        :param tags: Metadata that can be used to manage the job template.
        :param timeout_config: Specifies the amount of time each device has to finish its execution of the job. A timer is started when the job execution status is set to ``IN_PROGRESS`` . If the job execution status is not set to another terminal state before the timer expires, it will be automatically set to ``TIMED_OUT`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6ae87ac21ac364701bedc97923edce3167092f0de57514b10a0c7d7f61c4e43)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnJobTemplateProps(
            description=description,
            job_template_id=job_template_id,
            abort_config=abort_config,
            document=document,
            document_source=document_source,
            job_arn=job_arn,
            job_executions_rollout_config=job_executions_rollout_config,
            presigned_url_config=presigned_url_config,
            tags=tags,
            timeout_config=timeout_config,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e540bbe80561dc99a5e95510f3908cdfad3e7e800895992be55e0556eee73a02)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c714b28049fdfb5462bc15aafb30823e39213b84388ad13626d17ebcbd38b478)
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
        '''The ARN of the job to use as the basis for the job template.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''Metadata that can be used to manage the job template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="abortConfig")
    def abort_config(self) -> typing.Any:
        '''The criteria that determine when and how a job abort takes place.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-abortconfig
        '''
        return typing.cast(typing.Any, jsii.get(self, "abortConfig"))

    @abort_config.setter
    def abort_config(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0c163e2f7e3d96569821161b4db787f334aa09f0d6246b354ad47f357a6e5b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "abortConfig", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''A description of the job template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-description
        '''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6360d951d29c8c6dba1ecf345078aa3a681867bcf0eab64d409704e6b1f3ade2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="jobExecutionsRolloutConfig")
    def job_executions_rollout_config(self) -> typing.Any:
        '''Allows you to create a staged rollout of a job.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-jobexecutionsrolloutconfig
        '''
        return typing.cast(typing.Any, jsii.get(self, "jobExecutionsRolloutConfig"))

    @job_executions_rollout_config.setter
    def job_executions_rollout_config(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0582e1d8ce9cff0dd05164303eac92fa59ab15f6cada781f3b1641c1220006d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobExecutionsRolloutConfig", value)

    @builtins.property
    @jsii.member(jsii_name="jobTemplateId")
    def job_template_id(self) -> builtins.str:
        '''A unique identifier for the job template.

        We recommend using a UUID. Alpha-numeric characters, "-", and "_" are valid for use here.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-jobtemplateid
        '''
        return typing.cast(builtins.str, jsii.get(self, "jobTemplateId"))

    @job_template_id.setter
    def job_template_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a70e9489919ab2f13d25979014dca16c202289959793a22589931bbbd9a9493)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobTemplateId", value)

    @builtins.property
    @jsii.member(jsii_name="presignedUrlConfig")
    def presigned_url_config(self) -> typing.Any:
        '''Configuration for pre-signed S3 URLs.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-presignedurlconfig
        '''
        return typing.cast(typing.Any, jsii.get(self, "presignedUrlConfig"))

    @presigned_url_config.setter
    def presigned_url_config(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63ce99e49d9bcde619873266cec6f536c971497634407aca31ebe48986718e91)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "presignedUrlConfig", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutConfig")
    def timeout_config(self) -> typing.Any:
        '''Specifies the amount of time each device has to finish its execution of the job.

        A timer is started when the job execution status is set to ``IN_PROGRESS`` . If the job execution status is not set to another terminal state before the timer expires, it will be automatically set to ``TIMED_OUT`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-timeoutconfig
        '''
        return typing.cast(typing.Any, jsii.get(self, "timeoutConfig"))

    @timeout_config.setter
    def timeout_config(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6c45644e0543bf0702fa22b35d6eb5e1761ecdf1c4c83507f1816feea8e1dd0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutConfig", value)

    @builtins.property
    @jsii.member(jsii_name="document")
    def document(self) -> typing.Optional[builtins.str]:
        '''The job document.

        Required if you don't specify a value for ``documentSource`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-document
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "document"))

    @document.setter
    def document(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbd7fee843fd1c6208c7661e62a57645c563ce3bfe4977efc88e2db6e874ddc3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "document", value)

    @builtins.property
    @jsii.member(jsii_name="documentSource")
    def document_source(self) -> typing.Optional[builtins.str]:
        '''An S3 link to the job document to use in the template.

        Required if you don't specify a value for ``document`` .
        .. epigraph::

           If the job document resides in an S3 bucket, you must use a placeholder link when specifying the document.

           The placeholder link is of the following form:

           ``${aws:iot:s3-presigned-url:https://s3.amazonaws.com/ *bucket* / *key* }``

           where *bucket* is your bucket name and *key* is the object in the bucket to which you are linking.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-documentsource
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "documentSource"))

    @document_source.setter
    def document_source(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8ea3b2ce1e276358f7e126496357e5f3b42a19b6269f4b01a7d4463c7c5660e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "documentSource", value)

    @builtins.property
    @jsii.member(jsii_name="jobArn")
    def job_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the job to use as the basis for the job template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-jobarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobArn"))

    @job_arn.setter
    def job_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63edbe9554e9d577da6f373c1eea4064c9dbfcd432d5be5b4a7f776d2578ca50)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobArn", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnJobTemplate.AbortConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"criteria_list": "criteriaList"},
    )
    class AbortConfigProperty:
        def __init__(
            self,
            *,
            criteria_list: typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union["CfnJobTemplate.AbortCriteriaProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]],
        ) -> None:
            '''The criteria that determine when and how a job abort takes place.

            :param criteria_list: The list of criteria that determine when and how to abort the job.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-abortconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                abort_config_property = iot.CfnJobTemplate.AbortConfigProperty(
                    criteria_list=[iot.CfnJobTemplate.AbortCriteriaProperty(
                        action="action",
                        failure_type="failureType",
                        min_number_of_executed_things=123,
                        threshold_percentage=123
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f713fd224eae400c78a9c31920704be55aac90079a2fb14b888145dc3155489e)
                check_type(argname="argument criteria_list", value=criteria_list, expected_type=type_hints["criteria_list"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "criteria_list": criteria_list,
            }

        @builtins.property
        def criteria_list(
            self,
        ) -> typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnJobTemplate.AbortCriteriaProperty", _IResolvable_a771d0ef]]]:
            '''The list of criteria that determine when and how to abort the job.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-abortconfig.html#cfn-iot-jobtemplate-abortconfig-criterialist
            '''
            result = self._values.get("criteria_list")
            assert result is not None, "Required property 'criteria_list' is missing"
            return typing.cast(typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnJobTemplate.AbortCriteriaProperty", _IResolvable_a771d0ef]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AbortConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnJobTemplate.AbortCriteriaProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action": "action",
            "failure_type": "failureType",
            "min_number_of_executed_things": "minNumberOfExecutedThings",
            "threshold_percentage": "thresholdPercentage",
        },
    )
    class AbortCriteriaProperty:
        def __init__(
            self,
            *,
            action: builtins.str,
            failure_type: builtins.str,
            min_number_of_executed_things: jsii.Number,
            threshold_percentage: jsii.Number,
        ) -> None:
            '''The criteria that determine when and how a job abort takes place.

            :param action: The type of job action to take to initiate the job abort.
            :param failure_type: The type of job execution failures that can initiate a job abort.
            :param min_number_of_executed_things: The minimum number of things which must receive job execution notifications before the job can be aborted.
            :param threshold_percentage: The minimum percentage of job execution failures that must occur to initiate the job abort. AWS IoT Core supports up to two digits after the decimal (for example, 10.9 and 10.99, but not 10.999).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-abortcriteria.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                abort_criteria_property = iot.CfnJobTemplate.AbortCriteriaProperty(
                    action="action",
                    failure_type="failureType",
                    min_number_of_executed_things=123,
                    threshold_percentage=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f37cfdc20d16a90587cd6e9b32eaa846d03d80defc5cd35a6704fd495329de33)
                check_type(argname="argument action", value=action, expected_type=type_hints["action"])
                check_type(argname="argument failure_type", value=failure_type, expected_type=type_hints["failure_type"])
                check_type(argname="argument min_number_of_executed_things", value=min_number_of_executed_things, expected_type=type_hints["min_number_of_executed_things"])
                check_type(argname="argument threshold_percentage", value=threshold_percentage, expected_type=type_hints["threshold_percentage"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "action": action,
                "failure_type": failure_type,
                "min_number_of_executed_things": min_number_of_executed_things,
                "threshold_percentage": threshold_percentage,
            }

        @builtins.property
        def action(self) -> builtins.str:
            '''The type of job action to take to initiate the job abort.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-abortcriteria.html#cfn-iot-jobtemplate-abortcriteria-action
            '''
            result = self._values.get("action")
            assert result is not None, "Required property 'action' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def failure_type(self) -> builtins.str:
            '''The type of job execution failures that can initiate a job abort.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-abortcriteria.html#cfn-iot-jobtemplate-abortcriteria-failuretype
            '''
            result = self._values.get("failure_type")
            assert result is not None, "Required property 'failure_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def min_number_of_executed_things(self) -> jsii.Number:
            '''The minimum number of things which must receive job execution notifications before the job can be aborted.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-abortcriteria.html#cfn-iot-jobtemplate-abortcriteria-minnumberofexecutedthings
            '''
            result = self._values.get("min_number_of_executed_things")
            assert result is not None, "Required property 'min_number_of_executed_things' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def threshold_percentage(self) -> jsii.Number:
            '''The minimum percentage of job execution failures that must occur to initiate the job abort.

            AWS IoT Core supports up to two digits after the decimal (for example, 10.9 and 10.99, but not 10.999).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-abortcriteria.html#cfn-iot-jobtemplate-abortcriteria-thresholdpercentage
            '''
            result = self._values.get("threshold_percentage")
            assert result is not None, "Required property 'threshold_percentage' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AbortCriteriaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnJobTemplate.ExponentialRolloutRateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "base_rate_per_minute": "baseRatePerMinute",
            "increment_factor": "incrementFactor",
            "rate_increase_criteria": "rateIncreaseCriteria",
        },
    )
    class ExponentialRolloutRateProperty:
        def __init__(
            self,
            *,
            base_rate_per_minute: jsii.Number,
            increment_factor: jsii.Number,
            rate_increase_criteria: typing.Union[typing.Union["CfnJobTemplate.RateIncreaseCriteriaProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
        ) -> None:
            '''Allows you to create an exponential rate of rollout for a job.

            :param base_rate_per_minute: The minimum number of things that will be notified of a pending job, per minute at the start of job rollout. This parameter allows you to define the initial rate of rollout.
            :param increment_factor: The exponential factor to increase the rate of rollout for a job. AWS IoT Core supports up to one digit after the decimal (for example, 1.5, but not 1.55).
            :param rate_increase_criteria: The criteria to initiate the increase in rate of rollout for a job.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-exponentialrolloutrate.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                exponential_rollout_rate_property = iot.CfnJobTemplate.ExponentialRolloutRateProperty(
                    base_rate_per_minute=123,
                    increment_factor=123,
                    rate_increase_criteria=iot.CfnJobTemplate.RateIncreaseCriteriaProperty(
                        number_of_notified_things=123,
                        number_of_succeeded_things=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c2052a32a583bd05cf3037191b5c148ac2d2e32b19afb0b3ac4c5d0558bf6396)
                check_type(argname="argument base_rate_per_minute", value=base_rate_per_minute, expected_type=type_hints["base_rate_per_minute"])
                check_type(argname="argument increment_factor", value=increment_factor, expected_type=type_hints["increment_factor"])
                check_type(argname="argument rate_increase_criteria", value=rate_increase_criteria, expected_type=type_hints["rate_increase_criteria"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "base_rate_per_minute": base_rate_per_minute,
                "increment_factor": increment_factor,
                "rate_increase_criteria": rate_increase_criteria,
            }

        @builtins.property
        def base_rate_per_minute(self) -> jsii.Number:
            '''The minimum number of things that will be notified of a pending job, per minute at the start of job rollout.

            This parameter allows you to define the initial rate of rollout.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-exponentialrolloutrate.html#cfn-iot-jobtemplate-exponentialrolloutrate-baserateperminute
            '''
            result = self._values.get("base_rate_per_minute")
            assert result is not None, "Required property 'base_rate_per_minute' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def increment_factor(self) -> jsii.Number:
            '''The exponential factor to increase the rate of rollout for a job.

            AWS IoT Core supports up to one digit after the decimal (for example, 1.5, but not 1.55).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-exponentialrolloutrate.html#cfn-iot-jobtemplate-exponentialrolloutrate-incrementfactor
            '''
            result = self._values.get("increment_factor")
            assert result is not None, "Required property 'increment_factor' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def rate_increase_criteria(
            self,
        ) -> typing.Union["CfnJobTemplate.RateIncreaseCriteriaProperty", _IResolvable_a771d0ef]:
            '''The criteria to initiate the increase in rate of rollout for a job.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-exponentialrolloutrate.html#cfn-iot-jobtemplate-exponentialrolloutrate-rateincreasecriteria
            '''
            result = self._values.get("rate_increase_criteria")
            assert result is not None, "Required property 'rate_increase_criteria' is missing"
            return typing.cast(typing.Union["CfnJobTemplate.RateIncreaseCriteriaProperty", _IResolvable_a771d0ef], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExponentialRolloutRateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnJobTemplate.JobExecutionsRolloutConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "exponential_rollout_rate": "exponentialRolloutRate",
            "maximum_per_minute": "maximumPerMinute",
        },
    )
    class JobExecutionsRolloutConfigProperty:
        def __init__(
            self,
            *,
            exponential_rollout_rate: typing.Optional[typing.Union[typing.Union["CfnJobTemplate.ExponentialRolloutRateProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            maximum_per_minute: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Allows you to create a staged rollout of a job.

            :param exponential_rollout_rate: ``CfnJobTemplate.JobExecutionsRolloutConfigProperty.ExponentialRolloutRate``.
            :param maximum_per_minute: The maximum number of things that will be notified of a pending job, per minute. This parameter allows you to create a staged rollout.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-jobexecutionsrolloutconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                job_executions_rollout_config_property = iot.CfnJobTemplate.JobExecutionsRolloutConfigProperty(
                    exponential_rollout_rate=iot.CfnJobTemplate.ExponentialRolloutRateProperty(
                        base_rate_per_minute=123,
                        increment_factor=123,
                        rate_increase_criteria=iot.CfnJobTemplate.RateIncreaseCriteriaProperty(
                            number_of_notified_things=123,
                            number_of_succeeded_things=123
                        )
                    ),
                    maximum_per_minute=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__aac20f7f460de569a8f5d8e6a182e48b1956c801ac829d51e0002b820ee0f2e4)
                check_type(argname="argument exponential_rollout_rate", value=exponential_rollout_rate, expected_type=type_hints["exponential_rollout_rate"])
                check_type(argname="argument maximum_per_minute", value=maximum_per_minute, expected_type=type_hints["maximum_per_minute"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if exponential_rollout_rate is not None:
                self._values["exponential_rollout_rate"] = exponential_rollout_rate
            if maximum_per_minute is not None:
                self._values["maximum_per_minute"] = maximum_per_minute

        @builtins.property
        def exponential_rollout_rate(
            self,
        ) -> typing.Optional[typing.Union["CfnJobTemplate.ExponentialRolloutRateProperty", _IResolvable_a771d0ef]]:
            '''``CfnJobTemplate.JobExecutionsRolloutConfigProperty.ExponentialRolloutRate``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-jobexecutionsrolloutconfig.html#cfn-iot-jobtemplate-jobexecutionsrolloutconfig-exponentialrolloutrate
            '''
            result = self._values.get("exponential_rollout_rate")
            return typing.cast(typing.Optional[typing.Union["CfnJobTemplate.ExponentialRolloutRateProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def maximum_per_minute(self) -> typing.Optional[jsii.Number]:
            '''The maximum number of things that will be notified of a pending job, per minute.

            This parameter allows you to create a staged rollout.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-jobexecutionsrolloutconfig.html#cfn-iot-jobtemplate-jobexecutionsrolloutconfig-maximumperminute
            '''
            result = self._values.get("maximum_per_minute")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JobExecutionsRolloutConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnJobTemplate.PresignedUrlConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"role_arn": "roleArn", "expires_in_sec": "expiresInSec"},
    )
    class PresignedUrlConfigProperty:
        def __init__(
            self,
            *,
            role_arn: builtins.str,
            expires_in_sec: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Configuration for pre-signed S3 URLs.

            :param role_arn: The ARN of an IAM role that grants grants permission to download files from the S3 bucket where the job data/updates are stored. The role must also grant permission for IoT to download the files. .. epigraph:: For information about addressing the confused deputy problem, see `cross-service confused deputy prevention <https://docs.aws.amazon.com/iot/latest/developerguide/cross-service-confused-deputy-prevention.html>`_ in the *AWS IoT Core developer guide* .
            :param expires_in_sec: How long (in seconds) pre-signed URLs are valid. Valid values are 60 - 3600, the default value is 3600 seconds. Pre-signed URLs are generated when Jobs receives an MQTT request for the job document.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-presignedurlconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                presigned_url_config_property = iot.CfnJobTemplate.PresignedUrlConfigProperty(
                    role_arn="roleArn",
                
                    # the properties below are optional
                    expires_in_sec=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c4e94ff4d2f6d8f1b221fcac01434fbeab49de32c4145002c77d26cc1e4cf006)
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument expires_in_sec", value=expires_in_sec, expected_type=type_hints["expires_in_sec"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "role_arn": role_arn,
            }
            if expires_in_sec is not None:
                self._values["expires_in_sec"] = expires_in_sec

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of an IAM role that grants grants permission to download files from the S3 bucket where the job data/updates are stored.

            The role must also grant permission for IoT to download the files.
            .. epigraph::

               For information about addressing the confused deputy problem, see `cross-service confused deputy prevention <https://docs.aws.amazon.com/iot/latest/developerguide/cross-service-confused-deputy-prevention.html>`_ in the *AWS IoT Core developer guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-presignedurlconfig.html#cfn-iot-jobtemplate-presignedurlconfig-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def expires_in_sec(self) -> typing.Optional[jsii.Number]:
            '''How long (in seconds) pre-signed URLs are valid.

            Valid values are 60 - 3600, the default value is 3600 seconds. Pre-signed URLs are generated when Jobs receives an MQTT request for the job document.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-presignedurlconfig.html#cfn-iot-jobtemplate-presignedurlconfig-expiresinsec
            '''
            result = self._values.get("expires_in_sec")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PresignedUrlConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnJobTemplate.RateIncreaseCriteriaProperty",
        jsii_struct_bases=[],
        name_mapping={
            "number_of_notified_things": "numberOfNotifiedThings",
            "number_of_succeeded_things": "numberOfSucceededThings",
        },
    )
    class RateIncreaseCriteriaProperty:
        def __init__(
            self,
            *,
            number_of_notified_things: typing.Optional[jsii.Number] = None,
            number_of_succeeded_things: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Allows you to define a criteria to initiate the increase in rate of rollout for a job.

            :param number_of_notified_things: The threshold for number of notified things that will initiate the increase in rate of rollout.
            :param number_of_succeeded_things: The threshold for number of succeeded things that will initiate the increase in rate of rollout.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-rateincreasecriteria.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                rate_increase_criteria_property = iot.CfnJobTemplate.RateIncreaseCriteriaProperty(
                    number_of_notified_things=123,
                    number_of_succeeded_things=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6e5be353af0f898d3561e3fcbd7a9b2ecc609f1285539d8f844baddb1a04a445)
                check_type(argname="argument number_of_notified_things", value=number_of_notified_things, expected_type=type_hints["number_of_notified_things"])
                check_type(argname="argument number_of_succeeded_things", value=number_of_succeeded_things, expected_type=type_hints["number_of_succeeded_things"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if number_of_notified_things is not None:
                self._values["number_of_notified_things"] = number_of_notified_things
            if number_of_succeeded_things is not None:
                self._values["number_of_succeeded_things"] = number_of_succeeded_things

        @builtins.property
        def number_of_notified_things(self) -> typing.Optional[jsii.Number]:
            '''The threshold for number of notified things that will initiate the increase in rate of rollout.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-rateincreasecriteria.html#cfn-iot-jobtemplate-rateincreasecriteria-numberofnotifiedthings
            '''
            result = self._values.get("number_of_notified_things")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def number_of_succeeded_things(self) -> typing.Optional[jsii.Number]:
            '''The threshold for number of succeeded things that will initiate the increase in rate of rollout.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-rateincreasecriteria.html#cfn-iot-jobtemplate-rateincreasecriteria-numberofsucceededthings
            '''
            result = self._values.get("number_of_succeeded_things")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RateIncreaseCriteriaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnJobTemplate.TimeoutConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"in_progress_timeout_in_minutes": "inProgressTimeoutInMinutes"},
    )
    class TimeoutConfigProperty:
        def __init__(self, *, in_progress_timeout_in_minutes: jsii.Number) -> None:
            '''Specifies the amount of time each device has to finish its execution of the job.

            A timer is started when the job execution status is set to ``IN_PROGRESS`` . If the job execution status is not set to another terminal state before the timer expires, it will be automatically set to ``TIMED_OUT`` .

            :param in_progress_timeout_in_minutes: Specifies the amount of time, in minutes, this device has to finish execution of this job. The timeout interval can be anywhere between 1 minute and 7 days (1 to 10080 minutes). The in progress timer can't be updated and will apply to all job executions for the job. Whenever a job execution remains in the IN_PROGRESS status for longer than this interval, the job execution will fail and switch to the terminal ``TIMED_OUT`` status.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-timeoutconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                timeout_config_property = iot.CfnJobTemplate.TimeoutConfigProperty(
                    in_progress_timeout_in_minutes=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b4fd99ca69eb4073923cadbf5039d2c3d852ee132232742a4c7258c4869166d7)
                check_type(argname="argument in_progress_timeout_in_minutes", value=in_progress_timeout_in_minutes, expected_type=type_hints["in_progress_timeout_in_minutes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "in_progress_timeout_in_minutes": in_progress_timeout_in_minutes,
            }

        @builtins.property
        def in_progress_timeout_in_minutes(self) -> jsii.Number:
            '''Specifies the amount of time, in minutes, this device has to finish execution of this job.

            The timeout interval can be anywhere between 1 minute and 7 days (1 to 10080 minutes). The in progress timer can't be updated and will apply to all job executions for the job. Whenever a job execution remains in the IN_PROGRESS status for longer than this interval, the job execution will fail and switch to the terminal ``TIMED_OUT`` status.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-jobtemplate-timeoutconfig.html#cfn-iot-jobtemplate-timeoutconfig-inprogresstimeoutinminutes
            '''
            result = self._values.get("in_progress_timeout_in_minutes")
            assert result is not None, "Required property 'in_progress_timeout_in_minutes' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TimeoutConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_iot.CfnJobTemplateProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "job_template_id": "jobTemplateId",
        "abort_config": "abortConfig",
        "document": "document",
        "document_source": "documentSource",
        "job_arn": "jobArn",
        "job_executions_rollout_config": "jobExecutionsRolloutConfig",
        "presigned_url_config": "presignedUrlConfig",
        "tags": "tags",
        "timeout_config": "timeoutConfig",
    },
)
class CfnJobTemplateProps:
    def __init__(
        self,
        *,
        description: builtins.str,
        job_template_id: builtins.str,
        abort_config: typing.Any = None,
        document: typing.Optional[builtins.str] = None,
        document_source: typing.Optional[builtins.str] = None,
        job_arn: typing.Optional[builtins.str] = None,
        job_executions_rollout_config: typing.Any = None,
        presigned_url_config: typing.Any = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
        timeout_config: typing.Any = None,
    ) -> None:
        '''Properties for defining a ``CfnJobTemplate``.

        :param description: A description of the job template.
        :param job_template_id: A unique identifier for the job template. We recommend using a UUID. Alpha-numeric characters, "-", and "_" are valid for use here.
        :param abort_config: The criteria that determine when and how a job abort takes place.
        :param document: The job document. Required if you don't specify a value for ``documentSource`` .
        :param document_source: An S3 link to the job document to use in the template. Required if you don't specify a value for ``document`` . .. epigraph:: If the job document resides in an S3 bucket, you must use a placeholder link when specifying the document. The placeholder link is of the following form: ``${aws:iot:s3-presigned-url:https://s3.amazonaws.com/ *bucket* / *key* }`` where *bucket* is your bucket name and *key* is the object in the bucket to which you are linking.
        :param job_arn: The ARN of the job to use as the basis for the job template.
        :param job_executions_rollout_config: Allows you to create a staged rollout of a job.
        :param presigned_url_config: Configuration for pre-signed S3 URLs.
        :param tags: Metadata that can be used to manage the job template.
        :param timeout_config: Specifies the amount of time each device has to finish its execution of the job. A timer is started when the job execution status is set to ``IN_PROGRESS`` . If the job execution status is not set to another terminal state before the timer expires, it will be automatically set to ``TIMED_OUT`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_iot as iot
            
            # abort_config: Any
            # job_executions_rollout_config: Any
            # presigned_url_config: Any
            # timeout_config: Any
            
            cfn_job_template_props = iot.CfnJobTemplateProps(
                description="description",
                job_template_id="jobTemplateId",
            
                # the properties below are optional
                abort_config=abort_config,
                document="document",
                document_source="documentSource",
                job_arn="jobArn",
                job_executions_rollout_config=job_executions_rollout_config,
                presigned_url_config=presigned_url_config,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                timeout_config=timeout_config
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0decc37289d85c109d4c12fd8652a7a5ace85f7b636a9dd9a05a64bebc84309)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument job_template_id", value=job_template_id, expected_type=type_hints["job_template_id"])
            check_type(argname="argument abort_config", value=abort_config, expected_type=type_hints["abort_config"])
            check_type(argname="argument document", value=document, expected_type=type_hints["document"])
            check_type(argname="argument document_source", value=document_source, expected_type=type_hints["document_source"])
            check_type(argname="argument job_arn", value=job_arn, expected_type=type_hints["job_arn"])
            check_type(argname="argument job_executions_rollout_config", value=job_executions_rollout_config, expected_type=type_hints["job_executions_rollout_config"])
            check_type(argname="argument presigned_url_config", value=presigned_url_config, expected_type=type_hints["presigned_url_config"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeout_config", value=timeout_config, expected_type=type_hints["timeout_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "job_template_id": job_template_id,
        }
        if abort_config is not None:
            self._values["abort_config"] = abort_config
        if document is not None:
            self._values["document"] = document
        if document_source is not None:
            self._values["document_source"] = document_source
        if job_arn is not None:
            self._values["job_arn"] = job_arn
        if job_executions_rollout_config is not None:
            self._values["job_executions_rollout_config"] = job_executions_rollout_config
        if presigned_url_config is not None:
            self._values["presigned_url_config"] = presigned_url_config
        if tags is not None:
            self._values["tags"] = tags
        if timeout_config is not None:
            self._values["timeout_config"] = timeout_config

    @builtins.property
    def description(self) -> builtins.str:
        '''A description of the job template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def job_template_id(self) -> builtins.str:
        '''A unique identifier for the job template.

        We recommend using a UUID. Alpha-numeric characters, "-", and "_" are valid for use here.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-jobtemplateid
        '''
        result = self._values.get("job_template_id")
        assert result is not None, "Required property 'job_template_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def abort_config(self) -> typing.Any:
        '''The criteria that determine when and how a job abort takes place.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-abortconfig
        '''
        result = self._values.get("abort_config")
        return typing.cast(typing.Any, result)

    @builtins.property
    def document(self) -> typing.Optional[builtins.str]:
        '''The job document.

        Required if you don't specify a value for ``documentSource`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-document
        '''
        result = self._values.get("document")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def document_source(self) -> typing.Optional[builtins.str]:
        '''An S3 link to the job document to use in the template.

        Required if you don't specify a value for ``document`` .
        .. epigraph::

           If the job document resides in an S3 bucket, you must use a placeholder link when specifying the document.

           The placeholder link is of the following form:

           ``${aws:iot:s3-presigned-url:https://s3.amazonaws.com/ *bucket* / *key* }``

           where *bucket* is your bucket name and *key* is the object in the bucket to which you are linking.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-documentsource
        '''
        result = self._values.get("document_source")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def job_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the job to use as the basis for the job template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-jobarn
        '''
        result = self._values.get("job_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def job_executions_rollout_config(self) -> typing.Any:
        '''Allows you to create a staged rollout of a job.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-jobexecutionsrolloutconfig
        '''
        result = self._values.get("job_executions_rollout_config")
        return typing.cast(typing.Any, result)

    @builtins.property
    def presigned_url_config(self) -> typing.Any:
        '''Configuration for pre-signed S3 URLs.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-presignedurlconfig
        '''
        result = self._values.get("presigned_url_config")
        return typing.cast(typing.Any, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''Metadata that can be used to manage the job template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    @builtins.property
    def timeout_config(self) -> typing.Any:
        '''Specifies the amount of time each device has to finish its execution of the job.

        A timer is started when the job execution status is set to ``IN_PROGRESS`` . If the job execution status is not set to another terminal state before the timer expires, it will be automatically set to ``TIMED_OUT`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-jobtemplate.html#cfn-iot-jobtemplate-timeoutconfig
        '''
        result = self._values.get("timeout_config")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnJobTemplateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnLogging(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iot.CfnLogging",
):
    '''A CloudFormation ``AWS::IoT::Logging``.

    Configure logging.

    :cloudformationResource: AWS::IoT::Logging
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-logging.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_iot as iot
        
        cfn_logging = iot.CfnLogging(self, "MyCfnLogging",
            account_id="accountId",
            default_log_level="defaultLogLevel",
            role_arn="roleArn"
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        account_id: builtins.str,
        default_log_level: builtins.str,
        role_arn: builtins.str,
    ) -> None:
        '''Create a new ``AWS::IoT::Logging``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param account_id: The account ID.
        :param default_log_level: The default log level. Valid Values: ``DEBUG | INFO | ERROR | WARN | DISABLED``
        :param role_arn: The role ARN used for the log.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__094396c4ba46b29a170381deac5107d2d442c7327a43c7108fea10990cfc8aa5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLoggingProps(
            account_id=account_id,
            default_log_level=default_log_level,
            role_arn=role_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72aab6343747b627f655b318ab8cff0961b9985f8d4938911d2e6b719c1b77bc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8dc06cd0f2c036f3770e19b87d77f3d4b8db582665521b3da6ecc676fe899381)
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
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        '''The account ID.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-logging.html#cfn-iot-logging-accountid
        '''
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4096259646bae3677e768871b27d0032cbc0d107a078723298d984dd0e749835)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="defaultLogLevel")
    def default_log_level(self) -> builtins.str:
        '''The default log level.

        Valid Values: ``DEBUG | INFO | ERROR | WARN | DISABLED``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-logging.html#cfn-iot-logging-defaultloglevel
        '''
        return typing.cast(builtins.str, jsii.get(self, "defaultLogLevel"))

    @default_log_level.setter
    def default_log_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98616587275eb46377308ad9f5bdab9ad927c9eb8dcdc1b20ae94e82f821c860)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultLogLevel", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The role ARN used for the log.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-logging.html#cfn-iot-logging-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0aed8eaa9b09117c4de6bdb5e8eddfd3ce11681d84504cab7ebdeed7839910b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)


@jsii.data_type(
    jsii_type="monocdk.aws_iot.CfnLoggingProps",
    jsii_struct_bases=[],
    name_mapping={
        "account_id": "accountId",
        "default_log_level": "defaultLogLevel",
        "role_arn": "roleArn",
    },
)
class CfnLoggingProps:
    def __init__(
        self,
        *,
        account_id: builtins.str,
        default_log_level: builtins.str,
        role_arn: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnLogging``.

        :param account_id: The account ID.
        :param default_log_level: The default log level. Valid Values: ``DEBUG | INFO | ERROR | WARN | DISABLED``
        :param role_arn: The role ARN used for the log.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-logging.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_iot as iot
            
            cfn_logging_props = iot.CfnLoggingProps(
                account_id="accountId",
                default_log_level="defaultLogLevel",
                role_arn="roleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c49d63e33b9998468fa3da7a5e3b3007a5d6d5a584fd2ec917b0667107d73736)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument default_log_level", value=default_log_level, expected_type=type_hints["default_log_level"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_id": account_id,
            "default_log_level": default_log_level,
            "role_arn": role_arn,
        }

    @builtins.property
    def account_id(self) -> builtins.str:
        '''The account ID.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-logging.html#cfn-iot-logging-accountid
        '''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_log_level(self) -> builtins.str:
        '''The default log level.

        Valid Values: ``DEBUG | INFO | ERROR | WARN | DISABLED``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-logging.html#cfn-iot-logging-defaultloglevel
        '''
        result = self._values.get("default_log_level")
        assert result is not None, "Required property 'default_log_level' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The role ARN used for the log.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-logging.html#cfn-iot-logging-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLoggingProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnMitigationAction(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iot.CfnMitigationAction",
):
    '''A CloudFormation ``AWS::IoT::MitigationAction``.

    Defines an action that can be applied to audit findings by using StartAuditMitigationActionsTask. For API reference, see `CreateMitigationAction <https://docs.aws.amazon.com/iot/latest/apireference/API_CreateMitigationAction.html>`_ and for general information, see `Mitigation actions <https://docs.aws.amazon.com/iot/latest/developerguide/dd-mitigation-actions.html>`_ .

    :cloudformationResource: AWS::IoT::MitigationAction
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-mitigationaction.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_iot as iot
        
        cfn_mitigation_action = iot.CfnMitigationAction(self, "MyCfnMitigationAction",
            action_params=iot.CfnMitigationAction.ActionParamsProperty(
                add_things_to_thing_group_params=iot.CfnMitigationAction.AddThingsToThingGroupParamsProperty(
                    thing_group_names=["thingGroupNames"],
        
                    # the properties below are optional
                    override_dynamic_groups=False
                ),
                enable_io_tLogging_params=iot.CfnMitigationAction.EnableIoTLoggingParamsProperty(
                    log_level="logLevel",
                    role_arn_for_logging="roleArnForLogging"
                ),
                publish_finding_to_sns_params=iot.CfnMitigationAction.PublishFindingToSnsParamsProperty(
                    topic_arn="topicArn"
                ),
                replace_default_policy_version_params=iot.CfnMitigationAction.ReplaceDefaultPolicyVersionParamsProperty(
                    template_name="templateName"
                ),
                update_ca_certificate_params=iot.CfnMitigationAction.UpdateCACertificateParamsProperty(
                    action="action"
                ),
                update_device_certificate_params=iot.CfnMitigationAction.UpdateDeviceCertificateParamsProperty(
                    action="action"
                )
            ),
            role_arn="roleArn",
        
            # the properties below are optional
            action_name="actionName",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        action_params: typing.Union[typing.Union["CfnMitigationAction.ActionParamsProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
        role_arn: builtins.str,
        action_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::IoT::MitigationAction``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param action_params: The set of parameters for this mitigation action. The parameters vary, depending on the kind of action you apply.
        :param role_arn: The IAM role ARN used to apply this mitigation action.
        :param action_name: The friendly name of the mitigation action.
        :param tags: Metadata that can be used to manage the mitigation action.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f1fc93a374a9f5fbe17fc2443ad7de6d1da6e42bfcb421c2687874abfcc8c87)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMitigationActionProps(
            action_params=action_params,
            role_arn=role_arn,
            action_name=action_name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9681819be2ae3a90eabbe27bdb1e9e1cef3129de4b848903ecafe26c94cb567)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dc7905926753ab9369de30e8966a4b6b9c1a1d578be14c601cef5890774c5204)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrMitigationActionArn")
    def attr_mitigation_action_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the mitigation action.

        :cloudformationAttribute: MitigationActionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMitigationActionArn"))

    @builtins.property
    @jsii.member(jsii_name="attrMitigationActionId")
    def attr_mitigation_action_id(self) -> builtins.str:
        '''The ID of the mitigation action.

        :cloudformationAttribute: MitigationActionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMitigationActionId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''Metadata that can be used to manage the mitigation action.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-mitigationaction.html#cfn-iot-mitigationaction-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="actionParams")
    def action_params(
        self,
    ) -> typing.Union["CfnMitigationAction.ActionParamsProperty", _IResolvable_a771d0ef]:
        '''The set of parameters for this mitigation action.

        The parameters vary, depending on the kind of action you apply.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-mitigationaction.html#cfn-iot-mitigationaction-actionparams
        '''
        return typing.cast(typing.Union["CfnMitigationAction.ActionParamsProperty", _IResolvable_a771d0ef], jsii.get(self, "actionParams"))

    @action_params.setter
    def action_params(
        self,
        value: typing.Union["CfnMitigationAction.ActionParamsProperty", _IResolvable_a771d0ef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f87c4b2a4154c3a913ff062d9f80e18ede929978c58c77ea5330dbe5fa085b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionParams", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The IAM role ARN used to apply this mitigation action.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-mitigationaction.html#cfn-iot-mitigationaction-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d03fe96a6e41ba4ca36bbac697ea96ec1eef217f0a0bfed192421d6277445f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="actionName")
    def action_name(self) -> typing.Optional[builtins.str]:
        '''The friendly name of the mitigation action.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-mitigationaction.html#cfn-iot-mitigationaction-actionname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionName"))

    @action_name.setter
    def action_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2751a30a0ae45200585494f0ef85db81102e76115cd3f914e8eff79574830daa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionName", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnMitigationAction.ActionParamsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "add_things_to_thing_group_params": "addThingsToThingGroupParams",
            "enable_io_t_logging_params": "enableIoTLoggingParams",
            "publish_finding_to_sns_params": "publishFindingToSnsParams",
            "replace_default_policy_version_params": "replaceDefaultPolicyVersionParams",
            "update_ca_certificate_params": "updateCaCertificateParams",
            "update_device_certificate_params": "updateDeviceCertificateParams",
        },
    )
    class ActionParamsProperty:
        def __init__(
            self,
            *,
            add_things_to_thing_group_params: typing.Optional[typing.Union[typing.Union["CfnMitigationAction.AddThingsToThingGroupParamsProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            enable_io_t_logging_params: typing.Optional[typing.Union[typing.Union["CfnMitigationAction.EnableIoTLoggingParamsProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            publish_finding_to_sns_params: typing.Optional[typing.Union[typing.Union["CfnMitigationAction.PublishFindingToSnsParamsProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            replace_default_policy_version_params: typing.Optional[typing.Union[typing.Union["CfnMitigationAction.ReplaceDefaultPolicyVersionParamsProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            update_ca_certificate_params: typing.Optional[typing.Union[typing.Union["CfnMitigationAction.UpdateCACertificateParamsProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            update_device_certificate_params: typing.Optional[typing.Union[typing.Union["CfnMitigationAction.UpdateDeviceCertificateParamsProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''Defines the type of action and the parameters for that action.

            :param add_things_to_thing_group_params: Specifies the group to which you want to add the devices.
            :param enable_io_t_logging_params: Specifies the logging level and the role with permissions for logging. You cannot specify a logging level of ``DISABLED`` .
            :param publish_finding_to_sns_params: Specifies the topic to which the finding should be published.
            :param replace_default_policy_version_params: Replaces the policy version with a default or blank policy. You specify the template name. Only a value of ``BLANK_POLICY`` is currently supported.
            :param update_ca_certificate_params: Specifies the new state for the CA certificate. Only a value of ``DEACTIVATE`` is currently supported.
            :param update_device_certificate_params: Specifies the new state for a device certificate. Only a value of ``DEACTIVATE`` is currently supported.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-actionparams.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                action_params_property = iot.CfnMitigationAction.ActionParamsProperty(
                    add_things_to_thing_group_params=iot.CfnMitigationAction.AddThingsToThingGroupParamsProperty(
                        thing_group_names=["thingGroupNames"],
                
                        # the properties below are optional
                        override_dynamic_groups=False
                    ),
                    enable_io_tLogging_params=iot.CfnMitigationAction.EnableIoTLoggingParamsProperty(
                        log_level="logLevel",
                        role_arn_for_logging="roleArnForLogging"
                    ),
                    publish_finding_to_sns_params=iot.CfnMitigationAction.PublishFindingToSnsParamsProperty(
                        topic_arn="topicArn"
                    ),
                    replace_default_policy_version_params=iot.CfnMitigationAction.ReplaceDefaultPolicyVersionParamsProperty(
                        template_name="templateName"
                    ),
                    update_ca_certificate_params=iot.CfnMitigationAction.UpdateCACertificateParamsProperty(
                        action="action"
                    ),
                    update_device_certificate_params=iot.CfnMitigationAction.UpdateDeviceCertificateParamsProperty(
                        action="action"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9fa438995fc0d7aefbb02d6cb1cf2658e86c5feaba485ccb8cfbf158f2752d7b)
                check_type(argname="argument add_things_to_thing_group_params", value=add_things_to_thing_group_params, expected_type=type_hints["add_things_to_thing_group_params"])
                check_type(argname="argument enable_io_t_logging_params", value=enable_io_t_logging_params, expected_type=type_hints["enable_io_t_logging_params"])
                check_type(argname="argument publish_finding_to_sns_params", value=publish_finding_to_sns_params, expected_type=type_hints["publish_finding_to_sns_params"])
                check_type(argname="argument replace_default_policy_version_params", value=replace_default_policy_version_params, expected_type=type_hints["replace_default_policy_version_params"])
                check_type(argname="argument update_ca_certificate_params", value=update_ca_certificate_params, expected_type=type_hints["update_ca_certificate_params"])
                check_type(argname="argument update_device_certificate_params", value=update_device_certificate_params, expected_type=type_hints["update_device_certificate_params"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if add_things_to_thing_group_params is not None:
                self._values["add_things_to_thing_group_params"] = add_things_to_thing_group_params
            if enable_io_t_logging_params is not None:
                self._values["enable_io_t_logging_params"] = enable_io_t_logging_params
            if publish_finding_to_sns_params is not None:
                self._values["publish_finding_to_sns_params"] = publish_finding_to_sns_params
            if replace_default_policy_version_params is not None:
                self._values["replace_default_policy_version_params"] = replace_default_policy_version_params
            if update_ca_certificate_params is not None:
                self._values["update_ca_certificate_params"] = update_ca_certificate_params
            if update_device_certificate_params is not None:
                self._values["update_device_certificate_params"] = update_device_certificate_params

        @builtins.property
        def add_things_to_thing_group_params(
            self,
        ) -> typing.Optional[typing.Union["CfnMitigationAction.AddThingsToThingGroupParamsProperty", _IResolvable_a771d0ef]]:
            '''Specifies the group to which you want to add the devices.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-actionparams.html#cfn-iot-mitigationaction-actionparams-addthingstothinggroupparams
            '''
            result = self._values.get("add_things_to_thing_group_params")
            return typing.cast(typing.Optional[typing.Union["CfnMitigationAction.AddThingsToThingGroupParamsProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def enable_io_t_logging_params(
            self,
        ) -> typing.Optional[typing.Union["CfnMitigationAction.EnableIoTLoggingParamsProperty", _IResolvable_a771d0ef]]:
            '''Specifies the logging level and the role with permissions for logging.

            You cannot specify a logging level of ``DISABLED`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-actionparams.html#cfn-iot-mitigationaction-actionparams-enableiotloggingparams
            '''
            result = self._values.get("enable_io_t_logging_params")
            return typing.cast(typing.Optional[typing.Union["CfnMitigationAction.EnableIoTLoggingParamsProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def publish_finding_to_sns_params(
            self,
        ) -> typing.Optional[typing.Union["CfnMitigationAction.PublishFindingToSnsParamsProperty", _IResolvable_a771d0ef]]:
            '''Specifies the topic to which the finding should be published.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-actionparams.html#cfn-iot-mitigationaction-actionparams-publishfindingtosnsparams
            '''
            result = self._values.get("publish_finding_to_sns_params")
            return typing.cast(typing.Optional[typing.Union["CfnMitigationAction.PublishFindingToSnsParamsProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def replace_default_policy_version_params(
            self,
        ) -> typing.Optional[typing.Union["CfnMitigationAction.ReplaceDefaultPolicyVersionParamsProperty", _IResolvable_a771d0ef]]:
            '''Replaces the policy version with a default or blank policy.

            You specify the template name. Only a value of ``BLANK_POLICY`` is currently supported.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-actionparams.html#cfn-iot-mitigationaction-actionparams-replacedefaultpolicyversionparams
            '''
            result = self._values.get("replace_default_policy_version_params")
            return typing.cast(typing.Optional[typing.Union["CfnMitigationAction.ReplaceDefaultPolicyVersionParamsProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def update_ca_certificate_params(
            self,
        ) -> typing.Optional[typing.Union["CfnMitigationAction.UpdateCACertificateParamsProperty", _IResolvable_a771d0ef]]:
            '''Specifies the new state for the CA certificate.

            Only a value of ``DEACTIVATE`` is currently supported.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-actionparams.html#cfn-iot-mitigationaction-actionparams-updatecacertificateparams
            '''
            result = self._values.get("update_ca_certificate_params")
            return typing.cast(typing.Optional[typing.Union["CfnMitigationAction.UpdateCACertificateParamsProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def update_device_certificate_params(
            self,
        ) -> typing.Optional[typing.Union["CfnMitigationAction.UpdateDeviceCertificateParamsProperty", _IResolvable_a771d0ef]]:
            '''Specifies the new state for a device certificate.

            Only a value of ``DEACTIVATE`` is currently supported.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-actionparams.html#cfn-iot-mitigationaction-actionparams-updatedevicecertificateparams
            '''
            result = self._values.get("update_device_certificate_params")
            return typing.cast(typing.Optional[typing.Union["CfnMitigationAction.UpdateDeviceCertificateParamsProperty", _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActionParamsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnMitigationAction.AddThingsToThingGroupParamsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "thing_group_names": "thingGroupNames",
            "override_dynamic_groups": "overrideDynamicGroups",
        },
    )
    class AddThingsToThingGroupParamsProperty:
        def __init__(
            self,
            *,
            thing_group_names: typing.Sequence[builtins.str],
            override_dynamic_groups: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''Parameters used when defining a mitigation action that move a set of things to a thing group.

            :param thing_group_names: The list of groups to which you want to add the things that triggered the mitigation action. You can add a thing to a maximum of 10 groups, but you can't add a thing to more than one group in the same hierarchy.
            :param override_dynamic_groups: Specifies if this mitigation action can move the things that triggered the mitigation action even if they are part of one or more dynamic thing groups.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-addthingstothinggroupparams.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                add_things_to_thing_group_params_property = iot.CfnMitigationAction.AddThingsToThingGroupParamsProperty(
                    thing_group_names=["thingGroupNames"],
                
                    # the properties below are optional
                    override_dynamic_groups=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__62315475f8b9e1ad115d4b1043c244bdd7c7724f3b130ceb1366d049a4281573)
                check_type(argname="argument thing_group_names", value=thing_group_names, expected_type=type_hints["thing_group_names"])
                check_type(argname="argument override_dynamic_groups", value=override_dynamic_groups, expected_type=type_hints["override_dynamic_groups"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "thing_group_names": thing_group_names,
            }
            if override_dynamic_groups is not None:
                self._values["override_dynamic_groups"] = override_dynamic_groups

        @builtins.property
        def thing_group_names(self) -> typing.List[builtins.str]:
            '''The list of groups to which you want to add the things that triggered the mitigation action.

            You can add a thing to a maximum of 10 groups, but you can't add a thing to more than one group in the same hierarchy.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-addthingstothinggroupparams.html#cfn-iot-mitigationaction-addthingstothinggroupparams-thinggroupnames
            '''
            result = self._values.get("thing_group_names")
            assert result is not None, "Required property 'thing_group_names' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def override_dynamic_groups(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Specifies if this mitigation action can move the things that triggered the mitigation action even if they are part of one or more dynamic thing groups.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-addthingstothinggroupparams.html#cfn-iot-mitigationaction-addthingstothinggroupparams-overridedynamicgroups
            '''
            result = self._values.get("override_dynamic_groups")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AddThingsToThingGroupParamsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnMitigationAction.EnableIoTLoggingParamsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "log_level": "logLevel",
            "role_arn_for_logging": "roleArnForLogging",
        },
    )
    class EnableIoTLoggingParamsProperty:
        def __init__(
            self,
            *,
            log_level: builtins.str,
            role_arn_for_logging: builtins.str,
        ) -> None:
            '''Parameters used when defining a mitigation action that enable AWS IoT Core logging.

            :param log_level: Specifies the type of information to be logged.
            :param role_arn_for_logging: The Amazon Resource Name (ARN) of the IAM role used for logging.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-enableiotloggingparams.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                enable_io_tLogging_params_property = iot.CfnMitigationAction.EnableIoTLoggingParamsProperty(
                    log_level="logLevel",
                    role_arn_for_logging="roleArnForLogging"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__05f7fa9ace7eb3c7a73e5554fe913bffeda246838ad56cfeb2a6663babf21713)
                check_type(argname="argument log_level", value=log_level, expected_type=type_hints["log_level"])
                check_type(argname="argument role_arn_for_logging", value=role_arn_for_logging, expected_type=type_hints["role_arn_for_logging"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "log_level": log_level,
                "role_arn_for_logging": role_arn_for_logging,
            }

        @builtins.property
        def log_level(self) -> builtins.str:
            '''Specifies the type of information to be logged.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-enableiotloggingparams.html#cfn-iot-mitigationaction-enableiotloggingparams-loglevel
            '''
            result = self._values.get("log_level")
            assert result is not None, "Required property 'log_level' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn_for_logging(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the IAM role used for logging.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-enableiotloggingparams.html#cfn-iot-mitigationaction-enableiotloggingparams-rolearnforlogging
            '''
            result = self._values.get("role_arn_for_logging")
            assert result is not None, "Required property 'role_arn_for_logging' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EnableIoTLoggingParamsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnMitigationAction.PublishFindingToSnsParamsProperty",
        jsii_struct_bases=[],
        name_mapping={"topic_arn": "topicArn"},
    )
    class PublishFindingToSnsParamsProperty:
        def __init__(self, *, topic_arn: builtins.str) -> None:
            '''Parameters to define a mitigation action that publishes findings to Amazon SNS.

            You can implement your own custom actions in response to the Amazon SNS messages.

            :param topic_arn: The ARN of the topic to which you want to publish the findings.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-publishfindingtosnsparams.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                publish_finding_to_sns_params_property = iot.CfnMitigationAction.PublishFindingToSnsParamsProperty(
                    topic_arn="topicArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f7f908687b0442f75f713201d9dc73aab0b0bc6353a45aeef5fd76eaaa8819f8)
                check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "topic_arn": topic_arn,
            }

        @builtins.property
        def topic_arn(self) -> builtins.str:
            '''The ARN of the topic to which you want to publish the findings.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-publishfindingtosnsparams.html#cfn-iot-mitigationaction-publishfindingtosnsparams-topicarn
            '''
            result = self._values.get("topic_arn")
            assert result is not None, "Required property 'topic_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PublishFindingToSnsParamsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnMitigationAction.ReplaceDefaultPolicyVersionParamsProperty",
        jsii_struct_bases=[],
        name_mapping={"template_name": "templateName"},
    )
    class ReplaceDefaultPolicyVersionParamsProperty:
        def __init__(self, *, template_name: builtins.str) -> None:
            '''Parameters to define a mitigation action that adds a blank policy to restrict permissions.

            :param template_name: The name of the template to be applied. The only supported value is ``BLANK_POLICY`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-replacedefaultpolicyversionparams.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                replace_default_policy_version_params_property = iot.CfnMitigationAction.ReplaceDefaultPolicyVersionParamsProperty(
                    template_name="templateName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4fec333637e63c1005e865ee0a0f9d57f3c2e2480eead909c426c912d58979d3)
                check_type(argname="argument template_name", value=template_name, expected_type=type_hints["template_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "template_name": template_name,
            }

        @builtins.property
        def template_name(self) -> builtins.str:
            '''The name of the template to be applied.

            The only supported value is ``BLANK_POLICY`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-replacedefaultpolicyversionparams.html#cfn-iot-mitigationaction-replacedefaultpolicyversionparams-templatename
            '''
            result = self._values.get("template_name")
            assert result is not None, "Required property 'template_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ReplaceDefaultPolicyVersionParamsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnMitigationAction.UpdateCACertificateParamsProperty",
        jsii_struct_bases=[],
        name_mapping={"action": "action"},
    )
    class UpdateCACertificateParamsProperty:
        def __init__(self, *, action: builtins.str) -> None:
            '''Parameters to define a mitigation action that changes the state of the CA certificate to inactive.

            :param action: The action that you want to apply to the CA certificate. The only supported value is ``DEACTIVATE`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-updatecacertificateparams.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                update_cACertificate_params_property = iot.CfnMitigationAction.UpdateCACertificateParamsProperty(
                    action="action"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7d555f0718607bfbd2097eabd0431f4fce4106de8ed10abcb5949490b3baf2a6)
                check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "action": action,
            }

        @builtins.property
        def action(self) -> builtins.str:
            '''The action that you want to apply to the CA certificate.

            The only supported value is ``DEACTIVATE`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-updatecacertificateparams.html#cfn-iot-mitigationaction-updatecacertificateparams-action
            '''
            result = self._values.get("action")
            assert result is not None, "Required property 'action' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UpdateCACertificateParamsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnMitigationAction.UpdateDeviceCertificateParamsProperty",
        jsii_struct_bases=[],
        name_mapping={"action": "action"},
    )
    class UpdateDeviceCertificateParamsProperty:
        def __init__(self, *, action: builtins.str) -> None:
            '''Parameters to define a mitigation action that changes the state of the device certificate to inactive.

            :param action: The action that you want to apply to the device certificate. The only supported value is ``DEACTIVATE`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-updatedevicecertificateparams.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                update_device_certificate_params_property = iot.CfnMitigationAction.UpdateDeviceCertificateParamsProperty(
                    action="action"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4466ace39cb892646bcec1de381f51023676ca4ddb2c9d87e502df660d1cf46d)
                check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "action": action,
            }

        @builtins.property
        def action(self) -> builtins.str:
            '''The action that you want to apply to the device certificate.

            The only supported value is ``DEACTIVATE`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-mitigationaction-updatedevicecertificateparams.html#cfn-iot-mitigationaction-updatedevicecertificateparams-action
            '''
            result = self._values.get("action")
            assert result is not None, "Required property 'action' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UpdateDeviceCertificateParamsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_iot.CfnMitigationActionProps",
    jsii_struct_bases=[],
    name_mapping={
        "action_params": "actionParams",
        "role_arn": "roleArn",
        "action_name": "actionName",
        "tags": "tags",
    },
)
class CfnMitigationActionProps:
    def __init__(
        self,
        *,
        action_params: typing.Union[typing.Union[CfnMitigationAction.ActionParamsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
        role_arn: builtins.str,
        action_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnMitigationAction``.

        :param action_params: The set of parameters for this mitigation action. The parameters vary, depending on the kind of action you apply.
        :param role_arn: The IAM role ARN used to apply this mitigation action.
        :param action_name: The friendly name of the mitigation action.
        :param tags: Metadata that can be used to manage the mitigation action.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-mitigationaction.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_iot as iot
            
            cfn_mitigation_action_props = iot.CfnMitigationActionProps(
                action_params=iot.CfnMitigationAction.ActionParamsProperty(
                    add_things_to_thing_group_params=iot.CfnMitigationAction.AddThingsToThingGroupParamsProperty(
                        thing_group_names=["thingGroupNames"],
            
                        # the properties below are optional
                        override_dynamic_groups=False
                    ),
                    enable_io_tLogging_params=iot.CfnMitigationAction.EnableIoTLoggingParamsProperty(
                        log_level="logLevel",
                        role_arn_for_logging="roleArnForLogging"
                    ),
                    publish_finding_to_sns_params=iot.CfnMitigationAction.PublishFindingToSnsParamsProperty(
                        topic_arn="topicArn"
                    ),
                    replace_default_policy_version_params=iot.CfnMitigationAction.ReplaceDefaultPolicyVersionParamsProperty(
                        template_name="templateName"
                    ),
                    update_ca_certificate_params=iot.CfnMitigationAction.UpdateCACertificateParamsProperty(
                        action="action"
                    ),
                    update_device_certificate_params=iot.CfnMitigationAction.UpdateDeviceCertificateParamsProperty(
                        action="action"
                    )
                ),
                role_arn="roleArn",
            
                # the properties below are optional
                action_name="actionName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fc8df50d6a3c464d38587d33fb0412fafefeab7fc91aacd7771d258f6ef3612)
            check_type(argname="argument action_params", value=action_params, expected_type=type_hints["action_params"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument action_name", value=action_name, expected_type=type_hints["action_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action_params": action_params,
            "role_arn": role_arn,
        }
        if action_name is not None:
            self._values["action_name"] = action_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def action_params(
        self,
    ) -> typing.Union[CfnMitigationAction.ActionParamsProperty, _IResolvable_a771d0ef]:
        '''The set of parameters for this mitigation action.

        The parameters vary, depending on the kind of action you apply.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-mitigationaction.html#cfn-iot-mitigationaction-actionparams
        '''
        result = self._values.get("action_params")
        assert result is not None, "Required property 'action_params' is missing"
        return typing.cast(typing.Union[CfnMitigationAction.ActionParamsProperty, _IResolvable_a771d0ef], result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The IAM role ARN used to apply this mitigation action.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-mitigationaction.html#cfn-iot-mitigationaction-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def action_name(self) -> typing.Optional[builtins.str]:
        '''The friendly name of the mitigation action.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-mitigationaction.html#cfn-iot-mitigationaction-actionname
        '''
        result = self._values.get("action_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''Metadata that can be used to manage the mitigation action.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-mitigationaction.html#cfn-iot-mitigationaction-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMitigationActionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnPolicy(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iot.CfnPolicy",
):
    '''A CloudFormation ``AWS::IoT::Policy``.

    Use the ``AWS::IoT::Policy`` resource to declare an AWS IoT policy. For more information about working with AWS IoT policies, see `Authorization <https://docs.aws.amazon.com/iot/latest/developerguide/authorization.html>`_ in the *AWS IoT Developer Guide* .

    :cloudformationResource: AWS::IoT::Policy
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-policy.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_iot as iot
        
        # policy_document: Any
        
        cfn_policy = iot.CfnPolicy(self, "MyCfnPolicy",
            policy_document=policy_document,
        
            # the properties below are optional
            policy_name="policyName"
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        policy_document: typing.Any,
        policy_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::IoT::Policy``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param policy_document: The JSON document that describes the policy.
        :param policy_name: The policy name.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af5396a485d06b911d0023fd01f96d6bccbf23d00fe1558193b3debd143c3aef)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPolicyProps(
            policy_document=policy_document, policy_name=policy_name
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53e20aef529a293726b05d79c8367efb6a9f652f4121e6e59e1e208d1ede2365)
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
            type_hints = typing.get_type_hints(_typecheckingstub__82df28135aafb896b5052677a10e0ad0cc0a76c5f04bbf6abb6f452d4874b98b)
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
        '''The Amazon Resource Name (ARN) of the AWS IoT policy, such as ``arn:aws:iot:us-east-2:123456789012:policy/MyPolicy`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The name of this policy.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="policyDocument")
    def policy_document(self) -> typing.Any:
        '''The JSON document that describes the policy.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-policy.html#cfn-iot-policy-policydocument
        '''
        return typing.cast(typing.Any, jsii.get(self, "policyDocument"))

    @policy_document.setter
    def policy_document(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__971b0e779eec8b37c0aa0435e6ef8b6ec5c7102da4dee086f6f99109566ff118)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyDocument", value)

    @builtins.property
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> typing.Optional[builtins.str]:
        '''The policy name.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-policy.html#cfn-iot-policy-policyname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyName"))

    @policy_name.setter
    def policy_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d3ebbb610b1e68e94230fc11112a30bdf72a5f815e7442068d98ea3dd83f62b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyName", value)


@jsii.implements(_IInspectable_82c04a63)
class CfnPolicyPrincipalAttachment(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iot.CfnPolicyPrincipalAttachment",
):
    '''A CloudFormation ``AWS::IoT::PolicyPrincipalAttachment``.

    Use the ``AWS::IoT::PolicyPrincipalAttachment`` resource to attach an AWS IoT policy to a principal (an X.509 certificate or other credential).

    For information about working with AWS IoT policies and principals, see `Authorization <https://docs.aws.amazon.com/iot/latest/developerguide/authorization.html>`_ in the *AWS IoT Developer Guide* .

    :cloudformationResource: AWS::IoT::PolicyPrincipalAttachment
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-policyprincipalattachment.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_iot as iot
        
        cfn_policy_principal_attachment = iot.CfnPolicyPrincipalAttachment(self, "MyCfnPolicyPrincipalAttachment",
            policy_name="policyName",
            principal="principal"
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        policy_name: builtins.str,
        principal: builtins.str,
    ) -> None:
        '''Create a new ``AWS::IoT::PolicyPrincipalAttachment``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param policy_name: The name of the AWS IoT policy.
        :param principal: The principal, which can be a certificate ARN (as returned from the ``CreateCertificate`` operation) or an Amazon Cognito ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac497ff31455c302c3f5d97976877d66385ffe9c8e6e48d65de13104f7b0cac6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPolicyPrincipalAttachmentProps(
            policy_name=policy_name, principal=principal
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df9723249134a9366075c700cc71ceba31c3ab1430d67a749ffd155f44a0604a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5c6ebcf3653574963142342336ce4413f7f6d3817513511c4f7968747b9f9d4b)
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
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> builtins.str:
        '''The name of the AWS IoT policy.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-policyprincipalattachment.html#cfn-iot-policyprincipalattachment-policyname
        '''
        return typing.cast(builtins.str, jsii.get(self, "policyName"))

    @policy_name.setter
    def policy_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb834eb03939d2519ba3fe596d8aa6670002d89315b5315ba47fd581b62f5005)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyName", value)

    @builtins.property
    @jsii.member(jsii_name="principal")
    def principal(self) -> builtins.str:
        '''The principal, which can be a certificate ARN (as returned from the ``CreateCertificate`` operation) or an Amazon Cognito ID.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-policyprincipalattachment.html#cfn-iot-policyprincipalattachment-principal
        '''
        return typing.cast(builtins.str, jsii.get(self, "principal"))

    @principal.setter
    def principal(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f0f4dacfed464c52f4b1f63a29b3c0dde9beebee28bb3fb2e393a9f184b4bea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "principal", value)


@jsii.data_type(
    jsii_type="monocdk.aws_iot.CfnPolicyPrincipalAttachmentProps",
    jsii_struct_bases=[],
    name_mapping={"policy_name": "policyName", "principal": "principal"},
)
class CfnPolicyPrincipalAttachmentProps:
    def __init__(self, *, policy_name: builtins.str, principal: builtins.str) -> None:
        '''Properties for defining a ``CfnPolicyPrincipalAttachment``.

        :param policy_name: The name of the AWS IoT policy.
        :param principal: The principal, which can be a certificate ARN (as returned from the ``CreateCertificate`` operation) or an Amazon Cognito ID.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-policyprincipalattachment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_iot as iot
            
            cfn_policy_principal_attachment_props = iot.CfnPolicyPrincipalAttachmentProps(
                policy_name="policyName",
                principal="principal"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e33e6624c7935fc745022194b588c823cf604dad86124deb914487d6c8f0ca40)
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
            check_type(argname="argument principal", value=principal, expected_type=type_hints["principal"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy_name": policy_name,
            "principal": principal,
        }

    @builtins.property
    def policy_name(self) -> builtins.str:
        '''The name of the AWS IoT policy.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-policyprincipalattachment.html#cfn-iot-policyprincipalattachment-policyname
        '''
        result = self._values.get("policy_name")
        assert result is not None, "Required property 'policy_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def principal(self) -> builtins.str:
        '''The principal, which can be a certificate ARN (as returned from the ``CreateCertificate`` operation) or an Amazon Cognito ID.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-policyprincipalattachment.html#cfn-iot-policyprincipalattachment-principal
        '''
        result = self._values.get("principal")
        assert result is not None, "Required property 'principal' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPolicyPrincipalAttachmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_iot.CfnPolicyProps",
    jsii_struct_bases=[],
    name_mapping={"policy_document": "policyDocument", "policy_name": "policyName"},
)
class CfnPolicyProps:
    def __init__(
        self,
        *,
        policy_document: typing.Any,
        policy_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnPolicy``.

        :param policy_document: The JSON document that describes the policy.
        :param policy_name: The policy name.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-policy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_iot as iot
            
            # policy_document: Any
            
            cfn_policy_props = iot.CfnPolicyProps(
                policy_document=policy_document,
            
                # the properties below are optional
                policy_name="policyName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d2cfeb79448e99f155b4adbba540852e9fce0ec72e1393a4ed63a785bd25c56)
            check_type(argname="argument policy_document", value=policy_document, expected_type=type_hints["policy_document"])
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy_document": policy_document,
        }
        if policy_name is not None:
            self._values["policy_name"] = policy_name

    @builtins.property
    def policy_document(self) -> typing.Any:
        '''The JSON document that describes the policy.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-policy.html#cfn-iot-policy-policydocument
        '''
        result = self._values.get("policy_document")
        assert result is not None, "Required property 'policy_document' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def policy_name(self) -> typing.Optional[builtins.str]:
        '''The policy name.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-policy.html#cfn-iot-policy-policyname
        '''
        result = self._values.get("policy_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnProvisioningTemplate(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iot.CfnProvisioningTemplate",
):
    '''A CloudFormation ``AWS::IoT::ProvisioningTemplate``.

    Creates a fleet provisioning template.

    :cloudformationResource: AWS::IoT::ProvisioningTemplate
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_iot as iot
        
        cfn_provisioning_template = iot.CfnProvisioningTemplate(self, "MyCfnProvisioningTemplate",
            provisioning_role_arn="provisioningRoleArn",
            template_body="templateBody",
        
            # the properties below are optional
            description="description",
            enabled=False,
            pre_provisioning_hook=iot.CfnProvisioningTemplate.ProvisioningHookProperty(
                payload_version="payloadVersion",
                target_arn="targetArn"
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            template_name="templateName",
            template_type="templateType"
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        provisioning_role_arn: builtins.str,
        template_body: builtins.str,
        description: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        pre_provisioning_hook: typing.Optional[typing.Union[typing.Union["CfnProvisioningTemplate.ProvisioningHookProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
        template_name: typing.Optional[builtins.str] = None,
        template_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::IoT::ProvisioningTemplate``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param provisioning_role_arn: The role ARN for the role associated with the fleet provisioning template. This IoT role grants permission to provision a device.
        :param template_body: The JSON formatted contents of the fleet provisioning template version.
        :param description: The description of the fleet provisioning template.
        :param enabled: True to enable the fleet provisioning template, otherwise false.
        :param pre_provisioning_hook: Creates a pre-provisioning hook template.
        :param tags: Metadata that can be used to manage the fleet provisioning template.
        :param template_name: The name of the fleet provisioning template.
        :param template_type: The type of the provisioning template.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9cc379a1ac891d551f4dd43074a18069d69b0c3fa87a57b9cc09378518c3778)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnProvisioningTemplateProps(
            provisioning_role_arn=provisioning_role_arn,
            template_body=template_body,
            description=description,
            enabled=enabled,
            pre_provisioning_hook=pre_provisioning_hook,
            tags=tags,
            template_name=template_name,
            template_type=template_type,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db44932761309b6e1a448d9599affc21d9ef0bfd84014cddc94d66f4f11c4f48)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b2eba7d4a89a9f98d642f943528919e2343c5f422e0d9aef4c29b8c4878576fe)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrTemplateArn")
    def attr_template_arn(self) -> builtins.str:
        '''The ARN that identifies the provisioning template.

        :cloudformationAttribute: TemplateArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTemplateArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''Metadata that can be used to manage the fleet provisioning template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="provisioningRoleArn")
    def provisioning_role_arn(self) -> builtins.str:
        '''The role ARN for the role associated with the fleet provisioning template.

        This IoT role grants permission to provision a device.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-provisioningrolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "provisioningRoleArn"))

    @provisioning_role_arn.setter
    def provisioning_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce7231928f866847628df1fe1e1e64990553e8881b20092ab8939eae488913e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "provisioningRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="templateBody")
    def template_body(self) -> builtins.str:
        '''The JSON formatted contents of the fleet provisioning template version.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-templatebody
        '''
        return typing.cast(builtins.str, jsii.get(self, "templateBody"))

    @template_body.setter
    def template_body(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a275b33144106516b375d8d61597ab9bcb7a1b4997205f0a6b6f4c2151f3208)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateBody", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the fleet provisioning template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__709e3ddacbcf322681536c9d4f2b7862d26b2ccb1fde77c5f70dff1fb2d786b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''True to enable the fleet provisioning template, otherwise false.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-enabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__144346abf7a2c6c786889ad3638d66abf972abf34701eab01175689d3e14c74d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="preProvisioningHook")
    def pre_provisioning_hook(
        self,
    ) -> typing.Optional[typing.Union["CfnProvisioningTemplate.ProvisioningHookProperty", _IResolvable_a771d0ef]]:
        '''Creates a pre-provisioning hook template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-preprovisioninghook
        '''
        return typing.cast(typing.Optional[typing.Union["CfnProvisioningTemplate.ProvisioningHookProperty", _IResolvable_a771d0ef]], jsii.get(self, "preProvisioningHook"))

    @pre_provisioning_hook.setter
    def pre_provisioning_hook(
        self,
        value: typing.Optional[typing.Union["CfnProvisioningTemplate.ProvisioningHookProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f615ebe2c6a99e480d5cc80583dd1024ff0b766c4f3e8ce87f6a4f8d6a627e17)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preProvisioningHook", value)

    @builtins.property
    @jsii.member(jsii_name="templateName")
    def template_name(self) -> typing.Optional[builtins.str]:
        '''The name of the fleet provisioning template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-templatename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateName"))

    @template_name.setter
    def template_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df7d9da4fb073d9d10200ca7eae4ef56af4e6316944ed07d2eb3a02f6a54ca36)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateName", value)

    @builtins.property
    @jsii.member(jsii_name="templateType")
    def template_type(self) -> typing.Optional[builtins.str]:
        '''The type of the provisioning template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-templatetype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateType"))

    @template_type.setter
    def template_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9662c4fc1f9f14bccfe451083d889f9579df91e99a3d1a5abfbbbeb1a125d58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateType", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnProvisioningTemplate.ProvisioningHookProperty",
        jsii_struct_bases=[],
        name_mapping={"payload_version": "payloadVersion", "target_arn": "targetArn"},
    )
    class ProvisioningHookProperty:
        def __init__(
            self,
            *,
            payload_version: typing.Optional[builtins.str] = None,
            target_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Structure that contains payloadVersion and targetArn.

            Provisioning hooks can be used when fleet provisioning to validate device parameters before allowing the device to be provisioned.

            :param payload_version: The payload that was sent to the target function. The valid payload is ``"2020-04-01"`` .
            :param target_arn: The ARN of the target function.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-provisioningtemplate-provisioninghook.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                provisioning_hook_property = iot.CfnProvisioningTemplate.ProvisioningHookProperty(
                    payload_version="payloadVersion",
                    target_arn="targetArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2ced81513ed1957f556d89b411e507b5b7f3262f84b6619f9095c2291d19dc49)
                check_type(argname="argument payload_version", value=payload_version, expected_type=type_hints["payload_version"])
                check_type(argname="argument target_arn", value=target_arn, expected_type=type_hints["target_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if payload_version is not None:
                self._values["payload_version"] = payload_version
            if target_arn is not None:
                self._values["target_arn"] = target_arn

        @builtins.property
        def payload_version(self) -> typing.Optional[builtins.str]:
            '''The payload that was sent to the target function.

            The valid payload is ``"2020-04-01"`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-provisioningtemplate-provisioninghook.html#cfn-iot-provisioningtemplate-provisioninghook-payloadversion
            '''
            result = self._values.get("payload_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the target function.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-provisioningtemplate-provisioninghook.html#cfn-iot-provisioningtemplate-provisioninghook-targetarn
            '''
            result = self._values.get("target_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProvisioningHookProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_iot.CfnProvisioningTemplateProps",
    jsii_struct_bases=[],
    name_mapping={
        "provisioning_role_arn": "provisioningRoleArn",
        "template_body": "templateBody",
        "description": "description",
        "enabled": "enabled",
        "pre_provisioning_hook": "preProvisioningHook",
        "tags": "tags",
        "template_name": "templateName",
        "template_type": "templateType",
    },
)
class CfnProvisioningTemplateProps:
    def __init__(
        self,
        *,
        provisioning_role_arn: builtins.str,
        template_body: builtins.str,
        description: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        pre_provisioning_hook: typing.Optional[typing.Union[typing.Union[CfnProvisioningTemplate.ProvisioningHookProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
        template_name: typing.Optional[builtins.str] = None,
        template_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnProvisioningTemplate``.

        :param provisioning_role_arn: The role ARN for the role associated with the fleet provisioning template. This IoT role grants permission to provision a device.
        :param template_body: The JSON formatted contents of the fleet provisioning template version.
        :param description: The description of the fleet provisioning template.
        :param enabled: True to enable the fleet provisioning template, otherwise false.
        :param pre_provisioning_hook: Creates a pre-provisioning hook template.
        :param tags: Metadata that can be used to manage the fleet provisioning template.
        :param template_name: The name of the fleet provisioning template.
        :param template_type: The type of the provisioning template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_iot as iot
            
            cfn_provisioning_template_props = iot.CfnProvisioningTemplateProps(
                provisioning_role_arn="provisioningRoleArn",
                template_body="templateBody",
            
                # the properties below are optional
                description="description",
                enabled=False,
                pre_provisioning_hook=iot.CfnProvisioningTemplate.ProvisioningHookProperty(
                    payload_version="payloadVersion",
                    target_arn="targetArn"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                template_name="templateName",
                template_type="templateType"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d7209c01d71f034e1ef126539867cffa0b106104e703cd3a3729b6a17941714)
            check_type(argname="argument provisioning_role_arn", value=provisioning_role_arn, expected_type=type_hints["provisioning_role_arn"])
            check_type(argname="argument template_body", value=template_body, expected_type=type_hints["template_body"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument pre_provisioning_hook", value=pre_provisioning_hook, expected_type=type_hints["pre_provisioning_hook"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument template_name", value=template_name, expected_type=type_hints["template_name"])
            check_type(argname="argument template_type", value=template_type, expected_type=type_hints["template_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "provisioning_role_arn": provisioning_role_arn,
            "template_body": template_body,
        }
        if description is not None:
            self._values["description"] = description
        if enabled is not None:
            self._values["enabled"] = enabled
        if pre_provisioning_hook is not None:
            self._values["pre_provisioning_hook"] = pre_provisioning_hook
        if tags is not None:
            self._values["tags"] = tags
        if template_name is not None:
            self._values["template_name"] = template_name
        if template_type is not None:
            self._values["template_type"] = template_type

    @builtins.property
    def provisioning_role_arn(self) -> builtins.str:
        '''The role ARN for the role associated with the fleet provisioning template.

        This IoT role grants permission to provision a device.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-provisioningrolearn
        '''
        result = self._values.get("provisioning_role_arn")
        assert result is not None, "Required property 'provisioning_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def template_body(self) -> builtins.str:
        '''The JSON formatted contents of the fleet provisioning template version.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-templatebody
        '''
        result = self._values.get("template_body")
        assert result is not None, "Required property 'template_body' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the fleet provisioning template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''True to enable the fleet provisioning template, otherwise false.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

    @builtins.property
    def pre_provisioning_hook(
        self,
    ) -> typing.Optional[typing.Union[CfnProvisioningTemplate.ProvisioningHookProperty, _IResolvable_a771d0ef]]:
        '''Creates a pre-provisioning hook template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-preprovisioninghook
        '''
        result = self._values.get("pre_provisioning_hook")
        return typing.cast(typing.Optional[typing.Union[CfnProvisioningTemplate.ProvisioningHookProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''Metadata that can be used to manage the fleet provisioning template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    @builtins.property
    def template_name(self) -> typing.Optional[builtins.str]:
        '''The name of the fleet provisioning template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-templatename
        '''
        result = self._values.get("template_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def template_type(self) -> typing.Optional[builtins.str]:
        '''The type of the provisioning template.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-provisioningtemplate.html#cfn-iot-provisioningtemplate-templatetype
        '''
        result = self._values.get("template_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnProvisioningTemplateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnResourceSpecificLogging(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iot.CfnResourceSpecificLogging",
):
    '''A CloudFormation ``AWS::IoT::ResourceSpecificLogging``.

    Configure resource-specific logging.

    :cloudformationResource: AWS::IoT::ResourceSpecificLogging
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-resourcespecificlogging.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_iot as iot
        
        cfn_resource_specific_logging = iot.CfnResourceSpecificLogging(self, "MyCfnResourceSpecificLogging",
            log_level="logLevel",
            target_name="targetName",
            target_type="targetType"
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        log_level: builtins.str,
        target_name: builtins.str,
        target_type: builtins.str,
    ) -> None:
        '''Create a new ``AWS::IoT::ResourceSpecificLogging``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param log_level: The default log level.Valid Values: ``DEBUG | INFO | ERROR | WARN | DISABLED``.
        :param target_name: The target name.
        :param target_type: The target type. Valid Values: ``DEFAULT | THING_GROUP``
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b630339211723668b81832f3589aadce7d440e95a66ff9190e836691c68ad7f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnResourceSpecificLoggingProps(
            log_level=log_level, target_name=target_name, target_type=target_type
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce57de0b056fe68d516ef24518dd87de2e21033a636385f3a350cc1ff6897b3c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f198563162ee2533a2e8218b93d8c549d273ee2b89a7156db39fddfb82af7981)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrTargetId")
    def attr_target_id(self) -> builtins.str:
        '''The target Id.

        :cloudformationAttribute: TargetId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTargetId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="logLevel")
    def log_level(self) -> builtins.str:
        '''The default log level.Valid Values: ``DEBUG | INFO | ERROR | WARN | DISABLED``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-resourcespecificlogging.html#cfn-iot-resourcespecificlogging-loglevel
        '''
        return typing.cast(builtins.str, jsii.get(self, "logLevel"))

    @log_level.setter
    def log_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4236a35b9182532e90fdf5fc6ca8887a821bc52797a4fd87022341b742e2fa7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logLevel", value)

    @builtins.property
    @jsii.member(jsii_name="targetName")
    def target_name(self) -> builtins.str:
        '''The target name.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-resourcespecificlogging.html#cfn-iot-resourcespecificlogging-targetname
        '''
        return typing.cast(builtins.str, jsii.get(self, "targetName"))

    @target_name.setter
    def target_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__110b57edcb8597286159cf6b3bfdc4b13bf91793090681c58863143b68ca3399)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetName", value)

    @builtins.property
    @jsii.member(jsii_name="targetType")
    def target_type(self) -> builtins.str:
        '''The target type.

        Valid Values: ``DEFAULT | THING_GROUP``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-resourcespecificlogging.html#cfn-iot-resourcespecificlogging-targettype
        '''
        return typing.cast(builtins.str, jsii.get(self, "targetType"))

    @target_type.setter
    def target_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08be4bc56c419c342f967853f024b6173cb19a5ef182c8677881a595c83b4905)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetType", value)


@jsii.data_type(
    jsii_type="monocdk.aws_iot.CfnResourceSpecificLoggingProps",
    jsii_struct_bases=[],
    name_mapping={
        "log_level": "logLevel",
        "target_name": "targetName",
        "target_type": "targetType",
    },
)
class CfnResourceSpecificLoggingProps:
    def __init__(
        self,
        *,
        log_level: builtins.str,
        target_name: builtins.str,
        target_type: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnResourceSpecificLogging``.

        :param log_level: The default log level.Valid Values: ``DEBUG | INFO | ERROR | WARN | DISABLED``.
        :param target_name: The target name.
        :param target_type: The target type. Valid Values: ``DEFAULT | THING_GROUP``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-resourcespecificlogging.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_iot as iot
            
            cfn_resource_specific_logging_props = iot.CfnResourceSpecificLoggingProps(
                log_level="logLevel",
                target_name="targetName",
                target_type="targetType"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7e369880521489546f5efd2fe7aa3cfb1018673c148bed120d073246cc2ea60)
            check_type(argname="argument log_level", value=log_level, expected_type=type_hints["log_level"])
            check_type(argname="argument target_name", value=target_name, expected_type=type_hints["target_name"])
            check_type(argname="argument target_type", value=target_type, expected_type=type_hints["target_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "log_level": log_level,
            "target_name": target_name,
            "target_type": target_type,
        }

    @builtins.property
    def log_level(self) -> builtins.str:
        '''The default log level.Valid Values: ``DEBUG | INFO | ERROR | WARN | DISABLED``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-resourcespecificlogging.html#cfn-iot-resourcespecificlogging-loglevel
        '''
        result = self._values.get("log_level")
        assert result is not None, "Required property 'log_level' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_name(self) -> builtins.str:
        '''The target name.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-resourcespecificlogging.html#cfn-iot-resourcespecificlogging-targetname
        '''
        result = self._values.get("target_name")
        assert result is not None, "Required property 'target_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_type(self) -> builtins.str:
        '''The target type.

        Valid Values: ``DEFAULT | THING_GROUP``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-resourcespecificlogging.html#cfn-iot-resourcespecificlogging-targettype
        '''
        result = self._values.get("target_type")
        assert result is not None, "Required property 'target_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourceSpecificLoggingProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnRoleAlias(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iot.CfnRoleAlias",
):
    '''A CloudFormation ``AWS::IoT::RoleAlias``.

    Specifies a role alias.

    Requires permission to access the `CreateRoleAlias <https://docs.aws.amazon.com//service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions>`_ action.

    :cloudformationResource: AWS::IoT::RoleAlias
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-rolealias.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_iot as iot
        
        cfn_role_alias = iot.CfnRoleAlias(self, "MyCfnRoleAlias",
            role_arn="roleArn",
        
            # the properties below are optional
            credential_duration_seconds=123,
            role_alias="roleAlias",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        role_arn: builtins.str,
        credential_duration_seconds: typing.Optional[jsii.Number] = None,
        role_alias: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::IoT::RoleAlias``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param role_arn: The role ARN.
        :param credential_duration_seconds: The number of seconds for which the credential is valid.
        :param role_alias: The role alias.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4054758ae03efbb17f6b2c6ad952998ead4507c822323e611a58e9bbeb1c41c3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRoleAliasProps(
            role_arn=role_arn,
            credential_duration_seconds=credential_duration_seconds,
            role_alias=role_alias,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d71d161e9e9bc6ac5e0f16c3724d03afac9f415429209e5476bd64fa5ef8f1cd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5581e88d9608f5b289626bd63d21b8d7e9ddf098f0a5246492253404fd1a22a1)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrRoleAliasArn")
    def attr_role_alias_arn(self) -> builtins.str:
        '''The role alias ARN.

        :cloudformationAttribute: RoleAliasArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRoleAliasArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-rolealias.html#cfn-iot-rolealias-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The role ARN.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-rolealias.html#cfn-iot-rolealias-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b393bdc20e656c9c176563207b0a1c34b4c0652f49ac4de2a4ac05a71f936de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="credentialDurationSeconds")
    def credential_duration_seconds(self) -> typing.Optional[jsii.Number]:
        '''The number of seconds for which the credential is valid.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-rolealias.html#cfn-iot-rolealias-credentialdurationseconds
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "credentialDurationSeconds"))

    @credential_duration_seconds.setter
    def credential_duration_seconds(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__727fc005a29230d173f1f2d17596fc79d75c2d2edcddd2661c8a3a4a389b5bd4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "credentialDurationSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="roleAlias")
    def role_alias(self) -> typing.Optional[builtins.str]:
        '''The role alias.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-rolealias.html#cfn-iot-rolealias-rolealias
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleAlias"))

    @role_alias.setter
    def role_alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6749616f338b8776ffd9a84feb62cad4f5bb9b8588bdebfaf1098825e1172c42)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleAlias", value)


@jsii.data_type(
    jsii_type="monocdk.aws_iot.CfnRoleAliasProps",
    jsii_struct_bases=[],
    name_mapping={
        "role_arn": "roleArn",
        "credential_duration_seconds": "credentialDurationSeconds",
        "role_alias": "roleAlias",
        "tags": "tags",
    },
)
class CfnRoleAliasProps:
    def __init__(
        self,
        *,
        role_arn: builtins.str,
        credential_duration_seconds: typing.Optional[jsii.Number] = None,
        role_alias: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRoleAlias``.

        :param role_arn: The role ARN.
        :param credential_duration_seconds: The number of seconds for which the credential is valid.
        :param role_alias: The role alias.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-rolealias.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_iot as iot
            
            cfn_role_alias_props = iot.CfnRoleAliasProps(
                role_arn="roleArn",
            
                # the properties below are optional
                credential_duration_seconds=123,
                role_alias="roleAlias",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0c438605fdb7e9c3c6f22adbd92eaf20aa767385dcaae9a850f9aecbc273774)
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument credential_duration_seconds", value=credential_duration_seconds, expected_type=type_hints["credential_duration_seconds"])
            check_type(argname="argument role_alias", value=role_alias, expected_type=type_hints["role_alias"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "role_arn": role_arn,
        }
        if credential_duration_seconds is not None:
            self._values["credential_duration_seconds"] = credential_duration_seconds
        if role_alias is not None:
            self._values["role_alias"] = role_alias
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The role ARN.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-rolealias.html#cfn-iot-rolealias-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def credential_duration_seconds(self) -> typing.Optional[jsii.Number]:
        '''The number of seconds for which the credential is valid.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-rolealias.html#cfn-iot-rolealias-credentialdurationseconds
        '''
        result = self._values.get("credential_duration_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def role_alias(self) -> typing.Optional[builtins.str]:
        '''The role alias.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-rolealias.html#cfn-iot-rolealias-rolealias
        '''
        result = self._values.get("role_alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-rolealias.html#cfn-iot-rolealias-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRoleAliasProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnScheduledAudit(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iot.CfnScheduledAudit",
):
    '''A CloudFormation ``AWS::IoT::ScheduledAudit``.

    Use the ``AWS::IoT::ScheduledAudit`` resource to create a scheduled audit that is run at a specified time interval. For API reference, see `CreateScheduleAudit <https://docs.aws.amazon.com/iot/latest/apireference/API_CreateScheduledAudit.html>`_ and for general information, see `Audit <https://docs.aws.amazon.com/iot/latest/developerguide/device-defender-audit.html>`_ .

    :cloudformationResource: AWS::IoT::ScheduledAudit
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_iot as iot
        
        cfn_scheduled_audit = iot.CfnScheduledAudit(self, "MyCfnScheduledAudit",
            frequency="frequency",
            target_check_names=["targetCheckNames"],
        
            # the properties below are optional
            day_of_month="dayOfMonth",
            day_of_week="dayOfWeek",
            scheduled_audit_name="scheduledAuditName",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        frequency: builtins.str,
        target_check_names: typing.Sequence[builtins.str],
        day_of_month: typing.Optional[builtins.str] = None,
        day_of_week: typing.Optional[builtins.str] = None,
        scheduled_audit_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::IoT::ScheduledAudit``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param frequency: How often the scheduled audit occurs.
        :param target_check_names: Which checks are performed during the scheduled audit. Checks must be enabled for your account. (Use ``DescribeAccountAuditConfiguration`` to see the list of all checks, including those that are enabled or use ``UpdateAccountAuditConfiguration`` to select which checks are enabled.) The following checks are currently aviable: - ``AUTHENTICATED_COGNITO_ROLE_OVERLY_PERMISSIVE_CHECK`` - ``CA_CERTIFICATE_EXPIRING_CHECK`` - ``CA_CERTIFICATE_KEY_QUALITY_CHECK`` - ``CONFLICTING_CLIENT_IDS_CHECK`` - ``DEVICE_CERTIFICATE_EXPIRING_CHECK`` - ``DEVICE_CERTIFICATE_KEY_QUALITY_CHECK`` - ``DEVICE_CERTIFICATE_SHARED_CHECK`` - ``IOT_POLICY_OVERLY_PERMISSIVE_CHECK`` - ``IOT_ROLE_ALIAS_ALLOWS_ACCESS_TO_UNUSED_SERVICES_CHECK`` - ``IOT_ROLE_ALIAS_OVERLY_PERMISSIVE_CHECK`` - ``LOGGING_DISABLED_CHECK`` - ``REVOKED_CA_CERTIFICATE_STILL_ACTIVE_CHECK`` - ``REVOKED_DEVICE_CERTIFICATE_STILL_ACTIVE_CHECK`` - ``UNAUTHENTICATED_COGNITO_ROLE_OVERLY_PERMISSIVE_CHECK``
        :param day_of_month: The day of the month on which the scheduled audit is run (if the ``frequency`` is "MONTHLY"). If days 29-31 are specified, and the month does not have that many days, the audit takes place on the "LAST" day of the month.
        :param day_of_week: The day of the week on which the scheduled audit is run (if the ``frequency`` is "WEEKLY" or "BIWEEKLY").
        :param scheduled_audit_name: The name of the scheduled audit.
        :param tags: Metadata that can be used to manage the scheduled audit.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8ffb853881117918a35da2335f7aef38c4008a0dd5e49175120e6709e74fcf6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnScheduledAuditProps(
            frequency=frequency,
            target_check_names=target_check_names,
            day_of_month=day_of_month,
            day_of_week=day_of_week,
            scheduled_audit_name=scheduled_audit_name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aaf95edf172678e79abec7cc2a9b7664a3623041c9f3a6c096c42ef6a6743c25)
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
            type_hints = typing.get_type_hints(_typecheckingstub__32a2a9f2a819ccbb575e1143373a76dcc4b624254c9bbb8b11ac334cc1394e17)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrScheduledAuditArn")
    def attr_scheduled_audit_arn(self) -> builtins.str:
        '''The ARN of the scheduled audit.

        :cloudformationAttribute: ScheduledAuditArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrScheduledAuditArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''Metadata that can be used to manage the scheduled audit.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="frequency")
    def frequency(self) -> builtins.str:
        '''How often the scheduled audit occurs.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-frequency
        '''
        return typing.cast(builtins.str, jsii.get(self, "frequency"))

    @frequency.setter
    def frequency(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bafac4cea46b5f4f9231b34e778b3425457145e62114e7c110d25a9422342ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frequency", value)

    @builtins.property
    @jsii.member(jsii_name="targetCheckNames")
    def target_check_names(self) -> typing.List[builtins.str]:
        '''Which checks are performed during the scheduled audit.

        Checks must be enabled for your account. (Use ``DescribeAccountAuditConfiguration`` to see the list of all checks, including those that are enabled or use ``UpdateAccountAuditConfiguration`` to select which checks are enabled.)

        The following checks are currently aviable:

        - ``AUTHENTICATED_COGNITO_ROLE_OVERLY_PERMISSIVE_CHECK``
        - ``CA_CERTIFICATE_EXPIRING_CHECK``
        - ``CA_CERTIFICATE_KEY_QUALITY_CHECK``
        - ``CONFLICTING_CLIENT_IDS_CHECK``
        - ``DEVICE_CERTIFICATE_EXPIRING_CHECK``
        - ``DEVICE_CERTIFICATE_KEY_QUALITY_CHECK``
        - ``DEVICE_CERTIFICATE_SHARED_CHECK``
        - ``IOT_POLICY_OVERLY_PERMISSIVE_CHECK``
        - ``IOT_ROLE_ALIAS_ALLOWS_ACCESS_TO_UNUSED_SERVICES_CHECK``
        - ``IOT_ROLE_ALIAS_OVERLY_PERMISSIVE_CHECK``
        - ``LOGGING_DISABLED_CHECK``
        - ``REVOKED_CA_CERTIFICATE_STILL_ACTIVE_CHECK``
        - ``REVOKED_DEVICE_CERTIFICATE_STILL_ACTIVE_CHECK``
        - ``UNAUTHENTICATED_COGNITO_ROLE_OVERLY_PERMISSIVE_CHECK``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-targetchecknames
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "targetCheckNames"))

    @target_check_names.setter
    def target_check_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fee7a1476471d855c177f436f91235390e04d6cf7d1db5aef86e31812539662c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetCheckNames", value)

    @builtins.property
    @jsii.member(jsii_name="dayOfMonth")
    def day_of_month(self) -> typing.Optional[builtins.str]:
        '''The day of the month on which the scheduled audit is run (if the ``frequency`` is "MONTHLY").

        If days 29-31 are specified, and the month does not have that many days, the audit takes place on the "LAST" day of the month.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-dayofmonth
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dayOfMonth"))

    @day_of_month.setter
    def day_of_month(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__014dcae2cd55e3f55a56c8a01c0a263c4d4bb1108affa0377bc4c2a0656b63ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dayOfMonth", value)

    @builtins.property
    @jsii.member(jsii_name="dayOfWeek")
    def day_of_week(self) -> typing.Optional[builtins.str]:
        '''The day of the week on which the scheduled audit is run (if the ``frequency`` is "WEEKLY" or "BIWEEKLY").

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-dayofweek
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dayOfWeek"))

    @day_of_week.setter
    def day_of_week(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5f0c93d37c8a0e6950ab61bf453182274c6e76bd7bcce5dfb8db949ea93d649)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dayOfWeek", value)

    @builtins.property
    @jsii.member(jsii_name="scheduledAuditName")
    def scheduled_audit_name(self) -> typing.Optional[builtins.str]:
        '''The name of the scheduled audit.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-scheduledauditname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheduledAuditName"))

    @scheduled_audit_name.setter
    def scheduled_audit_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbe3ef86bba09618390e255e2ad32b6b17abec05d9118942cd8fcddd779728bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheduledAuditName", value)


@jsii.data_type(
    jsii_type="monocdk.aws_iot.CfnScheduledAuditProps",
    jsii_struct_bases=[],
    name_mapping={
        "frequency": "frequency",
        "target_check_names": "targetCheckNames",
        "day_of_month": "dayOfMonth",
        "day_of_week": "dayOfWeek",
        "scheduled_audit_name": "scheduledAuditName",
        "tags": "tags",
    },
)
class CfnScheduledAuditProps:
    def __init__(
        self,
        *,
        frequency: builtins.str,
        target_check_names: typing.Sequence[builtins.str],
        day_of_month: typing.Optional[builtins.str] = None,
        day_of_week: typing.Optional[builtins.str] = None,
        scheduled_audit_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnScheduledAudit``.

        :param frequency: How often the scheduled audit occurs.
        :param target_check_names: Which checks are performed during the scheduled audit. Checks must be enabled for your account. (Use ``DescribeAccountAuditConfiguration`` to see the list of all checks, including those that are enabled or use ``UpdateAccountAuditConfiguration`` to select which checks are enabled.) The following checks are currently aviable: - ``AUTHENTICATED_COGNITO_ROLE_OVERLY_PERMISSIVE_CHECK`` - ``CA_CERTIFICATE_EXPIRING_CHECK`` - ``CA_CERTIFICATE_KEY_QUALITY_CHECK`` - ``CONFLICTING_CLIENT_IDS_CHECK`` - ``DEVICE_CERTIFICATE_EXPIRING_CHECK`` - ``DEVICE_CERTIFICATE_KEY_QUALITY_CHECK`` - ``DEVICE_CERTIFICATE_SHARED_CHECK`` - ``IOT_POLICY_OVERLY_PERMISSIVE_CHECK`` - ``IOT_ROLE_ALIAS_ALLOWS_ACCESS_TO_UNUSED_SERVICES_CHECK`` - ``IOT_ROLE_ALIAS_OVERLY_PERMISSIVE_CHECK`` - ``LOGGING_DISABLED_CHECK`` - ``REVOKED_CA_CERTIFICATE_STILL_ACTIVE_CHECK`` - ``REVOKED_DEVICE_CERTIFICATE_STILL_ACTIVE_CHECK`` - ``UNAUTHENTICATED_COGNITO_ROLE_OVERLY_PERMISSIVE_CHECK``
        :param day_of_month: The day of the month on which the scheduled audit is run (if the ``frequency`` is "MONTHLY"). If days 29-31 are specified, and the month does not have that many days, the audit takes place on the "LAST" day of the month.
        :param day_of_week: The day of the week on which the scheduled audit is run (if the ``frequency`` is "WEEKLY" or "BIWEEKLY").
        :param scheduled_audit_name: The name of the scheduled audit.
        :param tags: Metadata that can be used to manage the scheduled audit.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_iot as iot
            
            cfn_scheduled_audit_props = iot.CfnScheduledAuditProps(
                frequency="frequency",
                target_check_names=["targetCheckNames"],
            
                # the properties below are optional
                day_of_month="dayOfMonth",
                day_of_week="dayOfWeek",
                scheduled_audit_name="scheduledAuditName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__871f7d0b44f119299f626d51b5c9e680a070cad7039547802efc9f89e736ab23)
            check_type(argname="argument frequency", value=frequency, expected_type=type_hints["frequency"])
            check_type(argname="argument target_check_names", value=target_check_names, expected_type=type_hints["target_check_names"])
            check_type(argname="argument day_of_month", value=day_of_month, expected_type=type_hints["day_of_month"])
            check_type(argname="argument day_of_week", value=day_of_week, expected_type=type_hints["day_of_week"])
            check_type(argname="argument scheduled_audit_name", value=scheduled_audit_name, expected_type=type_hints["scheduled_audit_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "frequency": frequency,
            "target_check_names": target_check_names,
        }
        if day_of_month is not None:
            self._values["day_of_month"] = day_of_month
        if day_of_week is not None:
            self._values["day_of_week"] = day_of_week
        if scheduled_audit_name is not None:
            self._values["scheduled_audit_name"] = scheduled_audit_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def frequency(self) -> builtins.str:
        '''How often the scheduled audit occurs.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-frequency
        '''
        result = self._values.get("frequency")
        assert result is not None, "Required property 'frequency' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_check_names(self) -> typing.List[builtins.str]:
        '''Which checks are performed during the scheduled audit.

        Checks must be enabled for your account. (Use ``DescribeAccountAuditConfiguration`` to see the list of all checks, including those that are enabled or use ``UpdateAccountAuditConfiguration`` to select which checks are enabled.)

        The following checks are currently aviable:

        - ``AUTHENTICATED_COGNITO_ROLE_OVERLY_PERMISSIVE_CHECK``
        - ``CA_CERTIFICATE_EXPIRING_CHECK``
        - ``CA_CERTIFICATE_KEY_QUALITY_CHECK``
        - ``CONFLICTING_CLIENT_IDS_CHECK``
        - ``DEVICE_CERTIFICATE_EXPIRING_CHECK``
        - ``DEVICE_CERTIFICATE_KEY_QUALITY_CHECK``
        - ``DEVICE_CERTIFICATE_SHARED_CHECK``
        - ``IOT_POLICY_OVERLY_PERMISSIVE_CHECK``
        - ``IOT_ROLE_ALIAS_ALLOWS_ACCESS_TO_UNUSED_SERVICES_CHECK``
        - ``IOT_ROLE_ALIAS_OVERLY_PERMISSIVE_CHECK``
        - ``LOGGING_DISABLED_CHECK``
        - ``REVOKED_CA_CERTIFICATE_STILL_ACTIVE_CHECK``
        - ``REVOKED_DEVICE_CERTIFICATE_STILL_ACTIVE_CHECK``
        - ``UNAUTHENTICATED_COGNITO_ROLE_OVERLY_PERMISSIVE_CHECK``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-targetchecknames
        '''
        result = self._values.get("target_check_names")
        assert result is not None, "Required property 'target_check_names' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def day_of_month(self) -> typing.Optional[builtins.str]:
        '''The day of the month on which the scheduled audit is run (if the ``frequency`` is "MONTHLY").

        If days 29-31 are specified, and the month does not have that many days, the audit takes place on the "LAST" day of the month.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-dayofmonth
        '''
        result = self._values.get("day_of_month")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def day_of_week(self) -> typing.Optional[builtins.str]:
        '''The day of the week on which the scheduled audit is run (if the ``frequency`` is "WEEKLY" or "BIWEEKLY").

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-dayofweek
        '''
        result = self._values.get("day_of_week")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scheduled_audit_name(self) -> typing.Optional[builtins.str]:
        '''The name of the scheduled audit.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-scheduledauditname
        '''
        result = self._values.get("scheduled_audit_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''Metadata that can be used to manage the scheduled audit.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-scheduledaudit.html#cfn-iot-scheduledaudit-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnScheduledAuditProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnSecurityProfile(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iot.CfnSecurityProfile",
):
    '''A CloudFormation ``AWS::IoT::SecurityProfile``.

    Use the ``AWS::IoT::SecurityProfile`` resource to create a Device Defender security profile. For API reference, see `CreateSecurityProfile <https://docs.aws.amazon.com/iot/latest/apireference/API_CreateSecurityProfile.html>`_ and for general information, see `Detect <https://docs.aws.amazon.com/iot/latest/developerguide/device-defender-detect.html>`_ .

    :cloudformationResource: AWS::IoT::SecurityProfile
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-securityprofile.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_iot as iot
        
        cfn_security_profile = iot.CfnSecurityProfile(self, "MyCfnSecurityProfile",
            additional_metrics_to_retain_v2=[iot.CfnSecurityProfile.MetricToRetainProperty(
                metric="metric",
        
                # the properties below are optional
                metric_dimension=iot.CfnSecurityProfile.MetricDimensionProperty(
                    dimension_name="dimensionName",
        
                    # the properties below are optional
                    operator="operator"
                )
            )],
            alert_targets={
                "alert_targets_key": iot.CfnSecurityProfile.AlertTargetProperty(
                    alert_target_arn="alertTargetArn",
                    role_arn="roleArn"
                )
            },
            behaviors=[iot.CfnSecurityProfile.BehaviorProperty(
                name="name",
        
                # the properties below are optional
                criteria=iot.CfnSecurityProfile.BehaviorCriteriaProperty(
                    comparison_operator="comparisonOperator",
                    consecutive_datapoints_to_alarm=123,
                    consecutive_datapoints_to_clear=123,
                    duration_seconds=123,
                    ml_detection_config=iot.CfnSecurityProfile.MachineLearningDetectionConfigProperty(
                        confidence_level="confidenceLevel"
                    ),
                    statistical_threshold=iot.CfnSecurityProfile.StatisticalThresholdProperty(
                        statistic="statistic"
                    ),
                    value=iot.CfnSecurityProfile.MetricValueProperty(
                        cidrs=["cidrs"],
                        count="count",
                        number=123,
                        numbers=[123],
                        ports=[123],
                        strings=["strings"]
                    )
                ),
                metric="metric",
                metric_dimension=iot.CfnSecurityProfile.MetricDimensionProperty(
                    dimension_name="dimensionName",
        
                    # the properties below are optional
                    operator="operator"
                ),
                suppress_alerts=False
            )],
            security_profile_description="securityProfileDescription",
            security_profile_name="securityProfileName",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            target_arns=["targetArns"]
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        additional_metrics_to_retain_v2: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union["CfnSecurityProfile.MetricToRetainProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]]] = None,
        alert_targets: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, typing.Union[typing.Union["CfnSecurityProfile.AlertTargetProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]]] = None,
        behaviors: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union["CfnSecurityProfile.BehaviorProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]]] = None,
        security_profile_description: typing.Optional[builtins.str] = None,
        security_profile_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
        target_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::IoT::SecurityProfile``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param additional_metrics_to_retain_v2: A list of metrics whose data is retained (stored). By default, data is retained for any metric used in the profile's ``behaviors`` , but it's also retained for any metric specified here. Can be used with custom metrics; can't be used with dimensions.
        :param alert_targets: Specifies the destinations to which alerts are sent. (Alerts are always sent to the console.) Alerts are generated when a device (thing) violates a behavior.
        :param behaviors: Specifies the behaviors that, when violated by a device (thing), cause an alert.
        :param security_profile_description: A description of the security profile.
        :param security_profile_name: The name you gave to the security profile.
        :param tags: Metadata that can be used to manage the security profile.
        :param target_arns: The ARN of the target (thing group) to which the security profile is attached.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e74d94d5b8d8032c89022311703d61e4fa4ddb326df97b3048d408073a8ded9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSecurityProfileProps(
            additional_metrics_to_retain_v2=additional_metrics_to_retain_v2,
            alert_targets=alert_targets,
            behaviors=behaviors,
            security_profile_description=security_profile_description,
            security_profile_name=security_profile_name,
            tags=tags,
            target_arns=target_arns,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68800bc12c54c432a21a17317b5350c63d970f0d4cdd71ed4c4f5018c130e89b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__96fbd27fd5e5b57dc866a7fb36df955f804896507348f5c8e717975aa1f6edcf)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrSecurityProfileArn")
    def attr_security_profile_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the security profile.

        :cloudformationAttribute: SecurityProfileArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSecurityProfileArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''Metadata that can be used to manage the security profile.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-securityprofile.html#cfn-iot-securityprofile-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="additionalMetricsToRetainV2")
    def additional_metrics_to_retain_v2(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnSecurityProfile.MetricToRetainProperty", _IResolvable_a771d0ef]]]]:
        '''A list of metrics whose data is retained (stored).

        By default, data is retained for any metric used in the profile's ``behaviors`` , but it's also retained for any metric specified here. Can be used with custom metrics; can't be used with dimensions.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-securityprofile.html#cfn-iot-securityprofile-additionalmetricstoretainv2
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnSecurityProfile.MetricToRetainProperty", _IResolvable_a771d0ef]]]], jsii.get(self, "additionalMetricsToRetainV2"))

    @additional_metrics_to_retain_v2.setter
    def additional_metrics_to_retain_v2(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnSecurityProfile.MetricToRetainProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81838e4cb995a14812d9167bfb161434ba5876279b4a108916c8d127f8aee908)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "additionalMetricsToRetainV2", value)

    @builtins.property
    @jsii.member(jsii_name="alertTargets")
    def alert_targets(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, typing.Union["CfnSecurityProfile.AlertTargetProperty", _IResolvable_a771d0ef]]]]:
        '''Specifies the destinations to which alerts are sent.

        (Alerts are always sent to the console.) Alerts are generated when a device (thing) violates a behavior.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-securityprofile.html#cfn-iot-securityprofile-alerttargets
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, typing.Union["CfnSecurityProfile.AlertTargetProperty", _IResolvable_a771d0ef]]]], jsii.get(self, "alertTargets"))

    @alert_targets.setter
    def alert_targets(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, typing.Union["CfnSecurityProfile.AlertTargetProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__534bb7b866e4fd89a7382da53a35f653c192a9994c0f8e7ae04f954f85fd9543)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alertTargets", value)

    @builtins.property
    @jsii.member(jsii_name="behaviors")
    def behaviors(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnSecurityProfile.BehaviorProperty", _IResolvable_a771d0ef]]]]:
        '''Specifies the behaviors that, when violated by a device (thing), cause an alert.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-securityprofile.html#cfn-iot-securityprofile-behaviors
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnSecurityProfile.BehaviorProperty", _IResolvable_a771d0ef]]]], jsii.get(self, "behaviors"))

    @behaviors.setter
    def behaviors(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnSecurityProfile.BehaviorProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07d2c3a6e0689893cd6d983125145987f7e1e3f31720fea49be136125fa67121)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "behaviors", value)

    @builtins.property
    @jsii.member(jsii_name="securityProfileDescription")
    def security_profile_description(self) -> typing.Optional[builtins.str]:
        '''A description of the security profile.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-securityprofile.html#cfn-iot-securityprofile-securityprofiledescription
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityProfileDescription"))

    @security_profile_description.setter
    def security_profile_description(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab52e337fcc5a516da985319885e9ffacde52974163a3081cb356e300bc20fb1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityProfileDescription", value)

    @builtins.property
    @jsii.member(jsii_name="securityProfileName")
    def security_profile_name(self) -> typing.Optional[builtins.str]:
        '''The name you gave to the security profile.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-securityprofile.html#cfn-iot-securityprofile-securityprofilename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityProfileName"))

    @security_profile_name.setter
    def security_profile_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffd0ab9152cb325752c9ee62d952c4c3da821a9e0f51644df36805109cf944a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityProfileName", value)

    @builtins.property
    @jsii.member(jsii_name="targetArns")
    def target_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The ARN of the target (thing group) to which the security profile is attached.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-securityprofile.html#cfn-iot-securityprofile-targetarns
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "targetArns"))

    @target_arns.setter
    def target_arns(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb167de690e8a57eedb0466e83db021e601ddbfb3051f43baf99cb381b9450a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetArns", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnSecurityProfile.AlertTargetProperty",
        jsii_struct_bases=[],
        name_mapping={"alert_target_arn": "alertTargetArn", "role_arn": "roleArn"},
    )
    class AlertTargetProperty:
        def __init__(
            self,
            *,
            alert_target_arn: builtins.str,
            role_arn: builtins.str,
        ) -> None:
            '''A structure containing the alert target ARN and the role ARN.

            :param alert_target_arn: The Amazon Resource Name (ARN) of the notification target to which alerts are sent.
            :param role_arn: The ARN of the role that grants permission to send alerts to the notification target.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-alerttarget.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                alert_target_property = iot.CfnSecurityProfile.AlertTargetProperty(
                    alert_target_arn="alertTargetArn",
                    role_arn="roleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b8a5ad4dacd618ca3c7c6be010c4e22bccdd0161a33e4f7c1370d93fc651da64)
                check_type(argname="argument alert_target_arn", value=alert_target_arn, expected_type=type_hints["alert_target_arn"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "alert_target_arn": alert_target_arn,
                "role_arn": role_arn,
            }

        @builtins.property
        def alert_target_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the notification target to which alerts are sent.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-alerttarget.html#cfn-iot-securityprofile-alerttarget-alerttargetarn
            '''
            result = self._values.get("alert_target_arn")
            assert result is not None, "Required property 'alert_target_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the role that grants permission to send alerts to the notification target.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-alerttarget.html#cfn-iot-securityprofile-alerttarget-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AlertTargetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnSecurityProfile.BehaviorCriteriaProperty",
        jsii_struct_bases=[],
        name_mapping={
            "comparison_operator": "comparisonOperator",
            "consecutive_datapoints_to_alarm": "consecutiveDatapointsToAlarm",
            "consecutive_datapoints_to_clear": "consecutiveDatapointsToClear",
            "duration_seconds": "durationSeconds",
            "ml_detection_config": "mlDetectionConfig",
            "statistical_threshold": "statisticalThreshold",
            "value": "value",
        },
    )
    class BehaviorCriteriaProperty:
        def __init__(
            self,
            *,
            comparison_operator: typing.Optional[builtins.str] = None,
            consecutive_datapoints_to_alarm: typing.Optional[jsii.Number] = None,
            consecutive_datapoints_to_clear: typing.Optional[jsii.Number] = None,
            duration_seconds: typing.Optional[jsii.Number] = None,
            ml_detection_config: typing.Optional[typing.Union[typing.Union["CfnSecurityProfile.MachineLearningDetectionConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            statistical_threshold: typing.Optional[typing.Union[typing.Union["CfnSecurityProfile.StatisticalThresholdProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            value: typing.Optional[typing.Union[typing.Union["CfnSecurityProfile.MetricValueProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''The criteria by which the behavior is determined to be normal.

            :param comparison_operator: The operator that relates the thing measured ( ``metric`` ) to the criteria (containing a ``value`` or ``statisticalThreshold`` ). Valid operators include: - ``string-list`` : ``in-set`` and ``not-in-set`` - ``number-list`` : ``in-set`` and ``not-in-set`` - ``ip-address-list`` : ``in-cidr-set`` and ``not-in-cidr-set`` - ``number`` : ``less-than`` , ``less-than-equals`` , ``greater-than`` , and ``greater-than-equals``
            :param consecutive_datapoints_to_alarm: If a device is in violation of the behavior for the specified number of consecutive datapoints, an alarm occurs. If not specified, the default is 1.
            :param consecutive_datapoints_to_clear: If an alarm has occurred and the offending device is no longer in violation of the behavior for the specified number of consecutive datapoints, the alarm is cleared. If not specified, the default is 1.
            :param duration_seconds: Use this to specify the time duration over which the behavior is evaluated, for those criteria that have a time dimension (for example, ``NUM_MESSAGES_SENT`` ). For a ``statisticalThreshhold`` metric comparison, measurements from all devices are accumulated over this time duration before being used to calculate percentiles, and later, measurements from an individual device are also accumulated over this time duration before being given a percentile rank. Cannot be used with list-based metric datatypes.
            :param ml_detection_config: The confidence level of the detection model.
            :param statistical_threshold: A statistical ranking (percentile)that indicates a threshold value by which a behavior is determined to be in compliance or in violation of the behavior.
            :param value: The value to be compared with the ``metric`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behaviorcriteria.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                behavior_criteria_property = iot.CfnSecurityProfile.BehaviorCriteriaProperty(
                    comparison_operator="comparisonOperator",
                    consecutive_datapoints_to_alarm=123,
                    consecutive_datapoints_to_clear=123,
                    duration_seconds=123,
                    ml_detection_config=iot.CfnSecurityProfile.MachineLearningDetectionConfigProperty(
                        confidence_level="confidenceLevel"
                    ),
                    statistical_threshold=iot.CfnSecurityProfile.StatisticalThresholdProperty(
                        statistic="statistic"
                    ),
                    value=iot.CfnSecurityProfile.MetricValueProperty(
                        cidrs=["cidrs"],
                        count="count",
                        number=123,
                        numbers=[123],
                        ports=[123],
                        strings=["strings"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__75533297fe0f2abbe581a0a9c7bf702421ffa0a6b15f0d540d300ee34f834a72)
                check_type(argname="argument comparison_operator", value=comparison_operator, expected_type=type_hints["comparison_operator"])
                check_type(argname="argument consecutive_datapoints_to_alarm", value=consecutive_datapoints_to_alarm, expected_type=type_hints["consecutive_datapoints_to_alarm"])
                check_type(argname="argument consecutive_datapoints_to_clear", value=consecutive_datapoints_to_clear, expected_type=type_hints["consecutive_datapoints_to_clear"])
                check_type(argname="argument duration_seconds", value=duration_seconds, expected_type=type_hints["duration_seconds"])
                check_type(argname="argument ml_detection_config", value=ml_detection_config, expected_type=type_hints["ml_detection_config"])
                check_type(argname="argument statistical_threshold", value=statistical_threshold, expected_type=type_hints["statistical_threshold"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if comparison_operator is not None:
                self._values["comparison_operator"] = comparison_operator
            if consecutive_datapoints_to_alarm is not None:
                self._values["consecutive_datapoints_to_alarm"] = consecutive_datapoints_to_alarm
            if consecutive_datapoints_to_clear is not None:
                self._values["consecutive_datapoints_to_clear"] = consecutive_datapoints_to_clear
            if duration_seconds is not None:
                self._values["duration_seconds"] = duration_seconds
            if ml_detection_config is not None:
                self._values["ml_detection_config"] = ml_detection_config
            if statistical_threshold is not None:
                self._values["statistical_threshold"] = statistical_threshold
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def comparison_operator(self) -> typing.Optional[builtins.str]:
            '''The operator that relates the thing measured ( ``metric`` ) to the criteria (containing a ``value`` or ``statisticalThreshold`` ).

            Valid operators include:

            - ``string-list`` : ``in-set`` and ``not-in-set``
            - ``number-list`` : ``in-set`` and ``not-in-set``
            - ``ip-address-list`` : ``in-cidr-set`` and ``not-in-cidr-set``
            - ``number`` : ``less-than`` , ``less-than-equals`` , ``greater-than`` , and ``greater-than-equals``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behaviorcriteria.html#cfn-iot-securityprofile-behaviorcriteria-comparisonoperator
            '''
            result = self._values.get("comparison_operator")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def consecutive_datapoints_to_alarm(self) -> typing.Optional[jsii.Number]:
            '''If a device is in violation of the behavior for the specified number of consecutive datapoints, an alarm occurs.

            If not specified, the default is 1.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behaviorcriteria.html#cfn-iot-securityprofile-behaviorcriteria-consecutivedatapointstoalarm
            '''
            result = self._values.get("consecutive_datapoints_to_alarm")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def consecutive_datapoints_to_clear(self) -> typing.Optional[jsii.Number]:
            '''If an alarm has occurred and the offending device is no longer in violation of the behavior for the specified number of consecutive datapoints, the alarm is cleared.

            If not specified, the default is 1.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behaviorcriteria.html#cfn-iot-securityprofile-behaviorcriteria-consecutivedatapointstoclear
            '''
            result = self._values.get("consecutive_datapoints_to_clear")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def duration_seconds(self) -> typing.Optional[jsii.Number]:
            '''Use this to specify the time duration over which the behavior is evaluated, for those criteria that have a time dimension (for example, ``NUM_MESSAGES_SENT`` ).

            For a ``statisticalThreshhold`` metric comparison, measurements from all devices are accumulated over this time duration before being used to calculate percentiles, and later, measurements from an individual device are also accumulated over this time duration before being given a percentile rank. Cannot be used with list-based metric datatypes.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behaviorcriteria.html#cfn-iot-securityprofile-behaviorcriteria-durationseconds
            '''
            result = self._values.get("duration_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def ml_detection_config(
            self,
        ) -> typing.Optional[typing.Union["CfnSecurityProfile.MachineLearningDetectionConfigProperty", _IResolvable_a771d0ef]]:
            '''The confidence level of the detection model.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behaviorcriteria.html#cfn-iot-securityprofile-behaviorcriteria-mldetectionconfig
            '''
            result = self._values.get("ml_detection_config")
            return typing.cast(typing.Optional[typing.Union["CfnSecurityProfile.MachineLearningDetectionConfigProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def statistical_threshold(
            self,
        ) -> typing.Optional[typing.Union["CfnSecurityProfile.StatisticalThresholdProperty", _IResolvable_a771d0ef]]:
            '''A statistical ranking (percentile)that indicates a threshold value by which a behavior is determined to be in compliance or in violation of the behavior.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behaviorcriteria.html#cfn-iot-securityprofile-behaviorcriteria-statisticalthreshold
            '''
            result = self._values.get("statistical_threshold")
            return typing.cast(typing.Optional[typing.Union["CfnSecurityProfile.StatisticalThresholdProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def value(
            self,
        ) -> typing.Optional[typing.Union["CfnSecurityProfile.MetricValueProperty", _IResolvable_a771d0ef]]:
            '''The value to be compared with the ``metric`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behaviorcriteria.html#cfn-iot-securityprofile-behaviorcriteria-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[typing.Union["CfnSecurityProfile.MetricValueProperty", _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BehaviorCriteriaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnSecurityProfile.BehaviorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "criteria": "criteria",
            "metric": "metric",
            "metric_dimension": "metricDimension",
            "suppress_alerts": "suppressAlerts",
        },
    )
    class BehaviorProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            criteria: typing.Optional[typing.Union[typing.Union["CfnSecurityProfile.BehaviorCriteriaProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            metric: typing.Optional[builtins.str] = None,
            metric_dimension: typing.Optional[typing.Union[typing.Union["CfnSecurityProfile.MetricDimensionProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            suppress_alerts: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''A Device Defender security profile behavior.

            :param name: The name you've given to the behavior.
            :param criteria: The criteria that determine if a device is behaving normally in regard to the ``metric`` .
            :param metric: What is measured by the behavior.
            :param metric_dimension: The dimension of the metric.
            :param suppress_alerts: The alert status. If you set the value to ``true`` , alerts will be suppressed.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behavior.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                behavior_property = iot.CfnSecurityProfile.BehaviorProperty(
                    name="name",
                
                    # the properties below are optional
                    criteria=iot.CfnSecurityProfile.BehaviorCriteriaProperty(
                        comparison_operator="comparisonOperator",
                        consecutive_datapoints_to_alarm=123,
                        consecutive_datapoints_to_clear=123,
                        duration_seconds=123,
                        ml_detection_config=iot.CfnSecurityProfile.MachineLearningDetectionConfigProperty(
                            confidence_level="confidenceLevel"
                        ),
                        statistical_threshold=iot.CfnSecurityProfile.StatisticalThresholdProperty(
                            statistic="statistic"
                        ),
                        value=iot.CfnSecurityProfile.MetricValueProperty(
                            cidrs=["cidrs"],
                            count="count",
                            number=123,
                            numbers=[123],
                            ports=[123],
                            strings=["strings"]
                        )
                    ),
                    metric="metric",
                    metric_dimension=iot.CfnSecurityProfile.MetricDimensionProperty(
                        dimension_name="dimensionName",
                
                        # the properties below are optional
                        operator="operator"
                    ),
                    suppress_alerts=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0c04941109d9114d090b7476b1e877559ef7fcd96a91277acc6cfa307b160890)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument criteria", value=criteria, expected_type=type_hints["criteria"])
                check_type(argname="argument metric", value=metric, expected_type=type_hints["metric"])
                check_type(argname="argument metric_dimension", value=metric_dimension, expected_type=type_hints["metric_dimension"])
                check_type(argname="argument suppress_alerts", value=suppress_alerts, expected_type=type_hints["suppress_alerts"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }
            if criteria is not None:
                self._values["criteria"] = criteria
            if metric is not None:
                self._values["metric"] = metric
            if metric_dimension is not None:
                self._values["metric_dimension"] = metric_dimension
            if suppress_alerts is not None:
                self._values["suppress_alerts"] = suppress_alerts

        @builtins.property
        def name(self) -> builtins.str:
            '''The name you've given to the behavior.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behavior.html#cfn-iot-securityprofile-behavior-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def criteria(
            self,
        ) -> typing.Optional[typing.Union["CfnSecurityProfile.BehaviorCriteriaProperty", _IResolvable_a771d0ef]]:
            '''The criteria that determine if a device is behaving normally in regard to the ``metric`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behavior.html#cfn-iot-securityprofile-behavior-criteria
            '''
            result = self._values.get("criteria")
            return typing.cast(typing.Optional[typing.Union["CfnSecurityProfile.BehaviorCriteriaProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def metric(self) -> typing.Optional[builtins.str]:
            '''What is measured by the behavior.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behavior.html#cfn-iot-securityprofile-behavior-metric
            '''
            result = self._values.get("metric")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def metric_dimension(
            self,
        ) -> typing.Optional[typing.Union["CfnSecurityProfile.MetricDimensionProperty", _IResolvable_a771d0ef]]:
            '''The dimension of the metric.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behavior.html#cfn-iot-securityprofile-behavior-metricdimension
            '''
            result = self._values.get("metric_dimension")
            return typing.cast(typing.Optional[typing.Union["CfnSecurityProfile.MetricDimensionProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def suppress_alerts(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''The alert status.

            If you set the value to ``true`` , alerts will be suppressed.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-behavior.html#cfn-iot-securityprofile-behavior-suppressalerts
            '''
            result = self._values.get("suppress_alerts")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BehaviorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnSecurityProfile.MachineLearningDetectionConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"confidence_level": "confidenceLevel"},
    )
    class MachineLearningDetectionConfigProperty:
        def __init__(
            self,
            *,
            confidence_level: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``MachineLearningDetectionConfig`` property type controls confidence of the machine learning model.

            :param confidence_level: The model confidence level. There are three levels of confidence, ``"high"`` , ``"medium"`` , and ``"low"`` . The higher the confidence level, the lower the sensitivity, and the lower the alarm frequency will be.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-machinelearningdetectionconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                machine_learning_detection_config_property = iot.CfnSecurityProfile.MachineLearningDetectionConfigProperty(
                    confidence_level="confidenceLevel"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a08b4e74a1b3543e60362e0381a167265581dde022cd0be74eec623c6bfa29d3)
                check_type(argname="argument confidence_level", value=confidence_level, expected_type=type_hints["confidence_level"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if confidence_level is not None:
                self._values["confidence_level"] = confidence_level

        @builtins.property
        def confidence_level(self) -> typing.Optional[builtins.str]:
            '''The model confidence level.

            There are three levels of confidence, ``"high"`` , ``"medium"`` , and ``"low"`` .

            The higher the confidence level, the lower the sensitivity, and the lower the alarm frequency will be.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-machinelearningdetectionconfig.html#cfn-iot-securityprofile-machinelearningdetectionconfig-confidencelevel
            '''
            result = self._values.get("confidence_level")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MachineLearningDetectionConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnSecurityProfile.MetricDimensionProperty",
        jsii_struct_bases=[],
        name_mapping={"dimension_name": "dimensionName", "operator": "operator"},
    )
    class MetricDimensionProperty:
        def __init__(
            self,
            *,
            dimension_name: builtins.str,
            operator: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The dimension of the metric.

            :param dimension_name: The name of the dimension.
            :param operator: Operators are constructs that perform logical operations. Valid values are ``IN`` and ``NOT_IN`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-metricdimension.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                metric_dimension_property = iot.CfnSecurityProfile.MetricDimensionProperty(
                    dimension_name="dimensionName",
                
                    # the properties below are optional
                    operator="operator"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__85cc6baaa7d59e823c42454d05036fba22d7dca549414b1a3c4659dc7bdbdeb4)
                check_type(argname="argument dimension_name", value=dimension_name, expected_type=type_hints["dimension_name"])
                check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "dimension_name": dimension_name,
            }
            if operator is not None:
                self._values["operator"] = operator

        @builtins.property
        def dimension_name(self) -> builtins.str:
            '''The name of the dimension.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-metricdimension.html#cfn-iot-securityprofile-metricdimension-dimensionname
            '''
            result = self._values.get("dimension_name")
            assert result is not None, "Required property 'dimension_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def operator(self) -> typing.Optional[builtins.str]:
            '''Operators are constructs that perform logical operations.

            Valid values are ``IN`` and ``NOT_IN`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-metricdimension.html#cfn-iot-securityprofile-metricdimension-operator
            '''
            result = self._values.get("operator")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricDimensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnSecurityProfile.MetricToRetainProperty",
        jsii_struct_bases=[],
        name_mapping={"metric": "metric", "metric_dimension": "metricDimension"},
    )
    class MetricToRetainProperty:
        def __init__(
            self,
            *,
            metric: builtins.str,
            metric_dimension: typing.Optional[typing.Union[typing.Union["CfnSecurityProfile.MetricDimensionProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''The metric you want to retain.

            Dimensions are optional.

            :param metric: A standard of measurement.
            :param metric_dimension: The dimension of the metric.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-metrictoretain.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                metric_to_retain_property = iot.CfnSecurityProfile.MetricToRetainProperty(
                    metric="metric",
                
                    # the properties below are optional
                    metric_dimension=iot.CfnSecurityProfile.MetricDimensionProperty(
                        dimension_name="dimensionName",
                
                        # the properties below are optional
                        operator="operator"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dd32bd896a41dc36f4bfb9459ad6759cd299f4d197d45b71a5226e9bd8498807)
                check_type(argname="argument metric", value=metric, expected_type=type_hints["metric"])
                check_type(argname="argument metric_dimension", value=metric_dimension, expected_type=type_hints["metric_dimension"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "metric": metric,
            }
            if metric_dimension is not None:
                self._values["metric_dimension"] = metric_dimension

        @builtins.property
        def metric(self) -> builtins.str:
            '''A standard of measurement.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-metrictoretain.html#cfn-iot-securityprofile-metrictoretain-metric
            '''
            result = self._values.get("metric")
            assert result is not None, "Required property 'metric' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def metric_dimension(
            self,
        ) -> typing.Optional[typing.Union["CfnSecurityProfile.MetricDimensionProperty", _IResolvable_a771d0ef]]:
            '''The dimension of the metric.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-metrictoretain.html#cfn-iot-securityprofile-metrictoretain-metricdimension
            '''
            result = self._values.get("metric_dimension")
            return typing.cast(typing.Optional[typing.Union["CfnSecurityProfile.MetricDimensionProperty", _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricToRetainProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnSecurityProfile.MetricValueProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cidrs": "cidrs",
            "count": "count",
            "number": "number",
            "numbers": "numbers",
            "ports": "ports",
            "strings": "strings",
        },
    )
    class MetricValueProperty:
        def __init__(
            self,
            *,
            cidrs: typing.Optional[typing.Sequence[builtins.str]] = None,
            count: typing.Optional[builtins.str] = None,
            number: typing.Optional[jsii.Number] = None,
            numbers: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[jsii.Number]]] = None,
            ports: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[jsii.Number]]] = None,
            strings: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The value to be compared with the ``metric`` .

            :param cidrs: If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set to be compared with the ``metric`` .
            :param count: If the ``comparisonOperator`` calls for a numeric value, use this to specify that numeric value to be compared with the ``metric`` .
            :param number: The numeric values of a metric.
            :param numbers: The numeric value of a metric.
            :param ports: If the ``comparisonOperator`` calls for a set of ports, use this to specify that set to be compared with the ``metric`` .
            :param strings: The string values of a metric.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-metricvalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                metric_value_property = iot.CfnSecurityProfile.MetricValueProperty(
                    cidrs=["cidrs"],
                    count="count",
                    number=123,
                    numbers=[123],
                    ports=[123],
                    strings=["strings"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__275696e34aa4e1fcb3a125dc4396d389ae4d4bcf0b4ac0426b2bff6471d2a50c)
                check_type(argname="argument cidrs", value=cidrs, expected_type=type_hints["cidrs"])
                check_type(argname="argument count", value=count, expected_type=type_hints["count"])
                check_type(argname="argument number", value=number, expected_type=type_hints["number"])
                check_type(argname="argument numbers", value=numbers, expected_type=type_hints["numbers"])
                check_type(argname="argument ports", value=ports, expected_type=type_hints["ports"])
                check_type(argname="argument strings", value=strings, expected_type=type_hints["strings"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cidrs is not None:
                self._values["cidrs"] = cidrs
            if count is not None:
                self._values["count"] = count
            if number is not None:
                self._values["number"] = number
            if numbers is not None:
                self._values["numbers"] = numbers
            if ports is not None:
                self._values["ports"] = ports
            if strings is not None:
                self._values["strings"] = strings

        @builtins.property
        def cidrs(self) -> typing.Optional[typing.List[builtins.str]]:
            '''If the ``comparisonOperator`` calls for a set of CIDRs, use this to specify that set to be compared with the ``metric`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-metricvalue.html#cfn-iot-securityprofile-metricvalue-cidrs
            '''
            result = self._values.get("cidrs")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def count(self) -> typing.Optional[builtins.str]:
            '''If the ``comparisonOperator`` calls for a numeric value, use this to specify that numeric value to be compared with the ``metric`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-metricvalue.html#cfn-iot-securityprofile-metricvalue-count
            '''
            result = self._values.get("count")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def number(self) -> typing.Optional[jsii.Number]:
            '''The numeric values of a metric.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-metricvalue.html#cfn-iot-securityprofile-metricvalue-number
            '''
            result = self._values.get("number")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def numbers(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[jsii.Number]]]:
            '''The numeric value of a metric.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-metricvalue.html#cfn-iot-securityprofile-metricvalue-numbers
            '''
            result = self._values.get("numbers")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[jsii.Number]]], result)

        @builtins.property
        def ports(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[jsii.Number]]]:
            '''If the ``comparisonOperator`` calls for a set of ports, use this to specify that set to be compared with the ``metric`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-metricvalue.html#cfn-iot-securityprofile-metricvalue-ports
            '''
            result = self._values.get("ports")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[jsii.Number]]], result)

        @builtins.property
        def strings(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The string values of a metric.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-metricvalue.html#cfn-iot-securityprofile-metricvalue-strings
            '''
            result = self._values.get("strings")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnSecurityProfile.StatisticalThresholdProperty",
        jsii_struct_bases=[],
        name_mapping={"statistic": "statistic"},
    )
    class StatisticalThresholdProperty:
        def __init__(self, *, statistic: typing.Optional[builtins.str] = None) -> None:
            '''A statistical ranking (percentile) that indicates a threshold value by which a behavior is determined to be in compliance or in violation of the behavior.

            :param statistic: The percentile that resolves to a threshold value by which compliance with a behavior is determined. Metrics are collected over the specified period ( ``durationSeconds`` ) from all reporting devices in your account and statistical ranks are calculated. Then, the measurements from a device are collected over the same period. If the accumulated measurements from the device fall above or below ( ``comparisonOperator`` ) the value associated with the percentile specified, then the device is considered to be in compliance with the behavior, otherwise a violation occurs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-statisticalthreshold.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                statistical_threshold_property = iot.CfnSecurityProfile.StatisticalThresholdProperty(
                    statistic="statistic"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__54afe0874ad88601aaffef752e346f18136aad948496d9e0d6f23b50971e25c1)
                check_type(argname="argument statistic", value=statistic, expected_type=type_hints["statistic"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if statistic is not None:
                self._values["statistic"] = statistic

        @builtins.property
        def statistic(self) -> typing.Optional[builtins.str]:
            '''The percentile that resolves to a threshold value by which compliance with a behavior is determined.

            Metrics are collected over the specified period ( ``durationSeconds`` ) from all reporting devices in your account and statistical ranks are calculated. Then, the measurements from a device are collected over the same period. If the accumulated measurements from the device fall above or below ( ``comparisonOperator`` ) the value associated with the percentile specified, then the device is considered to be in compliance with the behavior, otherwise a violation occurs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-securityprofile-statisticalthreshold.html#cfn-iot-securityprofile-statisticalthreshold-statistic
            '''
            result = self._values.get("statistic")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StatisticalThresholdProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_iot.CfnSecurityProfileProps",
    jsii_struct_bases=[],
    name_mapping={
        "additional_metrics_to_retain_v2": "additionalMetricsToRetainV2",
        "alert_targets": "alertTargets",
        "behaviors": "behaviors",
        "security_profile_description": "securityProfileDescription",
        "security_profile_name": "securityProfileName",
        "tags": "tags",
        "target_arns": "targetArns",
    },
)
class CfnSecurityProfileProps:
    def __init__(
        self,
        *,
        additional_metrics_to_retain_v2: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union[CfnSecurityProfile.MetricToRetainProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]]] = None,
        alert_targets: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, typing.Union[typing.Union[CfnSecurityProfile.AlertTargetProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]]] = None,
        behaviors: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union[CfnSecurityProfile.BehaviorProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]]] = None,
        security_profile_description: typing.Optional[builtins.str] = None,
        security_profile_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
        target_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSecurityProfile``.

        :param additional_metrics_to_retain_v2: A list of metrics whose data is retained (stored). By default, data is retained for any metric used in the profile's ``behaviors`` , but it's also retained for any metric specified here. Can be used with custom metrics; can't be used with dimensions.
        :param alert_targets: Specifies the destinations to which alerts are sent. (Alerts are always sent to the console.) Alerts are generated when a device (thing) violates a behavior.
        :param behaviors: Specifies the behaviors that, when violated by a device (thing), cause an alert.
        :param security_profile_description: A description of the security profile.
        :param security_profile_name: The name you gave to the security profile.
        :param tags: Metadata that can be used to manage the security profile.
        :param target_arns: The ARN of the target (thing group) to which the security profile is attached.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-securityprofile.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_iot as iot
            
            cfn_security_profile_props = iot.CfnSecurityProfileProps(
                additional_metrics_to_retain_v2=[iot.CfnSecurityProfile.MetricToRetainProperty(
                    metric="metric",
            
                    # the properties below are optional
                    metric_dimension=iot.CfnSecurityProfile.MetricDimensionProperty(
                        dimension_name="dimensionName",
            
                        # the properties below are optional
                        operator="operator"
                    )
                )],
                alert_targets={
                    "alert_targets_key": iot.CfnSecurityProfile.AlertTargetProperty(
                        alert_target_arn="alertTargetArn",
                        role_arn="roleArn"
                    )
                },
                behaviors=[iot.CfnSecurityProfile.BehaviorProperty(
                    name="name",
            
                    # the properties below are optional
                    criteria=iot.CfnSecurityProfile.BehaviorCriteriaProperty(
                        comparison_operator="comparisonOperator",
                        consecutive_datapoints_to_alarm=123,
                        consecutive_datapoints_to_clear=123,
                        duration_seconds=123,
                        ml_detection_config=iot.CfnSecurityProfile.MachineLearningDetectionConfigProperty(
                            confidence_level="confidenceLevel"
                        ),
                        statistical_threshold=iot.CfnSecurityProfile.StatisticalThresholdProperty(
                            statistic="statistic"
                        ),
                        value=iot.CfnSecurityProfile.MetricValueProperty(
                            cidrs=["cidrs"],
                            count="count",
                            number=123,
                            numbers=[123],
                            ports=[123],
                            strings=["strings"]
                        )
                    ),
                    metric="metric",
                    metric_dimension=iot.CfnSecurityProfile.MetricDimensionProperty(
                        dimension_name="dimensionName",
            
                        # the properties below are optional
                        operator="operator"
                    ),
                    suppress_alerts=False
                )],
                security_profile_description="securityProfileDescription",
                security_profile_name="securityProfileName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                target_arns=["targetArns"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b69de8ce9801a72b1fa4ee2a2d516f9f3ba8c2fb6b9f6148375d8f3cbefe41ba)
            check_type(argname="argument additional_metrics_to_retain_v2", value=additional_metrics_to_retain_v2, expected_type=type_hints["additional_metrics_to_retain_v2"])
            check_type(argname="argument alert_targets", value=alert_targets, expected_type=type_hints["alert_targets"])
            check_type(argname="argument behaviors", value=behaviors, expected_type=type_hints["behaviors"])
            check_type(argname="argument security_profile_description", value=security_profile_description, expected_type=type_hints["security_profile_description"])
            check_type(argname="argument security_profile_name", value=security_profile_name, expected_type=type_hints["security_profile_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument target_arns", value=target_arns, expected_type=type_hints["target_arns"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_metrics_to_retain_v2 is not None:
            self._values["additional_metrics_to_retain_v2"] = additional_metrics_to_retain_v2
        if alert_targets is not None:
            self._values["alert_targets"] = alert_targets
        if behaviors is not None:
            self._values["behaviors"] = behaviors
        if security_profile_description is not None:
            self._values["security_profile_description"] = security_profile_description
        if security_profile_name is not None:
            self._values["security_profile_name"] = security_profile_name
        if tags is not None:
            self._values["tags"] = tags
        if target_arns is not None:
            self._values["target_arns"] = target_arns

    @builtins.property
    def additional_metrics_to_retain_v2(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnSecurityProfile.MetricToRetainProperty, _IResolvable_a771d0ef]]]]:
        '''A list of metrics whose data is retained (stored).

        By default, data is retained for any metric used in the profile's ``behaviors`` , but it's also retained for any metric specified here. Can be used with custom metrics; can't be used with dimensions.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-securityprofile.html#cfn-iot-securityprofile-additionalmetricstoretainv2
        '''
        result = self._values.get("additional_metrics_to_retain_v2")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnSecurityProfile.MetricToRetainProperty, _IResolvable_a771d0ef]]]], result)

    @builtins.property
    def alert_targets(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, typing.Union[CfnSecurityProfile.AlertTargetProperty, _IResolvable_a771d0ef]]]]:
        '''Specifies the destinations to which alerts are sent.

        (Alerts are always sent to the console.) Alerts are generated when a device (thing) violates a behavior.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-securityprofile.html#cfn-iot-securityprofile-alerttargets
        '''
        result = self._values.get("alert_targets")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, typing.Union[CfnSecurityProfile.AlertTargetProperty, _IResolvable_a771d0ef]]]], result)

    @builtins.property
    def behaviors(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnSecurityProfile.BehaviorProperty, _IResolvable_a771d0ef]]]]:
        '''Specifies the behaviors that, when violated by a device (thing), cause an alert.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-securityprofile.html#cfn-iot-securityprofile-behaviors
        '''
        result = self._values.get("behaviors")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnSecurityProfile.BehaviorProperty, _IResolvable_a771d0ef]]]], result)

    @builtins.property
    def security_profile_description(self) -> typing.Optional[builtins.str]:
        '''A description of the security profile.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-securityprofile.html#cfn-iot-securityprofile-securityprofiledescription
        '''
        result = self._values.get("security_profile_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_profile_name(self) -> typing.Optional[builtins.str]:
        '''The name you gave to the security profile.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-securityprofile.html#cfn-iot-securityprofile-securityprofilename
        '''
        result = self._values.get("security_profile_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''Metadata that can be used to manage the security profile.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-securityprofile.html#cfn-iot-securityprofile-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    @builtins.property
    def target_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The ARN of the target (thing group) to which the security profile is attached.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-securityprofile.html#cfn-iot-securityprofile-targetarns
        '''
        result = self._values.get("target_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSecurityProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnThing(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iot.CfnThing",
):
    '''A CloudFormation ``AWS::IoT::Thing``.

    Use the ``AWS::IoT::Thing`` resource to declare an AWS IoT thing.

    For information about working with things, see `How AWS IoT Works <https://docs.aws.amazon.com/iot/latest/developerguide/aws-iot-how-it-works.html>`_ and `Device Registry for AWS IoT <https://docs.aws.amazon.com/iot/latest/developerguide/thing-registry.html>`_ in the *AWS IoT Developer Guide* .

    :cloudformationResource: AWS::IoT::Thing
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thing.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_iot as iot
        
        cfn_thing = iot.CfnThing(self, "MyCfnThing",
            attribute_payload=iot.CfnThing.AttributePayloadProperty(
                attributes={
                    "attributes_key": "attributes"
                }
            ),
            thing_name="thingName"
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        attribute_payload: typing.Optional[typing.Union[typing.Union["CfnThing.AttributePayloadProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        thing_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::IoT::Thing``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param attribute_payload: A string that contains up to three key value pairs. Maximum length of 800. Duplicates not allowed.
        :param thing_name: The name of the thing to update. You can't change a thing's name. To change a thing's name, you must create a new thing, give it the new name, and then delete the old thing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__437d130d2e5bcd734f97792aa608823e3c3860cb3a614bb3f156c8b26038798b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnThingProps(
            attribute_payload=attribute_payload, thing_name=thing_name
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ff5f03e628710104a6eff5df60151e38d1805fa533dce663677187c35fa94a3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__085e897ceae95b566817862ad7f09901ac62e0f2baf87a5b13219eb0e8014d1d)
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
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="attributePayload")
    def attribute_payload(
        self,
    ) -> typing.Optional[typing.Union["CfnThing.AttributePayloadProperty", _IResolvable_a771d0ef]]:
        '''A string that contains up to three key value pairs.

        Maximum length of 800. Duplicates not allowed.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thing.html#cfn-iot-thing-attributepayload
        '''
        return typing.cast(typing.Optional[typing.Union["CfnThing.AttributePayloadProperty", _IResolvable_a771d0ef]], jsii.get(self, "attributePayload"))

    @attribute_payload.setter
    def attribute_payload(
        self,
        value: typing.Optional[typing.Union["CfnThing.AttributePayloadProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71dfac710bca66dbe046744d860b33d688a2d19dae718dfcb09c24ab9b243a25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributePayload", value)

    @builtins.property
    @jsii.member(jsii_name="thingName")
    def thing_name(self) -> typing.Optional[builtins.str]:
        '''The name of the thing to update.

        You can't change a thing's name. To change a thing's name, you must create a new thing, give it the new name, and then delete the old thing.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thing.html#cfn-iot-thing-thingname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thingName"))

    @thing_name.setter
    def thing_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fea192f5ce9c6a101faee69bb6dfb9a8c23e3e4e6bfef26faa8adb0b2adb80e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thingName", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnThing.AttributePayloadProperty",
        jsii_struct_bases=[],
        name_mapping={"attributes": "attributes"},
    )
    class AttributePayloadProperty:
        def __init__(
            self,
            *,
            attributes: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, builtins.str]]] = None,
        ) -> None:
            '''The AttributePayload property specifies up to three attributes for an AWS IoT as key-value pairs.

            AttributePayload is a property of the `AWS::IoT::Thing <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thing.html>`_ resource.

            :param attributes: A JSON string containing up to three key-value pair in JSON format. For example:. ``{\\"attributes\\":{\\"string1\\":\\"string2\\"}}``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-thing-attributepayload.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                attribute_payload_property = iot.CfnThing.AttributePayloadProperty(
                    attributes={
                        "attributes_key": "attributes"
                    }
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__829580ffc78a180f74319e12b734c7fee35c1c9d273dbf57c9cf032199be1a9c)
                check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if attributes is not None:
                self._values["attributes"] = attributes

        @builtins.property
        def attributes(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, builtins.str]]]:
            '''A JSON string containing up to three key-value pair in JSON format. For example:.

            ``{\\"attributes\\":{\\"string1\\":\\"string2\\"}}``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-thing-attributepayload.html#cfn-iot-thing-attributepayload-attributes
            '''
            result = self._values.get("attributes")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, builtins.str]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AttributePayloadProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_82c04a63)
class CfnThingPrincipalAttachment(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iot.CfnThingPrincipalAttachment",
):
    '''A CloudFormation ``AWS::IoT::ThingPrincipalAttachment``.

    Use the ``AWS::IoT::ThingPrincipalAttachment`` resource to attach a principal (an X.509 certificate or another credential) to a thing.

    For more information about working with AWS IoT things and principals, see `Authorization <https://docs.aws.amazon.com/iot/latest/developerguide/authorization.html>`_ in the *AWS IoT Developer Guide* .

    :cloudformationResource: AWS::IoT::ThingPrincipalAttachment
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thingprincipalattachment.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_iot as iot
        
        cfn_thing_principal_attachment = iot.CfnThingPrincipalAttachment(self, "MyCfnThingPrincipalAttachment",
            principal="principal",
            thing_name="thingName"
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        principal: builtins.str,
        thing_name: builtins.str,
    ) -> None:
        '''Create a new ``AWS::IoT::ThingPrincipalAttachment``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param principal: The principal, which can be a certificate ARN (as returned from the ``CreateCertificate`` operation) or an Amazon Cognito ID.
        :param thing_name: The name of the AWS IoT thing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63492ad3993b02e4f624709e8f068e8e97eb78d1c5c7aef3734e9f49504a944c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnThingPrincipalAttachmentProps(
            principal=principal, thing_name=thing_name
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26000d234a9d676f4e6405dccace4f69950254d43c43dfe3d40c56ae8a38502e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__428a71070eb340e9562b190ed1dfdd886046a8ee5362886b72bf977347f637a4)
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
    @jsii.member(jsii_name="principal")
    def principal(self) -> builtins.str:
        '''The principal, which can be a certificate ARN (as returned from the ``CreateCertificate`` operation) or an Amazon Cognito ID.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thingprincipalattachment.html#cfn-iot-thingprincipalattachment-principal
        '''
        return typing.cast(builtins.str, jsii.get(self, "principal"))

    @principal.setter
    def principal(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__034debeed37c02601562645621017cb8017d1638111d4f7b039b320cabdc8efa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "principal", value)

    @builtins.property
    @jsii.member(jsii_name="thingName")
    def thing_name(self) -> builtins.str:
        '''The name of the AWS IoT thing.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thingprincipalattachment.html#cfn-iot-thingprincipalattachment-thingname
        '''
        return typing.cast(builtins.str, jsii.get(self, "thingName"))

    @thing_name.setter
    def thing_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fa53b0935f59bda6115a136d9142930984c3bef366afbaa85e450dc39655e0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thingName", value)


@jsii.data_type(
    jsii_type="monocdk.aws_iot.CfnThingPrincipalAttachmentProps",
    jsii_struct_bases=[],
    name_mapping={"principal": "principal", "thing_name": "thingName"},
)
class CfnThingPrincipalAttachmentProps:
    def __init__(self, *, principal: builtins.str, thing_name: builtins.str) -> None:
        '''Properties for defining a ``CfnThingPrincipalAttachment``.

        :param principal: The principal, which can be a certificate ARN (as returned from the ``CreateCertificate`` operation) or an Amazon Cognito ID.
        :param thing_name: The name of the AWS IoT thing.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thingprincipalattachment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_iot as iot
            
            cfn_thing_principal_attachment_props = iot.CfnThingPrincipalAttachmentProps(
                principal="principal",
                thing_name="thingName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2eca5dd28b04f48619a1406080061cf8aef11a3b72c035a0aa223f28afa773e)
            check_type(argname="argument principal", value=principal, expected_type=type_hints["principal"])
            check_type(argname="argument thing_name", value=thing_name, expected_type=type_hints["thing_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "principal": principal,
            "thing_name": thing_name,
        }

    @builtins.property
    def principal(self) -> builtins.str:
        '''The principal, which can be a certificate ARN (as returned from the ``CreateCertificate`` operation) or an Amazon Cognito ID.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thingprincipalattachment.html#cfn-iot-thingprincipalattachment-principal
        '''
        result = self._values.get("principal")
        assert result is not None, "Required property 'principal' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def thing_name(self) -> builtins.str:
        '''The name of the AWS IoT thing.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thingprincipalattachment.html#cfn-iot-thingprincipalattachment-thingname
        '''
        result = self._values.get("thing_name")
        assert result is not None, "Required property 'thing_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnThingPrincipalAttachmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_iot.CfnThingProps",
    jsii_struct_bases=[],
    name_mapping={"attribute_payload": "attributePayload", "thing_name": "thingName"},
)
class CfnThingProps:
    def __init__(
        self,
        *,
        attribute_payload: typing.Optional[typing.Union[typing.Union[CfnThing.AttributePayloadProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        thing_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnThing``.

        :param attribute_payload: A string that contains up to three key value pairs. Maximum length of 800. Duplicates not allowed.
        :param thing_name: The name of the thing to update. You can't change a thing's name. To change a thing's name, you must create a new thing, give it the new name, and then delete the old thing.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thing.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_iot as iot
            
            cfn_thing_props = iot.CfnThingProps(
                attribute_payload=iot.CfnThing.AttributePayloadProperty(
                    attributes={
                        "attributes_key": "attributes"
                    }
                ),
                thing_name="thingName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92aa4038efc687a706b388857c7d36a80effb18ea1a904224103609c6a458309)
            check_type(argname="argument attribute_payload", value=attribute_payload, expected_type=type_hints["attribute_payload"])
            check_type(argname="argument thing_name", value=thing_name, expected_type=type_hints["thing_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if attribute_payload is not None:
            self._values["attribute_payload"] = attribute_payload
        if thing_name is not None:
            self._values["thing_name"] = thing_name

    @builtins.property
    def attribute_payload(
        self,
    ) -> typing.Optional[typing.Union[CfnThing.AttributePayloadProperty, _IResolvable_a771d0ef]]:
        '''A string that contains up to three key value pairs.

        Maximum length of 800. Duplicates not allowed.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thing.html#cfn-iot-thing-attributepayload
        '''
        result = self._values.get("attribute_payload")
        return typing.cast(typing.Optional[typing.Union[CfnThing.AttributePayloadProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def thing_name(self) -> typing.Optional[builtins.str]:
        '''The name of the thing to update.

        You can't change a thing's name. To change a thing's name, you must create a new thing, give it the new name, and then delete the old thing.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thing.html#cfn-iot-thing-thingname
        '''
        result = self._values.get("thing_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnThingProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnTopicRule(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iot.CfnTopicRule",
):
    '''A CloudFormation ``AWS::IoT::TopicRule``.

    Use the ``AWS::IoT::TopicRule`` resource to declare an AWS IoT rule. For information about working with AWS IoT rules, see `Rules for AWS IoT <https://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html>`_ in the *AWS IoT Developer Guide* .

    :cloudformationResource: AWS::IoT::TopicRule
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicrule.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_iot as iot
        
        cfn_topic_rule = iot.CfnTopicRule(self, "MyCfnTopicRule",
            topic_rule_payload=iot.CfnTopicRule.TopicRulePayloadProperty(
                actions=[iot.CfnTopicRule.ActionProperty(
                    cloudwatch_alarm=iot.CfnTopicRule.CloudwatchAlarmActionProperty(
                        alarm_name="alarmName",
                        role_arn="roleArn",
                        state_reason="stateReason",
                        state_value="stateValue"
                    ),
                    cloudwatch_logs=iot.CfnTopicRule.CloudwatchLogsActionProperty(
                        log_group_name="logGroupName",
                        role_arn="roleArn"
                    ),
                    cloudwatch_metric=iot.CfnTopicRule.CloudwatchMetricActionProperty(
                        metric_name="metricName",
                        metric_namespace="metricNamespace",
                        metric_unit="metricUnit",
                        metric_value="metricValue",
                        role_arn="roleArn",
        
                        # the properties below are optional
                        metric_timestamp="metricTimestamp"
                    ),
                    dynamo_db=iot.CfnTopicRule.DynamoDBActionProperty(
                        hash_key_field="hashKeyField",
                        hash_key_value="hashKeyValue",
                        role_arn="roleArn",
                        table_name="tableName",
        
                        # the properties below are optional
                        hash_key_type="hashKeyType",
                        payload_field="payloadField",
                        range_key_field="rangeKeyField",
                        range_key_type="rangeKeyType",
                        range_key_value="rangeKeyValue"
                    ),
                    dynamo_dBv2=iot.CfnTopicRule.DynamoDBv2ActionProperty(
                        put_item=iot.CfnTopicRule.PutItemInputProperty(
                            table_name="tableName"
                        ),
                        role_arn="roleArn"
                    ),
                    elasticsearch=iot.CfnTopicRule.ElasticsearchActionProperty(
                        endpoint="endpoint",
                        id="id",
                        index="index",
                        role_arn="roleArn",
                        type="type"
                    ),
                    firehose=iot.CfnTopicRule.FirehoseActionProperty(
                        delivery_stream_name="deliveryStreamName",
                        role_arn="roleArn",
        
                        # the properties below are optional
                        batch_mode=False,
                        separator="separator"
                    ),
                    http=iot.CfnTopicRule.HttpActionProperty(
                        url="url",
        
                        # the properties below are optional
                        auth=iot.CfnTopicRule.HttpAuthorizationProperty(
                            sigv4=iot.CfnTopicRule.SigV4AuthorizationProperty(
                                role_arn="roleArn",
                                service_name="serviceName",
                                signing_region="signingRegion"
                            )
                        ),
                        confirmation_url="confirmationUrl",
                        headers=[iot.CfnTopicRule.HttpActionHeaderProperty(
                            key="key",
                            value="value"
                        )]
                    ),
                    iot_analytics=iot.CfnTopicRule.IotAnalyticsActionProperty(
                        channel_name="channelName",
                        role_arn="roleArn",
        
                        # the properties below are optional
                        batch_mode=False
                    ),
                    iot_events=iot.CfnTopicRule.IotEventsActionProperty(
                        input_name="inputName",
                        role_arn="roleArn",
        
                        # the properties below are optional
                        batch_mode=False,
                        message_id="messageId"
                    ),
                    iot_site_wise=iot.CfnTopicRule.IotSiteWiseActionProperty(
                        put_asset_property_value_entries=[iot.CfnTopicRule.PutAssetPropertyValueEntryProperty(
                            property_values=[iot.CfnTopicRule.AssetPropertyValueProperty(
                                timestamp=iot.CfnTopicRule.AssetPropertyTimestampProperty(
                                    time_in_seconds="timeInSeconds",
        
                                    # the properties below are optional
                                    offset_in_nanos="offsetInNanos"
                                ),
                                value=iot.CfnTopicRule.AssetPropertyVariantProperty(
                                    boolean_value="booleanValue",
                                    double_value="doubleValue",
                                    integer_value="integerValue",
                                    string_value="stringValue"
                                ),
        
                                # the properties below are optional
                                quality="quality"
                            )],
        
                            # the properties below are optional
                            asset_id="assetId",
                            entry_id="entryId",
                            property_alias="propertyAlias",
                            property_id="propertyId"
                        )],
                        role_arn="roleArn"
                    ),
                    kafka=iot.CfnTopicRule.KafkaActionProperty(
                        client_properties={
                            "client_properties_key": "clientProperties"
                        },
                        destination_arn="destinationArn",
                        topic="topic",
        
                        # the properties below are optional
                        key="key",
                        partition="partition"
                    ),
                    kinesis=iot.CfnTopicRule.KinesisActionProperty(
                        role_arn="roleArn",
                        stream_name="streamName",
        
                        # the properties below are optional
                        partition_key="partitionKey"
                    ),
                    lambda_=iot.CfnTopicRule.LambdaActionProperty(
                        function_arn="functionArn"
                    ),
                    location=iot.CfnTopicRule.LocationActionProperty(
                        device_id="deviceId",
                        latitude="latitude",
                        longitude="longitude",
                        role_arn="roleArn",
                        tracker_name="trackerName",
        
                        # the properties below are optional
                        timestamp=Date()
                    ),
                    open_search=iot.CfnTopicRule.OpenSearchActionProperty(
                        endpoint="endpoint",
                        id="id",
                        index="index",
                        role_arn="roleArn",
                        type="type"
                    ),
                    republish=iot.CfnTopicRule.RepublishActionProperty(
                        role_arn="roleArn",
                        topic="topic",
        
                        # the properties below are optional
                        headers=iot.CfnTopicRule.RepublishActionHeadersProperty(
                            content_type="contentType",
                            correlation_data="correlationData",
                            message_expiry="messageExpiry",
                            payload_format_indicator="payloadFormatIndicator",
                            response_topic="responseTopic",
                            user_properties=[iot.CfnTopicRule.UserPropertyProperty(
                                key="key",
                                value="value"
                            )]
                        ),
                        qos=123
                    ),
                    s3=iot.CfnTopicRule.S3ActionProperty(
                        bucket_name="bucketName",
                        key="key",
                        role_arn="roleArn",
        
                        # the properties below are optional
                        canned_acl="cannedAcl"
                    ),
                    sns=iot.CfnTopicRule.SnsActionProperty(
                        role_arn="roleArn",
                        target_arn="targetArn",
        
                        # the properties below are optional
                        message_format="messageFormat"
                    ),
                    sqs=iot.CfnTopicRule.SqsActionProperty(
                        queue_url="queueUrl",
                        role_arn="roleArn",
        
                        # the properties below are optional
                        use_base64=False
                    ),
                    step_functions=iot.CfnTopicRule.StepFunctionsActionProperty(
                        role_arn="roleArn",
                        state_machine_name="stateMachineName",
        
                        # the properties below are optional
                        execution_name_prefix="executionNamePrefix"
                    ),
                    timestream=iot.CfnTopicRule.TimestreamActionProperty(
                        database_name="databaseName",
                        dimensions=[iot.CfnTopicRule.TimestreamDimensionProperty(
                            name="name",
                            value="value"
                        )],
                        role_arn="roleArn",
                        table_name="tableName",
        
                        # the properties below are optional
                        timestamp=iot.CfnTopicRule.TimestreamTimestampProperty(
                            unit="unit",
                            value="value"
                        )
                    )
                )],
                sql="sql",
        
                # the properties below are optional
                aws_iot_sql_version="awsIotSqlVersion",
                description="description",
                error_action=iot.CfnTopicRule.ActionProperty(
                    cloudwatch_alarm=iot.CfnTopicRule.CloudwatchAlarmActionProperty(
                        alarm_name="alarmName",
                        role_arn="roleArn",
                        state_reason="stateReason",
                        state_value="stateValue"
                    ),
                    cloudwatch_logs=iot.CfnTopicRule.CloudwatchLogsActionProperty(
                        log_group_name="logGroupName",
                        role_arn="roleArn"
                    ),
                    cloudwatch_metric=iot.CfnTopicRule.CloudwatchMetricActionProperty(
                        metric_name="metricName",
                        metric_namespace="metricNamespace",
                        metric_unit="metricUnit",
                        metric_value="metricValue",
                        role_arn="roleArn",
        
                        # the properties below are optional
                        metric_timestamp="metricTimestamp"
                    ),
                    dynamo_db=iot.CfnTopicRule.DynamoDBActionProperty(
                        hash_key_field="hashKeyField",
                        hash_key_value="hashKeyValue",
                        role_arn="roleArn",
                        table_name="tableName",
        
                        # the properties below are optional
                        hash_key_type="hashKeyType",
                        payload_field="payloadField",
                        range_key_field="rangeKeyField",
                        range_key_type="rangeKeyType",
                        range_key_value="rangeKeyValue"
                    ),
                    dynamo_dBv2=iot.CfnTopicRule.DynamoDBv2ActionProperty(
                        put_item=iot.CfnTopicRule.PutItemInputProperty(
                            table_name="tableName"
                        ),
                        role_arn="roleArn"
                    ),
                    elasticsearch=iot.CfnTopicRule.ElasticsearchActionProperty(
                        endpoint="endpoint",
                        id="id",
                        index="index",
                        role_arn="roleArn",
                        type="type"
                    ),
                    firehose=iot.CfnTopicRule.FirehoseActionProperty(
                        delivery_stream_name="deliveryStreamName",
                        role_arn="roleArn",
        
                        # the properties below are optional
                        batch_mode=False,
                        separator="separator"
                    ),
                    http=iot.CfnTopicRule.HttpActionProperty(
                        url="url",
        
                        # the properties below are optional
                        auth=iot.CfnTopicRule.HttpAuthorizationProperty(
                            sigv4=iot.CfnTopicRule.SigV4AuthorizationProperty(
                                role_arn="roleArn",
                                service_name="serviceName",
                                signing_region="signingRegion"
                            )
                        ),
                        confirmation_url="confirmationUrl",
                        headers=[iot.CfnTopicRule.HttpActionHeaderProperty(
                            key="key",
                            value="value"
                        )]
                    ),
                    iot_analytics=iot.CfnTopicRule.IotAnalyticsActionProperty(
                        channel_name="channelName",
                        role_arn="roleArn",
        
                        # the properties below are optional
                        batch_mode=False
                    ),
                    iot_events=iot.CfnTopicRule.IotEventsActionProperty(
                        input_name="inputName",
                        role_arn="roleArn",
        
                        # the properties below are optional
                        batch_mode=False,
                        message_id="messageId"
                    ),
                    iot_site_wise=iot.CfnTopicRule.IotSiteWiseActionProperty(
                        put_asset_property_value_entries=[iot.CfnTopicRule.PutAssetPropertyValueEntryProperty(
                            property_values=[iot.CfnTopicRule.AssetPropertyValueProperty(
                                timestamp=iot.CfnTopicRule.AssetPropertyTimestampProperty(
                                    time_in_seconds="timeInSeconds",
        
                                    # the properties below are optional
                                    offset_in_nanos="offsetInNanos"
                                ),
                                value=iot.CfnTopicRule.AssetPropertyVariantProperty(
                                    boolean_value="booleanValue",
                                    double_value="doubleValue",
                                    integer_value="integerValue",
                                    string_value="stringValue"
                                ),
        
                                # the properties below are optional
                                quality="quality"
                            )],
        
                            # the properties below are optional
                            asset_id="assetId",
                            entry_id="entryId",
                            property_alias="propertyAlias",
                            property_id="propertyId"
                        )],
                        role_arn="roleArn"
                    ),
                    kafka=iot.CfnTopicRule.KafkaActionProperty(
                        client_properties={
                            "client_properties_key": "clientProperties"
                        },
                        destination_arn="destinationArn",
                        topic="topic",
        
                        # the properties below are optional
                        key="key",
                        partition="partition"
                    ),
                    kinesis=iot.CfnTopicRule.KinesisActionProperty(
                        role_arn="roleArn",
                        stream_name="streamName",
        
                        # the properties below are optional
                        partition_key="partitionKey"
                    ),
                    lambda_=iot.CfnTopicRule.LambdaActionProperty(
                        function_arn="functionArn"
                    ),
                    location=iot.CfnTopicRule.LocationActionProperty(
                        device_id="deviceId",
                        latitude="latitude",
                        longitude="longitude",
                        role_arn="roleArn",
                        tracker_name="trackerName",
        
                        # the properties below are optional
                        timestamp=Date()
                    ),
                    open_search=iot.CfnTopicRule.OpenSearchActionProperty(
                        endpoint="endpoint",
                        id="id",
                        index="index",
                        role_arn="roleArn",
                        type="type"
                    ),
                    republish=iot.CfnTopicRule.RepublishActionProperty(
                        role_arn="roleArn",
                        topic="topic",
        
                        # the properties below are optional
                        headers=iot.CfnTopicRule.RepublishActionHeadersProperty(
                            content_type="contentType",
                            correlation_data="correlationData",
                            message_expiry="messageExpiry",
                            payload_format_indicator="payloadFormatIndicator",
                            response_topic="responseTopic",
                            user_properties=[iot.CfnTopicRule.UserPropertyProperty(
                                key="key",
                                value="value"
                            )]
                        ),
                        qos=123
                    ),
                    s3=iot.CfnTopicRule.S3ActionProperty(
                        bucket_name="bucketName",
                        key="key",
                        role_arn="roleArn",
        
                        # the properties below are optional
                        canned_acl="cannedAcl"
                    ),
                    sns=iot.CfnTopicRule.SnsActionProperty(
                        role_arn="roleArn",
                        target_arn="targetArn",
        
                        # the properties below are optional
                        message_format="messageFormat"
                    ),
                    sqs=iot.CfnTopicRule.SqsActionProperty(
                        queue_url="queueUrl",
                        role_arn="roleArn",
        
                        # the properties below are optional
                        use_base64=False
                    ),
                    step_functions=iot.CfnTopicRule.StepFunctionsActionProperty(
                        role_arn="roleArn",
                        state_machine_name="stateMachineName",
        
                        # the properties below are optional
                        execution_name_prefix="executionNamePrefix"
                    ),
                    timestream=iot.CfnTopicRule.TimestreamActionProperty(
                        database_name="databaseName",
                        dimensions=[iot.CfnTopicRule.TimestreamDimensionProperty(
                            name="name",
                            value="value"
                        )],
                        role_arn="roleArn",
                        table_name="tableName",
        
                        # the properties below are optional
                        timestamp=iot.CfnTopicRule.TimestreamTimestampProperty(
                            unit="unit",
                            value="value"
                        )
                    )
                ),
                rule_disabled=False
            ),
        
            # the properties below are optional
            rule_name="ruleName",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        topic_rule_payload: typing.Union[typing.Union["CfnTopicRule.TopicRulePayloadProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
        rule_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::IoT::TopicRule``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param topic_rule_payload: The rule payload.
        :param rule_name: The name of the rule.
        :param tags: Metadata which can be used to manage the topic rule. .. epigraph:: For URI Request parameters use format: ...key1=value1&key2=value2... For the CLI command-line parameter use format: --tags "key1=value1&key2=value2..." For the cli-input-json file use format: "tags": "key1=value1&key2=value2..."
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5780647966e58bc5841b9b1ab64d849ddbcf402f186d19833f5217f9d8952a66)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTopicRuleProps(
            topic_rule_payload=topic_rule_payload, rule_name=rule_name, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d315303b35312dc048d741c1cdc99f5fa2fcc70194c200bd81eb6bb855a1e5da)
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
            type_hints = typing.get_type_hints(_typecheckingstub__57ced7e26a3e501a98010933d35438d0846a95eae5b076e028f69efc82b189cf)
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
        '''The Amazon Resource Name (ARN) of the AWS IoT rule, such as ``arn:aws:iot:us-east-2:123456789012:rule/MyIoTRule`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''Metadata which can be used to manage the topic rule.

        .. epigraph::

           For URI Request parameters use format: ...key1=value1&key2=value2...

           For the CLI command-line parameter use format: --tags "key1=value1&key2=value2..."

           For the cli-input-json file use format: "tags": "key1=value1&key2=value2..."

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicrule.html#cfn-iot-topicrule-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="topicRulePayload")
    def topic_rule_payload(
        self,
    ) -> typing.Union["CfnTopicRule.TopicRulePayloadProperty", _IResolvable_a771d0ef]:
        '''The rule payload.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicrule.html#cfn-iot-topicrule-topicrulepayload
        '''
        return typing.cast(typing.Union["CfnTopicRule.TopicRulePayloadProperty", _IResolvable_a771d0ef], jsii.get(self, "topicRulePayload"))

    @topic_rule_payload.setter
    def topic_rule_payload(
        self,
        value: typing.Union["CfnTopicRule.TopicRulePayloadProperty", _IResolvable_a771d0ef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08263eda82ec6be02e0ca1c2d9fc5febd21c271238f5ce5be2f717b32f1c7f64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "topicRulePayload", value)

    @builtins.property
    @jsii.member(jsii_name="ruleName")
    def rule_name(self) -> typing.Optional[builtins.str]:
        '''The name of the rule.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicrule.html#cfn-iot-topicrule-rulename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleName"))

    @rule_name.setter
    def rule_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__280863e549171664de08582d64da328a8846d2e60295b6a11c6ee8b7f0d625d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleName", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnTopicRule.ActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloudwatch_alarm": "cloudwatchAlarm",
            "cloudwatch_logs": "cloudwatchLogs",
            "cloudwatch_metric": "cloudwatchMetric",
            "dynamo_db": "dynamoDb",
            "dynamo_d_bv2": "dynamoDBv2",
            "elasticsearch": "elasticsearch",
            "firehose": "firehose",
            "http": "http",
            "iot_analytics": "iotAnalytics",
            "iot_events": "iotEvents",
            "iot_site_wise": "iotSiteWise",
            "kafka": "kafka",
            "kinesis": "kinesis",
            "lambda_": "lambda",
            "location": "location",
            "open_search": "openSearch",
            "republish": "republish",
            "s3": "s3",
            "sns": "sns",
            "sqs": "sqs",
            "step_functions": "stepFunctions",
            "timestream": "timestream",
        },
    )
    class ActionProperty:
        def __init__(
            self,
            *,
            cloudwatch_alarm: typing.Optional[typing.Union[typing.Union["CfnTopicRule.CloudwatchAlarmActionProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            cloudwatch_logs: typing.Optional[typing.Union[typing.Union["CfnTopicRule.CloudwatchLogsActionProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            cloudwatch_metric: typing.Optional[typing.Union[typing.Union["CfnTopicRule.CloudwatchMetricActionProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            dynamo_db: typing.Optional[typing.Union[typing.Union["CfnTopicRule.DynamoDBActionProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            dynamo_d_bv2: typing.Optional[typing.Union[typing.Union["CfnTopicRule.DynamoDBv2ActionProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            elasticsearch: typing.Optional[typing.Union[typing.Union["CfnTopicRule.ElasticsearchActionProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            firehose: typing.Optional[typing.Union[typing.Union["CfnTopicRule.FirehoseActionProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            http: typing.Optional[typing.Union[typing.Union["CfnTopicRule.HttpActionProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            iot_analytics: typing.Optional[typing.Union[typing.Union["CfnTopicRule.IotAnalyticsActionProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            iot_events: typing.Optional[typing.Union[typing.Union["CfnTopicRule.IotEventsActionProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            iot_site_wise: typing.Optional[typing.Union[typing.Union["CfnTopicRule.IotSiteWiseActionProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            kafka: typing.Optional[typing.Union[typing.Union["CfnTopicRule.KafkaActionProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            kinesis: typing.Optional[typing.Union[typing.Union["CfnTopicRule.KinesisActionProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            lambda_: typing.Optional[typing.Union[typing.Union["CfnTopicRule.LambdaActionProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            location: typing.Optional[typing.Union[typing.Union["CfnTopicRule.LocationActionProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            open_search: typing.Optional[typing.Union[typing.Union["CfnTopicRule.OpenSearchActionProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            republish: typing.Optional[typing.Union[typing.Union["CfnTopicRule.RepublishActionProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            s3: typing.Optional[typing.Union[typing.Union["CfnTopicRule.S3ActionProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            sns: typing.Optional[typing.Union[typing.Union["CfnTopicRule.SnsActionProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            sqs: typing.Optional[typing.Union[typing.Union["CfnTopicRule.SqsActionProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            step_functions: typing.Optional[typing.Union[typing.Union["CfnTopicRule.StepFunctionsActionProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            timestream: typing.Optional[typing.Union[typing.Union["CfnTopicRule.TimestreamActionProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''Describes the actions associated with a rule.

            :param cloudwatch_alarm: Change the state of a CloudWatch alarm.
            :param cloudwatch_logs: Sends data to CloudWatch.
            :param cloudwatch_metric: Capture a CloudWatch metric.
            :param dynamo_db: Write to a DynamoDB table.
            :param dynamo_d_bv2: Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to write each attribute in an MQTT message payload into a separate DynamoDB column.
            :param elasticsearch: Write data to an Amazon OpenSearch Service domain. .. epigraph:: The ``Elasticsearch`` action can only be used by existing rule actions. To create a new rule action or to update an existing rule action, use the ``OpenSearch`` rule action instead. For more information, see `OpenSearchAction <https://docs.aws.amazon.com//iot/latest/apireference/API_OpenSearchAction.html>`_ .
            :param firehose: Write to an Amazon Kinesis Firehose stream.
            :param http: Send data to an HTTPS endpoint.
            :param iot_analytics: Sends message data to an AWS IoT Analytics channel.
            :param iot_events: Sends an input to an AWS IoT Events detector.
            :param iot_site_wise: Sends data from the MQTT message that triggered the rule to AWS IoT SiteWise asset properties.
            :param kafka: Send messages to an Amazon Managed Streaming for Apache Kafka (Amazon MSK) or self-managed Apache Kafka cluster.
            :param kinesis: Write data to an Amazon Kinesis stream.
            :param lambda_: Invoke a Lambda function.
            :param location: Sends device location data to `Amazon Location Service <https://docs.aws.amazon.com//location/latest/developerguide/welcome.html>`_ .
            :param open_search: Write data to an Amazon OpenSearch Service domain.
            :param republish: Publish to another MQTT topic.
            :param s3: Write to an Amazon S3 bucket.
            :param sns: Publish to an Amazon SNS topic.
            :param sqs: Publish to an Amazon SQS queue.
            :param step_functions: Starts execution of a Step Functions state machine.
            :param timestream: Writes attributes from an MQTT message.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                action_property = iot.CfnTopicRule.ActionProperty(
                    cloudwatch_alarm=iot.CfnTopicRule.CloudwatchAlarmActionProperty(
                        alarm_name="alarmName",
                        role_arn="roleArn",
                        state_reason="stateReason",
                        state_value="stateValue"
                    ),
                    cloudwatch_logs=iot.CfnTopicRule.CloudwatchLogsActionProperty(
                        log_group_name="logGroupName",
                        role_arn="roleArn"
                    ),
                    cloudwatch_metric=iot.CfnTopicRule.CloudwatchMetricActionProperty(
                        metric_name="metricName",
                        metric_namespace="metricNamespace",
                        metric_unit="metricUnit",
                        metric_value="metricValue",
                        role_arn="roleArn",
                
                        # the properties below are optional
                        metric_timestamp="metricTimestamp"
                    ),
                    dynamo_db=iot.CfnTopicRule.DynamoDBActionProperty(
                        hash_key_field="hashKeyField",
                        hash_key_value="hashKeyValue",
                        role_arn="roleArn",
                        table_name="tableName",
                
                        # the properties below are optional
                        hash_key_type="hashKeyType",
                        payload_field="payloadField",
                        range_key_field="rangeKeyField",
                        range_key_type="rangeKeyType",
                        range_key_value="rangeKeyValue"
                    ),
                    dynamo_dBv2=iot.CfnTopicRule.DynamoDBv2ActionProperty(
                        put_item=iot.CfnTopicRule.PutItemInputProperty(
                            table_name="tableName"
                        ),
                        role_arn="roleArn"
                    ),
                    elasticsearch=iot.CfnTopicRule.ElasticsearchActionProperty(
                        endpoint="endpoint",
                        id="id",
                        index="index",
                        role_arn="roleArn",
                        type="type"
                    ),
                    firehose=iot.CfnTopicRule.FirehoseActionProperty(
                        delivery_stream_name="deliveryStreamName",
                        role_arn="roleArn",
                
                        # the properties below are optional
                        batch_mode=False,
                        separator="separator"
                    ),
                    http=iot.CfnTopicRule.HttpActionProperty(
                        url="url",
                
                        # the properties below are optional
                        auth=iot.CfnTopicRule.HttpAuthorizationProperty(
                            sigv4=iot.CfnTopicRule.SigV4AuthorizationProperty(
                                role_arn="roleArn",
                                service_name="serviceName",
                                signing_region="signingRegion"
                            )
                        ),
                        confirmation_url="confirmationUrl",
                        headers=[iot.CfnTopicRule.HttpActionHeaderProperty(
                            key="key",
                            value="value"
                        )]
                    ),
                    iot_analytics=iot.CfnTopicRule.IotAnalyticsActionProperty(
                        channel_name="channelName",
                        role_arn="roleArn",
                
                        # the properties below are optional
                        batch_mode=False
                    ),
                    iot_events=iot.CfnTopicRule.IotEventsActionProperty(
                        input_name="inputName",
                        role_arn="roleArn",
                
                        # the properties below are optional
                        batch_mode=False,
                        message_id="messageId"
                    ),
                    iot_site_wise=iot.CfnTopicRule.IotSiteWiseActionProperty(
                        put_asset_property_value_entries=[iot.CfnTopicRule.PutAssetPropertyValueEntryProperty(
                            property_values=[iot.CfnTopicRule.AssetPropertyValueProperty(
                                timestamp=iot.CfnTopicRule.AssetPropertyTimestampProperty(
                                    time_in_seconds="timeInSeconds",
                
                                    # the properties below are optional
                                    offset_in_nanos="offsetInNanos"
                                ),
                                value=iot.CfnTopicRule.AssetPropertyVariantProperty(
                                    boolean_value="booleanValue",
                                    double_value="doubleValue",
                                    integer_value="integerValue",
                                    string_value="stringValue"
                                ),
                
                                # the properties below are optional
                                quality="quality"
                            )],
                
                            # the properties below are optional
                            asset_id="assetId",
                            entry_id="entryId",
                            property_alias="propertyAlias",
                            property_id="propertyId"
                        )],
                        role_arn="roleArn"
                    ),
                    kafka=iot.CfnTopicRule.KafkaActionProperty(
                        client_properties={
                            "client_properties_key": "clientProperties"
                        },
                        destination_arn="destinationArn",
                        topic="topic",
                
                        # the properties below are optional
                        key="key",
                        partition="partition"
                    ),
                    kinesis=iot.CfnTopicRule.KinesisActionProperty(
                        role_arn="roleArn",
                        stream_name="streamName",
                
                        # the properties below are optional
                        partition_key="partitionKey"
                    ),
                    lambda_=iot.CfnTopicRule.LambdaActionProperty(
                        function_arn="functionArn"
                    ),
                    location=iot.CfnTopicRule.LocationActionProperty(
                        device_id="deviceId",
                        latitude="latitude",
                        longitude="longitude",
                        role_arn="roleArn",
                        tracker_name="trackerName",
                
                        # the properties below are optional
                        timestamp=Date()
                    ),
                    open_search=iot.CfnTopicRule.OpenSearchActionProperty(
                        endpoint="endpoint",
                        id="id",
                        index="index",
                        role_arn="roleArn",
                        type="type"
                    ),
                    republish=iot.CfnTopicRule.RepublishActionProperty(
                        role_arn="roleArn",
                        topic="topic",
                
                        # the properties below are optional
                        headers=iot.CfnTopicRule.RepublishActionHeadersProperty(
                            content_type="contentType",
                            correlation_data="correlationData",
                            message_expiry="messageExpiry",
                            payload_format_indicator="payloadFormatIndicator",
                            response_topic="responseTopic",
                            user_properties=[iot.CfnTopicRule.UserPropertyProperty(
                                key="key",
                                value="value"
                            )]
                        ),
                        qos=123
                    ),
                    s3=iot.CfnTopicRule.S3ActionProperty(
                        bucket_name="bucketName",
                        key="key",
                        role_arn="roleArn",
                
                        # the properties below are optional
                        canned_acl="cannedAcl"
                    ),
                    sns=iot.CfnTopicRule.SnsActionProperty(
                        role_arn="roleArn",
                        target_arn="targetArn",
                
                        # the properties below are optional
                        message_format="messageFormat"
                    ),
                    sqs=iot.CfnTopicRule.SqsActionProperty(
                        queue_url="queueUrl",
                        role_arn="roleArn",
                
                        # the properties below are optional
                        use_base64=False
                    ),
                    step_functions=iot.CfnTopicRule.StepFunctionsActionProperty(
                        role_arn="roleArn",
                        state_machine_name="stateMachineName",
                
                        # the properties below are optional
                        execution_name_prefix="executionNamePrefix"
                    ),
                    timestream=iot.CfnTopicRule.TimestreamActionProperty(
                        database_name="databaseName",
                        dimensions=[iot.CfnTopicRule.TimestreamDimensionProperty(
                            name="name",
                            value="value"
                        )],
                        role_arn="roleArn",
                        table_name="tableName",
                
                        # the properties below are optional
                        timestamp=iot.CfnTopicRule.TimestreamTimestampProperty(
                            unit="unit",
                            value="value"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__25f08751c79228946ac85e1a8a9ae48ed7c71628118f968f4f6fca741c717413)
                check_type(argname="argument cloudwatch_alarm", value=cloudwatch_alarm, expected_type=type_hints["cloudwatch_alarm"])
                check_type(argname="argument cloudwatch_logs", value=cloudwatch_logs, expected_type=type_hints["cloudwatch_logs"])
                check_type(argname="argument cloudwatch_metric", value=cloudwatch_metric, expected_type=type_hints["cloudwatch_metric"])
                check_type(argname="argument dynamo_db", value=dynamo_db, expected_type=type_hints["dynamo_db"])
                check_type(argname="argument dynamo_d_bv2", value=dynamo_d_bv2, expected_type=type_hints["dynamo_d_bv2"])
                check_type(argname="argument elasticsearch", value=elasticsearch, expected_type=type_hints["elasticsearch"])
                check_type(argname="argument firehose", value=firehose, expected_type=type_hints["firehose"])
                check_type(argname="argument http", value=http, expected_type=type_hints["http"])
                check_type(argname="argument iot_analytics", value=iot_analytics, expected_type=type_hints["iot_analytics"])
                check_type(argname="argument iot_events", value=iot_events, expected_type=type_hints["iot_events"])
                check_type(argname="argument iot_site_wise", value=iot_site_wise, expected_type=type_hints["iot_site_wise"])
                check_type(argname="argument kafka", value=kafka, expected_type=type_hints["kafka"])
                check_type(argname="argument kinesis", value=kinesis, expected_type=type_hints["kinesis"])
                check_type(argname="argument lambda_", value=lambda_, expected_type=type_hints["lambda_"])
                check_type(argname="argument location", value=location, expected_type=type_hints["location"])
                check_type(argname="argument open_search", value=open_search, expected_type=type_hints["open_search"])
                check_type(argname="argument republish", value=republish, expected_type=type_hints["republish"])
                check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
                check_type(argname="argument sns", value=sns, expected_type=type_hints["sns"])
                check_type(argname="argument sqs", value=sqs, expected_type=type_hints["sqs"])
                check_type(argname="argument step_functions", value=step_functions, expected_type=type_hints["step_functions"])
                check_type(argname="argument timestream", value=timestream, expected_type=type_hints["timestream"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cloudwatch_alarm is not None:
                self._values["cloudwatch_alarm"] = cloudwatch_alarm
            if cloudwatch_logs is not None:
                self._values["cloudwatch_logs"] = cloudwatch_logs
            if cloudwatch_metric is not None:
                self._values["cloudwatch_metric"] = cloudwatch_metric
            if dynamo_db is not None:
                self._values["dynamo_db"] = dynamo_db
            if dynamo_d_bv2 is not None:
                self._values["dynamo_d_bv2"] = dynamo_d_bv2
            if elasticsearch is not None:
                self._values["elasticsearch"] = elasticsearch
            if firehose is not None:
                self._values["firehose"] = firehose
            if http is not None:
                self._values["http"] = http
            if iot_analytics is not None:
                self._values["iot_analytics"] = iot_analytics
            if iot_events is not None:
                self._values["iot_events"] = iot_events
            if iot_site_wise is not None:
                self._values["iot_site_wise"] = iot_site_wise
            if kafka is not None:
                self._values["kafka"] = kafka
            if kinesis is not None:
                self._values["kinesis"] = kinesis
            if lambda_ is not None:
                self._values["lambda_"] = lambda_
            if location is not None:
                self._values["location"] = location
            if open_search is not None:
                self._values["open_search"] = open_search
            if republish is not None:
                self._values["republish"] = republish
            if s3 is not None:
                self._values["s3"] = s3
            if sns is not None:
                self._values["sns"] = sns
            if sqs is not None:
                self._values["sqs"] = sqs
            if step_functions is not None:
                self._values["step_functions"] = step_functions
            if timestream is not None:
                self._values["timestream"] = timestream

        @builtins.property
        def cloudwatch_alarm(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.CloudwatchAlarmActionProperty", _IResolvable_a771d0ef]]:
            '''Change the state of a CloudWatch alarm.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-cloudwatchalarm
            '''
            result = self._values.get("cloudwatch_alarm")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.CloudwatchAlarmActionProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def cloudwatch_logs(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.CloudwatchLogsActionProperty", _IResolvable_a771d0ef]]:
            '''Sends data to CloudWatch.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-cloudwatchlogs
            '''
            result = self._values.get("cloudwatch_logs")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.CloudwatchLogsActionProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def cloudwatch_metric(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.CloudwatchMetricActionProperty", _IResolvable_a771d0ef]]:
            '''Capture a CloudWatch metric.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-cloudwatchmetric
            '''
            result = self._values.get("cloudwatch_metric")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.CloudwatchMetricActionProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def dynamo_db(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.DynamoDBActionProperty", _IResolvable_a771d0ef]]:
            '''Write to a DynamoDB table.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-dynamodb
            '''
            result = self._values.get("dynamo_db")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.DynamoDBActionProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def dynamo_d_bv2(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.DynamoDBv2ActionProperty", _IResolvable_a771d0ef]]:
            '''Write to a DynamoDB table.

            This is a new version of the DynamoDB action. It allows you to write each attribute in an MQTT message payload into a separate DynamoDB column.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-dynamodbv2
            '''
            result = self._values.get("dynamo_d_bv2")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.DynamoDBv2ActionProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def elasticsearch(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.ElasticsearchActionProperty", _IResolvable_a771d0ef]]:
            '''Write data to an Amazon OpenSearch Service domain.

            .. epigraph::

               The ``Elasticsearch`` action can only be used by existing rule actions. To create a new rule action or to update an existing rule action, use the ``OpenSearch`` rule action instead. For more information, see `OpenSearchAction <https://docs.aws.amazon.com//iot/latest/apireference/API_OpenSearchAction.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-elasticsearch
            '''
            result = self._values.get("elasticsearch")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.ElasticsearchActionProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def firehose(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.FirehoseActionProperty", _IResolvable_a771d0ef]]:
            '''Write to an Amazon Kinesis Firehose stream.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-firehose
            '''
            result = self._values.get("firehose")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.FirehoseActionProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def http(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.HttpActionProperty", _IResolvable_a771d0ef]]:
            '''Send data to an HTTPS endpoint.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-http
            '''
            result = self._values.get("http")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.HttpActionProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def iot_analytics(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.IotAnalyticsActionProperty", _IResolvable_a771d0ef]]:
            '''Sends message data to an AWS IoT Analytics channel.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-iotanalytics
            '''
            result = self._values.get("iot_analytics")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.IotAnalyticsActionProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def iot_events(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.IotEventsActionProperty", _IResolvable_a771d0ef]]:
            '''Sends an input to an AWS IoT Events detector.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-iotevents
            '''
            result = self._values.get("iot_events")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.IotEventsActionProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def iot_site_wise(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.IotSiteWiseActionProperty", _IResolvable_a771d0ef]]:
            '''Sends data from the MQTT message that triggered the rule to AWS IoT SiteWise asset properties.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-iotsitewise
            '''
            result = self._values.get("iot_site_wise")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.IotSiteWiseActionProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def kafka(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.KafkaActionProperty", _IResolvable_a771d0ef]]:
            '''Send messages to an Amazon Managed Streaming for Apache Kafka (Amazon MSK) or self-managed Apache Kafka cluster.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-kafka
            '''
            result = self._values.get("kafka")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.KafkaActionProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def kinesis(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.KinesisActionProperty", _IResolvable_a771d0ef]]:
            '''Write data to an Amazon Kinesis stream.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-kinesis
            '''
            result = self._values.get("kinesis")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.KinesisActionProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def lambda_(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.LambdaActionProperty", _IResolvable_a771d0ef]]:
            '''Invoke a Lambda function.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-lambda
            '''
            result = self._values.get("lambda_")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.LambdaActionProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def location(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.LocationActionProperty", _IResolvable_a771d0ef]]:
            '''Sends device location data to `Amazon Location Service <https://docs.aws.amazon.com//location/latest/developerguide/welcome.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-location
            '''
            result = self._values.get("location")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.LocationActionProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def open_search(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.OpenSearchActionProperty", _IResolvable_a771d0ef]]:
            '''Write data to an Amazon OpenSearch Service domain.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-opensearch
            '''
            result = self._values.get("open_search")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.OpenSearchActionProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def republish(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.RepublishActionProperty", _IResolvable_a771d0ef]]:
            '''Publish to another MQTT topic.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-republish
            '''
            result = self._values.get("republish")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.RepublishActionProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def s3(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.S3ActionProperty", _IResolvable_a771d0ef]]:
            '''Write to an Amazon S3 bucket.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-s3
            '''
            result = self._values.get("s3")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.S3ActionProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def sns(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.SnsActionProperty", _IResolvable_a771d0ef]]:
            '''Publish to an Amazon SNS topic.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-sns
            '''
            result = self._values.get("sns")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.SnsActionProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def sqs(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.SqsActionProperty", _IResolvable_a771d0ef]]:
            '''Publish to an Amazon SQS queue.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-sqs
            '''
            result = self._values.get("sqs")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.SqsActionProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def step_functions(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.StepFunctionsActionProperty", _IResolvable_a771d0ef]]:
            '''Starts execution of a Step Functions state machine.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-stepfunctions
            '''
            result = self._values.get("step_functions")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.StepFunctionsActionProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def timestream(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.TimestreamActionProperty", _IResolvable_a771d0ef]]:
            '''Writes attributes from an MQTT message.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-action.html#cfn-iot-topicrule-action-timestream
            '''
            result = self._values.get("timestream")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.TimestreamActionProperty", _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnTopicRule.AssetPropertyTimestampProperty",
        jsii_struct_bases=[],
        name_mapping={
            "time_in_seconds": "timeInSeconds",
            "offset_in_nanos": "offsetInNanos",
        },
    )
    class AssetPropertyTimestampProperty:
        def __init__(
            self,
            *,
            time_in_seconds: builtins.str,
            offset_in_nanos: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An asset property timestamp entry containing the following information.

            :param time_in_seconds: A string that contains the time in seconds since epoch. Accepts substitution templates.
            :param offset_in_nanos: Optional. A string that contains the nanosecond time offset. Accepts substitution templates.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-assetpropertytimestamp.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                asset_property_timestamp_property = iot.CfnTopicRule.AssetPropertyTimestampProperty(
                    time_in_seconds="timeInSeconds",
                
                    # the properties below are optional
                    offset_in_nanos="offsetInNanos"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6e4e2188ad106b42cba2e456e1ba5b0c14164d9ef67bf367d0aa1c7ae6e5c875)
                check_type(argname="argument time_in_seconds", value=time_in_seconds, expected_type=type_hints["time_in_seconds"])
                check_type(argname="argument offset_in_nanos", value=offset_in_nanos, expected_type=type_hints["offset_in_nanos"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "time_in_seconds": time_in_seconds,
            }
            if offset_in_nanos is not None:
                self._values["offset_in_nanos"] = offset_in_nanos

        @builtins.property
        def time_in_seconds(self) -> builtins.str:
            '''A string that contains the time in seconds since epoch.

            Accepts substitution templates.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-assetpropertytimestamp.html#cfn-iot-topicrule-assetpropertytimestamp-timeinseconds
            '''
            result = self._values.get("time_in_seconds")
            assert result is not None, "Required property 'time_in_seconds' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def offset_in_nanos(self) -> typing.Optional[builtins.str]:
            '''Optional.

            A string that contains the nanosecond time offset. Accepts substitution templates.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-assetpropertytimestamp.html#cfn-iot-topicrule-assetpropertytimestamp-offsetinnanos
            '''
            result = self._values.get("offset_in_nanos")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AssetPropertyTimestampProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnTopicRule.AssetPropertyValueProperty",
        jsii_struct_bases=[],
        name_mapping={
            "timestamp": "timestamp",
            "value": "value",
            "quality": "quality",
        },
    )
    class AssetPropertyValueProperty:
        def __init__(
            self,
            *,
            timestamp: typing.Union[typing.Union["CfnTopicRule.AssetPropertyTimestampProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
            value: typing.Union[typing.Union["CfnTopicRule.AssetPropertyVariantProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
            quality: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An asset property value entry containing the following information.

            :param timestamp: The asset property value timestamp.
            :param value: The value of the asset property.
            :param quality: Optional. A string that describes the quality of the value. Accepts substitution templates. Must be ``GOOD`` , ``BAD`` , or ``UNCERTAIN`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-assetpropertyvalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                asset_property_value_property = iot.CfnTopicRule.AssetPropertyValueProperty(
                    timestamp=iot.CfnTopicRule.AssetPropertyTimestampProperty(
                        time_in_seconds="timeInSeconds",
                
                        # the properties below are optional
                        offset_in_nanos="offsetInNanos"
                    ),
                    value=iot.CfnTopicRule.AssetPropertyVariantProperty(
                        boolean_value="booleanValue",
                        double_value="doubleValue",
                        integer_value="integerValue",
                        string_value="stringValue"
                    ),
                
                    # the properties below are optional
                    quality="quality"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__daf3af14341e848695e62e242ea9b22ce5e9ba2912dee321d72c47666c1422d6)
                check_type(argname="argument timestamp", value=timestamp, expected_type=type_hints["timestamp"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
                check_type(argname="argument quality", value=quality, expected_type=type_hints["quality"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "timestamp": timestamp,
                "value": value,
            }
            if quality is not None:
                self._values["quality"] = quality

        @builtins.property
        def timestamp(
            self,
        ) -> typing.Union["CfnTopicRule.AssetPropertyTimestampProperty", _IResolvable_a771d0ef]:
            '''The asset property value timestamp.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-assetpropertyvalue.html#cfn-iot-topicrule-assetpropertyvalue-timestamp
            '''
            result = self._values.get("timestamp")
            assert result is not None, "Required property 'timestamp' is missing"
            return typing.cast(typing.Union["CfnTopicRule.AssetPropertyTimestampProperty", _IResolvable_a771d0ef], result)

        @builtins.property
        def value(
            self,
        ) -> typing.Union["CfnTopicRule.AssetPropertyVariantProperty", _IResolvable_a771d0ef]:
            '''The value of the asset property.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-assetpropertyvalue.html#cfn-iot-topicrule-assetpropertyvalue-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(typing.Union["CfnTopicRule.AssetPropertyVariantProperty", _IResolvable_a771d0ef], result)

        @builtins.property
        def quality(self) -> typing.Optional[builtins.str]:
            '''Optional.

            A string that describes the quality of the value. Accepts substitution templates. Must be ``GOOD`` , ``BAD`` , or ``UNCERTAIN`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-assetpropertyvalue.html#cfn-iot-topicrule-assetpropertyvalue-quality
            '''
            result = self._values.get("quality")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AssetPropertyValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnTopicRule.AssetPropertyVariantProperty",
        jsii_struct_bases=[],
        name_mapping={
            "boolean_value": "booleanValue",
            "double_value": "doubleValue",
            "integer_value": "integerValue",
            "string_value": "stringValue",
        },
    )
    class AssetPropertyVariantProperty:
        def __init__(
            self,
            *,
            boolean_value: typing.Optional[builtins.str] = None,
            double_value: typing.Optional[builtins.str] = None,
            integer_value: typing.Optional[builtins.str] = None,
            string_value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains an asset property value (of a single type).

            :param boolean_value: Optional. A string that contains the boolean value ( ``true`` or ``false`` ) of the value entry. Accepts substitution templates.
            :param double_value: Optional. A string that contains the double value of the value entry. Accepts substitution templates.
            :param integer_value: Optional. A string that contains the integer value of the value entry. Accepts substitution templates.
            :param string_value: Optional. The string value of the value entry. Accepts substitution templates.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-assetpropertyvariant.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                asset_property_variant_property = iot.CfnTopicRule.AssetPropertyVariantProperty(
                    boolean_value="booleanValue",
                    double_value="doubleValue",
                    integer_value="integerValue",
                    string_value="stringValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__128f95606291f57004f370101538fc181a4a4914357acc2a5f3b871cbb5051f7)
                check_type(argname="argument boolean_value", value=boolean_value, expected_type=type_hints["boolean_value"])
                check_type(argname="argument double_value", value=double_value, expected_type=type_hints["double_value"])
                check_type(argname="argument integer_value", value=integer_value, expected_type=type_hints["integer_value"])
                check_type(argname="argument string_value", value=string_value, expected_type=type_hints["string_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if boolean_value is not None:
                self._values["boolean_value"] = boolean_value
            if double_value is not None:
                self._values["double_value"] = double_value
            if integer_value is not None:
                self._values["integer_value"] = integer_value
            if string_value is not None:
                self._values["string_value"] = string_value

        @builtins.property
        def boolean_value(self) -> typing.Optional[builtins.str]:
            '''Optional.

            A string that contains the boolean value ( ``true`` or ``false`` ) of the value entry. Accepts substitution templates.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-assetpropertyvariant.html#cfn-iot-topicrule-assetpropertyvariant-booleanvalue
            '''
            result = self._values.get("boolean_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def double_value(self) -> typing.Optional[builtins.str]:
            '''Optional.

            A string that contains the double value of the value entry. Accepts substitution templates.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-assetpropertyvariant.html#cfn-iot-topicrule-assetpropertyvariant-doublevalue
            '''
            result = self._values.get("double_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def integer_value(self) -> typing.Optional[builtins.str]:
            '''Optional.

            A string that contains the integer value of the value entry. Accepts substitution templates.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-assetpropertyvariant.html#cfn-iot-topicrule-assetpropertyvariant-integervalue
            '''
            result = self._values.get("integer_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def string_value(self) -> typing.Optional[builtins.str]:
            '''Optional.

            The string value of the value entry. Accepts substitution templates.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-assetpropertyvariant.html#cfn-iot-topicrule-assetpropertyvariant-stringvalue
            '''
            result = self._values.get("string_value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AssetPropertyVariantProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnTopicRule.CloudwatchAlarmActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "alarm_name": "alarmName",
            "role_arn": "roleArn",
            "state_reason": "stateReason",
            "state_value": "stateValue",
        },
    )
    class CloudwatchAlarmActionProperty:
        def __init__(
            self,
            *,
            alarm_name: builtins.str,
            role_arn: builtins.str,
            state_reason: builtins.str,
            state_value: builtins.str,
        ) -> None:
            '''Describes an action that updates a CloudWatch alarm.

            :param alarm_name: The CloudWatch alarm name.
            :param role_arn: The IAM role that allows access to the CloudWatch alarm.
            :param state_reason: The reason for the alarm change.
            :param state_value: The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchalarmaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                cloudwatch_alarm_action_property = iot.CfnTopicRule.CloudwatchAlarmActionProperty(
                    alarm_name="alarmName",
                    role_arn="roleArn",
                    state_reason="stateReason",
                    state_value="stateValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8141e369458dbf936fb0c57a028c2436be2aa10f71ca1fd66656be906b24963d)
                check_type(argname="argument alarm_name", value=alarm_name, expected_type=type_hints["alarm_name"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument state_reason", value=state_reason, expected_type=type_hints["state_reason"])
                check_type(argname="argument state_value", value=state_value, expected_type=type_hints["state_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "alarm_name": alarm_name,
                "role_arn": role_arn,
                "state_reason": state_reason,
                "state_value": state_value,
            }

        @builtins.property
        def alarm_name(self) -> builtins.str:
            '''The CloudWatch alarm name.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchalarmaction.html#cfn-iot-topicrule-cloudwatchalarmaction-alarmname
            '''
            result = self._values.get("alarm_name")
            assert result is not None, "Required property 'alarm_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The IAM role that allows access to the CloudWatch alarm.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchalarmaction.html#cfn-iot-topicrule-cloudwatchalarmaction-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def state_reason(self) -> builtins.str:
            '''The reason for the alarm change.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchalarmaction.html#cfn-iot-topicrule-cloudwatchalarmaction-statereason
            '''
            result = self._values.get("state_reason")
            assert result is not None, "Required property 'state_reason' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def state_value(self) -> builtins.str:
            '''The value of the alarm state.

            Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchalarmaction.html#cfn-iot-topicrule-cloudwatchalarmaction-statevalue
            '''
            result = self._values.get("state_value")
            assert result is not None, "Required property 'state_value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudwatchAlarmActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnTopicRule.CloudwatchLogsActionProperty",
        jsii_struct_bases=[],
        name_mapping={"log_group_name": "logGroupName", "role_arn": "roleArn"},
    )
    class CloudwatchLogsActionProperty:
        def __init__(
            self,
            *,
            log_group_name: builtins.str,
            role_arn: builtins.str,
        ) -> None:
            '''Describes an action that updates a CloudWatch log.

            :param log_group_name: The CloudWatch log name.
            :param role_arn: The IAM role that allows access to the CloudWatch log.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchlogsaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                cloudwatch_logs_action_property = iot.CfnTopicRule.CloudwatchLogsActionProperty(
                    log_group_name="logGroupName",
                    role_arn="roleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2ade46dcee982968d97e8f07e9e4e8e0a87fa367a9d7b0ce01528af365f2501d)
                check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "log_group_name": log_group_name,
                "role_arn": role_arn,
            }

        @builtins.property
        def log_group_name(self) -> builtins.str:
            '''The CloudWatch log name.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchlogsaction.html#cfn-iot-topicrule-cloudwatchlogsaction-loggroupname
            '''
            result = self._values.get("log_group_name")
            assert result is not None, "Required property 'log_group_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The IAM role that allows access to the CloudWatch log.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchlogsaction.html#cfn-iot-topicrule-cloudwatchlogsaction-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudwatchLogsActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnTopicRule.CloudwatchMetricActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "metric_name": "metricName",
            "metric_namespace": "metricNamespace",
            "metric_unit": "metricUnit",
            "metric_value": "metricValue",
            "role_arn": "roleArn",
            "metric_timestamp": "metricTimestamp",
        },
    )
    class CloudwatchMetricActionProperty:
        def __init__(
            self,
            *,
            metric_name: builtins.str,
            metric_namespace: builtins.str,
            metric_unit: builtins.str,
            metric_value: builtins.str,
            role_arn: builtins.str,
            metric_timestamp: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes an action that captures a CloudWatch metric.

            :param metric_name: The CloudWatch metric name.
            :param metric_namespace: The CloudWatch metric namespace name.
            :param metric_unit: The `metric unit <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit>`_ supported by CloudWatch.
            :param metric_value: The CloudWatch metric value.
            :param role_arn: The IAM role that allows access to the CloudWatch metric.
            :param metric_timestamp: An optional `Unix timestamp <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchmetricaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                cloudwatch_metric_action_property = iot.CfnTopicRule.CloudwatchMetricActionProperty(
                    metric_name="metricName",
                    metric_namespace="metricNamespace",
                    metric_unit="metricUnit",
                    metric_value="metricValue",
                    role_arn="roleArn",
                
                    # the properties below are optional
                    metric_timestamp="metricTimestamp"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__670f7ba2a7c5acc73f882a1ee97c0fbbb67d3c3e195fb984e0ec162c5291bab6)
                check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
                check_type(argname="argument metric_namespace", value=metric_namespace, expected_type=type_hints["metric_namespace"])
                check_type(argname="argument metric_unit", value=metric_unit, expected_type=type_hints["metric_unit"])
                check_type(argname="argument metric_value", value=metric_value, expected_type=type_hints["metric_value"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument metric_timestamp", value=metric_timestamp, expected_type=type_hints["metric_timestamp"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "metric_name": metric_name,
                "metric_namespace": metric_namespace,
                "metric_unit": metric_unit,
                "metric_value": metric_value,
                "role_arn": role_arn,
            }
            if metric_timestamp is not None:
                self._values["metric_timestamp"] = metric_timestamp

        @builtins.property
        def metric_name(self) -> builtins.str:
            '''The CloudWatch metric name.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchmetricaction.html#cfn-iot-topicrule-cloudwatchmetricaction-metricname
            '''
            result = self._values.get("metric_name")
            assert result is not None, "Required property 'metric_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def metric_namespace(self) -> builtins.str:
            '''The CloudWatch metric namespace name.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchmetricaction.html#cfn-iot-topicrule-cloudwatchmetricaction-metricnamespace
            '''
            result = self._values.get("metric_namespace")
            assert result is not None, "Required property 'metric_namespace' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def metric_unit(self) -> builtins.str:
            '''The `metric unit <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit>`_ supported by CloudWatch.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchmetricaction.html#cfn-iot-topicrule-cloudwatchmetricaction-metricunit
            '''
            result = self._values.get("metric_unit")
            assert result is not None, "Required property 'metric_unit' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def metric_value(self) -> builtins.str:
            '''The CloudWatch metric value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchmetricaction.html#cfn-iot-topicrule-cloudwatchmetricaction-metricvalue
            '''
            result = self._values.get("metric_value")
            assert result is not None, "Required property 'metric_value' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The IAM role that allows access to the CloudWatch metric.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchmetricaction.html#cfn-iot-topicrule-cloudwatchmetricaction-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def metric_timestamp(self) -> typing.Optional[builtins.str]:
            '''An optional `Unix timestamp <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-cloudwatchmetricaction.html#cfn-iot-topicrule-cloudwatchmetricaction-metrictimestamp
            '''
            result = self._values.get("metric_timestamp")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudwatchMetricActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnTopicRule.DynamoDBActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "hash_key_field": "hashKeyField",
            "hash_key_value": "hashKeyValue",
            "role_arn": "roleArn",
            "table_name": "tableName",
            "hash_key_type": "hashKeyType",
            "payload_field": "payloadField",
            "range_key_field": "rangeKeyField",
            "range_key_type": "rangeKeyType",
            "range_key_value": "rangeKeyValue",
        },
    )
    class DynamoDBActionProperty:
        def __init__(
            self,
            *,
            hash_key_field: builtins.str,
            hash_key_value: builtins.str,
            role_arn: builtins.str,
            table_name: builtins.str,
            hash_key_type: typing.Optional[builtins.str] = None,
            payload_field: typing.Optional[builtins.str] = None,
            range_key_field: typing.Optional[builtins.str] = None,
            range_key_type: typing.Optional[builtins.str] = None,
            range_key_value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes an action to write to a DynamoDB table.

            The ``tableName`` , ``hashKeyField`` , and ``rangeKeyField`` values must match the values used when you created the table.

            The ``hashKeyValue`` and ``rangeKeyvalue`` fields use a substitution template syntax. These templates provide data at runtime. The syntax is as follows: ${ *sql-expression* }.

            You can specify any valid expression in a WHERE or SELECT clause, including JSON properties, comparisons, calculations, and functions. For example, the following field uses the third level of the topic:

            ``"hashKeyValue": "${topic(3)}"``

            The following field uses the timestamp:

            ``"rangeKeyValue": "${timestamp()}"``

            For more information, see `DynamoDBv2 Action <https://docs.aws.amazon.com/iot/latest/developerguide/iot-rule-actions.html>`_ in the *AWS IoT Developer Guide* .

            :param hash_key_field: The hash key name.
            :param hash_key_value: The hash key value.
            :param role_arn: The ARN of the IAM role that grants access to the DynamoDB table.
            :param table_name: The name of the DynamoDB table.
            :param hash_key_type: The hash key type. Valid values are "STRING" or "NUMBER"
            :param payload_field: The action payload. This name can be customized.
            :param range_key_field: The range key name.
            :param range_key_type: The range key type. Valid values are "STRING" or "NUMBER"
            :param range_key_value: The range key value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-dynamodbaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                dynamo_dBAction_property = iot.CfnTopicRule.DynamoDBActionProperty(
                    hash_key_field="hashKeyField",
                    hash_key_value="hashKeyValue",
                    role_arn="roleArn",
                    table_name="tableName",
                
                    # the properties below are optional
                    hash_key_type="hashKeyType",
                    payload_field="payloadField",
                    range_key_field="rangeKeyField",
                    range_key_type="rangeKeyType",
                    range_key_value="rangeKeyValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ae106cdfaa3d9b225f3f627378befde8d966ae3099d658baaa9b87145a02ba51)
                check_type(argname="argument hash_key_field", value=hash_key_field, expected_type=type_hints["hash_key_field"])
                check_type(argname="argument hash_key_value", value=hash_key_value, expected_type=type_hints["hash_key_value"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
                check_type(argname="argument hash_key_type", value=hash_key_type, expected_type=type_hints["hash_key_type"])
                check_type(argname="argument payload_field", value=payload_field, expected_type=type_hints["payload_field"])
                check_type(argname="argument range_key_field", value=range_key_field, expected_type=type_hints["range_key_field"])
                check_type(argname="argument range_key_type", value=range_key_type, expected_type=type_hints["range_key_type"])
                check_type(argname="argument range_key_value", value=range_key_value, expected_type=type_hints["range_key_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "hash_key_field": hash_key_field,
                "hash_key_value": hash_key_value,
                "role_arn": role_arn,
                "table_name": table_name,
            }
            if hash_key_type is not None:
                self._values["hash_key_type"] = hash_key_type
            if payload_field is not None:
                self._values["payload_field"] = payload_field
            if range_key_field is not None:
                self._values["range_key_field"] = range_key_field
            if range_key_type is not None:
                self._values["range_key_type"] = range_key_type
            if range_key_value is not None:
                self._values["range_key_value"] = range_key_value

        @builtins.property
        def hash_key_field(self) -> builtins.str:
            '''The hash key name.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-dynamodbaction.html#cfn-iot-topicrule-dynamodbaction-hashkeyfield
            '''
            result = self._values.get("hash_key_field")
            assert result is not None, "Required property 'hash_key_field' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def hash_key_value(self) -> builtins.str:
            '''The hash key value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-dynamodbaction.html#cfn-iot-topicrule-dynamodbaction-hashkeyvalue
            '''
            result = self._values.get("hash_key_value")
            assert result is not None, "Required property 'hash_key_value' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the IAM role that grants access to the DynamoDB table.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-dynamodbaction.html#cfn-iot-topicrule-dynamodbaction-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def table_name(self) -> builtins.str:
            '''The name of the DynamoDB table.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-dynamodbaction.html#cfn-iot-topicrule-dynamodbaction-tablename
            '''
            result = self._values.get("table_name")
            assert result is not None, "Required property 'table_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def hash_key_type(self) -> typing.Optional[builtins.str]:
            '''The hash key type.

            Valid values are "STRING" or "NUMBER"

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-dynamodbaction.html#cfn-iot-topicrule-dynamodbaction-hashkeytype
            '''
            result = self._values.get("hash_key_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def payload_field(self) -> typing.Optional[builtins.str]:
            '''The action payload.

            This name can be customized.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-dynamodbaction.html#cfn-iot-topicrule-dynamodbaction-payloadfield
            '''
            result = self._values.get("payload_field")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def range_key_field(self) -> typing.Optional[builtins.str]:
            '''The range key name.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-dynamodbaction.html#cfn-iot-topicrule-dynamodbaction-rangekeyfield
            '''
            result = self._values.get("range_key_field")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def range_key_type(self) -> typing.Optional[builtins.str]:
            '''The range key type.

            Valid values are "STRING" or "NUMBER"

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-dynamodbaction.html#cfn-iot-topicrule-dynamodbaction-rangekeytype
            '''
            result = self._values.get("range_key_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def range_key_value(self) -> typing.Optional[builtins.str]:
            '''The range key value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-dynamodbaction.html#cfn-iot-topicrule-dynamodbaction-rangekeyvalue
            '''
            result = self._values.get("range_key_value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DynamoDBActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnTopicRule.DynamoDBv2ActionProperty",
        jsii_struct_bases=[],
        name_mapping={"put_item": "putItem", "role_arn": "roleArn"},
    )
    class DynamoDBv2ActionProperty:
        def __init__(
            self,
            *,
            put_item: typing.Optional[typing.Union[typing.Union["CfnTopicRule.PutItemInputProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            role_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes an action to write to a DynamoDB table.

            This DynamoDB action writes each attribute in the message payload into it's own column in the DynamoDB table.

            :param put_item: Specifies the DynamoDB table to which the message data will be written. For example:. ``{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName": "my-table" } } }`` Each attribute in the message payload will be written to a separate column in the DynamoDB database.
            :param role_arn: The ARN of the IAM role that grants access to the DynamoDB table.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-dynamodbv2action.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                dynamo_dBv2_action_property = iot.CfnTopicRule.DynamoDBv2ActionProperty(
                    put_item=iot.CfnTopicRule.PutItemInputProperty(
                        table_name="tableName"
                    ),
                    role_arn="roleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__075d4c8ae4560d1997fa8eaaeab7db387c19d9b648d6b69b6bfb1eb65b47c30e)
                check_type(argname="argument put_item", value=put_item, expected_type=type_hints["put_item"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if put_item is not None:
                self._values["put_item"] = put_item
            if role_arn is not None:
                self._values["role_arn"] = role_arn

        @builtins.property
        def put_item(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.PutItemInputProperty", _IResolvable_a771d0ef]]:
            '''Specifies the DynamoDB table to which the message data will be written. For example:.

            ``{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName": "my-table" } } }``

            Each attribute in the message payload will be written to a separate column in the DynamoDB database.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-dynamodbv2action.html#cfn-iot-topicrule-dynamodbv2action-putitem
            '''
            result = self._values.get("put_item")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.PutItemInputProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def role_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the IAM role that grants access to the DynamoDB table.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-dynamodbv2action.html#cfn-iot-topicrule-dynamodbv2action-rolearn
            '''
            result = self._values.get("role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DynamoDBv2ActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnTopicRule.ElasticsearchActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint": "endpoint",
            "id": "id",
            "index": "index",
            "role_arn": "roleArn",
            "type": "type",
        },
    )
    class ElasticsearchActionProperty:
        def __init__(
            self,
            *,
            endpoint: builtins.str,
            id: builtins.str,
            index: builtins.str,
            role_arn: builtins.str,
            type: builtins.str,
        ) -> None:
            '''Describes an action that writes data to an Amazon OpenSearch Service domain.

            .. epigraph::

               The ``Elasticsearch`` action can only be used by existing rule actions. To create a new rule action or to update an existing rule action, use the ``OpenSearch`` rule action instead. For more information, see `OpenSearchAction <https://docs.aws.amazon.com//iot/latest/apireference/API_OpenSearchAction.html>`_ .

            :param endpoint: The endpoint of your OpenSearch domain.
            :param id: The unique identifier for the document you are storing.
            :param index: The index where you want to store your data.
            :param role_arn: The IAM role ARN that has access to OpenSearch.
            :param type: The type of document you are storing.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-elasticsearchaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                elasticsearch_action_property = iot.CfnTopicRule.ElasticsearchActionProperty(
                    endpoint="endpoint",
                    id="id",
                    index="index",
                    role_arn="roleArn",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9332bc16170a0b14a81bfb8d35bbceada490bfe002cd9a75edfd9bd085c9ca06)
                check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument index", value=index, expected_type=type_hints["index"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "endpoint": endpoint,
                "id": id,
                "index": index,
                "role_arn": role_arn,
                "type": type,
            }

        @builtins.property
        def endpoint(self) -> builtins.str:
            '''The endpoint of your OpenSearch domain.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-elasticsearchaction.html#cfn-iot-topicrule-elasticsearchaction-endpoint
            '''
            result = self._values.get("endpoint")
            assert result is not None, "Required property 'endpoint' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def id(self) -> builtins.str:
            '''The unique identifier for the document you are storing.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-elasticsearchaction.html#cfn-iot-topicrule-elasticsearchaction-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def index(self) -> builtins.str:
            '''The index where you want to store your data.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-elasticsearchaction.html#cfn-iot-topicrule-elasticsearchaction-index
            '''
            result = self._values.get("index")
            assert result is not None, "Required property 'index' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The IAM role ARN that has access to OpenSearch.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-elasticsearchaction.html#cfn-iot-topicrule-elasticsearchaction-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of document you are storing.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-elasticsearchaction.html#cfn-iot-topicrule-elasticsearchaction-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ElasticsearchActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnTopicRule.FirehoseActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "delivery_stream_name": "deliveryStreamName",
            "role_arn": "roleArn",
            "batch_mode": "batchMode",
            "separator": "separator",
        },
    )
    class FirehoseActionProperty:
        def __init__(
            self,
            *,
            delivery_stream_name: builtins.str,
            role_arn: builtins.str,
            batch_mode: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            separator: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes an action that writes data to an Amazon Kinesis Firehose stream.

            :param delivery_stream_name: The delivery stream name.
            :param role_arn: The IAM role that grants access to the Amazon Kinesis Firehose stream.
            :param batch_mode: Whether to deliver the Kinesis Data Firehose stream as a batch by using ```PutRecordBatch`` <https://docs.aws.amazon.com/firehose/latest/APIReference/API_PutRecordBatch.html>`_ . The default value is ``false`` . When ``batchMode`` is ``true`` and the rule's SQL statement evaluates to an Array, each Array element forms one record in the ```PutRecordBatch`` <https://docs.aws.amazon.com/firehose/latest/APIReference/API_PutRecordBatch.html>`_ request. The resulting array can't have more than 500 records.
            :param separator: A character separator that will be used to separate records written to the Firehose stream. Valid values are: '\\n' (newline), '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-firehoseaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                firehose_action_property = iot.CfnTopicRule.FirehoseActionProperty(
                    delivery_stream_name="deliveryStreamName",
                    role_arn="roleArn",
                
                    # the properties below are optional
                    batch_mode=False,
                    separator="separator"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__964fe8e07ebfd82428752c15d9c27c5ef449220f0760f699afdb4d9d2e0df872)
                check_type(argname="argument delivery_stream_name", value=delivery_stream_name, expected_type=type_hints["delivery_stream_name"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument batch_mode", value=batch_mode, expected_type=type_hints["batch_mode"])
                check_type(argname="argument separator", value=separator, expected_type=type_hints["separator"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "delivery_stream_name": delivery_stream_name,
                "role_arn": role_arn,
            }
            if batch_mode is not None:
                self._values["batch_mode"] = batch_mode
            if separator is not None:
                self._values["separator"] = separator

        @builtins.property
        def delivery_stream_name(self) -> builtins.str:
            '''The delivery stream name.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-firehoseaction.html#cfn-iot-topicrule-firehoseaction-deliverystreamname
            '''
            result = self._values.get("delivery_stream_name")
            assert result is not None, "Required property 'delivery_stream_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The IAM role that grants access to the Amazon Kinesis Firehose stream.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-firehoseaction.html#cfn-iot-topicrule-firehoseaction-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def batch_mode(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Whether to deliver the Kinesis Data Firehose stream as a batch by using ```PutRecordBatch`` <https://docs.aws.amazon.com/firehose/latest/APIReference/API_PutRecordBatch.html>`_ . The default value is ``false`` .

            When ``batchMode`` is ``true`` and the rule's SQL statement evaluates to an Array, each Array element forms one record in the ```PutRecordBatch`` <https://docs.aws.amazon.com/firehose/latest/APIReference/API_PutRecordBatch.html>`_ request. The resulting array can't have more than 500 records.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-firehoseaction.html#cfn-iot-topicrule-firehoseaction-batchmode
            '''
            result = self._values.get("batch_mode")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def separator(self) -> typing.Optional[builtins.str]:
            '''A character separator that will be used to separate records written to the Firehose stream.

            Valid values are: '\\n' (newline), '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-firehoseaction.html#cfn-iot-topicrule-firehoseaction-separator
            '''
            result = self._values.get("separator")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FirehoseActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnTopicRule.HttpActionHeaderProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class HttpActionHeaderProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''The HTTP action header.

            :param key: The HTTP header key.
            :param value: The HTTP header value. Substitution templates are supported.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-httpactionheader.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                http_action_header_property = iot.CfnTopicRule.HttpActionHeaderProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__04569b4551c74ddcbfb1c766475d3c7aeebc6f103dab739f79b04c260e29598d)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''The HTTP header key.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-httpactionheader.html#cfn-iot-topicrule-httpactionheader-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The HTTP header value.

            Substitution templates are supported.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-httpactionheader.html#cfn-iot-topicrule-httpactionheader-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpActionHeaderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnTopicRule.HttpActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "url": "url",
            "auth": "auth",
            "confirmation_url": "confirmationUrl",
            "headers": "headers",
        },
    )
    class HttpActionProperty:
        def __init__(
            self,
            *,
            url: builtins.str,
            auth: typing.Optional[typing.Union[typing.Union["CfnTopicRule.HttpAuthorizationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            confirmation_url: typing.Optional[builtins.str] = None,
            headers: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union["CfnTopicRule.HttpActionHeaderProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]]] = None,
        ) -> None:
            '''Send data to an HTTPS endpoint.

            :param url: The endpoint URL. If substitution templates are used in the URL, you must also specify a ``confirmationUrl`` . If this is a new destination, a new ``TopicRuleDestination`` is created if possible.
            :param auth: The authentication method to use when sending data to an HTTPS endpoint.
            :param confirmation_url: The URL to which AWS IoT sends a confirmation message. The value of the confirmation URL must be a prefix of the endpoint URL. If you do not specify a confirmation URL AWS IoT uses the endpoint URL as the confirmation URL. If you use substitution templates in the confirmationUrl, you must create and enable topic rule destinations that match each possible value of the substitution template before traffic is allowed to your endpoint URL.
            :param headers: The HTTP headers to send with the message data.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-httpaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                http_action_property = iot.CfnTopicRule.HttpActionProperty(
                    url="url",
                
                    # the properties below are optional
                    auth=iot.CfnTopicRule.HttpAuthorizationProperty(
                        sigv4=iot.CfnTopicRule.SigV4AuthorizationProperty(
                            role_arn="roleArn",
                            service_name="serviceName",
                            signing_region="signingRegion"
                        )
                    ),
                    confirmation_url="confirmationUrl",
                    headers=[iot.CfnTopicRule.HttpActionHeaderProperty(
                        key="key",
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__422489f82cd60ea1751702250bbe50041a4bdb9fea56de0ef2cd3cb5509fb54d)
                check_type(argname="argument url", value=url, expected_type=type_hints["url"])
                check_type(argname="argument auth", value=auth, expected_type=type_hints["auth"])
                check_type(argname="argument confirmation_url", value=confirmation_url, expected_type=type_hints["confirmation_url"])
                check_type(argname="argument headers", value=headers, expected_type=type_hints["headers"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "url": url,
            }
            if auth is not None:
                self._values["auth"] = auth
            if confirmation_url is not None:
                self._values["confirmation_url"] = confirmation_url
            if headers is not None:
                self._values["headers"] = headers

        @builtins.property
        def url(self) -> builtins.str:
            '''The endpoint URL.

            If substitution templates are used in the URL, you must also specify a ``confirmationUrl`` . If this is a new destination, a new ``TopicRuleDestination`` is created if possible.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-httpaction.html#cfn-iot-topicrule-httpaction-url
            '''
            result = self._values.get("url")
            assert result is not None, "Required property 'url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def auth(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.HttpAuthorizationProperty", _IResolvable_a771d0ef]]:
            '''The authentication method to use when sending data to an HTTPS endpoint.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-httpaction.html#cfn-iot-topicrule-httpaction-auth
            '''
            result = self._values.get("auth")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.HttpAuthorizationProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def confirmation_url(self) -> typing.Optional[builtins.str]:
            '''The URL to which AWS IoT sends a confirmation message.

            The value of the confirmation URL must be a prefix of the endpoint URL. If you do not specify a confirmation URL AWS IoT uses the endpoint URL as the confirmation URL. If you use substitution templates in the confirmationUrl, you must create and enable topic rule destinations that match each possible value of the substitution template before traffic is allowed to your endpoint URL.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-httpaction.html#cfn-iot-topicrule-httpaction-confirmationurl
            '''
            result = self._values.get("confirmation_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def headers(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTopicRule.HttpActionHeaderProperty", _IResolvable_a771d0ef]]]]:
            '''The HTTP headers to send with the message data.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-httpaction.html#cfn-iot-topicrule-httpaction-headers
            '''
            result = self._values.get("headers")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTopicRule.HttpActionHeaderProperty", _IResolvable_a771d0ef]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnTopicRule.HttpAuthorizationProperty",
        jsii_struct_bases=[],
        name_mapping={"sigv4": "sigv4"},
    )
    class HttpAuthorizationProperty:
        def __init__(
            self,
            *,
            sigv4: typing.Optional[typing.Union[typing.Union["CfnTopicRule.SigV4AuthorizationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''The authorization method used to send messages.

            :param sigv4: Use Sig V4 authorization. For more information, see `Signature Version 4 Signing Process <https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-httpauthorization.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                http_authorization_property = iot.CfnTopicRule.HttpAuthorizationProperty(
                    sigv4=iot.CfnTopicRule.SigV4AuthorizationProperty(
                        role_arn="roleArn",
                        service_name="serviceName",
                        signing_region="signingRegion"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d8201e4078dc4255867c7807fd2c90b8849b63044deba6157801bf278e2bf686)
                check_type(argname="argument sigv4", value=sigv4, expected_type=type_hints["sigv4"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if sigv4 is not None:
                self._values["sigv4"] = sigv4

        @builtins.property
        def sigv4(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.SigV4AuthorizationProperty", _IResolvable_a771d0ef]]:
            '''Use Sig V4 authorization.

            For more information, see `Signature Version 4 Signing Process <https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-httpauthorization.html#cfn-iot-topicrule-httpauthorization-sigv4
            '''
            result = self._values.get("sigv4")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.SigV4AuthorizationProperty", _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpAuthorizationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnTopicRule.IotAnalyticsActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "channel_name": "channelName",
            "role_arn": "roleArn",
            "batch_mode": "batchMode",
        },
    )
    class IotAnalyticsActionProperty:
        def __init__(
            self,
            *,
            channel_name: builtins.str,
            role_arn: builtins.str,
            batch_mode: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''Sends message data to an AWS IoT Analytics channel.

            :param channel_name: The name of the IoT Analytics channel to which message data will be sent.
            :param role_arn: The ARN of the role which has a policy that grants IoT Analytics permission to send message data via IoT Analytics (iotanalytics:BatchPutMessage).
            :param batch_mode: Whether to process the action as a batch. The default value is ``false`` . When ``batchMode`` is ``true`` and the rule SQL statement evaluates to an Array, each Array element is delivered as a separate message when passed by ```BatchPutMessage`` <https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_BatchPutMessage.html>`_ The resulting array can't have more than 100 messages.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-iotanalyticsaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                iot_analytics_action_property = iot.CfnTopicRule.IotAnalyticsActionProperty(
                    channel_name="channelName",
                    role_arn="roleArn",
                
                    # the properties below are optional
                    batch_mode=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d201cf9c7748acbb339ae03d069d7a07dc1fb07c23838f7ca1b618f27375697b)
                check_type(argname="argument channel_name", value=channel_name, expected_type=type_hints["channel_name"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument batch_mode", value=batch_mode, expected_type=type_hints["batch_mode"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "channel_name": channel_name,
                "role_arn": role_arn,
            }
            if batch_mode is not None:
                self._values["batch_mode"] = batch_mode

        @builtins.property
        def channel_name(self) -> builtins.str:
            '''The name of the IoT Analytics channel to which message data will be sent.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-iotanalyticsaction.html#cfn-iot-topicrule-iotanalyticsaction-channelname
            '''
            result = self._values.get("channel_name")
            assert result is not None, "Required property 'channel_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the role which has a policy that grants IoT Analytics permission to send message data via IoT Analytics (iotanalytics:BatchPutMessage).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-iotanalyticsaction.html#cfn-iot-topicrule-iotanalyticsaction-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def batch_mode(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Whether to process the action as a batch. The default value is ``false`` .

            When ``batchMode`` is ``true`` and the rule SQL statement evaluates to an Array, each Array element is delivered as a separate message when passed by ```BatchPutMessage`` <https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_BatchPutMessage.html>`_ The resulting array can't have more than 100 messages.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-iotanalyticsaction.html#cfn-iot-topicrule-iotanalyticsaction-batchmode
            '''
            result = self._values.get("batch_mode")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IotAnalyticsActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnTopicRule.IotEventsActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "input_name": "inputName",
            "role_arn": "roleArn",
            "batch_mode": "batchMode",
            "message_id": "messageId",
        },
    )
    class IotEventsActionProperty:
        def __init__(
            self,
            *,
            input_name: builtins.str,
            role_arn: builtins.str,
            batch_mode: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            message_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Sends an input to an AWS IoT Events detector.

            :param input_name: The name of the AWS IoT Events input.
            :param role_arn: The ARN of the role that grants AWS IoT permission to send an input to an AWS IoT Events detector. ("Action":"iotevents:BatchPutMessage").
            :param batch_mode: Whether to process the event actions as a batch. The default value is ``false`` . When ``batchMode`` is ``true`` , you can't specify a ``messageId`` . When ``batchMode`` is ``true`` and the rule SQL statement evaluates to an Array, each Array element is treated as a separate message when Events by calling ```BatchPutMessage`` <https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_BatchPutMessage.html>`_ . The resulting array can't have more than 10 messages.
            :param message_id: The ID of the message. The default ``messageId`` is a new UUID value. When ``batchMode`` is ``true`` , you can't specify a ``messageId`` --a new UUID value will be assigned. Assign a value to this property to ensure that only one input (message) with a given ``messageId`` will be processed by an AWS IoT Events detector.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-ioteventsaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                iot_events_action_property = iot.CfnTopicRule.IotEventsActionProperty(
                    input_name="inputName",
                    role_arn="roleArn",
                
                    # the properties below are optional
                    batch_mode=False,
                    message_id="messageId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f7c70a453b926326945287307b0539dd9b3cf53583d2870eaa5ee099a88c7c2e)
                check_type(argname="argument input_name", value=input_name, expected_type=type_hints["input_name"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument batch_mode", value=batch_mode, expected_type=type_hints["batch_mode"])
                check_type(argname="argument message_id", value=message_id, expected_type=type_hints["message_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "input_name": input_name,
                "role_arn": role_arn,
            }
            if batch_mode is not None:
                self._values["batch_mode"] = batch_mode
            if message_id is not None:
                self._values["message_id"] = message_id

        @builtins.property
        def input_name(self) -> builtins.str:
            '''The name of the AWS IoT Events input.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-ioteventsaction.html#cfn-iot-topicrule-ioteventsaction-inputname
            '''
            result = self._values.get("input_name")
            assert result is not None, "Required property 'input_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the role that grants AWS IoT permission to send an input to an AWS IoT Events detector.

            ("Action":"iotevents:BatchPutMessage").

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-ioteventsaction.html#cfn-iot-topicrule-ioteventsaction-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def batch_mode(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Whether to process the event actions as a batch. The default value is ``false`` .

            When ``batchMode`` is ``true`` , you can't specify a ``messageId`` .

            When ``batchMode`` is ``true`` and the rule SQL statement evaluates to an Array, each Array element is treated as a separate message when Events by calling ```BatchPutMessage`` <https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_BatchPutMessage.html>`_ . The resulting array can't have more than 10 messages.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-ioteventsaction.html#cfn-iot-topicrule-ioteventsaction-batchmode
            '''
            result = self._values.get("batch_mode")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def message_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the message. The default ``messageId`` is a new UUID value.

            When ``batchMode`` is ``true`` , you can't specify a ``messageId`` --a new UUID value will be assigned.

            Assign a value to this property to ensure that only one input (message) with a given ``messageId`` will be processed by an AWS IoT Events detector.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-ioteventsaction.html#cfn-iot-topicrule-ioteventsaction-messageid
            '''
            result = self._values.get("message_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IotEventsActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnTopicRule.IotSiteWiseActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "put_asset_property_value_entries": "putAssetPropertyValueEntries",
            "role_arn": "roleArn",
        },
    )
    class IotSiteWiseActionProperty:
        def __init__(
            self,
            *,
            put_asset_property_value_entries: typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union["CfnTopicRule.PutAssetPropertyValueEntryProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]],
            role_arn: builtins.str,
        ) -> None:
            '''Describes an action to send data from an MQTT message that triggered the rule to AWS IoT SiteWise asset properties.

            :param put_asset_property_value_entries: A list of asset property value entries.
            :param role_arn: The ARN of the role that grants AWS IoT permission to send an asset property value to AWS IoT SiteWise. ( ``"Action": "iotsitewise:BatchPutAssetPropertyValue"`` ). The trust policy can restrict access to specific asset hierarchy paths.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-iotsitewiseaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                iot_site_wise_action_property = iot.CfnTopicRule.IotSiteWiseActionProperty(
                    put_asset_property_value_entries=[iot.CfnTopicRule.PutAssetPropertyValueEntryProperty(
                        property_values=[iot.CfnTopicRule.AssetPropertyValueProperty(
                            timestamp=iot.CfnTopicRule.AssetPropertyTimestampProperty(
                                time_in_seconds="timeInSeconds",
                
                                # the properties below are optional
                                offset_in_nanos="offsetInNanos"
                            ),
                            value=iot.CfnTopicRule.AssetPropertyVariantProperty(
                                boolean_value="booleanValue",
                                double_value="doubleValue",
                                integer_value="integerValue",
                                string_value="stringValue"
                            ),
                
                            # the properties below are optional
                            quality="quality"
                        )],
                
                        # the properties below are optional
                        asset_id="assetId",
                        entry_id="entryId",
                        property_alias="propertyAlias",
                        property_id="propertyId"
                    )],
                    role_arn="roleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b272cfa6ee5519c1547d4e5459e0dd8e5c4b291d28984e95dbd422204707b751)
                check_type(argname="argument put_asset_property_value_entries", value=put_asset_property_value_entries, expected_type=type_hints["put_asset_property_value_entries"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "put_asset_property_value_entries": put_asset_property_value_entries,
                "role_arn": role_arn,
            }

        @builtins.property
        def put_asset_property_value_entries(
            self,
        ) -> typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTopicRule.PutAssetPropertyValueEntryProperty", _IResolvable_a771d0ef]]]:
            '''A list of asset property value entries.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-iotsitewiseaction.html#cfn-iot-topicrule-iotsitewiseaction-putassetpropertyvalueentries
            '''
            result = self._values.get("put_asset_property_value_entries")
            assert result is not None, "Required property 'put_asset_property_value_entries' is missing"
            return typing.cast(typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTopicRule.PutAssetPropertyValueEntryProperty", _IResolvable_a771d0ef]]], result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the role that grants AWS IoT permission to send an asset property value to AWS IoT SiteWise.

            ( ``"Action": "iotsitewise:BatchPutAssetPropertyValue"`` ). The trust policy can restrict access to specific asset hierarchy paths.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-iotsitewiseaction.html#cfn-iot-topicrule-iotsitewiseaction-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IotSiteWiseActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnTopicRule.KafkaActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "client_properties": "clientProperties",
            "destination_arn": "destinationArn",
            "topic": "topic",
            "key": "key",
            "partition": "partition",
        },
    )
    class KafkaActionProperty:
        def __init__(
            self,
            *,
            client_properties: typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, builtins.str]],
            destination_arn: builtins.str,
            topic: builtins.str,
            key: typing.Optional[builtins.str] = None,
            partition: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Send messages to an Amazon Managed Streaming for Apache Kafka (Amazon MSK) or self-managed Apache Kafka cluster.

            :param client_properties: Properties of the Apache Kafka producer client.
            :param destination_arn: The ARN of Kafka action's VPC ``TopicRuleDestination`` .
            :param topic: The Kafka topic for messages to be sent to the Kafka broker.
            :param key: The Kafka message key.
            :param partition: The Kafka message partition.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-kafkaaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                kafka_action_property = iot.CfnTopicRule.KafkaActionProperty(
                    client_properties={
                        "client_properties_key": "clientProperties"
                    },
                    destination_arn="destinationArn",
                    topic="topic",
                
                    # the properties below are optional
                    key="key",
                    partition="partition"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__955d06c2844189c8ea86b26203fff54ce63ce3b58df2dd2c4b115ddaa856859a)
                check_type(argname="argument client_properties", value=client_properties, expected_type=type_hints["client_properties"])
                check_type(argname="argument destination_arn", value=destination_arn, expected_type=type_hints["destination_arn"])
                check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument partition", value=partition, expected_type=type_hints["partition"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "client_properties": client_properties,
                "destination_arn": destination_arn,
                "topic": topic,
            }
            if key is not None:
                self._values["key"] = key
            if partition is not None:
                self._values["partition"] = partition

        @builtins.property
        def client_properties(
            self,
        ) -> typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, builtins.str]]:
            '''Properties of the Apache Kafka producer client.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-kafkaaction.html#cfn-iot-topicrule-kafkaaction-clientproperties
            '''
            result = self._values.get("client_properties")
            assert result is not None, "Required property 'client_properties' is missing"
            return typing.cast(typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, builtins.str]], result)

        @builtins.property
        def destination_arn(self) -> builtins.str:
            '''The ARN of Kafka action's VPC ``TopicRuleDestination`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-kafkaaction.html#cfn-iot-topicrule-kafkaaction-destinationarn
            '''
            result = self._values.get("destination_arn")
            assert result is not None, "Required property 'destination_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def topic(self) -> builtins.str:
            '''The Kafka topic for messages to be sent to the Kafka broker.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-kafkaaction.html#cfn-iot-topicrule-kafkaaction-topic
            '''
            result = self._values.get("topic")
            assert result is not None, "Required property 'topic' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''The Kafka message key.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-kafkaaction.html#cfn-iot-topicrule-kafkaaction-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def partition(self) -> typing.Optional[builtins.str]:
            '''The Kafka message partition.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-kafkaaction.html#cfn-iot-topicrule-kafkaaction-partition
            '''
            result = self._values.get("partition")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KafkaActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnTopicRule.KinesisActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "role_arn": "roleArn",
            "stream_name": "streamName",
            "partition_key": "partitionKey",
        },
    )
    class KinesisActionProperty:
        def __init__(
            self,
            *,
            role_arn: builtins.str,
            stream_name: builtins.str,
            partition_key: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes an action to write data to an Amazon Kinesis stream.

            :param role_arn: The ARN of the IAM role that grants access to the Amazon Kinesis stream.
            :param stream_name: The name of the Amazon Kinesis stream.
            :param partition_key: The partition key.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-kinesisaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                kinesis_action_property = iot.CfnTopicRule.KinesisActionProperty(
                    role_arn="roleArn",
                    stream_name="streamName",
                
                    # the properties below are optional
                    partition_key="partitionKey"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__690b42f1fbc9f7d8e0177522fcc8b685f8f51de31efe1e79e34849eb7ddaa66c)
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument stream_name", value=stream_name, expected_type=type_hints["stream_name"])
                check_type(argname="argument partition_key", value=partition_key, expected_type=type_hints["partition_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "role_arn": role_arn,
                "stream_name": stream_name,
            }
            if partition_key is not None:
                self._values["partition_key"] = partition_key

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the IAM role that grants access to the Amazon Kinesis stream.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-kinesisaction.html#cfn-iot-topicrule-kinesisaction-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def stream_name(self) -> builtins.str:
            '''The name of the Amazon Kinesis stream.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-kinesisaction.html#cfn-iot-topicrule-kinesisaction-streamname
            '''
            result = self._values.get("stream_name")
            assert result is not None, "Required property 'stream_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def partition_key(self) -> typing.Optional[builtins.str]:
            '''The partition key.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-kinesisaction.html#cfn-iot-topicrule-kinesisaction-partitionkey
            '''
            result = self._values.get("partition_key")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnTopicRule.LambdaActionProperty",
        jsii_struct_bases=[],
        name_mapping={"function_arn": "functionArn"},
    )
    class LambdaActionProperty:
        def __init__(
            self,
            *,
            function_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes an action to invoke a Lambda function.

            :param function_arn: The ARN of the Lambda function.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-lambdaaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                lambda_action_property = iot.CfnTopicRule.LambdaActionProperty(
                    function_arn="functionArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__512b80aa733d6d9b7a41a403040f6f160661dfbfff30438983ed9b7d28e415f3)
                check_type(argname="argument function_arn", value=function_arn, expected_type=type_hints["function_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if function_arn is not None:
                self._values["function_arn"] = function_arn

        @builtins.property
        def function_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the Lambda function.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-lambdaaction.html#cfn-iot-topicrule-lambdaaction-functionarn
            '''
            result = self._values.get("function_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnTopicRule.LocationActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "device_id": "deviceId",
            "latitude": "latitude",
            "longitude": "longitude",
            "role_arn": "roleArn",
            "tracker_name": "trackerName",
            "timestamp": "timestamp",
        },
    )
    class LocationActionProperty:
        def __init__(
            self,
            *,
            device_id: builtins.str,
            latitude: builtins.str,
            longitude: builtins.str,
            role_arn: builtins.str,
            tracker_name: builtins.str,
            timestamp: typing.Optional[typing.Union[_IResolvable_a771d0ef, datetime.datetime]] = None,
        ) -> None:
            '''Describes an action to send device location updates from an MQTT message to an Amazon Location tracker resource.

            :param device_id: The unique ID of the device providing the location data.
            :param latitude: A string that evaluates to a double value that represents the latitude of the device's location.
            :param longitude: A string that evaluates to a double value that represents the longitude of the device's location.
            :param role_arn: The IAM role that grants permission to write to the Amazon Location resource.
            :param tracker_name: The name of the tracker resource in Amazon Location in which the location is updated.
            :param timestamp: The time that the location data was sampled. The default value is the time the MQTT message was processed.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-locationaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                location_action_property = iot.CfnTopicRule.LocationActionProperty(
                    device_id="deviceId",
                    latitude="latitude",
                    longitude="longitude",
                    role_arn="roleArn",
                    tracker_name="trackerName",
                
                    # the properties below are optional
                    timestamp=Date()
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3c313dcd38d2393ca4a812109e774b48eeee5d674fe3d54bd7db53491e2620f5)
                check_type(argname="argument device_id", value=device_id, expected_type=type_hints["device_id"])
                check_type(argname="argument latitude", value=latitude, expected_type=type_hints["latitude"])
                check_type(argname="argument longitude", value=longitude, expected_type=type_hints["longitude"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument tracker_name", value=tracker_name, expected_type=type_hints["tracker_name"])
                check_type(argname="argument timestamp", value=timestamp, expected_type=type_hints["timestamp"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "device_id": device_id,
                "latitude": latitude,
                "longitude": longitude,
                "role_arn": role_arn,
                "tracker_name": tracker_name,
            }
            if timestamp is not None:
                self._values["timestamp"] = timestamp

        @builtins.property
        def device_id(self) -> builtins.str:
            '''The unique ID of the device providing the location data.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-locationaction.html#cfn-iot-topicrule-locationaction-deviceid
            '''
            result = self._values.get("device_id")
            assert result is not None, "Required property 'device_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def latitude(self) -> builtins.str:
            '''A string that evaluates to a double value that represents the latitude of the device's location.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-locationaction.html#cfn-iot-topicrule-locationaction-latitude
            '''
            result = self._values.get("latitude")
            assert result is not None, "Required property 'latitude' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def longitude(self) -> builtins.str:
            '''A string that evaluates to a double value that represents the longitude of the device's location.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-locationaction.html#cfn-iot-topicrule-locationaction-longitude
            '''
            result = self._values.get("longitude")
            assert result is not None, "Required property 'longitude' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The IAM role that grants permission to write to the Amazon Location resource.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-locationaction.html#cfn-iot-topicrule-locationaction-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def tracker_name(self) -> builtins.str:
            '''The name of the tracker resource in Amazon Location in which the location is updated.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-locationaction.html#cfn-iot-topicrule-locationaction-trackername
            '''
            result = self._values.get("tracker_name")
            assert result is not None, "Required property 'tracker_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def timestamp(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, datetime.datetime]]:
            '''The time that the location data was sampled.

            The default value is the time the MQTT message was processed.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-locationaction.html#cfn-iot-topicrule-locationaction-timestamp
            '''
            result = self._values.get("timestamp")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, datetime.datetime]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LocationActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnTopicRule.OpenSearchActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint": "endpoint",
            "id": "id",
            "index": "index",
            "role_arn": "roleArn",
            "type": "type",
        },
    )
    class OpenSearchActionProperty:
        def __init__(
            self,
            *,
            endpoint: builtins.str,
            id: builtins.str,
            index: builtins.str,
            role_arn: builtins.str,
            type: builtins.str,
        ) -> None:
            '''Describes an action that writes data to an Amazon OpenSearch Service domain.

            :param endpoint: The endpoint of your OpenSearch domain.
            :param id: The unique identifier for the document you are storing.
            :param index: The OpenSearch index where you want to store your data.
            :param role_arn: The IAM role ARN that has access to OpenSearch.
            :param type: The type of document you are storing.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-opensearchaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                open_search_action_property = iot.CfnTopicRule.OpenSearchActionProperty(
                    endpoint="endpoint",
                    id="id",
                    index="index",
                    role_arn="roleArn",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__65340f3d0af5956ac0dce9020bcc9191a17f60daecdac7e09bee689eddf1449c)
                check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument index", value=index, expected_type=type_hints["index"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "endpoint": endpoint,
                "id": id,
                "index": index,
                "role_arn": role_arn,
                "type": type,
            }

        @builtins.property
        def endpoint(self) -> builtins.str:
            '''The endpoint of your OpenSearch domain.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-opensearchaction.html#cfn-iot-topicrule-opensearchaction-endpoint
            '''
            result = self._values.get("endpoint")
            assert result is not None, "Required property 'endpoint' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def id(self) -> builtins.str:
            '''The unique identifier for the document you are storing.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-opensearchaction.html#cfn-iot-topicrule-opensearchaction-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def index(self) -> builtins.str:
            '''The OpenSearch index where you want to store your data.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-opensearchaction.html#cfn-iot-topicrule-opensearchaction-index
            '''
            result = self._values.get("index")
            assert result is not None, "Required property 'index' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The IAM role ARN that has access to OpenSearch.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-opensearchaction.html#cfn-iot-topicrule-opensearchaction-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of document you are storing.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-opensearchaction.html#cfn-iot-topicrule-opensearchaction-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OpenSearchActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnTopicRule.PutAssetPropertyValueEntryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "property_values": "propertyValues",
            "asset_id": "assetId",
            "entry_id": "entryId",
            "property_alias": "propertyAlias",
            "property_id": "propertyId",
        },
    )
    class PutAssetPropertyValueEntryProperty:
        def __init__(
            self,
            *,
            property_values: typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union["CfnTopicRule.AssetPropertyValueProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]],
            asset_id: typing.Optional[builtins.str] = None,
            entry_id: typing.Optional[builtins.str] = None,
            property_alias: typing.Optional[builtins.str] = None,
            property_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An asset property value entry containing the following information.

            :param property_values: A list of property values to insert that each contain timestamp, quality, and value (TQV) information.
            :param asset_id: The ID of the AWS IoT SiteWise asset. You must specify either a ``propertyAlias`` or both an ``aliasId`` and a ``propertyId`` . Accepts substitution templates.
            :param entry_id: Optional. A unique identifier for this entry that you can define to better track which message caused an error in case of failure. Accepts substitution templates. Defaults to a new UUID.
            :param property_alias: The name of the property alias associated with your asset property. You must specify either a ``propertyAlias`` or both an ``aliasId`` and a ``propertyId`` . Accepts substitution templates.
            :param property_id: The ID of the asset's property. You must specify either a ``propertyAlias`` or both an ``aliasId`` and a ``propertyId`` . Accepts substitution templates.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-putassetpropertyvalueentry.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                put_asset_property_value_entry_property = iot.CfnTopicRule.PutAssetPropertyValueEntryProperty(
                    property_values=[iot.CfnTopicRule.AssetPropertyValueProperty(
                        timestamp=iot.CfnTopicRule.AssetPropertyTimestampProperty(
                            time_in_seconds="timeInSeconds",
                
                            # the properties below are optional
                            offset_in_nanos="offsetInNanos"
                        ),
                        value=iot.CfnTopicRule.AssetPropertyVariantProperty(
                            boolean_value="booleanValue",
                            double_value="doubleValue",
                            integer_value="integerValue",
                            string_value="stringValue"
                        ),
                
                        # the properties below are optional
                        quality="quality"
                    )],
                
                    # the properties below are optional
                    asset_id="assetId",
                    entry_id="entryId",
                    property_alias="propertyAlias",
                    property_id="propertyId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c4e9228ec16fc3cc0f064ab7dd66bd0f3d7f4653676d60c0781886ed1587cbd5)
                check_type(argname="argument property_values", value=property_values, expected_type=type_hints["property_values"])
                check_type(argname="argument asset_id", value=asset_id, expected_type=type_hints["asset_id"])
                check_type(argname="argument entry_id", value=entry_id, expected_type=type_hints["entry_id"])
                check_type(argname="argument property_alias", value=property_alias, expected_type=type_hints["property_alias"])
                check_type(argname="argument property_id", value=property_id, expected_type=type_hints["property_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "property_values": property_values,
            }
            if asset_id is not None:
                self._values["asset_id"] = asset_id
            if entry_id is not None:
                self._values["entry_id"] = entry_id
            if property_alias is not None:
                self._values["property_alias"] = property_alias
            if property_id is not None:
                self._values["property_id"] = property_id

        @builtins.property
        def property_values(
            self,
        ) -> typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTopicRule.AssetPropertyValueProperty", _IResolvable_a771d0ef]]]:
            '''A list of property values to insert that each contain timestamp, quality, and value (TQV) information.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-putassetpropertyvalueentry.html#cfn-iot-topicrule-putassetpropertyvalueentry-propertyvalues
            '''
            result = self._values.get("property_values")
            assert result is not None, "Required property 'property_values' is missing"
            return typing.cast(typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTopicRule.AssetPropertyValueProperty", _IResolvable_a771d0ef]]], result)

        @builtins.property
        def asset_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the AWS IoT SiteWise asset.

            You must specify either a ``propertyAlias`` or both an ``aliasId`` and a ``propertyId`` . Accepts substitution templates.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-putassetpropertyvalueentry.html#cfn-iot-topicrule-putassetpropertyvalueentry-assetid
            '''
            result = self._values.get("asset_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def entry_id(self) -> typing.Optional[builtins.str]:
            '''Optional.

            A unique identifier for this entry that you can define to better track which message caused an error in case of failure. Accepts substitution templates. Defaults to a new UUID.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-putassetpropertyvalueentry.html#cfn-iot-topicrule-putassetpropertyvalueentry-entryid
            '''
            result = self._values.get("entry_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def property_alias(self) -> typing.Optional[builtins.str]:
            '''The name of the property alias associated with your asset property.

            You must specify either a ``propertyAlias`` or both an ``aliasId`` and a ``propertyId`` . Accepts substitution templates.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-putassetpropertyvalueentry.html#cfn-iot-topicrule-putassetpropertyvalueentry-propertyalias
            '''
            result = self._values.get("property_alias")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def property_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the asset's property.

            You must specify either a ``propertyAlias`` or both an ``aliasId`` and a ``propertyId`` . Accepts substitution templates.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-putassetpropertyvalueentry.html#cfn-iot-topicrule-putassetpropertyvalueentry-propertyid
            '''
            result = self._values.get("property_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PutAssetPropertyValueEntryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnTopicRule.PutItemInputProperty",
        jsii_struct_bases=[],
        name_mapping={"table_name": "tableName"},
    )
    class PutItemInputProperty:
        def __init__(self, *, table_name: builtins.str) -> None:
            '''The input for the DynamoActionVS action that specifies the DynamoDB table to which the message data will be written.

            :param table_name: The table where the message data will be written.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-putiteminput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                put_item_input_property = iot.CfnTopicRule.PutItemInputProperty(
                    table_name="tableName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__58eccbc1fc25d8820c01d9ee3e094684fecab052f42c577dee96d3e18a98c9ef)
                check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "table_name": table_name,
            }

        @builtins.property
        def table_name(self) -> builtins.str:
            '''The table where the message data will be written.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-putiteminput.html#cfn-iot-topicrule-putiteminput-tablename
            '''
            result = self._values.get("table_name")
            assert result is not None, "Required property 'table_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PutItemInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnTopicRule.RepublishActionHeadersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "content_type": "contentType",
            "correlation_data": "correlationData",
            "message_expiry": "messageExpiry",
            "payload_format_indicator": "payloadFormatIndicator",
            "response_topic": "responseTopic",
            "user_properties": "userProperties",
        },
    )
    class RepublishActionHeadersProperty:
        def __init__(
            self,
            *,
            content_type: typing.Optional[builtins.str] = None,
            correlation_data: typing.Optional[builtins.str] = None,
            message_expiry: typing.Optional[builtins.str] = None,
            payload_format_indicator: typing.Optional[builtins.str] = None,
            response_topic: typing.Optional[builtins.str] = None,
            user_properties: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union["CfnTopicRule.UserPropertyProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]]] = None,
        ) -> None:
            '''Specifies MQTT Version 5.0 headers information. For more information, see `MQTT <https://docs.aws.amazon.com//iot/latest/developerguide/mqtt.html>`_ in the IoT Core Developer Guide.

            :param content_type: A UTF-8 encoded string that describes the content of the publishing message. For more information, see `Content Type <https://docs.aws.amazon.com/https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html#_Toc3901118>`_ in the MQTT Version 5.0 specification. Supports `substitution templates <https://docs.aws.amazon.com//iot/latest/developerguide/iot-substitution-templates.html>`_ .
            :param correlation_data: The base64-encoded binary data used by the sender of the request message to identify which request the response message is for. For more information, see `Correlation Data <https://docs.aws.amazon.com/https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html#_Toc3901115>`_ in the MQTT Version 5.0 specification. Supports `substitution templates <https://docs.aws.amazon.com//iot/latest/developerguide/iot-substitution-templates.html>`_ . .. epigraph:: This binary data must be base64-encoded.
            :param message_expiry: A user-defined integer value that represents the message expiry interval at the broker. If the messages haven't been sent to the subscribers within that interval, the message expires and is removed. The value of ``messageExpiry`` represents the number of seconds before it expires. For more information about the limits of ``messageExpiry`` , see `Message broker and protocol limits and quotas <https://docs.aws.amazon.com//general/latest/gr/iot-core.html#limits_iot>`_ in the IoT Core Reference Guide. Supports `substitution templates <https://docs.aws.amazon.com//iot/latest/developerguide/iot-substitution-templates.html>`_ .
            :param payload_format_indicator: An ``Enum`` string value that indicates whether the payload is formatted as UTF-8. Valid values are ``UNSPECIFIED_BYTES`` and ``UTF8_DATA`` . For more information, see `Payload Format Indicator <https://docs.aws.amazon.com/https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html#_Toc3901111>`_ from the MQTT Version 5.0 specification. Supports `substitution templates <https://docs.aws.amazon.com//iot/latest/developerguide/iot-substitution-templates.html>`_ .
            :param response_topic: A UTF-8 encoded string that's used as the topic name for a response message. The response topic is used to describe the topic to which the receiver should publish as part of the request-response flow. The topic must not contain wildcard characters. For more information, see `Response Topic <https://docs.aws.amazon.com/https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html#_Toc3901114>`_ in the MQTT Version 5.0 specification. Supports `substitution templates <https://docs.aws.amazon.com//iot/latest/developerguide/iot-substitution-templates.html>`_ .
            :param user_properties: An array of key-value pairs that you define in the MQTT5 header.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-republishactionheaders.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                republish_action_headers_property = iot.CfnTopicRule.RepublishActionHeadersProperty(
                    content_type="contentType",
                    correlation_data="correlationData",
                    message_expiry="messageExpiry",
                    payload_format_indicator="payloadFormatIndicator",
                    response_topic="responseTopic",
                    user_properties=[iot.CfnTopicRule.UserPropertyProperty(
                        key="key",
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__04c619e1c6f2b508d2200f1c3ca471be43eb59efcc425565d1bc2aa4a11bd705)
                check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
                check_type(argname="argument correlation_data", value=correlation_data, expected_type=type_hints["correlation_data"])
                check_type(argname="argument message_expiry", value=message_expiry, expected_type=type_hints["message_expiry"])
                check_type(argname="argument payload_format_indicator", value=payload_format_indicator, expected_type=type_hints["payload_format_indicator"])
                check_type(argname="argument response_topic", value=response_topic, expected_type=type_hints["response_topic"])
                check_type(argname="argument user_properties", value=user_properties, expected_type=type_hints["user_properties"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if content_type is not None:
                self._values["content_type"] = content_type
            if correlation_data is not None:
                self._values["correlation_data"] = correlation_data
            if message_expiry is not None:
                self._values["message_expiry"] = message_expiry
            if payload_format_indicator is not None:
                self._values["payload_format_indicator"] = payload_format_indicator
            if response_topic is not None:
                self._values["response_topic"] = response_topic
            if user_properties is not None:
                self._values["user_properties"] = user_properties

        @builtins.property
        def content_type(self) -> typing.Optional[builtins.str]:
            '''A UTF-8 encoded string that describes the content of the publishing message.

            For more information, see `Content Type <https://docs.aws.amazon.com/https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html#_Toc3901118>`_ in the MQTT Version 5.0 specification.

            Supports `substitution templates <https://docs.aws.amazon.com//iot/latest/developerguide/iot-substitution-templates.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-republishactionheaders.html#cfn-iot-topicrule-republishactionheaders-contenttype
            '''
            result = self._values.get("content_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def correlation_data(self) -> typing.Optional[builtins.str]:
            '''The base64-encoded binary data used by the sender of the request message to identify which request the response message is for.

            For more information, see `Correlation Data <https://docs.aws.amazon.com/https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html#_Toc3901115>`_ in the MQTT Version 5.0 specification.

            Supports `substitution templates <https://docs.aws.amazon.com//iot/latest/developerguide/iot-substitution-templates.html>`_ .
            .. epigraph::

               This binary data must be base64-encoded.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-republishactionheaders.html#cfn-iot-topicrule-republishactionheaders-correlationdata
            '''
            result = self._values.get("correlation_data")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def message_expiry(self) -> typing.Optional[builtins.str]:
            '''A user-defined integer value that represents the message expiry interval at the broker.

            If the messages haven't been sent to the subscribers within that interval, the message expires and is removed. The value of ``messageExpiry`` represents the number of seconds before it expires. For more information about the limits of ``messageExpiry`` , see `Message broker and protocol limits and quotas <https://docs.aws.amazon.com//general/latest/gr/iot-core.html#limits_iot>`_ in the IoT Core Reference Guide.

            Supports `substitution templates <https://docs.aws.amazon.com//iot/latest/developerguide/iot-substitution-templates.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-republishactionheaders.html#cfn-iot-topicrule-republishactionheaders-messageexpiry
            '''
            result = self._values.get("message_expiry")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def payload_format_indicator(self) -> typing.Optional[builtins.str]:
            '''An ``Enum`` string value that indicates whether the payload is formatted as UTF-8.

            Valid values are ``UNSPECIFIED_BYTES`` and ``UTF8_DATA`` .

            For more information, see `Payload Format Indicator <https://docs.aws.amazon.com/https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html#_Toc3901111>`_ from the MQTT Version 5.0 specification.

            Supports `substitution templates <https://docs.aws.amazon.com//iot/latest/developerguide/iot-substitution-templates.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-republishactionheaders.html#cfn-iot-topicrule-republishactionheaders-payloadformatindicator
            '''
            result = self._values.get("payload_format_indicator")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def response_topic(self) -> typing.Optional[builtins.str]:
            '''A UTF-8 encoded string that's used as the topic name for a response message.

            The response topic is used to describe the topic to which the receiver should publish as part of the request-response flow. The topic must not contain wildcard characters.

            For more information, see `Response Topic <https://docs.aws.amazon.com/https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html#_Toc3901114>`_ in the MQTT Version 5.0 specification.

            Supports `substitution templates <https://docs.aws.amazon.com//iot/latest/developerguide/iot-substitution-templates.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-republishactionheaders.html#cfn-iot-topicrule-republishactionheaders-responsetopic
            '''
            result = self._values.get("response_topic")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def user_properties(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTopicRule.UserPropertyProperty", _IResolvable_a771d0ef]]]]:
            '''An array of key-value pairs that you define in the MQTT5 header.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-republishactionheaders.html#cfn-iot-topicrule-republishactionheaders-userproperties
            '''
            result = self._values.get("user_properties")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTopicRule.UserPropertyProperty", _IResolvable_a771d0ef]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RepublishActionHeadersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnTopicRule.RepublishActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "role_arn": "roleArn",
            "topic": "topic",
            "headers": "headers",
            "qos": "qos",
        },
    )
    class RepublishActionProperty:
        def __init__(
            self,
            *,
            role_arn: builtins.str,
            topic: builtins.str,
            headers: typing.Optional[typing.Union[typing.Union["CfnTopicRule.RepublishActionHeadersProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            qos: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Describes an action to republish to another topic.

            :param role_arn: The ARN of the IAM role that grants access.
            :param topic: The name of the MQTT topic.
            :param headers: MQTT Version 5.0 headers information. For more information, see `MQTT <https://docs.aws.amazon.com//iot/latest/developerguide/mqtt.html>`_ in the IoT Core Developer Guide.
            :param qos: The Quality of Service (QoS) level to use when republishing messages. The default value is 0.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-republishaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                republish_action_property = iot.CfnTopicRule.RepublishActionProperty(
                    role_arn="roleArn",
                    topic="topic",
                
                    # the properties below are optional
                    headers=iot.CfnTopicRule.RepublishActionHeadersProperty(
                        content_type="contentType",
                        correlation_data="correlationData",
                        message_expiry="messageExpiry",
                        payload_format_indicator="payloadFormatIndicator",
                        response_topic="responseTopic",
                        user_properties=[iot.CfnTopicRule.UserPropertyProperty(
                            key="key",
                            value="value"
                        )]
                    ),
                    qos=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2e064278f65540044d20c4fd2755bb7eaba09b540c20dd6cee0ec29b0ab48b66)
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
                check_type(argname="argument headers", value=headers, expected_type=type_hints["headers"])
                check_type(argname="argument qos", value=qos, expected_type=type_hints["qos"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "role_arn": role_arn,
                "topic": topic,
            }
            if headers is not None:
                self._values["headers"] = headers
            if qos is not None:
                self._values["qos"] = qos

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the IAM role that grants access.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-republishaction.html#cfn-iot-topicrule-republishaction-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def topic(self) -> builtins.str:
            '''The name of the MQTT topic.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-republishaction.html#cfn-iot-topicrule-republishaction-topic
            '''
            result = self._values.get("topic")
            assert result is not None, "Required property 'topic' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def headers(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.RepublishActionHeadersProperty", _IResolvable_a771d0ef]]:
            '''MQTT Version 5.0 headers information. For more information, see `MQTT <https://docs.aws.amazon.com//iot/latest/developerguide/mqtt.html>`_ in the IoT Core Developer Guide.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-republishaction.html#cfn-iot-topicrule-republishaction-headers
            '''
            result = self._values.get("headers")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.RepublishActionHeadersProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def qos(self) -> typing.Optional[jsii.Number]:
            '''The Quality of Service (QoS) level to use when republishing messages.

            The default value is 0.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-republishaction.html#cfn-iot-topicrule-republishaction-qos
            '''
            result = self._values.get("qos")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RepublishActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnTopicRule.S3ActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket_name": "bucketName",
            "key": "key",
            "role_arn": "roleArn",
            "canned_acl": "cannedAcl",
        },
    )
    class S3ActionProperty:
        def __init__(
            self,
            *,
            bucket_name: builtins.str,
            key: builtins.str,
            role_arn: builtins.str,
            canned_acl: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes an action to write data to an Amazon S3 bucket.

            :param bucket_name: The Amazon S3 bucket.
            :param key: The object key. For more information, see `Actions, resources, and condition keys for Amazon S3 <https://docs.aws.amazon.com/AmazonS3/latest/dev/list_amazons3.html>`_ .
            :param role_arn: The ARN of the IAM role that grants access.
            :param canned_acl: The Amazon S3 canned ACL that controls access to the object identified by the object key. For more information, see `S3 canned ACLs <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-s3action.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                s3_action_property = iot.CfnTopicRule.S3ActionProperty(
                    bucket_name="bucketName",
                    key="key",
                    role_arn="roleArn",
                
                    # the properties below are optional
                    canned_acl="cannedAcl"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__15a487dbc8102d292467a082644bd2cad01a57e1882aa96e161feef83e534360)
                check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument canned_acl", value=canned_acl, expected_type=type_hints["canned_acl"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket_name": bucket_name,
                "key": key,
                "role_arn": role_arn,
            }
            if canned_acl is not None:
                self._values["canned_acl"] = canned_acl

        @builtins.property
        def bucket_name(self) -> builtins.str:
            '''The Amazon S3 bucket.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-s3action.html#cfn-iot-topicrule-s3action-bucketname
            '''
            result = self._values.get("bucket_name")
            assert result is not None, "Required property 'bucket_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key(self) -> builtins.str:
            '''The object key.

            For more information, see `Actions, resources, and condition keys for Amazon S3 <https://docs.aws.amazon.com/AmazonS3/latest/dev/list_amazons3.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-s3action.html#cfn-iot-topicrule-s3action-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the IAM role that grants access.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-s3action.html#cfn-iot-topicrule-s3action-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def canned_acl(self) -> typing.Optional[builtins.str]:
            '''The Amazon S3 canned ACL that controls access to the object identified by the object key.

            For more information, see `S3 canned ACLs <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-s3action.html#cfn-iot-topicrule-s3action-cannedacl
            '''
            result = self._values.get("canned_acl")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3ActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnTopicRule.SigV4AuthorizationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "role_arn": "roleArn",
            "service_name": "serviceName",
            "signing_region": "signingRegion",
        },
    )
    class SigV4AuthorizationProperty:
        def __init__(
            self,
            *,
            role_arn: builtins.str,
            service_name: builtins.str,
            signing_region: builtins.str,
        ) -> None:
            '''For more information, see `Signature Version 4 signing process <https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html>`_ .

            :param role_arn: The ARN of the signing role.
            :param service_name: The service name to use while signing with Sig V4.
            :param signing_region: The signing region.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-sigv4authorization.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                sig_v4_authorization_property = iot.CfnTopicRule.SigV4AuthorizationProperty(
                    role_arn="roleArn",
                    service_name="serviceName",
                    signing_region="signingRegion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__06f8ca969f034928394d72825d8b8a6862353576d257b9fd1fe8da367be79d1f)
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
                check_type(argname="argument signing_region", value=signing_region, expected_type=type_hints["signing_region"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "role_arn": role_arn,
                "service_name": service_name,
                "signing_region": signing_region,
            }

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the signing role.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-sigv4authorization.html#cfn-iot-topicrule-sigv4authorization-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def service_name(self) -> builtins.str:
            '''The service name to use while signing with Sig V4.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-sigv4authorization.html#cfn-iot-topicrule-sigv4authorization-servicename
            '''
            result = self._values.get("service_name")
            assert result is not None, "Required property 'service_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def signing_region(self) -> builtins.str:
            '''The signing region.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-sigv4authorization.html#cfn-iot-topicrule-sigv4authorization-signingregion
            '''
            result = self._values.get("signing_region")
            assert result is not None, "Required property 'signing_region' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SigV4AuthorizationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnTopicRule.SnsActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "role_arn": "roleArn",
            "target_arn": "targetArn",
            "message_format": "messageFormat",
        },
    )
    class SnsActionProperty:
        def __init__(
            self,
            *,
            role_arn: builtins.str,
            target_arn: builtins.str,
            message_format: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes an action to publish to an Amazon SNS topic.

            :param role_arn: The ARN of the IAM role that grants access.
            :param target_arn: The ARN of the SNS topic.
            :param message_format: (Optional) The message format of the message to publish. Accepted values are "JSON" and "RAW". The default value of the attribute is "RAW". SNS uses this setting to determine if the payload should be parsed and relevant platform-specific bits of the payload should be extracted. For more information, see `Amazon SNS Message and JSON Formats <https://docs.aws.amazon.com/sns/latest/dg/json-formats.html>`_ in the *Amazon Simple Notification Service Developer Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-snsaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                sns_action_property = iot.CfnTopicRule.SnsActionProperty(
                    role_arn="roleArn",
                    target_arn="targetArn",
                
                    # the properties below are optional
                    message_format="messageFormat"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3666ce516fcd9093adfa8ddb1bbbab5817f9d177e357f95c9999aa74775607bd)
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument target_arn", value=target_arn, expected_type=type_hints["target_arn"])
                check_type(argname="argument message_format", value=message_format, expected_type=type_hints["message_format"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "role_arn": role_arn,
                "target_arn": target_arn,
            }
            if message_format is not None:
                self._values["message_format"] = message_format

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the IAM role that grants access.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-snsaction.html#cfn-iot-topicrule-snsaction-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def target_arn(self) -> builtins.str:
            '''The ARN of the SNS topic.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-snsaction.html#cfn-iot-topicrule-snsaction-targetarn
            '''
            result = self._values.get("target_arn")
            assert result is not None, "Required property 'target_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def message_format(self) -> typing.Optional[builtins.str]:
            '''(Optional) The message format of the message to publish.

            Accepted values are "JSON" and "RAW". The default value of the attribute is "RAW". SNS uses this setting to determine if the payload should be parsed and relevant platform-specific bits of the payload should be extracted. For more information, see `Amazon SNS Message and JSON Formats <https://docs.aws.amazon.com/sns/latest/dg/json-formats.html>`_ in the *Amazon Simple Notification Service Developer Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-snsaction.html#cfn-iot-topicrule-snsaction-messageformat
            '''
            result = self._values.get("message_format")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SnsActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnTopicRule.SqsActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "queue_url": "queueUrl",
            "role_arn": "roleArn",
            "use_base64": "useBase64",
        },
    )
    class SqsActionProperty:
        def __init__(
            self,
            *,
            queue_url: builtins.str,
            role_arn: builtins.str,
            use_base64: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''Describes an action to publish data to an Amazon SQS queue.

            :param queue_url: The URL of the Amazon SQS queue.
            :param role_arn: The ARN of the IAM role that grants access.
            :param use_base64: Specifies whether to use Base64 encoding.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-sqsaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                sqs_action_property = iot.CfnTopicRule.SqsActionProperty(
                    queue_url="queueUrl",
                    role_arn="roleArn",
                
                    # the properties below are optional
                    use_base64=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7d0bdd7a3c868cbcfd49e69c4c54828c76ad353bf40ebcf49ab1db3cb1de071a)
                check_type(argname="argument queue_url", value=queue_url, expected_type=type_hints["queue_url"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument use_base64", value=use_base64, expected_type=type_hints["use_base64"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "queue_url": queue_url,
                "role_arn": role_arn,
            }
            if use_base64 is not None:
                self._values["use_base64"] = use_base64

        @builtins.property
        def queue_url(self) -> builtins.str:
            '''The URL of the Amazon SQS queue.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-sqsaction.html#cfn-iot-topicrule-sqsaction-queueurl
            '''
            result = self._values.get("queue_url")
            assert result is not None, "Required property 'queue_url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the IAM role that grants access.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-sqsaction.html#cfn-iot-topicrule-sqsaction-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def use_base64(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Specifies whether to use Base64 encoding.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-sqsaction.html#cfn-iot-topicrule-sqsaction-usebase64
            '''
            result = self._values.get("use_base64")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SqsActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnTopicRule.StepFunctionsActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "role_arn": "roleArn",
            "state_machine_name": "stateMachineName",
            "execution_name_prefix": "executionNamePrefix",
        },
    )
    class StepFunctionsActionProperty:
        def __init__(
            self,
            *,
            role_arn: builtins.str,
            state_machine_name: builtins.str,
            execution_name_prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Starts execution of a Step Functions state machine.

            :param role_arn: The ARN of the role that grants IoT permission to start execution of a state machine ("Action":"states:StartExecution").
            :param state_machine_name: The name of the Step Functions state machine whose execution will be started.
            :param execution_name_prefix: (Optional) A name will be given to the state machine execution consisting of this prefix followed by a UUID. Step Functions automatically creates a unique name for each state machine execution if one is not provided.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-stepfunctionsaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                step_functions_action_property = iot.CfnTopicRule.StepFunctionsActionProperty(
                    role_arn="roleArn",
                    state_machine_name="stateMachineName",
                
                    # the properties below are optional
                    execution_name_prefix="executionNamePrefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2301c2177af5e7eb8bf56c1a0a964dfbc212bc2095e214260f18bbf749d63886)
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument state_machine_name", value=state_machine_name, expected_type=type_hints["state_machine_name"])
                check_type(argname="argument execution_name_prefix", value=execution_name_prefix, expected_type=type_hints["execution_name_prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "role_arn": role_arn,
                "state_machine_name": state_machine_name,
            }
            if execution_name_prefix is not None:
                self._values["execution_name_prefix"] = execution_name_prefix

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the role that grants IoT permission to start execution of a state machine ("Action":"states:StartExecution").

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-stepfunctionsaction.html#cfn-iot-topicrule-stepfunctionsaction-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def state_machine_name(self) -> builtins.str:
            '''The name of the Step Functions state machine whose execution will be started.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-stepfunctionsaction.html#cfn-iot-topicrule-stepfunctionsaction-statemachinename
            '''
            result = self._values.get("state_machine_name")
            assert result is not None, "Required property 'state_machine_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def execution_name_prefix(self) -> typing.Optional[builtins.str]:
            '''(Optional) A name will be given to the state machine execution consisting of this prefix followed by a UUID.

            Step Functions automatically creates a unique name for each state machine execution if one is not provided.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-stepfunctionsaction.html#cfn-iot-topicrule-stepfunctionsaction-executionnameprefix
            '''
            result = self._values.get("execution_name_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StepFunctionsActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnTopicRule.TimestampProperty",
        jsii_struct_bases=[],
        name_mapping={"value": "value", "unit": "unit"},
    )
    class TimestampProperty:
        def __init__(
            self,
            *,
            value: builtins.str,
            unit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes how to interpret an application-defined timestamp value from an MQTT message payload and the precision of that value.

            :param value: An expression that returns a long epoch time value.
            :param unit: The precision of the timestamp value that results from the expression described in ``value`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestamp.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                timestamp_property = iot.CfnTopicRule.TimestampProperty(
                    value="value",
                
                    # the properties below are optional
                    unit="unit"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ed3994d04f9eba52d292f3a3d33320b3b00a9f9fc772c0a3d07b7afbf79abd25)
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
                check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "value": value,
            }
            if unit is not None:
                self._values["unit"] = unit

        @builtins.property
        def value(self) -> builtins.str:
            '''An expression that returns a long epoch time value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestamp.html#cfn-iot-topicrule-timestamp-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def unit(self) -> typing.Optional[builtins.str]:
            '''The precision of the timestamp value that results from the expression described in ``value`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestamp.html#cfn-iot-topicrule-timestamp-unit
            '''
            result = self._values.get("unit")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TimestampProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnTopicRule.TimestreamActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "database_name": "databaseName",
            "dimensions": "dimensions",
            "role_arn": "roleArn",
            "table_name": "tableName",
            "timestamp": "timestamp",
        },
    )
    class TimestreamActionProperty:
        def __init__(
            self,
            *,
            database_name: builtins.str,
            dimensions: typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union["CfnTopicRule.TimestreamDimensionProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]],
            role_arn: builtins.str,
            table_name: builtins.str,
            timestamp: typing.Optional[typing.Union[typing.Union["CfnTopicRule.TimestreamTimestampProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''Describes an action that writes records into an Amazon Timestream table.

            :param database_name: The name of an Amazon Timestream database that has the table to write records into.
            :param dimensions: Metadata attributes of the time series that are written in each measure record.
            :param role_arn: The Amazon Resource Name (ARN) of the role that grants AWS IoT permission to write to the Timestream database table.
            :param table_name: The table where the message data will be written.
            :param timestamp: The value to use for the entry's timestamp. If blank, the time that the entry was processed is used.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                timestream_action_property = iot.CfnTopicRule.TimestreamActionProperty(
                    database_name="databaseName",
                    dimensions=[iot.CfnTopicRule.TimestreamDimensionProperty(
                        name="name",
                        value="value"
                    )],
                    role_arn="roleArn",
                    table_name="tableName",
                
                    # the properties below are optional
                    timestamp=iot.CfnTopicRule.TimestreamTimestampProperty(
                        unit="unit",
                        value="value"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2e584d87e7884bc9c63e8d8adf4f753e42a05b87e545f3ede17207a61245124a)
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument dimensions", value=dimensions, expected_type=type_hints["dimensions"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
                check_type(argname="argument timestamp", value=timestamp, expected_type=type_hints["timestamp"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "database_name": database_name,
                "dimensions": dimensions,
                "role_arn": role_arn,
                "table_name": table_name,
            }
            if timestamp is not None:
                self._values["timestamp"] = timestamp

        @builtins.property
        def database_name(self) -> builtins.str:
            '''The name of an Amazon Timestream database that has the table to write records into.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamaction.html#cfn-iot-topicrule-timestreamaction-databasename
            '''
            result = self._values.get("database_name")
            assert result is not None, "Required property 'database_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def dimensions(
            self,
        ) -> typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTopicRule.TimestreamDimensionProperty", _IResolvable_a771d0ef]]]:
            '''Metadata attributes of the time series that are written in each measure record.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamaction.html#cfn-iot-topicrule-timestreamaction-dimensions
            '''
            result = self._values.get("dimensions")
            assert result is not None, "Required property 'dimensions' is missing"
            return typing.cast(typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTopicRule.TimestreamDimensionProperty", _IResolvable_a771d0ef]]], result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the role that grants AWS IoT permission to write to the Timestream database table.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamaction.html#cfn-iot-topicrule-timestreamaction-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def table_name(self) -> builtins.str:
            '''The table where the message data will be written.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamaction.html#cfn-iot-topicrule-timestreamaction-tablename
            '''
            result = self._values.get("table_name")
            assert result is not None, "Required property 'table_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def timestamp(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.TimestreamTimestampProperty", _IResolvable_a771d0ef]]:
            '''The value to use for the entry's timestamp.

            If blank, the time that the entry was processed is used.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamaction.html#cfn-iot-topicrule-timestreamaction-timestamp
            '''
            result = self._values.get("timestamp")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.TimestreamTimestampProperty", _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TimestreamActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnTopicRule.TimestreamDimensionProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class TimestreamDimensionProperty:
        def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
            '''Metadata attributes of the time series that are written in each measure record.

            :param name: The metadata dimension name. This is the name of the column in the Amazon Timestream database table record.
            :param value: The value to write in this column of the database record.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamdimension.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                timestream_dimension_property = iot.CfnTopicRule.TimestreamDimensionProperty(
                    name="name",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__91a2bfa87f2b240294575893bf17aa3d805ccea7c95b05b5dc0da866c046c55e)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "value": value,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The metadata dimension name.

            This is the name of the column in the Amazon Timestream database table record.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamdimension.html#cfn-iot-topicrule-timestreamdimension-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The value to write in this column of the database record.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamdimension.html#cfn-iot-topicrule-timestreamdimension-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TimestreamDimensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnTopicRule.TimestreamTimestampProperty",
        jsii_struct_bases=[],
        name_mapping={"unit": "unit", "value": "value"},
    )
    class TimestreamTimestampProperty:
        def __init__(self, *, unit: builtins.str, value: builtins.str) -> None:
            '''The value to use for the entry's timestamp.

            If blank, the time that the entry was processed is used.

            :param unit: The precision of the timestamp value that results from the expression described in ``value`` .
            :param value: An expression that returns a long epoch time value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamtimestamp.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                timestream_timestamp_property = iot.CfnTopicRule.TimestreamTimestampProperty(
                    unit="unit",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a1d4e9ad3bc192f1845a6974505d3611853ac94cc6f64175b7f15fa79000c9c8)
                check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "unit": unit,
                "value": value,
            }

        @builtins.property
        def unit(self) -> builtins.str:
            '''The precision of the timestamp value that results from the expression described in ``value`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamtimestamp.html#cfn-iot-topicrule-timestreamtimestamp-unit
            '''
            result = self._values.get("unit")
            assert result is not None, "Required property 'unit' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''An expression that returns a long epoch time value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-timestreamtimestamp.html#cfn-iot-topicrule-timestreamtimestamp-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TimestreamTimestampProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnTopicRule.TopicRulePayloadProperty",
        jsii_struct_bases=[],
        name_mapping={
            "actions": "actions",
            "sql": "sql",
            "aws_iot_sql_version": "awsIotSqlVersion",
            "description": "description",
            "error_action": "errorAction",
            "rule_disabled": "ruleDisabled",
        },
    )
    class TopicRulePayloadProperty:
        def __init__(
            self,
            *,
            actions: typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union["CfnTopicRule.ActionProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]],
            sql: builtins.str,
            aws_iot_sql_version: typing.Optional[builtins.str] = None,
            description: typing.Optional[builtins.str] = None,
            error_action: typing.Optional[typing.Union[typing.Union["CfnTopicRule.ActionProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            rule_disabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''Describes a rule.

            :param actions: The actions associated with the rule.
            :param sql: The SQL statement used to query the topic. For more information, see `AWS IoT SQL Reference <https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-reference.html>`_ in the *AWS IoT Developer Guide* .
            :param aws_iot_sql_version: The version of the SQL rules engine to use when evaluating the rule. The default value is 2015-10-08.
            :param description: The description of the rule.
            :param error_action: The action to take when an error occurs.
            :param rule_disabled: Specifies whether the rule is disabled.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-topicrulepayload.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                topic_rule_payload_property = iot.CfnTopicRule.TopicRulePayloadProperty(
                    actions=[iot.CfnTopicRule.ActionProperty(
                        cloudwatch_alarm=iot.CfnTopicRule.CloudwatchAlarmActionProperty(
                            alarm_name="alarmName",
                            role_arn="roleArn",
                            state_reason="stateReason",
                            state_value="stateValue"
                        ),
                        cloudwatch_logs=iot.CfnTopicRule.CloudwatchLogsActionProperty(
                            log_group_name="logGroupName",
                            role_arn="roleArn"
                        ),
                        cloudwatch_metric=iot.CfnTopicRule.CloudwatchMetricActionProperty(
                            metric_name="metricName",
                            metric_namespace="metricNamespace",
                            metric_unit="metricUnit",
                            metric_value="metricValue",
                            role_arn="roleArn",
                
                            # the properties below are optional
                            metric_timestamp="metricTimestamp"
                        ),
                        dynamo_db=iot.CfnTopicRule.DynamoDBActionProperty(
                            hash_key_field="hashKeyField",
                            hash_key_value="hashKeyValue",
                            role_arn="roleArn",
                            table_name="tableName",
                
                            # the properties below are optional
                            hash_key_type="hashKeyType",
                            payload_field="payloadField",
                            range_key_field="rangeKeyField",
                            range_key_type="rangeKeyType",
                            range_key_value="rangeKeyValue"
                        ),
                        dynamo_dBv2=iot.CfnTopicRule.DynamoDBv2ActionProperty(
                            put_item=iot.CfnTopicRule.PutItemInputProperty(
                                table_name="tableName"
                            ),
                            role_arn="roleArn"
                        ),
                        elasticsearch=iot.CfnTopicRule.ElasticsearchActionProperty(
                            endpoint="endpoint",
                            id="id",
                            index="index",
                            role_arn="roleArn",
                            type="type"
                        ),
                        firehose=iot.CfnTopicRule.FirehoseActionProperty(
                            delivery_stream_name="deliveryStreamName",
                            role_arn="roleArn",
                
                            # the properties below are optional
                            batch_mode=False,
                            separator="separator"
                        ),
                        http=iot.CfnTopicRule.HttpActionProperty(
                            url="url",
                
                            # the properties below are optional
                            auth=iot.CfnTopicRule.HttpAuthorizationProperty(
                                sigv4=iot.CfnTopicRule.SigV4AuthorizationProperty(
                                    role_arn="roleArn",
                                    service_name="serviceName",
                                    signing_region="signingRegion"
                                )
                            ),
                            confirmation_url="confirmationUrl",
                            headers=[iot.CfnTopicRule.HttpActionHeaderProperty(
                                key="key",
                                value="value"
                            )]
                        ),
                        iot_analytics=iot.CfnTopicRule.IotAnalyticsActionProperty(
                            channel_name="channelName",
                            role_arn="roleArn",
                
                            # the properties below are optional
                            batch_mode=False
                        ),
                        iot_events=iot.CfnTopicRule.IotEventsActionProperty(
                            input_name="inputName",
                            role_arn="roleArn",
                
                            # the properties below are optional
                            batch_mode=False,
                            message_id="messageId"
                        ),
                        iot_site_wise=iot.CfnTopicRule.IotSiteWiseActionProperty(
                            put_asset_property_value_entries=[iot.CfnTopicRule.PutAssetPropertyValueEntryProperty(
                                property_values=[iot.CfnTopicRule.AssetPropertyValueProperty(
                                    timestamp=iot.CfnTopicRule.AssetPropertyTimestampProperty(
                                        time_in_seconds="timeInSeconds",
                
                                        # the properties below are optional
                                        offset_in_nanos="offsetInNanos"
                                    ),
                                    value=iot.CfnTopicRule.AssetPropertyVariantProperty(
                                        boolean_value="booleanValue",
                                        double_value="doubleValue",
                                        integer_value="integerValue",
                                        string_value="stringValue"
                                    ),
                
                                    # the properties below are optional
                                    quality="quality"
                                )],
                
                                # the properties below are optional
                                asset_id="assetId",
                                entry_id="entryId",
                                property_alias="propertyAlias",
                                property_id="propertyId"
                            )],
                            role_arn="roleArn"
                        ),
                        kafka=iot.CfnTopicRule.KafkaActionProperty(
                            client_properties={
                                "client_properties_key": "clientProperties"
                            },
                            destination_arn="destinationArn",
                            topic="topic",
                
                            # the properties below are optional
                            key="key",
                            partition="partition"
                        ),
                        kinesis=iot.CfnTopicRule.KinesisActionProperty(
                            role_arn="roleArn",
                            stream_name="streamName",
                
                            # the properties below are optional
                            partition_key="partitionKey"
                        ),
                        lambda_=iot.CfnTopicRule.LambdaActionProperty(
                            function_arn="functionArn"
                        ),
                        location=iot.CfnTopicRule.LocationActionProperty(
                            device_id="deviceId",
                            latitude="latitude",
                            longitude="longitude",
                            role_arn="roleArn",
                            tracker_name="trackerName",
                
                            # the properties below are optional
                            timestamp=Date()
                        ),
                        open_search=iot.CfnTopicRule.OpenSearchActionProperty(
                            endpoint="endpoint",
                            id="id",
                            index="index",
                            role_arn="roleArn",
                            type="type"
                        ),
                        republish=iot.CfnTopicRule.RepublishActionProperty(
                            role_arn="roleArn",
                            topic="topic",
                
                            # the properties below are optional
                            headers=iot.CfnTopicRule.RepublishActionHeadersProperty(
                                content_type="contentType",
                                correlation_data="correlationData",
                                message_expiry="messageExpiry",
                                payload_format_indicator="payloadFormatIndicator",
                                response_topic="responseTopic",
                                user_properties=[iot.CfnTopicRule.UserPropertyProperty(
                                    key="key",
                                    value="value"
                                )]
                            ),
                            qos=123
                        ),
                        s3=iot.CfnTopicRule.S3ActionProperty(
                            bucket_name="bucketName",
                            key="key",
                            role_arn="roleArn",
                
                            # the properties below are optional
                            canned_acl="cannedAcl"
                        ),
                        sns=iot.CfnTopicRule.SnsActionProperty(
                            role_arn="roleArn",
                            target_arn="targetArn",
                
                            # the properties below are optional
                            message_format="messageFormat"
                        ),
                        sqs=iot.CfnTopicRule.SqsActionProperty(
                            queue_url="queueUrl",
                            role_arn="roleArn",
                
                            # the properties below are optional
                            use_base64=False
                        ),
                        step_functions=iot.CfnTopicRule.StepFunctionsActionProperty(
                            role_arn="roleArn",
                            state_machine_name="stateMachineName",
                
                            # the properties below are optional
                            execution_name_prefix="executionNamePrefix"
                        ),
                        timestream=iot.CfnTopicRule.TimestreamActionProperty(
                            database_name="databaseName",
                            dimensions=[iot.CfnTopicRule.TimestreamDimensionProperty(
                                name="name",
                                value="value"
                            )],
                            role_arn="roleArn",
                            table_name="tableName",
                
                            # the properties below are optional
                            timestamp=iot.CfnTopicRule.TimestreamTimestampProperty(
                                unit="unit",
                                value="value"
                            )
                        )
                    )],
                    sql="sql",
                
                    # the properties below are optional
                    aws_iot_sql_version="awsIotSqlVersion",
                    description="description",
                    error_action=iot.CfnTopicRule.ActionProperty(
                        cloudwatch_alarm=iot.CfnTopicRule.CloudwatchAlarmActionProperty(
                            alarm_name="alarmName",
                            role_arn="roleArn",
                            state_reason="stateReason",
                            state_value="stateValue"
                        ),
                        cloudwatch_logs=iot.CfnTopicRule.CloudwatchLogsActionProperty(
                            log_group_name="logGroupName",
                            role_arn="roleArn"
                        ),
                        cloudwatch_metric=iot.CfnTopicRule.CloudwatchMetricActionProperty(
                            metric_name="metricName",
                            metric_namespace="metricNamespace",
                            metric_unit="metricUnit",
                            metric_value="metricValue",
                            role_arn="roleArn",
                
                            # the properties below are optional
                            metric_timestamp="metricTimestamp"
                        ),
                        dynamo_db=iot.CfnTopicRule.DynamoDBActionProperty(
                            hash_key_field="hashKeyField",
                            hash_key_value="hashKeyValue",
                            role_arn="roleArn",
                            table_name="tableName",
                
                            # the properties below are optional
                            hash_key_type="hashKeyType",
                            payload_field="payloadField",
                            range_key_field="rangeKeyField",
                            range_key_type="rangeKeyType",
                            range_key_value="rangeKeyValue"
                        ),
                        dynamo_dBv2=iot.CfnTopicRule.DynamoDBv2ActionProperty(
                            put_item=iot.CfnTopicRule.PutItemInputProperty(
                                table_name="tableName"
                            ),
                            role_arn="roleArn"
                        ),
                        elasticsearch=iot.CfnTopicRule.ElasticsearchActionProperty(
                            endpoint="endpoint",
                            id="id",
                            index="index",
                            role_arn="roleArn",
                            type="type"
                        ),
                        firehose=iot.CfnTopicRule.FirehoseActionProperty(
                            delivery_stream_name="deliveryStreamName",
                            role_arn="roleArn",
                
                            # the properties below are optional
                            batch_mode=False,
                            separator="separator"
                        ),
                        http=iot.CfnTopicRule.HttpActionProperty(
                            url="url",
                
                            # the properties below are optional
                            auth=iot.CfnTopicRule.HttpAuthorizationProperty(
                                sigv4=iot.CfnTopicRule.SigV4AuthorizationProperty(
                                    role_arn="roleArn",
                                    service_name="serviceName",
                                    signing_region="signingRegion"
                                )
                            ),
                            confirmation_url="confirmationUrl",
                            headers=[iot.CfnTopicRule.HttpActionHeaderProperty(
                                key="key",
                                value="value"
                            )]
                        ),
                        iot_analytics=iot.CfnTopicRule.IotAnalyticsActionProperty(
                            channel_name="channelName",
                            role_arn="roleArn",
                
                            # the properties below are optional
                            batch_mode=False
                        ),
                        iot_events=iot.CfnTopicRule.IotEventsActionProperty(
                            input_name="inputName",
                            role_arn="roleArn",
                
                            # the properties below are optional
                            batch_mode=False,
                            message_id="messageId"
                        ),
                        iot_site_wise=iot.CfnTopicRule.IotSiteWiseActionProperty(
                            put_asset_property_value_entries=[iot.CfnTopicRule.PutAssetPropertyValueEntryProperty(
                                property_values=[iot.CfnTopicRule.AssetPropertyValueProperty(
                                    timestamp=iot.CfnTopicRule.AssetPropertyTimestampProperty(
                                        time_in_seconds="timeInSeconds",
                
                                        # the properties below are optional
                                        offset_in_nanos="offsetInNanos"
                                    ),
                                    value=iot.CfnTopicRule.AssetPropertyVariantProperty(
                                        boolean_value="booleanValue",
                                        double_value="doubleValue",
                                        integer_value="integerValue",
                                        string_value="stringValue"
                                    ),
                
                                    # the properties below are optional
                                    quality="quality"
                                )],
                
                                # the properties below are optional
                                asset_id="assetId",
                                entry_id="entryId",
                                property_alias="propertyAlias",
                                property_id="propertyId"
                            )],
                            role_arn="roleArn"
                        ),
                        kafka=iot.CfnTopicRule.KafkaActionProperty(
                            client_properties={
                                "client_properties_key": "clientProperties"
                            },
                            destination_arn="destinationArn",
                            topic="topic",
                
                            # the properties below are optional
                            key="key",
                            partition="partition"
                        ),
                        kinesis=iot.CfnTopicRule.KinesisActionProperty(
                            role_arn="roleArn",
                            stream_name="streamName",
                
                            # the properties below are optional
                            partition_key="partitionKey"
                        ),
                        lambda_=iot.CfnTopicRule.LambdaActionProperty(
                            function_arn="functionArn"
                        ),
                        location=iot.CfnTopicRule.LocationActionProperty(
                            device_id="deviceId",
                            latitude="latitude",
                            longitude="longitude",
                            role_arn="roleArn",
                            tracker_name="trackerName",
                
                            # the properties below are optional
                            timestamp=Date()
                        ),
                        open_search=iot.CfnTopicRule.OpenSearchActionProperty(
                            endpoint="endpoint",
                            id="id",
                            index="index",
                            role_arn="roleArn",
                            type="type"
                        ),
                        republish=iot.CfnTopicRule.RepublishActionProperty(
                            role_arn="roleArn",
                            topic="topic",
                
                            # the properties below are optional
                            headers=iot.CfnTopicRule.RepublishActionHeadersProperty(
                                content_type="contentType",
                                correlation_data="correlationData",
                                message_expiry="messageExpiry",
                                payload_format_indicator="payloadFormatIndicator",
                                response_topic="responseTopic",
                                user_properties=[iot.CfnTopicRule.UserPropertyProperty(
                                    key="key",
                                    value="value"
                                )]
                            ),
                            qos=123
                        ),
                        s3=iot.CfnTopicRule.S3ActionProperty(
                            bucket_name="bucketName",
                            key="key",
                            role_arn="roleArn",
                
                            # the properties below are optional
                            canned_acl="cannedAcl"
                        ),
                        sns=iot.CfnTopicRule.SnsActionProperty(
                            role_arn="roleArn",
                            target_arn="targetArn",
                
                            # the properties below are optional
                            message_format="messageFormat"
                        ),
                        sqs=iot.CfnTopicRule.SqsActionProperty(
                            queue_url="queueUrl",
                            role_arn="roleArn",
                
                            # the properties below are optional
                            use_base64=False
                        ),
                        step_functions=iot.CfnTopicRule.StepFunctionsActionProperty(
                            role_arn="roleArn",
                            state_machine_name="stateMachineName",
                
                            # the properties below are optional
                            execution_name_prefix="executionNamePrefix"
                        ),
                        timestream=iot.CfnTopicRule.TimestreamActionProperty(
                            database_name="databaseName",
                            dimensions=[iot.CfnTopicRule.TimestreamDimensionProperty(
                                name="name",
                                value="value"
                            )],
                            role_arn="roleArn",
                            table_name="tableName",
                
                            # the properties below are optional
                            timestamp=iot.CfnTopicRule.TimestreamTimestampProperty(
                                unit="unit",
                                value="value"
                            )
                        )
                    ),
                    rule_disabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__81c1d417456e00c2a00cc1e1000ee721904e21e78d04148e1f18887da57f29d7)
                check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
                check_type(argname="argument sql", value=sql, expected_type=type_hints["sql"])
                check_type(argname="argument aws_iot_sql_version", value=aws_iot_sql_version, expected_type=type_hints["aws_iot_sql_version"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument error_action", value=error_action, expected_type=type_hints["error_action"])
                check_type(argname="argument rule_disabled", value=rule_disabled, expected_type=type_hints["rule_disabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "actions": actions,
                "sql": sql,
            }
            if aws_iot_sql_version is not None:
                self._values["aws_iot_sql_version"] = aws_iot_sql_version
            if description is not None:
                self._values["description"] = description
            if error_action is not None:
                self._values["error_action"] = error_action
            if rule_disabled is not None:
                self._values["rule_disabled"] = rule_disabled

        @builtins.property
        def actions(
            self,
        ) -> typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTopicRule.ActionProperty", _IResolvable_a771d0ef]]]:
            '''The actions associated with the rule.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-topicrulepayload.html#cfn-iot-topicrule-topicrulepayload-actions
            '''
            result = self._values.get("actions")
            assert result is not None, "Required property 'actions' is missing"
            return typing.cast(typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnTopicRule.ActionProperty", _IResolvable_a771d0ef]]], result)

        @builtins.property
        def sql(self) -> builtins.str:
            '''The SQL statement used to query the topic.

            For more information, see `AWS IoT SQL Reference <https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-reference.html>`_ in the *AWS IoT Developer Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-topicrulepayload.html#cfn-iot-topicrule-topicrulepayload-sql
            '''
            result = self._values.get("sql")
            assert result is not None, "Required property 'sql' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def aws_iot_sql_version(self) -> typing.Optional[builtins.str]:
            '''The version of the SQL rules engine to use when evaluating the rule.

            The default value is 2015-10-08.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-topicrulepayload.html#cfn-iot-topicrule-topicrulepayload-awsiotsqlversion
            '''
            result = self._values.get("aws_iot_sql_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The description of the rule.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-topicrulepayload.html#cfn-iot-topicrule-topicrulepayload-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def error_action(
            self,
        ) -> typing.Optional[typing.Union["CfnTopicRule.ActionProperty", _IResolvable_a771d0ef]]:
            '''The action to take when an error occurs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-topicrulepayload.html#cfn-iot-topicrule-topicrulepayload-erroraction
            '''
            result = self._values.get("error_action")
            return typing.cast(typing.Optional[typing.Union["CfnTopicRule.ActionProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def rule_disabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Specifies whether the rule is disabled.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-topicrulepayload.html#cfn-iot-topicrule-topicrulepayload-ruledisabled
            '''
            result = self._values.get("rule_disabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TopicRulePayloadProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnTopicRule.UserPropertyProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class UserPropertyProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''A key-value pair that you define in the header.

            :param key: A key to be specified in ``UserProperty`` .
            :param value: A value to be specified in ``UserProperty`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-userproperty.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                user_property_property = iot.CfnTopicRule.UserPropertyProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c7044584b09c908ca69d5398061943b6b496241675d44cbdf422c555763e3de3)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''A key to be specified in ``UserProperty`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-userproperty.html#cfn-iot-topicrule-userproperty-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''A value to be specified in ``UserProperty`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicrule-userproperty.html#cfn-iot-topicrule-userproperty-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UserPropertyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_82c04a63)
class CfnTopicRuleDestination(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iot.CfnTopicRuleDestination",
):
    '''A CloudFormation ``AWS::IoT::TopicRuleDestination``.

    A topic rule destination.

    :cloudformationResource: AWS::IoT::TopicRuleDestination
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicruledestination.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_iot as iot
        
        cfn_topic_rule_destination = iot.CfnTopicRuleDestination(self, "MyCfnTopicRuleDestination",
            http_url_properties=iot.CfnTopicRuleDestination.HttpUrlDestinationSummaryProperty(
                confirmation_url="confirmationUrl"
            ),
            status="status",
            vpc_properties=iot.CfnTopicRuleDestination.VpcDestinationPropertiesProperty(
                role_arn="roleArn",
                security_groups=["securityGroups"],
                subnet_ids=["subnetIds"],
                vpc_id="vpcId"
            )
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        http_url_properties: typing.Optional[typing.Union[typing.Union["CfnTopicRuleDestination.HttpUrlDestinationSummaryProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        status: typing.Optional[builtins.str] = None,
        vpc_properties: typing.Optional[typing.Union[typing.Union["CfnTopicRuleDestination.VpcDestinationPropertiesProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    ) -> None:
        '''Create a new ``AWS::IoT::TopicRuleDestination``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param http_url_properties: Properties of the HTTP URL.
        :param status: - **IN_PROGRESS** - A topic rule destination was created but has not been confirmed. You can set status to ``IN_PROGRESS`` by calling ``UpdateTopicRuleDestination`` . Calling ``UpdateTopicRuleDestination`` causes a new confirmation challenge to be sent to your confirmation endpoint. - **ENABLED** - Confirmation was completed, and traffic to this destination is allowed. You can set status to ``DISABLED`` by calling ``UpdateTopicRuleDestination`` . - **DISABLED** - Confirmation was completed, and traffic to this destination is not allowed. You can set status to ``ENABLED`` by calling ``UpdateTopicRuleDestination`` . - **ERROR** - Confirmation could not be completed; for example, if the confirmation timed out. You can call ``GetTopicRuleDestination`` for details about the error. You can set status to ``IN_PROGRESS`` by calling ``UpdateTopicRuleDestination`` . Calling ``UpdateTopicRuleDestination`` causes a new confirmation challenge to be sent to your confirmation endpoint.
        :param vpc_properties: Properties of the virtual private cloud (VPC) connection.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a89d7bdf9e78b54d5052730161337b384713df76d01cf480264c6790de25f9ea)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTopicRuleDestinationProps(
            http_url_properties=http_url_properties,
            status=status,
            vpc_properties=vpc_properties,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49028cbd79b31a1c1f8d1160a6d6afc41b0c5a1a3b24f0780806b6e25cb98532)
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
            type_hints = typing.get_type_hints(_typecheckingstub__472aae12c565c92d3d291369fffbd3d72084ac126081b860d9cff80afff0a222)
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
        '''The topic rule destination URL.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrStatusReason")
    def attr_status_reason(self) -> builtins.str:
        '''Additional details or reason why the topic rule destination is in the current status.

        :cloudformationAttribute: StatusReason
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatusReason"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="httpUrlProperties")
    def http_url_properties(
        self,
    ) -> typing.Optional[typing.Union["CfnTopicRuleDestination.HttpUrlDestinationSummaryProperty", _IResolvable_a771d0ef]]:
        '''Properties of the HTTP URL.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicruledestination.html#cfn-iot-topicruledestination-httpurlproperties
        '''
        return typing.cast(typing.Optional[typing.Union["CfnTopicRuleDestination.HttpUrlDestinationSummaryProperty", _IResolvable_a771d0ef]], jsii.get(self, "httpUrlProperties"))

    @http_url_properties.setter
    def http_url_properties(
        self,
        value: typing.Optional[typing.Union["CfnTopicRuleDestination.HttpUrlDestinationSummaryProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d2831eca5011fa45238a8550f9feb56ffa9bd2860b71dac4438d68745757980)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpUrlProperties", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''- **IN_PROGRESS** - A topic rule destination was created but has not been confirmed.

        You can set status to ``IN_PROGRESS`` by calling ``UpdateTopicRuleDestination`` . Calling ``UpdateTopicRuleDestination`` causes a new confirmation challenge to be sent to your confirmation endpoint.

        - **ENABLED** - Confirmation was completed, and traffic to this destination is allowed. You can set status to ``DISABLED`` by calling ``UpdateTopicRuleDestination`` .
        - **DISABLED** - Confirmation was completed, and traffic to this destination is not allowed. You can set status to ``ENABLED`` by calling ``UpdateTopicRuleDestination`` .
        - **ERROR** - Confirmation could not be completed; for example, if the confirmation timed out. You can call ``GetTopicRuleDestination`` for details about the error. You can set status to ``IN_PROGRESS`` by calling ``UpdateTopicRuleDestination`` . Calling ``UpdateTopicRuleDestination`` causes a new confirmation challenge to be sent to your confirmation endpoint.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicruledestination.html#cfn-iot-topicruledestination-status
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6c1cee44fa333ab24f9b08600a6d000e003f320453a441b5c06a3ad5036c466)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="vpcProperties")
    def vpc_properties(
        self,
    ) -> typing.Optional[typing.Union["CfnTopicRuleDestination.VpcDestinationPropertiesProperty", _IResolvable_a771d0ef]]:
        '''Properties of the virtual private cloud (VPC) connection.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicruledestination.html#cfn-iot-topicruledestination-vpcproperties
        '''
        return typing.cast(typing.Optional[typing.Union["CfnTopicRuleDestination.VpcDestinationPropertiesProperty", _IResolvable_a771d0ef]], jsii.get(self, "vpcProperties"))

    @vpc_properties.setter
    def vpc_properties(
        self,
        value: typing.Optional[typing.Union["CfnTopicRuleDestination.VpcDestinationPropertiesProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76259c8bc5a91a67fdfa66b8f1123cfaa50575f8121e35a75cf990270a6e2f04)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcProperties", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnTopicRuleDestination.HttpUrlDestinationSummaryProperty",
        jsii_struct_bases=[],
        name_mapping={"confirmation_url": "confirmationUrl"},
    )
    class HttpUrlDestinationSummaryProperty:
        def __init__(
            self,
            *,
            confirmation_url: typing.Optional[builtins.str] = None,
        ) -> None:
            '''HTTP URL destination properties.

            :param confirmation_url: The URL used to confirm the HTTP topic rule destination URL.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicruledestination-httpurldestinationsummary.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                http_url_destination_summary_property = iot.CfnTopicRuleDestination.HttpUrlDestinationSummaryProperty(
                    confirmation_url="confirmationUrl"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f07deaf20816db33dcac88fe2ff231f79a29e95e54c16d6ab60e84bee02029ce)
                check_type(argname="argument confirmation_url", value=confirmation_url, expected_type=type_hints["confirmation_url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if confirmation_url is not None:
                self._values["confirmation_url"] = confirmation_url

        @builtins.property
        def confirmation_url(self) -> typing.Optional[builtins.str]:
            '''The URL used to confirm the HTTP topic rule destination URL.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicruledestination-httpurldestinationsummary.html#cfn-iot-topicruledestination-httpurldestinationsummary-confirmationurl
            '''
            result = self._values.get("confirmation_url")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpUrlDestinationSummaryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_iot.CfnTopicRuleDestination.VpcDestinationPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "role_arn": "roleArn",
            "security_groups": "securityGroups",
            "subnet_ids": "subnetIds",
            "vpc_id": "vpcId",
        },
    )
    class VpcDestinationPropertiesProperty:
        def __init__(
            self,
            *,
            role_arn: typing.Optional[builtins.str] = None,
            security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
            subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            vpc_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The properties of a virtual private cloud (VPC) destination.

            :param role_arn: The ARN of a role that has permission to create and attach to elastic network interfaces (ENIs).
            :param security_groups: The security groups of the VPC destination.
            :param subnet_ids: The subnet IDs of the VPC destination.
            :param vpc_id: The ID of the VPC.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicruledestination-vpcdestinationproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_iot as iot
                
                vpc_destination_properties_property = iot.CfnTopicRuleDestination.VpcDestinationPropertiesProperty(
                    role_arn="roleArn",
                    security_groups=["securityGroups"],
                    subnet_ids=["subnetIds"],
                    vpc_id="vpcId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__28aa9f28bd1fef7e858705ebf6da6f102c1153e54fb5725da312213735d50ebb)
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
                check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
                check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if role_arn is not None:
                self._values["role_arn"] = role_arn
            if security_groups is not None:
                self._values["security_groups"] = security_groups
            if subnet_ids is not None:
                self._values["subnet_ids"] = subnet_ids
            if vpc_id is not None:
                self._values["vpc_id"] = vpc_id

        @builtins.property
        def role_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of a role that has permission to create and attach to elastic network interfaces (ENIs).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicruledestination-vpcdestinationproperties.html#cfn-iot-topicruledestination-vpcdestinationproperties-rolearn
            '''
            result = self._values.get("role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The security groups of the VPC destination.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicruledestination-vpcdestinationproperties.html#cfn-iot-topicruledestination-vpcdestinationproperties-securitygroups
            '''
            result = self._values.get("security_groups")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The subnet IDs of the VPC destination.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicruledestination-vpcdestinationproperties.html#cfn-iot-topicruledestination-vpcdestinationproperties-subnetids
            '''
            result = self._values.get("subnet_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def vpc_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the VPC.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot-topicruledestination-vpcdestinationproperties.html#cfn-iot-topicruledestination-vpcdestinationproperties-vpcid
            '''
            result = self._values.get("vpc_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcDestinationPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_iot.CfnTopicRuleDestinationProps",
    jsii_struct_bases=[],
    name_mapping={
        "http_url_properties": "httpUrlProperties",
        "status": "status",
        "vpc_properties": "vpcProperties",
    },
)
class CfnTopicRuleDestinationProps:
    def __init__(
        self,
        *,
        http_url_properties: typing.Optional[typing.Union[typing.Union[CfnTopicRuleDestination.HttpUrlDestinationSummaryProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        status: typing.Optional[builtins.str] = None,
        vpc_properties: typing.Optional[typing.Union[typing.Union[CfnTopicRuleDestination.VpcDestinationPropertiesProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    ) -> None:
        '''Properties for defining a ``CfnTopicRuleDestination``.

        :param http_url_properties: Properties of the HTTP URL.
        :param status: - **IN_PROGRESS** - A topic rule destination was created but has not been confirmed. You can set status to ``IN_PROGRESS`` by calling ``UpdateTopicRuleDestination`` . Calling ``UpdateTopicRuleDestination`` causes a new confirmation challenge to be sent to your confirmation endpoint. - **ENABLED** - Confirmation was completed, and traffic to this destination is allowed. You can set status to ``DISABLED`` by calling ``UpdateTopicRuleDestination`` . - **DISABLED** - Confirmation was completed, and traffic to this destination is not allowed. You can set status to ``ENABLED`` by calling ``UpdateTopicRuleDestination`` . - **ERROR** - Confirmation could not be completed; for example, if the confirmation timed out. You can call ``GetTopicRuleDestination`` for details about the error. You can set status to ``IN_PROGRESS`` by calling ``UpdateTopicRuleDestination`` . Calling ``UpdateTopicRuleDestination`` causes a new confirmation challenge to be sent to your confirmation endpoint.
        :param vpc_properties: Properties of the virtual private cloud (VPC) connection.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicruledestination.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_iot as iot
            
            cfn_topic_rule_destination_props = iot.CfnTopicRuleDestinationProps(
                http_url_properties=iot.CfnTopicRuleDestination.HttpUrlDestinationSummaryProperty(
                    confirmation_url="confirmationUrl"
                ),
                status="status",
                vpc_properties=iot.CfnTopicRuleDestination.VpcDestinationPropertiesProperty(
                    role_arn="roleArn",
                    security_groups=["securityGroups"],
                    subnet_ids=["subnetIds"],
                    vpc_id="vpcId"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb816759350a5c76754a0ccf63c48ce6c58d259ebc3598820b0df960c3cb4b8c)
            check_type(argname="argument http_url_properties", value=http_url_properties, expected_type=type_hints["http_url_properties"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument vpc_properties", value=vpc_properties, expected_type=type_hints["vpc_properties"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if http_url_properties is not None:
            self._values["http_url_properties"] = http_url_properties
        if status is not None:
            self._values["status"] = status
        if vpc_properties is not None:
            self._values["vpc_properties"] = vpc_properties

    @builtins.property
    def http_url_properties(
        self,
    ) -> typing.Optional[typing.Union[CfnTopicRuleDestination.HttpUrlDestinationSummaryProperty, _IResolvable_a771d0ef]]:
        '''Properties of the HTTP URL.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicruledestination.html#cfn-iot-topicruledestination-httpurlproperties
        '''
        result = self._values.get("http_url_properties")
        return typing.cast(typing.Optional[typing.Union[CfnTopicRuleDestination.HttpUrlDestinationSummaryProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''- **IN_PROGRESS** - A topic rule destination was created but has not been confirmed.

        You can set status to ``IN_PROGRESS`` by calling ``UpdateTopicRuleDestination`` . Calling ``UpdateTopicRuleDestination`` causes a new confirmation challenge to be sent to your confirmation endpoint.

        - **ENABLED** - Confirmation was completed, and traffic to this destination is allowed. You can set status to ``DISABLED`` by calling ``UpdateTopicRuleDestination`` .
        - **DISABLED** - Confirmation was completed, and traffic to this destination is not allowed. You can set status to ``ENABLED`` by calling ``UpdateTopicRuleDestination`` .
        - **ERROR** - Confirmation could not be completed; for example, if the confirmation timed out. You can call ``GetTopicRuleDestination`` for details about the error. You can set status to ``IN_PROGRESS`` by calling ``UpdateTopicRuleDestination`` . Calling ``UpdateTopicRuleDestination`` causes a new confirmation challenge to be sent to your confirmation endpoint.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicruledestination.html#cfn-iot-topicruledestination-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_properties(
        self,
    ) -> typing.Optional[typing.Union[CfnTopicRuleDestination.VpcDestinationPropertiesProperty, _IResolvable_a771d0ef]]:
        '''Properties of the virtual private cloud (VPC) connection.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicruledestination.html#cfn-iot-topicruledestination-vpcproperties
        '''
        result = self._values.get("vpc_properties")
        return typing.cast(typing.Optional[typing.Union[CfnTopicRuleDestination.VpcDestinationPropertiesProperty, _IResolvable_a771d0ef]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTopicRuleDestinationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_iot.CfnTopicRuleProps",
    jsii_struct_bases=[],
    name_mapping={
        "topic_rule_payload": "topicRulePayload",
        "rule_name": "ruleName",
        "tags": "tags",
    },
)
class CfnTopicRuleProps:
    def __init__(
        self,
        *,
        topic_rule_payload: typing.Union[typing.Union[CfnTopicRule.TopicRulePayloadProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
        rule_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnTopicRule``.

        :param topic_rule_payload: The rule payload.
        :param rule_name: The name of the rule.
        :param tags: Metadata which can be used to manage the topic rule. .. epigraph:: For URI Request parameters use format: ...key1=value1&key2=value2... For the CLI command-line parameter use format: --tags "key1=value1&key2=value2..." For the cli-input-json file use format: "tags": "key1=value1&key2=value2..."

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicrule.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_iot as iot
            
            cfn_topic_rule_props = iot.CfnTopicRuleProps(
                topic_rule_payload=iot.CfnTopicRule.TopicRulePayloadProperty(
                    actions=[iot.CfnTopicRule.ActionProperty(
                        cloudwatch_alarm=iot.CfnTopicRule.CloudwatchAlarmActionProperty(
                            alarm_name="alarmName",
                            role_arn="roleArn",
                            state_reason="stateReason",
                            state_value="stateValue"
                        ),
                        cloudwatch_logs=iot.CfnTopicRule.CloudwatchLogsActionProperty(
                            log_group_name="logGroupName",
                            role_arn="roleArn"
                        ),
                        cloudwatch_metric=iot.CfnTopicRule.CloudwatchMetricActionProperty(
                            metric_name="metricName",
                            metric_namespace="metricNamespace",
                            metric_unit="metricUnit",
                            metric_value="metricValue",
                            role_arn="roleArn",
            
                            # the properties below are optional
                            metric_timestamp="metricTimestamp"
                        ),
                        dynamo_db=iot.CfnTopicRule.DynamoDBActionProperty(
                            hash_key_field="hashKeyField",
                            hash_key_value="hashKeyValue",
                            role_arn="roleArn",
                            table_name="tableName",
            
                            # the properties below are optional
                            hash_key_type="hashKeyType",
                            payload_field="payloadField",
                            range_key_field="rangeKeyField",
                            range_key_type="rangeKeyType",
                            range_key_value="rangeKeyValue"
                        ),
                        dynamo_dBv2=iot.CfnTopicRule.DynamoDBv2ActionProperty(
                            put_item=iot.CfnTopicRule.PutItemInputProperty(
                                table_name="tableName"
                            ),
                            role_arn="roleArn"
                        ),
                        elasticsearch=iot.CfnTopicRule.ElasticsearchActionProperty(
                            endpoint="endpoint",
                            id="id",
                            index="index",
                            role_arn="roleArn",
                            type="type"
                        ),
                        firehose=iot.CfnTopicRule.FirehoseActionProperty(
                            delivery_stream_name="deliveryStreamName",
                            role_arn="roleArn",
            
                            # the properties below are optional
                            batch_mode=False,
                            separator="separator"
                        ),
                        http=iot.CfnTopicRule.HttpActionProperty(
                            url="url",
            
                            # the properties below are optional
                            auth=iot.CfnTopicRule.HttpAuthorizationProperty(
                                sigv4=iot.CfnTopicRule.SigV4AuthorizationProperty(
                                    role_arn="roleArn",
                                    service_name="serviceName",
                                    signing_region="signingRegion"
                                )
                            ),
                            confirmation_url="confirmationUrl",
                            headers=[iot.CfnTopicRule.HttpActionHeaderProperty(
                                key="key",
                                value="value"
                            )]
                        ),
                        iot_analytics=iot.CfnTopicRule.IotAnalyticsActionProperty(
                            channel_name="channelName",
                            role_arn="roleArn",
            
                            # the properties below are optional
                            batch_mode=False
                        ),
                        iot_events=iot.CfnTopicRule.IotEventsActionProperty(
                            input_name="inputName",
                            role_arn="roleArn",
            
                            # the properties below are optional
                            batch_mode=False,
                            message_id="messageId"
                        ),
                        iot_site_wise=iot.CfnTopicRule.IotSiteWiseActionProperty(
                            put_asset_property_value_entries=[iot.CfnTopicRule.PutAssetPropertyValueEntryProperty(
                                property_values=[iot.CfnTopicRule.AssetPropertyValueProperty(
                                    timestamp=iot.CfnTopicRule.AssetPropertyTimestampProperty(
                                        time_in_seconds="timeInSeconds",
            
                                        # the properties below are optional
                                        offset_in_nanos="offsetInNanos"
                                    ),
                                    value=iot.CfnTopicRule.AssetPropertyVariantProperty(
                                        boolean_value="booleanValue",
                                        double_value="doubleValue",
                                        integer_value="integerValue",
                                        string_value="stringValue"
                                    ),
            
                                    # the properties below are optional
                                    quality="quality"
                                )],
            
                                # the properties below are optional
                                asset_id="assetId",
                                entry_id="entryId",
                                property_alias="propertyAlias",
                                property_id="propertyId"
                            )],
                            role_arn="roleArn"
                        ),
                        kafka=iot.CfnTopicRule.KafkaActionProperty(
                            client_properties={
                                "client_properties_key": "clientProperties"
                            },
                            destination_arn="destinationArn",
                            topic="topic",
            
                            # the properties below are optional
                            key="key",
                            partition="partition"
                        ),
                        kinesis=iot.CfnTopicRule.KinesisActionProperty(
                            role_arn="roleArn",
                            stream_name="streamName",
            
                            # the properties below are optional
                            partition_key="partitionKey"
                        ),
                        lambda_=iot.CfnTopicRule.LambdaActionProperty(
                            function_arn="functionArn"
                        ),
                        location=iot.CfnTopicRule.LocationActionProperty(
                            device_id="deviceId",
                            latitude="latitude",
                            longitude="longitude",
                            role_arn="roleArn",
                            tracker_name="trackerName",
            
                            # the properties below are optional
                            timestamp=Date()
                        ),
                        open_search=iot.CfnTopicRule.OpenSearchActionProperty(
                            endpoint="endpoint",
                            id="id",
                            index="index",
                            role_arn="roleArn",
                            type="type"
                        ),
                        republish=iot.CfnTopicRule.RepublishActionProperty(
                            role_arn="roleArn",
                            topic="topic",
            
                            # the properties below are optional
                            headers=iot.CfnTopicRule.RepublishActionHeadersProperty(
                                content_type="contentType",
                                correlation_data="correlationData",
                                message_expiry="messageExpiry",
                                payload_format_indicator="payloadFormatIndicator",
                                response_topic="responseTopic",
                                user_properties=[iot.CfnTopicRule.UserPropertyProperty(
                                    key="key",
                                    value="value"
                                )]
                            ),
                            qos=123
                        ),
                        s3=iot.CfnTopicRule.S3ActionProperty(
                            bucket_name="bucketName",
                            key="key",
                            role_arn="roleArn",
            
                            # the properties below are optional
                            canned_acl="cannedAcl"
                        ),
                        sns=iot.CfnTopicRule.SnsActionProperty(
                            role_arn="roleArn",
                            target_arn="targetArn",
            
                            # the properties below are optional
                            message_format="messageFormat"
                        ),
                        sqs=iot.CfnTopicRule.SqsActionProperty(
                            queue_url="queueUrl",
                            role_arn="roleArn",
            
                            # the properties below are optional
                            use_base64=False
                        ),
                        step_functions=iot.CfnTopicRule.StepFunctionsActionProperty(
                            role_arn="roleArn",
                            state_machine_name="stateMachineName",
            
                            # the properties below are optional
                            execution_name_prefix="executionNamePrefix"
                        ),
                        timestream=iot.CfnTopicRule.TimestreamActionProperty(
                            database_name="databaseName",
                            dimensions=[iot.CfnTopicRule.TimestreamDimensionProperty(
                                name="name",
                                value="value"
                            )],
                            role_arn="roleArn",
                            table_name="tableName",
            
                            # the properties below are optional
                            timestamp=iot.CfnTopicRule.TimestreamTimestampProperty(
                                unit="unit",
                                value="value"
                            )
                        )
                    )],
                    sql="sql",
            
                    # the properties below are optional
                    aws_iot_sql_version="awsIotSqlVersion",
                    description="description",
                    error_action=iot.CfnTopicRule.ActionProperty(
                        cloudwatch_alarm=iot.CfnTopicRule.CloudwatchAlarmActionProperty(
                            alarm_name="alarmName",
                            role_arn="roleArn",
                            state_reason="stateReason",
                            state_value="stateValue"
                        ),
                        cloudwatch_logs=iot.CfnTopicRule.CloudwatchLogsActionProperty(
                            log_group_name="logGroupName",
                            role_arn="roleArn"
                        ),
                        cloudwatch_metric=iot.CfnTopicRule.CloudwatchMetricActionProperty(
                            metric_name="metricName",
                            metric_namespace="metricNamespace",
                            metric_unit="metricUnit",
                            metric_value="metricValue",
                            role_arn="roleArn",
            
                            # the properties below are optional
                            metric_timestamp="metricTimestamp"
                        ),
                        dynamo_db=iot.CfnTopicRule.DynamoDBActionProperty(
                            hash_key_field="hashKeyField",
                            hash_key_value="hashKeyValue",
                            role_arn="roleArn",
                            table_name="tableName",
            
                            # the properties below are optional
                            hash_key_type="hashKeyType",
                            payload_field="payloadField",
                            range_key_field="rangeKeyField",
                            range_key_type="rangeKeyType",
                            range_key_value="rangeKeyValue"
                        ),
                        dynamo_dBv2=iot.CfnTopicRule.DynamoDBv2ActionProperty(
                            put_item=iot.CfnTopicRule.PutItemInputProperty(
                                table_name="tableName"
                            ),
                            role_arn="roleArn"
                        ),
                        elasticsearch=iot.CfnTopicRule.ElasticsearchActionProperty(
                            endpoint="endpoint",
                            id="id",
                            index="index",
                            role_arn="roleArn",
                            type="type"
                        ),
                        firehose=iot.CfnTopicRule.FirehoseActionProperty(
                            delivery_stream_name="deliveryStreamName",
                            role_arn="roleArn",
            
                            # the properties below are optional
                            batch_mode=False,
                            separator="separator"
                        ),
                        http=iot.CfnTopicRule.HttpActionProperty(
                            url="url",
            
                            # the properties below are optional
                            auth=iot.CfnTopicRule.HttpAuthorizationProperty(
                                sigv4=iot.CfnTopicRule.SigV4AuthorizationProperty(
                                    role_arn="roleArn",
                                    service_name="serviceName",
                                    signing_region="signingRegion"
                                )
                            ),
                            confirmation_url="confirmationUrl",
                            headers=[iot.CfnTopicRule.HttpActionHeaderProperty(
                                key="key",
                                value="value"
                            )]
                        ),
                        iot_analytics=iot.CfnTopicRule.IotAnalyticsActionProperty(
                            channel_name="channelName",
                            role_arn="roleArn",
            
                            # the properties below are optional
                            batch_mode=False
                        ),
                        iot_events=iot.CfnTopicRule.IotEventsActionProperty(
                            input_name="inputName",
                            role_arn="roleArn",
            
                            # the properties below are optional
                            batch_mode=False,
                            message_id="messageId"
                        ),
                        iot_site_wise=iot.CfnTopicRule.IotSiteWiseActionProperty(
                            put_asset_property_value_entries=[iot.CfnTopicRule.PutAssetPropertyValueEntryProperty(
                                property_values=[iot.CfnTopicRule.AssetPropertyValueProperty(
                                    timestamp=iot.CfnTopicRule.AssetPropertyTimestampProperty(
                                        time_in_seconds="timeInSeconds",
            
                                        # the properties below are optional
                                        offset_in_nanos="offsetInNanos"
                                    ),
                                    value=iot.CfnTopicRule.AssetPropertyVariantProperty(
                                        boolean_value="booleanValue",
                                        double_value="doubleValue",
                                        integer_value="integerValue",
                                        string_value="stringValue"
                                    ),
            
                                    # the properties below are optional
                                    quality="quality"
                                )],
            
                                # the properties below are optional
                                asset_id="assetId",
                                entry_id="entryId",
                                property_alias="propertyAlias",
                                property_id="propertyId"
                            )],
                            role_arn="roleArn"
                        ),
                        kafka=iot.CfnTopicRule.KafkaActionProperty(
                            client_properties={
                                "client_properties_key": "clientProperties"
                            },
                            destination_arn="destinationArn",
                            topic="topic",
            
                            # the properties below are optional
                            key="key",
                            partition="partition"
                        ),
                        kinesis=iot.CfnTopicRule.KinesisActionProperty(
                            role_arn="roleArn",
                            stream_name="streamName",
            
                            # the properties below are optional
                            partition_key="partitionKey"
                        ),
                        lambda_=iot.CfnTopicRule.LambdaActionProperty(
                            function_arn="functionArn"
                        ),
                        location=iot.CfnTopicRule.LocationActionProperty(
                            device_id="deviceId",
                            latitude="latitude",
                            longitude="longitude",
                            role_arn="roleArn",
                            tracker_name="trackerName",
            
                            # the properties below are optional
                            timestamp=Date()
                        ),
                        open_search=iot.CfnTopicRule.OpenSearchActionProperty(
                            endpoint="endpoint",
                            id="id",
                            index="index",
                            role_arn="roleArn",
                            type="type"
                        ),
                        republish=iot.CfnTopicRule.RepublishActionProperty(
                            role_arn="roleArn",
                            topic="topic",
            
                            # the properties below are optional
                            headers=iot.CfnTopicRule.RepublishActionHeadersProperty(
                                content_type="contentType",
                                correlation_data="correlationData",
                                message_expiry="messageExpiry",
                                payload_format_indicator="payloadFormatIndicator",
                                response_topic="responseTopic",
                                user_properties=[iot.CfnTopicRule.UserPropertyProperty(
                                    key="key",
                                    value="value"
                                )]
                            ),
                            qos=123
                        ),
                        s3=iot.CfnTopicRule.S3ActionProperty(
                            bucket_name="bucketName",
                            key="key",
                            role_arn="roleArn",
            
                            # the properties below are optional
                            canned_acl="cannedAcl"
                        ),
                        sns=iot.CfnTopicRule.SnsActionProperty(
                            role_arn="roleArn",
                            target_arn="targetArn",
            
                            # the properties below are optional
                            message_format="messageFormat"
                        ),
                        sqs=iot.CfnTopicRule.SqsActionProperty(
                            queue_url="queueUrl",
                            role_arn="roleArn",
            
                            # the properties below are optional
                            use_base64=False
                        ),
                        step_functions=iot.CfnTopicRule.StepFunctionsActionProperty(
                            role_arn="roleArn",
                            state_machine_name="stateMachineName",
            
                            # the properties below are optional
                            execution_name_prefix="executionNamePrefix"
                        ),
                        timestream=iot.CfnTopicRule.TimestreamActionProperty(
                            database_name="databaseName",
                            dimensions=[iot.CfnTopicRule.TimestreamDimensionProperty(
                                name="name",
                                value="value"
                            )],
                            role_arn="roleArn",
                            table_name="tableName",
            
                            # the properties below are optional
                            timestamp=iot.CfnTopicRule.TimestreamTimestampProperty(
                                unit="unit",
                                value="value"
                            )
                        )
                    ),
                    rule_disabled=False
                ),
            
                # the properties below are optional
                rule_name="ruleName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55f9095b7da2c51028e09eab4070f6f5c19d89372748e0818ea666260fb7a0fe)
            check_type(argname="argument topic_rule_payload", value=topic_rule_payload, expected_type=type_hints["topic_rule_payload"])
            check_type(argname="argument rule_name", value=rule_name, expected_type=type_hints["rule_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "topic_rule_payload": topic_rule_payload,
        }
        if rule_name is not None:
            self._values["rule_name"] = rule_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def topic_rule_payload(
        self,
    ) -> typing.Union[CfnTopicRule.TopicRulePayloadProperty, _IResolvable_a771d0ef]:
        '''The rule payload.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicrule.html#cfn-iot-topicrule-topicrulepayload
        '''
        result = self._values.get("topic_rule_payload")
        assert result is not None, "Required property 'topic_rule_payload' is missing"
        return typing.cast(typing.Union[CfnTopicRule.TopicRulePayloadProperty, _IResolvable_a771d0ef], result)

    @builtins.property
    def rule_name(self) -> typing.Optional[builtins.str]:
        '''The name of the rule.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicrule.html#cfn-iot-topicrule-rulename
        '''
        result = self._values.get("rule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''Metadata which can be used to manage the topic rule.

        .. epigraph::

           For URI Request parameters use format: ...key1=value1&key2=value2...

           For the CLI command-line parameter use format: --tags "key1=value1&key2=value2..."

           For the cli-input-json file use format: "tags": "key1=value1&key2=value2..."

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicrule.html#cfn-iot-topicrule-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTopicRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="monocdk.aws_iot.IAction")
class IAction(typing_extensions.Protocol):
    '''(experimental) An abstract action for TopicRule.

    :stability: experimental
    '''

    @jsii.member(jsii_name="bind")
    def bind(self, topic_rule: "ITopicRule") -> ActionConfig:
        '''(experimental) Returns the topic rule action specification.

        :param topic_rule: The TopicRule that would trigger this action.

        :stability: experimental
        '''
        ...


class _IActionProxy:
    '''(experimental) An abstract action for TopicRule.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_iot.IAction"

    @jsii.member(jsii_name="bind")
    def bind(self, topic_rule: "ITopicRule") -> ActionConfig:
        '''(experimental) Returns the topic rule action specification.

        :param topic_rule: The TopicRule that would trigger this action.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__992fc37ab73c0cf93c297558ddadf0ad93320669301318a6864343134effbf96)
            check_type(argname="argument topic_rule", value=topic_rule, expected_type=type_hints["topic_rule"])
        return typing.cast(ActionConfig, jsii.invoke(self, "bind", [topic_rule]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAction).__jsii_proxy_class__ = lambda : _IActionProxy


@jsii.interface(jsii_type="monocdk.aws_iot.ITopicRule")
class ITopicRule(_IResource_8c1dbbbd, typing_extensions.Protocol):
    '''(experimental) Represents an AWS IoT Rule.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="topicRuleArn")
    def topic_rule_arn(self) -> builtins.str:
        '''(experimental) The value of the topic rule Amazon Resource Name (ARN), such as arn:aws:iot:us-east-2:123456789012:rule/rule_name.

        :stability: experimental
        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="topicRuleName")
    def topic_rule_name(self) -> builtins.str:
        '''(experimental) The name topic rule.

        :stability: experimental
        :attribute: true
        '''
        ...


class _ITopicRuleProxy(
    jsii.proxy_for(_IResource_8c1dbbbd), # type: ignore[misc]
):
    '''(experimental) Represents an AWS IoT Rule.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_iot.ITopicRule"

    @builtins.property
    @jsii.member(jsii_name="topicRuleArn")
    def topic_rule_arn(self) -> builtins.str:
        '''(experimental) The value of the topic rule Amazon Resource Name (ARN), such as arn:aws:iot:us-east-2:123456789012:rule/rule_name.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "topicRuleArn"))

    @builtins.property
    @jsii.member(jsii_name="topicRuleName")
    def topic_rule_name(self) -> builtins.str:
        '''(experimental) The name topic rule.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "topicRuleName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITopicRule).__jsii_proxy_class__ = lambda : _ITopicRuleProxy


class IotSql(metaclass=jsii.JSIIAbstractClass, jsii_type="monocdk.aws_iot.IotSql"):
    '''(experimental) Defines AWS IoT SQL.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        bucket = s3.Bucket(self, "MyBucket")
        
        iot.TopicRule(self, "TopicRule",
            sql=iot.IotSql.from_string_as_ver20160323("SELECT * FROM 'device/+/data'"),
            actions=[
                actions.S3PutObjectAction(bucket,
                    access_control=s3.BucketAccessControl.PUBLIC_READ
                )
            ]
        )
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="fromStringAsVer20151008")
    @builtins.classmethod
    def from_string_as_ver20151008(cls, sql: builtins.str) -> "IotSql":
        '''(experimental) Uses the original SQL version built on 2015-10-08.

        :param sql: The actual SQL-like syntax query.

        :return: Instance of IotSql

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb0c55f92d065b5aee0f2c2f0c5e55d4a84849ee435c7ca913b981c9c566b877)
            check_type(argname="argument sql", value=sql, expected_type=type_hints["sql"])
        return typing.cast("IotSql", jsii.sinvoke(cls, "fromStringAsVer20151008", [sql]))

    @jsii.member(jsii_name="fromStringAsVer20160323")
    @builtins.classmethod
    def from_string_as_ver20160323(cls, sql: builtins.str) -> "IotSql":
        '''(experimental) Uses the SQL version built on 2016-03-23.

        :param sql: The actual SQL-like syntax query.

        :return: Instance of IotSql

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ac2166f7d917030033ecde06814c9225b3fac8b7fc538c52de58a6b4a8c5bed)
            check_type(argname="argument sql", value=sql, expected_type=type_hints["sql"])
        return typing.cast("IotSql", jsii.sinvoke(cls, "fromStringAsVer20160323", [sql]))

    @jsii.member(jsii_name="fromStringAsVerNewestUnstable")
    @builtins.classmethod
    def from_string_as_ver_newest_unstable(cls, sql: builtins.str) -> "IotSql":
        '''(experimental) Uses the most recent beta SQL version.

        If you use this version, it might
        introduce breaking changes to your rules.

        :param sql: The actual SQL-like syntax query.

        :return: Instance of IotSql

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04b433d003522fac5136f25b9abb3f0bf205eae563cd06c951dc6d09f50971c8)
            check_type(argname="argument sql", value=sql, expected_type=type_hints["sql"])
        return typing.cast("IotSql", jsii.sinvoke(cls, "fromStringAsVerNewestUnstable", [sql]))

    @jsii.member(jsii_name="bind")
    @abc.abstractmethod
    def bind(self, scope: _constructs_77d1e7e8.Construct) -> "IotSqlConfig":
        '''(experimental) Returns the IoT SQL configuration.

        :param scope: -

        :stability: experimental
        '''
        ...


class _IotSqlProxy(IotSql):
    @jsii.member(jsii_name="bind")
    def bind(self, scope: _constructs_77d1e7e8.Construct) -> "IotSqlConfig":
        '''(experimental) Returns the IoT SQL configuration.

        :param scope: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a64f871a74e656d723c0d990bed48a5dfd7de0ff5366e3b00534ad53236578d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast("IotSqlConfig", jsii.invoke(self, "bind", [scope]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, IotSql).__jsii_proxy_class__ = lambda : _IotSqlProxy


@jsii.data_type(
    jsii_type="monocdk.aws_iot.IotSqlConfig",
    jsii_struct_bases=[],
    name_mapping={"aws_iot_sql_version": "awsIotSqlVersion", "sql": "sql"},
)
class IotSqlConfig:
    def __init__(self, *, aws_iot_sql_version: builtins.str, sql: builtins.str) -> None:
        '''(experimental) The type returned from the ``bind()`` method in {@link IotSql}.

        :param aws_iot_sql_version: (experimental) The version of the SQL rules engine to use when evaluating the rule.
        :param sql: (experimental) The SQL statement used to query the topic.

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_iot as iot
            
            iot_sql_config = iot.IotSqlConfig(
                aws_iot_sql_version="awsIotSqlVersion",
                sql="sql"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5aa54034018f3b129824b87c02de32e6d1f6a094164becba9c9488c679d7af1e)
            check_type(argname="argument aws_iot_sql_version", value=aws_iot_sql_version, expected_type=type_hints["aws_iot_sql_version"])
            check_type(argname="argument sql", value=sql, expected_type=type_hints["sql"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "aws_iot_sql_version": aws_iot_sql_version,
            "sql": sql,
        }

    @builtins.property
    def aws_iot_sql_version(self) -> builtins.str:
        '''(experimental) The version of the SQL rules engine to use when evaluating the rule.

        :stability: experimental
        '''
        result = self._values.get("aws_iot_sql_version")
        assert result is not None, "Required property 'aws_iot_sql_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sql(self) -> builtins.str:
        '''(experimental) The SQL statement used to query the topic.

        :stability: experimental
        '''
        result = self._values.get("sql")
        assert result is not None, "Required property 'sql' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotSqlConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(ITopicRule)
class TopicRule(
    _Resource_abff4495,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_iot.TopicRule",
):
    '''(experimental) Defines an AWS IoT Rule in this stack.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        bucket = s3.Bucket(self, "MyBucket")
        
        iot.TopicRule(self, "TopicRule",
            sql=iot.IotSql.from_string_as_ver20160323("SELECT * FROM 'device/+/data'"),
            actions=[
                actions.S3PutObjectAction(bucket,
                    access_control=s3.BucketAccessControl.PUBLIC_READ
                )
            ]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        sql: IotSql,
        actions: typing.Optional[typing.Sequence[IAction]] = None,
        description: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[builtins.bool] = None,
        error_action: typing.Optional[IAction] = None,
        topic_rule_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param sql: (experimental) A simplified SQL syntax to filter messages received on an MQTT topic and push the data elsewhere.
        :param actions: (experimental) The actions associated with the topic rule. Default: No actions will be perform
        :param description: (experimental) A textual description of the topic rule. Default: None
        :param enabled: (experimental) Specifies whether the rule is enabled. Default: true
        :param error_action: (experimental) The action AWS IoT performs when it is unable to perform a rule's action. Default: - no action will be performed
        :param topic_rule_name: (experimental) The name of the topic rule. Default: None

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1e1f7a13368fc4d47d88f55b877035d9782a55600a0632e60d6cb31a97d03a7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = TopicRuleProps(
            sql=sql,
            actions=actions,
            description=description,
            enabled=enabled,
            error_action=error_action,
            topic_rule_name=topic_rule_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromTopicRuleArn")
    @builtins.classmethod
    def from_topic_rule_arn(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        topic_rule_arn: builtins.str,
    ) -> ITopicRule:
        '''(experimental) Import an existing AWS IoT Rule provided an ARN.

        :param scope: The parent creating construct (usually ``this``).
        :param id: The construct's name.
        :param topic_rule_arn: AWS IoT Rule ARN (i.e. arn:aws:iot:::rule/MyRule).

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c41e62a57f74f91db099c49a0a62201ca9d32bf16a4005a62a04d2ba26bb3746)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument topic_rule_arn", value=topic_rule_arn, expected_type=type_hints["topic_rule_arn"])
        return typing.cast(ITopicRule, jsii.sinvoke(cls, "fromTopicRuleArn", [scope, id, topic_rule_arn]))

    @jsii.member(jsii_name="addAction")
    def add_action(self, action: IAction) -> None:
        '''(experimental) Add a action to the topic rule.

        :param action: the action to associate with the topic rule.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dfaa7a8aeddc4c10cfeda3a8589d52668ea589935ddc9aa8ee0ba1d9db5aa583)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
        return typing.cast(None, jsii.invoke(self, "addAction", [action]))

    @builtins.property
    @jsii.member(jsii_name="topicRuleArn")
    def topic_rule_arn(self) -> builtins.str:
        '''(experimental) Arn of this topic rule.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "topicRuleArn"))

    @builtins.property
    @jsii.member(jsii_name="topicRuleName")
    def topic_rule_name(self) -> builtins.str:
        '''(experimental) Name of this topic rule.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "topicRuleName"))


@jsii.data_type(
    jsii_type="monocdk.aws_iot.TopicRuleProps",
    jsii_struct_bases=[],
    name_mapping={
        "sql": "sql",
        "actions": "actions",
        "description": "description",
        "enabled": "enabled",
        "error_action": "errorAction",
        "topic_rule_name": "topicRuleName",
    },
)
class TopicRuleProps:
    def __init__(
        self,
        *,
        sql: IotSql,
        actions: typing.Optional[typing.Sequence[IAction]] = None,
        description: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[builtins.bool] = None,
        error_action: typing.Optional[IAction] = None,
        topic_rule_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Properties for defining an AWS IoT Rule.

        :param sql: (experimental) A simplified SQL syntax to filter messages received on an MQTT topic and push the data elsewhere.
        :param actions: (experimental) The actions associated with the topic rule. Default: No actions will be perform
        :param description: (experimental) A textual description of the topic rule. Default: None
        :param enabled: (experimental) Specifies whether the rule is enabled. Default: true
        :param error_action: (experimental) The action AWS IoT performs when it is unable to perform a rule's action. Default: - no action will be performed
        :param topic_rule_name: (experimental) The name of the topic rule. Default: None

        :stability: experimental
        :exampleMetadata: infused

        Example::

            bucket = s3.Bucket(self, "MyBucket")
            
            iot.TopicRule(self, "TopicRule",
                sql=iot.IotSql.from_string_as_ver20160323("SELECT * FROM 'device/+/data'"),
                actions=[
                    actions.S3PutObjectAction(bucket,
                        access_control=s3.BucketAccessControl.PUBLIC_READ
                    )
                ]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c48d275314c249b167a6a70bbba214a533770e8feb6e3a44b1748e24d6d3d10)
            check_type(argname="argument sql", value=sql, expected_type=type_hints["sql"])
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument error_action", value=error_action, expected_type=type_hints["error_action"])
            check_type(argname="argument topic_rule_name", value=topic_rule_name, expected_type=type_hints["topic_rule_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "sql": sql,
        }
        if actions is not None:
            self._values["actions"] = actions
        if description is not None:
            self._values["description"] = description
        if enabled is not None:
            self._values["enabled"] = enabled
        if error_action is not None:
            self._values["error_action"] = error_action
        if topic_rule_name is not None:
            self._values["topic_rule_name"] = topic_rule_name

    @builtins.property
    def sql(self) -> IotSql:
        '''(experimental) A simplified SQL syntax to filter messages received on an MQTT topic and push the data elsewhere.

        :see: https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-reference.html
        :stability: experimental
        '''
        result = self._values.get("sql")
        assert result is not None, "Required property 'sql' is missing"
        return typing.cast(IotSql, result)

    @builtins.property
    def actions(self) -> typing.Optional[typing.List[IAction]]:
        '''(experimental) The actions associated with the topic rule.

        :default: No actions will be perform

        :stability: experimental
        '''
        result = self._values.get("actions")
        return typing.cast(typing.Optional[typing.List[IAction]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) A textual description of the topic rule.

        :default: None

        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Specifies whether the rule is enabled.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def error_action(self) -> typing.Optional[IAction]:
        '''(experimental) The action AWS IoT performs when it is unable to perform a rule's action.

        :default: - no action will be performed

        :stability: experimental
        '''
        result = self._values.get("error_action")
        return typing.cast(typing.Optional[IAction], result)

    @builtins.property
    def topic_rule_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of the topic rule.

        :default: None

        :stability: experimental
        '''
        result = self._values.get("topic_rule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TopicRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ActionConfig",
    "CfnAccountAuditConfiguration",
    "CfnAccountAuditConfigurationProps",
    "CfnAuthorizer",
    "CfnAuthorizerProps",
    "CfnCACertificate",
    "CfnCACertificateProps",
    "CfnCertificate",
    "CfnCertificateProps",
    "CfnCustomMetric",
    "CfnCustomMetricProps",
    "CfnDimension",
    "CfnDimensionProps",
    "CfnDomainConfiguration",
    "CfnDomainConfigurationProps",
    "CfnFleetMetric",
    "CfnFleetMetricProps",
    "CfnJobTemplate",
    "CfnJobTemplateProps",
    "CfnLogging",
    "CfnLoggingProps",
    "CfnMitigationAction",
    "CfnMitigationActionProps",
    "CfnPolicy",
    "CfnPolicyPrincipalAttachment",
    "CfnPolicyPrincipalAttachmentProps",
    "CfnPolicyProps",
    "CfnProvisioningTemplate",
    "CfnProvisioningTemplateProps",
    "CfnResourceSpecificLogging",
    "CfnResourceSpecificLoggingProps",
    "CfnRoleAlias",
    "CfnRoleAliasProps",
    "CfnScheduledAudit",
    "CfnScheduledAuditProps",
    "CfnSecurityProfile",
    "CfnSecurityProfileProps",
    "CfnThing",
    "CfnThingPrincipalAttachment",
    "CfnThingPrincipalAttachmentProps",
    "CfnThingProps",
    "CfnTopicRule",
    "CfnTopicRuleDestination",
    "CfnTopicRuleDestinationProps",
    "CfnTopicRuleProps",
    "IAction",
    "ITopicRule",
    "IotSql",
    "IotSqlConfig",
    "TopicRule",
    "TopicRuleProps",
]

publication.publish()

def _typecheckingstub__917322bf96f684171fc47212b367dde8956db396e5a79655c238a3ab2480da71(
    *,
    configuration: typing.Union[CfnTopicRule.ActionProperty, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7735d9e6d93dc1a72b84f19f68fb84c0e33d0dfe59ed396a1399db9ce831a9dd(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    account_id: builtins.str,
    audit_check_configurations: typing.Union[typing.Union[CfnAccountAuditConfiguration.AuditCheckConfigurationsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
    role_arn: builtins.str,
    audit_notification_target_configurations: typing.Optional[typing.Union[typing.Union[CfnAccountAuditConfiguration.AuditNotificationTargetConfigurationsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b8b50dbd80fd95746de6c96a6dfbfae5bee9ad27502bc87c56e1b56c7c1de9c(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7d9e06c0b372fecc936f2c7b04b4599158dd256118c6e766cecfb09a0d56c7a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1df43efb3aa9a16d25a96f2305c8cc02e51f52f86b6d954e524590fa054b4f7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78dc0e43a4e743f05c4e07629dc49380fa5ea79f96e8250fef5f8b01a8821da1(
    value: typing.Union[CfnAccountAuditConfiguration.AuditCheckConfigurationsProperty, _IResolvable_a771d0ef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e5018125dbd21a9e8fda914b0cf8f7bb617e37b81d4f77092635de2ed725ea9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1099f85e532c40d2797fc0d72f60d910f5fb880c11ac1d145aa00cbe26ca3fb7(
    value: typing.Optional[typing.Union[CfnAccountAuditConfiguration.AuditNotificationTargetConfigurationsProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cdd76f4f5d6394b1c753a44de5552be456bfb670513bbbad85c6a7f46623ca3(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51c2e37ebbdc3f43373070b2ecda9ebaa07b63f6d481c66f9b00b0d6be5c4b47(
    *,
    authenticated_cognito_role_overly_permissive_check: typing.Optional[typing.Union[typing.Union[CfnAccountAuditConfiguration.AuditCheckConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    ca_certificate_expiring_check: typing.Optional[typing.Union[typing.Union[CfnAccountAuditConfiguration.AuditCheckConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    ca_certificate_key_quality_check: typing.Optional[typing.Union[typing.Union[CfnAccountAuditConfiguration.AuditCheckConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    conflicting_client_ids_check: typing.Optional[typing.Union[typing.Union[CfnAccountAuditConfiguration.AuditCheckConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    device_certificate_expiring_check: typing.Optional[typing.Union[typing.Union[CfnAccountAuditConfiguration.AuditCheckConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    device_certificate_key_quality_check: typing.Optional[typing.Union[typing.Union[CfnAccountAuditConfiguration.AuditCheckConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    device_certificate_shared_check: typing.Optional[typing.Union[typing.Union[CfnAccountAuditConfiguration.AuditCheckConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    intermediate_ca_revoked_for_active_device_certificates_check: typing.Optional[typing.Union[typing.Union[CfnAccountAuditConfiguration.AuditCheckConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    iot_policy_overly_permissive_check: typing.Optional[typing.Union[typing.Union[CfnAccountAuditConfiguration.AuditCheckConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    io_t_policy_potential_mis_configuration_check: typing.Optional[typing.Union[typing.Union[CfnAccountAuditConfiguration.AuditCheckConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    iot_role_alias_allows_access_to_unused_services_check: typing.Optional[typing.Union[typing.Union[CfnAccountAuditConfiguration.AuditCheckConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    iot_role_alias_overly_permissive_check: typing.Optional[typing.Union[typing.Union[CfnAccountAuditConfiguration.AuditCheckConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    logging_disabled_check: typing.Optional[typing.Union[typing.Union[CfnAccountAuditConfiguration.AuditCheckConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    revoked_ca_certificate_still_active_check: typing.Optional[typing.Union[typing.Union[CfnAccountAuditConfiguration.AuditCheckConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    revoked_device_certificate_still_active_check: typing.Optional[typing.Union[typing.Union[CfnAccountAuditConfiguration.AuditCheckConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    unauthenticated_cognito_role_overly_permissive_check: typing.Optional[typing.Union[typing.Union[CfnAccountAuditConfiguration.AuditCheckConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c705c85ad2da0d61407a058eab9f5441ae03ae0c66aee7af95c2c1056660062d(
    *,
    sns: typing.Optional[typing.Union[typing.Union[CfnAccountAuditConfiguration.AuditNotificationTargetProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b39bf997a93d6f0434a608e80932d99b1a895bb1959ce6398e21bb3087a2f93d(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    role_arn: typing.Optional[builtins.str] = None,
    target_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe4d039eb2fde6efe1379ffa426a8799a2e9611fa326ceb114c58a89078b1560(
    *,
    account_id: builtins.str,
    audit_check_configurations: typing.Union[typing.Union[CfnAccountAuditConfiguration.AuditCheckConfigurationsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
    role_arn: builtins.str,
    audit_notification_target_configurations: typing.Optional[typing.Union[typing.Union[CfnAccountAuditConfiguration.AuditNotificationTargetConfigurationsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb3d4475a2c47548b973752777c9b0cff14761d68b55e59b674d8ecd1e3b0534(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    authorizer_function_arn: builtins.str,
    authorizer_name: typing.Optional[builtins.str] = None,
    enable_caching_for_http: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    signing_disabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    status: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    token_key_name: typing.Optional[builtins.str] = None,
    token_signing_public_keys: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, builtins.str]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__393265a5c60fa3d96cacb06aaf67fea5b69fa5962102f55facae0247e4627fe2(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87153c2db95e8d2a428c654b27c0032207c40ada471606a006d46dd5e925a7db(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ddf58b6dd2822aa9ef7f673d2429759b7ec9f126bf87a5d2ab871493e908fea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37ef5ea4d3ab384464cbd4b3dd894b559abe2b73e7edbe814c0bb3c4b5470108(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52b0810482d8bfca9db2d7ded06a9e7da766b6ec01a3b569a63c1ba8cf408c6a(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9816cdb1250cc33b96cda68deb60d284d5a26fb35ab7439e4231ccb53df0fdce(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ae846646e7f76534ec709919af00314c49f1a20ff74b5d6c0dea4176f0e612d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4d22e3fb78176f8fb41cf67e1a83fc5bca67e2ff61d03f7b1e7c4ebab2c2e7a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a92430672f5805744463426fe7335e7a42edee162ca7eba2a4b3a49922f88f17(
    value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__622515a7aaf08f5fc240a31ae650f399d7cf0608bdc8c8030f2508bf611883f5(
    *,
    authorizer_function_arn: builtins.str,
    authorizer_name: typing.Optional[builtins.str] = None,
    enable_caching_for_http: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    signing_disabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    status: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    token_key_name: typing.Optional[builtins.str] = None,
    token_signing_public_keys: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, builtins.str]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5df10346f5adc6dc276c52d395ea544195453293830dc65db55e15eec8ce3d97(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    ca_certificate_pem: builtins.str,
    status: builtins.str,
    auto_registration_status: typing.Optional[builtins.str] = None,
    certificate_mode: typing.Optional[builtins.str] = None,
    registration_config: typing.Optional[typing.Union[typing.Union[CfnCACertificate.RegistrationConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    remove_auto_registration: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    verification_certificate_pem: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2954d0f735960aedcf41f245b79c96ba6a195d28e45d455ebe8bf4a37ec5c8d9(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f88ebd33a08489c9d2aa7d0f11215e1159c40adaa24e2243529e6ca1e0a6522(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07b24e8d3d99c28b3387bbad28620bfad12c47dda99fd97998117e22bde62d68(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35f6753340d6a65c1a34e9f7b99f2fea9a1a4bc1ab1b2fddea5f5ad848547021(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0909ccca1dcf081687443f2b1131f47dd47159ba891348f4274c1d6527c207ad(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5f97aedfa05b70d0f9c1bad07469f863220ecaeffd6862ba43ebad37c8c6d82(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdeb2d3dfd572ecb5655073a143af21a819a63a8766bc9e6753a6f50c800cb6a(
    value: typing.Optional[typing.Union[CfnCACertificate.RegistrationConfigProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2254fab851774a14895a29dfcc6b6930886ac15b9f5d11dcb2d78c43bb2d62ba(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d875df1b83d04338ef80f8897b314945159ddd0846b5b1bb02bb38e38798053(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46c70e01b06ea5f8172ce27ae017b96ca7c083ff55ea1cca833cb379c8c9bcec(
    *,
    role_arn: typing.Optional[builtins.str] = None,
    template_body: typing.Optional[builtins.str] = None,
    template_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3794474e144684ec752cf7d043907532c3c2793028dbcbaeeecdc73ed155167(
    *,
    ca_certificate_pem: builtins.str,
    status: builtins.str,
    auto_registration_status: typing.Optional[builtins.str] = None,
    certificate_mode: typing.Optional[builtins.str] = None,
    registration_config: typing.Optional[typing.Union[typing.Union[CfnCACertificate.RegistrationConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    remove_auto_registration: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    verification_certificate_pem: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e9f9930a9ef23dbbc0c80120852a3d3d7eaed14500fb832a34a7850a5fa02ec(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    status: builtins.str,
    ca_certificate_pem: typing.Optional[builtins.str] = None,
    certificate_mode: typing.Optional[builtins.str] = None,
    certificate_pem: typing.Optional[builtins.str] = None,
    certificate_signing_request: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc96b621eef02c335b00a479741d80fe785601c347561199d6c92c3d4a0f0c26(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56cd44293d14f49ccc9499874a0feac053f4743a00822272b08c8a9f8f03abb1(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c3ec031d0f8d34534c9490f6838104426047a5873f836979214c1e0e817bfb5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98d65aabc08896681c643a46b414185be01155fbbbdc53face2ff76c620c5099(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ac27a55c4f19acffeda86e297ef5f3902d0451c81cf4311a4f3b90ee00c7024(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9427cb91627083d5c604783fb2fdd96813bce8273bc0b4cf7211f279ca5e15c6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f751fb1b3c832b2ae9513cd80fbc3a592ac05a48f50d11e4e4d28f6bce1872b6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16f767e9b8ce74a2e27d508dfe51e4bf1d3cfb255b49b1f480bc2a0d8c643f33(
    *,
    status: builtins.str,
    ca_certificate_pem: typing.Optional[builtins.str] = None,
    certificate_mode: typing.Optional[builtins.str] = None,
    certificate_pem: typing.Optional[builtins.str] = None,
    certificate_signing_request: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ea99b45b7f4b56d3965922a562b9ad71ff1af6ad29be5d45c88d8debae4deb6(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    metric_type: builtins.str,
    display_name: typing.Optional[builtins.str] = None,
    metric_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f569eb8d969344bcec4d01cb0b2775e98604ae5a5f85f4ffc0a5642c5f39fc06(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18fc78138538df0f68c3687920dc04a2e8b5626aa90bd1fcce08d903c519a136(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52cf83af158df69ae1246e2607320bd9bef859fba73ad0d6703c9d4d039f621e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0932a4b138ed9513bfaccdd46b9debcb30c9dffb4a8f0baaaac56cafb0795e40(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6ce0019127a4adfdec183be6e19c979df1164122220af4f789c14159654dc10(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb4d6cbddb71e9e4cd4bd3f81a22d7fcd9a82141828d5d7d2ef317843439dca0(
    *,
    metric_type: builtins.str,
    display_name: typing.Optional[builtins.str] = None,
    metric_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06cf84da0cf82ce58aef400445e90ce286914282b92497e27bc27c69be795834(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    string_values: typing.Sequence[builtins.str],
    type: builtins.str,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c25a23adb0e23c44f82ad046f58d62744b1b141804301e90c514f4af28693af0(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33ea8897257f3f21768f39fe1a097709c45600ec87e3d67741d9510433ce1a0f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c087f199ff4686daadad3cc62a699572c85b7257381085a3e302cbc6d3d28145(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbe1bf77dbcf6fa1a7326d35cffb405a6f5d9b361a01766b98cfc7965970ffc1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__726401c262fbc85fa8a1847cfdcdf3513dc239b04f530b6cdbaa51a0827644a9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35ce00723e902f0b46065ca937def6947b708a0431cf4d5729f5fb988ed12309(
    *,
    string_values: typing.Sequence[builtins.str],
    type: builtins.str,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4f77b2d0d9579ebb455828dc3cede63a5e9e426f72891eb5acf208c94094670(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    authorizer_config: typing.Optional[typing.Union[typing.Union[CfnDomainConfiguration.AuthorizerConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    domain_configuration_name: typing.Optional[builtins.str] = None,
    domain_configuration_status: typing.Optional[builtins.str] = None,
    domain_name: typing.Optional[builtins.str] = None,
    server_certificate_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    service_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    validation_certificate_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34424cba98d5fd002279af60091cebece661a02a2e54b47c3eba5b7a5dacaeaa(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07fcd6f026b661c3afb848e58ae51d238faf4b3a1300829c3bc024ac176fc30a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07a2dc93550cbb719e30317479efbaf401d6aa9e4eba1935f757a30cb5b1afbc(
    value: typing.Optional[typing.Union[CfnDomainConfiguration.AuthorizerConfigProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecdc2464d6dc7099fc1ac686164ade1ef8263473dd0c70cb18cff7ef3ab38923(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6062d91a52a6e2f058bb8256a4994bec069946dad4e76a471846a8204c1019b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f138275dee3bc63e590defd3487ad6f8b6085c1702af336923fe0aa9d9cb248(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcbea10657987047afcf50b0f211e74045a25f552d465fc9a5e7ad20eebd1969(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89a2a17569b2ea82a87615d93e454e41d3a84e5f951b37939309842676fbaaa4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b55e1c672780e2e7b9130eb08180bbc14d2d64b47fd5cc880e9fdcff204d7cc3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a314a31439fda332ad90d8941379d5aa35f6979ccdd689ec7da0a1c8273b0b88(
    *,
    allow_authorizer_override: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    default_authorizer_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5998b48e54d6ca703ebea656a326aec99045f8a75952682ec6d44a4acbfd566(
    *,
    server_certificate_arn: typing.Optional[builtins.str] = None,
    server_certificate_status: typing.Optional[builtins.str] = None,
    server_certificate_status_detail: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9791be0b7126c5317bb6533c36262b9258afd7e1638de38299ba4e4db3f0d75(
    *,
    authorizer_config: typing.Optional[typing.Union[typing.Union[CfnDomainConfiguration.AuthorizerConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    domain_configuration_name: typing.Optional[builtins.str] = None,
    domain_configuration_status: typing.Optional[builtins.str] = None,
    domain_name: typing.Optional[builtins.str] = None,
    server_certificate_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    service_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    validation_certificate_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ad7e60f88b12c0a66362e3e5f6010339fff15ed323c0cc55f68167135b10788(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    metric_name: builtins.str,
    aggregation_field: typing.Optional[builtins.str] = None,
    aggregation_type: typing.Optional[typing.Union[typing.Union[CfnFleetMetric.AggregationTypeProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    description: typing.Optional[builtins.str] = None,
    index_name: typing.Optional[builtins.str] = None,
    period: typing.Optional[jsii.Number] = None,
    query_string: typing.Optional[builtins.str] = None,
    query_version: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    unit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5fd8d0171814851db4c44c37a7cce6b5112c531f2a57b44b2b0725ecdc1aad6(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9dcfaf66d471bdea96f603e58143c22b32b0d0dbe6aa413418a339677e02144c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c2acbeff787ff877313a4ec2b95574d5a80949dd269a985b73d741b3c3192af(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bb211b4b5a3eadbe0f3fb4e0370e939c47a91571a3f01c506b69752c96140e4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13472d3409b3845c68e55be14fcfe88a7e42fb4a57e4df346da4c2046a1b594f(
    value: typing.Optional[typing.Union[CfnFleetMetric.AggregationTypeProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11466b926632a4d4bebd6f7a6062d9e2d4e16acc6d4259a5533c3a286abb8595(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__874b92f83a08a65e8cc0d4dbe5bfb269348a7620899708b590194410ca10a5ad(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__974d067c0c4aaabbb36191bcb265cdaa6d9b88edd52d590299a61217391f4075(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22a291e38e3fca078dbafcd8da2d1d570e3347e1484b5b65a4de3539555f7d61(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e957fe630fd8a4b4978a61b8230963d24324584aadc323d51dd4a1fb10b4012b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec8c2b0c7f95ad810c55a87aaddd01070aa123237f8c594e93d1d0109dd2331e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f65e968ba2f22b03f2813acc234863e0e6865868c95bdf069bb4471b58f584d6(
    *,
    name: builtins.str,
    values: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f08a9cea47193eddb52faffb25f0135e360e21c0359b67cfe87ac3255e5ee2a(
    *,
    metric_name: builtins.str,
    aggregation_field: typing.Optional[builtins.str] = None,
    aggregation_type: typing.Optional[typing.Union[typing.Union[CfnFleetMetric.AggregationTypeProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    description: typing.Optional[builtins.str] = None,
    index_name: typing.Optional[builtins.str] = None,
    period: typing.Optional[jsii.Number] = None,
    query_string: typing.Optional[builtins.str] = None,
    query_version: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    unit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6ae87ac21ac364701bedc97923edce3167092f0de57514b10a0c7d7f61c4e43(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    description: builtins.str,
    job_template_id: builtins.str,
    abort_config: typing.Any = None,
    document: typing.Optional[builtins.str] = None,
    document_source: typing.Optional[builtins.str] = None,
    job_arn: typing.Optional[builtins.str] = None,
    job_executions_rollout_config: typing.Any = None,
    presigned_url_config: typing.Any = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    timeout_config: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e540bbe80561dc99a5e95510f3908cdfad3e7e800895992be55e0556eee73a02(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c714b28049fdfb5462bc15aafb30823e39213b84388ad13626d17ebcbd38b478(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0c163e2f7e3d96569821161b4db787f334aa09f0d6246b354ad47f357a6e5b0(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6360d951d29c8c6dba1ecf345078aa3a681867bcf0eab64d409704e6b1f3ade2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0582e1d8ce9cff0dd05164303eac92fa59ab15f6cada781f3b1641c1220006d1(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a70e9489919ab2f13d25979014dca16c202289959793a22589931bbbd9a9493(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63ce99e49d9bcde619873266cec6f536c971497634407aca31ebe48986718e91(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6c45644e0543bf0702fa22b35d6eb5e1761ecdf1c4c83507f1816feea8e1dd0(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbd7fee843fd1c6208c7661e62a57645c563ce3bfe4977efc88e2db6e874ddc3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8ea3b2ce1e276358f7e126496357e5f3b42a19b6269f4b01a7d4463c7c5660e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63edbe9554e9d577da6f373c1eea4064c9dbfcd432d5be5b4a7f776d2578ca50(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f713fd224eae400c78a9c31920704be55aac90079a2fb14b888145dc3155489e(
    *,
    criteria_list: typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union[CfnJobTemplate.AbortCriteriaProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f37cfdc20d16a90587cd6e9b32eaa846d03d80defc5cd35a6704fd495329de33(
    *,
    action: builtins.str,
    failure_type: builtins.str,
    min_number_of_executed_things: jsii.Number,
    threshold_percentage: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2052a32a583bd05cf3037191b5c148ac2d2e32b19afb0b3ac4c5d0558bf6396(
    *,
    base_rate_per_minute: jsii.Number,
    increment_factor: jsii.Number,
    rate_increase_criteria: typing.Union[typing.Union[CfnJobTemplate.RateIncreaseCriteriaProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aac20f7f460de569a8f5d8e6a182e48b1956c801ac829d51e0002b820ee0f2e4(
    *,
    exponential_rollout_rate: typing.Optional[typing.Union[typing.Union[CfnJobTemplate.ExponentialRolloutRateProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    maximum_per_minute: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4e94ff4d2f6d8f1b221fcac01434fbeab49de32c4145002c77d26cc1e4cf006(
    *,
    role_arn: builtins.str,
    expires_in_sec: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e5be353af0f898d3561e3fcbd7a9b2ecc609f1285539d8f844baddb1a04a445(
    *,
    number_of_notified_things: typing.Optional[jsii.Number] = None,
    number_of_succeeded_things: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4fd99ca69eb4073923cadbf5039d2c3d852ee132232742a4c7258c4869166d7(
    *,
    in_progress_timeout_in_minutes: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0decc37289d85c109d4c12fd8652a7a5ace85f7b636a9dd9a05a64bebc84309(
    *,
    description: builtins.str,
    job_template_id: builtins.str,
    abort_config: typing.Any = None,
    document: typing.Optional[builtins.str] = None,
    document_source: typing.Optional[builtins.str] = None,
    job_arn: typing.Optional[builtins.str] = None,
    job_executions_rollout_config: typing.Any = None,
    presigned_url_config: typing.Any = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    timeout_config: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__094396c4ba46b29a170381deac5107d2d442c7327a43c7108fea10990cfc8aa5(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    account_id: builtins.str,
    default_log_level: builtins.str,
    role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72aab6343747b627f655b318ab8cff0961b9985f8d4938911d2e6b719c1b77bc(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dc06cd0f2c036f3770e19b87d77f3d4b8db582665521b3da6ecc676fe899381(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4096259646bae3677e768871b27d0032cbc0d107a078723298d984dd0e749835(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98616587275eb46377308ad9f5bdab9ad927c9eb8dcdc1b20ae94e82f821c860(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0aed8eaa9b09117c4de6bdb5e8eddfd3ce11681d84504cab7ebdeed7839910b4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c49d63e33b9998468fa3da7a5e3b3007a5d6d5a584fd2ec917b0667107d73736(
    *,
    account_id: builtins.str,
    default_log_level: builtins.str,
    role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f1fc93a374a9f5fbe17fc2443ad7de6d1da6e42bfcb421c2687874abfcc8c87(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    action_params: typing.Union[typing.Union[CfnMitigationAction.ActionParamsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
    role_arn: builtins.str,
    action_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9681819be2ae3a90eabbe27bdb1e9e1cef3129de4b848903ecafe26c94cb567(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc7905926753ab9369de30e8966a4b6b9c1a1d578be14c601cef5890774c5204(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f87c4b2a4154c3a913ff062d9f80e18ede929978c58c77ea5330dbe5fa085b5(
    value: typing.Union[CfnMitigationAction.ActionParamsProperty, _IResolvable_a771d0ef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d03fe96a6e41ba4ca36bbac697ea96ec1eef217f0a0bfed192421d6277445f7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2751a30a0ae45200585494f0ef85db81102e76115cd3f914e8eff79574830daa(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fa438995fc0d7aefbb02d6cb1cf2658e86c5feaba485ccb8cfbf158f2752d7b(
    *,
    add_things_to_thing_group_params: typing.Optional[typing.Union[typing.Union[CfnMitigationAction.AddThingsToThingGroupParamsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    enable_io_t_logging_params: typing.Optional[typing.Union[typing.Union[CfnMitigationAction.EnableIoTLoggingParamsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    publish_finding_to_sns_params: typing.Optional[typing.Union[typing.Union[CfnMitigationAction.PublishFindingToSnsParamsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    replace_default_policy_version_params: typing.Optional[typing.Union[typing.Union[CfnMitigationAction.ReplaceDefaultPolicyVersionParamsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    update_ca_certificate_params: typing.Optional[typing.Union[typing.Union[CfnMitigationAction.UpdateCACertificateParamsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    update_device_certificate_params: typing.Optional[typing.Union[typing.Union[CfnMitigationAction.UpdateDeviceCertificateParamsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62315475f8b9e1ad115d4b1043c244bdd7c7724f3b130ceb1366d049a4281573(
    *,
    thing_group_names: typing.Sequence[builtins.str],
    override_dynamic_groups: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05f7fa9ace7eb3c7a73e5554fe913bffeda246838ad56cfeb2a6663babf21713(
    *,
    log_level: builtins.str,
    role_arn_for_logging: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7f908687b0442f75f713201d9dc73aab0b0bc6353a45aeef5fd76eaaa8819f8(
    *,
    topic_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fec333637e63c1005e865ee0a0f9d57f3c2e2480eead909c426c912d58979d3(
    *,
    template_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d555f0718607bfbd2097eabd0431f4fce4106de8ed10abcb5949490b3baf2a6(
    *,
    action: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4466ace39cb892646bcec1de381f51023676ca4ddb2c9d87e502df660d1cf46d(
    *,
    action: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fc8df50d6a3c464d38587d33fb0412fafefeab7fc91aacd7771d258f6ef3612(
    *,
    action_params: typing.Union[typing.Union[CfnMitigationAction.ActionParamsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
    role_arn: builtins.str,
    action_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af5396a485d06b911d0023fd01f96d6bccbf23d00fe1558193b3debd143c3aef(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    policy_document: typing.Any,
    policy_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53e20aef529a293726b05d79c8367efb6a9f652f4121e6e59e1e208d1ede2365(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82df28135aafb896b5052677a10e0ad0cc0a76c5f04bbf6abb6f452d4874b98b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__971b0e779eec8b37c0aa0435e6ef8b6ec5c7102da4dee086f6f99109566ff118(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d3ebbb610b1e68e94230fc11112a30bdf72a5f815e7442068d98ea3dd83f62b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac497ff31455c302c3f5d97976877d66385ffe9c8e6e48d65de13104f7b0cac6(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    policy_name: builtins.str,
    principal: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df9723249134a9366075c700cc71ceba31c3ab1430d67a749ffd155f44a0604a(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c6ebcf3653574963142342336ce4413f7f6d3817513511c4f7968747b9f9d4b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb834eb03939d2519ba3fe596d8aa6670002d89315b5315ba47fd581b62f5005(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f0f4dacfed464c52f4b1f63a29b3c0dde9beebee28bb3fb2e393a9f184b4bea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e33e6624c7935fc745022194b588c823cf604dad86124deb914487d6c8f0ca40(
    *,
    policy_name: builtins.str,
    principal: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d2cfeb79448e99f155b4adbba540852e9fce0ec72e1393a4ed63a785bd25c56(
    *,
    policy_document: typing.Any,
    policy_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9cc379a1ac891d551f4dd43074a18069d69b0c3fa87a57b9cc09378518c3778(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    provisioning_role_arn: builtins.str,
    template_body: builtins.str,
    description: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    pre_provisioning_hook: typing.Optional[typing.Union[typing.Union[CfnProvisioningTemplate.ProvisioningHookProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    template_name: typing.Optional[builtins.str] = None,
    template_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db44932761309b6e1a448d9599affc21d9ef0bfd84014cddc94d66f4f11c4f48(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2eba7d4a89a9f98d642f943528919e2343c5f422e0d9aef4c29b8c4878576fe(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce7231928f866847628df1fe1e1e64990553e8881b20092ab8939eae488913e6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a275b33144106516b375d8d61597ab9bcb7a1b4997205f0a6b6f4c2151f3208(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__709e3ddacbcf322681536c9d4f2b7862d26b2ccb1fde77c5f70dff1fb2d786b9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__144346abf7a2c6c786889ad3638d66abf972abf34701eab01175689d3e14c74d(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f615ebe2c6a99e480d5cc80583dd1024ff0b766c4f3e8ce87f6a4f8d6a627e17(
    value: typing.Optional[typing.Union[CfnProvisioningTemplate.ProvisioningHookProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df7d9da4fb073d9d10200ca7eae4ef56af4e6316944ed07d2eb3a02f6a54ca36(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9662c4fc1f9f14bccfe451083d889f9579df91e99a3d1a5abfbbbeb1a125d58(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ced81513ed1957f556d89b411e507b5b7f3262f84b6619f9095c2291d19dc49(
    *,
    payload_version: typing.Optional[builtins.str] = None,
    target_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d7209c01d71f034e1ef126539867cffa0b106104e703cd3a3729b6a17941714(
    *,
    provisioning_role_arn: builtins.str,
    template_body: builtins.str,
    description: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    pre_provisioning_hook: typing.Optional[typing.Union[typing.Union[CfnProvisioningTemplate.ProvisioningHookProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    template_name: typing.Optional[builtins.str] = None,
    template_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b630339211723668b81832f3589aadce7d440e95a66ff9190e836691c68ad7f(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    log_level: builtins.str,
    target_name: builtins.str,
    target_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce57de0b056fe68d516ef24518dd87de2e21033a636385f3a350cc1ff6897b3c(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f198563162ee2533a2e8218b93d8c549d273ee2b89a7156db39fddfb82af7981(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4236a35b9182532e90fdf5fc6ca8887a821bc52797a4fd87022341b742e2fa7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__110b57edcb8597286159cf6b3bfdc4b13bf91793090681c58863143b68ca3399(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08be4bc56c419c342f967853f024b6173cb19a5ef182c8677881a595c83b4905(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7e369880521489546f5efd2fe7aa3cfb1018673c148bed120d073246cc2ea60(
    *,
    log_level: builtins.str,
    target_name: builtins.str,
    target_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4054758ae03efbb17f6b2c6ad952998ead4507c822323e611a58e9bbeb1c41c3(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    role_arn: builtins.str,
    credential_duration_seconds: typing.Optional[jsii.Number] = None,
    role_alias: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d71d161e9e9bc6ac5e0f16c3724d03afac9f415429209e5476bd64fa5ef8f1cd(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5581e88d9608f5b289626bd63d21b8d7e9ddf098f0a5246492253404fd1a22a1(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b393bdc20e656c9c176563207b0a1c34b4c0652f49ac4de2a4ac05a71f936de(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__727fc005a29230d173f1f2d17596fc79d75c2d2edcddd2661c8a3a4a389b5bd4(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6749616f338b8776ffd9a84feb62cad4f5bb9b8588bdebfaf1098825e1172c42(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0c438605fdb7e9c3c6f22adbd92eaf20aa767385dcaae9a850f9aecbc273774(
    *,
    role_arn: builtins.str,
    credential_duration_seconds: typing.Optional[jsii.Number] = None,
    role_alias: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8ffb853881117918a35da2335f7aef38c4008a0dd5e49175120e6709e74fcf6(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    frequency: builtins.str,
    target_check_names: typing.Sequence[builtins.str],
    day_of_month: typing.Optional[builtins.str] = None,
    day_of_week: typing.Optional[builtins.str] = None,
    scheduled_audit_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aaf95edf172678e79abec7cc2a9b7664a3623041c9f3a6c096c42ef6a6743c25(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32a2a9f2a819ccbb575e1143373a76dcc4b624254c9bbb8b11ac334cc1394e17(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bafac4cea46b5f4f9231b34e778b3425457145e62114e7c110d25a9422342ca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fee7a1476471d855c177f436f91235390e04d6cf7d1db5aef86e31812539662c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__014dcae2cd55e3f55a56c8a01c0a263c4d4bb1108affa0377bc4c2a0656b63ea(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5f0c93d37c8a0e6950ab61bf453182274c6e76bd7bcce5dfb8db949ea93d649(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbe3ef86bba09618390e255e2ad32b6b17abec05d9118942cd8fcddd779728bf(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__871f7d0b44f119299f626d51b5c9e680a070cad7039547802efc9f89e736ab23(
    *,
    frequency: builtins.str,
    target_check_names: typing.Sequence[builtins.str],
    day_of_month: typing.Optional[builtins.str] = None,
    day_of_week: typing.Optional[builtins.str] = None,
    scheduled_audit_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e74d94d5b8d8032c89022311703d61e4fa4ddb326df97b3048d408073a8ded9(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    additional_metrics_to_retain_v2: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union[CfnSecurityProfile.MetricToRetainProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]]] = None,
    alert_targets: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, typing.Union[typing.Union[CfnSecurityProfile.AlertTargetProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]]] = None,
    behaviors: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union[CfnSecurityProfile.BehaviorProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]]] = None,
    security_profile_description: typing.Optional[builtins.str] = None,
    security_profile_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    target_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68800bc12c54c432a21a17317b5350c63d970f0d4cdd71ed4c4f5018c130e89b(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96fbd27fd5e5b57dc866a7fb36df955f804896507348f5c8e717975aa1f6edcf(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81838e4cb995a14812d9167bfb161434ba5876279b4a108916c8d127f8aee908(
    value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnSecurityProfile.MetricToRetainProperty, _IResolvable_a771d0ef]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__534bb7b866e4fd89a7382da53a35f653c192a9994c0f8e7ae04f954f85fd9543(
    value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, typing.Union[CfnSecurityProfile.AlertTargetProperty, _IResolvable_a771d0ef]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07d2c3a6e0689893cd6d983125145987f7e1e3f31720fea49be136125fa67121(
    value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnSecurityProfile.BehaviorProperty, _IResolvable_a771d0ef]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab52e337fcc5a516da985319885e9ffacde52974163a3081cb356e300bc20fb1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffd0ab9152cb325752c9ee62d952c4c3da821a9e0f51644df36805109cf944a4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb167de690e8a57eedb0466e83db021e601ddbfb3051f43baf99cb381b9450a0(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8a5ad4dacd618ca3c7c6be010c4e22bccdd0161a33e4f7c1370d93fc651da64(
    *,
    alert_target_arn: builtins.str,
    role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75533297fe0f2abbe581a0a9c7bf702421ffa0a6b15f0d540d300ee34f834a72(
    *,
    comparison_operator: typing.Optional[builtins.str] = None,
    consecutive_datapoints_to_alarm: typing.Optional[jsii.Number] = None,
    consecutive_datapoints_to_clear: typing.Optional[jsii.Number] = None,
    duration_seconds: typing.Optional[jsii.Number] = None,
    ml_detection_config: typing.Optional[typing.Union[typing.Union[CfnSecurityProfile.MachineLearningDetectionConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    statistical_threshold: typing.Optional[typing.Union[typing.Union[CfnSecurityProfile.StatisticalThresholdProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    value: typing.Optional[typing.Union[typing.Union[CfnSecurityProfile.MetricValueProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c04941109d9114d090b7476b1e877559ef7fcd96a91277acc6cfa307b160890(
    *,
    name: builtins.str,
    criteria: typing.Optional[typing.Union[typing.Union[CfnSecurityProfile.BehaviorCriteriaProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    metric: typing.Optional[builtins.str] = None,
    metric_dimension: typing.Optional[typing.Union[typing.Union[CfnSecurityProfile.MetricDimensionProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    suppress_alerts: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a08b4e74a1b3543e60362e0381a167265581dde022cd0be74eec623c6bfa29d3(
    *,
    confidence_level: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85cc6baaa7d59e823c42454d05036fba22d7dca549414b1a3c4659dc7bdbdeb4(
    *,
    dimension_name: builtins.str,
    operator: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd32bd896a41dc36f4bfb9459ad6759cd299f4d197d45b71a5226e9bd8498807(
    *,
    metric: builtins.str,
    metric_dimension: typing.Optional[typing.Union[typing.Union[CfnSecurityProfile.MetricDimensionProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__275696e34aa4e1fcb3a125dc4396d389ae4d4bcf0b4ac0426b2bff6471d2a50c(
    *,
    cidrs: typing.Optional[typing.Sequence[builtins.str]] = None,
    count: typing.Optional[builtins.str] = None,
    number: typing.Optional[jsii.Number] = None,
    numbers: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[jsii.Number]]] = None,
    ports: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[jsii.Number]]] = None,
    strings: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54afe0874ad88601aaffef752e346f18136aad948496d9e0d6f23b50971e25c1(
    *,
    statistic: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b69de8ce9801a72b1fa4ee2a2d516f9f3ba8c2fb6b9f6148375d8f3cbefe41ba(
    *,
    additional_metrics_to_retain_v2: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union[CfnSecurityProfile.MetricToRetainProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]]] = None,
    alert_targets: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, typing.Union[typing.Union[CfnSecurityProfile.AlertTargetProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]]] = None,
    behaviors: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union[CfnSecurityProfile.BehaviorProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]]] = None,
    security_profile_description: typing.Optional[builtins.str] = None,
    security_profile_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    target_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__437d130d2e5bcd734f97792aa608823e3c3860cb3a614bb3f156c8b26038798b(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    attribute_payload: typing.Optional[typing.Union[typing.Union[CfnThing.AttributePayloadProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    thing_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ff5f03e628710104a6eff5df60151e38d1805fa533dce663677187c35fa94a3(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__085e897ceae95b566817862ad7f09901ac62e0f2baf87a5b13219eb0e8014d1d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71dfac710bca66dbe046744d860b33d688a2d19dae718dfcb09c24ab9b243a25(
    value: typing.Optional[typing.Union[CfnThing.AttributePayloadProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fea192f5ce9c6a101faee69bb6dfb9a8c23e3e4e6bfef26faa8adb0b2adb80e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__829580ffc78a180f74319e12b734c7fee35c1c9d273dbf57c9cf032199be1a9c(
    *,
    attributes: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, builtins.str]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63492ad3993b02e4f624709e8f068e8e97eb78d1c5c7aef3734e9f49504a944c(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    principal: builtins.str,
    thing_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26000d234a9d676f4e6405dccace4f69950254d43c43dfe3d40c56ae8a38502e(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__428a71070eb340e9562b190ed1dfdd886046a8ee5362886b72bf977347f637a4(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__034debeed37c02601562645621017cb8017d1638111d4f7b039b320cabdc8efa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fa53b0935f59bda6115a136d9142930984c3bef366afbaa85e450dc39655e0a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2eca5dd28b04f48619a1406080061cf8aef11a3b72c035a0aa223f28afa773e(
    *,
    principal: builtins.str,
    thing_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92aa4038efc687a706b388857c7d36a80effb18ea1a904224103609c6a458309(
    *,
    attribute_payload: typing.Optional[typing.Union[typing.Union[CfnThing.AttributePayloadProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    thing_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5780647966e58bc5841b9b1ab64d849ddbcf402f186d19833f5217f9d8952a66(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    topic_rule_payload: typing.Union[typing.Union[CfnTopicRule.TopicRulePayloadProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
    rule_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d315303b35312dc048d741c1cdc99f5fa2fcc70194c200bd81eb6bb855a1e5da(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57ced7e26a3e501a98010933d35438d0846a95eae5b076e028f69efc82b189cf(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08263eda82ec6be02e0ca1c2d9fc5febd21c271238f5ce5be2f717b32f1c7f64(
    value: typing.Union[CfnTopicRule.TopicRulePayloadProperty, _IResolvable_a771d0ef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__280863e549171664de08582d64da328a8846d2e60295b6a11c6ee8b7f0d625d8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25f08751c79228946ac85e1a8a9ae48ed7c71628118f968f4f6fca741c717413(
    *,
    cloudwatch_alarm: typing.Optional[typing.Union[typing.Union[CfnTopicRule.CloudwatchAlarmActionProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    cloudwatch_logs: typing.Optional[typing.Union[typing.Union[CfnTopicRule.CloudwatchLogsActionProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    cloudwatch_metric: typing.Optional[typing.Union[typing.Union[CfnTopicRule.CloudwatchMetricActionProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    dynamo_db: typing.Optional[typing.Union[typing.Union[CfnTopicRule.DynamoDBActionProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    dynamo_d_bv2: typing.Optional[typing.Union[typing.Union[CfnTopicRule.DynamoDBv2ActionProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    elasticsearch: typing.Optional[typing.Union[typing.Union[CfnTopicRule.ElasticsearchActionProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    firehose: typing.Optional[typing.Union[typing.Union[CfnTopicRule.FirehoseActionProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    http: typing.Optional[typing.Union[typing.Union[CfnTopicRule.HttpActionProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    iot_analytics: typing.Optional[typing.Union[typing.Union[CfnTopicRule.IotAnalyticsActionProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    iot_events: typing.Optional[typing.Union[typing.Union[CfnTopicRule.IotEventsActionProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    iot_site_wise: typing.Optional[typing.Union[typing.Union[CfnTopicRule.IotSiteWiseActionProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    kafka: typing.Optional[typing.Union[typing.Union[CfnTopicRule.KafkaActionProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    kinesis: typing.Optional[typing.Union[typing.Union[CfnTopicRule.KinesisActionProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    lambda_: typing.Optional[typing.Union[typing.Union[CfnTopicRule.LambdaActionProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    location: typing.Optional[typing.Union[typing.Union[CfnTopicRule.LocationActionProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    open_search: typing.Optional[typing.Union[typing.Union[CfnTopicRule.OpenSearchActionProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    republish: typing.Optional[typing.Union[typing.Union[CfnTopicRule.RepublishActionProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    s3: typing.Optional[typing.Union[typing.Union[CfnTopicRule.S3ActionProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    sns: typing.Optional[typing.Union[typing.Union[CfnTopicRule.SnsActionProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    sqs: typing.Optional[typing.Union[typing.Union[CfnTopicRule.SqsActionProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    step_functions: typing.Optional[typing.Union[typing.Union[CfnTopicRule.StepFunctionsActionProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    timestream: typing.Optional[typing.Union[typing.Union[CfnTopicRule.TimestreamActionProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e4e2188ad106b42cba2e456e1ba5b0c14164d9ef67bf367d0aa1c7ae6e5c875(
    *,
    time_in_seconds: builtins.str,
    offset_in_nanos: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__daf3af14341e848695e62e242ea9b22ce5e9ba2912dee321d72c47666c1422d6(
    *,
    timestamp: typing.Union[typing.Union[CfnTopicRule.AssetPropertyTimestampProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
    value: typing.Union[typing.Union[CfnTopicRule.AssetPropertyVariantProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
    quality: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__128f95606291f57004f370101538fc181a4a4914357acc2a5f3b871cbb5051f7(
    *,
    boolean_value: typing.Optional[builtins.str] = None,
    double_value: typing.Optional[builtins.str] = None,
    integer_value: typing.Optional[builtins.str] = None,
    string_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8141e369458dbf936fb0c57a028c2436be2aa10f71ca1fd66656be906b24963d(
    *,
    alarm_name: builtins.str,
    role_arn: builtins.str,
    state_reason: builtins.str,
    state_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ade46dcee982968d97e8f07e9e4e8e0a87fa367a9d7b0ce01528af365f2501d(
    *,
    log_group_name: builtins.str,
    role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__670f7ba2a7c5acc73f882a1ee97c0fbbb67d3c3e195fb984e0ec162c5291bab6(
    *,
    metric_name: builtins.str,
    metric_namespace: builtins.str,
    metric_unit: builtins.str,
    metric_value: builtins.str,
    role_arn: builtins.str,
    metric_timestamp: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae106cdfaa3d9b225f3f627378befde8d966ae3099d658baaa9b87145a02ba51(
    *,
    hash_key_field: builtins.str,
    hash_key_value: builtins.str,
    role_arn: builtins.str,
    table_name: builtins.str,
    hash_key_type: typing.Optional[builtins.str] = None,
    payload_field: typing.Optional[builtins.str] = None,
    range_key_field: typing.Optional[builtins.str] = None,
    range_key_type: typing.Optional[builtins.str] = None,
    range_key_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__075d4c8ae4560d1997fa8eaaeab7db387c19d9b648d6b69b6bfb1eb65b47c30e(
    *,
    put_item: typing.Optional[typing.Union[typing.Union[CfnTopicRule.PutItemInputProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9332bc16170a0b14a81bfb8d35bbceada490bfe002cd9a75edfd9bd085c9ca06(
    *,
    endpoint: builtins.str,
    id: builtins.str,
    index: builtins.str,
    role_arn: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__964fe8e07ebfd82428752c15d9c27c5ef449220f0760f699afdb4d9d2e0df872(
    *,
    delivery_stream_name: builtins.str,
    role_arn: builtins.str,
    batch_mode: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    separator: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04569b4551c74ddcbfb1c766475d3c7aeebc6f103dab739f79b04c260e29598d(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__422489f82cd60ea1751702250bbe50041a4bdb9fea56de0ef2cd3cb5509fb54d(
    *,
    url: builtins.str,
    auth: typing.Optional[typing.Union[typing.Union[CfnTopicRule.HttpAuthorizationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    confirmation_url: typing.Optional[builtins.str] = None,
    headers: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union[CfnTopicRule.HttpActionHeaderProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8201e4078dc4255867c7807fd2c90b8849b63044deba6157801bf278e2bf686(
    *,
    sigv4: typing.Optional[typing.Union[typing.Union[CfnTopicRule.SigV4AuthorizationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d201cf9c7748acbb339ae03d069d7a07dc1fb07c23838f7ca1b618f27375697b(
    *,
    channel_name: builtins.str,
    role_arn: builtins.str,
    batch_mode: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7c70a453b926326945287307b0539dd9b3cf53583d2870eaa5ee099a88c7c2e(
    *,
    input_name: builtins.str,
    role_arn: builtins.str,
    batch_mode: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    message_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b272cfa6ee5519c1547d4e5459e0dd8e5c4b291d28984e95dbd422204707b751(
    *,
    put_asset_property_value_entries: typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union[CfnTopicRule.PutAssetPropertyValueEntryProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]],
    role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__955d06c2844189c8ea86b26203fff54ce63ce3b58df2dd2c4b115ddaa856859a(
    *,
    client_properties: typing.Union[_IResolvable_a771d0ef, typing.Mapping[builtins.str, builtins.str]],
    destination_arn: builtins.str,
    topic: builtins.str,
    key: typing.Optional[builtins.str] = None,
    partition: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__690b42f1fbc9f7d8e0177522fcc8b685f8f51de31efe1e79e34849eb7ddaa66c(
    *,
    role_arn: builtins.str,
    stream_name: builtins.str,
    partition_key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__512b80aa733d6d9b7a41a403040f6f160661dfbfff30438983ed9b7d28e415f3(
    *,
    function_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c313dcd38d2393ca4a812109e774b48eeee5d674fe3d54bd7db53491e2620f5(
    *,
    device_id: builtins.str,
    latitude: builtins.str,
    longitude: builtins.str,
    role_arn: builtins.str,
    tracker_name: builtins.str,
    timestamp: typing.Optional[typing.Union[_IResolvable_a771d0ef, datetime.datetime]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65340f3d0af5956ac0dce9020bcc9191a17f60daecdac7e09bee689eddf1449c(
    *,
    endpoint: builtins.str,
    id: builtins.str,
    index: builtins.str,
    role_arn: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4e9228ec16fc3cc0f064ab7dd66bd0f3d7f4653676d60c0781886ed1587cbd5(
    *,
    property_values: typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union[CfnTopicRule.AssetPropertyValueProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]],
    asset_id: typing.Optional[builtins.str] = None,
    entry_id: typing.Optional[builtins.str] = None,
    property_alias: typing.Optional[builtins.str] = None,
    property_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58eccbc1fc25d8820c01d9ee3e094684fecab052f42c577dee96d3e18a98c9ef(
    *,
    table_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04c619e1c6f2b508d2200f1c3ca471be43eb59efcc425565d1bc2aa4a11bd705(
    *,
    content_type: typing.Optional[builtins.str] = None,
    correlation_data: typing.Optional[builtins.str] = None,
    message_expiry: typing.Optional[builtins.str] = None,
    payload_format_indicator: typing.Optional[builtins.str] = None,
    response_topic: typing.Optional[builtins.str] = None,
    user_properties: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union[CfnTopicRule.UserPropertyProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e064278f65540044d20c4fd2755bb7eaba09b540c20dd6cee0ec29b0ab48b66(
    *,
    role_arn: builtins.str,
    topic: builtins.str,
    headers: typing.Optional[typing.Union[typing.Union[CfnTopicRule.RepublishActionHeadersProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    qos: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15a487dbc8102d292467a082644bd2cad01a57e1882aa96e161feef83e534360(
    *,
    bucket_name: builtins.str,
    key: builtins.str,
    role_arn: builtins.str,
    canned_acl: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06f8ca969f034928394d72825d8b8a6862353576d257b9fd1fe8da367be79d1f(
    *,
    role_arn: builtins.str,
    service_name: builtins.str,
    signing_region: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3666ce516fcd9093adfa8ddb1bbbab5817f9d177e357f95c9999aa74775607bd(
    *,
    role_arn: builtins.str,
    target_arn: builtins.str,
    message_format: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d0bdd7a3c868cbcfd49e69c4c54828c76ad353bf40ebcf49ab1db3cb1de071a(
    *,
    queue_url: builtins.str,
    role_arn: builtins.str,
    use_base64: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2301c2177af5e7eb8bf56c1a0a964dfbc212bc2095e214260f18bbf749d63886(
    *,
    role_arn: builtins.str,
    state_machine_name: builtins.str,
    execution_name_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed3994d04f9eba52d292f3a3d33320b3b00a9f9fc772c0a3d07b7afbf79abd25(
    *,
    value: builtins.str,
    unit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e584d87e7884bc9c63e8d8adf4f753e42a05b87e545f3ede17207a61245124a(
    *,
    database_name: builtins.str,
    dimensions: typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union[CfnTopicRule.TimestreamDimensionProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]],
    role_arn: builtins.str,
    table_name: builtins.str,
    timestamp: typing.Optional[typing.Union[typing.Union[CfnTopicRule.TimestreamTimestampProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91a2bfa87f2b240294575893bf17aa3d805ccea7c95b05b5dc0da866c046c55e(
    *,
    name: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1d4e9ad3bc192f1845a6974505d3611853ac94cc6f64175b7f15fa79000c9c8(
    *,
    unit: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81c1d417456e00c2a00cc1e1000ee721904e21e78d04148e1f18887da57f29d7(
    *,
    actions: typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union[CfnTopicRule.ActionProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]],
    sql: builtins.str,
    aws_iot_sql_version: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    error_action: typing.Optional[typing.Union[typing.Union[CfnTopicRule.ActionProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    rule_disabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7044584b09c908ca69d5398061943b6b496241675d44cbdf422c555763e3de3(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a89d7bdf9e78b54d5052730161337b384713df76d01cf480264c6790de25f9ea(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    http_url_properties: typing.Optional[typing.Union[typing.Union[CfnTopicRuleDestination.HttpUrlDestinationSummaryProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    status: typing.Optional[builtins.str] = None,
    vpc_properties: typing.Optional[typing.Union[typing.Union[CfnTopicRuleDestination.VpcDestinationPropertiesProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49028cbd79b31a1c1f8d1160a6d6afc41b0c5a1a3b24f0780806b6e25cb98532(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__472aae12c565c92d3d291369fffbd3d72084ac126081b860d9cff80afff0a222(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d2831eca5011fa45238a8550f9feb56ffa9bd2860b71dac4438d68745757980(
    value: typing.Optional[typing.Union[CfnTopicRuleDestination.HttpUrlDestinationSummaryProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6c1cee44fa333ab24f9b08600a6d000e003f320453a441b5c06a3ad5036c466(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76259c8bc5a91a67fdfa66b8f1123cfaa50575f8121e35a75cf990270a6e2f04(
    value: typing.Optional[typing.Union[CfnTopicRuleDestination.VpcDestinationPropertiesProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f07deaf20816db33dcac88fe2ff231f79a29e95e54c16d6ab60e84bee02029ce(
    *,
    confirmation_url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28aa9f28bd1fef7e858705ebf6da6f102c1153e54fb5725da312213735d50ebb(
    *,
    role_arn: typing.Optional[builtins.str] = None,
    security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    vpc_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb816759350a5c76754a0ccf63c48ce6c58d259ebc3598820b0df960c3cb4b8c(
    *,
    http_url_properties: typing.Optional[typing.Union[typing.Union[CfnTopicRuleDestination.HttpUrlDestinationSummaryProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    status: typing.Optional[builtins.str] = None,
    vpc_properties: typing.Optional[typing.Union[typing.Union[CfnTopicRuleDestination.VpcDestinationPropertiesProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55f9095b7da2c51028e09eab4070f6f5c19d89372748e0818ea666260fb7a0fe(
    *,
    topic_rule_payload: typing.Union[typing.Union[CfnTopicRule.TopicRulePayloadProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
    rule_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__992fc37ab73c0cf93c297558ddadf0ad93320669301318a6864343134effbf96(
    topic_rule: ITopicRule,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb0c55f92d065b5aee0f2c2f0c5e55d4a84849ee435c7ca913b981c9c566b877(
    sql: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ac2166f7d917030033ecde06814c9225b3fac8b7fc538c52de58a6b4a8c5bed(
    sql: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04b433d003522fac5136f25b9abb3f0bf205eae563cd06c951dc6d09f50971c8(
    sql: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a64f871a74e656d723c0d990bed48a5dfd7de0ff5366e3b00534ad53236578d(
    scope: _constructs_77d1e7e8.Construct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5aa54034018f3b129824b87c02de32e6d1f6a094164becba9c9488c679d7af1e(
    *,
    aws_iot_sql_version: builtins.str,
    sql: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1e1f7a13368fc4d47d88f55b877035d9782a55600a0632e60d6cb31a97d03a7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    sql: IotSql,
    actions: typing.Optional[typing.Sequence[IAction]] = None,
    description: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[builtins.bool] = None,
    error_action: typing.Optional[IAction] = None,
    topic_rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c41e62a57f74f91db099c49a0a62201ca9d32bf16a4005a62a04d2ba26bb3746(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    topic_rule_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfaa7a8aeddc4c10cfeda3a8589d52668ea589935ddc9aa8ee0ba1d9db5aa583(
    action: IAction,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c48d275314c249b167a6a70bbba214a533770e8feb6e3a44b1748e24d6d3d10(
    *,
    sql: IotSql,
    actions: typing.Optional[typing.Sequence[IAction]] = None,
    description: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[builtins.bool] = None,
    error_action: typing.Optional[IAction] = None,
    topic_rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

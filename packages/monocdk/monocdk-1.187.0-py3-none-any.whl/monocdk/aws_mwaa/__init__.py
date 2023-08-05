'''
# AWS::MWAA Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import monocdk as mwaa
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for MWAA construct libraries](https://constructs.dev/search?q=mwaa)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::MWAA resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_MWAA.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::MWAA](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_MWAA.html).

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

from .._jsii import *

from .. import (
    CfnResource as _CfnResource_e0a482dc,
    Construct as _Construct_e78e779f,
    IInspectable as _IInspectable_82c04a63,
    IResolvable as _IResolvable_a771d0ef,
    TagManager as _TagManager_0b7ab120,
    TreeInspector as _TreeInspector_1cd1894e,
)


@jsii.implements(_IInspectable_82c04a63)
class CfnEnvironment(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_mwaa.CfnEnvironment",
):
    '''A CloudFormation ``AWS::MWAA::Environment``.

    The ``AWS::MWAA::Environment`` resource creates an Amazon Managed Workflows for Apache Airflow (MWAA) environment.

    :cloudformationResource: AWS::MWAA::Environment
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_mwaa as mwaa
        
        # airflow_configuration_options: Any
        # tags: Any
        
        cfn_environment = mwaa.CfnEnvironment(self, "MyCfnEnvironment",
            name="name",
        
            # the properties below are optional
            airflow_configuration_options=airflow_configuration_options,
            airflow_version="airflowVersion",
            dag_s3_path="dagS3Path",
            environment_class="environmentClass",
            execution_role_arn="executionRoleArn",
            kms_key="kmsKey",
            logging_configuration=mwaa.CfnEnvironment.LoggingConfigurationProperty(
                dag_processing_logs=mwaa.CfnEnvironment.ModuleLoggingConfigurationProperty(
                    cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                    enabled=False,
                    log_level="logLevel"
                ),
                scheduler_logs=mwaa.CfnEnvironment.ModuleLoggingConfigurationProperty(
                    cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                    enabled=False,
                    log_level="logLevel"
                ),
                task_logs=mwaa.CfnEnvironment.ModuleLoggingConfigurationProperty(
                    cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                    enabled=False,
                    log_level="logLevel"
                ),
                webserver_logs=mwaa.CfnEnvironment.ModuleLoggingConfigurationProperty(
                    cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                    enabled=False,
                    log_level="logLevel"
                ),
                worker_logs=mwaa.CfnEnvironment.ModuleLoggingConfigurationProperty(
                    cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                    enabled=False,
                    log_level="logLevel"
                )
            ),
            max_workers=123,
            min_workers=123,
            network_configuration=mwaa.CfnEnvironment.NetworkConfigurationProperty(
                security_group_ids=["securityGroupIds"],
                subnet_ids=["subnetIds"]
            ),
            plugins_s3_object_version="pluginsS3ObjectVersion",
            plugins_s3_path="pluginsS3Path",
            requirements_s3_object_version="requirementsS3ObjectVersion",
            requirements_s3_path="requirementsS3Path",
            schedulers=123,
            source_bucket_arn="sourceBucketArn",
            tags=tags,
            webserver_access_mode="webserverAccessMode",
            weekly_maintenance_window_start="weeklyMaintenanceWindowStart"
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        name: builtins.str,
        airflow_configuration_options: typing.Any = None,
        airflow_version: typing.Optional[builtins.str] = None,
        dag_s3_path: typing.Optional[builtins.str] = None,
        environment_class: typing.Optional[builtins.str] = None,
        execution_role_arn: typing.Optional[builtins.str] = None,
        kms_key: typing.Optional[builtins.str] = None,
        logging_configuration: typing.Optional[typing.Union[typing.Union["CfnEnvironment.LoggingConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        max_workers: typing.Optional[jsii.Number] = None,
        min_workers: typing.Optional[jsii.Number] = None,
        network_configuration: typing.Optional[typing.Union[typing.Union["CfnEnvironment.NetworkConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        plugins_s3_object_version: typing.Optional[builtins.str] = None,
        plugins_s3_path: typing.Optional[builtins.str] = None,
        requirements_s3_object_version: typing.Optional[builtins.str] = None,
        requirements_s3_path: typing.Optional[builtins.str] = None,
        schedulers: typing.Optional[jsii.Number] = None,
        source_bucket_arn: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
        webserver_access_mode: typing.Optional[builtins.str] = None,
        weekly_maintenance_window_start: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::MWAA::Environment``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: The name of your Amazon MWAA environment.
        :param airflow_configuration_options: A list of key-value pairs containing the Airflow configuration options for your environment. For example, ``core.default_timezone: utc`` . To learn more, see `Apache Airflow configuration options <https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-env-variables.html>`_ .
        :param airflow_version: The version of Apache Airflow to use for the environment. If no value is specified, defaults to the latest version. Valid values: ``2.0.2`` , ``1.10.12`` , ``2.2.2`` .
        :param dag_s3_path: The relative path to the DAGs folder on your Amazon S3 bucket. For example, ``dags`` . To learn more, see `Adding or updating DAGs <https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-folder.html>`_ .
        :param environment_class: The environment class type. Valid values: ``mw1.small`` , ``mw1.medium`` , ``mw1.large`` . To learn more, see `Amazon MWAA environment class <https://docs.aws.amazon.com/mwaa/latest/userguide/environment-class.html>`_ .
        :param execution_role_arn: The Amazon Resource Name (ARN) of the execution role in IAM that allows MWAA to access AWS resources in your environment. For example, ``arn:aws:iam::123456789:role/my-execution-role`` . To learn more, see `Amazon MWAA Execution role <https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-create-role.html>`_ .
        :param kms_key: The AWS Key Management Service (KMS) key to encrypt and decrypt the data in your environment. You can use an AWS KMS key managed by MWAA, or a customer-managed KMS key (advanced).
        :param logging_configuration: The Apache Airflow logs being sent to CloudWatch Logs: ``DagProcessingLogs`` , ``SchedulerLogs`` , ``TaskLogs`` , ``WebserverLogs`` , ``WorkerLogs`` .
        :param max_workers: The maximum number of workers that you want to run in your environment. MWAA scales the number of Apache Airflow workers up to the number you specify in the ``MaxWorkers`` field. For example, ``20`` . When there are no more tasks running, and no more in the queue, MWAA disposes of the extra workers leaving the one worker that is included with your environment, or the number you specify in ``MinWorkers`` .
        :param min_workers: The minimum number of workers that you want to run in your environment. MWAA scales the number of Apache Airflow workers up to the number you specify in the ``MaxWorkers`` field. When there are no more tasks running, and no more in the queue, MWAA disposes of the extra workers leaving the worker count you specify in the ``MinWorkers`` field. For example, ``2`` .
        :param network_configuration: The VPC networking components used to secure and enable network traffic between the AWS resources for your environment. To learn more, see `About networking on Amazon MWAA <https://docs.aws.amazon.com/mwaa/latest/userguide/networking-about.html>`_ .
        :param plugins_s3_object_version: The version of the plugins.zip file on your Amazon S3 bucket. To learn more, see `Installing custom plugins <https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-import-plugins.html>`_ .
        :param plugins_s3_path: The relative path to the ``plugins.zip`` file on your Amazon S3 bucket. For example, ``plugins.zip`` . To learn more, see `Installing custom plugins <https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-import-plugins.html>`_ .
        :param requirements_s3_object_version: The version of the requirements.txt file on your Amazon S3 bucket. To learn more, see `Installing Python dependencies <https://docs.aws.amazon.com/mwaa/latest/userguide/working-dags-dependencies.html>`_ .
        :param requirements_s3_path: The relative path to the ``requirements.txt`` file on your Amazon S3 bucket. For example, ``requirements.txt`` . To learn more, see `Installing Python dependencies <https://docs.aws.amazon.com/mwaa/latest/userguide/working-dags-dependencies.html>`_ .
        :param schedulers: The number of schedulers that you want to run in your environment. Valid values:. - *v2.0.2* - Accepts between 2 to 5. Defaults to 2. - *v1.10.12* - Accepts 1.
        :param source_bucket_arn: The Amazon Resource Name (ARN) of the Amazon S3 bucket where your DAG code and supporting files are stored. For example, ``arn:aws:s3:::my-airflow-bucket-unique-name`` . To learn more, see `Create an Amazon S3 bucket for Amazon MWAA <https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-s3-bucket.html>`_ .
        :param tags: The key-value tag pairs associated to your environment. For example, ``"Environment": "Staging"`` . To learn more, see `Tagging <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .
        :param webserver_access_mode: The Apache Airflow *Web server* access mode. To learn more, see `Apache Airflow access modes <https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-networking.html>`_ . Valid values: ``PRIVATE_ONLY`` or ``PUBLIC_ONLY`` .
        :param weekly_maintenance_window_start: The day and time of the week to start weekly maintenance updates of your environment in the following format: ``DAY:HH:MM`` . For example: ``TUE:03:30`` . You can specify a start time in 30 minute increments only. Supported input includes the following: - MON|TUE|WED|THU|FRI|SAT|SUN:([01]\\d|2[0-3]):(00|30)
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__470828095b91afb3a680b6d2abb51b3a7c3db448123609c29b3cf4eda2d34c35)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEnvironmentProps(
            name=name,
            airflow_configuration_options=airflow_configuration_options,
            airflow_version=airflow_version,
            dag_s3_path=dag_s3_path,
            environment_class=environment_class,
            execution_role_arn=execution_role_arn,
            kms_key=kms_key,
            logging_configuration=logging_configuration,
            max_workers=max_workers,
            min_workers=min_workers,
            network_configuration=network_configuration,
            plugins_s3_object_version=plugins_s3_object_version,
            plugins_s3_path=plugins_s3_path,
            requirements_s3_object_version=requirements_s3_object_version,
            requirements_s3_path=requirements_s3_path,
            schedulers=schedulers,
            source_bucket_arn=source_bucket_arn,
            tags=tags,
            webserver_access_mode=webserver_access_mode,
            weekly_maintenance_window_start=weekly_maintenance_window_start,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5422cab040c438602a2333ec2516e0bca634c7fb7376aabc5db230d6230d56b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__427c507a35ef4cbf07937a63a5637c52bc8d33a1a506488b5711df4f3d98b2dd)
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
        '''The ARN for the Amazon MWAA environment.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrLoggingConfigurationDagProcessingLogsCloudWatchLogGroupArn")
    def attr_logging_configuration_dag_processing_logs_cloud_watch_log_group_arn(
        self,
    ) -> builtins.str:
        '''The ARN for the CloudWatch Logs group where the Apache Airflow DAG processing logs are published.

        :cloudformationAttribute: LoggingConfiguration.DagProcessingLogs.CloudWatchLogGroupArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLoggingConfigurationDagProcessingLogsCloudWatchLogGroupArn"))

    @builtins.property
    @jsii.member(jsii_name="attrLoggingConfigurationSchedulerLogsCloudWatchLogGroupArn")
    def attr_logging_configuration_scheduler_logs_cloud_watch_log_group_arn(
        self,
    ) -> builtins.str:
        '''The ARN for the CloudWatch Logs group where the Apache Airflow Scheduler logs are published.

        :cloudformationAttribute: LoggingConfiguration.SchedulerLogs.CloudWatchLogGroupArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLoggingConfigurationSchedulerLogsCloudWatchLogGroupArn"))

    @builtins.property
    @jsii.member(jsii_name="attrLoggingConfigurationTaskLogsCloudWatchLogGroupArn")
    def attr_logging_configuration_task_logs_cloud_watch_log_group_arn(
        self,
    ) -> builtins.str:
        '''The ARN for the CloudWatch Logs group where the Apache Airflow task logs are published.

        :cloudformationAttribute: LoggingConfiguration.TaskLogs.CloudWatchLogGroupArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLoggingConfigurationTaskLogsCloudWatchLogGroupArn"))

    @builtins.property
    @jsii.member(jsii_name="attrLoggingConfigurationWebserverLogsCloudWatchLogGroupArn")
    def attr_logging_configuration_webserver_logs_cloud_watch_log_group_arn(
        self,
    ) -> builtins.str:
        '''The ARN for the CloudWatch Logs group where the Apache Airflow Web server logs are published.

        :cloudformationAttribute: LoggingConfiguration.WebserverLogs.CloudWatchLogGroupArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLoggingConfigurationWebserverLogsCloudWatchLogGroupArn"))

    @builtins.property
    @jsii.member(jsii_name="attrLoggingConfigurationWorkerLogsCloudWatchLogGroupArn")
    def attr_logging_configuration_worker_logs_cloud_watch_log_group_arn(
        self,
    ) -> builtins.str:
        '''The ARN for the CloudWatch Logs group where the Apache Airflow Worker logs are published.

        :cloudformationAttribute: LoggingConfiguration.WorkerLogs.CloudWatchLogGroupArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLoggingConfigurationWorkerLogsCloudWatchLogGroupArn"))

    @builtins.property
    @jsii.member(jsii_name="attrWebserverUrl")
    def attr_webserver_url(self) -> builtins.str:
        '''The URL of your Apache Airflow UI.

        :cloudformationAttribute: WebserverUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrWebserverUrl"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''The key-value tag pairs associated to your environment.

        For example, ``"Environment": "Staging"`` . To learn more, see `Tagging <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="airflowConfigurationOptions")
    def airflow_configuration_options(self) -> typing.Any:
        '''A list of key-value pairs containing the Airflow configuration options for your environment.

        For example, ``core.default_timezone: utc`` . To learn more, see `Apache Airflow configuration options <https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-env-variables.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-airflowconfigurationoptions
        '''
        return typing.cast(typing.Any, jsii.get(self, "airflowConfigurationOptions"))

    @airflow_configuration_options.setter
    def airflow_configuration_options(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05ac9db5fda75fc618028e29b14b46f30a1b5c5c294b2c4c192a6fdfa1b58e9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "airflowConfigurationOptions", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of your Amazon MWAA environment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10a22ed6817a79463af7bd431f70f4734ff3ff3902abbe4362d59c9bc6015599)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="airflowVersion")
    def airflow_version(self) -> typing.Optional[builtins.str]:
        '''The version of Apache Airflow to use for the environment.

        If no value is specified, defaults to the latest version. Valid values: ``2.0.2`` , ``1.10.12`` , ``2.2.2`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-airflowversion
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "airflowVersion"))

    @airflow_version.setter
    def airflow_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f966da09774892771a8e99c24c01f9e489786294eeb2c7c6052ebc510fc5fefb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "airflowVersion", value)

    @builtins.property
    @jsii.member(jsii_name="dagS3Path")
    def dag_s3_path(self) -> typing.Optional[builtins.str]:
        '''The relative path to the DAGs folder on your Amazon S3 bucket.

        For example, ``dags`` . To learn more, see `Adding or updating DAGs <https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-folder.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-dags3path
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dagS3Path"))

    @dag_s3_path.setter
    def dag_s3_path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f22dadcba5bba6af9ecb79706dc01ff7a78aea0f54305244bbfd78058c2a134)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dagS3Path", value)

    @builtins.property
    @jsii.member(jsii_name="environmentClass")
    def environment_class(self) -> typing.Optional[builtins.str]:
        '''The environment class type.

        Valid values: ``mw1.small`` , ``mw1.medium`` , ``mw1.large`` . To learn more, see `Amazon MWAA environment class <https://docs.aws.amazon.com/mwaa/latest/userguide/environment-class.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-environmentclass
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environmentClass"))

    @environment_class.setter
    def environment_class(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b41ebc1c1325dd4684c914d0e62d471c2a70dd830ee7bed91fd8325707bdf61a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentClass", value)

    @builtins.property
    @jsii.member(jsii_name="executionRoleArn")
    def execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the execution role in IAM that allows MWAA to access AWS resources in your environment.

        For example, ``arn:aws:iam::123456789:role/my-execution-role`` . To learn more, see `Amazon MWAA Execution role <https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-create-role.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-executionrolearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionRoleArn"))

    @execution_role_arn.setter
    def execution_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4311e19671686d923a5c23f3d8d631b40051216addd2240840223e55f14ebe66)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKey")
    def kms_key(self) -> typing.Optional[builtins.str]:
        '''The AWS Key Management Service (KMS) key to encrypt and decrypt the data in your environment.

        You can use an AWS KMS key managed by MWAA, or a customer-managed KMS key (advanced).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-kmskey
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKey"))

    @kms_key.setter
    def kms_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af57b04ee04aa6ac912321585c71e01cb73008abb3586f7a4b1194e478efa9ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKey", value)

    @builtins.property
    @jsii.member(jsii_name="loggingConfiguration")
    def logging_configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnEnvironment.LoggingConfigurationProperty", _IResolvable_a771d0ef]]:
        '''The Apache Airflow logs being sent to CloudWatch Logs: ``DagProcessingLogs`` , ``SchedulerLogs`` , ``TaskLogs`` , ``WebserverLogs`` , ``WorkerLogs`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-loggingconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union["CfnEnvironment.LoggingConfigurationProperty", _IResolvable_a771d0ef]], jsii.get(self, "loggingConfiguration"))

    @logging_configuration.setter
    def logging_configuration(
        self,
        value: typing.Optional[typing.Union["CfnEnvironment.LoggingConfigurationProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37f8b1b0ae6ffed44277364161d1f86d58367ecb5970a4cb6624d272bb98c572)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loggingConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="maxWorkers")
    def max_workers(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of workers that you want to run in your environment.

        MWAA scales the number of Apache Airflow workers up to the number you specify in the ``MaxWorkers`` field. For example, ``20`` . When there are no more tasks running, and no more in the queue, MWAA disposes of the extra workers leaving the one worker that is included with your environment, or the number you specify in ``MinWorkers`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-maxworkers
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxWorkers"))

    @max_workers.setter
    def max_workers(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d59d82588fb7f3b275babec4165ca9601097d1cebde0447e519907cb80c6446)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxWorkers", value)

    @builtins.property
    @jsii.member(jsii_name="minWorkers")
    def min_workers(self) -> typing.Optional[jsii.Number]:
        '''The minimum number of workers that you want to run in your environment.

        MWAA scales the number of Apache Airflow workers up to the number you specify in the ``MaxWorkers`` field. When there are no more tasks running, and no more in the queue, MWAA disposes of the extra workers leaving the worker count you specify in the ``MinWorkers`` field. For example, ``2`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-minworkers
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minWorkers"))

    @min_workers.setter
    def min_workers(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1258587e49cdc9830166a04720beee61b83a48578b0e83facf0c707e6382691f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minWorkers", value)

    @builtins.property
    @jsii.member(jsii_name="networkConfiguration")
    def network_configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnEnvironment.NetworkConfigurationProperty", _IResolvable_a771d0ef]]:
        '''The VPC networking components used to secure and enable network traffic between the AWS resources for your environment.

        To learn more, see `About networking on Amazon MWAA <https://docs.aws.amazon.com/mwaa/latest/userguide/networking-about.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-networkconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union["CfnEnvironment.NetworkConfigurationProperty", _IResolvable_a771d0ef]], jsii.get(self, "networkConfiguration"))

    @network_configuration.setter
    def network_configuration(
        self,
        value: typing.Optional[typing.Union["CfnEnvironment.NetworkConfigurationProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7db5bc459e6b21e4387894746807a9dbfbec37245713ba80a68e08284b143de2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="pluginsS3ObjectVersion")
    def plugins_s3_object_version(self) -> typing.Optional[builtins.str]:
        '''The version of the plugins.zip file on your Amazon S3 bucket. To learn more, see `Installing custom plugins <https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-import-plugins.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-pluginss3objectversion
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pluginsS3ObjectVersion"))

    @plugins_s3_object_version.setter
    def plugins_s3_object_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1778a4a6a5ff2b8815182049512859e4314a4c3e749a324b468bfa6d296a90bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pluginsS3ObjectVersion", value)

    @builtins.property
    @jsii.member(jsii_name="pluginsS3Path")
    def plugins_s3_path(self) -> typing.Optional[builtins.str]:
        '''The relative path to the ``plugins.zip`` file on your Amazon S3 bucket. For example, ``plugins.zip`` . To learn more, see `Installing custom plugins <https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-import-plugins.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-pluginss3path
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pluginsS3Path"))

    @plugins_s3_path.setter
    def plugins_s3_path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04bf9fbc29749ccb6deacd0db0efa6bb1626d913f3c0e178fa981bb94ec77bae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pluginsS3Path", value)

    @builtins.property
    @jsii.member(jsii_name="requirementsS3ObjectVersion")
    def requirements_s3_object_version(self) -> typing.Optional[builtins.str]:
        '''The version of the requirements.txt file on your Amazon S3 bucket. To learn more, see `Installing Python dependencies <https://docs.aws.amazon.com/mwaa/latest/userguide/working-dags-dependencies.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-requirementss3objectversion
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "requirementsS3ObjectVersion"))

    @requirements_s3_object_version.setter
    def requirements_s3_object_version(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28ce3289b4ec54728fbe269e260b9079a44a80e91ea429196444b94d1912fe98)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requirementsS3ObjectVersion", value)

    @builtins.property
    @jsii.member(jsii_name="requirementsS3Path")
    def requirements_s3_path(self) -> typing.Optional[builtins.str]:
        '''The relative path to the ``requirements.txt`` file on your Amazon S3 bucket. For example, ``requirements.txt`` . To learn more, see `Installing Python dependencies <https://docs.aws.amazon.com/mwaa/latest/userguide/working-dags-dependencies.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-requirementss3path
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "requirementsS3Path"))

    @requirements_s3_path.setter
    def requirements_s3_path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd9cdb7bbe8c59536e4aaf94f40342b100f02011531786712f22572e9d368869)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requirementsS3Path", value)

    @builtins.property
    @jsii.member(jsii_name="schedulers")
    def schedulers(self) -> typing.Optional[jsii.Number]:
        '''The number of schedulers that you want to run in your environment. Valid values:.

        - *v2.0.2* - Accepts between 2 to 5. Defaults to 2.
        - *v1.10.12* - Accepts 1.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-schedulers
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "schedulers"))

    @schedulers.setter
    def schedulers(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7f23ace8eec74f2bbea1d9abad65064362841f2e2387dc79d796e65cda0ea23)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedulers", value)

    @builtins.property
    @jsii.member(jsii_name="sourceBucketArn")
    def source_bucket_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the Amazon S3 bucket where your DAG code and supporting files are stored.

        For example, ``arn:aws:s3:::my-airflow-bucket-unique-name`` . To learn more, see `Create an Amazon S3 bucket for Amazon MWAA <https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-s3-bucket.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-sourcebucketarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceBucketArn"))

    @source_bucket_arn.setter
    def source_bucket_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c774ff3a8e404c7f38d93b4263284adb0699d5b8880bfbfc42654a0be0f08247)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceBucketArn", value)

    @builtins.property
    @jsii.member(jsii_name="webserverAccessMode")
    def webserver_access_mode(self) -> typing.Optional[builtins.str]:
        '''The Apache Airflow *Web server* access mode.

        To learn more, see `Apache Airflow access modes <https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-networking.html>`_ . Valid values: ``PRIVATE_ONLY`` or ``PUBLIC_ONLY`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-webserveraccessmode
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "webserverAccessMode"))

    @webserver_access_mode.setter
    def webserver_access_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa02042e7dbdd64a2a2ab013c14dc385037db4f3f0cad68ab8fbbb898bee8121)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "webserverAccessMode", value)

    @builtins.property
    @jsii.member(jsii_name="weeklyMaintenanceWindowStart")
    def weekly_maintenance_window_start(self) -> typing.Optional[builtins.str]:
        '''The day and time of the week to start weekly maintenance updates of your environment in the following format: ``DAY:HH:MM`` .

        For example: ``TUE:03:30`` . You can specify a start time in 30 minute increments only. Supported input includes the following:

        - MON|TUE|WED|THU|FRI|SAT|SUN:([01]\\d|2[0-3]):(00|30)

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-weeklymaintenancewindowstart
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "weeklyMaintenanceWindowStart"))

    @weekly_maintenance_window_start.setter
    def weekly_maintenance_window_start(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1b6f64e6413c2fd8cfc8d54a66b45029ce1c781ce9d532c6b4f79d0178d59c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weeklyMaintenanceWindowStart", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_mwaa.CfnEnvironment.LoggingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dag_processing_logs": "dagProcessingLogs",
            "scheduler_logs": "schedulerLogs",
            "task_logs": "taskLogs",
            "webserver_logs": "webserverLogs",
            "worker_logs": "workerLogs",
        },
    )
    class LoggingConfigurationProperty:
        def __init__(
            self,
            *,
            dag_processing_logs: typing.Optional[typing.Union[typing.Union["CfnEnvironment.ModuleLoggingConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            scheduler_logs: typing.Optional[typing.Union[typing.Union["CfnEnvironment.ModuleLoggingConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            task_logs: typing.Optional[typing.Union[typing.Union["CfnEnvironment.ModuleLoggingConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            webserver_logs: typing.Optional[typing.Union[typing.Union["CfnEnvironment.ModuleLoggingConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            worker_logs: typing.Optional[typing.Union[typing.Union["CfnEnvironment.ModuleLoggingConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''The type of Apache Airflow logs to send to CloudWatch Logs.

            :param dag_processing_logs: Defines the processing logs sent to CloudWatch Logs and the logging level to send.
            :param scheduler_logs: Defines the scheduler logs sent to CloudWatch Logs and the logging level to send.
            :param task_logs: Defines the task logs sent to CloudWatch Logs and the logging level to send.
            :param webserver_logs: Defines the web server logs sent to CloudWatch Logs and the logging level to send.
            :param worker_logs: Defines the worker logs sent to CloudWatch Logs and the logging level to send.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-loggingconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_mwaa as mwaa
                
                logging_configuration_property = mwaa.CfnEnvironment.LoggingConfigurationProperty(
                    dag_processing_logs=mwaa.CfnEnvironment.ModuleLoggingConfigurationProperty(
                        cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                        enabled=False,
                        log_level="logLevel"
                    ),
                    scheduler_logs=mwaa.CfnEnvironment.ModuleLoggingConfigurationProperty(
                        cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                        enabled=False,
                        log_level="logLevel"
                    ),
                    task_logs=mwaa.CfnEnvironment.ModuleLoggingConfigurationProperty(
                        cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                        enabled=False,
                        log_level="logLevel"
                    ),
                    webserver_logs=mwaa.CfnEnvironment.ModuleLoggingConfigurationProperty(
                        cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                        enabled=False,
                        log_level="logLevel"
                    ),
                    worker_logs=mwaa.CfnEnvironment.ModuleLoggingConfigurationProperty(
                        cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                        enabled=False,
                        log_level="logLevel"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a74a6a5c6ea6f2a96e725fd5a0fe0f0bc7f8e741de73505c5281f59c3d689845)
                check_type(argname="argument dag_processing_logs", value=dag_processing_logs, expected_type=type_hints["dag_processing_logs"])
                check_type(argname="argument scheduler_logs", value=scheduler_logs, expected_type=type_hints["scheduler_logs"])
                check_type(argname="argument task_logs", value=task_logs, expected_type=type_hints["task_logs"])
                check_type(argname="argument webserver_logs", value=webserver_logs, expected_type=type_hints["webserver_logs"])
                check_type(argname="argument worker_logs", value=worker_logs, expected_type=type_hints["worker_logs"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if dag_processing_logs is not None:
                self._values["dag_processing_logs"] = dag_processing_logs
            if scheduler_logs is not None:
                self._values["scheduler_logs"] = scheduler_logs
            if task_logs is not None:
                self._values["task_logs"] = task_logs
            if webserver_logs is not None:
                self._values["webserver_logs"] = webserver_logs
            if worker_logs is not None:
                self._values["worker_logs"] = worker_logs

        @builtins.property
        def dag_processing_logs(
            self,
        ) -> typing.Optional[typing.Union["CfnEnvironment.ModuleLoggingConfigurationProperty", _IResolvable_a771d0ef]]:
            '''Defines the processing logs sent to CloudWatch Logs and the logging level to send.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-loggingconfiguration.html#cfn-mwaa-environment-loggingconfiguration-dagprocessinglogs
            '''
            result = self._values.get("dag_processing_logs")
            return typing.cast(typing.Optional[typing.Union["CfnEnvironment.ModuleLoggingConfigurationProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def scheduler_logs(
            self,
        ) -> typing.Optional[typing.Union["CfnEnvironment.ModuleLoggingConfigurationProperty", _IResolvable_a771d0ef]]:
            '''Defines the scheduler logs sent to CloudWatch Logs and the logging level to send.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-loggingconfiguration.html#cfn-mwaa-environment-loggingconfiguration-schedulerlogs
            '''
            result = self._values.get("scheduler_logs")
            return typing.cast(typing.Optional[typing.Union["CfnEnvironment.ModuleLoggingConfigurationProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def task_logs(
            self,
        ) -> typing.Optional[typing.Union["CfnEnvironment.ModuleLoggingConfigurationProperty", _IResolvable_a771d0ef]]:
            '''Defines the task logs sent to CloudWatch Logs and the logging level to send.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-loggingconfiguration.html#cfn-mwaa-environment-loggingconfiguration-tasklogs
            '''
            result = self._values.get("task_logs")
            return typing.cast(typing.Optional[typing.Union["CfnEnvironment.ModuleLoggingConfigurationProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def webserver_logs(
            self,
        ) -> typing.Optional[typing.Union["CfnEnvironment.ModuleLoggingConfigurationProperty", _IResolvable_a771d0ef]]:
            '''Defines the web server logs sent to CloudWatch Logs and the logging level to send.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-loggingconfiguration.html#cfn-mwaa-environment-loggingconfiguration-webserverlogs
            '''
            result = self._values.get("webserver_logs")
            return typing.cast(typing.Optional[typing.Union["CfnEnvironment.ModuleLoggingConfigurationProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def worker_logs(
            self,
        ) -> typing.Optional[typing.Union["CfnEnvironment.ModuleLoggingConfigurationProperty", _IResolvable_a771d0ef]]:
            '''Defines the worker logs sent to CloudWatch Logs and the logging level to send.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-loggingconfiguration.html#cfn-mwaa-environment-loggingconfiguration-workerlogs
            '''
            result = self._values.get("worker_logs")
            return typing.cast(typing.Optional[typing.Union["CfnEnvironment.ModuleLoggingConfigurationProperty", _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoggingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_mwaa.CfnEnvironment.ModuleLoggingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloud_watch_log_group_arn": "cloudWatchLogGroupArn",
            "enabled": "enabled",
            "log_level": "logLevel",
        },
    )
    class ModuleLoggingConfigurationProperty:
        def __init__(
            self,
            *,
            cloud_watch_log_group_arn: typing.Optional[builtins.str] = None,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            log_level: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines the type of logs to send for the Apache Airflow log type (e.g. ``DagProcessingLogs`` ).

            :param cloud_watch_log_group_arn: The ARN of the CloudWatch Logs log group for each type of Apache Airflow log type that you have enabled. .. epigraph:: ``CloudWatchLogGroupArn`` is available only as a return value, accessible when specified as an attribute in the ```Fn:GetAtt`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#aws-resource-mwaa-environment-return-values>`_ intrinsic function. Any value you provide for ``CloudWatchLogGroupArn`` is discarded by Amazon MWAA.
            :param enabled: Indicates whether to enable the Apache Airflow log type (e.g. ``DagProcessingLogs`` ) in CloudWatch Logs.
            :param log_level: Defines the Apache Airflow logs to send for the log type (e.g. ``DagProcessingLogs`` ) to CloudWatch Logs. Valid values: ``CRITICAL`` , ``ERROR`` , ``WARNING`` , ``INFO`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-moduleloggingconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_mwaa as mwaa
                
                module_logging_configuration_property = mwaa.CfnEnvironment.ModuleLoggingConfigurationProperty(
                    cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                    enabled=False,
                    log_level="logLevel"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3fd6893555c0e4f2f8d4eb2ea5671b2f001cae7e4c1d187604a8275014488a4d)
                check_type(argname="argument cloud_watch_log_group_arn", value=cloud_watch_log_group_arn, expected_type=type_hints["cloud_watch_log_group_arn"])
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument log_level", value=log_level, expected_type=type_hints["log_level"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cloud_watch_log_group_arn is not None:
                self._values["cloud_watch_log_group_arn"] = cloud_watch_log_group_arn
            if enabled is not None:
                self._values["enabled"] = enabled
            if log_level is not None:
                self._values["log_level"] = log_level

        @builtins.property
        def cloud_watch_log_group_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the CloudWatch Logs log group for each type of Apache Airflow log type that you have enabled.

            .. epigraph::

               ``CloudWatchLogGroupArn`` is available only as a return value, accessible when specified as an attribute in the ```Fn:GetAtt`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#aws-resource-mwaa-environment-return-values>`_ intrinsic function. Any value you provide for ``CloudWatchLogGroupArn`` is discarded by Amazon MWAA.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-moduleloggingconfiguration.html#cfn-mwaa-environment-moduleloggingconfiguration-cloudwatchloggrouparn
            '''
            result = self._values.get("cloud_watch_log_group_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Indicates whether to enable the Apache Airflow log type (e.g. ``DagProcessingLogs`` ) in CloudWatch Logs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-moduleloggingconfiguration.html#cfn-mwaa-environment-moduleloggingconfiguration-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def log_level(self) -> typing.Optional[builtins.str]:
            '''Defines the Apache Airflow logs to send for the log type (e.g. ``DagProcessingLogs`` ) to CloudWatch Logs. Valid values: ``CRITICAL`` , ``ERROR`` , ``WARNING`` , ``INFO`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-moduleloggingconfiguration.html#cfn-mwaa-environment-moduleloggingconfiguration-loglevel
            '''
            result = self._values.get("log_level")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ModuleLoggingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_mwaa.CfnEnvironment.NetworkConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "security_group_ids": "securityGroupIds",
            "subnet_ids": "subnetIds",
        },
    )
    class NetworkConfigurationProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The VPC networking components used to secure and enable network traffic between the AWS resources for your environment.

            To learn more, see `About networking on Amazon MWAA <https://docs.aws.amazon.com/mwaa/latest/userguide/networking-about.html>`_ .

            :param security_group_ids: A list of one or more security group IDs. Accepts up to 5 security group IDs. A security group must be attached to the same VPC as the subnets. To learn more, see `Security in your VPC on Amazon MWAA <https://docs.aws.amazon.com/mwaa/latest/userguide/vpc-security.html>`_ .
            :param subnet_ids: A list of subnet IDs. *Required* to create an environment. Must be private subnets in two different availability zones. A subnet must be attached to the same VPC as the security group. To learn more, see `About networking on Amazon MWAA <https://docs.aws.amazon.com/mwaa/latest/userguide/networking-about.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-networkconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_mwaa as mwaa
                
                network_configuration_property = mwaa.CfnEnvironment.NetworkConfigurationProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__eb62beb473f1d7adab029f9278979874d515944fd02c3cffe7387403013cc55e)
                check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
                check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if security_group_ids is not None:
                self._values["security_group_ids"] = security_group_ids
            if subnet_ids is not None:
                self._values["subnet_ids"] = subnet_ids

        @builtins.property
        def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of one or more security group IDs.

            Accepts up to 5 security group IDs. A security group must be attached to the same VPC as the subnets. To learn more, see `Security in your VPC on Amazon MWAA <https://docs.aws.amazon.com/mwaa/latest/userguide/vpc-security.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-networkconfiguration.html#cfn-mwaa-environment-networkconfiguration-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of subnet IDs.

            *Required* to create an environment. Must be private subnets in two different availability zones. A subnet must be attached to the same VPC as the security group. To learn more, see `About networking on Amazon MWAA <https://docs.aws.amazon.com/mwaa/latest/userguide/networking-about.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-networkconfiguration.html#cfn-mwaa-environment-networkconfiguration-subnetids
            '''
            result = self._values.get("subnet_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_mwaa.CfnEnvironmentProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "airflow_configuration_options": "airflowConfigurationOptions",
        "airflow_version": "airflowVersion",
        "dag_s3_path": "dagS3Path",
        "environment_class": "environmentClass",
        "execution_role_arn": "executionRoleArn",
        "kms_key": "kmsKey",
        "logging_configuration": "loggingConfiguration",
        "max_workers": "maxWorkers",
        "min_workers": "minWorkers",
        "network_configuration": "networkConfiguration",
        "plugins_s3_object_version": "pluginsS3ObjectVersion",
        "plugins_s3_path": "pluginsS3Path",
        "requirements_s3_object_version": "requirementsS3ObjectVersion",
        "requirements_s3_path": "requirementsS3Path",
        "schedulers": "schedulers",
        "source_bucket_arn": "sourceBucketArn",
        "tags": "tags",
        "webserver_access_mode": "webserverAccessMode",
        "weekly_maintenance_window_start": "weeklyMaintenanceWindowStart",
    },
)
class CfnEnvironmentProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        airflow_configuration_options: typing.Any = None,
        airflow_version: typing.Optional[builtins.str] = None,
        dag_s3_path: typing.Optional[builtins.str] = None,
        environment_class: typing.Optional[builtins.str] = None,
        execution_role_arn: typing.Optional[builtins.str] = None,
        kms_key: typing.Optional[builtins.str] = None,
        logging_configuration: typing.Optional[typing.Union[typing.Union[CfnEnvironment.LoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        max_workers: typing.Optional[jsii.Number] = None,
        min_workers: typing.Optional[jsii.Number] = None,
        network_configuration: typing.Optional[typing.Union[typing.Union[CfnEnvironment.NetworkConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        plugins_s3_object_version: typing.Optional[builtins.str] = None,
        plugins_s3_path: typing.Optional[builtins.str] = None,
        requirements_s3_object_version: typing.Optional[builtins.str] = None,
        requirements_s3_path: typing.Optional[builtins.str] = None,
        schedulers: typing.Optional[jsii.Number] = None,
        source_bucket_arn: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
        webserver_access_mode: typing.Optional[builtins.str] = None,
        weekly_maintenance_window_start: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnEnvironment``.

        :param name: The name of your Amazon MWAA environment.
        :param airflow_configuration_options: A list of key-value pairs containing the Airflow configuration options for your environment. For example, ``core.default_timezone: utc`` . To learn more, see `Apache Airflow configuration options <https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-env-variables.html>`_ .
        :param airflow_version: The version of Apache Airflow to use for the environment. If no value is specified, defaults to the latest version. Valid values: ``2.0.2`` , ``1.10.12`` , ``2.2.2`` .
        :param dag_s3_path: The relative path to the DAGs folder on your Amazon S3 bucket. For example, ``dags`` . To learn more, see `Adding or updating DAGs <https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-folder.html>`_ .
        :param environment_class: The environment class type. Valid values: ``mw1.small`` , ``mw1.medium`` , ``mw1.large`` . To learn more, see `Amazon MWAA environment class <https://docs.aws.amazon.com/mwaa/latest/userguide/environment-class.html>`_ .
        :param execution_role_arn: The Amazon Resource Name (ARN) of the execution role in IAM that allows MWAA to access AWS resources in your environment. For example, ``arn:aws:iam::123456789:role/my-execution-role`` . To learn more, see `Amazon MWAA Execution role <https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-create-role.html>`_ .
        :param kms_key: The AWS Key Management Service (KMS) key to encrypt and decrypt the data in your environment. You can use an AWS KMS key managed by MWAA, or a customer-managed KMS key (advanced).
        :param logging_configuration: The Apache Airflow logs being sent to CloudWatch Logs: ``DagProcessingLogs`` , ``SchedulerLogs`` , ``TaskLogs`` , ``WebserverLogs`` , ``WorkerLogs`` .
        :param max_workers: The maximum number of workers that you want to run in your environment. MWAA scales the number of Apache Airflow workers up to the number you specify in the ``MaxWorkers`` field. For example, ``20`` . When there are no more tasks running, and no more in the queue, MWAA disposes of the extra workers leaving the one worker that is included with your environment, or the number you specify in ``MinWorkers`` .
        :param min_workers: The minimum number of workers that you want to run in your environment. MWAA scales the number of Apache Airflow workers up to the number you specify in the ``MaxWorkers`` field. When there are no more tasks running, and no more in the queue, MWAA disposes of the extra workers leaving the worker count you specify in the ``MinWorkers`` field. For example, ``2`` .
        :param network_configuration: The VPC networking components used to secure and enable network traffic between the AWS resources for your environment. To learn more, see `About networking on Amazon MWAA <https://docs.aws.amazon.com/mwaa/latest/userguide/networking-about.html>`_ .
        :param plugins_s3_object_version: The version of the plugins.zip file on your Amazon S3 bucket. To learn more, see `Installing custom plugins <https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-import-plugins.html>`_ .
        :param plugins_s3_path: The relative path to the ``plugins.zip`` file on your Amazon S3 bucket. For example, ``plugins.zip`` . To learn more, see `Installing custom plugins <https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-import-plugins.html>`_ .
        :param requirements_s3_object_version: The version of the requirements.txt file on your Amazon S3 bucket. To learn more, see `Installing Python dependencies <https://docs.aws.amazon.com/mwaa/latest/userguide/working-dags-dependencies.html>`_ .
        :param requirements_s3_path: The relative path to the ``requirements.txt`` file on your Amazon S3 bucket. For example, ``requirements.txt`` . To learn more, see `Installing Python dependencies <https://docs.aws.amazon.com/mwaa/latest/userguide/working-dags-dependencies.html>`_ .
        :param schedulers: The number of schedulers that you want to run in your environment. Valid values:. - *v2.0.2* - Accepts between 2 to 5. Defaults to 2. - *v1.10.12* - Accepts 1.
        :param source_bucket_arn: The Amazon Resource Name (ARN) of the Amazon S3 bucket where your DAG code and supporting files are stored. For example, ``arn:aws:s3:::my-airflow-bucket-unique-name`` . To learn more, see `Create an Amazon S3 bucket for Amazon MWAA <https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-s3-bucket.html>`_ .
        :param tags: The key-value tag pairs associated to your environment. For example, ``"Environment": "Staging"`` . To learn more, see `Tagging <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .
        :param webserver_access_mode: The Apache Airflow *Web server* access mode. To learn more, see `Apache Airflow access modes <https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-networking.html>`_ . Valid values: ``PRIVATE_ONLY`` or ``PUBLIC_ONLY`` .
        :param weekly_maintenance_window_start: The day and time of the week to start weekly maintenance updates of your environment in the following format: ``DAY:HH:MM`` . For example: ``TUE:03:30`` . You can specify a start time in 30 minute increments only. Supported input includes the following: - MON|TUE|WED|THU|FRI|SAT|SUN:([01]\\d|2[0-3]):(00|30)

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_mwaa as mwaa
            
            # airflow_configuration_options: Any
            # tags: Any
            
            cfn_environment_props = mwaa.CfnEnvironmentProps(
                name="name",
            
                # the properties below are optional
                airflow_configuration_options=airflow_configuration_options,
                airflow_version="airflowVersion",
                dag_s3_path="dagS3Path",
                environment_class="environmentClass",
                execution_role_arn="executionRoleArn",
                kms_key="kmsKey",
                logging_configuration=mwaa.CfnEnvironment.LoggingConfigurationProperty(
                    dag_processing_logs=mwaa.CfnEnvironment.ModuleLoggingConfigurationProperty(
                        cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                        enabled=False,
                        log_level="logLevel"
                    ),
                    scheduler_logs=mwaa.CfnEnvironment.ModuleLoggingConfigurationProperty(
                        cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                        enabled=False,
                        log_level="logLevel"
                    ),
                    task_logs=mwaa.CfnEnvironment.ModuleLoggingConfigurationProperty(
                        cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                        enabled=False,
                        log_level="logLevel"
                    ),
                    webserver_logs=mwaa.CfnEnvironment.ModuleLoggingConfigurationProperty(
                        cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                        enabled=False,
                        log_level="logLevel"
                    ),
                    worker_logs=mwaa.CfnEnvironment.ModuleLoggingConfigurationProperty(
                        cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                        enabled=False,
                        log_level="logLevel"
                    )
                ),
                max_workers=123,
                min_workers=123,
                network_configuration=mwaa.CfnEnvironment.NetworkConfigurationProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                ),
                plugins_s3_object_version="pluginsS3ObjectVersion",
                plugins_s3_path="pluginsS3Path",
                requirements_s3_object_version="requirementsS3ObjectVersion",
                requirements_s3_path="requirementsS3Path",
                schedulers=123,
                source_bucket_arn="sourceBucketArn",
                tags=tags,
                webserver_access_mode="webserverAccessMode",
                weekly_maintenance_window_start="weeklyMaintenanceWindowStart"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29a947a969bc33c4ba86bc63fe661bb71a755a0bddc1405a35475e723ff57386)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument airflow_configuration_options", value=airflow_configuration_options, expected_type=type_hints["airflow_configuration_options"])
            check_type(argname="argument airflow_version", value=airflow_version, expected_type=type_hints["airflow_version"])
            check_type(argname="argument dag_s3_path", value=dag_s3_path, expected_type=type_hints["dag_s3_path"])
            check_type(argname="argument environment_class", value=environment_class, expected_type=type_hints["environment_class"])
            check_type(argname="argument execution_role_arn", value=execution_role_arn, expected_type=type_hints["execution_role_arn"])
            check_type(argname="argument kms_key", value=kms_key, expected_type=type_hints["kms_key"])
            check_type(argname="argument logging_configuration", value=logging_configuration, expected_type=type_hints["logging_configuration"])
            check_type(argname="argument max_workers", value=max_workers, expected_type=type_hints["max_workers"])
            check_type(argname="argument min_workers", value=min_workers, expected_type=type_hints["min_workers"])
            check_type(argname="argument network_configuration", value=network_configuration, expected_type=type_hints["network_configuration"])
            check_type(argname="argument plugins_s3_object_version", value=plugins_s3_object_version, expected_type=type_hints["plugins_s3_object_version"])
            check_type(argname="argument plugins_s3_path", value=plugins_s3_path, expected_type=type_hints["plugins_s3_path"])
            check_type(argname="argument requirements_s3_object_version", value=requirements_s3_object_version, expected_type=type_hints["requirements_s3_object_version"])
            check_type(argname="argument requirements_s3_path", value=requirements_s3_path, expected_type=type_hints["requirements_s3_path"])
            check_type(argname="argument schedulers", value=schedulers, expected_type=type_hints["schedulers"])
            check_type(argname="argument source_bucket_arn", value=source_bucket_arn, expected_type=type_hints["source_bucket_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument webserver_access_mode", value=webserver_access_mode, expected_type=type_hints["webserver_access_mode"])
            check_type(argname="argument weekly_maintenance_window_start", value=weekly_maintenance_window_start, expected_type=type_hints["weekly_maintenance_window_start"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if airflow_configuration_options is not None:
            self._values["airflow_configuration_options"] = airflow_configuration_options
        if airflow_version is not None:
            self._values["airflow_version"] = airflow_version
        if dag_s3_path is not None:
            self._values["dag_s3_path"] = dag_s3_path
        if environment_class is not None:
            self._values["environment_class"] = environment_class
        if execution_role_arn is not None:
            self._values["execution_role_arn"] = execution_role_arn
        if kms_key is not None:
            self._values["kms_key"] = kms_key
        if logging_configuration is not None:
            self._values["logging_configuration"] = logging_configuration
        if max_workers is not None:
            self._values["max_workers"] = max_workers
        if min_workers is not None:
            self._values["min_workers"] = min_workers
        if network_configuration is not None:
            self._values["network_configuration"] = network_configuration
        if plugins_s3_object_version is not None:
            self._values["plugins_s3_object_version"] = plugins_s3_object_version
        if plugins_s3_path is not None:
            self._values["plugins_s3_path"] = plugins_s3_path
        if requirements_s3_object_version is not None:
            self._values["requirements_s3_object_version"] = requirements_s3_object_version
        if requirements_s3_path is not None:
            self._values["requirements_s3_path"] = requirements_s3_path
        if schedulers is not None:
            self._values["schedulers"] = schedulers
        if source_bucket_arn is not None:
            self._values["source_bucket_arn"] = source_bucket_arn
        if tags is not None:
            self._values["tags"] = tags
        if webserver_access_mode is not None:
            self._values["webserver_access_mode"] = webserver_access_mode
        if weekly_maintenance_window_start is not None:
            self._values["weekly_maintenance_window_start"] = weekly_maintenance_window_start

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of your Amazon MWAA environment.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def airflow_configuration_options(self) -> typing.Any:
        '''A list of key-value pairs containing the Airflow configuration options for your environment.

        For example, ``core.default_timezone: utc`` . To learn more, see `Apache Airflow configuration options <https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-env-variables.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-airflowconfigurationoptions
        '''
        result = self._values.get("airflow_configuration_options")
        return typing.cast(typing.Any, result)

    @builtins.property
    def airflow_version(self) -> typing.Optional[builtins.str]:
        '''The version of Apache Airflow to use for the environment.

        If no value is specified, defaults to the latest version. Valid values: ``2.0.2`` , ``1.10.12`` , ``2.2.2`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-airflowversion
        '''
        result = self._values.get("airflow_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dag_s3_path(self) -> typing.Optional[builtins.str]:
        '''The relative path to the DAGs folder on your Amazon S3 bucket.

        For example, ``dags`` . To learn more, see `Adding or updating DAGs <https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-folder.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-dags3path
        '''
        result = self._values.get("dag_s3_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment_class(self) -> typing.Optional[builtins.str]:
        '''The environment class type.

        Valid values: ``mw1.small`` , ``mw1.medium`` , ``mw1.large`` . To learn more, see `Amazon MWAA environment class <https://docs.aws.amazon.com/mwaa/latest/userguide/environment-class.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-environmentclass
        '''
        result = self._values.get("environment_class")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the execution role in IAM that allows MWAA to access AWS resources in your environment.

        For example, ``arn:aws:iam::123456789:role/my-execution-role`` . To learn more, see `Amazon MWAA Execution role <https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-create-role.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-executionrolearn
        '''
        result = self._values.get("execution_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key(self) -> typing.Optional[builtins.str]:
        '''The AWS Key Management Service (KMS) key to encrypt and decrypt the data in your environment.

        You can use an AWS KMS key managed by MWAA, or a customer-managed KMS key (advanced).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-kmskey
        '''
        result = self._values.get("kms_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logging_configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnEnvironment.LoggingConfigurationProperty, _IResolvable_a771d0ef]]:
        '''The Apache Airflow logs being sent to CloudWatch Logs: ``DagProcessingLogs`` , ``SchedulerLogs`` , ``TaskLogs`` , ``WebserverLogs`` , ``WorkerLogs`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-loggingconfiguration
        '''
        result = self._values.get("logging_configuration")
        return typing.cast(typing.Optional[typing.Union[CfnEnvironment.LoggingConfigurationProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def max_workers(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of workers that you want to run in your environment.

        MWAA scales the number of Apache Airflow workers up to the number you specify in the ``MaxWorkers`` field. For example, ``20`` . When there are no more tasks running, and no more in the queue, MWAA disposes of the extra workers leaving the one worker that is included with your environment, or the number you specify in ``MinWorkers`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-maxworkers
        '''
        result = self._values.get("max_workers")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_workers(self) -> typing.Optional[jsii.Number]:
        '''The minimum number of workers that you want to run in your environment.

        MWAA scales the number of Apache Airflow workers up to the number you specify in the ``MaxWorkers`` field. When there are no more tasks running, and no more in the queue, MWAA disposes of the extra workers leaving the worker count you specify in the ``MinWorkers`` field. For example, ``2`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-minworkers
        '''
        result = self._values.get("min_workers")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def network_configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnEnvironment.NetworkConfigurationProperty, _IResolvable_a771d0ef]]:
        '''The VPC networking components used to secure and enable network traffic between the AWS resources for your environment.

        To learn more, see `About networking on Amazon MWAA <https://docs.aws.amazon.com/mwaa/latest/userguide/networking-about.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-networkconfiguration
        '''
        result = self._values.get("network_configuration")
        return typing.cast(typing.Optional[typing.Union[CfnEnvironment.NetworkConfigurationProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def plugins_s3_object_version(self) -> typing.Optional[builtins.str]:
        '''The version of the plugins.zip file on your Amazon S3 bucket. To learn more, see `Installing custom plugins <https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-import-plugins.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-pluginss3objectversion
        '''
        result = self._values.get("plugins_s3_object_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def plugins_s3_path(self) -> typing.Optional[builtins.str]:
        '''The relative path to the ``plugins.zip`` file on your Amazon S3 bucket. For example, ``plugins.zip`` . To learn more, see `Installing custom plugins <https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-import-plugins.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-pluginss3path
        '''
        result = self._values.get("plugins_s3_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def requirements_s3_object_version(self) -> typing.Optional[builtins.str]:
        '''The version of the requirements.txt file on your Amazon S3 bucket. To learn more, see `Installing Python dependencies <https://docs.aws.amazon.com/mwaa/latest/userguide/working-dags-dependencies.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-requirementss3objectversion
        '''
        result = self._values.get("requirements_s3_object_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def requirements_s3_path(self) -> typing.Optional[builtins.str]:
        '''The relative path to the ``requirements.txt`` file on your Amazon S3 bucket. For example, ``requirements.txt`` . To learn more, see `Installing Python dependencies <https://docs.aws.amazon.com/mwaa/latest/userguide/working-dags-dependencies.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-requirementss3path
        '''
        result = self._values.get("requirements_s3_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schedulers(self) -> typing.Optional[jsii.Number]:
        '''The number of schedulers that you want to run in your environment. Valid values:.

        - *v2.0.2* - Accepts between 2 to 5. Defaults to 2.
        - *v1.10.12* - Accepts 1.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-schedulers
        '''
        result = self._values.get("schedulers")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def source_bucket_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the Amazon S3 bucket where your DAG code and supporting files are stored.

        For example, ``arn:aws:s3:::my-airflow-bucket-unique-name`` . To learn more, see `Create an Amazon S3 bucket for Amazon MWAA <https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-s3-bucket.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-sourcebucketarn
        '''
        result = self._values.get("source_bucket_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''The key-value tag pairs associated to your environment.

        For example, ``"Environment": "Staging"`` . To learn more, see `Tagging <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    @builtins.property
    def webserver_access_mode(self) -> typing.Optional[builtins.str]:
        '''The Apache Airflow *Web server* access mode.

        To learn more, see `Apache Airflow access modes <https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-networking.html>`_ . Valid values: ``PRIVATE_ONLY`` or ``PUBLIC_ONLY`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-webserveraccessmode
        '''
        result = self._values.get("webserver_access_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def weekly_maintenance_window_start(self) -> typing.Optional[builtins.str]:
        '''The day and time of the week to start weekly maintenance updates of your environment in the following format: ``DAY:HH:MM`` .

        For example: ``TUE:03:30`` . You can specify a start time in 30 minute increments only. Supported input includes the following:

        - MON|TUE|WED|THU|FRI|SAT|SUN:([01]\\d|2[0-3]):(00|30)

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-weeklymaintenancewindowstart
        '''
        result = self._values.get("weekly_maintenance_window_start")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEnvironmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnEnvironment",
    "CfnEnvironmentProps",
]

publication.publish()

def _typecheckingstub__470828095b91afb3a680b6d2abb51b3a7c3db448123609c29b3cf4eda2d34c35(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    name: builtins.str,
    airflow_configuration_options: typing.Any = None,
    airflow_version: typing.Optional[builtins.str] = None,
    dag_s3_path: typing.Optional[builtins.str] = None,
    environment_class: typing.Optional[builtins.str] = None,
    execution_role_arn: typing.Optional[builtins.str] = None,
    kms_key: typing.Optional[builtins.str] = None,
    logging_configuration: typing.Optional[typing.Union[typing.Union[CfnEnvironment.LoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    max_workers: typing.Optional[jsii.Number] = None,
    min_workers: typing.Optional[jsii.Number] = None,
    network_configuration: typing.Optional[typing.Union[typing.Union[CfnEnvironment.NetworkConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    plugins_s3_object_version: typing.Optional[builtins.str] = None,
    plugins_s3_path: typing.Optional[builtins.str] = None,
    requirements_s3_object_version: typing.Optional[builtins.str] = None,
    requirements_s3_path: typing.Optional[builtins.str] = None,
    schedulers: typing.Optional[jsii.Number] = None,
    source_bucket_arn: typing.Optional[builtins.str] = None,
    tags: typing.Any = None,
    webserver_access_mode: typing.Optional[builtins.str] = None,
    weekly_maintenance_window_start: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5422cab040c438602a2333ec2516e0bca634c7fb7376aabc5db230d6230d56b(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__427c507a35ef4cbf07937a63a5637c52bc8d33a1a506488b5711df4f3d98b2dd(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05ac9db5fda75fc618028e29b14b46f30a1b5c5c294b2c4c192a6fdfa1b58e9c(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10a22ed6817a79463af7bd431f70f4734ff3ff3902abbe4362d59c9bc6015599(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f966da09774892771a8e99c24c01f9e489786294eeb2c7c6052ebc510fc5fefb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f22dadcba5bba6af9ecb79706dc01ff7a78aea0f54305244bbfd78058c2a134(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b41ebc1c1325dd4684c914d0e62d471c2a70dd830ee7bed91fd8325707bdf61a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4311e19671686d923a5c23f3d8d631b40051216addd2240840223e55f14ebe66(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af57b04ee04aa6ac912321585c71e01cb73008abb3586f7a4b1194e478efa9ef(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37f8b1b0ae6ffed44277364161d1f86d58367ecb5970a4cb6624d272bb98c572(
    value: typing.Optional[typing.Union[CfnEnvironment.LoggingConfigurationProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d59d82588fb7f3b275babec4165ca9601097d1cebde0447e519907cb80c6446(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1258587e49cdc9830166a04720beee61b83a48578b0e83facf0c707e6382691f(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7db5bc459e6b21e4387894746807a9dbfbec37245713ba80a68e08284b143de2(
    value: typing.Optional[typing.Union[CfnEnvironment.NetworkConfigurationProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1778a4a6a5ff2b8815182049512859e4314a4c3e749a324b468bfa6d296a90bc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04bf9fbc29749ccb6deacd0db0efa6bb1626d913f3c0e178fa981bb94ec77bae(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28ce3289b4ec54728fbe269e260b9079a44a80e91ea429196444b94d1912fe98(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd9cdb7bbe8c59536e4aaf94f40342b100f02011531786712f22572e9d368869(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7f23ace8eec74f2bbea1d9abad65064362841f2e2387dc79d796e65cda0ea23(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c774ff3a8e404c7f38d93b4263284adb0699d5b8880bfbfc42654a0be0f08247(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa02042e7dbdd64a2a2ab013c14dc385037db4f3f0cad68ab8fbbb898bee8121(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1b6f64e6413c2fd8cfc8d54a66b45029ce1c781ce9d532c6b4f79d0178d59c8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a74a6a5c6ea6f2a96e725fd5a0fe0f0bc7f8e741de73505c5281f59c3d689845(
    *,
    dag_processing_logs: typing.Optional[typing.Union[typing.Union[CfnEnvironment.ModuleLoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    scheduler_logs: typing.Optional[typing.Union[typing.Union[CfnEnvironment.ModuleLoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    task_logs: typing.Optional[typing.Union[typing.Union[CfnEnvironment.ModuleLoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    webserver_logs: typing.Optional[typing.Union[typing.Union[CfnEnvironment.ModuleLoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    worker_logs: typing.Optional[typing.Union[typing.Union[CfnEnvironment.ModuleLoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fd6893555c0e4f2f8d4eb2ea5671b2f001cae7e4c1d187604a8275014488a4d(
    *,
    cloud_watch_log_group_arn: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    log_level: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb62beb473f1d7adab029f9278979874d515944fd02c3cffe7387403013cc55e(
    *,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29a947a969bc33c4ba86bc63fe661bb71a755a0bddc1405a35475e723ff57386(
    *,
    name: builtins.str,
    airflow_configuration_options: typing.Any = None,
    airflow_version: typing.Optional[builtins.str] = None,
    dag_s3_path: typing.Optional[builtins.str] = None,
    environment_class: typing.Optional[builtins.str] = None,
    execution_role_arn: typing.Optional[builtins.str] = None,
    kms_key: typing.Optional[builtins.str] = None,
    logging_configuration: typing.Optional[typing.Union[typing.Union[CfnEnvironment.LoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    max_workers: typing.Optional[jsii.Number] = None,
    min_workers: typing.Optional[jsii.Number] = None,
    network_configuration: typing.Optional[typing.Union[typing.Union[CfnEnvironment.NetworkConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    plugins_s3_object_version: typing.Optional[builtins.str] = None,
    plugins_s3_path: typing.Optional[builtins.str] = None,
    requirements_s3_object_version: typing.Optional[builtins.str] = None,
    requirements_s3_path: typing.Optional[builtins.str] = None,
    schedulers: typing.Optional[jsii.Number] = None,
    source_bucket_arn: typing.Optional[builtins.str] = None,
    tags: typing.Any = None,
    webserver_access_mode: typing.Optional[builtins.str] = None,
    weekly_maintenance_window_start: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

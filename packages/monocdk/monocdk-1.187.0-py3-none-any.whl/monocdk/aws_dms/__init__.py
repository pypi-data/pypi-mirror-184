'''
# AWS Database Migration Service Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import monocdk as dms
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for DMS construct libraries](https://constructs.dev/search?q=dms)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::DMS resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DMS.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::DMS](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DMS.html).

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
    CfnTag as _CfnTag_95fbdc29,
    Construct as _Construct_e78e779f,
    IInspectable as _IInspectable_82c04a63,
    IResolvable as _IResolvable_a771d0ef,
    TagManager as _TagManager_0b7ab120,
    TreeInspector as _TreeInspector_1cd1894e,
)


@jsii.implements(_IInspectable_82c04a63)
class CfnCertificate(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_dms.CfnCertificate",
):
    '''A CloudFormation ``AWS::DMS::Certificate``.

    The ``AWS::DMS::Certificate`` resource creates an Secure Sockets Layer (SSL) certificate that encrypts connections between AWS DMS endpoints and the replication instance.

    :cloudformationResource: AWS::DMS::Certificate
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-certificate.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_dms as dms
        
        cfn_certificate = dms.CfnCertificate(self, "MyCfnCertificate",
            certificate_identifier="certificateIdentifier",
            certificate_pem="certificatePem",
            certificate_wallet="certificateWallet"
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        certificate_identifier: typing.Optional[builtins.str] = None,
        certificate_pem: typing.Optional[builtins.str] = None,
        certificate_wallet: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::DMS::Certificate``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param certificate_identifier: A customer-assigned name for the certificate. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen or contain two consecutive hyphens.
        :param certificate_pem: The contents of a ``.pem`` file, which contains an X.509 certificate.
        :param certificate_wallet: The location of an imported Oracle Wallet certificate for use with SSL. An example is: ``filebase64("${path.root}/rds-ca-2019-root.sso")``
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d979b5faaef30b55f0baa438530b2b64189152fed38d623cd51c26acc3f6a6f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCertificateProps(
            certificate_identifier=certificate_identifier,
            certificate_pem=certificate_pem,
            certificate_wallet=certificate_wallet,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86a510a264dfa2e34b691e7a27244e66cf90815c0f30584cec7d7c9778fa5e9f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6fbdc78514f3756bf1e34650115adde8108c4ddf23c2cdf2c0596e969de6cf34)
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
    @jsii.member(jsii_name="certificateIdentifier")
    def certificate_identifier(self) -> typing.Optional[builtins.str]:
        '''A customer-assigned name for the certificate.

        Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen or contain two consecutive hyphens.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-certificate.html#cfn-dms-certificate-certificateidentifier
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateIdentifier"))

    @certificate_identifier.setter
    def certificate_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99b2aefa35e0a8c9e52900fb49eddd2e702f971fb9dae833a50eab73e431f004)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="certificatePem")
    def certificate_pem(self) -> typing.Optional[builtins.str]:
        '''The contents of a ``.pem`` file, which contains an X.509 certificate.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-certificate.html#cfn-dms-certificate-certificatepem
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificatePem"))

    @certificate_pem.setter
    def certificate_pem(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__890d88ab2b7f7ccf0086b1a36ab18c8f209a2482233ce7cb521748ffd18dd92a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificatePem", value)

    @builtins.property
    @jsii.member(jsii_name="certificateWallet")
    def certificate_wallet(self) -> typing.Optional[builtins.str]:
        '''The location of an imported Oracle Wallet certificate for use with SSL.

        An example is: ``filebase64("${path.root}/rds-ca-2019-root.sso")``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-certificate.html#cfn-dms-certificate-certificatewallet
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateWallet"))

    @certificate_wallet.setter
    def certificate_wallet(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4067982d1e3936e4784a4ac328aa852dbadcf4bef5e14ee2d61d055147c9ea8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateWallet", value)


@jsii.data_type(
    jsii_type="monocdk.aws_dms.CfnCertificateProps",
    jsii_struct_bases=[],
    name_mapping={
        "certificate_identifier": "certificateIdentifier",
        "certificate_pem": "certificatePem",
        "certificate_wallet": "certificateWallet",
    },
)
class CfnCertificateProps:
    def __init__(
        self,
        *,
        certificate_identifier: typing.Optional[builtins.str] = None,
        certificate_pem: typing.Optional[builtins.str] = None,
        certificate_wallet: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnCertificate``.

        :param certificate_identifier: A customer-assigned name for the certificate. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen or contain two consecutive hyphens.
        :param certificate_pem: The contents of a ``.pem`` file, which contains an X.509 certificate.
        :param certificate_wallet: The location of an imported Oracle Wallet certificate for use with SSL. An example is: ``filebase64("${path.root}/rds-ca-2019-root.sso")``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-certificate.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_dms as dms
            
            cfn_certificate_props = dms.CfnCertificateProps(
                certificate_identifier="certificateIdentifier",
                certificate_pem="certificatePem",
                certificate_wallet="certificateWallet"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01d018beae7bb80039522a75ca3d5437e2b052649fbbd020d98a2eff34641e38)
            check_type(argname="argument certificate_identifier", value=certificate_identifier, expected_type=type_hints["certificate_identifier"])
            check_type(argname="argument certificate_pem", value=certificate_pem, expected_type=type_hints["certificate_pem"])
            check_type(argname="argument certificate_wallet", value=certificate_wallet, expected_type=type_hints["certificate_wallet"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if certificate_identifier is not None:
            self._values["certificate_identifier"] = certificate_identifier
        if certificate_pem is not None:
            self._values["certificate_pem"] = certificate_pem
        if certificate_wallet is not None:
            self._values["certificate_wallet"] = certificate_wallet

    @builtins.property
    def certificate_identifier(self) -> typing.Optional[builtins.str]:
        '''A customer-assigned name for the certificate.

        Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen or contain two consecutive hyphens.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-certificate.html#cfn-dms-certificate-certificateidentifier
        '''
        result = self._values.get("certificate_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_pem(self) -> typing.Optional[builtins.str]:
        '''The contents of a ``.pem`` file, which contains an X.509 certificate.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-certificate.html#cfn-dms-certificate-certificatepem
        '''
        result = self._values.get("certificate_pem")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_wallet(self) -> typing.Optional[builtins.str]:
        '''The location of an imported Oracle Wallet certificate for use with SSL.

        An example is: ``filebase64("${path.root}/rds-ca-2019-root.sso")``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-certificate.html#cfn-dms-certificate-certificatewallet
        '''
        result = self._values.get("certificate_wallet")
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
class CfnEndpoint(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_dms.CfnEndpoint",
):
    '''A CloudFormation ``AWS::DMS::Endpoint``.

    The ``AWS::DMS::Endpoint`` resource specifies an AWS DMS endpoint.

    Currently, AWS CloudFormation supports all AWS DMS endpoint types.

    :cloudformationResource: AWS::DMS::Endpoint
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_dms as dms
        
        cfn_endpoint = dms.CfnEndpoint(self, "MyCfnEndpoint",
            endpoint_type="endpointType",
            engine_name="engineName",
        
            # the properties below are optional
            certificate_arn="certificateArn",
            database_name="databaseName",
            doc_db_settings=dms.CfnEndpoint.DocDbSettingsProperty(
                docs_to_investigate=123,
                extract_doc_id=False,
                nesting_level="nestingLevel",
                secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                secrets_manager_secret_id="secretsManagerSecretId"
            ),
            dynamo_db_settings=dms.CfnEndpoint.DynamoDbSettingsProperty(
                service_access_role_arn="serviceAccessRoleArn"
            ),
            elasticsearch_settings=dms.CfnEndpoint.ElasticsearchSettingsProperty(
                endpoint_uri="endpointUri",
                error_retry_duration=123,
                full_load_error_percentage=123,
                service_access_role_arn="serviceAccessRoleArn"
            ),
            endpoint_identifier="endpointIdentifier",
            extra_connection_attributes="extraConnectionAttributes",
            gcp_my_sql_settings=dms.CfnEndpoint.GcpMySQLSettingsProperty(
                after_connect_script="afterConnectScript",
                clean_source_metadata_on_mismatch=False,
                database_name="databaseName",
                events_poll_interval=123,
                max_file_size=123,
                parallel_load_threads=123,
                password="password",
                port=123,
                secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                secrets_manager_secret_id="secretsManagerSecretId",
                server_name="serverName",
                server_timezone="serverTimezone",
                username="username"
            ),
            ibm_db2_settings=dms.CfnEndpoint.IbmDb2SettingsProperty(
                current_lsn="currentLsn",
                max_kBytes_per_read=123,
                secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                secrets_manager_secret_id="secretsManagerSecretId",
                set_data_capture_changes=False
            ),
            kafka_settings=dms.CfnEndpoint.KafkaSettingsProperty(
                broker="broker",
                include_control_details=False,
                include_null_and_empty=False,
                include_partition_value=False,
                include_table_alter_operations=False,
                include_transaction_details=False,
                message_format="messageFormat",
                message_max_bytes=123,
                no_hex_prefix=False,
                partition_include_schema_table=False,
                sasl_password="saslPassword",
                sasl_user_name="saslUserName",
                security_protocol="securityProtocol",
                ssl_ca_certificate_arn="sslCaCertificateArn",
                ssl_client_certificate_arn="sslClientCertificateArn",
                ssl_client_key_arn="sslClientKeyArn",
                ssl_client_key_password="sslClientKeyPassword",
                topic="topic"
            ),
            kinesis_settings=dms.CfnEndpoint.KinesisSettingsProperty(
                include_control_details=False,
                include_null_and_empty=False,
                include_partition_value=False,
                include_table_alter_operations=False,
                include_transaction_details=False,
                message_format="messageFormat",
                no_hex_prefix=False,
                partition_include_schema_table=False,
                service_access_role_arn="serviceAccessRoleArn",
                stream_arn="streamArn"
            ),
            kms_key_id="kmsKeyId",
            microsoft_sql_server_settings=dms.CfnEndpoint.MicrosoftSqlServerSettingsProperty(
                bcp_packet_size=123,
                control_tables_file_group="controlTablesFileGroup",
                query_single_always_on_node=False,
                read_backup_only=False,
                safeguard_policy="safeguardPolicy",
                secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                secrets_manager_secret_id="secretsManagerSecretId",
                use_bcp_full_load=False,
                use_third_party_backup_device=False
            ),
            mongo_db_settings=dms.CfnEndpoint.MongoDbSettingsProperty(
                auth_mechanism="authMechanism",
                auth_source="authSource",
                auth_type="authType",
                database_name="databaseName",
                docs_to_investigate="docsToInvestigate",
                extract_doc_id="extractDocId",
                nesting_level="nestingLevel",
                password="password",
                port=123,
                secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                secrets_manager_secret_id="secretsManagerSecretId",
                server_name="serverName",
                username="username"
            ),
            my_sql_settings=dms.CfnEndpoint.MySqlSettingsProperty(
                after_connect_script="afterConnectScript",
                clean_source_metadata_on_mismatch=False,
                events_poll_interval=123,
                max_file_size=123,
                parallel_load_threads=123,
                secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                secrets_manager_secret_id="secretsManagerSecretId",
                server_timezone="serverTimezone",
                target_db_type="targetDbType"
            ),
            neptune_settings=dms.CfnEndpoint.NeptuneSettingsProperty(
                error_retry_duration=123,
                iam_auth_enabled=False,
                max_file_size=123,
                max_retry_count=123,
                s3_bucket_folder="s3BucketFolder",
                s3_bucket_name="s3BucketName",
                service_access_role_arn="serviceAccessRoleArn"
            ),
            oracle_settings=dms.CfnEndpoint.OracleSettingsProperty(
                access_alternate_directly=False,
                additional_archived_log_dest_id=123,
                add_supplemental_logging=False,
                allow_select_nested_tables=False,
                archived_log_dest_id=123,
                archived_logs_only=False,
                asm_password="asmPassword",
                asm_server="asmServer",
                asm_user="asmUser",
                char_length_semantics="charLengthSemantics",
                direct_path_no_log=False,
                direct_path_parallel_load=False,
                enable_homogenous_tablespace=False,
                extra_archived_log_dest_ids=[123],
                fail_tasks_on_lob_truncation=False,
                number_datatype_scale=123,
                oracle_path_prefix="oraclePathPrefix",
                parallel_asm_read_threads=123,
                read_ahead_blocks=123,
                read_table_space_name=False,
                replace_path_prefix=False,
                retry_interval=123,
                secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                secrets_manager_oracle_asm_access_role_arn="secretsManagerOracleAsmAccessRoleArn",
                secrets_manager_oracle_asm_secret_id="secretsManagerOracleAsmSecretId",
                secrets_manager_secret_id="secretsManagerSecretId",
                security_db_encryption="securityDbEncryption",
                security_db_encryption_name="securityDbEncryptionName",
                spatial_data_option_to_geo_json_function_name="spatialDataOptionToGeoJsonFunctionName",
                standby_delay_time=123,
                use_alternate_folder_for_online=False,
                use_bFile=False,
                use_direct_path_full_load=False,
                use_logminer_reader=False,
                use_path_prefix="usePathPrefix"
            ),
            password="password",
            port=123,
            postgre_sql_settings=dms.CfnEndpoint.PostgreSqlSettingsProperty(
                after_connect_script="afterConnectScript",
                capture_ddls=False,
                ddl_artifacts_schema="ddlArtifactsSchema",
                execute_timeout=123,
                fail_tasks_on_lob_truncation=False,
                heartbeat_enable=False,
                heartbeat_frequency=123,
                heartbeat_schema="heartbeatSchema",
                max_file_size=123,
                plugin_name="pluginName",
                secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                secrets_manager_secret_id="secretsManagerSecretId",
                slot_name="slotName"
            ),
            redis_settings=dms.CfnEndpoint.RedisSettingsProperty(
                auth_password="authPassword",
                auth_type="authType",
                auth_user_name="authUserName",
                port=123,
                server_name="serverName",
                ssl_ca_certificate_arn="sslCaCertificateArn",
                ssl_security_protocol="sslSecurityProtocol"
            ),
            redshift_settings=dms.CfnEndpoint.RedshiftSettingsProperty(
                accept_any_date=False,
                after_connect_script="afterConnectScript",
                bucket_folder="bucketFolder",
                bucket_name="bucketName",
                case_sensitive_names=False,
                comp_update=False,
                connection_timeout=123,
                date_format="dateFormat",
                empty_as_null=False,
                encryption_mode="encryptionMode",
                explicit_ids=False,
                file_transfer_upload_streams=123,
                load_timeout=123,
                max_file_size=123,
                remove_quotes=False,
                replace_chars="replaceChars",
                replace_invalid_chars="replaceInvalidChars",
                secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                secrets_manager_secret_id="secretsManagerSecretId",
                server_side_encryption_kms_key_id="serverSideEncryptionKmsKeyId",
                service_access_role_arn="serviceAccessRoleArn",
                time_format="timeFormat",
                trim_blanks=False,
                truncate_columns=False,
                write_buffer_size=123
            ),
            resource_identifier="resourceIdentifier",
            s3_settings=dms.CfnEndpoint.S3SettingsProperty(
                add_column_name=False,
                bucket_folder="bucketFolder",
                bucket_name="bucketName",
                canned_acl_for_objects="cannedAclForObjects",
                cdc_inserts_and_updates=False,
                cdc_inserts_only=False,
                cdc_max_batch_interval=123,
                cdc_min_file_size=123,
                cdc_path="cdcPath",
                compression_type="compressionType",
                csv_delimiter="csvDelimiter",
                csv_no_sup_value="csvNoSupValue",
                csv_null_value="csvNullValue",
                csv_row_delimiter="csvRowDelimiter",
                data_format="dataFormat",
                data_page_size=123,
                date_partition_delimiter="datePartitionDelimiter",
                date_partition_enabled=False,
                date_partition_sequence="datePartitionSequence",
                date_partition_timezone="datePartitionTimezone",
                dict_page_size_limit=123,
                enable_statistics=False,
                encoding_type="encodingType",
                encryption_mode="encryptionMode",
                external_table_definition="externalTableDefinition",
                ignore_header_rows=123,
                include_op_for_full_load=False,
                max_file_size=123,
                parquet_timestamp_in_millisecond=False,
                parquet_version="parquetVersion",
                preserve_transactions=False,
                rfc4180=False,
                row_group_length=123,
                server_side_encryption_kms_key_id="serverSideEncryptionKmsKeyId",
                service_access_role_arn="serviceAccessRoleArn",
                timestamp_column_name="timestampColumnName",
                use_csv_no_sup_value=False,
                use_task_start_time_for_full_load_timestamp=False
            ),
            server_name="serverName",
            ssl_mode="sslMode",
            sybase_settings=dms.CfnEndpoint.SybaseSettingsProperty(
                secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                secrets_manager_secret_id="secretsManagerSecretId"
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            username="username"
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        endpoint_type: builtins.str,
        engine_name: builtins.str,
        certificate_arn: typing.Optional[builtins.str] = None,
        database_name: typing.Optional[builtins.str] = None,
        doc_db_settings: typing.Optional[typing.Union[typing.Union["CfnEndpoint.DocDbSettingsProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        dynamo_db_settings: typing.Optional[typing.Union[typing.Union["CfnEndpoint.DynamoDbSettingsProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        elasticsearch_settings: typing.Optional[typing.Union[typing.Union["CfnEndpoint.ElasticsearchSettingsProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        endpoint_identifier: typing.Optional[builtins.str] = None,
        extra_connection_attributes: typing.Optional[builtins.str] = None,
        gcp_my_sql_settings: typing.Optional[typing.Union[typing.Union["CfnEndpoint.GcpMySQLSettingsProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        ibm_db2_settings: typing.Optional[typing.Union[typing.Union["CfnEndpoint.IbmDb2SettingsProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        kafka_settings: typing.Optional[typing.Union[typing.Union["CfnEndpoint.KafkaSettingsProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        kinesis_settings: typing.Optional[typing.Union[typing.Union["CfnEndpoint.KinesisSettingsProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        microsoft_sql_server_settings: typing.Optional[typing.Union[typing.Union["CfnEndpoint.MicrosoftSqlServerSettingsProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        mongo_db_settings: typing.Optional[typing.Union[typing.Union["CfnEndpoint.MongoDbSettingsProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        my_sql_settings: typing.Optional[typing.Union[typing.Union["CfnEndpoint.MySqlSettingsProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        neptune_settings: typing.Optional[typing.Union[typing.Union["CfnEndpoint.NeptuneSettingsProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        oracle_settings: typing.Optional[typing.Union[typing.Union["CfnEndpoint.OracleSettingsProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        password: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        postgre_sql_settings: typing.Optional[typing.Union[typing.Union["CfnEndpoint.PostgreSqlSettingsProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        redis_settings: typing.Optional[typing.Union[typing.Union["CfnEndpoint.RedisSettingsProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        redshift_settings: typing.Optional[typing.Union[typing.Union["CfnEndpoint.RedshiftSettingsProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        resource_identifier: typing.Optional[builtins.str] = None,
        s3_settings: typing.Optional[typing.Union[typing.Union["CfnEndpoint.S3SettingsProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        server_name: typing.Optional[builtins.str] = None,
        ssl_mode: typing.Optional[builtins.str] = None,
        sybase_settings: typing.Optional[typing.Union[typing.Union["CfnEndpoint.SybaseSettingsProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::DMS::Endpoint``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param endpoint_type: The type of endpoint. Valid values are ``source`` and ``target`` .
        :param engine_name: The type of engine for the endpoint, depending on the ``EndpointType`` value. *Valid values* : ``mysql`` | ``oracle`` | ``postgres`` | ``mariadb`` | ``aurora`` | ``aurora-postgresql`` | ``opensearch`` | ``redshift`` | ``s3`` | ``db2`` | ``azuredb`` | ``sybase`` | ``dynamodb`` | ``mongodb`` | ``kinesis`` | ``kafka`` | ``elasticsearch`` | ``docdb`` | ``sqlserver`` | ``neptune``
        :param certificate_arn: The Amazon Resource Name (ARN) for the certificate.
        :param database_name: The name of the endpoint database. For a MySQL source or target endpoint, don't specify ``DatabaseName`` . To migrate to a specific database, use this setting and ``targetDbType`` .
        :param doc_db_settings: Settings in JSON format for the source and target DocumentDB endpoint. For more information about other available settings, see `Using extra connections attributes with Amazon DocumentDB as a source <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.DocumentDB.html#CHAP_Source.DocumentDB.ECAs>`_ and `Using Amazon DocumentDB as a target for AWS Database Migration Service <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.DocumentDB.html>`_ in the *AWS Database Migration Service User Guide* .
        :param dynamo_db_settings: Settings in JSON format for the target Amazon DynamoDB endpoint. For information about other available settings, see `Using object mapping to migrate data to DynamoDB <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.DynamoDB.html#CHAP_Target.DynamoDB.ObjectMapping>`_ in the *AWS Database Migration Service User Guide* .
        :param elasticsearch_settings: Settings in JSON format for the target OpenSearch endpoint. For more information about the available settings, see `Extra connection attributes when using OpenSearch as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Elasticsearch.html#CHAP_Target.Elasticsearch.Configuration>`_ in the *AWS Database Migration Service User Guide* .
        :param endpoint_identifier: The database endpoint identifier. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen, or contain two consecutive hyphens.
        :param extra_connection_attributes: Additional attributes associated with the connection. Each attribute is specified as a name-value pair associated by an equal sign (=). Multiple attributes are separated by a semicolon (;) with no additional white space. For information on the attributes available for connecting your source or target endpoint, see `Working with AWS DMS Endpoints <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Endpoints.html>`_ in the *AWS Database Migration Service User Guide* .
        :param gcp_my_sql_settings: Settings in JSON format for the source GCP MySQL endpoint. These settings are much the same as the settings for any MySQL-compatible endpoint. For more information, see `Extra connection attributes when using MySQL as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html#CHAP_Source.MySQL.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .
        :param ibm_db2_settings: Settings in JSON format for the source IBM Db2 LUW endpoint. For information about other available settings, see `Extra connection attributes when using Db2 LUW as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.DB2.html#CHAP_Source.DB2.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .
        :param kafka_settings: Settings in JSON format for the target Apache Kafka endpoint. For more information about other available settings, see `Using object mapping to migrate data to a Kafka topic <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kafka.html#CHAP_Target.Kafka.ObjectMapping>`_ in the *AWS Database Migration Service User Guide* .
        :param kinesis_settings: Settings in JSON format for the target endpoint for Amazon Kinesis Data Streams. For more information about other available settings, see `Using object mapping to migrate data to a Kinesis data stream <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kinesis.html#CHAP_Target.Kinesis.ObjectMapping>`_ in the *AWS Database Migration Service User Guide* .
        :param kms_key_id: An AWS KMS key identifier that is used to encrypt the connection parameters for the endpoint. If you don't specify a value for the ``KmsKeyId`` parameter, AWS DMS uses your default encryption key. AWS KMS creates the default encryption key for your AWS account . Your AWS account has a different default encryption key for each AWS Region .
        :param microsoft_sql_server_settings: Settings in JSON format for the source and target Microsoft SQL Server endpoint. For information about other available settings, see `Extra connection attributes when using SQL Server as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SQLServer.html#CHAP_Source.SQLServer.ConnectionAttrib>`_ and `Extra connection attributes when using SQL Server as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.SQLServer.html#CHAP_Target.SQLServer.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .
        :param mongo_db_settings: Settings in JSON format for the source MongoDB endpoint. For more information about the available settings, see `Using MongoDB as a target for AWS Database Migration Service <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MongoDB.html#CHAP_Source.MongoDB.Configuration>`_ in the *AWS Database Migration Service User Guide* .
        :param my_sql_settings: Settings in JSON format for the source and target MySQL endpoint. For information about other available settings, see `Extra connection attributes when using MySQL as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html#CHAP_Source.MySQL.ConnectionAttrib>`_ and `Extra connection attributes when using a MySQL-compatible database as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.MySQL.html#CHAP_Target.MySQL.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .
        :param neptune_settings: Settings in JSON format for the target Amazon Neptune endpoint. For more information about the available settings, see `Specifying endpoint settings for Amazon Neptune as a target <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Neptune.html#CHAP_Target.Neptune.EndpointSettings>`_ in the *AWS Database Migration Service User Guide* .
        :param oracle_settings: Settings in JSON format for the source and target Oracle endpoint. For information about other available settings, see `Extra connection attributes when using Oracle as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.ConnectionAttrib>`_ and `Extra connection attributes when using Oracle as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Oracle.html#CHAP_Target.Oracle.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .
        :param password: The password to be used to log in to the endpoint database.
        :param port: The port used by the endpoint database.
        :param postgre_sql_settings: Settings in JSON format for the source and target PostgreSQL endpoint. For information about other available settings, see `Extra connection attributes when using PostgreSQL as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.PostgreSQL.html#CHAP_Source.PostgreSQL.ConnectionAttrib>`_ and `Extra connection attributes when using PostgreSQL as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.PostgreSQL.html#CHAP_Target.PostgreSQL.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .
        :param redis_settings: Settings in JSON format for the target Redis endpoint. For information about other available settings, see `Specifying endpoint settings for Redis as a target <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Redis.html#CHAP_Target.Redis.EndpointSettings>`_ in the *AWS Database Migration Service User Guide* .
        :param redshift_settings: Settings in JSON format for the Amazon Redshift endpoint. For more information about other available settings, see `Extra connection attributes when using Amazon Redshift as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Redshift.html#CHAP_Target.Redshift.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .
        :param resource_identifier: A display name for the resource identifier at the end of the ``EndpointArn`` response parameter that is returned in the created ``Endpoint`` object. The value for this parameter can have up to 31 characters. It can contain only ASCII letters, digits, and hyphen ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter, such as ``Example-App-ARN1`` . For example, this value might result in the ``EndpointArn`` value ``arn:aws:dms:eu-west-1:012345678901:rep:Example-App-ARN1`` . If you don't specify a ``ResourceIdentifier`` value, AWS DMS generates a default identifier value for the end of ``EndpointArn`` .
        :param s3_settings: Settings in JSON format for the source and target Amazon S3 endpoint. For more information about other available settings, see `Extra connection attributes when using Amazon S3 as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.S3.html#CHAP_Source.S3.Configuring>`_ and `Extra connection attributes when using Amazon S3 as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring>`_ in the *AWS Database Migration Service User Guide* .
        :param server_name: The name of the server where the endpoint database resides.
        :param ssl_mode: The Secure Sockets Layer (SSL) mode to use for the SSL connection. The default is ``none`` . .. epigraph:: When ``engine_name`` is set to S3, the only allowed value is ``none`` .
        :param sybase_settings: Settings in JSON format for the source and target SAP ASE endpoint. For information about other available settings, see `Extra connection attributes when using SAP ASE as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SAP.html#CHAP_Source.SAP.ConnectionAttrib>`_ and `Extra connection attributes when using SAP ASE as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.SAP.html#CHAP_Target.SAP.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .
        :param tags: One or more tags to be assigned to the endpoint.
        :param username: The user name to be used to log in to the endpoint database.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b80cb01550182c42f97c84801688a4219f207ab936e9783f1e911db3806e295a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEndpointProps(
            endpoint_type=endpoint_type,
            engine_name=engine_name,
            certificate_arn=certificate_arn,
            database_name=database_name,
            doc_db_settings=doc_db_settings,
            dynamo_db_settings=dynamo_db_settings,
            elasticsearch_settings=elasticsearch_settings,
            endpoint_identifier=endpoint_identifier,
            extra_connection_attributes=extra_connection_attributes,
            gcp_my_sql_settings=gcp_my_sql_settings,
            ibm_db2_settings=ibm_db2_settings,
            kafka_settings=kafka_settings,
            kinesis_settings=kinesis_settings,
            kms_key_id=kms_key_id,
            microsoft_sql_server_settings=microsoft_sql_server_settings,
            mongo_db_settings=mongo_db_settings,
            my_sql_settings=my_sql_settings,
            neptune_settings=neptune_settings,
            oracle_settings=oracle_settings,
            password=password,
            port=port,
            postgre_sql_settings=postgre_sql_settings,
            redis_settings=redis_settings,
            redshift_settings=redshift_settings,
            resource_identifier=resource_identifier,
            s3_settings=s3_settings,
            server_name=server_name,
            ssl_mode=ssl_mode,
            sybase_settings=sybase_settings,
            tags=tags,
            username=username,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2042813baa1c1096c0ac960beceffaf958fe9e9101f69d5ea2dd3f9ae221384)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6fac39ac07c8358ab2389fcf1be93f2f7c07e208334af5c21ecdfc4f97604630)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrExternalId")
    def attr_external_id(self) -> builtins.str:
        '''A value that can be used for cross-account validation.

        :cloudformationAttribute: ExternalId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrExternalId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''One or more tags to be assigned to the endpoint.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="endpointType")
    def endpoint_type(self) -> builtins.str:
        '''The type of endpoint.

        Valid values are ``source`` and ``target`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-endpointtype
        '''
        return typing.cast(builtins.str, jsii.get(self, "endpointType"))

    @endpoint_type.setter
    def endpoint_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b70e3048cb5084f9d84e4aa2c4e868cca681866dbe60d1b345df05989ead56e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointType", value)

    @builtins.property
    @jsii.member(jsii_name="engineName")
    def engine_name(self) -> builtins.str:
        '''The type of engine for the endpoint, depending on the ``EndpointType`` value.

        *Valid values* : ``mysql`` | ``oracle`` | ``postgres`` | ``mariadb`` | ``aurora`` | ``aurora-postgresql`` | ``opensearch`` | ``redshift`` | ``s3`` | ``db2`` | ``azuredb`` | ``sybase`` | ``dynamodb`` | ``mongodb`` | ``kinesis`` | ``kafka`` | ``elasticsearch`` | ``docdb`` | ``sqlserver`` | ``neptune``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-enginename
        '''
        return typing.cast(builtins.str, jsii.get(self, "engineName"))

    @engine_name.setter
    def engine_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36111ba9dee88e796f732bfe8f6fb7caae87359f0fbb10fffec894d6cb3f2baf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engineName", value)

    @builtins.property
    @jsii.member(jsii_name="certificateArn")
    def certificate_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) for the certificate.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-certificatearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateArn"))

    @certificate_arn.setter
    def certificate_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71b73a99af429b60f2650588b5d17e2d43ff0ff5cf1a84371a866e10e0212f03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateArn", value)

    @builtins.property
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> typing.Optional[builtins.str]:
        '''The name of the endpoint database.

        For a MySQL source or target endpoint, don't specify ``DatabaseName`` . To migrate to a specific database, use this setting and ``targetDbType`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-databasename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseName"))

    @database_name.setter
    def database_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3d2f46c0259759c3f4bfd34159da2d8860b465dd17753b65f65a23a9222b8e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseName", value)

    @builtins.property
    @jsii.member(jsii_name="docDbSettings")
    def doc_db_settings(
        self,
    ) -> typing.Optional[typing.Union["CfnEndpoint.DocDbSettingsProperty", _IResolvable_a771d0ef]]:
        '''Settings in JSON format for the source and target DocumentDB endpoint.

        For more information about other available settings, see `Using extra connections attributes with Amazon DocumentDB as a source <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.DocumentDB.html#CHAP_Source.DocumentDB.ECAs>`_ and `Using Amazon DocumentDB as a target for AWS Database Migration Service <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.DocumentDB.html>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-docdbsettings
        '''
        return typing.cast(typing.Optional[typing.Union["CfnEndpoint.DocDbSettingsProperty", _IResolvable_a771d0ef]], jsii.get(self, "docDbSettings"))

    @doc_db_settings.setter
    def doc_db_settings(
        self,
        value: typing.Optional[typing.Union["CfnEndpoint.DocDbSettingsProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1120b87703d042c0d113f94d99d58995a7dbb2d6bbfe4131fa13245992f7edc3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "docDbSettings", value)

    @builtins.property
    @jsii.member(jsii_name="dynamoDbSettings")
    def dynamo_db_settings(
        self,
    ) -> typing.Optional[typing.Union["CfnEndpoint.DynamoDbSettingsProperty", _IResolvable_a771d0ef]]:
        '''Settings in JSON format for the target Amazon DynamoDB endpoint.

        For information about other available settings, see `Using object mapping to migrate data to DynamoDB <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.DynamoDB.html#CHAP_Target.DynamoDB.ObjectMapping>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-dynamodbsettings
        '''
        return typing.cast(typing.Optional[typing.Union["CfnEndpoint.DynamoDbSettingsProperty", _IResolvable_a771d0ef]], jsii.get(self, "dynamoDbSettings"))

    @dynamo_db_settings.setter
    def dynamo_db_settings(
        self,
        value: typing.Optional[typing.Union["CfnEndpoint.DynamoDbSettingsProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f5ae59f17daf8acc4379d9bb5fe7de5abeaf6694b06d0248dd0b07b7dd9ca38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dynamoDbSettings", value)

    @builtins.property
    @jsii.member(jsii_name="elasticsearchSettings")
    def elasticsearch_settings(
        self,
    ) -> typing.Optional[typing.Union["CfnEndpoint.ElasticsearchSettingsProperty", _IResolvable_a771d0ef]]:
        '''Settings in JSON format for the target OpenSearch endpoint.

        For more information about the available settings, see `Extra connection attributes when using OpenSearch as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Elasticsearch.html#CHAP_Target.Elasticsearch.Configuration>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-elasticsearchsettings
        '''
        return typing.cast(typing.Optional[typing.Union["CfnEndpoint.ElasticsearchSettingsProperty", _IResolvable_a771d0ef]], jsii.get(self, "elasticsearchSettings"))

    @elasticsearch_settings.setter
    def elasticsearch_settings(
        self,
        value: typing.Optional[typing.Union["CfnEndpoint.ElasticsearchSettingsProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3190e88c08339bcbabe7ab7335318fdefe45dfe697cf6d4e28cd5344ef67ac59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elasticsearchSettings", value)

    @builtins.property
    @jsii.member(jsii_name="endpointIdentifier")
    def endpoint_identifier(self) -> typing.Optional[builtins.str]:
        '''The database endpoint identifier.

        Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen, or contain two consecutive hyphens.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-endpointidentifier
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointIdentifier"))

    @endpoint_identifier.setter
    def endpoint_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b0dbaddc79e1f97c356c0aa921ef4dedf80cab928da7cf17b90c860f4636f3c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="extraConnectionAttributes")
    def extra_connection_attributes(self) -> typing.Optional[builtins.str]:
        '''Additional attributes associated with the connection.

        Each attribute is specified as a name-value pair associated by an equal sign (=). Multiple attributes are separated by a semicolon (;) with no additional white space. For information on the attributes available for connecting your source or target endpoint, see `Working with AWS DMS Endpoints <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Endpoints.html>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-extraconnectionattributes
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "extraConnectionAttributes"))

    @extra_connection_attributes.setter
    def extra_connection_attributes(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__471feade4152dc0e46bf911d1f434fbaa7677edb330b1ba73dc651c3fd5577a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "extraConnectionAttributes", value)

    @builtins.property
    @jsii.member(jsii_name="gcpMySqlSettings")
    def gcp_my_sql_settings(
        self,
    ) -> typing.Optional[typing.Union["CfnEndpoint.GcpMySQLSettingsProperty", _IResolvable_a771d0ef]]:
        '''Settings in JSON format for the source GCP MySQL endpoint.

        These settings are much the same as the settings for any MySQL-compatible endpoint. For more information, see `Extra connection attributes when using MySQL as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html#CHAP_Source.MySQL.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-gcpmysqlsettings
        '''
        return typing.cast(typing.Optional[typing.Union["CfnEndpoint.GcpMySQLSettingsProperty", _IResolvable_a771d0ef]], jsii.get(self, "gcpMySqlSettings"))

    @gcp_my_sql_settings.setter
    def gcp_my_sql_settings(
        self,
        value: typing.Optional[typing.Union["CfnEndpoint.GcpMySQLSettingsProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__676e92674b3a8b72cfa3018ece21734f3ba08bf12a853b3973abc95817a00c3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gcpMySqlSettings", value)

    @builtins.property
    @jsii.member(jsii_name="ibmDb2Settings")
    def ibm_db2_settings(
        self,
    ) -> typing.Optional[typing.Union["CfnEndpoint.IbmDb2SettingsProperty", _IResolvable_a771d0ef]]:
        '''Settings in JSON format for the source IBM Db2 LUW endpoint.

        For information about other available settings, see `Extra connection attributes when using Db2 LUW as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.DB2.html#CHAP_Source.DB2.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-ibmdb2settings
        '''
        return typing.cast(typing.Optional[typing.Union["CfnEndpoint.IbmDb2SettingsProperty", _IResolvable_a771d0ef]], jsii.get(self, "ibmDb2Settings"))

    @ibm_db2_settings.setter
    def ibm_db2_settings(
        self,
        value: typing.Optional[typing.Union["CfnEndpoint.IbmDb2SettingsProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1e2595f5be5c8fa25c5ec8eb41077880b98d0d00b0d98d30464d0f57bfc4679)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ibmDb2Settings", value)

    @builtins.property
    @jsii.member(jsii_name="kafkaSettings")
    def kafka_settings(
        self,
    ) -> typing.Optional[typing.Union["CfnEndpoint.KafkaSettingsProperty", _IResolvable_a771d0ef]]:
        '''Settings in JSON format for the target Apache Kafka endpoint.

        For more information about other available settings, see `Using object mapping to migrate data to a Kafka topic <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kafka.html#CHAP_Target.Kafka.ObjectMapping>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-kafkasettings
        '''
        return typing.cast(typing.Optional[typing.Union["CfnEndpoint.KafkaSettingsProperty", _IResolvable_a771d0ef]], jsii.get(self, "kafkaSettings"))

    @kafka_settings.setter
    def kafka_settings(
        self,
        value: typing.Optional[typing.Union["CfnEndpoint.KafkaSettingsProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14678eb823011b903079a8ba375dd724cf9a8bca5d5ad96e7bd7ad9fcc2d4367)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kafkaSettings", value)

    @builtins.property
    @jsii.member(jsii_name="kinesisSettings")
    def kinesis_settings(
        self,
    ) -> typing.Optional[typing.Union["CfnEndpoint.KinesisSettingsProperty", _IResolvable_a771d0ef]]:
        '''Settings in JSON format for the target endpoint for Amazon Kinesis Data Streams.

        For more information about other available settings, see `Using object mapping to migrate data to a Kinesis data stream <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kinesis.html#CHAP_Target.Kinesis.ObjectMapping>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-kinesissettings
        '''
        return typing.cast(typing.Optional[typing.Union["CfnEndpoint.KinesisSettingsProperty", _IResolvable_a771d0ef]], jsii.get(self, "kinesisSettings"))

    @kinesis_settings.setter
    def kinesis_settings(
        self,
        value: typing.Optional[typing.Union["CfnEndpoint.KinesisSettingsProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__418213c4c9ab68626c51ff6e44f646ed99d9fde2bcadb8ab392aed65074bb4fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kinesisSettings", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''An AWS KMS key identifier that is used to encrypt the connection parameters for the endpoint.

        If you don't specify a value for the ``KmsKeyId`` parameter, AWS DMS uses your default encryption key.

        AWS KMS creates the default encryption key for your AWS account . Your AWS account has a different default encryption key for each AWS Region .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-kmskeyid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a34e72cc1fff2080b1994b47ea9da8148c1879d16020b37a2e32a62feb3c2915)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="microsoftSqlServerSettings")
    def microsoft_sql_server_settings(
        self,
    ) -> typing.Optional[typing.Union["CfnEndpoint.MicrosoftSqlServerSettingsProperty", _IResolvable_a771d0ef]]:
        '''Settings in JSON format for the source and target Microsoft SQL Server endpoint.

        For information about other available settings, see `Extra connection attributes when using SQL Server as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SQLServer.html#CHAP_Source.SQLServer.ConnectionAttrib>`_ and `Extra connection attributes when using SQL Server as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.SQLServer.html#CHAP_Target.SQLServer.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-microsoftsqlserversettings
        '''
        return typing.cast(typing.Optional[typing.Union["CfnEndpoint.MicrosoftSqlServerSettingsProperty", _IResolvable_a771d0ef]], jsii.get(self, "microsoftSqlServerSettings"))

    @microsoft_sql_server_settings.setter
    def microsoft_sql_server_settings(
        self,
        value: typing.Optional[typing.Union["CfnEndpoint.MicrosoftSqlServerSettingsProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afbaa24445d4af14203f62cf7fa50694a4a51f03ae7f9fb9dde28842c0158158)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "microsoftSqlServerSettings", value)

    @builtins.property
    @jsii.member(jsii_name="mongoDbSettings")
    def mongo_db_settings(
        self,
    ) -> typing.Optional[typing.Union["CfnEndpoint.MongoDbSettingsProperty", _IResolvable_a771d0ef]]:
        '''Settings in JSON format for the source MongoDB endpoint.

        For more information about the available settings, see `Using MongoDB as a target for AWS Database Migration Service <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MongoDB.html#CHAP_Source.MongoDB.Configuration>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-mongodbsettings
        '''
        return typing.cast(typing.Optional[typing.Union["CfnEndpoint.MongoDbSettingsProperty", _IResolvable_a771d0ef]], jsii.get(self, "mongoDbSettings"))

    @mongo_db_settings.setter
    def mongo_db_settings(
        self,
        value: typing.Optional[typing.Union["CfnEndpoint.MongoDbSettingsProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0a4d656104d0034cdf0ecf8db38f742b0a8bb1b764befd23b869ab961758c0d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mongoDbSettings", value)

    @builtins.property
    @jsii.member(jsii_name="mySqlSettings")
    def my_sql_settings(
        self,
    ) -> typing.Optional[typing.Union["CfnEndpoint.MySqlSettingsProperty", _IResolvable_a771d0ef]]:
        '''Settings in JSON format for the source and target MySQL endpoint.

        For information about other available settings, see `Extra connection attributes when using MySQL as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html#CHAP_Source.MySQL.ConnectionAttrib>`_ and `Extra connection attributes when using a MySQL-compatible database as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.MySQL.html#CHAP_Target.MySQL.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-mysqlsettings
        '''
        return typing.cast(typing.Optional[typing.Union["CfnEndpoint.MySqlSettingsProperty", _IResolvable_a771d0ef]], jsii.get(self, "mySqlSettings"))

    @my_sql_settings.setter
    def my_sql_settings(
        self,
        value: typing.Optional[typing.Union["CfnEndpoint.MySqlSettingsProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c32b50c347948e95a16708723f156974efaa51c6cb635142ee7ffe1a46f5c821)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mySqlSettings", value)

    @builtins.property
    @jsii.member(jsii_name="neptuneSettings")
    def neptune_settings(
        self,
    ) -> typing.Optional[typing.Union["CfnEndpoint.NeptuneSettingsProperty", _IResolvable_a771d0ef]]:
        '''Settings in JSON format for the target Amazon Neptune endpoint.

        For more information about the available settings, see `Specifying endpoint settings for Amazon Neptune as a target <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Neptune.html#CHAP_Target.Neptune.EndpointSettings>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-neptunesettings
        '''
        return typing.cast(typing.Optional[typing.Union["CfnEndpoint.NeptuneSettingsProperty", _IResolvable_a771d0ef]], jsii.get(self, "neptuneSettings"))

    @neptune_settings.setter
    def neptune_settings(
        self,
        value: typing.Optional[typing.Union["CfnEndpoint.NeptuneSettingsProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__031b01d60f73af53e6d4e6ce936c2427553caa8cc09263201fa907fc04de4570)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "neptuneSettings", value)

    @builtins.property
    @jsii.member(jsii_name="oracleSettings")
    def oracle_settings(
        self,
    ) -> typing.Optional[typing.Union["CfnEndpoint.OracleSettingsProperty", _IResolvable_a771d0ef]]:
        '''Settings in JSON format for the source and target Oracle endpoint.

        For information about other available settings, see `Extra connection attributes when using Oracle as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.ConnectionAttrib>`_ and `Extra connection attributes when using Oracle as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Oracle.html#CHAP_Target.Oracle.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-oraclesettings
        '''
        return typing.cast(typing.Optional[typing.Union["CfnEndpoint.OracleSettingsProperty", _IResolvable_a771d0ef]], jsii.get(self, "oracleSettings"))

    @oracle_settings.setter
    def oracle_settings(
        self,
        value: typing.Optional[typing.Union["CfnEndpoint.OracleSettingsProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfccaff9a31133bfea110e6d6d860b621a431aa55db33fb3d2be007deed2a08c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oracleSettings", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> typing.Optional[builtins.str]:
        '''The password to be used to log in to the endpoint database.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-password
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "password"))

    @password.setter
    def password(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__245fdc73212922a23c7d84d6d92ebb70d4d1e8280e95bf17391d6f64ca42c204)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> typing.Optional[jsii.Number]:
        '''The port used by the endpoint database.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-port
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "port"))

    @port.setter
    def port(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9690ad6532fe25316497e40dd439fa7ee253ac5f2f472f662bc46b970873c70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="postgreSqlSettings")
    def postgre_sql_settings(
        self,
    ) -> typing.Optional[typing.Union["CfnEndpoint.PostgreSqlSettingsProperty", _IResolvable_a771d0ef]]:
        '''Settings in JSON format for the source and target PostgreSQL endpoint.

        For information about other available settings, see `Extra connection attributes when using PostgreSQL as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.PostgreSQL.html#CHAP_Source.PostgreSQL.ConnectionAttrib>`_ and `Extra connection attributes when using PostgreSQL as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.PostgreSQL.html#CHAP_Target.PostgreSQL.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-postgresqlsettings
        '''
        return typing.cast(typing.Optional[typing.Union["CfnEndpoint.PostgreSqlSettingsProperty", _IResolvable_a771d0ef]], jsii.get(self, "postgreSqlSettings"))

    @postgre_sql_settings.setter
    def postgre_sql_settings(
        self,
        value: typing.Optional[typing.Union["CfnEndpoint.PostgreSqlSettingsProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc691848968c1d6d50e8b7d858474a94304bce094c79dae632b5e4220c62c208)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "postgreSqlSettings", value)

    @builtins.property
    @jsii.member(jsii_name="redisSettings")
    def redis_settings(
        self,
    ) -> typing.Optional[typing.Union["CfnEndpoint.RedisSettingsProperty", _IResolvable_a771d0ef]]:
        '''Settings in JSON format for the target Redis endpoint.

        For information about other available settings, see `Specifying endpoint settings for Redis as a target <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Redis.html#CHAP_Target.Redis.EndpointSettings>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-redissettings
        '''
        return typing.cast(typing.Optional[typing.Union["CfnEndpoint.RedisSettingsProperty", _IResolvable_a771d0ef]], jsii.get(self, "redisSettings"))

    @redis_settings.setter
    def redis_settings(
        self,
        value: typing.Optional[typing.Union["CfnEndpoint.RedisSettingsProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a369014e246456df9c5c756bfd7fc8a85b93ca632b01927f9c1ebb32ff2ddd1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redisSettings", value)

    @builtins.property
    @jsii.member(jsii_name="redshiftSettings")
    def redshift_settings(
        self,
    ) -> typing.Optional[typing.Union["CfnEndpoint.RedshiftSettingsProperty", _IResolvable_a771d0ef]]:
        '''Settings in JSON format for the Amazon Redshift endpoint.

        For more information about other available settings, see `Extra connection attributes when using Amazon Redshift as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Redshift.html#CHAP_Target.Redshift.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-redshiftsettings
        '''
        return typing.cast(typing.Optional[typing.Union["CfnEndpoint.RedshiftSettingsProperty", _IResolvable_a771d0ef]], jsii.get(self, "redshiftSettings"))

    @redshift_settings.setter
    def redshift_settings(
        self,
        value: typing.Optional[typing.Union["CfnEndpoint.RedshiftSettingsProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d774c13d229e8bab977cf9a990620508801d41760bd7299019de0c11cb8358c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redshiftSettings", value)

    @builtins.property
    @jsii.member(jsii_name="resourceIdentifier")
    def resource_identifier(self) -> typing.Optional[builtins.str]:
        '''A display name for the resource identifier at the end of the ``EndpointArn`` response parameter that is returned in the created ``Endpoint`` object.

        The value for this parameter can have up to 31 characters. It can contain only ASCII letters, digits, and hyphen ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter, such as ``Example-App-ARN1`` .

        For example, this value might result in the ``EndpointArn`` value ``arn:aws:dms:eu-west-1:012345678901:rep:Example-App-ARN1`` . If you don't specify a ``ResourceIdentifier`` value, AWS DMS generates a default identifier value for the end of ``EndpointArn`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-resourceidentifier
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceIdentifier"))

    @resource_identifier.setter
    def resource_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5a006892b9a525c811f210fc6e69d5f60e15b970e3320c59cc0d0b306167b5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="s3Settings")
    def s3_settings(
        self,
    ) -> typing.Optional[typing.Union["CfnEndpoint.S3SettingsProperty", _IResolvable_a771d0ef]]:
        '''Settings in JSON format for the source and target Amazon S3 endpoint.

        For more information about other available settings, see `Extra connection attributes when using Amazon S3 as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.S3.html#CHAP_Source.S3.Configuring>`_ and `Extra connection attributes when using Amazon S3 as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-s3settings
        '''
        return typing.cast(typing.Optional[typing.Union["CfnEndpoint.S3SettingsProperty", _IResolvable_a771d0ef]], jsii.get(self, "s3Settings"))

    @s3_settings.setter
    def s3_settings(
        self,
        value: typing.Optional[typing.Union["CfnEndpoint.S3SettingsProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__398ce1cf49f22c04aa9c9ad875a6e9894d6c98d088034ac0601478e40c8ce596)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3Settings", value)

    @builtins.property
    @jsii.member(jsii_name="serverName")
    def server_name(self) -> typing.Optional[builtins.str]:
        '''The name of the server where the endpoint database resides.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-servername
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverName"))

    @server_name.setter
    def server_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2c8f32cfe4f822507c85fd661022611ecd212b975e9509e612be7b494cbeb38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverName", value)

    @builtins.property
    @jsii.member(jsii_name="sslMode")
    def ssl_mode(self) -> typing.Optional[builtins.str]:
        '''The Secure Sockets Layer (SSL) mode to use for the SSL connection. The default is ``none`` .

        .. epigraph::

           When ``engine_name`` is set to S3, the only allowed value is ``none`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-sslmode
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslMode"))

    @ssl_mode.setter
    def ssl_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8c22accc018eead3b74efafeaf1a183065ee233dcd9a31ed8cff37078fe9eb3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslMode", value)

    @builtins.property
    @jsii.member(jsii_name="sybaseSettings")
    def sybase_settings(
        self,
    ) -> typing.Optional[typing.Union["CfnEndpoint.SybaseSettingsProperty", _IResolvable_a771d0ef]]:
        '''Settings in JSON format for the source and target SAP ASE endpoint.

        For information about other available settings, see `Extra connection attributes when using SAP ASE as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SAP.html#CHAP_Source.SAP.ConnectionAttrib>`_ and `Extra connection attributes when using SAP ASE as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.SAP.html#CHAP_Target.SAP.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-sybasesettings
        '''
        return typing.cast(typing.Optional[typing.Union["CfnEndpoint.SybaseSettingsProperty", _IResolvable_a771d0ef]], jsii.get(self, "sybaseSettings"))

    @sybase_settings.setter
    def sybase_settings(
        self,
        value: typing.Optional[typing.Union["CfnEndpoint.SybaseSettingsProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b87c8e781a2d3285ddd8999e8c1f6157cf08f0573db90e15bdd0bbe00fa58d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sybaseSettings", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> typing.Optional[builtins.str]:
        '''The user name to be used to log in to the endpoint database.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-username
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "username"))

    @username.setter
    def username(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de6d2c3659f33d7556f3d0a49f7707551d65c11199e7e2f1fda7a3f4c4084475)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_dms.CfnEndpoint.DocDbSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "docs_to_investigate": "docsToInvestigate",
            "extract_doc_id": "extractDocId",
            "nesting_level": "nestingLevel",
            "secrets_manager_access_role_arn": "secretsManagerAccessRoleArn",
            "secrets_manager_secret_id": "secretsManagerSecretId",
        },
    )
    class DocDbSettingsProperty:
        def __init__(
            self,
            *,
            docs_to_investigate: typing.Optional[jsii.Number] = None,
            extract_doc_id: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            nesting_level: typing.Optional[builtins.str] = None,
            secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
            secrets_manager_secret_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides information that defines a DocumentDB endpoint.

            This information includes the output format of records applied to the endpoint and details of transaction and control table data information. For more information about other available settings, see `Using extra connections attributes with Amazon DocumentDB as a source <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.DocumentDB.html#CHAP_Source.DocumentDB.ECAs>`_ and `Using Amazon DocumentDB as a target for AWS Database Migration Service <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.DocumentDB.html>`_ in the *AWS Database Migration Service User Guide* .

            :param docs_to_investigate: Indicates the number of documents to preview to determine the document organization. Use this setting when ``NestingLevel`` is set to ``"one"`` . Must be a positive value greater than ``0`` . Default value is ``1000`` .
            :param extract_doc_id: Specifies the document ID. Use this setting when ``NestingLevel`` is set to ``"none"`` . Default value is ``"false"`` .
            :param nesting_level: Specifies either document or table mode. Default value is ``"none"`` . Specify ``"none"`` to use document mode. Specify ``"one"`` to use table mode.
            :param secrets_manager_access_role_arn: The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in ``SecretsManagerSecret`` . The role must allow the ``iam:PassRole`` action. ``SecretsManagerSecret`` has the value of the AWS Secrets Manager secret that allows access to the DocumentDB endpoint. .. epigraph:: You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerSecretId`` . Or you can specify clear-text values for ``UserName`` , ``Password`` , ``ServerName`` , and ``Port`` . You can't specify both. For more information on creating this ``SecretsManagerSecret`` , the corresponding ``SecretsManagerAccessRoleArn`` , and the ``SecretsManagerSecretId`` that is required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .
            :param secrets_manager_secret_id: The full ARN, partial ARN, or display name of the ``SecretsManagerSecret`` that contains the DocumentDB endpoint connection details.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-docdbsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dms as dms
                
                doc_db_settings_property = dms.CfnEndpoint.DocDbSettingsProperty(
                    docs_to_investigate=123,
                    extract_doc_id=False,
                    nesting_level="nestingLevel",
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_secret_id="secretsManagerSecretId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b9bf8276635c85953ae5f0c4c3b0492f4aa31f1ed93aff08b1590f79fc9178cf)
                check_type(argname="argument docs_to_investigate", value=docs_to_investigate, expected_type=type_hints["docs_to_investigate"])
                check_type(argname="argument extract_doc_id", value=extract_doc_id, expected_type=type_hints["extract_doc_id"])
                check_type(argname="argument nesting_level", value=nesting_level, expected_type=type_hints["nesting_level"])
                check_type(argname="argument secrets_manager_access_role_arn", value=secrets_manager_access_role_arn, expected_type=type_hints["secrets_manager_access_role_arn"])
                check_type(argname="argument secrets_manager_secret_id", value=secrets_manager_secret_id, expected_type=type_hints["secrets_manager_secret_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if docs_to_investigate is not None:
                self._values["docs_to_investigate"] = docs_to_investigate
            if extract_doc_id is not None:
                self._values["extract_doc_id"] = extract_doc_id
            if nesting_level is not None:
                self._values["nesting_level"] = nesting_level
            if secrets_manager_access_role_arn is not None:
                self._values["secrets_manager_access_role_arn"] = secrets_manager_access_role_arn
            if secrets_manager_secret_id is not None:
                self._values["secrets_manager_secret_id"] = secrets_manager_secret_id

        @builtins.property
        def docs_to_investigate(self) -> typing.Optional[jsii.Number]:
            '''Indicates the number of documents to preview to determine the document organization.

            Use this setting when ``NestingLevel`` is set to ``"one"`` .

            Must be a positive value greater than ``0`` . Default value is ``1000`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-docdbsettings.html#cfn-dms-endpoint-docdbsettings-docstoinvestigate
            '''
            result = self._values.get("docs_to_investigate")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def extract_doc_id(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Specifies the document ID. Use this setting when ``NestingLevel`` is set to ``"none"`` .

            Default value is ``"false"`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-docdbsettings.html#cfn-dms-endpoint-docdbsettings-extractdocid
            '''
            result = self._values.get("extract_doc_id")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def nesting_level(self) -> typing.Optional[builtins.str]:
            '''Specifies either document or table mode.

            Default value is ``"none"`` . Specify ``"none"`` to use document mode. Specify ``"one"`` to use table mode.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-docdbsettings.html#cfn-dms-endpoint-docdbsettings-nestinglevel
            '''
            result = self._values.get("nesting_level")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secrets_manager_access_role_arn(self) -> typing.Optional[builtins.str]:
            '''The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in ``SecretsManagerSecret`` .

            The role must allow the ``iam:PassRole`` action. ``SecretsManagerSecret`` has the value of the AWS Secrets Manager secret that allows access to the DocumentDB endpoint.
            .. epigraph::

               You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerSecretId`` . Or you can specify clear-text values for ``UserName`` , ``Password`` , ``ServerName`` , and ``Port`` . You can't specify both.

               For more information on creating this ``SecretsManagerSecret`` , the corresponding ``SecretsManagerAccessRoleArn`` , and the ``SecretsManagerSecretId`` that is required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-docdbsettings.html#cfn-dms-endpoint-docdbsettings-secretsmanageraccessrolearn
            '''
            result = self._values.get("secrets_manager_access_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secrets_manager_secret_id(self) -> typing.Optional[builtins.str]:
            '''The full ARN, partial ARN, or display name of the ``SecretsManagerSecret`` that contains the DocumentDB endpoint connection details.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-docdbsettings.html#cfn-dms-endpoint-docdbsettings-secretsmanagersecretid
            '''
            result = self._values.get("secrets_manager_secret_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DocDbSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dms.CfnEndpoint.DynamoDbSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"service_access_role_arn": "serviceAccessRoleArn"},
    )
    class DynamoDbSettingsProperty:
        def __init__(
            self,
            *,
            service_access_role_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides information, including the Amazon Resource Name (ARN) of the IAM role used to define an Amazon DynamoDB target endpoint.

            This information also includes the output format of records applied to the endpoint and details of transaction and control table data information. For information about other available settings, see `Using object mapping to migrate data to DynamoDB <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.DynamoDB.html#CHAP_Target.DynamoDB.ObjectMapping>`_ in the *AWS Database Migration Service User Guide* .

            :param service_access_role_arn: The Amazon Resource Name (ARN) used by the service to access the IAM role. The role must allow the ``iam:PassRole`` action.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-dynamodbsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dms as dms
                
                dynamo_db_settings_property = dms.CfnEndpoint.DynamoDbSettingsProperty(
                    service_access_role_arn="serviceAccessRoleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__41bc0e22e70470a9b4db3855416e7bfa0d12ffd2533dff28cae680ff337a0ffc)
                check_type(argname="argument service_access_role_arn", value=service_access_role_arn, expected_type=type_hints["service_access_role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if service_access_role_arn is not None:
                self._values["service_access_role_arn"] = service_access_role_arn

        @builtins.property
        def service_access_role_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) used by the service to access the IAM role.

            The role must allow the ``iam:PassRole`` action.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-dynamodbsettings.html#cfn-dms-endpoint-dynamodbsettings-serviceaccessrolearn
            '''
            result = self._values.get("service_access_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DynamoDbSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dms.CfnEndpoint.ElasticsearchSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint_uri": "endpointUri",
            "error_retry_duration": "errorRetryDuration",
            "full_load_error_percentage": "fullLoadErrorPercentage",
            "service_access_role_arn": "serviceAccessRoleArn",
        },
    )
    class ElasticsearchSettingsProperty:
        def __init__(
            self,
            *,
            endpoint_uri: typing.Optional[builtins.str] = None,
            error_retry_duration: typing.Optional[jsii.Number] = None,
            full_load_error_percentage: typing.Optional[jsii.Number] = None,
            service_access_role_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides information that defines an OpenSearch endpoint.

            This information includes the output format of records applied to the endpoint and details of transaction and control table data information. For more information about the available settings, see `Extra connection attributes when using OpenSearch as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Elasticsearch.html#CHAP_Target.Elasticsearch.Configuration>`_ in the *AWS Database Migration Service User Guide* .

            :param endpoint_uri: The endpoint for the OpenSearch cluster. AWS DMS uses HTTPS if a transport protocol (either HTTP or HTTPS) isn't specified.
            :param error_retry_duration: The maximum number of seconds for which DMS retries failed API requests to the OpenSearch cluster.
            :param full_load_error_percentage: The maximum percentage of records that can fail to be written before a full load operation stops. To avoid early failure, this counter is only effective after 1,000 records are transferred. OpenSearch also has the concept of error monitoring during the last 10 minutes of an Observation Window. If transfer of all records fail in the last 10 minutes, the full load operation stops.
            :param service_access_role_arn: The Amazon Resource Name (ARN) used by the service to access the IAM role. The role must allow the ``iam:PassRole`` action.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-elasticsearchsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dms as dms
                
                elasticsearch_settings_property = dms.CfnEndpoint.ElasticsearchSettingsProperty(
                    endpoint_uri="endpointUri",
                    error_retry_duration=123,
                    full_load_error_percentage=123,
                    service_access_role_arn="serviceAccessRoleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__682cf18e83c5c00fdb751700432cce646117b4a92d41af518f4663fa98814d2c)
                check_type(argname="argument endpoint_uri", value=endpoint_uri, expected_type=type_hints["endpoint_uri"])
                check_type(argname="argument error_retry_duration", value=error_retry_duration, expected_type=type_hints["error_retry_duration"])
                check_type(argname="argument full_load_error_percentage", value=full_load_error_percentage, expected_type=type_hints["full_load_error_percentage"])
                check_type(argname="argument service_access_role_arn", value=service_access_role_arn, expected_type=type_hints["service_access_role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if endpoint_uri is not None:
                self._values["endpoint_uri"] = endpoint_uri
            if error_retry_duration is not None:
                self._values["error_retry_duration"] = error_retry_duration
            if full_load_error_percentage is not None:
                self._values["full_load_error_percentage"] = full_load_error_percentage
            if service_access_role_arn is not None:
                self._values["service_access_role_arn"] = service_access_role_arn

        @builtins.property
        def endpoint_uri(self) -> typing.Optional[builtins.str]:
            '''The endpoint for the OpenSearch cluster.

            AWS DMS uses HTTPS if a transport protocol (either HTTP or HTTPS) isn't specified.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-elasticsearchsettings.html#cfn-dms-endpoint-elasticsearchsettings-endpointuri
            '''
            result = self._values.get("endpoint_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def error_retry_duration(self) -> typing.Optional[jsii.Number]:
            '''The maximum number of seconds for which DMS retries failed API requests to the OpenSearch cluster.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-elasticsearchsettings.html#cfn-dms-endpoint-elasticsearchsettings-errorretryduration
            '''
            result = self._values.get("error_retry_duration")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def full_load_error_percentage(self) -> typing.Optional[jsii.Number]:
            '''The maximum percentage of records that can fail to be written before a full load operation stops.

            To avoid early failure, this counter is only effective after 1,000 records are transferred. OpenSearch also has the concept of error monitoring during the last 10 minutes of an Observation Window. If transfer of all records fail in the last 10 minutes, the full load operation stops.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-elasticsearchsettings.html#cfn-dms-endpoint-elasticsearchsettings-fullloaderrorpercentage
            '''
            result = self._values.get("full_load_error_percentage")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def service_access_role_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) used by the service to access the IAM role.

            The role must allow the ``iam:PassRole`` action.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-elasticsearchsettings.html#cfn-dms-endpoint-elasticsearchsettings-serviceaccessrolearn
            '''
            result = self._values.get("service_access_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ElasticsearchSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dms.CfnEndpoint.GcpMySQLSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "after_connect_script": "afterConnectScript",
            "clean_source_metadata_on_mismatch": "cleanSourceMetadataOnMismatch",
            "database_name": "databaseName",
            "events_poll_interval": "eventsPollInterval",
            "max_file_size": "maxFileSize",
            "parallel_load_threads": "parallelLoadThreads",
            "password": "password",
            "port": "port",
            "secrets_manager_access_role_arn": "secretsManagerAccessRoleArn",
            "secrets_manager_secret_id": "secretsManagerSecretId",
            "server_name": "serverName",
            "server_timezone": "serverTimezone",
            "username": "username",
        },
    )
    class GcpMySQLSettingsProperty:
        def __init__(
            self,
            *,
            after_connect_script: typing.Optional[builtins.str] = None,
            clean_source_metadata_on_mismatch: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            database_name: typing.Optional[builtins.str] = None,
            events_poll_interval: typing.Optional[jsii.Number] = None,
            max_file_size: typing.Optional[jsii.Number] = None,
            parallel_load_threads: typing.Optional[jsii.Number] = None,
            password: typing.Optional[builtins.str] = None,
            port: typing.Optional[jsii.Number] = None,
            secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
            secrets_manager_secret_id: typing.Optional[builtins.str] = None,
            server_name: typing.Optional[builtins.str] = None,
            server_timezone: typing.Optional[builtins.str] = None,
            username: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides information that defines a GCP MySQL endpoint.

            This information includes the output format of records applied to the endpoint and details of transaction and control table data information. These settings are much the same as the settings for any MySQL-compatible endpoint. For more information, see `Extra connection attributes when using MySQL as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html#CHAP_Source.MySQL.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

            :param after_connect_script: Specifies a script to run immediately after AWS DMS connects to the endpoint. The migration task continues running regardless if the SQL statement succeeds or fails. For this parameter, provide the code of the script itself, not the name of a file containing the script.
            :param clean_source_metadata_on_mismatch: Adjusts the behavior of AWS DMS when migrating from an SQL Server source database that is hosted as part of an Always On availability group cluster. If you need AWS DMS to poll all the nodes in the Always On cluster for transaction backups, set this attribute to ``false`` .
            :param database_name: Database name for the endpoint. For a MySQL source or target endpoint, don't explicitly specify the database using the ``DatabaseName`` request parameter on either the ``CreateEndpoint`` or ``ModifyEndpoint`` API call. Specifying ``DatabaseName`` when you create or modify a MySQL endpoint replicates all the task tables to this single database. For MySQL endpoints, you specify the database only when you specify the schema in the table-mapping rules of the AWS DMS task.
            :param events_poll_interval: Specifies how often to check the binary log for new changes/events when the database is idle. The default is five seconds. Example: ``eventsPollInterval=5;`` In the example, AWS DMS checks for changes in the binary logs every five seconds.
            :param max_file_size: Specifies the maximum size (in KB) of any .csv file used to transfer data to a MySQL-compatible database. Example: ``maxFileSize=512``
            :param parallel_load_threads: Improves performance when loading data into the MySQL-compatible target database. Specifies how many threads to use to load the data into the MySQL-compatible target database. Setting a large number of threads can have an adverse effect on database performance, because a separate connection is required for each thread. The default is one. Example: ``parallelLoadThreads=1``
            :param password: Endpoint connection password.
            :param port: The port used by the endpoint database.
            :param secrets_manager_access_role_arn: The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in ``SecretsManagerSecret.`` The role must allow the ``iam:PassRole`` action. ``SecretsManagerSecret`` has the value of the AWS Secrets Manager secret that allows access to the MySQL endpoint. .. epigraph:: You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerSecretId`` . Or you can specify clear-text values for ``UserName`` , ``Password`` , ``ServerName`` , and ``Port`` . You can't specify both. For more information on creating this ``SecretsManagerSecret`` , the corresponding ``SecretsManagerAccessRoleArn`` , and the ``SecretsManagerSecretId`` required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .
            :param secrets_manager_secret_id: The full ARN, partial ARN, or display name of the ``SecretsManagerSecret`` that contains the MySQL endpoint connection details.
            :param server_name: Endpoint TCP port.
            :param server_timezone: Specifies the time zone for the source MySQL database. Don't enclose time zones in single quotation marks. Example: ``serverTimezone=US/Pacific;``
            :param username: Endpoint connection user name.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dms as dms
                
                gcp_my_sQLSettings_property = dms.CfnEndpoint.GcpMySQLSettingsProperty(
                    after_connect_script="afterConnectScript",
                    clean_source_metadata_on_mismatch=False,
                    database_name="databaseName",
                    events_poll_interval=123,
                    max_file_size=123,
                    parallel_load_threads=123,
                    password="password",
                    port=123,
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_secret_id="secretsManagerSecretId",
                    server_name="serverName",
                    server_timezone="serverTimezone",
                    username="username"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dd1c0b06c8ceaf467d835d6ab2c746c73f943852b107b3ac3d8d83df2820914e)
                check_type(argname="argument after_connect_script", value=after_connect_script, expected_type=type_hints["after_connect_script"])
                check_type(argname="argument clean_source_metadata_on_mismatch", value=clean_source_metadata_on_mismatch, expected_type=type_hints["clean_source_metadata_on_mismatch"])
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument events_poll_interval", value=events_poll_interval, expected_type=type_hints["events_poll_interval"])
                check_type(argname="argument max_file_size", value=max_file_size, expected_type=type_hints["max_file_size"])
                check_type(argname="argument parallel_load_threads", value=parallel_load_threads, expected_type=type_hints["parallel_load_threads"])
                check_type(argname="argument password", value=password, expected_type=type_hints["password"])
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
                check_type(argname="argument secrets_manager_access_role_arn", value=secrets_manager_access_role_arn, expected_type=type_hints["secrets_manager_access_role_arn"])
                check_type(argname="argument secrets_manager_secret_id", value=secrets_manager_secret_id, expected_type=type_hints["secrets_manager_secret_id"])
                check_type(argname="argument server_name", value=server_name, expected_type=type_hints["server_name"])
                check_type(argname="argument server_timezone", value=server_timezone, expected_type=type_hints["server_timezone"])
                check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if after_connect_script is not None:
                self._values["after_connect_script"] = after_connect_script
            if clean_source_metadata_on_mismatch is not None:
                self._values["clean_source_metadata_on_mismatch"] = clean_source_metadata_on_mismatch
            if database_name is not None:
                self._values["database_name"] = database_name
            if events_poll_interval is not None:
                self._values["events_poll_interval"] = events_poll_interval
            if max_file_size is not None:
                self._values["max_file_size"] = max_file_size
            if parallel_load_threads is not None:
                self._values["parallel_load_threads"] = parallel_load_threads
            if password is not None:
                self._values["password"] = password
            if port is not None:
                self._values["port"] = port
            if secrets_manager_access_role_arn is not None:
                self._values["secrets_manager_access_role_arn"] = secrets_manager_access_role_arn
            if secrets_manager_secret_id is not None:
                self._values["secrets_manager_secret_id"] = secrets_manager_secret_id
            if server_name is not None:
                self._values["server_name"] = server_name
            if server_timezone is not None:
                self._values["server_timezone"] = server_timezone
            if username is not None:
                self._values["username"] = username

        @builtins.property
        def after_connect_script(self) -> typing.Optional[builtins.str]:
            '''Specifies a script to run immediately after AWS DMS connects to the endpoint.

            The migration task continues running regardless if the SQL statement succeeds or fails.

            For this parameter, provide the code of the script itself, not the name of a file containing the script.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html#cfn-dms-endpoint-gcpmysqlsettings-afterconnectscript
            '''
            result = self._values.get("after_connect_script")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def clean_source_metadata_on_mismatch(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Adjusts the behavior of AWS DMS when migrating from an SQL Server source database that is hosted as part of an Always On availability group cluster.

            If you need AWS DMS to poll all the nodes in the Always On cluster for transaction backups, set this attribute to ``false`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html#cfn-dms-endpoint-gcpmysqlsettings-cleansourcemetadataonmismatch
            '''
            result = self._values.get("clean_source_metadata_on_mismatch")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def database_name(self) -> typing.Optional[builtins.str]:
            '''Database name for the endpoint.

            For a MySQL source or target endpoint, don't explicitly specify the database using the ``DatabaseName`` request parameter on either the ``CreateEndpoint`` or ``ModifyEndpoint`` API call. Specifying ``DatabaseName`` when you create or modify a MySQL endpoint replicates all the task tables to this single database. For MySQL endpoints, you specify the database only when you specify the schema in the table-mapping rules of the AWS DMS task.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html#cfn-dms-endpoint-gcpmysqlsettings-databasename
            '''
            result = self._values.get("database_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def events_poll_interval(self) -> typing.Optional[jsii.Number]:
            '''Specifies how often to check the binary log for new changes/events when the database is idle.

            The default is five seconds.

            Example: ``eventsPollInterval=5;``

            In the example, AWS DMS checks for changes in the binary logs every five seconds.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html#cfn-dms-endpoint-gcpmysqlsettings-eventspollinterval
            '''
            result = self._values.get("events_poll_interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_file_size(self) -> typing.Optional[jsii.Number]:
            '''Specifies the maximum size (in KB) of any .csv file used to transfer data to a MySQL-compatible database.

            Example: ``maxFileSize=512``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html#cfn-dms-endpoint-gcpmysqlsettings-maxfilesize
            '''
            result = self._values.get("max_file_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def parallel_load_threads(self) -> typing.Optional[jsii.Number]:
            '''Improves performance when loading data into the MySQL-compatible target database.

            Specifies how many threads to use to load the data into the MySQL-compatible target database. Setting a large number of threads can have an adverse effect on database performance, because a separate connection is required for each thread. The default is one.

            Example: ``parallelLoadThreads=1``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html#cfn-dms-endpoint-gcpmysqlsettings-parallelloadthreads
            '''
            result = self._values.get("parallel_load_threads")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def password(self) -> typing.Optional[builtins.str]:
            '''Endpoint connection password.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html#cfn-dms-endpoint-gcpmysqlsettings-password
            '''
            result = self._values.get("password")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def port(self) -> typing.Optional[jsii.Number]:
            '''The port used by the endpoint database.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html#cfn-dms-endpoint-gcpmysqlsettings-port
            '''
            result = self._values.get("port")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def secrets_manager_access_role_arn(self) -> typing.Optional[builtins.str]:
            '''The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in ``SecretsManagerSecret.`` The role must allow the ``iam:PassRole`` action. ``SecretsManagerSecret`` has the value of the AWS Secrets Manager secret that allows access to the MySQL endpoint.

            .. epigraph::

               You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerSecretId`` . Or you can specify clear-text values for ``UserName`` , ``Password`` , ``ServerName`` , and ``Port`` . You can't specify both.

               For more information on creating this ``SecretsManagerSecret`` , the corresponding ``SecretsManagerAccessRoleArn`` , and the ``SecretsManagerSecretId`` required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html#cfn-dms-endpoint-gcpmysqlsettings-secretsmanageraccessrolearn
            '''
            result = self._values.get("secrets_manager_access_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secrets_manager_secret_id(self) -> typing.Optional[builtins.str]:
            '''The full ARN, partial ARN, or display name of the ``SecretsManagerSecret`` that contains the MySQL endpoint connection details.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html#cfn-dms-endpoint-gcpmysqlsettings-secretsmanagersecretid
            '''
            result = self._values.get("secrets_manager_secret_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def server_name(self) -> typing.Optional[builtins.str]:
            '''Endpoint TCP port.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html#cfn-dms-endpoint-gcpmysqlsettings-servername
            '''
            result = self._values.get("server_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def server_timezone(self) -> typing.Optional[builtins.str]:
            '''Specifies the time zone for the source MySQL database. Don't enclose time zones in single quotation marks.

            Example: ``serverTimezone=US/Pacific;``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html#cfn-dms-endpoint-gcpmysqlsettings-servertimezone
            '''
            result = self._values.get("server_timezone")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def username(self) -> typing.Optional[builtins.str]:
            '''Endpoint connection user name.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html#cfn-dms-endpoint-gcpmysqlsettings-username
            '''
            result = self._values.get("username")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GcpMySQLSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dms.CfnEndpoint.IbmDb2SettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "current_lsn": "currentLsn",
            "max_k_bytes_per_read": "maxKBytesPerRead",
            "secrets_manager_access_role_arn": "secretsManagerAccessRoleArn",
            "secrets_manager_secret_id": "secretsManagerSecretId",
            "set_data_capture_changes": "setDataCaptureChanges",
        },
    )
    class IbmDb2SettingsProperty:
        def __init__(
            self,
            *,
            current_lsn: typing.Optional[builtins.str] = None,
            max_k_bytes_per_read: typing.Optional[jsii.Number] = None,
            secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
            secrets_manager_secret_id: typing.Optional[builtins.str] = None,
            set_data_capture_changes: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''Provides information that defines an IBMDB2 endpoint.

            This information includes the output format of records applied to the endpoint and details of transaction and control table data information. For more information about other available settings, see `Extra connection attributes when using Db2 LUW as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.DB2.html#CHAP_Source.DB2.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

            :param current_lsn: For ongoing replication (CDC), use CurrentLSN to specify a log sequence number (LSN) where you want the replication to start.
            :param max_k_bytes_per_read: Maximum number of bytes per read, as a NUMBER value. The default is 64 KB.
            :param secrets_manager_access_role_arn: The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in ``SecretsManagerSecret`` . The role must allow the ``iam:PassRole`` action. ``SecretsManagerSecret`` has the value ofthe AWS Secrets Manager secret that allows access to the Db2 LUW endpoint. .. epigraph:: You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerSecretId`` . Or you can specify clear-text values for ``UserName`` , ``Password`` , ``ServerName`` , and ``Port`` . You can't specify both. For more information on creating this ``SecretsManagerSecret`` , the corresponding ``SecretsManagerAccessRoleArn`` , and the ``SecretsManagerSecretId`` that is required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .
            :param secrets_manager_secret_id: The full ARN, partial ARN, or display name of the ``SecretsManagerSecret`` that contains the IBMDB2 endpoint connection details.
            :param set_data_capture_changes: Enables ongoing replication (CDC) as a BOOLEAN value. The default is true.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-ibmdb2settings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dms as dms
                
                ibm_db2_settings_property = dms.CfnEndpoint.IbmDb2SettingsProperty(
                    current_lsn="currentLsn",
                    max_kBytes_per_read=123,
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_secret_id="secretsManagerSecretId",
                    set_data_capture_changes=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b0bb9685ace29805f69a4500ec1350518c53956efb1d676ffb3a67ee5b2170c7)
                check_type(argname="argument current_lsn", value=current_lsn, expected_type=type_hints["current_lsn"])
                check_type(argname="argument max_k_bytes_per_read", value=max_k_bytes_per_read, expected_type=type_hints["max_k_bytes_per_read"])
                check_type(argname="argument secrets_manager_access_role_arn", value=secrets_manager_access_role_arn, expected_type=type_hints["secrets_manager_access_role_arn"])
                check_type(argname="argument secrets_manager_secret_id", value=secrets_manager_secret_id, expected_type=type_hints["secrets_manager_secret_id"])
                check_type(argname="argument set_data_capture_changes", value=set_data_capture_changes, expected_type=type_hints["set_data_capture_changes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if current_lsn is not None:
                self._values["current_lsn"] = current_lsn
            if max_k_bytes_per_read is not None:
                self._values["max_k_bytes_per_read"] = max_k_bytes_per_read
            if secrets_manager_access_role_arn is not None:
                self._values["secrets_manager_access_role_arn"] = secrets_manager_access_role_arn
            if secrets_manager_secret_id is not None:
                self._values["secrets_manager_secret_id"] = secrets_manager_secret_id
            if set_data_capture_changes is not None:
                self._values["set_data_capture_changes"] = set_data_capture_changes

        @builtins.property
        def current_lsn(self) -> typing.Optional[builtins.str]:
            '''For ongoing replication (CDC), use CurrentLSN to specify a log sequence number (LSN) where you want the replication to start.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-ibmdb2settings.html#cfn-dms-endpoint-ibmdb2settings-currentlsn
            '''
            result = self._values.get("current_lsn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def max_k_bytes_per_read(self) -> typing.Optional[jsii.Number]:
            '''Maximum number of bytes per read, as a NUMBER value.

            The default is 64 KB.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-ibmdb2settings.html#cfn-dms-endpoint-ibmdb2settings-maxkbytesperread
            '''
            result = self._values.get("max_k_bytes_per_read")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def secrets_manager_access_role_arn(self) -> typing.Optional[builtins.str]:
            '''The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in ``SecretsManagerSecret`` .

            The role must allow the ``iam:PassRole`` action. ``SecretsManagerSecret`` has the value ofthe AWS Secrets Manager secret that allows access to the Db2 LUW endpoint.
            .. epigraph::

               You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerSecretId`` . Or you can specify clear-text values for ``UserName`` , ``Password`` , ``ServerName`` , and ``Port`` . You can't specify both.

               For more information on creating this ``SecretsManagerSecret`` , the corresponding ``SecretsManagerAccessRoleArn`` , and the ``SecretsManagerSecretId`` that is required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-ibmdb2settings.html#cfn-dms-endpoint-ibmdb2settings-secretsmanageraccessrolearn
            '''
            result = self._values.get("secrets_manager_access_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secrets_manager_secret_id(self) -> typing.Optional[builtins.str]:
            '''The full ARN, partial ARN, or display name of the ``SecretsManagerSecret`` that contains the IBMDB2 endpoint connection details.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-ibmdb2settings.html#cfn-dms-endpoint-ibmdb2settings-secretsmanagersecretid
            '''
            result = self._values.get("secrets_manager_secret_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def set_data_capture_changes(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Enables ongoing replication (CDC) as a BOOLEAN value.

            The default is true.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-ibmdb2settings.html#cfn-dms-endpoint-ibmdb2settings-setdatacapturechanges
            '''
            result = self._values.get("set_data_capture_changes")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IbmDb2SettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dms.CfnEndpoint.KafkaSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "broker": "broker",
            "include_control_details": "includeControlDetails",
            "include_null_and_empty": "includeNullAndEmpty",
            "include_partition_value": "includePartitionValue",
            "include_table_alter_operations": "includeTableAlterOperations",
            "include_transaction_details": "includeTransactionDetails",
            "message_format": "messageFormat",
            "message_max_bytes": "messageMaxBytes",
            "no_hex_prefix": "noHexPrefix",
            "partition_include_schema_table": "partitionIncludeSchemaTable",
            "sasl_password": "saslPassword",
            "sasl_user_name": "saslUserName",
            "security_protocol": "securityProtocol",
            "ssl_ca_certificate_arn": "sslCaCertificateArn",
            "ssl_client_certificate_arn": "sslClientCertificateArn",
            "ssl_client_key_arn": "sslClientKeyArn",
            "ssl_client_key_password": "sslClientKeyPassword",
            "topic": "topic",
        },
    )
    class KafkaSettingsProperty:
        def __init__(
            self,
            *,
            broker: typing.Optional[builtins.str] = None,
            include_control_details: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            include_null_and_empty: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            include_partition_value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            include_table_alter_operations: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            include_transaction_details: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            message_format: typing.Optional[builtins.str] = None,
            message_max_bytes: typing.Optional[jsii.Number] = None,
            no_hex_prefix: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            partition_include_schema_table: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            sasl_password: typing.Optional[builtins.str] = None,
            sasl_user_name: typing.Optional[builtins.str] = None,
            security_protocol: typing.Optional[builtins.str] = None,
            ssl_ca_certificate_arn: typing.Optional[builtins.str] = None,
            ssl_client_certificate_arn: typing.Optional[builtins.str] = None,
            ssl_client_key_arn: typing.Optional[builtins.str] = None,
            ssl_client_key_password: typing.Optional[builtins.str] = None,
            topic: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides information that describes an Apache Kafka endpoint.

            This information includes the output format of records applied to the endpoint and details of transaction and control table data information. For more information about other available settings, see `Using object mapping to migrate data to a Kafka topic <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kafka.html#CHAP_Target.Kafka.ObjectMapping>`_ in the *AWS Database Migration Service User Guide* .

            :param broker: A comma-separated list of one or more broker locations in your Kafka cluster that host your Kafka instance. Specify each broker location in the form ``*broker-hostname-or-ip* : *port*`` . For example, ``"ec2-12-345-678-901.compute-1.amazonaws.com:2345"`` . For more information and examples of specifying a list of broker locations, see `Using Apache Kafka as a target for AWS Database Migration Service <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kafka.html>`_ in the *AWS Database Migration Service User Guide* .
            :param include_control_details: Shows detailed control information for table definition, column definition, and table and column changes in the Kafka message output. The default is ``false`` .
            :param include_null_and_empty: Include NULL and empty columns for records migrated to the endpoint. The default is ``false`` .
            :param include_partition_value: Shows the partition value within the Kafka message output unless the partition type is ``schema-table-type`` . The default is ``false`` .
            :param include_table_alter_operations: Includes any data definition language (DDL) operations that change the table in the control data, such as ``rename-table`` , ``drop-table`` , ``add-column`` , ``drop-column`` , and ``rename-column`` . The default is ``false`` .
            :param include_transaction_details: Provides detailed transaction information from the source database. This information includes a commit timestamp, a log position, and values for ``transaction_id`` , previous ``transaction_id`` , and ``transaction_record_id`` (the record offset within a transaction). The default is ``false`` .
            :param message_format: The output format for the records created on the endpoint. The message format is ``JSON`` (default) or ``JSON_UNFORMATTED`` (a single line with no tab).
            :param message_max_bytes: The maximum size in bytes for records created on the endpoint The default is 1,000,000.
            :param no_hex_prefix: Set this optional parameter to ``true`` to avoid adding a '0x' prefix to raw data in hexadecimal format. For example, by default, AWS DMS adds a '0x' prefix to the LOB column type in hexadecimal format moving from an Oracle source to a Kafka target. Use the ``NoHexPrefix`` endpoint setting to enable migration of RAW data type columns without adding the '0x' prefix.
            :param partition_include_schema_table: Prefixes schema and table names to partition values, when the partition type is ``primary-key-type`` . Doing this increases data distribution among Kafka partitions. For example, suppose that a SysBench schema has thousands of tables and each table has only limited range for a primary key. In this case, the same primary key is sent from thousands of tables to the same partition, which causes throttling. The default is ``false`` .
            :param sasl_password: The secure password that you created when you first set up your Amazon MSK cluster to validate a client identity and make an encrypted connection between server and client using SASL-SSL authentication.
            :param sasl_user_name: The secure user name you created when you first set up your Amazon MSK cluster to validate a client identity and make an encrypted connection between server and client using SASL-SSL authentication.
            :param security_protocol: Set secure connection to a Kafka target endpoint using Transport Layer Security (TLS). Options include ``ssl-encryption`` , ``ssl-authentication`` , and ``sasl-ssl`` . ``sasl-ssl`` requires ``SaslUsername`` and ``SaslPassword`` .
            :param ssl_ca_certificate_arn: The Amazon Resource Name (ARN) for the private certificate authority (CA) cert that AWS DMS uses to securely connect to your Kafka target endpoint.
            :param ssl_client_certificate_arn: The Amazon Resource Name (ARN) of the client certificate used to securely connect to a Kafka target endpoint.
            :param ssl_client_key_arn: The Amazon Resource Name (ARN) for the client private key used to securely connect to a Kafka target endpoint.
            :param ssl_client_key_password: The password for the client private key used to securely connect to a Kafka target endpoint.
            :param topic: The topic to which you migrate the data. If you don't specify a topic, AWS DMS specifies ``"kafka-default-topic"`` as the migration topic.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dms as dms
                
                kafka_settings_property = dms.CfnEndpoint.KafkaSettingsProperty(
                    broker="broker",
                    include_control_details=False,
                    include_null_and_empty=False,
                    include_partition_value=False,
                    include_table_alter_operations=False,
                    include_transaction_details=False,
                    message_format="messageFormat",
                    message_max_bytes=123,
                    no_hex_prefix=False,
                    partition_include_schema_table=False,
                    sasl_password="saslPassword",
                    sasl_user_name="saslUserName",
                    security_protocol="securityProtocol",
                    ssl_ca_certificate_arn="sslCaCertificateArn",
                    ssl_client_certificate_arn="sslClientCertificateArn",
                    ssl_client_key_arn="sslClientKeyArn",
                    ssl_client_key_password="sslClientKeyPassword",
                    topic="topic"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7b2bfaca6d665af7431f159590048ac8b759b878af0480fc254f2c8cf011d547)
                check_type(argname="argument broker", value=broker, expected_type=type_hints["broker"])
                check_type(argname="argument include_control_details", value=include_control_details, expected_type=type_hints["include_control_details"])
                check_type(argname="argument include_null_and_empty", value=include_null_and_empty, expected_type=type_hints["include_null_and_empty"])
                check_type(argname="argument include_partition_value", value=include_partition_value, expected_type=type_hints["include_partition_value"])
                check_type(argname="argument include_table_alter_operations", value=include_table_alter_operations, expected_type=type_hints["include_table_alter_operations"])
                check_type(argname="argument include_transaction_details", value=include_transaction_details, expected_type=type_hints["include_transaction_details"])
                check_type(argname="argument message_format", value=message_format, expected_type=type_hints["message_format"])
                check_type(argname="argument message_max_bytes", value=message_max_bytes, expected_type=type_hints["message_max_bytes"])
                check_type(argname="argument no_hex_prefix", value=no_hex_prefix, expected_type=type_hints["no_hex_prefix"])
                check_type(argname="argument partition_include_schema_table", value=partition_include_schema_table, expected_type=type_hints["partition_include_schema_table"])
                check_type(argname="argument sasl_password", value=sasl_password, expected_type=type_hints["sasl_password"])
                check_type(argname="argument sasl_user_name", value=sasl_user_name, expected_type=type_hints["sasl_user_name"])
                check_type(argname="argument security_protocol", value=security_protocol, expected_type=type_hints["security_protocol"])
                check_type(argname="argument ssl_ca_certificate_arn", value=ssl_ca_certificate_arn, expected_type=type_hints["ssl_ca_certificate_arn"])
                check_type(argname="argument ssl_client_certificate_arn", value=ssl_client_certificate_arn, expected_type=type_hints["ssl_client_certificate_arn"])
                check_type(argname="argument ssl_client_key_arn", value=ssl_client_key_arn, expected_type=type_hints["ssl_client_key_arn"])
                check_type(argname="argument ssl_client_key_password", value=ssl_client_key_password, expected_type=type_hints["ssl_client_key_password"])
                check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if broker is not None:
                self._values["broker"] = broker
            if include_control_details is not None:
                self._values["include_control_details"] = include_control_details
            if include_null_and_empty is not None:
                self._values["include_null_and_empty"] = include_null_and_empty
            if include_partition_value is not None:
                self._values["include_partition_value"] = include_partition_value
            if include_table_alter_operations is not None:
                self._values["include_table_alter_operations"] = include_table_alter_operations
            if include_transaction_details is not None:
                self._values["include_transaction_details"] = include_transaction_details
            if message_format is not None:
                self._values["message_format"] = message_format
            if message_max_bytes is not None:
                self._values["message_max_bytes"] = message_max_bytes
            if no_hex_prefix is not None:
                self._values["no_hex_prefix"] = no_hex_prefix
            if partition_include_schema_table is not None:
                self._values["partition_include_schema_table"] = partition_include_schema_table
            if sasl_password is not None:
                self._values["sasl_password"] = sasl_password
            if sasl_user_name is not None:
                self._values["sasl_user_name"] = sasl_user_name
            if security_protocol is not None:
                self._values["security_protocol"] = security_protocol
            if ssl_ca_certificate_arn is not None:
                self._values["ssl_ca_certificate_arn"] = ssl_ca_certificate_arn
            if ssl_client_certificate_arn is not None:
                self._values["ssl_client_certificate_arn"] = ssl_client_certificate_arn
            if ssl_client_key_arn is not None:
                self._values["ssl_client_key_arn"] = ssl_client_key_arn
            if ssl_client_key_password is not None:
                self._values["ssl_client_key_password"] = ssl_client_key_password
            if topic is not None:
                self._values["topic"] = topic

        @builtins.property
        def broker(self) -> typing.Optional[builtins.str]:
            '''A comma-separated list of one or more broker locations in your Kafka cluster that host your Kafka instance.

            Specify each broker location in the form ``*broker-hostname-or-ip* : *port*`` . For example, ``"ec2-12-345-678-901.compute-1.amazonaws.com:2345"`` . For more information and examples of specifying a list of broker locations, see `Using Apache Kafka as a target for AWS Database Migration Service <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kafka.html>`_ in the *AWS Database Migration Service User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-broker
            '''
            result = self._values.get("broker")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def include_control_details(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Shows detailed control information for table definition, column definition, and table and column changes in the Kafka message output.

            The default is ``false`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-includecontroldetails
            '''
            result = self._values.get("include_control_details")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def include_null_and_empty(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Include NULL and empty columns for records migrated to the endpoint.

            The default is ``false`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-includenullandempty
            '''
            result = self._values.get("include_null_and_empty")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def include_partition_value(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Shows the partition value within the Kafka message output unless the partition type is ``schema-table-type`` .

            The default is ``false`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-includepartitionvalue
            '''
            result = self._values.get("include_partition_value")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def include_table_alter_operations(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Includes any data definition language (DDL) operations that change the table in the control data, such as ``rename-table`` , ``drop-table`` , ``add-column`` , ``drop-column`` , and ``rename-column`` .

            The default is ``false`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-includetablealteroperations
            '''
            result = self._values.get("include_table_alter_operations")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def include_transaction_details(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Provides detailed transaction information from the source database.

            This information includes a commit timestamp, a log position, and values for ``transaction_id`` , previous ``transaction_id`` , and ``transaction_record_id`` (the record offset within a transaction). The default is ``false`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-includetransactiondetails
            '''
            result = self._values.get("include_transaction_details")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def message_format(self) -> typing.Optional[builtins.str]:
            '''The output format for the records created on the endpoint.

            The message format is ``JSON`` (default) or ``JSON_UNFORMATTED`` (a single line with no tab).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-messageformat
            '''
            result = self._values.get("message_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def message_max_bytes(self) -> typing.Optional[jsii.Number]:
            '''The maximum size in bytes for records created on the endpoint The default is 1,000,000.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-messagemaxbytes
            '''
            result = self._values.get("message_max_bytes")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def no_hex_prefix(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Set this optional parameter to ``true`` to avoid adding a '0x' prefix to raw data in hexadecimal format.

            For example, by default, AWS DMS adds a '0x' prefix to the LOB column type in hexadecimal format moving from an Oracle source to a Kafka target. Use the ``NoHexPrefix`` endpoint setting to enable migration of RAW data type columns without adding the '0x' prefix.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-nohexprefix
            '''
            result = self._values.get("no_hex_prefix")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def partition_include_schema_table(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Prefixes schema and table names to partition values, when the partition type is ``primary-key-type`` .

            Doing this increases data distribution among Kafka partitions. For example, suppose that a SysBench schema has thousands of tables and each table has only limited range for a primary key. In this case, the same primary key is sent from thousands of tables to the same partition, which causes throttling. The default is ``false`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-partitionincludeschematable
            '''
            result = self._values.get("partition_include_schema_table")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def sasl_password(self) -> typing.Optional[builtins.str]:
            '''The secure password that you created when you first set up your Amazon MSK cluster to validate a client identity and make an encrypted connection between server and client using SASL-SSL authentication.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-saslpassword
            '''
            result = self._values.get("sasl_password")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sasl_user_name(self) -> typing.Optional[builtins.str]:
            '''The secure user name you created when you first set up your Amazon MSK cluster to validate a client identity and make an encrypted connection between server and client using SASL-SSL authentication.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-saslusername
            '''
            result = self._values.get("sasl_user_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def security_protocol(self) -> typing.Optional[builtins.str]:
            '''Set secure connection to a Kafka target endpoint using Transport Layer Security (TLS).

            Options include ``ssl-encryption`` , ``ssl-authentication`` , and ``sasl-ssl`` . ``sasl-ssl`` requires ``SaslUsername`` and ``SaslPassword`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-securityprotocol
            '''
            result = self._values.get("security_protocol")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ssl_ca_certificate_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) for the private certificate authority (CA) cert that AWS DMS uses to securely connect to your Kafka target endpoint.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-sslcacertificatearn
            '''
            result = self._values.get("ssl_ca_certificate_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ssl_client_certificate_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the client certificate used to securely connect to a Kafka target endpoint.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-sslclientcertificatearn
            '''
            result = self._values.get("ssl_client_certificate_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ssl_client_key_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) for the client private key used to securely connect to a Kafka target endpoint.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-sslclientkeyarn
            '''
            result = self._values.get("ssl_client_key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ssl_client_key_password(self) -> typing.Optional[builtins.str]:
            '''The password for the client private key used to securely connect to a Kafka target endpoint.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-sslclientkeypassword
            '''
            result = self._values.get("ssl_client_key_password")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def topic(self) -> typing.Optional[builtins.str]:
            '''The topic to which you migrate the data.

            If you don't specify a topic, AWS DMS specifies ``"kafka-default-topic"`` as the migration topic.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-topic
            '''
            result = self._values.get("topic")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KafkaSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dms.CfnEndpoint.KinesisSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "include_control_details": "includeControlDetails",
            "include_null_and_empty": "includeNullAndEmpty",
            "include_partition_value": "includePartitionValue",
            "include_table_alter_operations": "includeTableAlterOperations",
            "include_transaction_details": "includeTransactionDetails",
            "message_format": "messageFormat",
            "no_hex_prefix": "noHexPrefix",
            "partition_include_schema_table": "partitionIncludeSchemaTable",
            "service_access_role_arn": "serviceAccessRoleArn",
            "stream_arn": "streamArn",
        },
    )
    class KinesisSettingsProperty:
        def __init__(
            self,
            *,
            include_control_details: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            include_null_and_empty: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            include_partition_value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            include_table_alter_operations: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            include_transaction_details: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            message_format: typing.Optional[builtins.str] = None,
            no_hex_prefix: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            partition_include_schema_table: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            service_access_role_arn: typing.Optional[builtins.str] = None,
            stream_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides information that describes an Amazon Kinesis Data Stream endpoint.

            This information includes the output format of records applied to the endpoint and details of transaction and control table data information. For more information about other available settings, see `Using object mapping to migrate data to a Kinesis data stream <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kinesis.html#CHAP_Target.Kinesis.ObjectMapping>`_ in the *AWS Database Migration Service User Guide* .

            :param include_control_details: Shows detailed control information for table definition, column definition, and table and column changes in the Kinesis message output. The default is ``false`` .
            :param include_null_and_empty: Include NULL and empty columns for records migrated to the endpoint. The default is ``false`` .
            :param include_partition_value: Shows the partition value within the Kinesis message output, unless the partition type is ``schema-table-type`` . The default is ``false`` .
            :param include_table_alter_operations: Includes any data definition language (DDL) operations that change the table in the control data, such as ``rename-table`` , ``drop-table`` , ``add-column`` , ``drop-column`` , and ``rename-column`` . The default is ``false`` .
            :param include_transaction_details: Provides detailed transaction information from the source database. This information includes a commit timestamp, a log position, and values for ``transaction_id`` , previous ``transaction_id`` , and ``transaction_record_id`` (the record offset within a transaction). The default is ``false`` .
            :param message_format: The output format for the records created on the endpoint. The message format is ``JSON`` (default) or ``JSON_UNFORMATTED`` (a single line with no tab).
            :param no_hex_prefix: Set this optional parameter to ``true`` to avoid adding a '0x' prefix to raw data in hexadecimal format. For example, by default, AWS DMS adds a '0x' prefix to the LOB column type in hexadecimal format moving from an Oracle source to an Amazon Kinesis target. Use the ``NoHexPrefix`` endpoint setting to enable migration of RAW data type columns without adding the '0x' prefix.
            :param partition_include_schema_table: Prefixes schema and table names to partition values, when the partition type is ``primary-key-type`` . Doing this increases data distribution among Kinesis shards. For example, suppose that a SysBench schema has thousands of tables and each table has only limited range for a primary key. In this case, the same primary key is sent from thousands of tables to the same shard, which causes throttling. The default is ``false`` .
            :param service_access_role_arn: The Amazon Resource Name (ARN) for the IAM role that AWS DMS uses to write to the Kinesis data stream. The role must allow the ``iam:PassRole`` action.
            :param stream_arn: The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kinesissettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dms as dms
                
                kinesis_settings_property = dms.CfnEndpoint.KinesisSettingsProperty(
                    include_control_details=False,
                    include_null_and_empty=False,
                    include_partition_value=False,
                    include_table_alter_operations=False,
                    include_transaction_details=False,
                    message_format="messageFormat",
                    no_hex_prefix=False,
                    partition_include_schema_table=False,
                    service_access_role_arn="serviceAccessRoleArn",
                    stream_arn="streamArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__50ae30a854acf9cf5d2be7057f5211ed1623f13610e13f1ee2066cbe68d2bf26)
                check_type(argname="argument include_control_details", value=include_control_details, expected_type=type_hints["include_control_details"])
                check_type(argname="argument include_null_and_empty", value=include_null_and_empty, expected_type=type_hints["include_null_and_empty"])
                check_type(argname="argument include_partition_value", value=include_partition_value, expected_type=type_hints["include_partition_value"])
                check_type(argname="argument include_table_alter_operations", value=include_table_alter_operations, expected_type=type_hints["include_table_alter_operations"])
                check_type(argname="argument include_transaction_details", value=include_transaction_details, expected_type=type_hints["include_transaction_details"])
                check_type(argname="argument message_format", value=message_format, expected_type=type_hints["message_format"])
                check_type(argname="argument no_hex_prefix", value=no_hex_prefix, expected_type=type_hints["no_hex_prefix"])
                check_type(argname="argument partition_include_schema_table", value=partition_include_schema_table, expected_type=type_hints["partition_include_schema_table"])
                check_type(argname="argument service_access_role_arn", value=service_access_role_arn, expected_type=type_hints["service_access_role_arn"])
                check_type(argname="argument stream_arn", value=stream_arn, expected_type=type_hints["stream_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if include_control_details is not None:
                self._values["include_control_details"] = include_control_details
            if include_null_and_empty is not None:
                self._values["include_null_and_empty"] = include_null_and_empty
            if include_partition_value is not None:
                self._values["include_partition_value"] = include_partition_value
            if include_table_alter_operations is not None:
                self._values["include_table_alter_operations"] = include_table_alter_operations
            if include_transaction_details is not None:
                self._values["include_transaction_details"] = include_transaction_details
            if message_format is not None:
                self._values["message_format"] = message_format
            if no_hex_prefix is not None:
                self._values["no_hex_prefix"] = no_hex_prefix
            if partition_include_schema_table is not None:
                self._values["partition_include_schema_table"] = partition_include_schema_table
            if service_access_role_arn is not None:
                self._values["service_access_role_arn"] = service_access_role_arn
            if stream_arn is not None:
                self._values["stream_arn"] = stream_arn

        @builtins.property
        def include_control_details(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Shows detailed control information for table definition, column definition, and table and column changes in the Kinesis message output.

            The default is ``false`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kinesissettings.html#cfn-dms-endpoint-kinesissettings-includecontroldetails
            '''
            result = self._values.get("include_control_details")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def include_null_and_empty(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Include NULL and empty columns for records migrated to the endpoint.

            The default is ``false`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kinesissettings.html#cfn-dms-endpoint-kinesissettings-includenullandempty
            '''
            result = self._values.get("include_null_and_empty")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def include_partition_value(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Shows the partition value within the Kinesis message output, unless the partition type is ``schema-table-type`` .

            The default is ``false`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kinesissettings.html#cfn-dms-endpoint-kinesissettings-includepartitionvalue
            '''
            result = self._values.get("include_partition_value")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def include_table_alter_operations(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Includes any data definition language (DDL) operations that change the table in the control data, such as ``rename-table`` , ``drop-table`` , ``add-column`` , ``drop-column`` , and ``rename-column`` .

            The default is ``false`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kinesissettings.html#cfn-dms-endpoint-kinesissettings-includetablealteroperations
            '''
            result = self._values.get("include_table_alter_operations")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def include_transaction_details(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Provides detailed transaction information from the source database.

            This information includes a commit timestamp, a log position, and values for ``transaction_id`` , previous ``transaction_id`` , and ``transaction_record_id`` (the record offset within a transaction). The default is ``false`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kinesissettings.html#cfn-dms-endpoint-kinesissettings-includetransactiondetails
            '''
            result = self._values.get("include_transaction_details")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def message_format(self) -> typing.Optional[builtins.str]:
            '''The output format for the records created on the endpoint.

            The message format is ``JSON`` (default) or ``JSON_UNFORMATTED`` (a single line with no tab).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kinesissettings.html#cfn-dms-endpoint-kinesissettings-messageformat
            '''
            result = self._values.get("message_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def no_hex_prefix(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Set this optional parameter to ``true`` to avoid adding a '0x' prefix to raw data in hexadecimal format.

            For example, by default, AWS DMS adds a '0x' prefix to the LOB column type in hexadecimal format moving from an Oracle source to an Amazon Kinesis target. Use the ``NoHexPrefix`` endpoint setting to enable migration of RAW data type columns without adding the '0x' prefix.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kinesissettings.html#cfn-dms-endpoint-kinesissettings-nohexprefix
            '''
            result = self._values.get("no_hex_prefix")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def partition_include_schema_table(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Prefixes schema and table names to partition values, when the partition type is ``primary-key-type`` .

            Doing this increases data distribution among Kinesis shards. For example, suppose that a SysBench schema has thousands of tables and each table has only limited range for a primary key. In this case, the same primary key is sent from thousands of tables to the same shard, which causes throttling. The default is ``false`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kinesissettings.html#cfn-dms-endpoint-kinesissettings-partitionincludeschematable
            '''
            result = self._values.get("partition_include_schema_table")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def service_access_role_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) for the IAM role that AWS DMS uses to write to the Kinesis data stream.

            The role must allow the ``iam:PassRole`` action.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kinesissettings.html#cfn-dms-endpoint-kinesissettings-serviceaccessrolearn
            '''
            result = self._values.get("service_access_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def stream_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kinesissettings.html#cfn-dms-endpoint-kinesissettings-streamarn
            '''
            result = self._values.get("stream_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dms.CfnEndpoint.MicrosoftSqlServerSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bcp_packet_size": "bcpPacketSize",
            "control_tables_file_group": "controlTablesFileGroup",
            "query_single_always_on_node": "querySingleAlwaysOnNode",
            "read_backup_only": "readBackupOnly",
            "safeguard_policy": "safeguardPolicy",
            "secrets_manager_access_role_arn": "secretsManagerAccessRoleArn",
            "secrets_manager_secret_id": "secretsManagerSecretId",
            "use_bcp_full_load": "useBcpFullLoad",
            "use_third_party_backup_device": "useThirdPartyBackupDevice",
        },
    )
    class MicrosoftSqlServerSettingsProperty:
        def __init__(
            self,
            *,
            bcp_packet_size: typing.Optional[jsii.Number] = None,
            control_tables_file_group: typing.Optional[builtins.str] = None,
            query_single_always_on_node: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            read_backup_only: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            safeguard_policy: typing.Optional[builtins.str] = None,
            secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
            secrets_manager_secret_id: typing.Optional[builtins.str] = None,
            use_bcp_full_load: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            use_third_party_backup_device: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''Provides information that defines a Microsoft SQL Server endpoint.

            This information includes the output format of records applied to the endpoint and details of transaction and control table data information. For information about other available settings, see `Extra connection attributes when using SQL Server as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SQLServer.html#CHAP_Source.SQLServer.ConnectionAttrib>`_ and `Extra connection attributes when using SQL Server as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.SQLServer.html#CHAP_Target.SQLServer.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

            :param bcp_packet_size: The maximum size of the packets (in bytes) used to transfer data using BCP.
            :param control_tables_file_group: Specifies a file group for the AWS DMS internal tables. When the replication task starts, all the internal AWS DMS control tables (awsdms_ apply_exception, awsdms_apply, awsdms_changes) are created for the specified file group.
            :param query_single_always_on_node: Cleans and recreates table metadata information on the replication instance when a mismatch occurs. An example is a situation where running an alter DDL statement on a table might result in different information about the table cached in the replication instance.
            :param read_backup_only: When this attribute is set to ``Y`` , AWS DMS only reads changes from transaction log backups and doesn't read from the active transaction log file during ongoing replication. Setting this parameter to ``Y`` enables you to control active transaction log file growth during full load and ongoing replication tasks. However, it can add some source latency to ongoing replication.
            :param safeguard_policy: Use this attribute to minimize the need to access the backup log and enable AWS DMS to prevent truncation using one of the following two methods. *Start transactions in the database:* This is the default method. When this method is used, AWS DMS prevents TLOG truncation by mimicking a transaction in the database. As long as such a transaction is open, changes that appear after the transaction started aren't truncated. If you need Microsoft Replication to be enabled in your database, then you must choose this method. *Exclusively use sp_repldone within a single task* : When this method is used, AWS DMS reads the changes and then uses sp_repldone to mark the TLOG transactions as ready for truncation. Although this method doesn't involve any transactional activities, it can only be used when Microsoft Replication isn't running. Also, when using this method, only one AWS DMS task can access the database at any given time. Therefore, if you need to run parallel AWS DMS tasks against the same database, use the default method.
            :param secrets_manager_access_role_arn: The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in ``SecretsManagerSecret`` . The role must allow the ``iam:PassRole`` action. ``SecretsManagerSecret`` has the value of the AWS Secrets Manager secret that allows access to the SQL Server endpoint. .. epigraph:: You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerSecretId`` . Or you can specify clear-text values for ``UserName`` , ``Password`` , ``ServerName`` , and ``Port`` . You can't specify both. For more information on creating this ``SecretsManagerSecret`` , the corresponding ``SecretsManagerAccessRoleArn`` , and the ``SecretsManagerSecretId`` that is required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .
            :param secrets_manager_secret_id: The full ARN, partial ARN, or display name of the ``SecretsManagerSecret`` that contains the MicrosoftSQLServer endpoint connection details.
            :param use_bcp_full_load: Use this to attribute to transfer data for full-load operations using BCP. When the target table contains an identity column that does not exist in the source table, you must disable the use BCP for loading table option.
            :param use_third_party_backup_device: When this attribute is set to ``Y`` , DMS processes third-party transaction log backups if they are created in native format.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dms as dms
                
                microsoft_sql_server_settings_property = dms.CfnEndpoint.MicrosoftSqlServerSettingsProperty(
                    bcp_packet_size=123,
                    control_tables_file_group="controlTablesFileGroup",
                    query_single_always_on_node=False,
                    read_backup_only=False,
                    safeguard_policy="safeguardPolicy",
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_secret_id="secretsManagerSecretId",
                    use_bcp_full_load=False,
                    use_third_party_backup_device=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4f7a6006215e1604c5eb4dbda619ce3e1479d08380de7614aded7df76594b7d8)
                check_type(argname="argument bcp_packet_size", value=bcp_packet_size, expected_type=type_hints["bcp_packet_size"])
                check_type(argname="argument control_tables_file_group", value=control_tables_file_group, expected_type=type_hints["control_tables_file_group"])
                check_type(argname="argument query_single_always_on_node", value=query_single_always_on_node, expected_type=type_hints["query_single_always_on_node"])
                check_type(argname="argument read_backup_only", value=read_backup_only, expected_type=type_hints["read_backup_only"])
                check_type(argname="argument safeguard_policy", value=safeguard_policy, expected_type=type_hints["safeguard_policy"])
                check_type(argname="argument secrets_manager_access_role_arn", value=secrets_manager_access_role_arn, expected_type=type_hints["secrets_manager_access_role_arn"])
                check_type(argname="argument secrets_manager_secret_id", value=secrets_manager_secret_id, expected_type=type_hints["secrets_manager_secret_id"])
                check_type(argname="argument use_bcp_full_load", value=use_bcp_full_load, expected_type=type_hints["use_bcp_full_load"])
                check_type(argname="argument use_third_party_backup_device", value=use_third_party_backup_device, expected_type=type_hints["use_third_party_backup_device"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if bcp_packet_size is not None:
                self._values["bcp_packet_size"] = bcp_packet_size
            if control_tables_file_group is not None:
                self._values["control_tables_file_group"] = control_tables_file_group
            if query_single_always_on_node is not None:
                self._values["query_single_always_on_node"] = query_single_always_on_node
            if read_backup_only is not None:
                self._values["read_backup_only"] = read_backup_only
            if safeguard_policy is not None:
                self._values["safeguard_policy"] = safeguard_policy
            if secrets_manager_access_role_arn is not None:
                self._values["secrets_manager_access_role_arn"] = secrets_manager_access_role_arn
            if secrets_manager_secret_id is not None:
                self._values["secrets_manager_secret_id"] = secrets_manager_secret_id
            if use_bcp_full_load is not None:
                self._values["use_bcp_full_load"] = use_bcp_full_load
            if use_third_party_backup_device is not None:
                self._values["use_third_party_backup_device"] = use_third_party_backup_device

        @builtins.property
        def bcp_packet_size(self) -> typing.Optional[jsii.Number]:
            '''The maximum size of the packets (in bytes) used to transfer data using BCP.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-bcppacketsize
            '''
            result = self._values.get("bcp_packet_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def control_tables_file_group(self) -> typing.Optional[builtins.str]:
            '''Specifies a file group for the AWS DMS internal tables.

            When the replication task starts, all the internal AWS DMS control tables (awsdms_ apply_exception, awsdms_apply, awsdms_changes) are created for the specified file group.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-controltablesfilegroup
            '''
            result = self._values.get("control_tables_file_group")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def query_single_always_on_node(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Cleans and recreates table metadata information on the replication instance when a mismatch occurs.

            An example is a situation where running an alter DDL statement on a table might result in different information about the table cached in the replication instance.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-querysinglealwaysonnode
            '''
            result = self._values.get("query_single_always_on_node")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def read_backup_only(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''When this attribute is set to ``Y`` , AWS DMS only reads changes from transaction log backups and doesn't read from the active transaction log file during ongoing replication.

            Setting this parameter to ``Y`` enables you to control active transaction log file growth during full load and ongoing replication tasks. However, it can add some source latency to ongoing replication.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-readbackuponly
            '''
            result = self._values.get("read_backup_only")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def safeguard_policy(self) -> typing.Optional[builtins.str]:
            '''Use this attribute to minimize the need to access the backup log and enable AWS DMS to prevent truncation using one of the following two methods.

            *Start transactions in the database:* This is the default method. When this method is used, AWS DMS prevents TLOG truncation by mimicking a transaction in the database. As long as such a transaction is open, changes that appear after the transaction started aren't truncated. If you need Microsoft Replication to be enabled in your database, then you must choose this method.

            *Exclusively use sp_repldone within a single task* : When this method is used, AWS DMS reads the changes and then uses sp_repldone to mark the TLOG transactions as ready for truncation. Although this method doesn't involve any transactional activities, it can only be used when Microsoft Replication isn't running. Also, when using this method, only one AWS DMS task can access the database at any given time. Therefore, if you need to run parallel AWS DMS tasks against the same database, use the default method.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-safeguardpolicy
            '''
            result = self._values.get("safeguard_policy")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secrets_manager_access_role_arn(self) -> typing.Optional[builtins.str]:
            '''The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in ``SecretsManagerSecret`` .

            The role must allow the ``iam:PassRole`` action. ``SecretsManagerSecret`` has the value of the AWS Secrets Manager secret that allows access to the SQL Server endpoint.
            .. epigraph::

               You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerSecretId`` . Or you can specify clear-text values for ``UserName`` , ``Password`` , ``ServerName`` , and ``Port`` . You can't specify both.

               For more information on creating this ``SecretsManagerSecret`` , the corresponding ``SecretsManagerAccessRoleArn`` , and the ``SecretsManagerSecretId`` that is required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-secretsmanageraccessrolearn
            '''
            result = self._values.get("secrets_manager_access_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secrets_manager_secret_id(self) -> typing.Optional[builtins.str]:
            '''The full ARN, partial ARN, or display name of the ``SecretsManagerSecret`` that contains the MicrosoftSQLServer endpoint connection details.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-secretsmanagersecretid
            '''
            result = self._values.get("secrets_manager_secret_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def use_bcp_full_load(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Use this to attribute to transfer data for full-load operations using BCP.

            When the target table contains an identity column that does not exist in the source table, you must disable the use BCP for loading table option.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-usebcpfullload
            '''
            result = self._values.get("use_bcp_full_load")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def use_third_party_backup_device(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''When this attribute is set to ``Y`` , DMS processes third-party transaction log backups if they are created in native format.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-usethirdpartybackupdevice
            '''
            result = self._values.get("use_third_party_backup_device")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MicrosoftSqlServerSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dms.CfnEndpoint.MongoDbSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "auth_mechanism": "authMechanism",
            "auth_source": "authSource",
            "auth_type": "authType",
            "database_name": "databaseName",
            "docs_to_investigate": "docsToInvestigate",
            "extract_doc_id": "extractDocId",
            "nesting_level": "nestingLevel",
            "password": "password",
            "port": "port",
            "secrets_manager_access_role_arn": "secretsManagerAccessRoleArn",
            "secrets_manager_secret_id": "secretsManagerSecretId",
            "server_name": "serverName",
            "username": "username",
        },
    )
    class MongoDbSettingsProperty:
        def __init__(
            self,
            *,
            auth_mechanism: typing.Optional[builtins.str] = None,
            auth_source: typing.Optional[builtins.str] = None,
            auth_type: typing.Optional[builtins.str] = None,
            database_name: typing.Optional[builtins.str] = None,
            docs_to_investigate: typing.Optional[builtins.str] = None,
            extract_doc_id: typing.Optional[builtins.str] = None,
            nesting_level: typing.Optional[builtins.str] = None,
            password: typing.Optional[builtins.str] = None,
            port: typing.Optional[jsii.Number] = None,
            secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
            secrets_manager_secret_id: typing.Optional[builtins.str] = None,
            server_name: typing.Optional[builtins.str] = None,
            username: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides information that defines a MongoDB endpoint.

            This information includes the output format of records applied to the endpoint and details of transaction and control table data information. For more information about other available settings, see `Endpoint configuration settings when using MongoDB as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MongoDB.html#CHAP_Source.MongoDB.Configuration>`_ in the *AWS Database Migration Service User Guide* .

            :param auth_mechanism: The authentication mechanism you use to access the MongoDB source endpoint. For the default value, in MongoDB version 2.x, ``"default"`` is ``"mongodb_cr"`` . For MongoDB version 3.x or later, ``"default"`` is ``"scram_sha_1"`` . This setting isn't used when ``AuthType`` is set to ``"no"`` .
            :param auth_source: The MongoDB database name. This setting isn't used when ``AuthType`` is set to ``"no"`` . The default is ``"admin"`` .
            :param auth_type: The authentication type you use to access the MongoDB source endpoint. When set to ``"no"`` , user name and password parameters are not used and can be empty.
            :param database_name: The database name on the MongoDB source endpoint.
            :param docs_to_investigate: Indicates the number of documents to preview to determine the document organization. Use this setting when ``NestingLevel`` is set to ``"one"`` . Must be a positive value greater than ``0`` . Default value is ``1000`` .
            :param extract_doc_id: Specifies the document ID. Use this setting when ``NestingLevel`` is set to ``"none"`` . Default value is ``"false"`` .
            :param nesting_level: Specifies either document or table mode. Default value is ``"none"`` . Specify ``"none"`` to use document mode. Specify ``"one"`` to use table mode.
            :param password: The password for the user account you use to access the MongoDB source endpoint.
            :param port: The port value for the MongoDB source endpoint.
            :param secrets_manager_access_role_arn: The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in ``SecretsManagerSecret`` . The role must allow the ``iam:PassRole`` action. ``SecretsManagerSecret`` has the value of the AWS Secrets Manager secret that allows access to the MongoDB endpoint. .. epigraph:: You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerSecretId`` . Or you can specify clear-text values for ``UserName`` , ``Password`` , ``ServerName`` , and ``Port`` . You can't specify both. For more information on creating this ``SecretsManagerSecret`` , the corresponding ``SecretsManagerAccessRoleArn`` , and the ``SecretsManagerSecretId`` that is required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .
            :param secrets_manager_secret_id: The full ARN, partial ARN, or display name of the ``SecretsManagerSecret`` that contains the MongoDB endpoint connection details.
            :param server_name: The name of the server on the MongoDB source endpoint.
            :param username: The user name you use to access the MongoDB source endpoint.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dms as dms
                
                mongo_db_settings_property = dms.CfnEndpoint.MongoDbSettingsProperty(
                    auth_mechanism="authMechanism",
                    auth_source="authSource",
                    auth_type="authType",
                    database_name="databaseName",
                    docs_to_investigate="docsToInvestigate",
                    extract_doc_id="extractDocId",
                    nesting_level="nestingLevel",
                    password="password",
                    port=123,
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_secret_id="secretsManagerSecretId",
                    server_name="serverName",
                    username="username"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9a1be5105bbfbd03cd358a6d7a5d96718fb6e587c51f31f62e2103b312b45641)
                check_type(argname="argument auth_mechanism", value=auth_mechanism, expected_type=type_hints["auth_mechanism"])
                check_type(argname="argument auth_source", value=auth_source, expected_type=type_hints["auth_source"])
                check_type(argname="argument auth_type", value=auth_type, expected_type=type_hints["auth_type"])
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument docs_to_investigate", value=docs_to_investigate, expected_type=type_hints["docs_to_investigate"])
                check_type(argname="argument extract_doc_id", value=extract_doc_id, expected_type=type_hints["extract_doc_id"])
                check_type(argname="argument nesting_level", value=nesting_level, expected_type=type_hints["nesting_level"])
                check_type(argname="argument password", value=password, expected_type=type_hints["password"])
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
                check_type(argname="argument secrets_manager_access_role_arn", value=secrets_manager_access_role_arn, expected_type=type_hints["secrets_manager_access_role_arn"])
                check_type(argname="argument secrets_manager_secret_id", value=secrets_manager_secret_id, expected_type=type_hints["secrets_manager_secret_id"])
                check_type(argname="argument server_name", value=server_name, expected_type=type_hints["server_name"])
                check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if auth_mechanism is not None:
                self._values["auth_mechanism"] = auth_mechanism
            if auth_source is not None:
                self._values["auth_source"] = auth_source
            if auth_type is not None:
                self._values["auth_type"] = auth_type
            if database_name is not None:
                self._values["database_name"] = database_name
            if docs_to_investigate is not None:
                self._values["docs_to_investigate"] = docs_to_investigate
            if extract_doc_id is not None:
                self._values["extract_doc_id"] = extract_doc_id
            if nesting_level is not None:
                self._values["nesting_level"] = nesting_level
            if password is not None:
                self._values["password"] = password
            if port is not None:
                self._values["port"] = port
            if secrets_manager_access_role_arn is not None:
                self._values["secrets_manager_access_role_arn"] = secrets_manager_access_role_arn
            if secrets_manager_secret_id is not None:
                self._values["secrets_manager_secret_id"] = secrets_manager_secret_id
            if server_name is not None:
                self._values["server_name"] = server_name
            if username is not None:
                self._values["username"] = username

        @builtins.property
        def auth_mechanism(self) -> typing.Optional[builtins.str]:
            '''The authentication mechanism you use to access the MongoDB source endpoint.

            For the default value, in MongoDB version 2.x, ``"default"`` is ``"mongodb_cr"`` . For MongoDB version 3.x or later, ``"default"`` is ``"scram_sha_1"`` . This setting isn't used when ``AuthType`` is set to ``"no"`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html#cfn-dms-endpoint-mongodbsettings-authmechanism
            '''
            result = self._values.get("auth_mechanism")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def auth_source(self) -> typing.Optional[builtins.str]:
            '''The MongoDB database name. This setting isn't used when ``AuthType`` is set to ``"no"`` .

            The default is ``"admin"`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html#cfn-dms-endpoint-mongodbsettings-authsource
            '''
            result = self._values.get("auth_source")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def auth_type(self) -> typing.Optional[builtins.str]:
            '''The authentication type you use to access the MongoDB source endpoint.

            When set to ``"no"`` , user name and password parameters are not used and can be empty.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html#cfn-dms-endpoint-mongodbsettings-authtype
            '''
            result = self._values.get("auth_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def database_name(self) -> typing.Optional[builtins.str]:
            '''The database name on the MongoDB source endpoint.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html#cfn-dms-endpoint-mongodbsettings-databasename
            '''
            result = self._values.get("database_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def docs_to_investigate(self) -> typing.Optional[builtins.str]:
            '''Indicates the number of documents to preview to determine the document organization.

            Use this setting when ``NestingLevel`` is set to ``"one"`` .

            Must be a positive value greater than ``0`` . Default value is ``1000`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html#cfn-dms-endpoint-mongodbsettings-docstoinvestigate
            '''
            result = self._values.get("docs_to_investigate")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def extract_doc_id(self) -> typing.Optional[builtins.str]:
            '''Specifies the document ID. Use this setting when ``NestingLevel`` is set to ``"none"`` .

            Default value is ``"false"`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html#cfn-dms-endpoint-mongodbsettings-extractdocid
            '''
            result = self._values.get("extract_doc_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def nesting_level(self) -> typing.Optional[builtins.str]:
            '''Specifies either document or table mode.

            Default value is ``"none"`` . Specify ``"none"`` to use document mode. Specify ``"one"`` to use table mode.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html#cfn-dms-endpoint-mongodbsettings-nestinglevel
            '''
            result = self._values.get("nesting_level")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def password(self) -> typing.Optional[builtins.str]:
            '''The password for the user account you use to access the MongoDB source endpoint.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html#cfn-dms-endpoint-mongodbsettings-password
            '''
            result = self._values.get("password")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def port(self) -> typing.Optional[jsii.Number]:
            '''The port value for the MongoDB source endpoint.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html#cfn-dms-endpoint-mongodbsettings-port
            '''
            result = self._values.get("port")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def secrets_manager_access_role_arn(self) -> typing.Optional[builtins.str]:
            '''The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in ``SecretsManagerSecret`` .

            The role must allow the ``iam:PassRole`` action. ``SecretsManagerSecret`` has the value of the AWS Secrets Manager secret that allows access to the MongoDB endpoint.
            .. epigraph::

               You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerSecretId`` . Or you can specify clear-text values for ``UserName`` , ``Password`` , ``ServerName`` , and ``Port`` . You can't specify both.

               For more information on creating this ``SecretsManagerSecret`` , the corresponding ``SecretsManagerAccessRoleArn`` , and the ``SecretsManagerSecretId`` that is required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html#cfn-dms-endpoint-mongodbsettings-secretsmanageraccessrolearn
            '''
            result = self._values.get("secrets_manager_access_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secrets_manager_secret_id(self) -> typing.Optional[builtins.str]:
            '''The full ARN, partial ARN, or display name of the ``SecretsManagerSecret`` that contains the MongoDB endpoint connection details.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html#cfn-dms-endpoint-mongodbsettings-secretsmanagersecretid
            '''
            result = self._values.get("secrets_manager_secret_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def server_name(self) -> typing.Optional[builtins.str]:
            '''The name of the server on the MongoDB source endpoint.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html#cfn-dms-endpoint-mongodbsettings-servername
            '''
            result = self._values.get("server_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def username(self) -> typing.Optional[builtins.str]:
            '''The user name you use to access the MongoDB source endpoint.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html#cfn-dms-endpoint-mongodbsettings-username
            '''
            result = self._values.get("username")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MongoDbSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dms.CfnEndpoint.MySqlSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "after_connect_script": "afterConnectScript",
            "clean_source_metadata_on_mismatch": "cleanSourceMetadataOnMismatch",
            "events_poll_interval": "eventsPollInterval",
            "max_file_size": "maxFileSize",
            "parallel_load_threads": "parallelLoadThreads",
            "secrets_manager_access_role_arn": "secretsManagerAccessRoleArn",
            "secrets_manager_secret_id": "secretsManagerSecretId",
            "server_timezone": "serverTimezone",
            "target_db_type": "targetDbType",
        },
    )
    class MySqlSettingsProperty:
        def __init__(
            self,
            *,
            after_connect_script: typing.Optional[builtins.str] = None,
            clean_source_metadata_on_mismatch: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            events_poll_interval: typing.Optional[jsii.Number] = None,
            max_file_size: typing.Optional[jsii.Number] = None,
            parallel_load_threads: typing.Optional[jsii.Number] = None,
            secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
            secrets_manager_secret_id: typing.Optional[builtins.str] = None,
            server_timezone: typing.Optional[builtins.str] = None,
            target_db_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides information that defines a MySQL endpoint.

            This information includes the output format of records applied to the endpoint and details of transaction and control table data information. For information about other available settings, see `Extra connection attributes when using MySQL as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html#CHAP_Source.MySQL.ConnectionAttrib>`_ and `Extra connection attributes when using a MySQL-compatible database as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.MySQL.html#CHAP_Target.MySQL.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

            :param after_connect_script: Specifies a script to run immediately after AWS DMS connects to the endpoint. The migration task continues running regardless if the SQL statement succeeds or fails. For this parameter, provide the code of the script itself, not the name of a file containing the script.
            :param clean_source_metadata_on_mismatch: Cleans and recreates table metadata information on the replication instance when a mismatch occurs. For example, in a situation where running an alter DDL on the table could result in different information about the table cached in the replication instance.
            :param events_poll_interval: Specifies how often to check the binary log for new changes/events when the database is idle. The default is five seconds. Example: ``eventsPollInterval=5;`` In the example, AWS DMS checks for changes in the binary logs every five seconds.
            :param max_file_size: Specifies the maximum size (in KB) of any .csv file used to transfer data to a MySQL-compatible database. Example: ``maxFileSize=512``
            :param parallel_load_threads: Improves performance when loading data into the MySQL-compatible target database. Specifies how many threads to use to load the data into the MySQL-compatible target database. Setting a large number of threads can have an adverse effect on database performance, because a separate connection is required for each thread. The default is one. Example: ``parallelLoadThreads=1``
            :param secrets_manager_access_role_arn: The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in ``SecretsManagerSecret`` . The role must allow the ``iam:PassRole`` action. ``SecretsManagerSecret`` has the value of the AWS Secrets Manager secret that allows access to the MySQL endpoint. .. epigraph:: You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerSecretId`` . Or you can specify clear-text values for ``UserName`` , ``Password`` , ``ServerName`` , and ``Port`` . You can't specify both. For more information on creating this ``SecretsManagerSecret`` , the corresponding ``SecretsManagerAccessRoleArn`` , and the ``SecretsManagerSecretId`` that is required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .
            :param secrets_manager_secret_id: The full ARN, partial ARN, or display name of the ``SecretsManagerSecret`` that contains the MySQL endpoint connection details.
            :param server_timezone: Specifies the time zone for the source MySQL database. Example: ``serverTimezone=US/Pacific;`` Note: Do not enclose time zones in single quotes.
            :param target_db_type: Specifies where to migrate source tables on the target, either to a single database or multiple databases. If you specify ``SPECIFIC_DATABASE`` , specify the database name using the ``DatabaseName`` parameter of the ``Endpoint`` object. Example: ``targetDbType=MULTIPLE_DATABASES``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mysqlsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dms as dms
                
                my_sql_settings_property = dms.CfnEndpoint.MySqlSettingsProperty(
                    after_connect_script="afterConnectScript",
                    clean_source_metadata_on_mismatch=False,
                    events_poll_interval=123,
                    max_file_size=123,
                    parallel_load_threads=123,
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_secret_id="secretsManagerSecretId",
                    server_timezone="serverTimezone",
                    target_db_type="targetDbType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__be0b06e0664968b276ec30fd4245521fd3675357dfe12029f709bac30b468529)
                check_type(argname="argument after_connect_script", value=after_connect_script, expected_type=type_hints["after_connect_script"])
                check_type(argname="argument clean_source_metadata_on_mismatch", value=clean_source_metadata_on_mismatch, expected_type=type_hints["clean_source_metadata_on_mismatch"])
                check_type(argname="argument events_poll_interval", value=events_poll_interval, expected_type=type_hints["events_poll_interval"])
                check_type(argname="argument max_file_size", value=max_file_size, expected_type=type_hints["max_file_size"])
                check_type(argname="argument parallel_load_threads", value=parallel_load_threads, expected_type=type_hints["parallel_load_threads"])
                check_type(argname="argument secrets_manager_access_role_arn", value=secrets_manager_access_role_arn, expected_type=type_hints["secrets_manager_access_role_arn"])
                check_type(argname="argument secrets_manager_secret_id", value=secrets_manager_secret_id, expected_type=type_hints["secrets_manager_secret_id"])
                check_type(argname="argument server_timezone", value=server_timezone, expected_type=type_hints["server_timezone"])
                check_type(argname="argument target_db_type", value=target_db_type, expected_type=type_hints["target_db_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if after_connect_script is not None:
                self._values["after_connect_script"] = after_connect_script
            if clean_source_metadata_on_mismatch is not None:
                self._values["clean_source_metadata_on_mismatch"] = clean_source_metadata_on_mismatch
            if events_poll_interval is not None:
                self._values["events_poll_interval"] = events_poll_interval
            if max_file_size is not None:
                self._values["max_file_size"] = max_file_size
            if parallel_load_threads is not None:
                self._values["parallel_load_threads"] = parallel_load_threads
            if secrets_manager_access_role_arn is not None:
                self._values["secrets_manager_access_role_arn"] = secrets_manager_access_role_arn
            if secrets_manager_secret_id is not None:
                self._values["secrets_manager_secret_id"] = secrets_manager_secret_id
            if server_timezone is not None:
                self._values["server_timezone"] = server_timezone
            if target_db_type is not None:
                self._values["target_db_type"] = target_db_type

        @builtins.property
        def after_connect_script(self) -> typing.Optional[builtins.str]:
            '''Specifies a script to run immediately after AWS DMS connects to the endpoint.

            The migration task continues running regardless if the SQL statement succeeds or fails.

            For this parameter, provide the code of the script itself, not the name of a file containing the script.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mysqlsettings.html#cfn-dms-endpoint-mysqlsettings-afterconnectscript
            '''
            result = self._values.get("after_connect_script")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def clean_source_metadata_on_mismatch(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Cleans and recreates table metadata information on the replication instance when a mismatch occurs.

            For example, in a situation where running an alter DDL on the table could result in different information about the table cached in the replication instance.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mysqlsettings.html#cfn-dms-endpoint-mysqlsettings-cleansourcemetadataonmismatch
            '''
            result = self._values.get("clean_source_metadata_on_mismatch")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def events_poll_interval(self) -> typing.Optional[jsii.Number]:
            '''Specifies how often to check the binary log for new changes/events when the database is idle.

            The default is five seconds.

            Example: ``eventsPollInterval=5;``

            In the example, AWS DMS checks for changes in the binary logs every five seconds.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mysqlsettings.html#cfn-dms-endpoint-mysqlsettings-eventspollinterval
            '''
            result = self._values.get("events_poll_interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_file_size(self) -> typing.Optional[jsii.Number]:
            '''Specifies the maximum size (in KB) of any .csv file used to transfer data to a MySQL-compatible database.

            Example: ``maxFileSize=512``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mysqlsettings.html#cfn-dms-endpoint-mysqlsettings-maxfilesize
            '''
            result = self._values.get("max_file_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def parallel_load_threads(self) -> typing.Optional[jsii.Number]:
            '''Improves performance when loading data into the MySQL-compatible target database.

            Specifies how many threads to use to load the data into the MySQL-compatible target database. Setting a large number of threads can have an adverse effect on database performance, because a separate connection is required for each thread. The default is one.

            Example: ``parallelLoadThreads=1``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mysqlsettings.html#cfn-dms-endpoint-mysqlsettings-parallelloadthreads
            '''
            result = self._values.get("parallel_load_threads")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def secrets_manager_access_role_arn(self) -> typing.Optional[builtins.str]:
            '''The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in ``SecretsManagerSecret`` .

            The role must allow the ``iam:PassRole`` action. ``SecretsManagerSecret`` has the value of the AWS Secrets Manager secret that allows access to the MySQL endpoint.
            .. epigraph::

               You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerSecretId`` . Or you can specify clear-text values for ``UserName`` , ``Password`` , ``ServerName`` , and ``Port`` . You can't specify both.

               For more information on creating this ``SecretsManagerSecret`` , the corresponding ``SecretsManagerAccessRoleArn`` , and the ``SecretsManagerSecretId`` that is required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mysqlsettings.html#cfn-dms-endpoint-mysqlsettings-secretsmanageraccessrolearn
            '''
            result = self._values.get("secrets_manager_access_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secrets_manager_secret_id(self) -> typing.Optional[builtins.str]:
            '''The full ARN, partial ARN, or display name of the ``SecretsManagerSecret`` that contains the MySQL endpoint connection details.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mysqlsettings.html#cfn-dms-endpoint-mysqlsettings-secretsmanagersecretid
            '''
            result = self._values.get("secrets_manager_secret_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def server_timezone(self) -> typing.Optional[builtins.str]:
            '''Specifies the time zone for the source MySQL database.

            Example: ``serverTimezone=US/Pacific;``

            Note: Do not enclose time zones in single quotes.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mysqlsettings.html#cfn-dms-endpoint-mysqlsettings-servertimezone
            '''
            result = self._values.get("server_timezone")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target_db_type(self) -> typing.Optional[builtins.str]:
            '''Specifies where to migrate source tables on the target, either to a single database or multiple databases.

            If you specify ``SPECIFIC_DATABASE`` , specify the database name using the ``DatabaseName`` parameter of the ``Endpoint`` object.

            Example: ``targetDbType=MULTIPLE_DATABASES``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mysqlsettings.html#cfn-dms-endpoint-mysqlsettings-targetdbtype
            '''
            result = self._values.get("target_db_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MySqlSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dms.CfnEndpoint.NeptuneSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "error_retry_duration": "errorRetryDuration",
            "iam_auth_enabled": "iamAuthEnabled",
            "max_file_size": "maxFileSize",
            "max_retry_count": "maxRetryCount",
            "s3_bucket_folder": "s3BucketFolder",
            "s3_bucket_name": "s3BucketName",
            "service_access_role_arn": "serviceAccessRoleArn",
        },
    )
    class NeptuneSettingsProperty:
        def __init__(
            self,
            *,
            error_retry_duration: typing.Optional[jsii.Number] = None,
            iam_auth_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            max_file_size: typing.Optional[jsii.Number] = None,
            max_retry_count: typing.Optional[jsii.Number] = None,
            s3_bucket_folder: typing.Optional[builtins.str] = None,
            s3_bucket_name: typing.Optional[builtins.str] = None,
            service_access_role_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides information that defines an Amazon Neptune endpoint.

            This information includes the output format of records applied to the endpoint and details of transaction and control table data information. For more information about the available settings, see `Specifying endpoint settings for Amazon Neptune as a target <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Neptune.html#CHAP_Target.Neptune.EndpointSettings>`_ in the *AWS Database Migration Service User Guide* .

            :param error_retry_duration: The number of milliseconds for AWS DMS to wait to retry a bulk-load of migrated graph data to the Neptune target database before raising an error. The default is 250.
            :param iam_auth_enabled: If you want IAM authorization enabled for this endpoint, set this parameter to ``true`` . Then attach the appropriate IAM policy document to your service role specified by ``ServiceAccessRoleArn`` . The default is ``false`` .
            :param max_file_size: The maximum size in kilobytes of migrated graph data stored in a .csv file before AWS DMS bulk-loads the data to the Neptune target database. The default is 1,048,576 KB. If the bulk load is successful, AWS DMS clears the bucket, ready to store the next batch of migrated graph data.
            :param max_retry_count: The number of times for AWS DMS to retry a bulk load of migrated graph data to the Neptune target database before raising an error. The default is 5.
            :param s3_bucket_folder: A folder path where you want AWS DMS to store migrated graph data in the S3 bucket specified by ``S3BucketName``.
            :param s3_bucket_name: The name of the Amazon S3 bucket where AWS DMS can temporarily store migrated graph data in .csv files before bulk-loading it to the Neptune target database. AWS DMS maps the SQL source data to graph data before storing it in these .csv files.
            :param service_access_role_arn: The Amazon Resource Name (ARN) of the service role that you created for the Neptune target endpoint. The role must allow the ``iam:PassRole`` action. For more information, see `Creating an IAM Service Role for Accessing Amazon Neptune as a Target <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Neptune.html#CHAP_Target.Neptune.ServiceRole>`_ in the *AWS Database Migration Service User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-neptunesettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dms as dms
                
                neptune_settings_property = dms.CfnEndpoint.NeptuneSettingsProperty(
                    error_retry_duration=123,
                    iam_auth_enabled=False,
                    max_file_size=123,
                    max_retry_count=123,
                    s3_bucket_folder="s3BucketFolder",
                    s3_bucket_name="s3BucketName",
                    service_access_role_arn="serviceAccessRoleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__434a69112509f8f99ce9dbb760f746ede02a0d869f4afa6869e7606ba3ce2409)
                check_type(argname="argument error_retry_duration", value=error_retry_duration, expected_type=type_hints["error_retry_duration"])
                check_type(argname="argument iam_auth_enabled", value=iam_auth_enabled, expected_type=type_hints["iam_auth_enabled"])
                check_type(argname="argument max_file_size", value=max_file_size, expected_type=type_hints["max_file_size"])
                check_type(argname="argument max_retry_count", value=max_retry_count, expected_type=type_hints["max_retry_count"])
                check_type(argname="argument s3_bucket_folder", value=s3_bucket_folder, expected_type=type_hints["s3_bucket_folder"])
                check_type(argname="argument s3_bucket_name", value=s3_bucket_name, expected_type=type_hints["s3_bucket_name"])
                check_type(argname="argument service_access_role_arn", value=service_access_role_arn, expected_type=type_hints["service_access_role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if error_retry_duration is not None:
                self._values["error_retry_duration"] = error_retry_duration
            if iam_auth_enabled is not None:
                self._values["iam_auth_enabled"] = iam_auth_enabled
            if max_file_size is not None:
                self._values["max_file_size"] = max_file_size
            if max_retry_count is not None:
                self._values["max_retry_count"] = max_retry_count
            if s3_bucket_folder is not None:
                self._values["s3_bucket_folder"] = s3_bucket_folder
            if s3_bucket_name is not None:
                self._values["s3_bucket_name"] = s3_bucket_name
            if service_access_role_arn is not None:
                self._values["service_access_role_arn"] = service_access_role_arn

        @builtins.property
        def error_retry_duration(self) -> typing.Optional[jsii.Number]:
            '''The number of milliseconds for AWS DMS to wait to retry a bulk-load of migrated graph data to the Neptune target database before raising an error.

            The default is 250.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-neptunesettings.html#cfn-dms-endpoint-neptunesettings-errorretryduration
            '''
            result = self._values.get("error_retry_duration")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def iam_auth_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''If you want IAM authorization enabled for this endpoint, set this parameter to ``true`` .

            Then attach the appropriate IAM policy document to your service role specified by ``ServiceAccessRoleArn`` . The default is ``false`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-neptunesettings.html#cfn-dms-endpoint-neptunesettings-iamauthenabled
            '''
            result = self._values.get("iam_auth_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def max_file_size(self) -> typing.Optional[jsii.Number]:
            '''The maximum size in kilobytes of migrated graph data stored in a .csv file before AWS DMS bulk-loads the data to the Neptune target database. The default is 1,048,576 KB. If the bulk load is successful, AWS DMS clears the bucket, ready to store the next batch of migrated graph data.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-neptunesettings.html#cfn-dms-endpoint-neptunesettings-maxfilesize
            '''
            result = self._values.get("max_file_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_retry_count(self) -> typing.Optional[jsii.Number]:
            '''The number of times for AWS DMS to retry a bulk load of migrated graph data to the Neptune target database before raising an error.

            The default is 5.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-neptunesettings.html#cfn-dms-endpoint-neptunesettings-maxretrycount
            '''
            result = self._values.get("max_retry_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def s3_bucket_folder(self) -> typing.Optional[builtins.str]:
            '''A folder path where you want AWS DMS to store migrated graph data in the S3 bucket specified by ``S3BucketName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-neptunesettings.html#cfn-dms-endpoint-neptunesettings-s3bucketfolder
            '''
            result = self._values.get("s3_bucket_folder")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_bucket_name(self) -> typing.Optional[builtins.str]:
            '''The name of the Amazon S3 bucket where AWS DMS can temporarily store migrated graph data in .csv files before bulk-loading it to the Neptune target database. AWS DMS maps the SQL source data to graph data before storing it in these .csv files.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-neptunesettings.html#cfn-dms-endpoint-neptunesettings-s3bucketname
            '''
            result = self._values.get("s3_bucket_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def service_access_role_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the service role that you created for the Neptune target endpoint.

            The role must allow the ``iam:PassRole`` action.

            For more information, see `Creating an IAM Service Role for Accessing Amazon Neptune as a Target <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Neptune.html#CHAP_Target.Neptune.ServiceRole>`_ in the *AWS Database Migration Service User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-neptunesettings.html#cfn-dms-endpoint-neptunesettings-serviceaccessrolearn
            '''
            result = self._values.get("service_access_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NeptuneSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dms.CfnEndpoint.OracleSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "access_alternate_directly": "accessAlternateDirectly",
            "additional_archived_log_dest_id": "additionalArchivedLogDestId",
            "add_supplemental_logging": "addSupplementalLogging",
            "allow_select_nested_tables": "allowSelectNestedTables",
            "archived_log_dest_id": "archivedLogDestId",
            "archived_logs_only": "archivedLogsOnly",
            "asm_password": "asmPassword",
            "asm_server": "asmServer",
            "asm_user": "asmUser",
            "char_length_semantics": "charLengthSemantics",
            "direct_path_no_log": "directPathNoLog",
            "direct_path_parallel_load": "directPathParallelLoad",
            "enable_homogenous_tablespace": "enableHomogenousTablespace",
            "extra_archived_log_dest_ids": "extraArchivedLogDestIds",
            "fail_tasks_on_lob_truncation": "failTasksOnLobTruncation",
            "number_datatype_scale": "numberDatatypeScale",
            "oracle_path_prefix": "oraclePathPrefix",
            "parallel_asm_read_threads": "parallelAsmReadThreads",
            "read_ahead_blocks": "readAheadBlocks",
            "read_table_space_name": "readTableSpaceName",
            "replace_path_prefix": "replacePathPrefix",
            "retry_interval": "retryInterval",
            "secrets_manager_access_role_arn": "secretsManagerAccessRoleArn",
            "secrets_manager_oracle_asm_access_role_arn": "secretsManagerOracleAsmAccessRoleArn",
            "secrets_manager_oracle_asm_secret_id": "secretsManagerOracleAsmSecretId",
            "secrets_manager_secret_id": "secretsManagerSecretId",
            "security_db_encryption": "securityDbEncryption",
            "security_db_encryption_name": "securityDbEncryptionName",
            "spatial_data_option_to_geo_json_function_name": "spatialDataOptionToGeoJsonFunctionName",
            "standby_delay_time": "standbyDelayTime",
            "use_alternate_folder_for_online": "useAlternateFolderForOnline",
            "use_b_file": "useBFile",
            "use_direct_path_full_load": "useDirectPathFullLoad",
            "use_logminer_reader": "useLogminerReader",
            "use_path_prefix": "usePathPrefix",
        },
    )
    class OracleSettingsProperty:
        def __init__(
            self,
            *,
            access_alternate_directly: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            additional_archived_log_dest_id: typing.Optional[jsii.Number] = None,
            add_supplemental_logging: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            allow_select_nested_tables: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            archived_log_dest_id: typing.Optional[jsii.Number] = None,
            archived_logs_only: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            asm_password: typing.Optional[builtins.str] = None,
            asm_server: typing.Optional[builtins.str] = None,
            asm_user: typing.Optional[builtins.str] = None,
            char_length_semantics: typing.Optional[builtins.str] = None,
            direct_path_no_log: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            direct_path_parallel_load: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            enable_homogenous_tablespace: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            extra_archived_log_dest_ids: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[jsii.Number]]] = None,
            fail_tasks_on_lob_truncation: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            number_datatype_scale: typing.Optional[jsii.Number] = None,
            oracle_path_prefix: typing.Optional[builtins.str] = None,
            parallel_asm_read_threads: typing.Optional[jsii.Number] = None,
            read_ahead_blocks: typing.Optional[jsii.Number] = None,
            read_table_space_name: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            replace_path_prefix: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            retry_interval: typing.Optional[jsii.Number] = None,
            secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
            secrets_manager_oracle_asm_access_role_arn: typing.Optional[builtins.str] = None,
            secrets_manager_oracle_asm_secret_id: typing.Optional[builtins.str] = None,
            secrets_manager_secret_id: typing.Optional[builtins.str] = None,
            security_db_encryption: typing.Optional[builtins.str] = None,
            security_db_encryption_name: typing.Optional[builtins.str] = None,
            spatial_data_option_to_geo_json_function_name: typing.Optional[builtins.str] = None,
            standby_delay_time: typing.Optional[jsii.Number] = None,
            use_alternate_folder_for_online: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            use_b_file: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            use_direct_path_full_load: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            use_logminer_reader: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            use_path_prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides information that defines an Oracle endpoint.

            This information includes the output format of records applied to the endpoint and details of transaction and control table data information. For information about other available settings, see `Extra connection attributes when using Oracle as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.ConnectionAttrib>`_ and `Extra connection attributes when using Oracle as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Oracle.html#CHAP_Target.Oracle.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

            :param access_alternate_directly: Set this attribute to ``false`` in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source. This tells the DMS instance to not access redo logs through any specified path prefix replacement using direct file access.
            :param additional_archived_log_dest_id: Set this attribute with ``ArchivedLogDestId`` in a primary/ standby setup. This attribute is useful in the case of a switchover. In this case, AWS DMS needs to know which destination to get archive redo logs from to read changes. This need arises because the previous primary instance is now a standby instance after switchover. Although AWS DMS supports the use of the Oracle ``RESETLOGS`` option to open the database, never use ``RESETLOGS`` unless necessary. For additional information about ``RESETLOGS`` , see `RMAN Data Repair Concepts <https://docs.aws.amazon.com/https://docs.oracle.com/en/database/oracle/oracle-database/19/bradv/rman-data-repair-concepts.html#GUID-1805CCF7-4AF2-482D-B65A-998192F89C2B>`_ in the *Oracle Database Backup and Recovery User's Guide* .
            :param add_supplemental_logging: Set this attribute to set up table-level supplemental logging for the Oracle database. This attribute enables PRIMARY KEY supplemental logging on all tables selected for a migration task. If you use this option, you still need to enable database-level supplemental logging.
            :param allow_select_nested_tables: Set this attribute to ``true`` to enable replication of Oracle tables containing columns that are nested tables or defined types.
            :param archived_log_dest_id: Specifies the ID of the destination for the archived redo logs. This value should be the same as a number in the dest_id column of the v$archived_log view. If you work with an additional redo log destination, use the ``AdditionalArchivedLogDestId`` option to specify the additional destination ID. Doing this improves performance by ensuring that the correct logs are accessed from the outset.
            :param archived_logs_only: When this field is set to ``Y`` , AWS DMS only accesses the archived redo logs. If the archived redo logs are stored on Automatic Storage Management (ASM) only, the AWS DMS user account needs to be granted ASM privileges.
            :param asm_password: For an Oracle source endpoint, your Oracle Automatic Storage Management (ASM) password. You can set this value from the ``*asm_user_password*`` value. You set this value as part of the comma-separated value that you set to the ``Password`` request parameter when you create the endpoint to access transaction logs using Binary Reader. For more information, see `Configuration for change data capture (CDC) on an Oracle source database <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC.Configuration>`_ .
            :param asm_server: For an Oracle source endpoint, your ASM server address. You can set this value from the ``asm_server`` value. You set ``asm_server`` as part of the extra connection attribute string to access an Oracle server with Binary Reader that uses ASM. For more information, see `Configuration for change data capture (CDC) on an Oracle source database <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC.Configuration>`_ .
            :param asm_user: For an Oracle source endpoint, your ASM user name. You can set this value from the ``asm_user`` value. You set ``asm_user`` as part of the extra connection attribute string to access an Oracle server with Binary Reader that uses ASM. For more information, see `Configuration for change data capture (CDC) on an Oracle source database <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC.Configuration>`_ .
            :param char_length_semantics: Specifies whether the length of a character column is in bytes or in characters. To indicate that the character column length is in characters, set this attribute to ``CHAR`` . Otherwise, the character column length is in bytes. Example: ``charLengthSemantics=CHAR;``
            :param direct_path_no_log: When set to ``true`` , this attribute helps to increase the commit rate on the Oracle target database by writing directly to tables and not writing a trail to database logs.
            :param direct_path_parallel_load: When set to ``true`` , this attribute specifies a parallel load when ``useDirectPathFullLoad`` is set to ``Y`` . This attribute also only applies when you use the AWS DMS parallel load feature. Note that the target table cannot have any constraints or indexes.
            :param enable_homogenous_tablespace: Set this attribute to enable homogenous tablespace replication and create existing tables or indexes under the same tablespace on the target.
            :param extra_archived_log_dest_ids: Specifies the IDs of one more destinations for one or more archived redo logs. These IDs are the values of the ``dest_id`` column in the ``v$archived_log`` view. Use this setting with the ``archivedLogDestId`` extra connection attribute in a primary-to-single setup or a primary-to-multiple-standby setup. This setting is useful in a switchover when you use an Oracle Data Guard database as a source. In this case, AWS DMS needs information about what destination to get archive redo logs from to read changes. AWS DMS needs this because after the switchover the previous primary is a standby instance. For example, in a primary-to-single standby setup you might apply the following settings. ``archivedLogDestId=1; ExtraArchivedLogDestIds=[2]`` In a primary-to-multiple-standby setup, you might apply the following settings. ``archivedLogDestId=1; ExtraArchivedLogDestIds=[2,3,4]`` Although AWS DMS supports the use of the Oracle ``RESETLOGS`` option to open the database, never use ``RESETLOGS`` unless it's necessary. For more information about ``RESETLOGS`` , see `RMAN Data Repair Concepts <https://docs.aws.amazon.com/https://docs.oracle.com/en/database/oracle/oracle-database/19/bradv/rman-data-repair-concepts.html#GUID-1805CCF7-4AF2-482D-B65A-998192F89C2B>`_ in the *Oracle Database Backup and Recovery User's Guide* .
            :param fail_tasks_on_lob_truncation: When set to ``true`` , this attribute causes a task to fail if the actual size of an LOB column is greater than the specified ``LobMaxSize`` . If a task is set to limited LOB mode and this option is set to ``true`` , the task fails instead of truncating the LOB data.
            :param number_datatype_scale: Specifies the number scale. You can select a scale up to 38, or you can select FLOAT. By default, the NUMBER data type is converted to precision 38, scale 10. Example: ``numberDataTypeScale=12``
            :param oracle_path_prefix: Set this string attribute to the required value in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source. This value specifies the default Oracle root used to access the redo logs.
            :param parallel_asm_read_threads: Set this attribute to change the number of threads that DMS configures to perform a change data capture (CDC) load using Oracle Automatic Storage Management (ASM). You can specify an integer value between 2 (the default) and 8 (the maximum). Use this attribute together with the ``readAheadBlocks`` attribute.
            :param read_ahead_blocks: Set this attribute to change the number of read-ahead blocks that DMS configures to perform a change data capture (CDC) load using Oracle Automatic Storage Management (ASM). You can specify an integer value between 1000 (the default) and 200,000 (the maximum).
            :param read_table_space_name: When set to ``true`` , this attribute supports tablespace replication.
            :param replace_path_prefix: Set this attribute to true in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source. This setting tells DMS instance to replace the default Oracle root with the specified ``usePathPrefix`` setting to access the redo logs.
            :param retry_interval: Specifies the number of seconds that the system waits before resending a query. Example: ``retryInterval=6;``
            :param secrets_manager_access_role_arn: The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in ``SecretsManagerSecret`` . The role must allow the ``iam:PassRole`` action. ``SecretsManagerSecret`` has the value of the AWS Secrets Manager secret that allows access to the Oracle endpoint. .. epigraph:: You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerSecretId`` . Or you can specify clear-text values for ``UserName`` , ``Password`` , ``ServerName`` , and ``Port`` . You can't specify both. For more information on creating this ``SecretsManagerSecret`` , the corresponding ``SecretsManagerAccessRoleArn`` , and the ``SecretsManagerSecretId`` that is required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .
            :param secrets_manager_oracle_asm_access_role_arn: Required only if your Oracle endpoint uses Advanced Storage Manager (ASM). The full ARN of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the ``SecretsManagerOracleAsmSecret`` . This ``SecretsManagerOracleAsmSecret`` has the secret value that allows access to the Oracle ASM of the endpoint. .. epigraph:: You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerOracleAsmSecretId`` . Or you can specify clear-text values for ``AsmUserName`` , ``AsmPassword`` , and ``AsmServerName`` . You can't specify both. For more information on creating this ``SecretsManagerOracleAsmSecret`` , the corresponding ``SecretsManagerOracleAsmAccessRoleArn`` , and the ``SecretsManagerOracleAsmSecretId`` that is required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .
            :param secrets_manager_oracle_asm_secret_id: Required only if your Oracle endpoint uses Advanced Storage Manager (ASM). The full ARN, partial ARN, or display name of the ``SecretsManagerOracleAsmSecret`` that contains the Oracle ASM connection details for the Oracle endpoint.
            :param secrets_manager_secret_id: The full ARN, partial ARN, or display name of the ``SecretsManagerSecret`` that contains the Oracle endpoint connection details.
            :param security_db_encryption: For an Oracle source endpoint, the transparent data encryption (TDE) password required by AWM DMS to access Oracle redo logs encrypted by TDE using Binary Reader. It is also the ``*TDE_Password*`` part of the comma-separated value you set to the ``Password`` request parameter when you create the endpoint. The ``SecurityDbEncryptian`` setting is related to this ``SecurityDbEncryptionName`` setting. For more information, see `Supported encryption methods for using Oracle as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.Encryption>`_ in the *AWS Database Migration Service User Guide* .
            :param security_db_encryption_name: For an Oracle source endpoint, the name of a key used for the transparent data encryption (TDE) of the columns and tablespaces in an Oracle source database that is encrypted using TDE. The key value is the value of the ``SecurityDbEncryption`` setting. For more information on setting the key name value of ``SecurityDbEncryptionName`` , see the information and example for setting the ``securityDbEncryptionName`` extra connection attribute in `Supported encryption methods for using Oracle as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.Encryption>`_ in the *AWS Database Migration Service User Guide* .
            :param spatial_data_option_to_geo_json_function_name: Use this attribute to convert ``SDO_GEOMETRY`` to ``GEOJSON`` format. By default, DMS calls the ``SDO2GEOJSON`` custom function if present and accessible. Or you can create your own custom function that mimics the operation of ``SDOGEOJSON`` and set ``SpatialDataOptionToGeoJsonFunctionName`` to call it instead.
            :param standby_delay_time: Use this attribute to specify a time in minutes for the delay in standby sync. If the source is an Oracle Active Data Guard standby database, use this attribute to specify the time lag between primary and standby databases. In AWS DMS , you can create an Oracle CDC task that uses an Active Data Guard standby instance as a source for replicating ongoing changes. Doing this eliminates the need to connect to an active database that might be in production.
            :param use_alternate_folder_for_online: Set this attribute to ``true`` in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source. This tells the DMS instance to use any specified prefix replacement to access all online redo logs.
            :param use_b_file: Set this attribute to Y to capture change data using the Binary Reader utility. Set ``UseLogminerReader`` to N to set this attribute to Y. To use Binary Reader with Amazon RDS for Oracle as the source, you set additional attributes. For more information about using this setting with Oracle Automatic Storage Management (ASM), see `Using Oracle LogMiner or AWS DMS Binary Reader for CDC <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC>`_ .
            :param use_direct_path_full_load: Set this attribute to Y to have AWS DMS use a direct path full load. Specify this value to use the direct path protocol in the Oracle Call Interface (OCI). By using this OCI protocol, you can bulk-load Oracle target tables during a full load.
            :param use_logminer_reader: Set this attribute to Y to capture change data using the Oracle LogMiner utility (the default). Set this attribute to N if you want to access the redo logs as a binary file. When you set ``UseLogminerReader`` to N, also set ``UseBfile`` to Y. For more information on this setting and using Oracle ASM, see `Using Oracle LogMiner or AWS DMS Binary Reader for CDC <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC>`_ in the *AWS DMS User Guide* .
            :param use_path_prefix: Set this string attribute to the required value in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source. This value specifies the path prefix used to replace the default Oracle root to access the redo logs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dms as dms
                
                oracle_settings_property = dms.CfnEndpoint.OracleSettingsProperty(
                    access_alternate_directly=False,
                    additional_archived_log_dest_id=123,
                    add_supplemental_logging=False,
                    allow_select_nested_tables=False,
                    archived_log_dest_id=123,
                    archived_logs_only=False,
                    asm_password="asmPassword",
                    asm_server="asmServer",
                    asm_user="asmUser",
                    char_length_semantics="charLengthSemantics",
                    direct_path_no_log=False,
                    direct_path_parallel_load=False,
                    enable_homogenous_tablespace=False,
                    extra_archived_log_dest_ids=[123],
                    fail_tasks_on_lob_truncation=False,
                    number_datatype_scale=123,
                    oracle_path_prefix="oraclePathPrefix",
                    parallel_asm_read_threads=123,
                    read_ahead_blocks=123,
                    read_table_space_name=False,
                    replace_path_prefix=False,
                    retry_interval=123,
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_oracle_asm_access_role_arn="secretsManagerOracleAsmAccessRoleArn",
                    secrets_manager_oracle_asm_secret_id="secretsManagerOracleAsmSecretId",
                    secrets_manager_secret_id="secretsManagerSecretId",
                    security_db_encryption="securityDbEncryption",
                    security_db_encryption_name="securityDbEncryptionName",
                    spatial_data_option_to_geo_json_function_name="spatialDataOptionToGeoJsonFunctionName",
                    standby_delay_time=123,
                    use_alternate_folder_for_online=False,
                    use_bFile=False,
                    use_direct_path_full_load=False,
                    use_logminer_reader=False,
                    use_path_prefix="usePathPrefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__464af41633f33a1ed9a8fe247f62c425817f547882c8631d54fe5ede395c9f20)
                check_type(argname="argument access_alternate_directly", value=access_alternate_directly, expected_type=type_hints["access_alternate_directly"])
                check_type(argname="argument additional_archived_log_dest_id", value=additional_archived_log_dest_id, expected_type=type_hints["additional_archived_log_dest_id"])
                check_type(argname="argument add_supplemental_logging", value=add_supplemental_logging, expected_type=type_hints["add_supplemental_logging"])
                check_type(argname="argument allow_select_nested_tables", value=allow_select_nested_tables, expected_type=type_hints["allow_select_nested_tables"])
                check_type(argname="argument archived_log_dest_id", value=archived_log_dest_id, expected_type=type_hints["archived_log_dest_id"])
                check_type(argname="argument archived_logs_only", value=archived_logs_only, expected_type=type_hints["archived_logs_only"])
                check_type(argname="argument asm_password", value=asm_password, expected_type=type_hints["asm_password"])
                check_type(argname="argument asm_server", value=asm_server, expected_type=type_hints["asm_server"])
                check_type(argname="argument asm_user", value=asm_user, expected_type=type_hints["asm_user"])
                check_type(argname="argument char_length_semantics", value=char_length_semantics, expected_type=type_hints["char_length_semantics"])
                check_type(argname="argument direct_path_no_log", value=direct_path_no_log, expected_type=type_hints["direct_path_no_log"])
                check_type(argname="argument direct_path_parallel_load", value=direct_path_parallel_load, expected_type=type_hints["direct_path_parallel_load"])
                check_type(argname="argument enable_homogenous_tablespace", value=enable_homogenous_tablespace, expected_type=type_hints["enable_homogenous_tablespace"])
                check_type(argname="argument extra_archived_log_dest_ids", value=extra_archived_log_dest_ids, expected_type=type_hints["extra_archived_log_dest_ids"])
                check_type(argname="argument fail_tasks_on_lob_truncation", value=fail_tasks_on_lob_truncation, expected_type=type_hints["fail_tasks_on_lob_truncation"])
                check_type(argname="argument number_datatype_scale", value=number_datatype_scale, expected_type=type_hints["number_datatype_scale"])
                check_type(argname="argument oracle_path_prefix", value=oracle_path_prefix, expected_type=type_hints["oracle_path_prefix"])
                check_type(argname="argument parallel_asm_read_threads", value=parallel_asm_read_threads, expected_type=type_hints["parallel_asm_read_threads"])
                check_type(argname="argument read_ahead_blocks", value=read_ahead_blocks, expected_type=type_hints["read_ahead_blocks"])
                check_type(argname="argument read_table_space_name", value=read_table_space_name, expected_type=type_hints["read_table_space_name"])
                check_type(argname="argument replace_path_prefix", value=replace_path_prefix, expected_type=type_hints["replace_path_prefix"])
                check_type(argname="argument retry_interval", value=retry_interval, expected_type=type_hints["retry_interval"])
                check_type(argname="argument secrets_manager_access_role_arn", value=secrets_manager_access_role_arn, expected_type=type_hints["secrets_manager_access_role_arn"])
                check_type(argname="argument secrets_manager_oracle_asm_access_role_arn", value=secrets_manager_oracle_asm_access_role_arn, expected_type=type_hints["secrets_manager_oracle_asm_access_role_arn"])
                check_type(argname="argument secrets_manager_oracle_asm_secret_id", value=secrets_manager_oracle_asm_secret_id, expected_type=type_hints["secrets_manager_oracle_asm_secret_id"])
                check_type(argname="argument secrets_manager_secret_id", value=secrets_manager_secret_id, expected_type=type_hints["secrets_manager_secret_id"])
                check_type(argname="argument security_db_encryption", value=security_db_encryption, expected_type=type_hints["security_db_encryption"])
                check_type(argname="argument security_db_encryption_name", value=security_db_encryption_name, expected_type=type_hints["security_db_encryption_name"])
                check_type(argname="argument spatial_data_option_to_geo_json_function_name", value=spatial_data_option_to_geo_json_function_name, expected_type=type_hints["spatial_data_option_to_geo_json_function_name"])
                check_type(argname="argument standby_delay_time", value=standby_delay_time, expected_type=type_hints["standby_delay_time"])
                check_type(argname="argument use_alternate_folder_for_online", value=use_alternate_folder_for_online, expected_type=type_hints["use_alternate_folder_for_online"])
                check_type(argname="argument use_b_file", value=use_b_file, expected_type=type_hints["use_b_file"])
                check_type(argname="argument use_direct_path_full_load", value=use_direct_path_full_load, expected_type=type_hints["use_direct_path_full_load"])
                check_type(argname="argument use_logminer_reader", value=use_logminer_reader, expected_type=type_hints["use_logminer_reader"])
                check_type(argname="argument use_path_prefix", value=use_path_prefix, expected_type=type_hints["use_path_prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if access_alternate_directly is not None:
                self._values["access_alternate_directly"] = access_alternate_directly
            if additional_archived_log_dest_id is not None:
                self._values["additional_archived_log_dest_id"] = additional_archived_log_dest_id
            if add_supplemental_logging is not None:
                self._values["add_supplemental_logging"] = add_supplemental_logging
            if allow_select_nested_tables is not None:
                self._values["allow_select_nested_tables"] = allow_select_nested_tables
            if archived_log_dest_id is not None:
                self._values["archived_log_dest_id"] = archived_log_dest_id
            if archived_logs_only is not None:
                self._values["archived_logs_only"] = archived_logs_only
            if asm_password is not None:
                self._values["asm_password"] = asm_password
            if asm_server is not None:
                self._values["asm_server"] = asm_server
            if asm_user is not None:
                self._values["asm_user"] = asm_user
            if char_length_semantics is not None:
                self._values["char_length_semantics"] = char_length_semantics
            if direct_path_no_log is not None:
                self._values["direct_path_no_log"] = direct_path_no_log
            if direct_path_parallel_load is not None:
                self._values["direct_path_parallel_load"] = direct_path_parallel_load
            if enable_homogenous_tablespace is not None:
                self._values["enable_homogenous_tablespace"] = enable_homogenous_tablespace
            if extra_archived_log_dest_ids is not None:
                self._values["extra_archived_log_dest_ids"] = extra_archived_log_dest_ids
            if fail_tasks_on_lob_truncation is not None:
                self._values["fail_tasks_on_lob_truncation"] = fail_tasks_on_lob_truncation
            if number_datatype_scale is not None:
                self._values["number_datatype_scale"] = number_datatype_scale
            if oracle_path_prefix is not None:
                self._values["oracle_path_prefix"] = oracle_path_prefix
            if parallel_asm_read_threads is not None:
                self._values["parallel_asm_read_threads"] = parallel_asm_read_threads
            if read_ahead_blocks is not None:
                self._values["read_ahead_blocks"] = read_ahead_blocks
            if read_table_space_name is not None:
                self._values["read_table_space_name"] = read_table_space_name
            if replace_path_prefix is not None:
                self._values["replace_path_prefix"] = replace_path_prefix
            if retry_interval is not None:
                self._values["retry_interval"] = retry_interval
            if secrets_manager_access_role_arn is not None:
                self._values["secrets_manager_access_role_arn"] = secrets_manager_access_role_arn
            if secrets_manager_oracle_asm_access_role_arn is not None:
                self._values["secrets_manager_oracle_asm_access_role_arn"] = secrets_manager_oracle_asm_access_role_arn
            if secrets_manager_oracle_asm_secret_id is not None:
                self._values["secrets_manager_oracle_asm_secret_id"] = secrets_manager_oracle_asm_secret_id
            if secrets_manager_secret_id is not None:
                self._values["secrets_manager_secret_id"] = secrets_manager_secret_id
            if security_db_encryption is not None:
                self._values["security_db_encryption"] = security_db_encryption
            if security_db_encryption_name is not None:
                self._values["security_db_encryption_name"] = security_db_encryption_name
            if spatial_data_option_to_geo_json_function_name is not None:
                self._values["spatial_data_option_to_geo_json_function_name"] = spatial_data_option_to_geo_json_function_name
            if standby_delay_time is not None:
                self._values["standby_delay_time"] = standby_delay_time
            if use_alternate_folder_for_online is not None:
                self._values["use_alternate_folder_for_online"] = use_alternate_folder_for_online
            if use_b_file is not None:
                self._values["use_b_file"] = use_b_file
            if use_direct_path_full_load is not None:
                self._values["use_direct_path_full_load"] = use_direct_path_full_load
            if use_logminer_reader is not None:
                self._values["use_logminer_reader"] = use_logminer_reader
            if use_path_prefix is not None:
                self._values["use_path_prefix"] = use_path_prefix

        @builtins.property
        def access_alternate_directly(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Set this attribute to ``false`` in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source.

            This tells the DMS instance to not access redo logs through any specified path prefix replacement using direct file access.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-accessalternatedirectly
            '''
            result = self._values.get("access_alternate_directly")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def additional_archived_log_dest_id(self) -> typing.Optional[jsii.Number]:
            '''Set this attribute with ``ArchivedLogDestId`` in a primary/ standby setup.

            This attribute is useful in the case of a switchover. In this case, AWS DMS needs to know which destination to get archive redo logs from to read changes. This need arises because the previous primary instance is now a standby instance after switchover.

            Although AWS DMS supports the use of the Oracle ``RESETLOGS`` option to open the database, never use ``RESETLOGS`` unless necessary. For additional information about ``RESETLOGS`` , see `RMAN Data Repair Concepts <https://docs.aws.amazon.com/https://docs.oracle.com/en/database/oracle/oracle-database/19/bradv/rman-data-repair-concepts.html#GUID-1805CCF7-4AF2-482D-B65A-998192F89C2B>`_ in the *Oracle Database Backup and Recovery User's Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-additionalarchivedlogdestid
            '''
            result = self._values.get("additional_archived_log_dest_id")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def add_supplemental_logging(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Set this attribute to set up table-level supplemental logging for the Oracle database.

            This attribute enables PRIMARY KEY supplemental logging on all tables selected for a migration task.

            If you use this option, you still need to enable database-level supplemental logging.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-addsupplementallogging
            '''
            result = self._values.get("add_supplemental_logging")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def allow_select_nested_tables(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Set this attribute to ``true`` to enable replication of Oracle tables containing columns that are nested tables or defined types.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-allowselectnestedtables
            '''
            result = self._values.get("allow_select_nested_tables")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def archived_log_dest_id(self) -> typing.Optional[jsii.Number]:
            '''Specifies the ID of the destination for the archived redo logs.

            This value should be the same as a number in the dest_id column of the v$archived_log view. If you work with an additional redo log destination, use the ``AdditionalArchivedLogDestId`` option to specify the additional destination ID. Doing this improves performance by ensuring that the correct logs are accessed from the outset.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-archivedlogdestid
            '''
            result = self._values.get("archived_log_dest_id")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def archived_logs_only(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''When this field is set to ``Y`` , AWS DMS only accesses the archived redo logs.

            If the archived redo logs are stored on Automatic Storage Management (ASM) only, the AWS DMS user account needs to be granted ASM privileges.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-archivedlogsonly
            '''
            result = self._values.get("archived_logs_only")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def asm_password(self) -> typing.Optional[builtins.str]:
            '''For an Oracle source endpoint, your Oracle Automatic Storage Management (ASM) password.

            You can set this value from the ``*asm_user_password*`` value. You set this value as part of the comma-separated value that you set to the ``Password`` request parameter when you create the endpoint to access transaction logs using Binary Reader. For more information, see `Configuration for change data capture (CDC) on an Oracle source database <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC.Configuration>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-asmpassword
            '''
            result = self._values.get("asm_password")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def asm_server(self) -> typing.Optional[builtins.str]:
            '''For an Oracle source endpoint, your ASM server address.

            You can set this value from the ``asm_server`` value. You set ``asm_server`` as part of the extra connection attribute string to access an Oracle server with Binary Reader that uses ASM. For more information, see `Configuration for change data capture (CDC) on an Oracle source database <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC.Configuration>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-asmserver
            '''
            result = self._values.get("asm_server")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def asm_user(self) -> typing.Optional[builtins.str]:
            '''For an Oracle source endpoint, your ASM user name.

            You can set this value from the ``asm_user`` value. You set ``asm_user`` as part of the extra connection attribute string to access an Oracle server with Binary Reader that uses ASM. For more information, see `Configuration for change data capture (CDC) on an Oracle source database <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC.Configuration>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-asmuser
            '''
            result = self._values.get("asm_user")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def char_length_semantics(self) -> typing.Optional[builtins.str]:
            '''Specifies whether the length of a character column is in bytes or in characters.

            To indicate that the character column length is in characters, set this attribute to ``CHAR`` . Otherwise, the character column length is in bytes.

            Example: ``charLengthSemantics=CHAR;``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-charlengthsemantics
            '''
            result = self._values.get("char_length_semantics")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def direct_path_no_log(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''When set to ``true`` , this attribute helps to increase the commit rate on the Oracle target database by writing directly to tables and not writing a trail to database logs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-directpathnolog
            '''
            result = self._values.get("direct_path_no_log")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def direct_path_parallel_load(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''When set to ``true`` , this attribute specifies a parallel load when ``useDirectPathFullLoad`` is set to ``Y`` .

            This attribute also only applies when you use the AWS DMS parallel load feature. Note that the target table cannot have any constraints or indexes.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-directpathparallelload
            '''
            result = self._values.get("direct_path_parallel_load")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def enable_homogenous_tablespace(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Set this attribute to enable homogenous tablespace replication and create existing tables or indexes under the same tablespace on the target.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-enablehomogenoustablespace
            '''
            result = self._values.get("enable_homogenous_tablespace")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def extra_archived_log_dest_ids(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[jsii.Number]]]:
            '''Specifies the IDs of one more destinations for one or more archived redo logs.

            These IDs are the values of the ``dest_id`` column in the ``v$archived_log`` view. Use this setting with the ``archivedLogDestId`` extra connection attribute in a primary-to-single setup or a primary-to-multiple-standby setup.

            This setting is useful in a switchover when you use an Oracle Data Guard database as a source. In this case, AWS DMS needs information about what destination to get archive redo logs from to read changes. AWS DMS needs this because after the switchover the previous primary is a standby instance. For example, in a primary-to-single standby setup you might apply the following settings.

            ``archivedLogDestId=1; ExtraArchivedLogDestIds=[2]``

            In a primary-to-multiple-standby setup, you might apply the following settings.

            ``archivedLogDestId=1; ExtraArchivedLogDestIds=[2,3,4]``

            Although AWS DMS supports the use of the Oracle ``RESETLOGS`` option to open the database, never use ``RESETLOGS`` unless it's necessary. For more information about ``RESETLOGS`` , see `RMAN Data Repair Concepts <https://docs.aws.amazon.com/https://docs.oracle.com/en/database/oracle/oracle-database/19/bradv/rman-data-repair-concepts.html#GUID-1805CCF7-4AF2-482D-B65A-998192F89C2B>`_ in the *Oracle Database Backup and Recovery User's Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-extraarchivedlogdestids
            '''
            result = self._values.get("extra_archived_log_dest_ids")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[jsii.Number]]], result)

        @builtins.property
        def fail_tasks_on_lob_truncation(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''When set to ``true`` , this attribute causes a task to fail if the actual size of an LOB column is greater than the specified ``LobMaxSize`` .

            If a task is set to limited LOB mode and this option is set to ``true`` , the task fails instead of truncating the LOB data.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-failtasksonlobtruncation
            '''
            result = self._values.get("fail_tasks_on_lob_truncation")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def number_datatype_scale(self) -> typing.Optional[jsii.Number]:
            '''Specifies the number scale.

            You can select a scale up to 38, or you can select FLOAT. By default, the NUMBER data type is converted to precision 38, scale 10.

            Example: ``numberDataTypeScale=12``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-numberdatatypescale
            '''
            result = self._values.get("number_datatype_scale")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def oracle_path_prefix(self) -> typing.Optional[builtins.str]:
            '''Set this string attribute to the required value in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source.

            This value specifies the default Oracle root used to access the redo logs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-oraclepathprefix
            '''
            result = self._values.get("oracle_path_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def parallel_asm_read_threads(self) -> typing.Optional[jsii.Number]:
            '''Set this attribute to change the number of threads that DMS configures to perform a change data capture (CDC) load using Oracle Automatic Storage Management (ASM).

            You can specify an integer value between 2 (the default) and 8 (the maximum). Use this attribute together with the ``readAheadBlocks`` attribute.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-parallelasmreadthreads
            '''
            result = self._values.get("parallel_asm_read_threads")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def read_ahead_blocks(self) -> typing.Optional[jsii.Number]:
            '''Set this attribute to change the number of read-ahead blocks that DMS configures to perform a change data capture (CDC) load using Oracle Automatic Storage Management (ASM).

            You can specify an integer value between 1000 (the default) and 200,000 (the maximum).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-readaheadblocks
            '''
            result = self._values.get("read_ahead_blocks")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def read_table_space_name(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''When set to ``true`` , this attribute supports tablespace replication.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-readtablespacename
            '''
            result = self._values.get("read_table_space_name")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def replace_path_prefix(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Set this attribute to true in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source.

            This setting tells DMS instance to replace the default Oracle root with the specified ``usePathPrefix`` setting to access the redo logs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-replacepathprefix
            '''
            result = self._values.get("replace_path_prefix")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def retry_interval(self) -> typing.Optional[jsii.Number]:
            '''Specifies the number of seconds that the system waits before resending a query.

            Example: ``retryInterval=6;``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-retryinterval
            '''
            result = self._values.get("retry_interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def secrets_manager_access_role_arn(self) -> typing.Optional[builtins.str]:
            '''The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in ``SecretsManagerSecret`` .

            The role must allow the ``iam:PassRole`` action. ``SecretsManagerSecret`` has the value of the AWS Secrets Manager secret that allows access to the Oracle endpoint.
            .. epigraph::

               You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerSecretId`` . Or you can specify clear-text values for ``UserName`` , ``Password`` , ``ServerName`` , and ``Port`` . You can't specify both.

               For more information on creating this ``SecretsManagerSecret`` , the corresponding ``SecretsManagerAccessRoleArn`` , and the ``SecretsManagerSecretId`` that is required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-secretsmanageraccessrolearn
            '''
            result = self._values.get("secrets_manager_access_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secrets_manager_oracle_asm_access_role_arn(
            self,
        ) -> typing.Optional[builtins.str]:
            '''Required only if your Oracle endpoint uses Advanced Storage Manager (ASM).

            The full ARN of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the ``SecretsManagerOracleAsmSecret`` . This ``SecretsManagerOracleAsmSecret`` has the secret value that allows access to the Oracle ASM of the endpoint.
            .. epigraph::

               You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerOracleAsmSecretId`` . Or you can specify clear-text values for ``AsmUserName`` , ``AsmPassword`` , and ``AsmServerName`` . You can't specify both.

               For more information on creating this ``SecretsManagerOracleAsmSecret`` , the corresponding ``SecretsManagerOracleAsmAccessRoleArn`` , and the ``SecretsManagerOracleAsmSecretId`` that is required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-secretsmanageroracleasmaccessrolearn
            '''
            result = self._values.get("secrets_manager_oracle_asm_access_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secrets_manager_oracle_asm_secret_id(self) -> typing.Optional[builtins.str]:
            '''Required only if your Oracle endpoint uses Advanced Storage Manager (ASM).

            The full ARN, partial ARN, or display name of the ``SecretsManagerOracleAsmSecret`` that contains the Oracle ASM connection details for the Oracle endpoint.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-secretsmanageroracleasmsecretid
            '''
            result = self._values.get("secrets_manager_oracle_asm_secret_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secrets_manager_secret_id(self) -> typing.Optional[builtins.str]:
            '''The full ARN, partial ARN, or display name of the ``SecretsManagerSecret`` that contains the Oracle endpoint connection details.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-secretsmanagersecretid
            '''
            result = self._values.get("secrets_manager_secret_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def security_db_encryption(self) -> typing.Optional[builtins.str]:
            '''For an Oracle source endpoint, the transparent data encryption (TDE) password required by AWM DMS to access Oracle redo logs encrypted by TDE using Binary Reader.

            It is also the ``*TDE_Password*`` part of the comma-separated value you set to the ``Password`` request parameter when you create the endpoint. The ``SecurityDbEncryptian`` setting is related to this ``SecurityDbEncryptionName`` setting. For more information, see `Supported encryption methods for using Oracle as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.Encryption>`_ in the *AWS Database Migration Service User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-securitydbencryption
            '''
            result = self._values.get("security_db_encryption")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def security_db_encryption_name(self) -> typing.Optional[builtins.str]:
            '''For an Oracle source endpoint, the name of a key used for the transparent data encryption (TDE) of the columns and tablespaces in an Oracle source database that is encrypted using TDE.

            The key value is the value of the ``SecurityDbEncryption`` setting. For more information on setting the key name value of ``SecurityDbEncryptionName`` , see the information and example for setting the ``securityDbEncryptionName`` extra connection attribute in `Supported encryption methods for using Oracle as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.Encryption>`_ in the *AWS Database Migration Service User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-securitydbencryptionname
            '''
            result = self._values.get("security_db_encryption_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def spatial_data_option_to_geo_json_function_name(
            self,
        ) -> typing.Optional[builtins.str]:
            '''Use this attribute to convert ``SDO_GEOMETRY`` to ``GEOJSON`` format.

            By default, DMS calls the ``SDO2GEOJSON`` custom function if present and accessible. Or you can create your own custom function that mimics the operation of ``SDOGEOJSON`` and set ``SpatialDataOptionToGeoJsonFunctionName`` to call it instead.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-spatialdataoptiontogeojsonfunctionname
            '''
            result = self._values.get("spatial_data_option_to_geo_json_function_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def standby_delay_time(self) -> typing.Optional[jsii.Number]:
            '''Use this attribute to specify a time in minutes for the delay in standby sync.

            If the source is an Oracle Active Data Guard standby database, use this attribute to specify the time lag between primary and standby databases.

            In AWS DMS , you can create an Oracle CDC task that uses an Active Data Guard standby instance as a source for replicating ongoing changes. Doing this eliminates the need to connect to an active database that might be in production.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-standbydelaytime
            '''
            result = self._values.get("standby_delay_time")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def use_alternate_folder_for_online(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Set this attribute to ``true`` in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source.

            This tells the DMS instance to use any specified prefix replacement to access all online redo logs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-usealternatefolderforonline
            '''
            result = self._values.get("use_alternate_folder_for_online")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def use_b_file(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Set this attribute to Y to capture change data using the Binary Reader utility.

            Set ``UseLogminerReader`` to N to set this attribute to Y. To use Binary Reader with Amazon RDS for Oracle as the source, you set additional attributes. For more information about using this setting with Oracle Automatic Storage Management (ASM), see `Using Oracle LogMiner or AWS DMS Binary Reader for CDC <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-usebfile
            '''
            result = self._values.get("use_b_file")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def use_direct_path_full_load(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Set this attribute to Y to have AWS DMS use a direct path full load.

            Specify this value to use the direct path protocol in the Oracle Call Interface (OCI). By using this OCI protocol, you can bulk-load Oracle target tables during a full load.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-usedirectpathfullload
            '''
            result = self._values.get("use_direct_path_full_load")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def use_logminer_reader(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''Set this attribute to Y to capture change data using the Oracle LogMiner utility (the default).

            Set this attribute to N if you want to access the redo logs as a binary file. When you set ``UseLogminerReader`` to N, also set ``UseBfile`` to Y. For more information on this setting and using Oracle ASM, see `Using Oracle LogMiner or AWS DMS Binary Reader for CDC <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC>`_ in the *AWS DMS User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-uselogminerreader
            '''
            result = self._values.get("use_logminer_reader")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def use_path_prefix(self) -> typing.Optional[builtins.str]:
            '''Set this string attribute to the required value in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source.

            This value specifies the path prefix used to replace the default Oracle root to access the redo logs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-usepathprefix
            '''
            result = self._values.get("use_path_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OracleSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dms.CfnEndpoint.PostgreSqlSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "after_connect_script": "afterConnectScript",
            "capture_ddls": "captureDdls",
            "ddl_artifacts_schema": "ddlArtifactsSchema",
            "execute_timeout": "executeTimeout",
            "fail_tasks_on_lob_truncation": "failTasksOnLobTruncation",
            "heartbeat_enable": "heartbeatEnable",
            "heartbeat_frequency": "heartbeatFrequency",
            "heartbeat_schema": "heartbeatSchema",
            "max_file_size": "maxFileSize",
            "plugin_name": "pluginName",
            "secrets_manager_access_role_arn": "secretsManagerAccessRoleArn",
            "secrets_manager_secret_id": "secretsManagerSecretId",
            "slot_name": "slotName",
        },
    )
    class PostgreSqlSettingsProperty:
        def __init__(
            self,
            *,
            after_connect_script: typing.Optional[builtins.str] = None,
            capture_ddls: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            ddl_artifacts_schema: typing.Optional[builtins.str] = None,
            execute_timeout: typing.Optional[jsii.Number] = None,
            fail_tasks_on_lob_truncation: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            heartbeat_enable: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            heartbeat_frequency: typing.Optional[jsii.Number] = None,
            heartbeat_schema: typing.Optional[builtins.str] = None,
            max_file_size: typing.Optional[jsii.Number] = None,
            plugin_name: typing.Optional[builtins.str] = None,
            secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
            secrets_manager_secret_id: typing.Optional[builtins.str] = None,
            slot_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides information that defines a PostgreSQL endpoint.

            This information includes the output format of records applied to the endpoint and details of transaction and control table data information. For information about other available settings, see `Extra connection attributes when using PostgreSQL as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.PostgreSQL.html#CHAP_Source.PostgreSQL.ConnectionAttrib>`_ and `Extra connection attributes when using PostgreSQL as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.PostgreSQL.html#CHAP_Target.PostgreSQL.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

            :param after_connect_script: For use with change data capture (CDC) only, this attribute has AWS DMS bypass foreign keys and user triggers to reduce the time it takes to bulk load data. Example: ``afterConnectScript=SET session_replication_role='replica'``
            :param capture_ddls: To capture DDL events, AWS DMS creates various artifacts in the PostgreSQL database when the task starts. You can later remove these artifacts. If this value is set to ``N`` , you don't have to create tables or triggers on the source database.
            :param ddl_artifacts_schema: The schema in which the operational DDL database artifacts are created. Example: ``ddlArtifactsSchema=xyzddlschema;``
            :param execute_timeout: Sets the client statement timeout for the PostgreSQL instance, in seconds. The default value is 60 seconds. Example: ``executeTimeout=100;``
            :param fail_tasks_on_lob_truncation: When set to ``true`` , this value causes a task to fail if the actual size of a LOB column is greater than the specified ``LobMaxSize`` . If task is set to Limited LOB mode and this option is set to true, the task fails instead of truncating the LOB data.
            :param heartbeat_enable: The write-ahead log (WAL) heartbeat feature mimics a dummy transaction. By doing this, it prevents idle logical replication slots from holding onto old WAL logs, which can result in storage full situations on the source. This heartbeat keeps ``restart_lsn`` moving and prevents storage full scenarios.
            :param heartbeat_frequency: Sets the WAL heartbeat frequency (in minutes).
            :param heartbeat_schema: Sets the schema in which the heartbeat artifacts are created.
            :param max_file_size: Specifies the maximum size (in KB) of any .csv file used to transfer data to PostgreSQL. Example: ``maxFileSize=512``
            :param plugin_name: Specifies the plugin to use to create a replication slot.
            :param secrets_manager_access_role_arn: The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in ``SecretsManagerSecret`` . The role must allow the ``iam:PassRole`` action. ``SecretsManagerSecret`` has the value of the AWS Secrets Manager secret that allows access to the PostgreSQL endpoint. .. epigraph:: You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerSecretId`` . Or you can specify clear-text values for ``UserName`` , ``Password`` , ``ServerName`` , and ``Port`` . You can't specify both. For more information on creating this ``SecretsManagerSecret`` , the corresponding ``SecretsManagerAccessRoleArn`` , and the ``SecretsManagerSecretId`` that is required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .
            :param secrets_manager_secret_id: The full ARN, partial ARN, or display name of the ``SecretsManagerSecret`` that contains the PostgreSQL endpoint connection details.
            :param slot_name: Sets the name of a previously created logical replication slot for a change data capture (CDC) load of the PostgreSQL source instance. When used with the ``CdcStartPosition`` request parameter for the AWS DMS API , this attribute also makes it possible to use native CDC start points. DMS verifies that the specified logical replication slot exists before starting the CDC load task. It also verifies that the task was created with a valid setting of ``CdcStartPosition`` . If the specified slot doesn't exist or the task doesn't have a valid ``CdcStartPosition`` setting, DMS raises an error. For more information about setting the ``CdcStartPosition`` request parameter, see `Determining a CDC native start point <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Task.CDC.html#CHAP_Task.CDC.StartPoint.Native>`_ in the *AWS Database Migration Service User Guide* . For more information about using ``CdcStartPosition`` , see `CreateReplicationTask <https://docs.aws.amazon.com/dms/latest/APIReference/API_CreateReplicationTask.html>`_ , `StartReplicationTask <https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTask.html>`_ , and `ModifyReplicationTask <https://docs.aws.amazon.com/dms/latest/APIReference/API_ModifyReplicationTask.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dms as dms
                
                postgre_sql_settings_property = dms.CfnEndpoint.PostgreSqlSettingsProperty(
                    after_connect_script="afterConnectScript",
                    capture_ddls=False,
                    ddl_artifacts_schema="ddlArtifactsSchema",
                    execute_timeout=123,
                    fail_tasks_on_lob_truncation=False,
                    heartbeat_enable=False,
                    heartbeat_frequency=123,
                    heartbeat_schema="heartbeatSchema",
                    max_file_size=123,
                    plugin_name="pluginName",
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_secret_id="secretsManagerSecretId",
                    slot_name="slotName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d7718c9f321a7e3ac2ac907ba6716972aa25acd11ecf939790c5f30bbdf9f4f8)
                check_type(argname="argument after_connect_script", value=after_connect_script, expected_type=type_hints["after_connect_script"])
                check_type(argname="argument capture_ddls", value=capture_ddls, expected_type=type_hints["capture_ddls"])
                check_type(argname="argument ddl_artifacts_schema", value=ddl_artifacts_schema, expected_type=type_hints["ddl_artifacts_schema"])
                check_type(argname="argument execute_timeout", value=execute_timeout, expected_type=type_hints["execute_timeout"])
                check_type(argname="argument fail_tasks_on_lob_truncation", value=fail_tasks_on_lob_truncation, expected_type=type_hints["fail_tasks_on_lob_truncation"])
                check_type(argname="argument heartbeat_enable", value=heartbeat_enable, expected_type=type_hints["heartbeat_enable"])
                check_type(argname="argument heartbeat_frequency", value=heartbeat_frequency, expected_type=type_hints["heartbeat_frequency"])
                check_type(argname="argument heartbeat_schema", value=heartbeat_schema, expected_type=type_hints["heartbeat_schema"])
                check_type(argname="argument max_file_size", value=max_file_size, expected_type=type_hints["max_file_size"])
                check_type(argname="argument plugin_name", value=plugin_name, expected_type=type_hints["plugin_name"])
                check_type(argname="argument secrets_manager_access_role_arn", value=secrets_manager_access_role_arn, expected_type=type_hints["secrets_manager_access_role_arn"])
                check_type(argname="argument secrets_manager_secret_id", value=secrets_manager_secret_id, expected_type=type_hints["secrets_manager_secret_id"])
                check_type(argname="argument slot_name", value=slot_name, expected_type=type_hints["slot_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if after_connect_script is not None:
                self._values["after_connect_script"] = after_connect_script
            if capture_ddls is not None:
                self._values["capture_ddls"] = capture_ddls
            if ddl_artifacts_schema is not None:
                self._values["ddl_artifacts_schema"] = ddl_artifacts_schema
            if execute_timeout is not None:
                self._values["execute_timeout"] = execute_timeout
            if fail_tasks_on_lob_truncation is not None:
                self._values["fail_tasks_on_lob_truncation"] = fail_tasks_on_lob_truncation
            if heartbeat_enable is not None:
                self._values["heartbeat_enable"] = heartbeat_enable
            if heartbeat_frequency is not None:
                self._values["heartbeat_frequency"] = heartbeat_frequency
            if heartbeat_schema is not None:
                self._values["heartbeat_schema"] = heartbeat_schema
            if max_file_size is not None:
                self._values["max_file_size"] = max_file_size
            if plugin_name is not None:
                self._values["plugin_name"] = plugin_name
            if secrets_manager_access_role_arn is not None:
                self._values["secrets_manager_access_role_arn"] = secrets_manager_access_role_arn
            if secrets_manager_secret_id is not None:
                self._values["secrets_manager_secret_id"] = secrets_manager_secret_id
            if slot_name is not None:
                self._values["slot_name"] = slot_name

        @builtins.property
        def after_connect_script(self) -> typing.Optional[builtins.str]:
            '''For use with change data capture (CDC) only, this attribute has AWS DMS bypass foreign keys and user triggers to reduce the time it takes to bulk load data.

            Example: ``afterConnectScript=SET session_replication_role='replica'``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-afterconnectscript
            '''
            result = self._values.get("after_connect_script")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def capture_ddls(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''To capture DDL events, AWS DMS creates various artifacts in the PostgreSQL database when the task starts.

            You can later remove these artifacts.

            If this value is set to ``N`` , you don't have to create tables or triggers on the source database.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-captureddls
            '''
            result = self._values.get("capture_ddls")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def ddl_artifacts_schema(self) -> typing.Optional[builtins.str]:
            '''The schema in which the operational DDL database artifacts are created.

            Example: ``ddlArtifactsSchema=xyzddlschema;``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-ddlartifactsschema
            '''
            result = self._values.get("ddl_artifacts_schema")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def execute_timeout(self) -> typing.Optional[jsii.Number]:
            '''Sets the client statement timeout for the PostgreSQL instance, in seconds. The default value is 60 seconds.

            Example: ``executeTimeout=100;``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-executetimeout
            '''
            result = self._values.get("execute_timeout")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def fail_tasks_on_lob_truncation(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''When set to ``true`` , this value causes a task to fail if the actual size of a LOB column is greater than the specified ``LobMaxSize`` .

            If task is set to Limited LOB mode and this option is set to true, the task fails instead of truncating the LOB data.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-failtasksonlobtruncation
            '''
            result = self._values.get("fail_tasks_on_lob_truncation")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def heartbeat_enable(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''The write-ahead log (WAL) heartbeat feature mimics a dummy transaction.

            By doing this, it prevents idle logical replication slots from holding onto old WAL logs, which can result in storage full situations on the source. This heartbeat keeps ``restart_lsn`` moving and prevents storage full scenarios.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-heartbeatenable
            '''
            result = self._values.get("heartbeat_enable")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def heartbeat_frequency(self) -> typing.Optional[jsii.Number]:
            '''Sets the WAL heartbeat frequency (in minutes).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-heartbeatfrequency
            '''
            result = self._values.get("heartbeat_frequency")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def heartbeat_schema(self) -> typing.Optional[builtins.str]:
            '''Sets the schema in which the heartbeat artifacts are created.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-heartbeatschema
            '''
            result = self._values.get("heartbeat_schema")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def max_file_size(self) -> typing.Optional[jsii.Number]:
            '''Specifies the maximum size (in KB) of any .csv file used to transfer data to PostgreSQL.

            Example: ``maxFileSize=512``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-maxfilesize
            '''
            result = self._values.get("max_file_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def plugin_name(self) -> typing.Optional[builtins.str]:
            '''Specifies the plugin to use to create a replication slot.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-pluginname
            '''
            result = self._values.get("plugin_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secrets_manager_access_role_arn(self) -> typing.Optional[builtins.str]:
            '''The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in ``SecretsManagerSecret`` .

            The role must allow the ``iam:PassRole`` action. ``SecretsManagerSecret`` has the value of the AWS Secrets Manager secret that allows access to the PostgreSQL endpoint.
            .. epigraph::

               You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerSecretId`` . Or you can specify clear-text values for ``UserName`` , ``Password`` , ``ServerName`` , and ``Port`` . You can't specify both.

               For more information on creating this ``SecretsManagerSecret`` , the corresponding ``SecretsManagerAccessRoleArn`` , and the ``SecretsManagerSecretId`` that is required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-secretsmanageraccessrolearn
            '''
            result = self._values.get("secrets_manager_access_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secrets_manager_secret_id(self) -> typing.Optional[builtins.str]:
            '''The full ARN, partial ARN, or display name of the ``SecretsManagerSecret`` that contains the PostgreSQL endpoint connection details.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-secretsmanagersecretid
            '''
            result = self._values.get("secrets_manager_secret_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def slot_name(self) -> typing.Optional[builtins.str]:
            '''Sets the name of a previously created logical replication slot for a change data capture (CDC) load of the PostgreSQL source instance.

            When used with the ``CdcStartPosition`` request parameter for the AWS DMS API , this attribute also makes it possible to use native CDC start points. DMS verifies that the specified logical replication slot exists before starting the CDC load task. It also verifies that the task was created with a valid setting of ``CdcStartPosition`` . If the specified slot doesn't exist or the task doesn't have a valid ``CdcStartPosition`` setting, DMS raises an error.

            For more information about setting the ``CdcStartPosition`` request parameter, see `Determining a CDC native start point <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Task.CDC.html#CHAP_Task.CDC.StartPoint.Native>`_ in the *AWS Database Migration Service User Guide* . For more information about using ``CdcStartPosition`` , see `CreateReplicationTask <https://docs.aws.amazon.com/dms/latest/APIReference/API_CreateReplicationTask.html>`_ , `StartReplicationTask <https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTask.html>`_ , and `ModifyReplicationTask <https://docs.aws.amazon.com/dms/latest/APIReference/API_ModifyReplicationTask.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-slotname
            '''
            result = self._values.get("slot_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PostgreSqlSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dms.CfnEndpoint.RedisSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "auth_password": "authPassword",
            "auth_type": "authType",
            "auth_user_name": "authUserName",
            "port": "port",
            "server_name": "serverName",
            "ssl_ca_certificate_arn": "sslCaCertificateArn",
            "ssl_security_protocol": "sslSecurityProtocol",
        },
    )
    class RedisSettingsProperty:
        def __init__(
            self,
            *,
            auth_password: typing.Optional[builtins.str] = None,
            auth_type: typing.Optional[builtins.str] = None,
            auth_user_name: typing.Optional[builtins.str] = None,
            port: typing.Optional[jsii.Number] = None,
            server_name: typing.Optional[builtins.str] = None,
            ssl_ca_certificate_arn: typing.Optional[builtins.str] = None,
            ssl_security_protocol: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides information that defines a Redis target endpoint.

            This information includes the output format of records applied to the endpoint and details of transaction and control table data information. For information about other available settings, see `Specifying endpoint settings for Redis as a target <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Redis.html#CHAP_Target.Redis.EndpointSettings>`_ in the *AWS Database Migration Service User Guide* .

            :param auth_password: The password provided with the ``auth-role`` and ``auth-token`` options of the ``AuthType`` setting for a Redis target endpoint.
            :param auth_type: The type of authentication to perform when connecting to a Redis target. Options include ``none`` , ``auth-token`` , and ``auth-role`` . The ``auth-token`` option requires an ``AuthPassword`` value to be provided. The ``auth-role`` option requires ``AuthUserName`` and ``AuthPassword`` values to be provided.
            :param auth_user_name: The user name provided with the ``auth-role`` option of the ``AuthType`` setting for a Redis target endpoint.
            :param port: Transmission Control Protocol (TCP) port for the endpoint.
            :param server_name: Fully qualified domain name of the endpoint.
            :param ssl_ca_certificate_arn: The Amazon Resource Name (ARN) for the certificate authority (CA) that DMS uses to connect to your Redis target endpoint.
            :param ssl_security_protocol: The connection to a Redis target endpoint using Transport Layer Security (TLS). Valid values include ``plaintext`` and ``ssl-encryption`` . The default is ``ssl-encryption`` . The ``ssl-encryption`` option makes an encrypted connection. Optionally, you can identify an Amazon Resource Name (ARN) for an SSL certificate authority (CA) using the ``SslCaCertificateArn`` setting. If an ARN isn't given for a CA, DMS uses the Amazon root CA. The ``plaintext`` option doesn't provide Transport Layer Security (TLS) encryption for traffic between endpoint and database.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redissettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dms as dms
                
                redis_settings_property = dms.CfnEndpoint.RedisSettingsProperty(
                    auth_password="authPassword",
                    auth_type="authType",
                    auth_user_name="authUserName",
                    port=123,
                    server_name="serverName",
                    ssl_ca_certificate_arn="sslCaCertificateArn",
                    ssl_security_protocol="sslSecurityProtocol"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b554461776ac556361ecd0dd0196b43627b912f433b8c4b1117c65b9d0fcf9c2)
                check_type(argname="argument auth_password", value=auth_password, expected_type=type_hints["auth_password"])
                check_type(argname="argument auth_type", value=auth_type, expected_type=type_hints["auth_type"])
                check_type(argname="argument auth_user_name", value=auth_user_name, expected_type=type_hints["auth_user_name"])
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
                check_type(argname="argument server_name", value=server_name, expected_type=type_hints["server_name"])
                check_type(argname="argument ssl_ca_certificate_arn", value=ssl_ca_certificate_arn, expected_type=type_hints["ssl_ca_certificate_arn"])
                check_type(argname="argument ssl_security_protocol", value=ssl_security_protocol, expected_type=type_hints["ssl_security_protocol"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if auth_password is not None:
                self._values["auth_password"] = auth_password
            if auth_type is not None:
                self._values["auth_type"] = auth_type
            if auth_user_name is not None:
                self._values["auth_user_name"] = auth_user_name
            if port is not None:
                self._values["port"] = port
            if server_name is not None:
                self._values["server_name"] = server_name
            if ssl_ca_certificate_arn is not None:
                self._values["ssl_ca_certificate_arn"] = ssl_ca_certificate_arn
            if ssl_security_protocol is not None:
                self._values["ssl_security_protocol"] = ssl_security_protocol

        @builtins.property
        def auth_password(self) -> typing.Optional[builtins.str]:
            '''The password provided with the ``auth-role`` and ``auth-token`` options of the ``AuthType`` setting for a Redis target endpoint.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redissettings.html#cfn-dms-endpoint-redissettings-authpassword
            '''
            result = self._values.get("auth_password")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def auth_type(self) -> typing.Optional[builtins.str]:
            '''The type of authentication to perform when connecting to a Redis target.

            Options include ``none`` , ``auth-token`` , and ``auth-role`` . The ``auth-token`` option requires an ``AuthPassword`` value to be provided. The ``auth-role`` option requires ``AuthUserName`` and ``AuthPassword`` values to be provided.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redissettings.html#cfn-dms-endpoint-redissettings-authtype
            '''
            result = self._values.get("auth_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def auth_user_name(self) -> typing.Optional[builtins.str]:
            '''The user name provided with the ``auth-role`` option of the ``AuthType`` setting for a Redis target endpoint.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redissettings.html#cfn-dms-endpoint-redissettings-authusername
            '''
            result = self._values.get("auth_user_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def port(self) -> typing.Optional[jsii.Number]:
            '''Transmission Control Protocol (TCP) port for the endpoint.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redissettings.html#cfn-dms-endpoint-redissettings-port
            '''
            result = self._values.get("port")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def server_name(self) -> typing.Optional[builtins.str]:
            '''Fully qualified domain name of the endpoint.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redissettings.html#cfn-dms-endpoint-redissettings-servername
            '''
            result = self._values.get("server_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ssl_ca_certificate_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) for the certificate authority (CA) that DMS uses to connect to your Redis target endpoint.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redissettings.html#cfn-dms-endpoint-redissettings-sslcacertificatearn
            '''
            result = self._values.get("ssl_ca_certificate_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ssl_security_protocol(self) -> typing.Optional[builtins.str]:
            '''The connection to a Redis target endpoint using Transport Layer Security (TLS).

            Valid values include ``plaintext`` and ``ssl-encryption`` . The default is ``ssl-encryption`` . The ``ssl-encryption`` option makes an encrypted connection. Optionally, you can identify an Amazon Resource Name (ARN) for an SSL certificate authority (CA) using the ``SslCaCertificateArn`` setting. If an ARN isn't given for a CA, DMS uses the Amazon root CA.

            The ``plaintext`` option doesn't provide Transport Layer Security (TLS) encryption for traffic between endpoint and database.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redissettings.html#cfn-dms-endpoint-redissettings-sslsecurityprotocol
            '''
            result = self._values.get("ssl_security_protocol")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RedisSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dms.CfnEndpoint.RedshiftSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "accept_any_date": "acceptAnyDate",
            "after_connect_script": "afterConnectScript",
            "bucket_folder": "bucketFolder",
            "bucket_name": "bucketName",
            "case_sensitive_names": "caseSensitiveNames",
            "comp_update": "compUpdate",
            "connection_timeout": "connectionTimeout",
            "date_format": "dateFormat",
            "empty_as_null": "emptyAsNull",
            "encryption_mode": "encryptionMode",
            "explicit_ids": "explicitIds",
            "file_transfer_upload_streams": "fileTransferUploadStreams",
            "load_timeout": "loadTimeout",
            "max_file_size": "maxFileSize",
            "remove_quotes": "removeQuotes",
            "replace_chars": "replaceChars",
            "replace_invalid_chars": "replaceInvalidChars",
            "secrets_manager_access_role_arn": "secretsManagerAccessRoleArn",
            "secrets_manager_secret_id": "secretsManagerSecretId",
            "server_side_encryption_kms_key_id": "serverSideEncryptionKmsKeyId",
            "service_access_role_arn": "serviceAccessRoleArn",
            "time_format": "timeFormat",
            "trim_blanks": "trimBlanks",
            "truncate_columns": "truncateColumns",
            "write_buffer_size": "writeBufferSize",
        },
    )
    class RedshiftSettingsProperty:
        def __init__(
            self,
            *,
            accept_any_date: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            after_connect_script: typing.Optional[builtins.str] = None,
            bucket_folder: typing.Optional[builtins.str] = None,
            bucket_name: typing.Optional[builtins.str] = None,
            case_sensitive_names: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            comp_update: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            connection_timeout: typing.Optional[jsii.Number] = None,
            date_format: typing.Optional[builtins.str] = None,
            empty_as_null: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            encryption_mode: typing.Optional[builtins.str] = None,
            explicit_ids: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            file_transfer_upload_streams: typing.Optional[jsii.Number] = None,
            load_timeout: typing.Optional[jsii.Number] = None,
            max_file_size: typing.Optional[jsii.Number] = None,
            remove_quotes: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            replace_chars: typing.Optional[builtins.str] = None,
            replace_invalid_chars: typing.Optional[builtins.str] = None,
            secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
            secrets_manager_secret_id: typing.Optional[builtins.str] = None,
            server_side_encryption_kms_key_id: typing.Optional[builtins.str] = None,
            service_access_role_arn: typing.Optional[builtins.str] = None,
            time_format: typing.Optional[builtins.str] = None,
            trim_blanks: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            truncate_columns: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            write_buffer_size: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Provides information that defines an Amazon Redshift endpoint.

            This information includes the output format of records applied to the endpoint and details of transaction and control table data information. For more information about other available settings, see `Extra connection attributes when using Amazon Redshift as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Redshift.html#CHAP_Target.Redshift.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

            :param accept_any_date: A value that indicates to allow any date format, including invalid formats such as 00/00/00 00:00:00, to be loaded without generating an error. You can choose ``true`` or ``false`` (the default). This parameter applies only to TIMESTAMP and DATE columns. Always use ACCEPTANYDATE with the DATEFORMAT parameter. If the date format for the data doesn't match the DATEFORMAT specification, Amazon Redshift inserts a NULL value into that field.
            :param after_connect_script: Code to run after connecting. This parameter should contain the code itself, not the name of a file containing the code.
            :param bucket_folder: An S3 folder where the comma-separated-value (.csv) files are stored before being uploaded to the target Redshift cluster. For full load mode, AWS DMS converts source records into .csv files and loads them to the *BucketFolder/TableID* path. AWS DMS uses the Redshift ``COPY`` command to upload the .csv files to the target table. The files are deleted once the ``COPY`` operation has finished. For more information, see `COPY <https://docs.aws.amazon.com/redshift/latest/dg/r_COPY.html>`_ in the *Amazon Redshift Database Developer Guide* . For change-data-capture (CDC) mode, AWS DMS creates a *NetChanges* table, and loads the .csv files to this *BucketFolder/NetChangesTableID* path.
            :param bucket_name: The name of the intermediate S3 bucket used to store .csv files before uploading data to Redshift.
            :param case_sensitive_names: If Amazon Redshift is configured to support case sensitive schema names, set ``CaseSensitiveNames`` to ``true`` . The default is ``false`` .
            :param comp_update: If you set ``CompUpdate`` to ``true`` Amazon Redshift applies automatic compression if the table is empty. This applies even if the table columns already have encodings other than ``RAW`` . If you set ``CompUpdate`` to ``false`` , automatic compression is disabled and existing column encodings aren't changed. The default is ``true`` .
            :param connection_timeout: A value that sets the amount of time to wait (in milliseconds) before timing out, beginning from when you initially establish a connection.
            :param date_format: The date format that you are using. Valid values are ``auto`` (case-sensitive), your date format string enclosed in quotes, or NULL. If this parameter is left unset (NULL), it defaults to a format of 'YYYY-MM-DD'. Using ``auto`` recognizes most strings, even some that aren't supported when you use a date format string. If your date and time values use formats different from each other, set this to ``auto`` .
            :param empty_as_null: A value that specifies whether AWS DMS should migrate empty CHAR and VARCHAR fields as NULL. A value of ``true`` sets empty CHAR and VARCHAR fields to null. The default is ``false`` .
            :param encryption_mode: The type of server-side encryption that you want to use for your data. This encryption type is part of the endpoint settings or the extra connections attributes for Amazon S3. You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` . .. epigraph:: For the ``ModifyEndpoint`` operation, you can change the existing value of the ``EncryptionMode`` parameter from ``SSE_KMS`` to ``SSE_S3`` . But you can’t change the existing value from ``SSE_S3`` to ``SSE_KMS`` . To use ``SSE_S3`` , create an AWS Identity and Access Management (IAM) role with a policy that allows ``"arn:aws:s3:::*"`` to use the following actions: ``"s3:PutObject", "s3:ListBucket"``
            :param explicit_ids: This setting is only valid for a full-load migration task. Set ``ExplicitIds`` to ``true`` to have tables with ``IDENTITY`` columns override their auto-generated values with explicit values loaded from the source data files used to populate the tables. The default is ``false`` .
            :param file_transfer_upload_streams: The number of threads used to upload a single file. This parameter accepts a value from 1 through 64. It defaults to 10. The number of parallel streams used to upload a single .csv file to an S3 bucket using S3 Multipart Upload. For more information, see `Multipart upload overview <https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html>`_ . ``FileTransferUploadStreams`` accepts a value from 1 through 64. It defaults to 10.
            :param load_timeout: The amount of time to wait (in milliseconds) before timing out of operations performed by AWS DMS on a Redshift cluster, such as Redshift COPY, INSERT, DELETE, and UPDATE.
            :param max_file_size: The maximum size (in KB) of any .csv file used to load data on an S3 bucket and transfer data to Amazon Redshift. It defaults to 1048576KB (1 GB).
            :param remove_quotes: A value that specifies to remove surrounding quotation marks from strings in the incoming data. All characters within the quotation marks, including delimiters, are retained. Choose ``true`` to remove quotation marks. The default is ``false`` .
            :param replace_chars: A value that specifies to replaces the invalid characters specified in ``ReplaceInvalidChars`` , substituting the specified characters instead. The default is ``"?"`` .
            :param replace_invalid_chars: A list of characters that you want to replace. Use with ``ReplaceChars`` .
            :param secrets_manager_access_role_arn: The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in ``SecretsManagerSecret`` . The role must allow the ``iam:PassRole`` action. ``SecretsManagerSecret`` has the value of the AWS Secrets Manager secret that allows access to the Amazon Redshift endpoint. .. epigraph:: You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerSecretId`` . Or you can specify clear-text values for ``UserName`` , ``Password`` , ``ServerName`` , and ``Port`` . You can't specify both. For more information on creating this ``SecretsManagerSecret`` , the corresponding ``SecretsManagerAccessRoleArn`` , and the ``SecretsManagerSecretId`` that is required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .
            :param secrets_manager_secret_id: The full ARN, partial ARN, or display name of the ``SecretsManagerSecret`` that contains the Amazon Redshift endpoint connection details.
            :param server_side_encryption_kms_key_id: The AWS KMS key ID. If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide this key ID. The key that you use needs an attached policy that enables IAM user permissions and allows use of the key.
            :param service_access_role_arn: The Amazon Resource Name (ARN) of the IAM role that has access to the Amazon Redshift service. The role must allow the ``iam:PassRole`` action.
            :param time_format: The time format that you want to use. Valid values are ``auto`` (case-sensitive), ``'timeformat_string'`` , ``'epochsecs'`` , or ``'epochmillisecs'`` . It defaults to 10. Using ``auto`` recognizes most strings, even some that aren't supported when you use a time format string. If your date and time values use formats different from each other, set this parameter to ``auto`` .
            :param trim_blanks: A value that specifies to remove the trailing white space characters from a VARCHAR string. This parameter applies only to columns with a VARCHAR data type. Choose ``true`` to remove unneeded white space. The default is ``false`` .
            :param truncate_columns: A value that specifies to truncate data in columns to the appropriate number of characters, so that the data fits in the column. This parameter applies only to columns with a VARCHAR or CHAR data type, and rows with a size of 4 MB or less. Choose ``true`` to truncate data. The default is ``false`` .
            :param write_buffer_size: The size (in KB) of the in-memory file write buffer used when generating .csv files on the local disk at the DMS replication instance. The default value is 1000 (buffer size is 1000KB).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dms as dms
                
                redshift_settings_property = dms.CfnEndpoint.RedshiftSettingsProperty(
                    accept_any_date=False,
                    after_connect_script="afterConnectScript",
                    bucket_folder="bucketFolder",
                    bucket_name="bucketName",
                    case_sensitive_names=False,
                    comp_update=False,
                    connection_timeout=123,
                    date_format="dateFormat",
                    empty_as_null=False,
                    encryption_mode="encryptionMode",
                    explicit_ids=False,
                    file_transfer_upload_streams=123,
                    load_timeout=123,
                    max_file_size=123,
                    remove_quotes=False,
                    replace_chars="replaceChars",
                    replace_invalid_chars="replaceInvalidChars",
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_secret_id="secretsManagerSecretId",
                    server_side_encryption_kms_key_id="serverSideEncryptionKmsKeyId",
                    service_access_role_arn="serviceAccessRoleArn",
                    time_format="timeFormat",
                    trim_blanks=False,
                    truncate_columns=False,
                    write_buffer_size=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__296834ac1ac0261ad3737a1bddc3d51ca428ac3e7f151aa7861afe37a343b544)
                check_type(argname="argument accept_any_date", value=accept_any_date, expected_type=type_hints["accept_any_date"])
                check_type(argname="argument after_connect_script", value=after_connect_script, expected_type=type_hints["after_connect_script"])
                check_type(argname="argument bucket_folder", value=bucket_folder, expected_type=type_hints["bucket_folder"])
                check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
                check_type(argname="argument case_sensitive_names", value=case_sensitive_names, expected_type=type_hints["case_sensitive_names"])
                check_type(argname="argument comp_update", value=comp_update, expected_type=type_hints["comp_update"])
                check_type(argname="argument connection_timeout", value=connection_timeout, expected_type=type_hints["connection_timeout"])
                check_type(argname="argument date_format", value=date_format, expected_type=type_hints["date_format"])
                check_type(argname="argument empty_as_null", value=empty_as_null, expected_type=type_hints["empty_as_null"])
                check_type(argname="argument encryption_mode", value=encryption_mode, expected_type=type_hints["encryption_mode"])
                check_type(argname="argument explicit_ids", value=explicit_ids, expected_type=type_hints["explicit_ids"])
                check_type(argname="argument file_transfer_upload_streams", value=file_transfer_upload_streams, expected_type=type_hints["file_transfer_upload_streams"])
                check_type(argname="argument load_timeout", value=load_timeout, expected_type=type_hints["load_timeout"])
                check_type(argname="argument max_file_size", value=max_file_size, expected_type=type_hints["max_file_size"])
                check_type(argname="argument remove_quotes", value=remove_quotes, expected_type=type_hints["remove_quotes"])
                check_type(argname="argument replace_chars", value=replace_chars, expected_type=type_hints["replace_chars"])
                check_type(argname="argument replace_invalid_chars", value=replace_invalid_chars, expected_type=type_hints["replace_invalid_chars"])
                check_type(argname="argument secrets_manager_access_role_arn", value=secrets_manager_access_role_arn, expected_type=type_hints["secrets_manager_access_role_arn"])
                check_type(argname="argument secrets_manager_secret_id", value=secrets_manager_secret_id, expected_type=type_hints["secrets_manager_secret_id"])
                check_type(argname="argument server_side_encryption_kms_key_id", value=server_side_encryption_kms_key_id, expected_type=type_hints["server_side_encryption_kms_key_id"])
                check_type(argname="argument service_access_role_arn", value=service_access_role_arn, expected_type=type_hints["service_access_role_arn"])
                check_type(argname="argument time_format", value=time_format, expected_type=type_hints["time_format"])
                check_type(argname="argument trim_blanks", value=trim_blanks, expected_type=type_hints["trim_blanks"])
                check_type(argname="argument truncate_columns", value=truncate_columns, expected_type=type_hints["truncate_columns"])
                check_type(argname="argument write_buffer_size", value=write_buffer_size, expected_type=type_hints["write_buffer_size"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if accept_any_date is not None:
                self._values["accept_any_date"] = accept_any_date
            if after_connect_script is not None:
                self._values["after_connect_script"] = after_connect_script
            if bucket_folder is not None:
                self._values["bucket_folder"] = bucket_folder
            if bucket_name is not None:
                self._values["bucket_name"] = bucket_name
            if case_sensitive_names is not None:
                self._values["case_sensitive_names"] = case_sensitive_names
            if comp_update is not None:
                self._values["comp_update"] = comp_update
            if connection_timeout is not None:
                self._values["connection_timeout"] = connection_timeout
            if date_format is not None:
                self._values["date_format"] = date_format
            if empty_as_null is not None:
                self._values["empty_as_null"] = empty_as_null
            if encryption_mode is not None:
                self._values["encryption_mode"] = encryption_mode
            if explicit_ids is not None:
                self._values["explicit_ids"] = explicit_ids
            if file_transfer_upload_streams is not None:
                self._values["file_transfer_upload_streams"] = file_transfer_upload_streams
            if load_timeout is not None:
                self._values["load_timeout"] = load_timeout
            if max_file_size is not None:
                self._values["max_file_size"] = max_file_size
            if remove_quotes is not None:
                self._values["remove_quotes"] = remove_quotes
            if replace_chars is not None:
                self._values["replace_chars"] = replace_chars
            if replace_invalid_chars is not None:
                self._values["replace_invalid_chars"] = replace_invalid_chars
            if secrets_manager_access_role_arn is not None:
                self._values["secrets_manager_access_role_arn"] = secrets_manager_access_role_arn
            if secrets_manager_secret_id is not None:
                self._values["secrets_manager_secret_id"] = secrets_manager_secret_id
            if server_side_encryption_kms_key_id is not None:
                self._values["server_side_encryption_kms_key_id"] = server_side_encryption_kms_key_id
            if service_access_role_arn is not None:
                self._values["service_access_role_arn"] = service_access_role_arn
            if time_format is not None:
                self._values["time_format"] = time_format
            if trim_blanks is not None:
                self._values["trim_blanks"] = trim_blanks
            if truncate_columns is not None:
                self._values["truncate_columns"] = truncate_columns
            if write_buffer_size is not None:
                self._values["write_buffer_size"] = write_buffer_size

        @builtins.property
        def accept_any_date(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''A value that indicates to allow any date format, including invalid formats such as 00/00/00 00:00:00, to be loaded without generating an error.

            You can choose ``true`` or ``false`` (the default).

            This parameter applies only to TIMESTAMP and DATE columns. Always use ACCEPTANYDATE with the DATEFORMAT parameter. If the date format for the data doesn't match the DATEFORMAT specification, Amazon Redshift inserts a NULL value into that field.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-acceptanydate
            '''
            result = self._values.get("accept_any_date")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def after_connect_script(self) -> typing.Optional[builtins.str]:
            '''Code to run after connecting.

            This parameter should contain the code itself, not the name of a file containing the code.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-afterconnectscript
            '''
            result = self._values.get("after_connect_script")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def bucket_folder(self) -> typing.Optional[builtins.str]:
            '''An S3 folder where the comma-separated-value (.csv) files are stored before being uploaded to the target Redshift cluster.

            For full load mode, AWS DMS converts source records into .csv files and loads them to the *BucketFolder/TableID* path. AWS DMS uses the Redshift ``COPY`` command to upload the .csv files to the target table. The files are deleted once the ``COPY`` operation has finished. For more information, see `COPY <https://docs.aws.amazon.com/redshift/latest/dg/r_COPY.html>`_ in the *Amazon Redshift Database Developer Guide* .

            For change-data-capture (CDC) mode, AWS DMS creates a *NetChanges* table, and loads the .csv files to this *BucketFolder/NetChangesTableID* path.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-bucketfolder
            '''
            result = self._values.get("bucket_folder")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def bucket_name(self) -> typing.Optional[builtins.str]:
            '''The name of the intermediate S3 bucket used to store .csv files before uploading data to Redshift.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-bucketname
            '''
            result = self._values.get("bucket_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def case_sensitive_names(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''If Amazon Redshift is configured to support case sensitive schema names, set ``CaseSensitiveNames`` to ``true`` .

            The default is ``false`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-casesensitivenames
            '''
            result = self._values.get("case_sensitive_names")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def comp_update(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''If you set ``CompUpdate`` to ``true`` Amazon Redshift applies automatic compression if the table is empty.

            This applies even if the table columns already have encodings other than ``RAW`` . If you set ``CompUpdate`` to ``false`` , automatic compression is disabled and existing column encodings aren't changed. The default is ``true`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-compupdate
            '''
            result = self._values.get("comp_update")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def connection_timeout(self) -> typing.Optional[jsii.Number]:
            '''A value that sets the amount of time to wait (in milliseconds) before timing out, beginning from when you initially establish a connection.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-connectiontimeout
            '''
            result = self._values.get("connection_timeout")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def date_format(self) -> typing.Optional[builtins.str]:
            '''The date format that you are using.

            Valid values are ``auto`` (case-sensitive), your date format string enclosed in quotes, or NULL. If this parameter is left unset (NULL), it defaults to a format of 'YYYY-MM-DD'. Using ``auto`` recognizes most strings, even some that aren't supported when you use a date format string.

            If your date and time values use formats different from each other, set this to ``auto`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-dateformat
            '''
            result = self._values.get("date_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def empty_as_null(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''A value that specifies whether AWS DMS should migrate empty CHAR and VARCHAR fields as NULL.

            A value of ``true`` sets empty CHAR and VARCHAR fields to null. The default is ``false`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-emptyasnull
            '''
            result = self._values.get("empty_as_null")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def encryption_mode(self) -> typing.Optional[builtins.str]:
            '''The type of server-side encryption that you want to use for your data.

            This encryption type is part of the endpoint settings or the extra connections attributes for Amazon S3. You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` .
            .. epigraph::

               For the ``ModifyEndpoint`` operation, you can change the existing value of the ``EncryptionMode`` parameter from ``SSE_KMS`` to ``SSE_S3`` . But you can’t change the existing value from ``SSE_S3`` to ``SSE_KMS`` .

            To use ``SSE_S3`` , create an AWS Identity and Access Management (IAM) role with a policy that allows ``"arn:aws:s3:::*"`` to use the following actions: ``"s3:PutObject", "s3:ListBucket"``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-encryptionmode
            '''
            result = self._values.get("encryption_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def explicit_ids(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''This setting is only valid for a full-load migration task.

            Set ``ExplicitIds`` to ``true`` to have tables with ``IDENTITY`` columns override their auto-generated values with explicit values loaded from the source data files used to populate the tables. The default is ``false`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-explicitids
            '''
            result = self._values.get("explicit_ids")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def file_transfer_upload_streams(self) -> typing.Optional[jsii.Number]:
            '''The number of threads used to upload a single file.

            This parameter accepts a value from 1 through 64. It defaults to 10.

            The number of parallel streams used to upload a single .csv file to an S3 bucket using S3 Multipart Upload. For more information, see `Multipart upload overview <https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html>`_ .

            ``FileTransferUploadStreams`` accepts a value from 1 through 64. It defaults to 10.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-filetransferuploadstreams
            '''
            result = self._values.get("file_transfer_upload_streams")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def load_timeout(self) -> typing.Optional[jsii.Number]:
            '''The amount of time to wait (in milliseconds) before timing out of operations performed by AWS DMS on a Redshift cluster, such as Redshift COPY, INSERT, DELETE, and UPDATE.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-loadtimeout
            '''
            result = self._values.get("load_timeout")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_file_size(self) -> typing.Optional[jsii.Number]:
            '''The maximum size (in KB) of any .csv file used to load data on an S3 bucket and transfer data to Amazon Redshift. It defaults to 1048576KB (1 GB).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-maxfilesize
            '''
            result = self._values.get("max_file_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def remove_quotes(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''A value that specifies to remove surrounding quotation marks from strings in the incoming data.

            All characters within the quotation marks, including delimiters, are retained. Choose ``true`` to remove quotation marks. The default is ``false`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-removequotes
            '''
            result = self._values.get("remove_quotes")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def replace_chars(self) -> typing.Optional[builtins.str]:
            '''A value that specifies to replaces the invalid characters specified in ``ReplaceInvalidChars`` , substituting the specified characters instead.

            The default is ``"?"`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-replacechars
            '''
            result = self._values.get("replace_chars")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def replace_invalid_chars(self) -> typing.Optional[builtins.str]:
            '''A list of characters that you want to replace.

            Use with ``ReplaceChars`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-replaceinvalidchars
            '''
            result = self._values.get("replace_invalid_chars")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secrets_manager_access_role_arn(self) -> typing.Optional[builtins.str]:
            '''The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in ``SecretsManagerSecret`` .

            The role must allow the ``iam:PassRole`` action. ``SecretsManagerSecret`` has the value of the AWS Secrets Manager secret that allows access to the Amazon Redshift endpoint.
            .. epigraph::

               You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerSecretId`` . Or you can specify clear-text values for ``UserName`` , ``Password`` , ``ServerName`` , and ``Port`` . You can't specify both.

               For more information on creating this ``SecretsManagerSecret`` , the corresponding ``SecretsManagerAccessRoleArn`` , and the ``SecretsManagerSecretId`` that is required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-secretsmanageraccessrolearn
            '''
            result = self._values.get("secrets_manager_access_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secrets_manager_secret_id(self) -> typing.Optional[builtins.str]:
            '''The full ARN, partial ARN, or display name of the ``SecretsManagerSecret`` that contains the Amazon Redshift endpoint connection details.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-secretsmanagersecretid
            '''
            result = self._values.get("secrets_manager_secret_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def server_side_encryption_kms_key_id(self) -> typing.Optional[builtins.str]:
            '''The AWS KMS key ID.

            If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide this key ID. The key that you use needs an attached policy that enables IAM user permissions and allows use of the key.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-serversideencryptionkmskeyid
            '''
            result = self._values.get("server_side_encryption_kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def service_access_role_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the IAM role that has access to the Amazon Redshift service.

            The role must allow the ``iam:PassRole`` action.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-serviceaccessrolearn
            '''
            result = self._values.get("service_access_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def time_format(self) -> typing.Optional[builtins.str]:
            '''The time format that you want to use.

            Valid values are ``auto`` (case-sensitive), ``'timeformat_string'`` , ``'epochsecs'`` , or ``'epochmillisecs'`` . It defaults to 10. Using ``auto`` recognizes most strings, even some that aren't supported when you use a time format string.

            If your date and time values use formats different from each other, set this parameter to ``auto`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-timeformat
            '''
            result = self._values.get("time_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def trim_blanks(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''A value that specifies to remove the trailing white space characters from a VARCHAR string.

            This parameter applies only to columns with a VARCHAR data type. Choose ``true`` to remove unneeded white space. The default is ``false`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-trimblanks
            '''
            result = self._values.get("trim_blanks")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def truncate_columns(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''A value that specifies to truncate data in columns to the appropriate number of characters, so that the data fits in the column.

            This parameter applies only to columns with a VARCHAR or CHAR data type, and rows with a size of 4 MB or less. Choose ``true`` to truncate data. The default is ``false`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-truncatecolumns
            '''
            result = self._values.get("truncate_columns")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def write_buffer_size(self) -> typing.Optional[jsii.Number]:
            '''The size (in KB) of the in-memory file write buffer used when generating .csv files on the local disk at the DMS replication instance. The default value is 1000 (buffer size is 1000KB).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-writebuffersize
            '''
            result = self._values.get("write_buffer_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RedshiftSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dms.CfnEndpoint.S3SettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "add_column_name": "addColumnName",
            "bucket_folder": "bucketFolder",
            "bucket_name": "bucketName",
            "canned_acl_for_objects": "cannedAclForObjects",
            "cdc_inserts_and_updates": "cdcInsertsAndUpdates",
            "cdc_inserts_only": "cdcInsertsOnly",
            "cdc_max_batch_interval": "cdcMaxBatchInterval",
            "cdc_min_file_size": "cdcMinFileSize",
            "cdc_path": "cdcPath",
            "compression_type": "compressionType",
            "csv_delimiter": "csvDelimiter",
            "csv_no_sup_value": "csvNoSupValue",
            "csv_null_value": "csvNullValue",
            "csv_row_delimiter": "csvRowDelimiter",
            "data_format": "dataFormat",
            "data_page_size": "dataPageSize",
            "date_partition_delimiter": "datePartitionDelimiter",
            "date_partition_enabled": "datePartitionEnabled",
            "date_partition_sequence": "datePartitionSequence",
            "date_partition_timezone": "datePartitionTimezone",
            "dict_page_size_limit": "dictPageSizeLimit",
            "enable_statistics": "enableStatistics",
            "encoding_type": "encodingType",
            "encryption_mode": "encryptionMode",
            "external_table_definition": "externalTableDefinition",
            "ignore_header_rows": "ignoreHeaderRows",
            "include_op_for_full_load": "includeOpForFullLoad",
            "max_file_size": "maxFileSize",
            "parquet_timestamp_in_millisecond": "parquetTimestampInMillisecond",
            "parquet_version": "parquetVersion",
            "preserve_transactions": "preserveTransactions",
            "rfc4180": "rfc4180",
            "row_group_length": "rowGroupLength",
            "server_side_encryption_kms_key_id": "serverSideEncryptionKmsKeyId",
            "service_access_role_arn": "serviceAccessRoleArn",
            "timestamp_column_name": "timestampColumnName",
            "use_csv_no_sup_value": "useCsvNoSupValue",
            "use_task_start_time_for_full_load_timestamp": "useTaskStartTimeForFullLoadTimestamp",
        },
    )
    class S3SettingsProperty:
        def __init__(
            self,
            *,
            add_column_name: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            bucket_folder: typing.Optional[builtins.str] = None,
            bucket_name: typing.Optional[builtins.str] = None,
            canned_acl_for_objects: typing.Optional[builtins.str] = None,
            cdc_inserts_and_updates: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            cdc_inserts_only: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            cdc_max_batch_interval: typing.Optional[jsii.Number] = None,
            cdc_min_file_size: typing.Optional[jsii.Number] = None,
            cdc_path: typing.Optional[builtins.str] = None,
            compression_type: typing.Optional[builtins.str] = None,
            csv_delimiter: typing.Optional[builtins.str] = None,
            csv_no_sup_value: typing.Optional[builtins.str] = None,
            csv_null_value: typing.Optional[builtins.str] = None,
            csv_row_delimiter: typing.Optional[builtins.str] = None,
            data_format: typing.Optional[builtins.str] = None,
            data_page_size: typing.Optional[jsii.Number] = None,
            date_partition_delimiter: typing.Optional[builtins.str] = None,
            date_partition_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            date_partition_sequence: typing.Optional[builtins.str] = None,
            date_partition_timezone: typing.Optional[builtins.str] = None,
            dict_page_size_limit: typing.Optional[jsii.Number] = None,
            enable_statistics: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            encoding_type: typing.Optional[builtins.str] = None,
            encryption_mode: typing.Optional[builtins.str] = None,
            external_table_definition: typing.Optional[builtins.str] = None,
            ignore_header_rows: typing.Optional[jsii.Number] = None,
            include_op_for_full_load: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            max_file_size: typing.Optional[jsii.Number] = None,
            parquet_timestamp_in_millisecond: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            parquet_version: typing.Optional[builtins.str] = None,
            preserve_transactions: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            rfc4180: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            row_group_length: typing.Optional[jsii.Number] = None,
            server_side_encryption_kms_key_id: typing.Optional[builtins.str] = None,
            service_access_role_arn: typing.Optional[builtins.str] = None,
            timestamp_column_name: typing.Optional[builtins.str] = None,
            use_csv_no_sup_value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            use_task_start_time_for_full_load_timestamp: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''Provides information that defines an Amazon S3 endpoint.

            This information includes the output format of records applied to the endpoint and details of transaction and control table data information. For more information about the available settings, see `Extra connection attributes when using Amazon S3 as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.S3.html#CHAP_Source.S3.Configuring>`_ and `Extra connection attributes when using Amazon S3 as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring>`_ in the *AWS Database Migration Service User Guide* .

            :param add_column_name: An optional parameter that, when set to ``true`` or ``y`` , you can use to add column name information to the .csv output file. The default value is ``false`` . Valid values are ``true`` , ``false`` , ``y`` , and ``n`` .
            :param bucket_folder: An optional parameter to set a folder name in the S3 bucket. If provided, tables are created in the path ``*bucketFolder* / *schema_name* / *table_name* /`` . If this parameter isn't specified, the path used is ``*schema_name* / *table_name* /`` .
            :param bucket_name: The name of the S3 bucket.
            :param canned_acl_for_objects: A value that enables AWS DMS to specify a predefined (canned) access control list (ACL) for objects created in an Amazon S3 bucket as .csv or .parquet files. For more information about Amazon S3 canned ACLs, see `Canned ACL <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`_ in the *Amazon S3 Developer Guide* . The default value is NONE. Valid values include NONE, PRIVATE, PUBLIC_READ, PUBLIC_READ_WRITE, AUTHENTICATED_READ, AWS_EXEC_READ, BUCKET_OWNER_READ, and BUCKET_OWNER_FULL_CONTROL.
            :param cdc_inserts_and_updates: A value that enables a change data capture (CDC) load to write INSERT and UPDATE operations to .csv or .parquet (columnar storage) output files. The default setting is ``false`` , but when ``CdcInsertsAndUpdates`` is set to ``true`` or ``y`` , only INSERTs and UPDATEs from the source database are migrated to the .csv or .parquet file. For .csv file format only, how these INSERTs and UPDATEs are recorded depends on the value of the ``IncludeOpForFullLoad`` parameter. If ``IncludeOpForFullLoad`` is set to ``true`` , the first field of every CDC record is set to either ``I`` or ``U`` to indicate INSERT and UPDATE operations at the source. But if ``IncludeOpForFullLoad`` is set to ``false`` , CDC records are written without an indication of INSERT or UPDATE operations at the source. For more information about how these settings work together, see `Indicating Source DB Operations in Migrated S3 Data <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`_ in the *AWS Database Migration Service User Guide* . .. epigraph:: AWS DMS supports the use of the ``CdcInsertsAndUpdates`` parameter in versions 3.3.1 and later. ``CdcInsertsOnly`` and ``CdcInsertsAndUpdates`` can't both be set to ``true`` for the same endpoint. Set either ``CdcInsertsOnly`` or ``CdcInsertsAndUpdates`` to ``true`` for the same endpoint, but not both.
            :param cdc_inserts_only: A value that enables a change data capture (CDC) load to write only INSERT operations to .csv or columnar storage (.parquet) output files. By default (the ``false`` setting), the first field in a .csv or .parquet record contains the letter I (INSERT), U (UPDATE), or D (DELETE). These values indicate whether the row was inserted, updated, or deleted at the source database for a CDC load to the target. If ``CdcInsertsOnly`` is set to ``true`` or ``y`` , only INSERTs from the source database are migrated to the .csv or .parquet file. For .csv format only, how these INSERTs are recorded depends on the value of ``IncludeOpForFullLoad`` . If ``IncludeOpForFullLoad`` is set to ``true`` , the first field of every CDC record is set to I to indicate the INSERT operation at the source. If ``IncludeOpForFullLoad`` is set to ``false`` , every CDC record is written without a first field to indicate the INSERT operation at the source. For more information about how these settings work together, see `Indicating Source DB Operations in Migrated S3 Data <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`_ in the *AWS Database Migration Service User Guide* . .. epigraph:: AWS DMS supports the interaction described preceding between the ``CdcInsertsOnly`` and ``IncludeOpForFullLoad`` parameters in versions 3.1.4 and later. ``CdcInsertsOnly`` and ``CdcInsertsAndUpdates`` can't both be set to ``true`` for the same endpoint. Set either ``CdcInsertsOnly`` or ``CdcInsertsAndUpdates`` to ``true`` for the same endpoint, but not both.
            :param cdc_max_batch_interval: Maximum length of the interval, defined in seconds, after which to output a file to Amazon S3. When ``CdcMaxBatchInterval`` and ``CdcMinFileSize`` are both specified, the file write is triggered by whichever parameter condition is met first within an AWS DMS CloudFormation template. The default value is 60 seconds.
            :param cdc_min_file_size: Minimum file size, defined in kilobytes, to reach for a file output to Amazon S3. When ``CdcMinFileSize`` and ``CdcMaxBatchInterval`` are both specified, the file write is triggered by whichever parameter condition is met first within an AWS DMS CloudFormation template. The default value is 32 MB.
            :param cdc_path: Specifies the folder path of CDC files. For an S3 source, this setting is required if a task captures change data; otherwise, it's optional. If ``CdcPath`` is set, AWS DMS reads CDC files from this path and replicates the data changes to the target endpoint. For an S3 target if you set ```PreserveTransactions`` <https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings-PreserveTransactions>`_ to ``true`` , AWS DMS verifies that you have set this parameter to a folder path on your S3 target where AWS DMS can save the transaction order for the CDC load. AWS DMS creates this CDC folder path in either your S3 target working directory or the S3 target location specified by ```BucketFolder`` <https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings-BucketFolder>`_ and ```BucketName`` <https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings-BucketName>`_ . For example, if you specify ``CdcPath`` as ``MyChangedData`` , and you specify ``BucketName`` as ``MyTargetBucket`` but do not specify ``BucketFolder`` , AWS DMS creates the CDC folder path following: ``MyTargetBucket/MyChangedData`` . If you specify the same ``CdcPath`` , and you specify ``BucketName`` as ``MyTargetBucket`` and ``BucketFolder`` as ``MyTargetData`` , AWS DMS creates the CDC folder path following: ``MyTargetBucket/MyTargetData/MyChangedData`` . For more information on CDC including transaction order on an S3 target, see `Capturing data changes (CDC) including transaction order on the S3 target <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.EndpointSettings.CdcPath>`_ . .. epigraph:: This setting is supported in AWS DMS versions 3.4.2 and later.
            :param compression_type: An optional parameter. When set to GZIP it enables the service to compress the target files. To allow the service to write the target files uncompressed, either set this parameter to NONE (the default) or don't specify the parameter at all. This parameter applies to both .csv and .parquet file formats.
            :param csv_delimiter: The delimiter used to separate columns in the .csv file for both source and target. The default is a comma.
            :param csv_no_sup_value: This setting only applies if your Amazon S3 output files during a change data capture (CDC) load are written in .csv format. If ```UseCsvNoSupValue`` <https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings-UseCsvNoSupValue>`_ is set to true, specify a string value that you want AWS DMS to use for all columns not included in the supplemental log. If you do not specify a string value, AWS DMS uses the null value for these columns regardless of the ``UseCsvNoSupValue`` setting. .. epigraph:: This setting is supported in AWS DMS versions 3.4.1 and later.
            :param csv_null_value: An optional parameter that specifies how AWS DMS treats null values. While handling the null value, you can use this parameter to pass a user-defined string as null when writing to the target. For example, when target columns are not nullable, you can use this option to differentiate between the empty string value and the null value. So, if you set this parameter value to the empty string ("" or ''), AWS DMS treats the empty string as the null value instead of ``NULL`` . The default value is ``NULL`` . Valid values include any valid string.
            :param csv_row_delimiter: The delimiter used to separate rows in the .csv file for both source and target. The default is a carriage return ( ``\\n`` ).
            :param data_format: The format of the data that you want to use for output. You can choose one of the following:. - ``csv`` : This is a row-based file format with comma-separated values (.csv). - ``parquet`` : Apache Parquet (.parquet) is a columnar storage file format that features efficient compression and provides faster query response.
            :param data_page_size: The size of one data page in bytes. This parameter defaults to 1024 * 1024 bytes (1 MiB). This number is used for .parquet file format only.
            :param date_partition_delimiter: Specifies a date separating delimiter to use during folder partitioning. The default value is ``SLASH`` . Use this parameter when ``DatePartitionedEnabled`` is set to ``true`` .
            :param date_partition_enabled: When set to ``true`` , this parameter partitions S3 bucket folders based on transaction commit dates. The default value is ``false`` . For more information about date-based folder partitioning, see `Using date-based folder partitioning <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.DatePartitioning>`_ .
            :param date_partition_sequence: Identifies the sequence of the date format to use during folder partitioning. The default value is ``YYYYMMDD`` . Use this parameter when ``DatePartitionedEnabled`` is set to ``true`` .
            :param date_partition_timezone: When creating an S3 target endpoint, set ``DatePartitionTimezone`` to convert the current UTC time into a specified time zone. The conversion occurs when a date partition folder is created and a change data capture (CDC) file name is generated. The time zone format is Area/Location. Use this parameter when ``DatePartitionedEnabled`` is set to ``true`` , as shown in the following example. ``s3-settings='{"DatePartitionEnabled": true, "DatePartitionSequence": "YYYYMMDDHH", "DatePartitionDelimiter": "SLASH", "DatePartitionTimezone":" *Asia/Seoul* ", "BucketName": "dms-nattarat-test"}'``
            :param dict_page_size_limit: The maximum size of an encoded dictionary page of a column. If the dictionary page exceeds this, this column is stored using an encoding type of ``PLAIN`` . This parameter defaults to 1024 * 1024 bytes (1 MiB), the maximum size of a dictionary page before it reverts to ``PLAIN`` encoding. This size is used for .parquet file format only.
            :param enable_statistics: A value that enables statistics for Parquet pages and row groups. Choose ``true`` to enable statistics, ``false`` to disable. Statistics include ``NULL`` , ``DISTINCT`` , ``MAX`` , and ``MIN`` values. This parameter defaults to ``true`` . This value is used for .parquet file format only.
            :param encoding_type: The type of encoding that you're using:. - ``RLE_DICTIONARY`` uses a combination of bit-packing and run-length encoding to store repeated values more efficiently. This is the default. - ``PLAIN`` doesn't use encoding at all. Values are stored as they are. - ``PLAIN_DICTIONARY`` builds a dictionary of the values encountered in a given column. The dictionary is stored in a dictionary page for each column chunk.
            :param encryption_mode: The type of server-side encryption that you want to use for your data. This encryption type is part of the endpoint settings or the extra connections attributes for Amazon S3. You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` . .. epigraph:: For the ``ModifyEndpoint`` operation, you can change the existing value of the ``EncryptionMode`` parameter from ``SSE_KMS`` to ``SSE_S3`` . But you can’t change the existing value from ``SSE_S3`` to ``SSE_KMS`` . To use ``SSE_S3`` , you need an IAM role with permission to allow ``"arn:aws:s3:::dms-*"`` to use the following actions: - ``s3:CreateBucket`` - ``s3:ListBucket`` - ``s3:DeleteBucket`` - ``s3:GetBucketLocation`` - ``s3:GetObject`` - ``s3:PutObject`` - ``s3:DeleteObject`` - ``s3:GetObjectVersion`` - ``s3:GetBucketPolicy`` - ``s3:PutBucketPolicy`` - ``s3:DeleteBucketPolicy``
            :param external_table_definition: The external table definition. Conditional: If ``S3`` is used as a source then ``ExternalTableDefinition`` is required.
            :param ignore_header_rows: When this value is set to 1, AWS DMS ignores the first row header in a .csv file. A value of 1 turns on the feature; a value of 0 turns off the feature. The default is 0.
            :param include_op_for_full_load: A value that enables a full load to write INSERT operations to the comma-separated value (.csv) output files only to indicate how the rows were added to the source database. .. epigraph:: AWS DMS supports the ``IncludeOpForFullLoad`` parameter in versions 3.1.4 and later. For full load, records can only be inserted. By default (the ``false`` setting), no information is recorded in these output files for a full load to indicate that the rows were inserted at the source database. If ``IncludeOpForFullLoad`` is set to ``true`` or ``y`` , the INSERT is recorded as an I annotation in the first field of the .csv file. This allows the format of your target records from a full load to be consistent with the target records from a CDC load. .. epigraph:: This setting works together with the ``CdcInsertsOnly`` and the ``CdcInsertsAndUpdates`` parameters for output to .csv files only. For more information about how these settings work together, see `Indicating Source DB Operations in Migrated S3 Data <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`_ in the *AWS Database Migration Service User Guide* .
            :param max_file_size: A value that specifies the maximum size (in KB) of any .csv file to be created while migrating to an S3 target during full load. The default value is 1,048,576 KB (1 GB). Valid values include 1 to 1,048,576.
            :param parquet_timestamp_in_millisecond: A value that specifies the precision of any ``TIMESTAMP`` column values that are written to an Amazon S3 object file in .parquet format. .. epigraph:: AWS DMS supports the ``ParquetTimestampInMillisecond`` parameter in versions 3.1.4 and later. When ``ParquetTimestampInMillisecond`` is set to ``true`` or ``y`` , AWS DMS writes all ``TIMESTAMP`` columns in a .parquet formatted file with millisecond precision. Otherwise, DMS writes them with microsecond precision. Currently, Amazon Athena and AWS Glue can handle only millisecond precision for ``TIMESTAMP`` values. Set this parameter to ``true`` for S3 endpoint object files that are .parquet formatted only if you plan to query or process the data with Athena or AWS Glue . .. epigraph:: AWS DMS writes any ``TIMESTAMP`` column values written to an S3 file in .csv format with microsecond precision. Setting ``ParquetTimestampInMillisecond`` has no effect on the string format of the timestamp column value that is inserted by setting the ``TimestampColumnName`` parameter.
            :param parquet_version: The version of the Apache Parquet format that you want to use: ``parquet_1_0`` (the default) or ``parquet_2_0`` .
            :param preserve_transactions: If this setting is set to ``true`` , AWS DMS saves the transaction order for a change data capture (CDC) load on the Amazon S3 target specified by ```CdcPath`` <https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings-CdcPath>`_ . For more information, see `Capturing data changes (CDC) including transaction order on the S3 target <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.EndpointSettings.CdcPath>`_ . .. epigraph:: This setting is supported in AWS DMS versions 3.4.2 and later.
            :param rfc4180: For an S3 source, when this value is set to ``true`` or ``y`` , each leading double quotation mark has to be followed by an ending double quotation mark. This formatting complies with RFC 4180. When this value is set to ``false`` or ``n`` , string literals are copied to the target as is. In this case, a delimiter (row or column) signals the end of the field. Thus, you can't use a delimiter as part of the string, because it signals the end of the value. For an S3 target, an optional parameter used to set behavior to comply with RFC 4180 for data migrated to Amazon S3 using .csv file format only. When this value is set to ``true`` or ``y`` using Amazon S3 as a target, if the data has quotation marks or newline characters in it, AWS DMS encloses the entire column with an additional pair of double quotation marks ("). Every quotation mark within the data is repeated twice. The default value is ``true`` . Valid values include ``true`` , ``false`` , ``y`` , and ``n`` .
            :param row_group_length: The number of rows in a row group. A smaller row group size provides faster reads. But as the number of row groups grows, the slower writes become. This parameter defaults to 10,000 rows. This number is used for .parquet file format only. If you choose a value larger than the maximum, ``RowGroupLength`` is set to the max row group length in bytes (64 * 1024 * 1024).
            :param server_side_encryption_kms_key_id: If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide the AWS KMS key ID. The key that you use needs an attached policy that enables IAM user permissions and allows use of the key. Here is a CLI example: ``aws dms create-endpoint --endpoint-identifier *value* --endpoint-type target --engine-name s3 --s3-settings ServiceAccessRoleArn= *value* ,BucketFolder= *value* ,BucketName= *value* ,EncryptionMode=SSE_KMS,ServerSideEncryptionKmsKeyId= *value*``
            :param service_access_role_arn: A required parameter that specifies the Amazon Resource Name (ARN) used by the service to access the IAM role. The role must allow the ``iam:PassRole`` action. It enables AWS DMS to read and write objects from an S3 bucket.
            :param timestamp_column_name: A value that when nonblank causes AWS DMS to add a column with timestamp information to the endpoint data for an Amazon S3 target. .. epigraph:: AWS DMS supports the ``TimestampColumnName`` parameter in versions 3.1.4 and later. AWS DMS includes an additional ``STRING`` column in the .csv or .parquet object files of your migrated data when you set ``TimestampColumnName`` to a nonblank value. For a full load, each row of this timestamp column contains a timestamp for when the data was transferred from the source to the target by DMS. For a change data capture (CDC) load, each row of the timestamp column contains the timestamp for the commit of that row in the source database. The string format for this timestamp column value is ``yyyy-MM-dd HH:mm:ss.SSSSSS`` . By default, the precision of this value is in microseconds. For a CDC load, the rounding of the precision depends on the commit timestamp supported by DMS for the source database. When the ``AddColumnName`` parameter is set to ``true`` , DMS also includes a name for the timestamp column that you set with ``TimestampColumnName`` .
            :param use_csv_no_sup_value: This setting applies if the S3 output files during a change data capture (CDC) load are written in .csv format. If this setting is set to ``true`` for columns not included in the supplemental log, AWS DMS uses the value specified by ```CsvNoSupValue`` <https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings-CsvNoSupValue>`_ . If this setting isn't set or is set to ``false`` , AWS DMS uses the null value for these columns. .. epigraph:: This setting is supported in AWS DMS versions 3.4.1 and later.
            :param use_task_start_time_for_full_load_timestamp: When set to true, this parameter uses the task start time as the timestamp column value instead of the time data is written to target. For full load, when ``useTaskStartTimeForFullLoadTimestamp`` is set to ``true`` , each row of the timestamp column contains the task start time. For CDC loads, each row of the timestamp column contains the transaction commit time. When ``useTaskStartTimeForFullLoadTimestamp`` is set to ``false`` , the full load timestamp in the timestamp column increments with the time data arrives at the target.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dms as dms
                
                s3_settings_property = dms.CfnEndpoint.S3SettingsProperty(
                    add_column_name=False,
                    bucket_folder="bucketFolder",
                    bucket_name="bucketName",
                    canned_acl_for_objects="cannedAclForObjects",
                    cdc_inserts_and_updates=False,
                    cdc_inserts_only=False,
                    cdc_max_batch_interval=123,
                    cdc_min_file_size=123,
                    cdc_path="cdcPath",
                    compression_type="compressionType",
                    csv_delimiter="csvDelimiter",
                    csv_no_sup_value="csvNoSupValue",
                    csv_null_value="csvNullValue",
                    csv_row_delimiter="csvRowDelimiter",
                    data_format="dataFormat",
                    data_page_size=123,
                    date_partition_delimiter="datePartitionDelimiter",
                    date_partition_enabled=False,
                    date_partition_sequence="datePartitionSequence",
                    date_partition_timezone="datePartitionTimezone",
                    dict_page_size_limit=123,
                    enable_statistics=False,
                    encoding_type="encodingType",
                    encryption_mode="encryptionMode",
                    external_table_definition="externalTableDefinition",
                    ignore_header_rows=123,
                    include_op_for_full_load=False,
                    max_file_size=123,
                    parquet_timestamp_in_millisecond=False,
                    parquet_version="parquetVersion",
                    preserve_transactions=False,
                    rfc4180=False,
                    row_group_length=123,
                    server_side_encryption_kms_key_id="serverSideEncryptionKmsKeyId",
                    service_access_role_arn="serviceAccessRoleArn",
                    timestamp_column_name="timestampColumnName",
                    use_csv_no_sup_value=False,
                    use_task_start_time_for_full_load_timestamp=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dce05f410d1325b0f2dfd514c502c320539e35971e8d2d9efc2220a7eb138441)
                check_type(argname="argument add_column_name", value=add_column_name, expected_type=type_hints["add_column_name"])
                check_type(argname="argument bucket_folder", value=bucket_folder, expected_type=type_hints["bucket_folder"])
                check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
                check_type(argname="argument canned_acl_for_objects", value=canned_acl_for_objects, expected_type=type_hints["canned_acl_for_objects"])
                check_type(argname="argument cdc_inserts_and_updates", value=cdc_inserts_and_updates, expected_type=type_hints["cdc_inserts_and_updates"])
                check_type(argname="argument cdc_inserts_only", value=cdc_inserts_only, expected_type=type_hints["cdc_inserts_only"])
                check_type(argname="argument cdc_max_batch_interval", value=cdc_max_batch_interval, expected_type=type_hints["cdc_max_batch_interval"])
                check_type(argname="argument cdc_min_file_size", value=cdc_min_file_size, expected_type=type_hints["cdc_min_file_size"])
                check_type(argname="argument cdc_path", value=cdc_path, expected_type=type_hints["cdc_path"])
                check_type(argname="argument compression_type", value=compression_type, expected_type=type_hints["compression_type"])
                check_type(argname="argument csv_delimiter", value=csv_delimiter, expected_type=type_hints["csv_delimiter"])
                check_type(argname="argument csv_no_sup_value", value=csv_no_sup_value, expected_type=type_hints["csv_no_sup_value"])
                check_type(argname="argument csv_null_value", value=csv_null_value, expected_type=type_hints["csv_null_value"])
                check_type(argname="argument csv_row_delimiter", value=csv_row_delimiter, expected_type=type_hints["csv_row_delimiter"])
                check_type(argname="argument data_format", value=data_format, expected_type=type_hints["data_format"])
                check_type(argname="argument data_page_size", value=data_page_size, expected_type=type_hints["data_page_size"])
                check_type(argname="argument date_partition_delimiter", value=date_partition_delimiter, expected_type=type_hints["date_partition_delimiter"])
                check_type(argname="argument date_partition_enabled", value=date_partition_enabled, expected_type=type_hints["date_partition_enabled"])
                check_type(argname="argument date_partition_sequence", value=date_partition_sequence, expected_type=type_hints["date_partition_sequence"])
                check_type(argname="argument date_partition_timezone", value=date_partition_timezone, expected_type=type_hints["date_partition_timezone"])
                check_type(argname="argument dict_page_size_limit", value=dict_page_size_limit, expected_type=type_hints["dict_page_size_limit"])
                check_type(argname="argument enable_statistics", value=enable_statistics, expected_type=type_hints["enable_statistics"])
                check_type(argname="argument encoding_type", value=encoding_type, expected_type=type_hints["encoding_type"])
                check_type(argname="argument encryption_mode", value=encryption_mode, expected_type=type_hints["encryption_mode"])
                check_type(argname="argument external_table_definition", value=external_table_definition, expected_type=type_hints["external_table_definition"])
                check_type(argname="argument ignore_header_rows", value=ignore_header_rows, expected_type=type_hints["ignore_header_rows"])
                check_type(argname="argument include_op_for_full_load", value=include_op_for_full_load, expected_type=type_hints["include_op_for_full_load"])
                check_type(argname="argument max_file_size", value=max_file_size, expected_type=type_hints["max_file_size"])
                check_type(argname="argument parquet_timestamp_in_millisecond", value=parquet_timestamp_in_millisecond, expected_type=type_hints["parquet_timestamp_in_millisecond"])
                check_type(argname="argument parquet_version", value=parquet_version, expected_type=type_hints["parquet_version"])
                check_type(argname="argument preserve_transactions", value=preserve_transactions, expected_type=type_hints["preserve_transactions"])
                check_type(argname="argument rfc4180", value=rfc4180, expected_type=type_hints["rfc4180"])
                check_type(argname="argument row_group_length", value=row_group_length, expected_type=type_hints["row_group_length"])
                check_type(argname="argument server_side_encryption_kms_key_id", value=server_side_encryption_kms_key_id, expected_type=type_hints["server_side_encryption_kms_key_id"])
                check_type(argname="argument service_access_role_arn", value=service_access_role_arn, expected_type=type_hints["service_access_role_arn"])
                check_type(argname="argument timestamp_column_name", value=timestamp_column_name, expected_type=type_hints["timestamp_column_name"])
                check_type(argname="argument use_csv_no_sup_value", value=use_csv_no_sup_value, expected_type=type_hints["use_csv_no_sup_value"])
                check_type(argname="argument use_task_start_time_for_full_load_timestamp", value=use_task_start_time_for_full_load_timestamp, expected_type=type_hints["use_task_start_time_for_full_load_timestamp"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if add_column_name is not None:
                self._values["add_column_name"] = add_column_name
            if bucket_folder is not None:
                self._values["bucket_folder"] = bucket_folder
            if bucket_name is not None:
                self._values["bucket_name"] = bucket_name
            if canned_acl_for_objects is not None:
                self._values["canned_acl_for_objects"] = canned_acl_for_objects
            if cdc_inserts_and_updates is not None:
                self._values["cdc_inserts_and_updates"] = cdc_inserts_and_updates
            if cdc_inserts_only is not None:
                self._values["cdc_inserts_only"] = cdc_inserts_only
            if cdc_max_batch_interval is not None:
                self._values["cdc_max_batch_interval"] = cdc_max_batch_interval
            if cdc_min_file_size is not None:
                self._values["cdc_min_file_size"] = cdc_min_file_size
            if cdc_path is not None:
                self._values["cdc_path"] = cdc_path
            if compression_type is not None:
                self._values["compression_type"] = compression_type
            if csv_delimiter is not None:
                self._values["csv_delimiter"] = csv_delimiter
            if csv_no_sup_value is not None:
                self._values["csv_no_sup_value"] = csv_no_sup_value
            if csv_null_value is not None:
                self._values["csv_null_value"] = csv_null_value
            if csv_row_delimiter is not None:
                self._values["csv_row_delimiter"] = csv_row_delimiter
            if data_format is not None:
                self._values["data_format"] = data_format
            if data_page_size is not None:
                self._values["data_page_size"] = data_page_size
            if date_partition_delimiter is not None:
                self._values["date_partition_delimiter"] = date_partition_delimiter
            if date_partition_enabled is not None:
                self._values["date_partition_enabled"] = date_partition_enabled
            if date_partition_sequence is not None:
                self._values["date_partition_sequence"] = date_partition_sequence
            if date_partition_timezone is not None:
                self._values["date_partition_timezone"] = date_partition_timezone
            if dict_page_size_limit is not None:
                self._values["dict_page_size_limit"] = dict_page_size_limit
            if enable_statistics is not None:
                self._values["enable_statistics"] = enable_statistics
            if encoding_type is not None:
                self._values["encoding_type"] = encoding_type
            if encryption_mode is not None:
                self._values["encryption_mode"] = encryption_mode
            if external_table_definition is not None:
                self._values["external_table_definition"] = external_table_definition
            if ignore_header_rows is not None:
                self._values["ignore_header_rows"] = ignore_header_rows
            if include_op_for_full_load is not None:
                self._values["include_op_for_full_load"] = include_op_for_full_load
            if max_file_size is not None:
                self._values["max_file_size"] = max_file_size
            if parquet_timestamp_in_millisecond is not None:
                self._values["parquet_timestamp_in_millisecond"] = parquet_timestamp_in_millisecond
            if parquet_version is not None:
                self._values["parquet_version"] = parquet_version
            if preserve_transactions is not None:
                self._values["preserve_transactions"] = preserve_transactions
            if rfc4180 is not None:
                self._values["rfc4180"] = rfc4180
            if row_group_length is not None:
                self._values["row_group_length"] = row_group_length
            if server_side_encryption_kms_key_id is not None:
                self._values["server_side_encryption_kms_key_id"] = server_side_encryption_kms_key_id
            if service_access_role_arn is not None:
                self._values["service_access_role_arn"] = service_access_role_arn
            if timestamp_column_name is not None:
                self._values["timestamp_column_name"] = timestamp_column_name
            if use_csv_no_sup_value is not None:
                self._values["use_csv_no_sup_value"] = use_csv_no_sup_value
            if use_task_start_time_for_full_load_timestamp is not None:
                self._values["use_task_start_time_for_full_load_timestamp"] = use_task_start_time_for_full_load_timestamp

        @builtins.property
        def add_column_name(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''An optional parameter that, when set to ``true`` or ``y`` , you can use to add column name information to the .csv output file.

            The default value is ``false`` . Valid values are ``true`` , ``false`` , ``y`` , and ``n`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-addcolumnname
            '''
            result = self._values.get("add_column_name")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def bucket_folder(self) -> typing.Optional[builtins.str]:
            '''An optional parameter to set a folder name in the S3 bucket.

            If provided, tables are created in the path ``*bucketFolder* / *schema_name* / *table_name* /`` . If this parameter isn't specified, the path used is ``*schema_name* / *table_name* /`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-bucketfolder
            '''
            result = self._values.get("bucket_folder")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def bucket_name(self) -> typing.Optional[builtins.str]:
            '''The name of the S3 bucket.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-bucketname
            '''
            result = self._values.get("bucket_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def canned_acl_for_objects(self) -> typing.Optional[builtins.str]:
            '''A value that enables AWS DMS to specify a predefined (canned) access control list (ACL) for objects created in an Amazon S3 bucket as .csv or .parquet files. For more information about Amazon S3 canned ACLs, see `Canned ACL <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`_ in the *Amazon S3 Developer Guide* .

            The default value is NONE. Valid values include NONE, PRIVATE, PUBLIC_READ, PUBLIC_READ_WRITE, AUTHENTICATED_READ, AWS_EXEC_READ, BUCKET_OWNER_READ, and BUCKET_OWNER_FULL_CONTROL.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-cannedaclforobjects
            '''
            result = self._values.get("canned_acl_for_objects")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def cdc_inserts_and_updates(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''A value that enables a change data capture (CDC) load to write INSERT and UPDATE operations to .csv or .parquet (columnar storage) output files. The default setting is ``false`` , but when ``CdcInsertsAndUpdates`` is set to ``true`` or ``y`` , only INSERTs and UPDATEs from the source database are migrated to the .csv or .parquet file.

            For .csv file format only, how these INSERTs and UPDATEs are recorded depends on the value of the ``IncludeOpForFullLoad`` parameter. If ``IncludeOpForFullLoad`` is set to ``true`` , the first field of every CDC record is set to either ``I`` or ``U`` to indicate INSERT and UPDATE operations at the source. But if ``IncludeOpForFullLoad`` is set to ``false`` , CDC records are written without an indication of INSERT or UPDATE operations at the source. For more information about how these settings work together, see `Indicating Source DB Operations in Migrated S3 Data <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`_ in the *AWS Database Migration Service User Guide* .
            .. epigraph::

               AWS DMS supports the use of the ``CdcInsertsAndUpdates`` parameter in versions 3.3.1 and later.

               ``CdcInsertsOnly`` and ``CdcInsertsAndUpdates`` can't both be set to ``true`` for the same endpoint. Set either ``CdcInsertsOnly`` or ``CdcInsertsAndUpdates`` to ``true`` for the same endpoint, but not both.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-cdcinsertsandupdates
            '''
            result = self._values.get("cdc_inserts_and_updates")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def cdc_inserts_only(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''A value that enables a change data capture (CDC) load to write only INSERT operations to .csv or columnar storage (.parquet) output files. By default (the ``false`` setting), the first field in a .csv or .parquet record contains the letter I (INSERT), U (UPDATE), or D (DELETE). These values indicate whether the row was inserted, updated, or deleted at the source database for a CDC load to the target.

            If ``CdcInsertsOnly`` is set to ``true`` or ``y`` , only INSERTs from the source database are migrated to the .csv or .parquet file. For .csv format only, how these INSERTs are recorded depends on the value of ``IncludeOpForFullLoad`` . If ``IncludeOpForFullLoad`` is set to ``true`` , the first field of every CDC record is set to I to indicate the INSERT operation at the source. If ``IncludeOpForFullLoad`` is set to ``false`` , every CDC record is written without a first field to indicate the INSERT operation at the source. For more information about how these settings work together, see `Indicating Source DB Operations in Migrated S3 Data <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`_ in the *AWS Database Migration Service User Guide* .
            .. epigraph::

               AWS DMS supports the interaction described preceding between the ``CdcInsertsOnly`` and ``IncludeOpForFullLoad`` parameters in versions 3.1.4 and later.

               ``CdcInsertsOnly`` and ``CdcInsertsAndUpdates`` can't both be set to ``true`` for the same endpoint. Set either ``CdcInsertsOnly`` or ``CdcInsertsAndUpdates`` to ``true`` for the same endpoint, but not both.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-cdcinsertsonly
            '''
            result = self._values.get("cdc_inserts_only")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def cdc_max_batch_interval(self) -> typing.Optional[jsii.Number]:
            '''Maximum length of the interval, defined in seconds, after which to output a file to Amazon S3.

            When ``CdcMaxBatchInterval`` and ``CdcMinFileSize`` are both specified, the file write is triggered by whichever parameter condition is met first within an AWS DMS CloudFormation template.

            The default value is 60 seconds.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-cdcmaxbatchinterval
            '''
            result = self._values.get("cdc_max_batch_interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def cdc_min_file_size(self) -> typing.Optional[jsii.Number]:
            '''Minimum file size, defined in kilobytes, to reach for a file output to Amazon S3.

            When ``CdcMinFileSize`` and ``CdcMaxBatchInterval`` are both specified, the file write is triggered by whichever parameter condition is met first within an AWS DMS CloudFormation template.

            The default value is 32 MB.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-cdcminfilesize
            '''
            result = self._values.get("cdc_min_file_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def cdc_path(self) -> typing.Optional[builtins.str]:
            '''Specifies the folder path of CDC files.

            For an S3 source, this setting is required if a task captures change data; otherwise, it's optional. If ``CdcPath`` is set, AWS DMS reads CDC files from this path and replicates the data changes to the target endpoint. For an S3 target if you set ```PreserveTransactions`` <https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings-PreserveTransactions>`_ to ``true`` , AWS DMS verifies that you have set this parameter to a folder path on your S3 target where AWS DMS can save the transaction order for the CDC load. AWS DMS creates this CDC folder path in either your S3 target working directory or the S3 target location specified by ```BucketFolder`` <https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings-BucketFolder>`_ and ```BucketName`` <https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings-BucketName>`_ .

            For example, if you specify ``CdcPath`` as ``MyChangedData`` , and you specify ``BucketName`` as ``MyTargetBucket`` but do not specify ``BucketFolder`` , AWS DMS creates the CDC folder path following: ``MyTargetBucket/MyChangedData`` .

            If you specify the same ``CdcPath`` , and you specify ``BucketName`` as ``MyTargetBucket`` and ``BucketFolder`` as ``MyTargetData`` , AWS DMS creates the CDC folder path following: ``MyTargetBucket/MyTargetData/MyChangedData`` .

            For more information on CDC including transaction order on an S3 target, see `Capturing data changes (CDC) including transaction order on the S3 target <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.EndpointSettings.CdcPath>`_ .
            .. epigraph::

               This setting is supported in AWS DMS versions 3.4.2 and later.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-cdcpath
            '''
            result = self._values.get("cdc_path")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def compression_type(self) -> typing.Optional[builtins.str]:
            '''An optional parameter.

            When set to GZIP it enables the service to compress the target files. To allow the service to write the target files uncompressed, either set this parameter to NONE (the default) or don't specify the parameter at all. This parameter applies to both .csv and .parquet file formats.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-compressiontype
            '''
            result = self._values.get("compression_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def csv_delimiter(self) -> typing.Optional[builtins.str]:
            '''The delimiter used to separate columns in the .csv file for both source and target. The default is a comma.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-csvdelimiter
            '''
            result = self._values.get("csv_delimiter")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def csv_no_sup_value(self) -> typing.Optional[builtins.str]:
            '''This setting only applies if your Amazon S3 output files during a change data capture (CDC) load are written in .csv format. If ```UseCsvNoSupValue`` <https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings-UseCsvNoSupValue>`_ is set to true, specify a string value that you want AWS DMS to use for all columns not included in the supplemental log. If you do not specify a string value, AWS DMS uses the null value for these columns regardless of the ``UseCsvNoSupValue`` setting.

            .. epigraph::

               This setting is supported in AWS DMS versions 3.4.1 and later.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-csvnosupvalue
            '''
            result = self._values.get("csv_no_sup_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def csv_null_value(self) -> typing.Optional[builtins.str]:
            '''An optional parameter that specifies how AWS DMS treats null values.

            While handling the null value, you can use this parameter to pass a user-defined string as null when writing to the target. For example, when target columns are not nullable, you can use this option to differentiate between the empty string value and the null value. So, if you set this parameter value to the empty string ("" or ''), AWS DMS treats the empty string as the null value instead of ``NULL`` .

            The default value is ``NULL`` . Valid values include any valid string.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-csvnullvalue
            '''
            result = self._values.get("csv_null_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def csv_row_delimiter(self) -> typing.Optional[builtins.str]:
            '''The delimiter used to separate rows in the .csv file for both source and target.

            The default is a carriage return ( ``\\n`` ).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-csvrowdelimiter
            '''
            result = self._values.get("csv_row_delimiter")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def data_format(self) -> typing.Optional[builtins.str]:
            '''The format of the data that you want to use for output. You can choose one of the following:.

            - ``csv`` : This is a row-based file format with comma-separated values (.csv).
            - ``parquet`` : Apache Parquet (.parquet) is a columnar storage file format that features efficient compression and provides faster query response.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-dataformat
            '''
            result = self._values.get("data_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def data_page_size(self) -> typing.Optional[jsii.Number]:
            '''The size of one data page in bytes.

            This parameter defaults to 1024 * 1024 bytes (1 MiB). This number is used for .parquet file format only.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-datapagesize
            '''
            result = self._values.get("data_page_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def date_partition_delimiter(self) -> typing.Optional[builtins.str]:
            '''Specifies a date separating delimiter to use during folder partitioning.

            The default value is ``SLASH`` . Use this parameter when ``DatePartitionedEnabled`` is set to ``true`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-datepartitiondelimiter
            '''
            result = self._values.get("date_partition_delimiter")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def date_partition_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''When set to ``true`` , this parameter partitions S3 bucket folders based on transaction commit dates.

            The default value is ``false`` . For more information about date-based folder partitioning, see `Using date-based folder partitioning <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.DatePartitioning>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-datepartitionenabled
            '''
            result = self._values.get("date_partition_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def date_partition_sequence(self) -> typing.Optional[builtins.str]:
            '''Identifies the sequence of the date format to use during folder partitioning.

            The default value is ``YYYYMMDD`` . Use this parameter when ``DatePartitionedEnabled`` is set to ``true`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-datepartitionsequence
            '''
            result = self._values.get("date_partition_sequence")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def date_partition_timezone(self) -> typing.Optional[builtins.str]:
            '''When creating an S3 target endpoint, set ``DatePartitionTimezone`` to convert the current UTC time into a specified time zone.

            The conversion occurs when a date partition folder is created and a change data capture (CDC) file name is generated. The time zone format is Area/Location. Use this parameter when ``DatePartitionedEnabled`` is set to ``true`` , as shown in the following example.

            ``s3-settings='{"DatePartitionEnabled": true, "DatePartitionSequence": "YYYYMMDDHH", "DatePartitionDelimiter": "SLASH", "DatePartitionTimezone":" *Asia/Seoul* ", "BucketName": "dms-nattarat-test"}'``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-datepartitiontimezone
            '''
            result = self._values.get("date_partition_timezone")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def dict_page_size_limit(self) -> typing.Optional[jsii.Number]:
            '''The maximum size of an encoded dictionary page of a column.

            If the dictionary page exceeds this, this column is stored using an encoding type of ``PLAIN`` . This parameter defaults to 1024 * 1024 bytes (1 MiB), the maximum size of a dictionary page before it reverts to ``PLAIN`` encoding. This size is used for .parquet file format only.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-dictpagesizelimit
            '''
            result = self._values.get("dict_page_size_limit")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def enable_statistics(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''A value that enables statistics for Parquet pages and row groups.

            Choose ``true`` to enable statistics, ``false`` to disable. Statistics include ``NULL`` , ``DISTINCT`` , ``MAX`` , and ``MIN`` values. This parameter defaults to ``true`` . This value is used for .parquet file format only.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-enablestatistics
            '''
            result = self._values.get("enable_statistics")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def encoding_type(self) -> typing.Optional[builtins.str]:
            '''The type of encoding that you're using:.

            - ``RLE_DICTIONARY`` uses a combination of bit-packing and run-length encoding to store repeated values more efficiently. This is the default.
            - ``PLAIN`` doesn't use encoding at all. Values are stored as they are.
            - ``PLAIN_DICTIONARY`` builds a dictionary of the values encountered in a given column. The dictionary is stored in a dictionary page for each column chunk.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-encodingtype
            '''
            result = self._values.get("encoding_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def encryption_mode(self) -> typing.Optional[builtins.str]:
            '''The type of server-side encryption that you want to use for your data.

            This encryption type is part of the endpoint settings or the extra connections attributes for Amazon S3. You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` .
            .. epigraph::

               For the ``ModifyEndpoint`` operation, you can change the existing value of the ``EncryptionMode`` parameter from ``SSE_KMS`` to ``SSE_S3`` . But you can’t change the existing value from ``SSE_S3`` to ``SSE_KMS`` .

            To use ``SSE_S3`` , you need an IAM role with permission to allow ``"arn:aws:s3:::dms-*"`` to use the following actions:

            - ``s3:CreateBucket``
            - ``s3:ListBucket``
            - ``s3:DeleteBucket``
            - ``s3:GetBucketLocation``
            - ``s3:GetObject``
            - ``s3:PutObject``
            - ``s3:DeleteObject``
            - ``s3:GetObjectVersion``
            - ``s3:GetBucketPolicy``
            - ``s3:PutBucketPolicy``
            - ``s3:DeleteBucketPolicy``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-encryptionmode
            '''
            result = self._values.get("encryption_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def external_table_definition(self) -> typing.Optional[builtins.str]:
            '''The external table definition.

            Conditional: If ``S3`` is used as a source then ``ExternalTableDefinition`` is required.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-externaltabledefinition
            '''
            result = self._values.get("external_table_definition")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ignore_header_rows(self) -> typing.Optional[jsii.Number]:
            '''When this value is set to 1, AWS DMS ignores the first row header in a .csv file. A value of 1 turns on the feature; a value of 0 turns off the feature.

            The default is 0.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-ignoreheaderrows
            '''
            result = self._values.get("ignore_header_rows")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def include_op_for_full_load(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''A value that enables a full load to write INSERT operations to the comma-separated value (.csv) output files only to indicate how the rows were added to the source database.

            .. epigraph::

               AWS DMS supports the ``IncludeOpForFullLoad`` parameter in versions 3.1.4 and later.

            For full load, records can only be inserted. By default (the ``false`` setting), no information is recorded in these output files for a full load to indicate that the rows were inserted at the source database. If ``IncludeOpForFullLoad`` is set to ``true`` or ``y`` , the INSERT is recorded as an I annotation in the first field of the .csv file. This allows the format of your target records from a full load to be consistent with the target records from a CDC load.
            .. epigraph::

               This setting works together with the ``CdcInsertsOnly`` and the ``CdcInsertsAndUpdates`` parameters for output to .csv files only. For more information about how these settings work together, see `Indicating Source DB Operations in Migrated S3 Data <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`_ in the *AWS Database Migration Service User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-includeopforfullload
            '''
            result = self._values.get("include_op_for_full_load")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def max_file_size(self) -> typing.Optional[jsii.Number]:
            '''A value that specifies the maximum size (in KB) of any .csv file to be created while migrating to an S3 target during full load.

            The default value is 1,048,576 KB (1 GB). Valid values include 1 to 1,048,576.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-maxfilesize
            '''
            result = self._values.get("max_file_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def parquet_timestamp_in_millisecond(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''A value that specifies the precision of any ``TIMESTAMP`` column values that are written to an Amazon S3 object file in .parquet format.

            .. epigraph::

               AWS DMS supports the ``ParquetTimestampInMillisecond`` parameter in versions 3.1.4 and later.

            When ``ParquetTimestampInMillisecond`` is set to ``true`` or ``y`` , AWS DMS writes all ``TIMESTAMP`` columns in a .parquet formatted file with millisecond precision. Otherwise, DMS writes them with microsecond precision.

            Currently, Amazon Athena and AWS Glue can handle only millisecond precision for ``TIMESTAMP`` values. Set this parameter to ``true`` for S3 endpoint object files that are .parquet formatted only if you plan to query or process the data with Athena or AWS Glue .
            .. epigraph::

               AWS DMS writes any ``TIMESTAMP`` column values written to an S3 file in .csv format with microsecond precision.

               Setting ``ParquetTimestampInMillisecond`` has no effect on the string format of the timestamp column value that is inserted by setting the ``TimestampColumnName`` parameter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-parquettimestampinmillisecond
            '''
            result = self._values.get("parquet_timestamp_in_millisecond")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def parquet_version(self) -> typing.Optional[builtins.str]:
            '''The version of the Apache Parquet format that you want to use: ``parquet_1_0`` (the default) or ``parquet_2_0`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-parquetversion
            '''
            result = self._values.get("parquet_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def preserve_transactions(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''If this setting is set to ``true`` , AWS DMS saves the transaction order for a change data capture (CDC) load on the Amazon S3 target specified by ```CdcPath`` <https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings-CdcPath>`_ . For more information, see `Capturing data changes (CDC) including transaction order on the S3 target <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.EndpointSettings.CdcPath>`_ .

            .. epigraph::

               This setting is supported in AWS DMS versions 3.4.2 and later.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-preservetransactions
            '''
            result = self._values.get("preserve_transactions")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def rfc4180(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''For an S3 source, when this value is set to ``true`` or ``y`` , each leading double quotation mark has to be followed by an ending double quotation mark.

            This formatting complies with RFC 4180. When this value is set to ``false`` or ``n`` , string literals are copied to the target as is. In this case, a delimiter (row or column) signals the end of the field. Thus, you can't use a delimiter as part of the string, because it signals the end of the value.

            For an S3 target, an optional parameter used to set behavior to comply with RFC 4180 for data migrated to Amazon S3 using .csv file format only. When this value is set to ``true`` or ``y`` using Amazon S3 as a target, if the data has quotation marks or newline characters in it, AWS DMS encloses the entire column with an additional pair of double quotation marks ("). Every quotation mark within the data is repeated twice.

            The default value is ``true`` . Valid values include ``true`` , ``false`` , ``y`` , and ``n`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-rfc4180
            '''
            result = self._values.get("rfc4180")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def row_group_length(self) -> typing.Optional[jsii.Number]:
            '''The number of rows in a row group.

            A smaller row group size provides faster reads. But as the number of row groups grows, the slower writes become. This parameter defaults to 10,000 rows. This number is used for .parquet file format only.

            If you choose a value larger than the maximum, ``RowGroupLength`` is set to the max row group length in bytes (64 * 1024 * 1024).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-rowgrouplength
            '''
            result = self._values.get("row_group_length")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def server_side_encryption_kms_key_id(self) -> typing.Optional[builtins.str]:
            '''If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide the AWS KMS key ID.

            The key that you use needs an attached policy that enables IAM user permissions and allows use of the key.

            Here is a CLI example: ``aws dms create-endpoint --endpoint-identifier *value* --endpoint-type target --engine-name s3 --s3-settings ServiceAccessRoleArn= *value* ,BucketFolder= *value* ,BucketName= *value* ,EncryptionMode=SSE_KMS,ServerSideEncryptionKmsKeyId= *value*``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-serversideencryptionkmskeyid
            '''
            result = self._values.get("server_side_encryption_kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def service_access_role_arn(self) -> typing.Optional[builtins.str]:
            '''A required parameter that specifies the Amazon Resource Name (ARN) used by the service to access the IAM role.

            The role must allow the ``iam:PassRole`` action. It enables AWS DMS to read and write objects from an S3 bucket.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-serviceaccessrolearn
            '''
            result = self._values.get("service_access_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def timestamp_column_name(self) -> typing.Optional[builtins.str]:
            '''A value that when nonblank causes AWS DMS to add a column with timestamp information to the endpoint data for an Amazon S3 target.

            .. epigraph::

               AWS DMS supports the ``TimestampColumnName`` parameter in versions 3.1.4 and later.

            AWS DMS includes an additional ``STRING`` column in the .csv or .parquet object files of your migrated data when you set ``TimestampColumnName`` to a nonblank value.

            For a full load, each row of this timestamp column contains a timestamp for when the data was transferred from the source to the target by DMS.

            For a change data capture (CDC) load, each row of the timestamp column contains the timestamp for the commit of that row in the source database.

            The string format for this timestamp column value is ``yyyy-MM-dd HH:mm:ss.SSSSSS`` . By default, the precision of this value is in microseconds. For a CDC load, the rounding of the precision depends on the commit timestamp supported by DMS for the source database.

            When the ``AddColumnName`` parameter is set to ``true`` , DMS also includes a name for the timestamp column that you set with ``TimestampColumnName`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-timestampcolumnname
            '''
            result = self._values.get("timestamp_column_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def use_csv_no_sup_value(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''This setting applies if the S3 output files during a change data capture (CDC) load are written in .csv format. If this setting is set to ``true`` for columns not included in the supplemental log, AWS DMS uses the value specified by ```CsvNoSupValue`` <https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings-CsvNoSupValue>`_ . If this setting isn't set or is set to ``false`` , AWS DMS uses the null value for these columns.

            .. epigraph::

               This setting is supported in AWS DMS versions 3.4.1 and later.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-usecsvnosupvalue
            '''
            result = self._values.get("use_csv_no_sup_value")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def use_task_start_time_for_full_load_timestamp(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''When set to true, this parameter uses the task start time as the timestamp column value instead of the time data is written to target.

            For full load, when ``useTaskStartTimeForFullLoadTimestamp`` is set to ``true`` , each row of the timestamp column contains the task start time. For CDC loads, each row of the timestamp column contains the transaction commit time.

            When ``useTaskStartTimeForFullLoadTimestamp`` is set to ``false`` , the full load timestamp in the timestamp column increments with the time data arrives at the target.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-usetaskstarttimeforfullloadtimestamp
            '''
            result = self._values.get("use_task_start_time_for_full_load_timestamp")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3SettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_dms.CfnEndpoint.SybaseSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "secrets_manager_access_role_arn": "secretsManagerAccessRoleArn",
            "secrets_manager_secret_id": "secretsManagerSecretId",
        },
    )
    class SybaseSettingsProperty:
        def __init__(
            self,
            *,
            secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
            secrets_manager_secret_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides information that defines a SAP ASE endpoint.

            This information includes the output format of records applied to the endpoint and details of transaction and control table data information. For information about other available settings, see `Extra connection attributes when using SAP ASE as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SAP.html#CHAP_Source.SAP.ConnectionAttrib>`_ and `Extra connection attributes when using SAP ASE as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.SAP.html#CHAP_Target.SAP.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

            :param secrets_manager_access_role_arn: The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in ``SecretsManagerSecret`` . The role must allow the ``iam:PassRole`` action. ``SecretsManagerSecret`` has the value of the AWS Secrets Manager secret that allows access to the SAP ASE endpoint. .. epigraph:: You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerSecretId`` . Or you can specify clear-text values for ``UserName`` , ``Password`` , ``ServerName`` , and ``Port`` . You can't specify both. For more information on creating this ``SecretsManagerSecret`` , the corresponding ``SecretsManagerAccessRoleArn`` , and the ``SecretsManagerSecretId`` that is required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .
            :param secrets_manager_secret_id: The full ARN, partial ARN, or display name of the ``SecretsManagerSecret`` that contains the SAP SAE endpoint connection details.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-sybasesettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_dms as dms
                
                sybase_settings_property = dms.CfnEndpoint.SybaseSettingsProperty(
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_secret_id="secretsManagerSecretId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__37f8ecccccfa862918c84ab832ab1b008e37457d1dd134f815173627c73c7baf)
                check_type(argname="argument secrets_manager_access_role_arn", value=secrets_manager_access_role_arn, expected_type=type_hints["secrets_manager_access_role_arn"])
                check_type(argname="argument secrets_manager_secret_id", value=secrets_manager_secret_id, expected_type=type_hints["secrets_manager_secret_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if secrets_manager_access_role_arn is not None:
                self._values["secrets_manager_access_role_arn"] = secrets_manager_access_role_arn
            if secrets_manager_secret_id is not None:
                self._values["secrets_manager_secret_id"] = secrets_manager_secret_id

        @builtins.property
        def secrets_manager_access_role_arn(self) -> typing.Optional[builtins.str]:
            '''The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in ``SecretsManagerSecret`` .

            The role must allow the ``iam:PassRole`` action. ``SecretsManagerSecret`` has the value of the AWS Secrets Manager secret that allows access to the SAP ASE endpoint.
            .. epigraph::

               You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerSecretId`` . Or you can specify clear-text values for ``UserName`` , ``Password`` , ``ServerName`` , and ``Port`` . You can't specify both.

               For more information on creating this ``SecretsManagerSecret`` , the corresponding ``SecretsManagerAccessRoleArn`` , and the ``SecretsManagerSecretId`` that is required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-sybasesettings.html#cfn-dms-endpoint-sybasesettings-secretsmanageraccessrolearn
            '''
            result = self._values.get("secrets_manager_access_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secrets_manager_secret_id(self) -> typing.Optional[builtins.str]:
            '''The full ARN, partial ARN, or display name of the ``SecretsManagerSecret`` that contains the SAP SAE endpoint connection details.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-sybasesettings.html#cfn-dms-endpoint-sybasesettings-secretsmanagersecretid
            '''
            result = self._values.get("secrets_manager_secret_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SybaseSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_dms.CfnEndpointProps",
    jsii_struct_bases=[],
    name_mapping={
        "endpoint_type": "endpointType",
        "engine_name": "engineName",
        "certificate_arn": "certificateArn",
        "database_name": "databaseName",
        "doc_db_settings": "docDbSettings",
        "dynamo_db_settings": "dynamoDbSettings",
        "elasticsearch_settings": "elasticsearchSettings",
        "endpoint_identifier": "endpointIdentifier",
        "extra_connection_attributes": "extraConnectionAttributes",
        "gcp_my_sql_settings": "gcpMySqlSettings",
        "ibm_db2_settings": "ibmDb2Settings",
        "kafka_settings": "kafkaSettings",
        "kinesis_settings": "kinesisSettings",
        "kms_key_id": "kmsKeyId",
        "microsoft_sql_server_settings": "microsoftSqlServerSettings",
        "mongo_db_settings": "mongoDbSettings",
        "my_sql_settings": "mySqlSettings",
        "neptune_settings": "neptuneSettings",
        "oracle_settings": "oracleSettings",
        "password": "password",
        "port": "port",
        "postgre_sql_settings": "postgreSqlSettings",
        "redis_settings": "redisSettings",
        "redshift_settings": "redshiftSettings",
        "resource_identifier": "resourceIdentifier",
        "s3_settings": "s3Settings",
        "server_name": "serverName",
        "ssl_mode": "sslMode",
        "sybase_settings": "sybaseSettings",
        "tags": "tags",
        "username": "username",
    },
)
class CfnEndpointProps:
    def __init__(
        self,
        *,
        endpoint_type: builtins.str,
        engine_name: builtins.str,
        certificate_arn: typing.Optional[builtins.str] = None,
        database_name: typing.Optional[builtins.str] = None,
        doc_db_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.DocDbSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        dynamo_db_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.DynamoDbSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        elasticsearch_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.ElasticsearchSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        endpoint_identifier: typing.Optional[builtins.str] = None,
        extra_connection_attributes: typing.Optional[builtins.str] = None,
        gcp_my_sql_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.GcpMySQLSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        ibm_db2_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.IbmDb2SettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        kafka_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.KafkaSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        kinesis_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.KinesisSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        microsoft_sql_server_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.MicrosoftSqlServerSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        mongo_db_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.MongoDbSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        my_sql_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.MySqlSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        neptune_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.NeptuneSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        oracle_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.OracleSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        password: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        postgre_sql_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.PostgreSqlSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        redis_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.RedisSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        redshift_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.RedshiftSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        resource_identifier: typing.Optional[builtins.str] = None,
        s3_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.S3SettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        server_name: typing.Optional[builtins.str] = None,
        ssl_mode: typing.Optional[builtins.str] = None,
        sybase_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.SybaseSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnEndpoint``.

        :param endpoint_type: The type of endpoint. Valid values are ``source`` and ``target`` .
        :param engine_name: The type of engine for the endpoint, depending on the ``EndpointType`` value. *Valid values* : ``mysql`` | ``oracle`` | ``postgres`` | ``mariadb`` | ``aurora`` | ``aurora-postgresql`` | ``opensearch`` | ``redshift`` | ``s3`` | ``db2`` | ``azuredb`` | ``sybase`` | ``dynamodb`` | ``mongodb`` | ``kinesis`` | ``kafka`` | ``elasticsearch`` | ``docdb`` | ``sqlserver`` | ``neptune``
        :param certificate_arn: The Amazon Resource Name (ARN) for the certificate.
        :param database_name: The name of the endpoint database. For a MySQL source or target endpoint, don't specify ``DatabaseName`` . To migrate to a specific database, use this setting and ``targetDbType`` .
        :param doc_db_settings: Settings in JSON format for the source and target DocumentDB endpoint. For more information about other available settings, see `Using extra connections attributes with Amazon DocumentDB as a source <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.DocumentDB.html#CHAP_Source.DocumentDB.ECAs>`_ and `Using Amazon DocumentDB as a target for AWS Database Migration Service <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.DocumentDB.html>`_ in the *AWS Database Migration Service User Guide* .
        :param dynamo_db_settings: Settings in JSON format for the target Amazon DynamoDB endpoint. For information about other available settings, see `Using object mapping to migrate data to DynamoDB <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.DynamoDB.html#CHAP_Target.DynamoDB.ObjectMapping>`_ in the *AWS Database Migration Service User Guide* .
        :param elasticsearch_settings: Settings in JSON format for the target OpenSearch endpoint. For more information about the available settings, see `Extra connection attributes when using OpenSearch as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Elasticsearch.html#CHAP_Target.Elasticsearch.Configuration>`_ in the *AWS Database Migration Service User Guide* .
        :param endpoint_identifier: The database endpoint identifier. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen, or contain two consecutive hyphens.
        :param extra_connection_attributes: Additional attributes associated with the connection. Each attribute is specified as a name-value pair associated by an equal sign (=). Multiple attributes are separated by a semicolon (;) with no additional white space. For information on the attributes available for connecting your source or target endpoint, see `Working with AWS DMS Endpoints <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Endpoints.html>`_ in the *AWS Database Migration Service User Guide* .
        :param gcp_my_sql_settings: Settings in JSON format for the source GCP MySQL endpoint. These settings are much the same as the settings for any MySQL-compatible endpoint. For more information, see `Extra connection attributes when using MySQL as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html#CHAP_Source.MySQL.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .
        :param ibm_db2_settings: Settings in JSON format for the source IBM Db2 LUW endpoint. For information about other available settings, see `Extra connection attributes when using Db2 LUW as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.DB2.html#CHAP_Source.DB2.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .
        :param kafka_settings: Settings in JSON format for the target Apache Kafka endpoint. For more information about other available settings, see `Using object mapping to migrate data to a Kafka topic <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kafka.html#CHAP_Target.Kafka.ObjectMapping>`_ in the *AWS Database Migration Service User Guide* .
        :param kinesis_settings: Settings in JSON format for the target endpoint for Amazon Kinesis Data Streams. For more information about other available settings, see `Using object mapping to migrate data to a Kinesis data stream <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kinesis.html#CHAP_Target.Kinesis.ObjectMapping>`_ in the *AWS Database Migration Service User Guide* .
        :param kms_key_id: An AWS KMS key identifier that is used to encrypt the connection parameters for the endpoint. If you don't specify a value for the ``KmsKeyId`` parameter, AWS DMS uses your default encryption key. AWS KMS creates the default encryption key for your AWS account . Your AWS account has a different default encryption key for each AWS Region .
        :param microsoft_sql_server_settings: Settings in JSON format for the source and target Microsoft SQL Server endpoint. For information about other available settings, see `Extra connection attributes when using SQL Server as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SQLServer.html#CHAP_Source.SQLServer.ConnectionAttrib>`_ and `Extra connection attributes when using SQL Server as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.SQLServer.html#CHAP_Target.SQLServer.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .
        :param mongo_db_settings: Settings in JSON format for the source MongoDB endpoint. For more information about the available settings, see `Using MongoDB as a target for AWS Database Migration Service <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MongoDB.html#CHAP_Source.MongoDB.Configuration>`_ in the *AWS Database Migration Service User Guide* .
        :param my_sql_settings: Settings in JSON format for the source and target MySQL endpoint. For information about other available settings, see `Extra connection attributes when using MySQL as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html#CHAP_Source.MySQL.ConnectionAttrib>`_ and `Extra connection attributes when using a MySQL-compatible database as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.MySQL.html#CHAP_Target.MySQL.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .
        :param neptune_settings: Settings in JSON format for the target Amazon Neptune endpoint. For more information about the available settings, see `Specifying endpoint settings for Amazon Neptune as a target <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Neptune.html#CHAP_Target.Neptune.EndpointSettings>`_ in the *AWS Database Migration Service User Guide* .
        :param oracle_settings: Settings in JSON format for the source and target Oracle endpoint. For information about other available settings, see `Extra connection attributes when using Oracle as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.ConnectionAttrib>`_ and `Extra connection attributes when using Oracle as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Oracle.html#CHAP_Target.Oracle.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .
        :param password: The password to be used to log in to the endpoint database.
        :param port: The port used by the endpoint database.
        :param postgre_sql_settings: Settings in JSON format for the source and target PostgreSQL endpoint. For information about other available settings, see `Extra connection attributes when using PostgreSQL as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.PostgreSQL.html#CHAP_Source.PostgreSQL.ConnectionAttrib>`_ and `Extra connection attributes when using PostgreSQL as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.PostgreSQL.html#CHAP_Target.PostgreSQL.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .
        :param redis_settings: Settings in JSON format for the target Redis endpoint. For information about other available settings, see `Specifying endpoint settings for Redis as a target <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Redis.html#CHAP_Target.Redis.EndpointSettings>`_ in the *AWS Database Migration Service User Guide* .
        :param redshift_settings: Settings in JSON format for the Amazon Redshift endpoint. For more information about other available settings, see `Extra connection attributes when using Amazon Redshift as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Redshift.html#CHAP_Target.Redshift.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .
        :param resource_identifier: A display name for the resource identifier at the end of the ``EndpointArn`` response parameter that is returned in the created ``Endpoint`` object. The value for this parameter can have up to 31 characters. It can contain only ASCII letters, digits, and hyphen ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter, such as ``Example-App-ARN1`` . For example, this value might result in the ``EndpointArn`` value ``arn:aws:dms:eu-west-1:012345678901:rep:Example-App-ARN1`` . If you don't specify a ``ResourceIdentifier`` value, AWS DMS generates a default identifier value for the end of ``EndpointArn`` .
        :param s3_settings: Settings in JSON format for the source and target Amazon S3 endpoint. For more information about other available settings, see `Extra connection attributes when using Amazon S3 as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.S3.html#CHAP_Source.S3.Configuring>`_ and `Extra connection attributes when using Amazon S3 as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring>`_ in the *AWS Database Migration Service User Guide* .
        :param server_name: The name of the server where the endpoint database resides.
        :param ssl_mode: The Secure Sockets Layer (SSL) mode to use for the SSL connection. The default is ``none`` . .. epigraph:: When ``engine_name`` is set to S3, the only allowed value is ``none`` .
        :param sybase_settings: Settings in JSON format for the source and target SAP ASE endpoint. For information about other available settings, see `Extra connection attributes when using SAP ASE as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SAP.html#CHAP_Source.SAP.ConnectionAttrib>`_ and `Extra connection attributes when using SAP ASE as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.SAP.html#CHAP_Target.SAP.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .
        :param tags: One or more tags to be assigned to the endpoint.
        :param username: The user name to be used to log in to the endpoint database.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_dms as dms
            
            cfn_endpoint_props = dms.CfnEndpointProps(
                endpoint_type="endpointType",
                engine_name="engineName",
            
                # the properties below are optional
                certificate_arn="certificateArn",
                database_name="databaseName",
                doc_db_settings=dms.CfnEndpoint.DocDbSettingsProperty(
                    docs_to_investigate=123,
                    extract_doc_id=False,
                    nesting_level="nestingLevel",
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_secret_id="secretsManagerSecretId"
                ),
                dynamo_db_settings=dms.CfnEndpoint.DynamoDbSettingsProperty(
                    service_access_role_arn="serviceAccessRoleArn"
                ),
                elasticsearch_settings=dms.CfnEndpoint.ElasticsearchSettingsProperty(
                    endpoint_uri="endpointUri",
                    error_retry_duration=123,
                    full_load_error_percentage=123,
                    service_access_role_arn="serviceAccessRoleArn"
                ),
                endpoint_identifier="endpointIdentifier",
                extra_connection_attributes="extraConnectionAttributes",
                gcp_my_sql_settings=dms.CfnEndpoint.GcpMySQLSettingsProperty(
                    after_connect_script="afterConnectScript",
                    clean_source_metadata_on_mismatch=False,
                    database_name="databaseName",
                    events_poll_interval=123,
                    max_file_size=123,
                    parallel_load_threads=123,
                    password="password",
                    port=123,
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_secret_id="secretsManagerSecretId",
                    server_name="serverName",
                    server_timezone="serverTimezone",
                    username="username"
                ),
                ibm_db2_settings=dms.CfnEndpoint.IbmDb2SettingsProperty(
                    current_lsn="currentLsn",
                    max_kBytes_per_read=123,
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_secret_id="secretsManagerSecretId",
                    set_data_capture_changes=False
                ),
                kafka_settings=dms.CfnEndpoint.KafkaSettingsProperty(
                    broker="broker",
                    include_control_details=False,
                    include_null_and_empty=False,
                    include_partition_value=False,
                    include_table_alter_operations=False,
                    include_transaction_details=False,
                    message_format="messageFormat",
                    message_max_bytes=123,
                    no_hex_prefix=False,
                    partition_include_schema_table=False,
                    sasl_password="saslPassword",
                    sasl_user_name="saslUserName",
                    security_protocol="securityProtocol",
                    ssl_ca_certificate_arn="sslCaCertificateArn",
                    ssl_client_certificate_arn="sslClientCertificateArn",
                    ssl_client_key_arn="sslClientKeyArn",
                    ssl_client_key_password="sslClientKeyPassword",
                    topic="topic"
                ),
                kinesis_settings=dms.CfnEndpoint.KinesisSettingsProperty(
                    include_control_details=False,
                    include_null_and_empty=False,
                    include_partition_value=False,
                    include_table_alter_operations=False,
                    include_transaction_details=False,
                    message_format="messageFormat",
                    no_hex_prefix=False,
                    partition_include_schema_table=False,
                    service_access_role_arn="serviceAccessRoleArn",
                    stream_arn="streamArn"
                ),
                kms_key_id="kmsKeyId",
                microsoft_sql_server_settings=dms.CfnEndpoint.MicrosoftSqlServerSettingsProperty(
                    bcp_packet_size=123,
                    control_tables_file_group="controlTablesFileGroup",
                    query_single_always_on_node=False,
                    read_backup_only=False,
                    safeguard_policy="safeguardPolicy",
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_secret_id="secretsManagerSecretId",
                    use_bcp_full_load=False,
                    use_third_party_backup_device=False
                ),
                mongo_db_settings=dms.CfnEndpoint.MongoDbSettingsProperty(
                    auth_mechanism="authMechanism",
                    auth_source="authSource",
                    auth_type="authType",
                    database_name="databaseName",
                    docs_to_investigate="docsToInvestigate",
                    extract_doc_id="extractDocId",
                    nesting_level="nestingLevel",
                    password="password",
                    port=123,
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_secret_id="secretsManagerSecretId",
                    server_name="serverName",
                    username="username"
                ),
                my_sql_settings=dms.CfnEndpoint.MySqlSettingsProperty(
                    after_connect_script="afterConnectScript",
                    clean_source_metadata_on_mismatch=False,
                    events_poll_interval=123,
                    max_file_size=123,
                    parallel_load_threads=123,
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_secret_id="secretsManagerSecretId",
                    server_timezone="serverTimezone",
                    target_db_type="targetDbType"
                ),
                neptune_settings=dms.CfnEndpoint.NeptuneSettingsProperty(
                    error_retry_duration=123,
                    iam_auth_enabled=False,
                    max_file_size=123,
                    max_retry_count=123,
                    s3_bucket_folder="s3BucketFolder",
                    s3_bucket_name="s3BucketName",
                    service_access_role_arn="serviceAccessRoleArn"
                ),
                oracle_settings=dms.CfnEndpoint.OracleSettingsProperty(
                    access_alternate_directly=False,
                    additional_archived_log_dest_id=123,
                    add_supplemental_logging=False,
                    allow_select_nested_tables=False,
                    archived_log_dest_id=123,
                    archived_logs_only=False,
                    asm_password="asmPassword",
                    asm_server="asmServer",
                    asm_user="asmUser",
                    char_length_semantics="charLengthSemantics",
                    direct_path_no_log=False,
                    direct_path_parallel_load=False,
                    enable_homogenous_tablespace=False,
                    extra_archived_log_dest_ids=[123],
                    fail_tasks_on_lob_truncation=False,
                    number_datatype_scale=123,
                    oracle_path_prefix="oraclePathPrefix",
                    parallel_asm_read_threads=123,
                    read_ahead_blocks=123,
                    read_table_space_name=False,
                    replace_path_prefix=False,
                    retry_interval=123,
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_oracle_asm_access_role_arn="secretsManagerOracleAsmAccessRoleArn",
                    secrets_manager_oracle_asm_secret_id="secretsManagerOracleAsmSecretId",
                    secrets_manager_secret_id="secretsManagerSecretId",
                    security_db_encryption="securityDbEncryption",
                    security_db_encryption_name="securityDbEncryptionName",
                    spatial_data_option_to_geo_json_function_name="spatialDataOptionToGeoJsonFunctionName",
                    standby_delay_time=123,
                    use_alternate_folder_for_online=False,
                    use_bFile=False,
                    use_direct_path_full_load=False,
                    use_logminer_reader=False,
                    use_path_prefix="usePathPrefix"
                ),
                password="password",
                port=123,
                postgre_sql_settings=dms.CfnEndpoint.PostgreSqlSettingsProperty(
                    after_connect_script="afterConnectScript",
                    capture_ddls=False,
                    ddl_artifacts_schema="ddlArtifactsSchema",
                    execute_timeout=123,
                    fail_tasks_on_lob_truncation=False,
                    heartbeat_enable=False,
                    heartbeat_frequency=123,
                    heartbeat_schema="heartbeatSchema",
                    max_file_size=123,
                    plugin_name="pluginName",
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_secret_id="secretsManagerSecretId",
                    slot_name="slotName"
                ),
                redis_settings=dms.CfnEndpoint.RedisSettingsProperty(
                    auth_password="authPassword",
                    auth_type="authType",
                    auth_user_name="authUserName",
                    port=123,
                    server_name="serverName",
                    ssl_ca_certificate_arn="sslCaCertificateArn",
                    ssl_security_protocol="sslSecurityProtocol"
                ),
                redshift_settings=dms.CfnEndpoint.RedshiftSettingsProperty(
                    accept_any_date=False,
                    after_connect_script="afterConnectScript",
                    bucket_folder="bucketFolder",
                    bucket_name="bucketName",
                    case_sensitive_names=False,
                    comp_update=False,
                    connection_timeout=123,
                    date_format="dateFormat",
                    empty_as_null=False,
                    encryption_mode="encryptionMode",
                    explicit_ids=False,
                    file_transfer_upload_streams=123,
                    load_timeout=123,
                    max_file_size=123,
                    remove_quotes=False,
                    replace_chars="replaceChars",
                    replace_invalid_chars="replaceInvalidChars",
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_secret_id="secretsManagerSecretId",
                    server_side_encryption_kms_key_id="serverSideEncryptionKmsKeyId",
                    service_access_role_arn="serviceAccessRoleArn",
                    time_format="timeFormat",
                    trim_blanks=False,
                    truncate_columns=False,
                    write_buffer_size=123
                ),
                resource_identifier="resourceIdentifier",
                s3_settings=dms.CfnEndpoint.S3SettingsProperty(
                    add_column_name=False,
                    bucket_folder="bucketFolder",
                    bucket_name="bucketName",
                    canned_acl_for_objects="cannedAclForObjects",
                    cdc_inserts_and_updates=False,
                    cdc_inserts_only=False,
                    cdc_max_batch_interval=123,
                    cdc_min_file_size=123,
                    cdc_path="cdcPath",
                    compression_type="compressionType",
                    csv_delimiter="csvDelimiter",
                    csv_no_sup_value="csvNoSupValue",
                    csv_null_value="csvNullValue",
                    csv_row_delimiter="csvRowDelimiter",
                    data_format="dataFormat",
                    data_page_size=123,
                    date_partition_delimiter="datePartitionDelimiter",
                    date_partition_enabled=False,
                    date_partition_sequence="datePartitionSequence",
                    date_partition_timezone="datePartitionTimezone",
                    dict_page_size_limit=123,
                    enable_statistics=False,
                    encoding_type="encodingType",
                    encryption_mode="encryptionMode",
                    external_table_definition="externalTableDefinition",
                    ignore_header_rows=123,
                    include_op_for_full_load=False,
                    max_file_size=123,
                    parquet_timestamp_in_millisecond=False,
                    parquet_version="parquetVersion",
                    preserve_transactions=False,
                    rfc4180=False,
                    row_group_length=123,
                    server_side_encryption_kms_key_id="serverSideEncryptionKmsKeyId",
                    service_access_role_arn="serviceAccessRoleArn",
                    timestamp_column_name="timestampColumnName",
                    use_csv_no_sup_value=False,
                    use_task_start_time_for_full_load_timestamp=False
                ),
                server_name="serverName",
                ssl_mode="sslMode",
                sybase_settings=dms.CfnEndpoint.SybaseSettingsProperty(
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_secret_id="secretsManagerSecretId"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                username="username"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3846aa4465700375d8cb01199b03bb11e111b3f12d9f6508c8b2c749d6f87d05)
            check_type(argname="argument endpoint_type", value=endpoint_type, expected_type=type_hints["endpoint_type"])
            check_type(argname="argument engine_name", value=engine_name, expected_type=type_hints["engine_name"])
            check_type(argname="argument certificate_arn", value=certificate_arn, expected_type=type_hints["certificate_arn"])
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument doc_db_settings", value=doc_db_settings, expected_type=type_hints["doc_db_settings"])
            check_type(argname="argument dynamo_db_settings", value=dynamo_db_settings, expected_type=type_hints["dynamo_db_settings"])
            check_type(argname="argument elasticsearch_settings", value=elasticsearch_settings, expected_type=type_hints["elasticsearch_settings"])
            check_type(argname="argument endpoint_identifier", value=endpoint_identifier, expected_type=type_hints["endpoint_identifier"])
            check_type(argname="argument extra_connection_attributes", value=extra_connection_attributes, expected_type=type_hints["extra_connection_attributes"])
            check_type(argname="argument gcp_my_sql_settings", value=gcp_my_sql_settings, expected_type=type_hints["gcp_my_sql_settings"])
            check_type(argname="argument ibm_db2_settings", value=ibm_db2_settings, expected_type=type_hints["ibm_db2_settings"])
            check_type(argname="argument kafka_settings", value=kafka_settings, expected_type=type_hints["kafka_settings"])
            check_type(argname="argument kinesis_settings", value=kinesis_settings, expected_type=type_hints["kinesis_settings"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument microsoft_sql_server_settings", value=microsoft_sql_server_settings, expected_type=type_hints["microsoft_sql_server_settings"])
            check_type(argname="argument mongo_db_settings", value=mongo_db_settings, expected_type=type_hints["mongo_db_settings"])
            check_type(argname="argument my_sql_settings", value=my_sql_settings, expected_type=type_hints["my_sql_settings"])
            check_type(argname="argument neptune_settings", value=neptune_settings, expected_type=type_hints["neptune_settings"])
            check_type(argname="argument oracle_settings", value=oracle_settings, expected_type=type_hints["oracle_settings"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument postgre_sql_settings", value=postgre_sql_settings, expected_type=type_hints["postgre_sql_settings"])
            check_type(argname="argument redis_settings", value=redis_settings, expected_type=type_hints["redis_settings"])
            check_type(argname="argument redshift_settings", value=redshift_settings, expected_type=type_hints["redshift_settings"])
            check_type(argname="argument resource_identifier", value=resource_identifier, expected_type=type_hints["resource_identifier"])
            check_type(argname="argument s3_settings", value=s3_settings, expected_type=type_hints["s3_settings"])
            check_type(argname="argument server_name", value=server_name, expected_type=type_hints["server_name"])
            check_type(argname="argument ssl_mode", value=ssl_mode, expected_type=type_hints["ssl_mode"])
            check_type(argname="argument sybase_settings", value=sybase_settings, expected_type=type_hints["sybase_settings"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "endpoint_type": endpoint_type,
            "engine_name": engine_name,
        }
        if certificate_arn is not None:
            self._values["certificate_arn"] = certificate_arn
        if database_name is not None:
            self._values["database_name"] = database_name
        if doc_db_settings is not None:
            self._values["doc_db_settings"] = doc_db_settings
        if dynamo_db_settings is not None:
            self._values["dynamo_db_settings"] = dynamo_db_settings
        if elasticsearch_settings is not None:
            self._values["elasticsearch_settings"] = elasticsearch_settings
        if endpoint_identifier is not None:
            self._values["endpoint_identifier"] = endpoint_identifier
        if extra_connection_attributes is not None:
            self._values["extra_connection_attributes"] = extra_connection_attributes
        if gcp_my_sql_settings is not None:
            self._values["gcp_my_sql_settings"] = gcp_my_sql_settings
        if ibm_db2_settings is not None:
            self._values["ibm_db2_settings"] = ibm_db2_settings
        if kafka_settings is not None:
            self._values["kafka_settings"] = kafka_settings
        if kinesis_settings is not None:
            self._values["kinesis_settings"] = kinesis_settings
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if microsoft_sql_server_settings is not None:
            self._values["microsoft_sql_server_settings"] = microsoft_sql_server_settings
        if mongo_db_settings is not None:
            self._values["mongo_db_settings"] = mongo_db_settings
        if my_sql_settings is not None:
            self._values["my_sql_settings"] = my_sql_settings
        if neptune_settings is not None:
            self._values["neptune_settings"] = neptune_settings
        if oracle_settings is not None:
            self._values["oracle_settings"] = oracle_settings
        if password is not None:
            self._values["password"] = password
        if port is not None:
            self._values["port"] = port
        if postgre_sql_settings is not None:
            self._values["postgre_sql_settings"] = postgre_sql_settings
        if redis_settings is not None:
            self._values["redis_settings"] = redis_settings
        if redshift_settings is not None:
            self._values["redshift_settings"] = redshift_settings
        if resource_identifier is not None:
            self._values["resource_identifier"] = resource_identifier
        if s3_settings is not None:
            self._values["s3_settings"] = s3_settings
        if server_name is not None:
            self._values["server_name"] = server_name
        if ssl_mode is not None:
            self._values["ssl_mode"] = ssl_mode
        if sybase_settings is not None:
            self._values["sybase_settings"] = sybase_settings
        if tags is not None:
            self._values["tags"] = tags
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def endpoint_type(self) -> builtins.str:
        '''The type of endpoint.

        Valid values are ``source`` and ``target`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-endpointtype
        '''
        result = self._values.get("endpoint_type")
        assert result is not None, "Required property 'endpoint_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def engine_name(self) -> builtins.str:
        '''The type of engine for the endpoint, depending on the ``EndpointType`` value.

        *Valid values* : ``mysql`` | ``oracle`` | ``postgres`` | ``mariadb`` | ``aurora`` | ``aurora-postgresql`` | ``opensearch`` | ``redshift`` | ``s3`` | ``db2`` | ``azuredb`` | ``sybase`` | ``dynamodb`` | ``mongodb`` | ``kinesis`` | ``kafka`` | ``elasticsearch`` | ``docdb`` | ``sqlserver`` | ``neptune``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-enginename
        '''
        result = self._values.get("engine_name")
        assert result is not None, "Required property 'engine_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) for the certificate.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-certificatearn
        '''
        result = self._values.get("certificate_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def database_name(self) -> typing.Optional[builtins.str]:
        '''The name of the endpoint database.

        For a MySQL source or target endpoint, don't specify ``DatabaseName`` . To migrate to a specific database, use this setting and ``targetDbType`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-databasename
        '''
        result = self._values.get("database_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def doc_db_settings(
        self,
    ) -> typing.Optional[typing.Union[CfnEndpoint.DocDbSettingsProperty, _IResolvable_a771d0ef]]:
        '''Settings in JSON format for the source and target DocumentDB endpoint.

        For more information about other available settings, see `Using extra connections attributes with Amazon DocumentDB as a source <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.DocumentDB.html#CHAP_Source.DocumentDB.ECAs>`_ and `Using Amazon DocumentDB as a target for AWS Database Migration Service <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.DocumentDB.html>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-docdbsettings
        '''
        result = self._values.get("doc_db_settings")
        return typing.cast(typing.Optional[typing.Union[CfnEndpoint.DocDbSettingsProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def dynamo_db_settings(
        self,
    ) -> typing.Optional[typing.Union[CfnEndpoint.DynamoDbSettingsProperty, _IResolvable_a771d0ef]]:
        '''Settings in JSON format for the target Amazon DynamoDB endpoint.

        For information about other available settings, see `Using object mapping to migrate data to DynamoDB <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.DynamoDB.html#CHAP_Target.DynamoDB.ObjectMapping>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-dynamodbsettings
        '''
        result = self._values.get("dynamo_db_settings")
        return typing.cast(typing.Optional[typing.Union[CfnEndpoint.DynamoDbSettingsProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def elasticsearch_settings(
        self,
    ) -> typing.Optional[typing.Union[CfnEndpoint.ElasticsearchSettingsProperty, _IResolvable_a771d0ef]]:
        '''Settings in JSON format for the target OpenSearch endpoint.

        For more information about the available settings, see `Extra connection attributes when using OpenSearch as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Elasticsearch.html#CHAP_Target.Elasticsearch.Configuration>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-elasticsearchsettings
        '''
        result = self._values.get("elasticsearch_settings")
        return typing.cast(typing.Optional[typing.Union[CfnEndpoint.ElasticsearchSettingsProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def endpoint_identifier(self) -> typing.Optional[builtins.str]:
        '''The database endpoint identifier.

        Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen, or contain two consecutive hyphens.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-endpointidentifier
        '''
        result = self._values.get("endpoint_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extra_connection_attributes(self) -> typing.Optional[builtins.str]:
        '''Additional attributes associated with the connection.

        Each attribute is specified as a name-value pair associated by an equal sign (=). Multiple attributes are separated by a semicolon (;) with no additional white space. For information on the attributes available for connecting your source or target endpoint, see `Working with AWS DMS Endpoints <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Endpoints.html>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-extraconnectionattributes
        '''
        result = self._values.get("extra_connection_attributes")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def gcp_my_sql_settings(
        self,
    ) -> typing.Optional[typing.Union[CfnEndpoint.GcpMySQLSettingsProperty, _IResolvable_a771d0ef]]:
        '''Settings in JSON format for the source GCP MySQL endpoint.

        These settings are much the same as the settings for any MySQL-compatible endpoint. For more information, see `Extra connection attributes when using MySQL as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html#CHAP_Source.MySQL.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-gcpmysqlsettings
        '''
        result = self._values.get("gcp_my_sql_settings")
        return typing.cast(typing.Optional[typing.Union[CfnEndpoint.GcpMySQLSettingsProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def ibm_db2_settings(
        self,
    ) -> typing.Optional[typing.Union[CfnEndpoint.IbmDb2SettingsProperty, _IResolvable_a771d0ef]]:
        '''Settings in JSON format for the source IBM Db2 LUW endpoint.

        For information about other available settings, see `Extra connection attributes when using Db2 LUW as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.DB2.html#CHAP_Source.DB2.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-ibmdb2settings
        '''
        result = self._values.get("ibm_db2_settings")
        return typing.cast(typing.Optional[typing.Union[CfnEndpoint.IbmDb2SettingsProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def kafka_settings(
        self,
    ) -> typing.Optional[typing.Union[CfnEndpoint.KafkaSettingsProperty, _IResolvable_a771d0ef]]:
        '''Settings in JSON format for the target Apache Kafka endpoint.

        For more information about other available settings, see `Using object mapping to migrate data to a Kafka topic <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kafka.html#CHAP_Target.Kafka.ObjectMapping>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-kafkasettings
        '''
        result = self._values.get("kafka_settings")
        return typing.cast(typing.Optional[typing.Union[CfnEndpoint.KafkaSettingsProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def kinesis_settings(
        self,
    ) -> typing.Optional[typing.Union[CfnEndpoint.KinesisSettingsProperty, _IResolvable_a771d0ef]]:
        '''Settings in JSON format for the target endpoint for Amazon Kinesis Data Streams.

        For more information about other available settings, see `Using object mapping to migrate data to a Kinesis data stream <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kinesis.html#CHAP_Target.Kinesis.ObjectMapping>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-kinesissettings
        '''
        result = self._values.get("kinesis_settings")
        return typing.cast(typing.Optional[typing.Union[CfnEndpoint.KinesisSettingsProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''An AWS KMS key identifier that is used to encrypt the connection parameters for the endpoint.

        If you don't specify a value for the ``KmsKeyId`` parameter, AWS DMS uses your default encryption key.

        AWS KMS creates the default encryption key for your AWS account . Your AWS account has a different default encryption key for each AWS Region .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def microsoft_sql_server_settings(
        self,
    ) -> typing.Optional[typing.Union[CfnEndpoint.MicrosoftSqlServerSettingsProperty, _IResolvable_a771d0ef]]:
        '''Settings in JSON format for the source and target Microsoft SQL Server endpoint.

        For information about other available settings, see `Extra connection attributes when using SQL Server as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SQLServer.html#CHAP_Source.SQLServer.ConnectionAttrib>`_ and `Extra connection attributes when using SQL Server as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.SQLServer.html#CHAP_Target.SQLServer.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-microsoftsqlserversettings
        '''
        result = self._values.get("microsoft_sql_server_settings")
        return typing.cast(typing.Optional[typing.Union[CfnEndpoint.MicrosoftSqlServerSettingsProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def mongo_db_settings(
        self,
    ) -> typing.Optional[typing.Union[CfnEndpoint.MongoDbSettingsProperty, _IResolvable_a771d0ef]]:
        '''Settings in JSON format for the source MongoDB endpoint.

        For more information about the available settings, see `Using MongoDB as a target for AWS Database Migration Service <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MongoDB.html#CHAP_Source.MongoDB.Configuration>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-mongodbsettings
        '''
        result = self._values.get("mongo_db_settings")
        return typing.cast(typing.Optional[typing.Union[CfnEndpoint.MongoDbSettingsProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def my_sql_settings(
        self,
    ) -> typing.Optional[typing.Union[CfnEndpoint.MySqlSettingsProperty, _IResolvable_a771d0ef]]:
        '''Settings in JSON format for the source and target MySQL endpoint.

        For information about other available settings, see `Extra connection attributes when using MySQL as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html#CHAP_Source.MySQL.ConnectionAttrib>`_ and `Extra connection attributes when using a MySQL-compatible database as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.MySQL.html#CHAP_Target.MySQL.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-mysqlsettings
        '''
        result = self._values.get("my_sql_settings")
        return typing.cast(typing.Optional[typing.Union[CfnEndpoint.MySqlSettingsProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def neptune_settings(
        self,
    ) -> typing.Optional[typing.Union[CfnEndpoint.NeptuneSettingsProperty, _IResolvable_a771d0ef]]:
        '''Settings in JSON format for the target Amazon Neptune endpoint.

        For more information about the available settings, see `Specifying endpoint settings for Amazon Neptune as a target <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Neptune.html#CHAP_Target.Neptune.EndpointSettings>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-neptunesettings
        '''
        result = self._values.get("neptune_settings")
        return typing.cast(typing.Optional[typing.Union[CfnEndpoint.NeptuneSettingsProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def oracle_settings(
        self,
    ) -> typing.Optional[typing.Union[CfnEndpoint.OracleSettingsProperty, _IResolvable_a771d0ef]]:
        '''Settings in JSON format for the source and target Oracle endpoint.

        For information about other available settings, see `Extra connection attributes when using Oracle as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.ConnectionAttrib>`_ and `Extra connection attributes when using Oracle as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Oracle.html#CHAP_Target.Oracle.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-oraclesettings
        '''
        result = self._values.get("oracle_settings")
        return typing.cast(typing.Optional[typing.Union[CfnEndpoint.OracleSettingsProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The password to be used to log in to the endpoint database.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-password
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The port used by the endpoint database.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def postgre_sql_settings(
        self,
    ) -> typing.Optional[typing.Union[CfnEndpoint.PostgreSqlSettingsProperty, _IResolvable_a771d0ef]]:
        '''Settings in JSON format for the source and target PostgreSQL endpoint.

        For information about other available settings, see `Extra connection attributes when using PostgreSQL as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.PostgreSQL.html#CHAP_Source.PostgreSQL.ConnectionAttrib>`_ and `Extra connection attributes when using PostgreSQL as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.PostgreSQL.html#CHAP_Target.PostgreSQL.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-postgresqlsettings
        '''
        result = self._values.get("postgre_sql_settings")
        return typing.cast(typing.Optional[typing.Union[CfnEndpoint.PostgreSqlSettingsProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def redis_settings(
        self,
    ) -> typing.Optional[typing.Union[CfnEndpoint.RedisSettingsProperty, _IResolvable_a771d0ef]]:
        '''Settings in JSON format for the target Redis endpoint.

        For information about other available settings, see `Specifying endpoint settings for Redis as a target <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Redis.html#CHAP_Target.Redis.EndpointSettings>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-redissettings
        '''
        result = self._values.get("redis_settings")
        return typing.cast(typing.Optional[typing.Union[CfnEndpoint.RedisSettingsProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def redshift_settings(
        self,
    ) -> typing.Optional[typing.Union[CfnEndpoint.RedshiftSettingsProperty, _IResolvable_a771d0ef]]:
        '''Settings in JSON format for the Amazon Redshift endpoint.

        For more information about other available settings, see `Extra connection attributes when using Amazon Redshift as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Redshift.html#CHAP_Target.Redshift.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-redshiftsettings
        '''
        result = self._values.get("redshift_settings")
        return typing.cast(typing.Optional[typing.Union[CfnEndpoint.RedshiftSettingsProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def resource_identifier(self) -> typing.Optional[builtins.str]:
        '''A display name for the resource identifier at the end of the ``EndpointArn`` response parameter that is returned in the created ``Endpoint`` object.

        The value for this parameter can have up to 31 characters. It can contain only ASCII letters, digits, and hyphen ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter, such as ``Example-App-ARN1`` .

        For example, this value might result in the ``EndpointArn`` value ``arn:aws:dms:eu-west-1:012345678901:rep:Example-App-ARN1`` . If you don't specify a ``ResourceIdentifier`` value, AWS DMS generates a default identifier value for the end of ``EndpointArn`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-resourceidentifier
        '''
        result = self._values.get("resource_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_settings(
        self,
    ) -> typing.Optional[typing.Union[CfnEndpoint.S3SettingsProperty, _IResolvable_a771d0ef]]:
        '''Settings in JSON format for the source and target Amazon S3 endpoint.

        For more information about other available settings, see `Extra connection attributes when using Amazon S3 as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.S3.html#CHAP_Source.S3.Configuring>`_ and `Extra connection attributes when using Amazon S3 as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-s3settings
        '''
        result = self._values.get("s3_settings")
        return typing.cast(typing.Optional[typing.Union[CfnEndpoint.S3SettingsProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def server_name(self) -> typing.Optional[builtins.str]:
        '''The name of the server where the endpoint database resides.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-servername
        '''
        result = self._values.get("server_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssl_mode(self) -> typing.Optional[builtins.str]:
        '''The Secure Sockets Layer (SSL) mode to use for the SSL connection. The default is ``none`` .

        .. epigraph::

           When ``engine_name`` is set to S3, the only allowed value is ``none`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-sslmode
        '''
        result = self._values.get("ssl_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sybase_settings(
        self,
    ) -> typing.Optional[typing.Union[CfnEndpoint.SybaseSettingsProperty, _IResolvable_a771d0ef]]:
        '''Settings in JSON format for the source and target SAP ASE endpoint.

        For information about other available settings, see `Extra connection attributes when using SAP ASE as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SAP.html#CHAP_Source.SAP.ConnectionAttrib>`_ and `Extra connection attributes when using SAP ASE as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.SAP.html#CHAP_Target.SAP.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-sybasesettings
        '''
        result = self._values.get("sybase_settings")
        return typing.cast(typing.Optional[typing.Union[CfnEndpoint.SybaseSettingsProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''One or more tags to be assigned to the endpoint.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''The user name to be used to log in to the endpoint database.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-username
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEndpointProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnEventSubscription(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_dms.CfnEventSubscription",
):
    '''A CloudFormation ``AWS::DMS::EventSubscription``.

    Use the ``AWS::DMS::EventSubscription`` resource to get notifications for AWS Database Migration Service events through the Amazon Simple Notification Service . For more information, see `Working with events and notifications in AWS Database Migration Service <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Events.html>`_ in the *AWS Database Migration Service User Guide* .

    :cloudformationResource: AWS::DMS::EventSubscription
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-eventsubscription.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_dms as dms
        
        cfn_event_subscription = dms.CfnEventSubscription(self, "MyCfnEventSubscription",
            sns_topic_arn="snsTopicArn",
        
            # the properties below are optional
            enabled=False,
            event_categories=["eventCategories"],
            source_ids=["sourceIds"],
            source_type="sourceType",
            subscription_name="subscriptionName",
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
        sns_topic_arn: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        event_categories: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_type: typing.Optional[builtins.str] = None,
        subscription_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::DMS::EventSubscription``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param sns_topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic created for event notification. The ARN is created by Amazon SNS when you create a topic and subscribe to it.
        :param enabled: Indicates whether to activate the subscription. If you don't specify this property, AWS CloudFormation activates the subscription.
        :param event_categories: A list of event categories for a source type that you want to subscribe to. If you don't specify this property, you are notified about all event categories. For more information, see `Working with Events and Notifications <https://docs.aws.amazon.com//dms/latest/userguide/CHAP_Events.html>`_ in the *AWS DMS User Guide* .
        :param source_ids: A list of identifiers for which AWS DMS provides notification events. If you don't specify a value, notifications are provided for all sources. If you specify multiple values, they must be of the same type. For example, if you specify a database instance ID, then all of the other values must be database instance IDs.
        :param source_type: The type of AWS DMS resource that generates the events. For example, if you want to be notified of events generated by a replication instance, you set this parameter to ``replication-instance`` . If this value isn't specified, all events are returned. *Valid values* : ``replication-instance`` | ``replication-task``
        :param subscription_name: The name of the AWS DMS event notification subscription. This name must be less than 255 characters.
        :param tags: One or more tags to be assigned to the event subscription.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed9a483887b88712ab19bee610dcc1a5ff39c64ec9fe87997156ac3d1ca216b9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEventSubscriptionProps(
            sns_topic_arn=sns_topic_arn,
            enabled=enabled,
            event_categories=event_categories,
            source_ids=source_ids,
            source_type=source_type,
            subscription_name=subscription_name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f01a7158f4408996e13a84b3b49f3feb30f1e37b19d5050e4b011111575ce7fa)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1fe006d58faba91c41d51b0ee2ecfa08d1c0e22755db43f0f5fde7e5b4aa9fa4)
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
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''One or more tags to be assigned to the event subscription.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-eventsubscription.html#cfn-dms-eventsubscription-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="snsTopicArn")
    def sns_topic_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Amazon SNS topic created for event notification.

        The ARN is created by Amazon SNS when you create a topic and subscribe to it.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-eventsubscription.html#cfn-dms-eventsubscription-snstopicarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "snsTopicArn"))

    @sns_topic_arn.setter
    def sns_topic_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c08a7c92b4af17042cf19ae9abcda4c43973a0a7ee94183999181f4cd9655dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snsTopicArn", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''Indicates whether to activate the subscription.

        If you don't specify this property, AWS CloudFormation activates the subscription.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-eventsubscription.html#cfn-dms-eventsubscription-enabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ad5bc447803eaea717199b040f0f67698408028c14ede5356de494be484fb16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="eventCategories")
    def event_categories(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of event categories for a source type that you want to subscribe to.

        If you don't specify this property, you are notified about all event categories. For more information, see `Working with Events and Notifications <https://docs.aws.amazon.com//dms/latest/userguide/CHAP_Events.html>`_ in the *AWS DMS User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-eventsubscription.html#cfn-dms-eventsubscription-eventcategories
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "eventCategories"))

    @event_categories.setter
    def event_categories(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c43ce4d555948bf9ee822a2dd1de8218a83479a5b9759b64daf593372716ee90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventCategories", value)

    @builtins.property
    @jsii.member(jsii_name="sourceIds")
    def source_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of identifiers for which AWS DMS provides notification events.

        If you don't specify a value, notifications are provided for all sources.

        If you specify multiple values, they must be of the same type. For example, if you specify a database instance ID, then all of the other values must be database instance IDs.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-eventsubscription.html#cfn-dms-eventsubscription-sourceids
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourceIds"))

    @source_ids.setter
    def source_ids(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04a3aae04d2f640bec56df5901dcea54370c57f08a1e62c3a31ecc0a8accf0ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceIds", value)

    @builtins.property
    @jsii.member(jsii_name="sourceType")
    def source_type(self) -> typing.Optional[builtins.str]:
        '''The type of AWS DMS resource that generates the events.

        For example, if you want to be notified of events generated by a replication instance, you set this parameter to ``replication-instance`` . If this value isn't specified, all events are returned.

        *Valid values* : ``replication-instance`` | ``replication-task``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-eventsubscription.html#cfn-dms-eventsubscription-sourcetype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceType"))

    @source_type.setter
    def source_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c808822a5e0035629732866ec86ed7a5f5b5153f5625bb27d64bd6c7b3f91fc9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceType", value)

    @builtins.property
    @jsii.member(jsii_name="subscriptionName")
    def subscription_name(self) -> typing.Optional[builtins.str]:
        '''The name of the AWS DMS event notification subscription.

        This name must be less than 255 characters.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-eventsubscription.html#cfn-dms-eventsubscription-subscriptionname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subscriptionName"))

    @subscription_name.setter
    def subscription_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d91c8f261cce5023aac6450efe2b21eb7cdcb1c3bc30e9287b17598f8cc83cae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subscriptionName", value)


@jsii.data_type(
    jsii_type="monocdk.aws_dms.CfnEventSubscriptionProps",
    jsii_struct_bases=[],
    name_mapping={
        "sns_topic_arn": "snsTopicArn",
        "enabled": "enabled",
        "event_categories": "eventCategories",
        "source_ids": "sourceIds",
        "source_type": "sourceType",
        "subscription_name": "subscriptionName",
        "tags": "tags",
    },
)
class CfnEventSubscriptionProps:
    def __init__(
        self,
        *,
        sns_topic_arn: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        event_categories: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_type: typing.Optional[builtins.str] = None,
        subscription_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEventSubscription``.

        :param sns_topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic created for event notification. The ARN is created by Amazon SNS when you create a topic and subscribe to it.
        :param enabled: Indicates whether to activate the subscription. If you don't specify this property, AWS CloudFormation activates the subscription.
        :param event_categories: A list of event categories for a source type that you want to subscribe to. If you don't specify this property, you are notified about all event categories. For more information, see `Working with Events and Notifications <https://docs.aws.amazon.com//dms/latest/userguide/CHAP_Events.html>`_ in the *AWS DMS User Guide* .
        :param source_ids: A list of identifiers for which AWS DMS provides notification events. If you don't specify a value, notifications are provided for all sources. If you specify multiple values, they must be of the same type. For example, if you specify a database instance ID, then all of the other values must be database instance IDs.
        :param source_type: The type of AWS DMS resource that generates the events. For example, if you want to be notified of events generated by a replication instance, you set this parameter to ``replication-instance`` . If this value isn't specified, all events are returned. *Valid values* : ``replication-instance`` | ``replication-task``
        :param subscription_name: The name of the AWS DMS event notification subscription. This name must be less than 255 characters.
        :param tags: One or more tags to be assigned to the event subscription.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-eventsubscription.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_dms as dms
            
            cfn_event_subscription_props = dms.CfnEventSubscriptionProps(
                sns_topic_arn="snsTopicArn",
            
                # the properties below are optional
                enabled=False,
                event_categories=["eventCategories"],
                source_ids=["sourceIds"],
                source_type="sourceType",
                subscription_name="subscriptionName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eac6da9bf7916943fcc6ef84e232a432ed6a28b7157007ad4fc22d5a4cbf436f)
            check_type(argname="argument sns_topic_arn", value=sns_topic_arn, expected_type=type_hints["sns_topic_arn"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument event_categories", value=event_categories, expected_type=type_hints["event_categories"])
            check_type(argname="argument source_ids", value=source_ids, expected_type=type_hints["source_ids"])
            check_type(argname="argument source_type", value=source_type, expected_type=type_hints["source_type"])
            check_type(argname="argument subscription_name", value=subscription_name, expected_type=type_hints["subscription_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "sns_topic_arn": sns_topic_arn,
        }
        if enabled is not None:
            self._values["enabled"] = enabled
        if event_categories is not None:
            self._values["event_categories"] = event_categories
        if source_ids is not None:
            self._values["source_ids"] = source_ids
        if source_type is not None:
            self._values["source_type"] = source_type
        if subscription_name is not None:
            self._values["subscription_name"] = subscription_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def sns_topic_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Amazon SNS topic created for event notification.

        The ARN is created by Amazon SNS when you create a topic and subscribe to it.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-eventsubscription.html#cfn-dms-eventsubscription-snstopicarn
        '''
        result = self._values.get("sns_topic_arn")
        assert result is not None, "Required property 'sns_topic_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''Indicates whether to activate the subscription.

        If you don't specify this property, AWS CloudFormation activates the subscription.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-eventsubscription.html#cfn-dms-eventsubscription-enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

    @builtins.property
    def event_categories(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of event categories for a source type that you want to subscribe to.

        If you don't specify this property, you are notified about all event categories. For more information, see `Working with Events and Notifications <https://docs.aws.amazon.com//dms/latest/userguide/CHAP_Events.html>`_ in the *AWS DMS User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-eventsubscription.html#cfn-dms-eventsubscription-eventcategories
        '''
        result = self._values.get("event_categories")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def source_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of identifiers for which AWS DMS provides notification events.

        If you don't specify a value, notifications are provided for all sources.

        If you specify multiple values, they must be of the same type. For example, if you specify a database instance ID, then all of the other values must be database instance IDs.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-eventsubscription.html#cfn-dms-eventsubscription-sourceids
        '''
        result = self._values.get("source_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def source_type(self) -> typing.Optional[builtins.str]:
        '''The type of AWS DMS resource that generates the events.

        For example, if you want to be notified of events generated by a replication instance, you set this parameter to ``replication-instance`` . If this value isn't specified, all events are returned.

        *Valid values* : ``replication-instance`` | ``replication-task``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-eventsubscription.html#cfn-dms-eventsubscription-sourcetype
        '''
        result = self._values.get("source_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subscription_name(self) -> typing.Optional[builtins.str]:
        '''The name of the AWS DMS event notification subscription.

        This name must be less than 255 characters.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-eventsubscription.html#cfn-dms-eventsubscription-subscriptionname
        '''
        result = self._values.get("subscription_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''One or more tags to be assigned to the event subscription.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-eventsubscription.html#cfn-dms-eventsubscription-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEventSubscriptionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnReplicationInstance(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_dms.CfnReplicationInstance",
):
    '''A CloudFormation ``AWS::DMS::ReplicationInstance``.

    The ``AWS::DMS::ReplicationInstance`` resource creates an AWS DMS replication instance.

    :cloudformationResource: AWS::DMS::ReplicationInstance
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_dms as dms
        
        cfn_replication_instance = dms.CfnReplicationInstance(self, "MyCfnReplicationInstance",
            replication_instance_class="replicationInstanceClass",
        
            # the properties below are optional
            allocated_storage=123,
            allow_major_version_upgrade=False,
            auto_minor_version_upgrade=False,
            availability_zone="availabilityZone",
            engine_version="engineVersion",
            kms_key_id="kmsKeyId",
            multi_az=False,
            preferred_maintenance_window="preferredMaintenanceWindow",
            publicly_accessible=False,
            replication_instance_identifier="replicationInstanceIdentifier",
            replication_subnet_group_identifier="replicationSubnetGroupIdentifier",
            resource_identifier="resourceIdentifier",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            vpc_security_group_ids=["vpcSecurityGroupIds"]
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        replication_instance_class: builtins.str,
        allocated_storage: typing.Optional[jsii.Number] = None,
        allow_major_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        engine_version: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        multi_az: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        publicly_accessible: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        replication_instance_identifier: typing.Optional[builtins.str] = None,
        replication_subnet_group_identifier: typing.Optional[builtins.str] = None,
        resource_identifier: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::DMS::ReplicationInstance``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param replication_instance_class: The compute and memory capacity of the replication instance as defined for the specified replication instance class. For example, to specify the instance class dms.c4.large, set this parameter to ``"dms.c4.large"`` . For more information on the settings and capacities for the available replication instance classes, see `Selecting the right AWS DMS replication instance for your migration <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html#CHAP_ReplicationInstance.InDepth>`_ in the *AWS Database Migration Service User Guide* .
        :param allocated_storage: The amount of storage (in gigabytes) to be initially allocated for the replication instance.
        :param allow_major_version_upgrade: Indicates that major version upgrades are allowed. Changing this parameter does not result in an outage, and the change is asynchronously applied as soon as possible. This parameter must be set to ``true`` when specifying a value for the ``EngineVersion`` parameter that is a different major version than the replication instance's current version.
        :param auto_minor_version_upgrade: A value that indicates whether minor engine upgrades are applied automatically to the replication instance during the maintenance window. This parameter defaults to ``true`` . Default: ``true``
        :param availability_zone: The Availability Zone that the replication instance will be created in. The default value is a random, system-chosen Availability Zone in the endpoint's AWS Region , for example ``us-east-1d`` .
        :param engine_version: The engine version number of the replication instance. If an engine version number is not specified when a replication instance is created, the default is the latest engine version available.
        :param kms_key_id: An AWS KMS key identifier that is used to encrypt the data on the replication instance. If you don't specify a value for the ``KmsKeyId`` parameter, AWS DMS uses your default encryption key. AWS KMS creates the default encryption key for your AWS account . Your AWS account has a different default encryption key for each AWS Region .
        :param multi_az: Specifies whether the replication instance is a Multi-AZ deployment. You can't set the ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .
        :param preferred_maintenance_window: The weekly time range during which system maintenance can occur, in UTC. *Format* : ``ddd:hh24:mi-ddd:hh24:mi`` *Default* : A 30-minute window selected at random from an 8-hour block of time per AWS Region , occurring on a random day of the week. *Valid days* ( ``ddd`` ): ``Mon`` | ``Tue`` | ``Wed`` | ``Thu`` | ``Fri`` | ``Sat`` | ``Sun`` *Constraints* : Minimum 30-minute window.
        :param publicly_accessible: Specifies the accessibility options for the replication instance. A value of ``true`` represents an instance with a public IP address. A value of ``false`` represents an instance with a private IP address. The default value is ``true`` .
        :param replication_instance_identifier: The replication instance identifier. This parameter is stored as a lowercase string. Constraints: - Must contain 1-63 alphanumeric characters or hyphens. - First character must be a letter. - Can't end with a hyphen or contain two consecutive hyphens. Example: ``myrepinstance``
        :param replication_subnet_group_identifier: A subnet group to associate with the replication instance.
        :param resource_identifier: A display name for the resource identifier at the end of the ``EndpointArn`` response parameter that is returned in the created ``Endpoint`` object. The value for this parameter can have up to 31 characters. It can contain only ASCII letters, digits, and hyphen ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter, such as ``Example-App-ARN1`` . For example, this value might result in the ``EndpointArn`` value ``arn:aws:dms:eu-west-1:012345678901:rep:Example-App-ARN1`` . If you don't specify a ``ResourceIdentifier`` value, AWS DMS generates a default identifier value for the end of ``EndpointArn`` .
        :param tags: One or more tags to be assigned to the replication instance.
        :param vpc_security_group_ids: Specifies the virtual private cloud (VPC) security group to be used with the replication instance. The VPC security group must work with the VPC containing the replication instance.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae453d536c4e8595e0abb4dc24ed93cbd3b8a113e9a2b8b51eaf575741838495)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnReplicationInstanceProps(
            replication_instance_class=replication_instance_class,
            allocated_storage=allocated_storage,
            allow_major_version_upgrade=allow_major_version_upgrade,
            auto_minor_version_upgrade=auto_minor_version_upgrade,
            availability_zone=availability_zone,
            engine_version=engine_version,
            kms_key_id=kms_key_id,
            multi_az=multi_az,
            preferred_maintenance_window=preferred_maintenance_window,
            publicly_accessible=publicly_accessible,
            replication_instance_identifier=replication_instance_identifier,
            replication_subnet_group_identifier=replication_subnet_group_identifier,
            resource_identifier=resource_identifier,
            tags=tags,
            vpc_security_group_ids=vpc_security_group_ids,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__632cae8ff54d24b7437bda048de9a67a46ba6bcf027a39935e3662bfc00fff69)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9868685aad0720bb2ccfab61702851662ecebe6a8d4ca79c0d67a1e031b7e2dc)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrReplicationInstancePrivateIpAddresses")
    def attr_replication_instance_private_ip_addresses(self) -> builtins.str:
        '''One or more private IP addresses for the replication instance.

        :cloudformationAttribute: ReplicationInstancePrivateIpAddresses
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrReplicationInstancePrivateIpAddresses"))

    @builtins.property
    @jsii.member(jsii_name="attrReplicationInstancePublicIpAddresses")
    def attr_replication_instance_public_ip_addresses(self) -> builtins.str:
        '''One or more public IP addresses for the replication instance.

        :cloudformationAttribute: ReplicationInstancePublicIpAddresses
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrReplicationInstancePublicIpAddresses"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''One or more tags to be assigned to the replication instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="replicationInstanceClass")
    def replication_instance_class(self) -> builtins.str:
        '''The compute and memory capacity of the replication instance as defined for the specified replication instance class.

        For example, to specify the instance class dms.c4.large, set this parameter to ``"dms.c4.large"`` . For more information on the settings and capacities for the available replication instance classes, see `Selecting the right AWS DMS replication instance for your migration <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html#CHAP_ReplicationInstance.InDepth>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-replicationinstanceclass
        '''
        return typing.cast(builtins.str, jsii.get(self, "replicationInstanceClass"))

    @replication_instance_class.setter
    def replication_instance_class(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f5a1c59b7279890ab539ff6e7d4f5ac30c040f813db3cabc40d980489eca971)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationInstanceClass", value)

    @builtins.property
    @jsii.member(jsii_name="allocatedStorage")
    def allocated_storage(self) -> typing.Optional[jsii.Number]:
        '''The amount of storage (in gigabytes) to be initially allocated for the replication instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-allocatedstorage
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "allocatedStorage"))

    @allocated_storage.setter
    def allocated_storage(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09d532711776e1ff5af2d32dcee888e22de3c4bc903dd890f2c716dfd29577ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allocatedStorage", value)

    @builtins.property
    @jsii.member(jsii_name="allowMajorVersionUpgrade")
    def allow_major_version_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''Indicates that major version upgrades are allowed.

        Changing this parameter does not result in an outage, and the change is asynchronously applied as soon as possible.

        This parameter must be set to ``true`` when specifying a value for the ``EngineVersion`` parameter that is a different major version than the replication instance's current version.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-allowmajorversionupgrade
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], jsii.get(self, "allowMajorVersionUpgrade"))

    @allow_major_version_upgrade.setter
    def allow_major_version_upgrade(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fd1890b6eebf4f32727ed3092ce3d7d01afc4c77381eac8af9ba21b497464be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowMajorVersionUpgrade", value)

    @builtins.property
    @jsii.member(jsii_name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''A value that indicates whether minor engine upgrades are applied automatically to the replication instance during the maintenance window.

        This parameter defaults to ``true`` .

        Default: ``true``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-autominorversionupgrade
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], jsii.get(self, "autoMinorVersionUpgrade"))

    @auto_minor_version_upgrade.setter
    def auto_minor_version_upgrade(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cff2dd5ed975a5598743d11b78b425f45f92f58a53465abf89edf3703cd2428b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoMinorVersionUpgrade", value)

    @builtins.property
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''The Availability Zone that the replication instance will be created in.

        The default value is a random, system-chosen Availability Zone in the endpoint's AWS Region , for example ``us-east-1d`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-availabilityzone
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZone"))

    @availability_zone.setter
    def availability_zone(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afdaeb43ae281129316de8f496a57be65627595a9563c167841cba0ca27286ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZone", value)

    @builtins.property
    @jsii.member(jsii_name="engineVersion")
    def engine_version(self) -> typing.Optional[builtins.str]:
        '''The engine version number of the replication instance.

        If an engine version number is not specified when a replication instance is created, the default is the latest engine version available.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-engineversion
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "engineVersion"))

    @engine_version.setter
    def engine_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a7ea0f656af005d9f13e3d242ea44643ea5484bf7a0d683ad5322c0dbf2519c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engineVersion", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''An AWS KMS key identifier that is used to encrypt the data on the replication instance.

        If you don't specify a value for the ``KmsKeyId`` parameter, AWS DMS uses your default encryption key.

        AWS KMS creates the default encryption key for your AWS account . Your AWS account has a different default encryption key for each AWS Region .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-kmskeyid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d39dc31bf0755b81f62a2a84e7be3832e18fb18d3ffa6259200f4cb45e6eca79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="multiAz")
    def multi_az(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''Specifies whether the replication instance is a Multi-AZ deployment.

        You can't set the ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-multiaz
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], jsii.get(self, "multiAz"))

    @multi_az.setter
    def multi_az(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ca8d5ccec5794109accb5cbd60c59f121fff0c1ded70038c3e4ca74123c585c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "multiAz", value)

    @builtins.property
    @jsii.member(jsii_name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''The weekly time range during which system maintenance can occur, in UTC.

        *Format* : ``ddd:hh24:mi-ddd:hh24:mi``

        *Default* : A 30-minute window selected at random from an 8-hour block of time per AWS Region , occurring on a random day of the week.

        *Valid days* ( ``ddd`` ): ``Mon`` | ``Tue`` | ``Wed`` | ``Thu`` | ``Fri`` | ``Sat`` | ``Sun``

        *Constraints* : Minimum 30-minute window.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-preferredmaintenancewindow
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredMaintenanceWindow"))

    @preferred_maintenance_window.setter
    def preferred_maintenance_window(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c98146675fc31fd640b7732727ca2dacd831d410bcc40c227b04ce7cfa9d82e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredMaintenanceWindow", value)

    @builtins.property
    @jsii.member(jsii_name="publiclyAccessible")
    def publicly_accessible(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''Specifies the accessibility options for the replication instance.

        A value of ``true`` represents an instance with a public IP address. A value of ``false`` represents an instance with a private IP address. The default value is ``true`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-publiclyaccessible
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], jsii.get(self, "publiclyAccessible"))

    @publicly_accessible.setter
    def publicly_accessible(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d58ccab74e1c937bf66a7ae37a2e09afd1d9015eec4bb6eec1d75cb99a88922)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publiclyAccessible", value)

    @builtins.property
    @jsii.member(jsii_name="replicationInstanceIdentifier")
    def replication_instance_identifier(self) -> typing.Optional[builtins.str]:
        '''The replication instance identifier. This parameter is stored as a lowercase string.

        Constraints:

        - Must contain 1-63 alphanumeric characters or hyphens.
        - First character must be a letter.
        - Can't end with a hyphen or contain two consecutive hyphens.

        Example: ``myrepinstance``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-replicationinstanceidentifier
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replicationInstanceIdentifier"))

    @replication_instance_identifier.setter
    def replication_instance_identifier(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99ac926e09a8e5e43bf2b3e3fa08f009caf6fe50eab7ced6e31e33ab3d8729f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationInstanceIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="replicationSubnetGroupIdentifier")
    def replication_subnet_group_identifier(self) -> typing.Optional[builtins.str]:
        '''A subnet group to associate with the replication instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-replicationsubnetgroupidentifier
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replicationSubnetGroupIdentifier"))

    @replication_subnet_group_identifier.setter
    def replication_subnet_group_identifier(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__045a7a1dbbde8107ef98ad5bf3d82acf91a6ae7585c5d9f41dc3864d67a20529)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationSubnetGroupIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="resourceIdentifier")
    def resource_identifier(self) -> typing.Optional[builtins.str]:
        '''A display name for the resource identifier at the end of the ``EndpointArn`` response parameter that is returned in the created ``Endpoint`` object.

        The value for this parameter can have up to 31 characters. It can contain only ASCII letters, digits, and hyphen ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter, such as ``Example-App-ARN1`` . For example, this value might result in the ``EndpointArn`` value ``arn:aws:dms:eu-west-1:012345678901:rep:Example-App-ARN1`` . If you don't specify a ``ResourceIdentifier`` value, AWS DMS generates a default identifier value for the end of ``EndpointArn`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-resourceidentifier
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceIdentifier"))

    @resource_identifier.setter
    def resource_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae36fd884b6c8fe3f981a55ccfbfba6a10282d23a4e201299025a731346083d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the virtual private cloud (VPC) security group to be used with the replication instance.

        The VPC security group must work with the VPC containing the replication instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-vpcsecuritygroupids
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "vpcSecurityGroupIds"))

    @vpc_security_group_ids.setter
    def vpc_security_group_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2cbda897f9a10b2ee4f1d9b42f33012bb8b9b34a93b503fc66a812b2b469d72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcSecurityGroupIds", value)


@jsii.data_type(
    jsii_type="monocdk.aws_dms.CfnReplicationInstanceProps",
    jsii_struct_bases=[],
    name_mapping={
        "replication_instance_class": "replicationInstanceClass",
        "allocated_storage": "allocatedStorage",
        "allow_major_version_upgrade": "allowMajorVersionUpgrade",
        "auto_minor_version_upgrade": "autoMinorVersionUpgrade",
        "availability_zone": "availabilityZone",
        "engine_version": "engineVersion",
        "kms_key_id": "kmsKeyId",
        "multi_az": "multiAz",
        "preferred_maintenance_window": "preferredMaintenanceWindow",
        "publicly_accessible": "publiclyAccessible",
        "replication_instance_identifier": "replicationInstanceIdentifier",
        "replication_subnet_group_identifier": "replicationSubnetGroupIdentifier",
        "resource_identifier": "resourceIdentifier",
        "tags": "tags",
        "vpc_security_group_ids": "vpcSecurityGroupIds",
    },
)
class CfnReplicationInstanceProps:
    def __init__(
        self,
        *,
        replication_instance_class: builtins.str,
        allocated_storage: typing.Optional[jsii.Number] = None,
        allow_major_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        engine_version: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        multi_az: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        publicly_accessible: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        replication_instance_identifier: typing.Optional[builtins.str] = None,
        replication_subnet_group_identifier: typing.Optional[builtins.str] = None,
        resource_identifier: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnReplicationInstance``.

        :param replication_instance_class: The compute and memory capacity of the replication instance as defined for the specified replication instance class. For example, to specify the instance class dms.c4.large, set this parameter to ``"dms.c4.large"`` . For more information on the settings and capacities for the available replication instance classes, see `Selecting the right AWS DMS replication instance for your migration <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html#CHAP_ReplicationInstance.InDepth>`_ in the *AWS Database Migration Service User Guide* .
        :param allocated_storage: The amount of storage (in gigabytes) to be initially allocated for the replication instance.
        :param allow_major_version_upgrade: Indicates that major version upgrades are allowed. Changing this parameter does not result in an outage, and the change is asynchronously applied as soon as possible. This parameter must be set to ``true`` when specifying a value for the ``EngineVersion`` parameter that is a different major version than the replication instance's current version.
        :param auto_minor_version_upgrade: A value that indicates whether minor engine upgrades are applied automatically to the replication instance during the maintenance window. This parameter defaults to ``true`` . Default: ``true``
        :param availability_zone: The Availability Zone that the replication instance will be created in. The default value is a random, system-chosen Availability Zone in the endpoint's AWS Region , for example ``us-east-1d`` .
        :param engine_version: The engine version number of the replication instance. If an engine version number is not specified when a replication instance is created, the default is the latest engine version available.
        :param kms_key_id: An AWS KMS key identifier that is used to encrypt the data on the replication instance. If you don't specify a value for the ``KmsKeyId`` parameter, AWS DMS uses your default encryption key. AWS KMS creates the default encryption key for your AWS account . Your AWS account has a different default encryption key for each AWS Region .
        :param multi_az: Specifies whether the replication instance is a Multi-AZ deployment. You can't set the ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .
        :param preferred_maintenance_window: The weekly time range during which system maintenance can occur, in UTC. *Format* : ``ddd:hh24:mi-ddd:hh24:mi`` *Default* : A 30-minute window selected at random from an 8-hour block of time per AWS Region , occurring on a random day of the week. *Valid days* ( ``ddd`` ): ``Mon`` | ``Tue`` | ``Wed`` | ``Thu`` | ``Fri`` | ``Sat`` | ``Sun`` *Constraints* : Minimum 30-minute window.
        :param publicly_accessible: Specifies the accessibility options for the replication instance. A value of ``true`` represents an instance with a public IP address. A value of ``false`` represents an instance with a private IP address. The default value is ``true`` .
        :param replication_instance_identifier: The replication instance identifier. This parameter is stored as a lowercase string. Constraints: - Must contain 1-63 alphanumeric characters or hyphens. - First character must be a letter. - Can't end with a hyphen or contain two consecutive hyphens. Example: ``myrepinstance``
        :param replication_subnet_group_identifier: A subnet group to associate with the replication instance.
        :param resource_identifier: A display name for the resource identifier at the end of the ``EndpointArn`` response parameter that is returned in the created ``Endpoint`` object. The value for this parameter can have up to 31 characters. It can contain only ASCII letters, digits, and hyphen ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter, such as ``Example-App-ARN1`` . For example, this value might result in the ``EndpointArn`` value ``arn:aws:dms:eu-west-1:012345678901:rep:Example-App-ARN1`` . If you don't specify a ``ResourceIdentifier`` value, AWS DMS generates a default identifier value for the end of ``EndpointArn`` .
        :param tags: One or more tags to be assigned to the replication instance.
        :param vpc_security_group_ids: Specifies the virtual private cloud (VPC) security group to be used with the replication instance. The VPC security group must work with the VPC containing the replication instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_dms as dms
            
            cfn_replication_instance_props = dms.CfnReplicationInstanceProps(
                replication_instance_class="replicationInstanceClass",
            
                # the properties below are optional
                allocated_storage=123,
                allow_major_version_upgrade=False,
                auto_minor_version_upgrade=False,
                availability_zone="availabilityZone",
                engine_version="engineVersion",
                kms_key_id="kmsKeyId",
                multi_az=False,
                preferred_maintenance_window="preferredMaintenanceWindow",
                publicly_accessible=False,
                replication_instance_identifier="replicationInstanceIdentifier",
                replication_subnet_group_identifier="replicationSubnetGroupIdentifier",
                resource_identifier="resourceIdentifier",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                vpc_security_group_ids=["vpcSecurityGroupIds"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2a6b5c4e5317ed21f76f6d4a59e7a60981666a61eebbadac007afa548eda3cc)
            check_type(argname="argument replication_instance_class", value=replication_instance_class, expected_type=type_hints["replication_instance_class"])
            check_type(argname="argument allocated_storage", value=allocated_storage, expected_type=type_hints["allocated_storage"])
            check_type(argname="argument allow_major_version_upgrade", value=allow_major_version_upgrade, expected_type=type_hints["allow_major_version_upgrade"])
            check_type(argname="argument auto_minor_version_upgrade", value=auto_minor_version_upgrade, expected_type=type_hints["auto_minor_version_upgrade"])
            check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
            check_type(argname="argument engine_version", value=engine_version, expected_type=type_hints["engine_version"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument multi_az", value=multi_az, expected_type=type_hints["multi_az"])
            check_type(argname="argument preferred_maintenance_window", value=preferred_maintenance_window, expected_type=type_hints["preferred_maintenance_window"])
            check_type(argname="argument publicly_accessible", value=publicly_accessible, expected_type=type_hints["publicly_accessible"])
            check_type(argname="argument replication_instance_identifier", value=replication_instance_identifier, expected_type=type_hints["replication_instance_identifier"])
            check_type(argname="argument replication_subnet_group_identifier", value=replication_subnet_group_identifier, expected_type=type_hints["replication_subnet_group_identifier"])
            check_type(argname="argument resource_identifier", value=resource_identifier, expected_type=type_hints["resource_identifier"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument vpc_security_group_ids", value=vpc_security_group_ids, expected_type=type_hints["vpc_security_group_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "replication_instance_class": replication_instance_class,
        }
        if allocated_storage is not None:
            self._values["allocated_storage"] = allocated_storage
        if allow_major_version_upgrade is not None:
            self._values["allow_major_version_upgrade"] = allow_major_version_upgrade
        if auto_minor_version_upgrade is not None:
            self._values["auto_minor_version_upgrade"] = auto_minor_version_upgrade
        if availability_zone is not None:
            self._values["availability_zone"] = availability_zone
        if engine_version is not None:
            self._values["engine_version"] = engine_version
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if multi_az is not None:
            self._values["multi_az"] = multi_az
        if preferred_maintenance_window is not None:
            self._values["preferred_maintenance_window"] = preferred_maintenance_window
        if publicly_accessible is not None:
            self._values["publicly_accessible"] = publicly_accessible
        if replication_instance_identifier is not None:
            self._values["replication_instance_identifier"] = replication_instance_identifier
        if replication_subnet_group_identifier is not None:
            self._values["replication_subnet_group_identifier"] = replication_subnet_group_identifier
        if resource_identifier is not None:
            self._values["resource_identifier"] = resource_identifier
        if tags is not None:
            self._values["tags"] = tags
        if vpc_security_group_ids is not None:
            self._values["vpc_security_group_ids"] = vpc_security_group_ids

    @builtins.property
    def replication_instance_class(self) -> builtins.str:
        '''The compute and memory capacity of the replication instance as defined for the specified replication instance class.

        For example, to specify the instance class dms.c4.large, set this parameter to ``"dms.c4.large"`` . For more information on the settings and capacities for the available replication instance classes, see `Selecting the right AWS DMS replication instance for your migration <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html#CHAP_ReplicationInstance.InDepth>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-replicationinstanceclass
        '''
        result = self._values.get("replication_instance_class")
        assert result is not None, "Required property 'replication_instance_class' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allocated_storage(self) -> typing.Optional[jsii.Number]:
        '''The amount of storage (in gigabytes) to be initially allocated for the replication instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-allocatedstorage
        '''
        result = self._values.get("allocated_storage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def allow_major_version_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''Indicates that major version upgrades are allowed.

        Changing this parameter does not result in an outage, and the change is asynchronously applied as soon as possible.

        This parameter must be set to ``true`` when specifying a value for the ``EngineVersion`` parameter that is a different major version than the replication instance's current version.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-allowmajorversionupgrade
        '''
        result = self._values.get("allow_major_version_upgrade")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

    @builtins.property
    def auto_minor_version_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''A value that indicates whether minor engine upgrades are applied automatically to the replication instance during the maintenance window.

        This parameter defaults to ``true`` .

        Default: ``true``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-autominorversionupgrade
        '''
        result = self._values.get("auto_minor_version_upgrade")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

    @builtins.property
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''The Availability Zone that the replication instance will be created in.

        The default value is a random, system-chosen Availability Zone in the endpoint's AWS Region , for example ``us-east-1d`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-availabilityzone
        '''
        result = self._values.get("availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def engine_version(self) -> typing.Optional[builtins.str]:
        '''The engine version number of the replication instance.

        If an engine version number is not specified when a replication instance is created, the default is the latest engine version available.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-engineversion
        '''
        result = self._values.get("engine_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''An AWS KMS key identifier that is used to encrypt the data on the replication instance.

        If you don't specify a value for the ``KmsKeyId`` parameter, AWS DMS uses your default encryption key.

        AWS KMS creates the default encryption key for your AWS account . Your AWS account has a different default encryption key for each AWS Region .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def multi_az(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''Specifies whether the replication instance is a Multi-AZ deployment.

        You can't set the ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-multiaz
        '''
        result = self._values.get("multi_az")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

    @builtins.property
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''The weekly time range during which system maintenance can occur, in UTC.

        *Format* : ``ddd:hh24:mi-ddd:hh24:mi``

        *Default* : A 30-minute window selected at random from an 8-hour block of time per AWS Region , occurring on a random day of the week.

        *Valid days* ( ``ddd`` ): ``Mon`` | ``Tue`` | ``Wed`` | ``Thu`` | ``Fri`` | ``Sat`` | ``Sun``

        *Constraints* : Minimum 30-minute window.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-preferredmaintenancewindow
        '''
        result = self._values.get("preferred_maintenance_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def publicly_accessible(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''Specifies the accessibility options for the replication instance.

        A value of ``true`` represents an instance with a public IP address. A value of ``false`` represents an instance with a private IP address. The default value is ``true`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-publiclyaccessible
        '''
        result = self._values.get("publicly_accessible")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

    @builtins.property
    def replication_instance_identifier(self) -> typing.Optional[builtins.str]:
        '''The replication instance identifier. This parameter is stored as a lowercase string.

        Constraints:

        - Must contain 1-63 alphanumeric characters or hyphens.
        - First character must be a letter.
        - Can't end with a hyphen or contain two consecutive hyphens.

        Example: ``myrepinstance``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-replicationinstanceidentifier
        '''
        result = self._values.get("replication_instance_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def replication_subnet_group_identifier(self) -> typing.Optional[builtins.str]:
        '''A subnet group to associate with the replication instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-replicationsubnetgroupidentifier
        '''
        result = self._values.get("replication_subnet_group_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_identifier(self) -> typing.Optional[builtins.str]:
        '''A display name for the resource identifier at the end of the ``EndpointArn`` response parameter that is returned in the created ``Endpoint`` object.

        The value for this parameter can have up to 31 characters. It can contain only ASCII letters, digits, and hyphen ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter, such as ``Example-App-ARN1`` . For example, this value might result in the ``EndpointArn`` value ``arn:aws:dms:eu-west-1:012345678901:rep:Example-App-ARN1`` . If you don't specify a ``ResourceIdentifier`` value, AWS DMS generates a default identifier value for the end of ``EndpointArn`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-resourceidentifier
        '''
        result = self._values.get("resource_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''One or more tags to be assigned to the replication instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    @builtins.property
    def vpc_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the virtual private cloud (VPC) security group to be used with the replication instance.

        The VPC security group must work with the VPC containing the replication instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-vpcsecuritygroupids
        '''
        result = self._values.get("vpc_security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnReplicationInstanceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnReplicationSubnetGroup(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_dms.CfnReplicationSubnetGroup",
):
    '''A CloudFormation ``AWS::DMS::ReplicationSubnetGroup``.

    The ``AWS::DMS::ReplicationSubnetGroup`` resource creates an AWS DMS replication subnet group. Subnet groups must contain at least two subnets in two different Availability Zones in the same AWS Region .
    .. epigraph::

       Resource creation fails if the ``dms-vpc-role`` AWS Identity and Access Management ( IAM ) role doesn't already exist. For more information, see `Creating the IAM Roles to Use With the AWS CLI and AWS DMS API <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.APIRole.html>`_ in the *AWS Database Migration Service User Guide* .

    :cloudformationResource: AWS::DMS::ReplicationSubnetGroup
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationsubnetgroup.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_dms as dms
        
        cfn_replication_subnet_group = dms.CfnReplicationSubnetGroup(self, "MyCfnReplicationSubnetGroup",
            replication_subnet_group_description="replicationSubnetGroupDescription",
            subnet_ids=["subnetIds"],
        
            # the properties below are optional
            replication_subnet_group_identifier="replicationSubnetGroupIdentifier",
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
        replication_subnet_group_description: builtins.str,
        subnet_ids: typing.Sequence[builtins.str],
        replication_subnet_group_identifier: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::DMS::ReplicationSubnetGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param replication_subnet_group_description: The description for the subnet group.
        :param subnet_ids: One or more subnet IDs to be assigned to the subnet group.
        :param replication_subnet_group_identifier: The identifier for the replication subnet group. If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the identifier.
        :param tags: One or more tags to be assigned to the subnet group.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ee2ab3c4c6babb11533157420d742b259cdc90bdf9630bcdadc97829fe97e54)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnReplicationSubnetGroupProps(
            replication_subnet_group_description=replication_subnet_group_description,
            subnet_ids=subnet_ids,
            replication_subnet_group_identifier=replication_subnet_group_identifier,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fbafc9aa2e578da41cca9e6efe630a8f7411c6b27e32043cf07cfffda3c38a8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__451ba3e252d44ae9950f0913cc62216091d6498cb5bd7fc2b835b3822fdd1149)
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
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''One or more tags to be assigned to the subnet group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationsubnetgroup.html#cfn-dms-replicationsubnetgroup-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="replicationSubnetGroupDescription")
    def replication_subnet_group_description(self) -> builtins.str:
        '''The description for the subnet group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationsubnetgroup.html#cfn-dms-replicationsubnetgroup-replicationsubnetgroupdescription
        '''
        return typing.cast(builtins.str, jsii.get(self, "replicationSubnetGroupDescription"))

    @replication_subnet_group_description.setter
    def replication_subnet_group_description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7af0faaa13b2bd3840d178bf83e3cf5b44b8c4284e36eb921537a6d402dae7d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationSubnetGroupDescription", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''One or more subnet IDs to be assigned to the subnet group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationsubnetgroup.html#cfn-dms-replicationsubnetgroup-subnetids
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb9770e1eb956a551dab01abf98da7dd9b457b477e6c9a8c7472e35668070ae4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="replicationSubnetGroupIdentifier")
    def replication_subnet_group_identifier(self) -> typing.Optional[builtins.str]:
        '''The identifier for the replication subnet group.

        If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the identifier.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationsubnetgroup.html#cfn-dms-replicationsubnetgroup-replicationsubnetgroupidentifier
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replicationSubnetGroupIdentifier"))

    @replication_subnet_group_identifier.setter
    def replication_subnet_group_identifier(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a76a1f2ea529ce0cad0fc9f60cbd373ab040b5468718c95b74cc8ed82e8466a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationSubnetGroupIdentifier", value)


@jsii.data_type(
    jsii_type="monocdk.aws_dms.CfnReplicationSubnetGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "replication_subnet_group_description": "replicationSubnetGroupDescription",
        "subnet_ids": "subnetIds",
        "replication_subnet_group_identifier": "replicationSubnetGroupIdentifier",
        "tags": "tags",
    },
)
class CfnReplicationSubnetGroupProps:
    def __init__(
        self,
        *,
        replication_subnet_group_description: builtins.str,
        subnet_ids: typing.Sequence[builtins.str],
        replication_subnet_group_identifier: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnReplicationSubnetGroup``.

        :param replication_subnet_group_description: The description for the subnet group.
        :param subnet_ids: One or more subnet IDs to be assigned to the subnet group.
        :param replication_subnet_group_identifier: The identifier for the replication subnet group. If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the identifier.
        :param tags: One or more tags to be assigned to the subnet group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationsubnetgroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_dms as dms
            
            cfn_replication_subnet_group_props = dms.CfnReplicationSubnetGroupProps(
                replication_subnet_group_description="replicationSubnetGroupDescription",
                subnet_ids=["subnetIds"],
            
                # the properties below are optional
                replication_subnet_group_identifier="replicationSubnetGroupIdentifier",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3569fc156ff19c9a6fc6e712b9e869dde2594772c31a77ab58f39891fc567c5)
            check_type(argname="argument replication_subnet_group_description", value=replication_subnet_group_description, expected_type=type_hints["replication_subnet_group_description"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument replication_subnet_group_identifier", value=replication_subnet_group_identifier, expected_type=type_hints["replication_subnet_group_identifier"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "replication_subnet_group_description": replication_subnet_group_description,
            "subnet_ids": subnet_ids,
        }
        if replication_subnet_group_identifier is not None:
            self._values["replication_subnet_group_identifier"] = replication_subnet_group_identifier
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def replication_subnet_group_description(self) -> builtins.str:
        '''The description for the subnet group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationsubnetgroup.html#cfn-dms-replicationsubnetgroup-replicationsubnetgroupdescription
        '''
        result = self._values.get("replication_subnet_group_description")
        assert result is not None, "Required property 'replication_subnet_group_description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''One or more subnet IDs to be assigned to the subnet group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationsubnetgroup.html#cfn-dms-replicationsubnetgroup-subnetids
        '''
        result = self._values.get("subnet_ids")
        assert result is not None, "Required property 'subnet_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def replication_subnet_group_identifier(self) -> typing.Optional[builtins.str]:
        '''The identifier for the replication subnet group.

        If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the identifier.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationsubnetgroup.html#cfn-dms-replicationsubnetgroup-replicationsubnetgroupidentifier
        '''
        result = self._values.get("replication_subnet_group_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''One or more tags to be assigned to the subnet group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationsubnetgroup.html#cfn-dms-replicationsubnetgroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnReplicationSubnetGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnReplicationTask(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_dms.CfnReplicationTask",
):
    '''A CloudFormation ``AWS::DMS::ReplicationTask``.

    The ``AWS::DMS::ReplicationTask`` resource creates an AWS DMS replication task.

    :cloudformationResource: AWS::DMS::ReplicationTask
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_dms as dms
        
        cfn_replication_task = dms.CfnReplicationTask(self, "MyCfnReplicationTask",
            migration_type="migrationType",
            replication_instance_arn="replicationInstanceArn",
            source_endpoint_arn="sourceEndpointArn",
            table_mappings="tableMappings",
            target_endpoint_arn="targetEndpointArn",
        
            # the properties below are optional
            cdc_start_position="cdcStartPosition",
            cdc_start_time=123,
            cdc_stop_position="cdcStopPosition",
            replication_task_identifier="replicationTaskIdentifier",
            replication_task_settings="replicationTaskSettings",
            resource_identifier="resourceIdentifier",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            task_data="taskData"
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        migration_type: builtins.str,
        replication_instance_arn: builtins.str,
        source_endpoint_arn: builtins.str,
        table_mappings: builtins.str,
        target_endpoint_arn: builtins.str,
        cdc_start_position: typing.Optional[builtins.str] = None,
        cdc_start_time: typing.Optional[jsii.Number] = None,
        cdc_stop_position: typing.Optional[builtins.str] = None,
        replication_task_identifier: typing.Optional[builtins.str] = None,
        replication_task_settings: typing.Optional[builtins.str] = None,
        resource_identifier: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
        task_data: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::DMS::ReplicationTask``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param migration_type: The migration type. Valid values: ``full-load`` | ``cdc`` | ``full-load-and-cdc``
        :param replication_instance_arn: The Amazon Resource Name (ARN) of a replication instance.
        :param source_endpoint_arn: An Amazon Resource Name (ARN) that uniquely identifies the source endpoint.
        :param table_mappings: The table mappings for the task, in JSON format. For more information, see `Using Table Mapping to Specify Task Settings <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.html>`_ in the *AWS Database Migration Service User Guide* .
        :param target_endpoint_arn: An Amazon Resource Name (ARN) that uniquely identifies the target endpoint.
        :param cdc_start_position: Indicates when you want a change data capture (CDC) operation to start. Use either ``CdcStartPosition`` or ``CdcStartTime`` to specify when you want a CDC operation to start. Specifying both values results in an error. The value can be in date, checkpoint, log sequence number (LSN), or system change number (SCN) format. Here is a date example: ``--cdc-start-position "2018-03-08T12:12:12"`` Here is a checkpoint example: ``--cdc-start-position "checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93"`` Here is an LSN example: ``--cdc-start-position “mysql-bin-changelog.000024:373”`` .. epigraph:: When you use this task setting with a source PostgreSQL database, a logical replication slot should already be created and associated with the source endpoint. You can verify this by setting the ``slotName`` extra connection attribute to the name of this logical replication slot. For more information, see `Extra Connection Attributes When Using PostgreSQL as a Source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.PostgreSQL.html#CHAP_Source.PostgreSQL.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .
        :param cdc_start_time: Indicates the start time for a change data capture (CDC) operation.
        :param cdc_stop_position: Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time. Here is a server time example: ``--cdc-stop-position "server_time:2018-02-09T12:12:12"`` Here is a commit time example: ``--cdc-stop-position "commit_time: 2018-02-09T12:12:12"``
        :param replication_task_identifier: An identifier for the replication task. Constraints: - Must contain 1-255 alphanumeric characters or hyphens. - First character must be a letter. - Cannot end with a hyphen or contain two consecutive hyphens.
        :param replication_task_settings: Overall settings for the task, in JSON format. For more information, see `Specifying Task Settings for AWS Database Migration Service Tasks <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.html>`_ in the *AWS Database Migration Service User Guide* .
        :param resource_identifier: A display name for the resource identifier at the end of the ``EndpointArn`` response parameter that is returned in the created ``Endpoint`` object. The value for this parameter can have up to 31 characters. It can contain only ASCII letters, digits, and hyphen ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter, such as ``Example-App-ARN1`` . For example, this value might result in the ``EndpointArn`` value ``arn:aws:dms:eu-west-1:012345678901:rep:Example-App-ARN1`` . If you don't specify a ``ResourceIdentifier`` value, AWS DMS generates a default identifier value for the end of ``EndpointArn`` .
        :param tags: One or more tags to be assigned to the replication task.
        :param task_data: ``AWS::DMS::ReplicationTask.TaskData``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97cc37eb6af081c79d3af15c060ef72233337275ff6e28cc7acfee1ecdf5adb9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnReplicationTaskProps(
            migration_type=migration_type,
            replication_instance_arn=replication_instance_arn,
            source_endpoint_arn=source_endpoint_arn,
            table_mappings=table_mappings,
            target_endpoint_arn=target_endpoint_arn,
            cdc_start_position=cdc_start_position,
            cdc_start_time=cdc_start_time,
            cdc_stop_position=cdc_stop_position,
            replication_task_identifier=replication_task_identifier,
            replication_task_settings=replication_task_settings,
            resource_identifier=resource_identifier,
            tags=tags,
            task_data=task_data,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79ca4a4a60747edd129fc1b059a94bc9471c748befc135eaedbe30fa51807026)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f9a57bc05c04d125a890afbcd5fe93263cbdcaafe8ef6a54af80d6fee4e6d4cd)
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
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''One or more tags to be assigned to the replication task.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="migrationType")
    def migration_type(self) -> builtins.str:
        '''The migration type.

        Valid values: ``full-load`` | ``cdc`` | ``full-load-and-cdc``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-migrationtype
        '''
        return typing.cast(builtins.str, jsii.get(self, "migrationType"))

    @migration_type.setter
    def migration_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c47b925de554f6357194e559fbe203b0eb360bb6f3497f5c18440e84bfbac210)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "migrationType", value)

    @builtins.property
    @jsii.member(jsii_name="replicationInstanceArn")
    def replication_instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of a replication instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-replicationinstancearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "replicationInstanceArn"))

    @replication_instance_arn.setter
    def replication_instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0041f1f0146349c8df11428bf6b5b91753f0498420b7b95d8f962c9ace7d6b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationInstanceArn", value)

    @builtins.property
    @jsii.member(jsii_name="sourceEndpointArn")
    def source_endpoint_arn(self) -> builtins.str:
        '''An Amazon Resource Name (ARN) that uniquely identifies the source endpoint.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-sourceendpointarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "sourceEndpointArn"))

    @source_endpoint_arn.setter
    def source_endpoint_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adba1e1d3b5becf895fbce7a8994965b5db1691d736557409624d932f3c600f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceEndpointArn", value)

    @builtins.property
    @jsii.member(jsii_name="tableMappings")
    def table_mappings(self) -> builtins.str:
        '''The table mappings for the task, in JSON format.

        For more information, see `Using Table Mapping to Specify Task Settings <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.html>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-tablemappings
        '''
        return typing.cast(builtins.str, jsii.get(self, "tableMappings"))

    @table_mappings.setter
    def table_mappings(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f11e429ee8ff9b1be059cd7f66aac0429bf11bf575deaedc4f52a8bd217cf8fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableMappings", value)

    @builtins.property
    @jsii.member(jsii_name="targetEndpointArn")
    def target_endpoint_arn(self) -> builtins.str:
        '''An Amazon Resource Name (ARN) that uniquely identifies the target endpoint.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-targetendpointarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "targetEndpointArn"))

    @target_endpoint_arn.setter
    def target_endpoint_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f56b887dc0ac08cecc93bc76aa36b6326447eb10eaf36c127d4da0484fd03c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetEndpointArn", value)

    @builtins.property
    @jsii.member(jsii_name="cdcStartPosition")
    def cdc_start_position(self) -> typing.Optional[builtins.str]:
        '''Indicates when you want a change data capture (CDC) operation to start.

        Use either ``CdcStartPosition`` or ``CdcStartTime`` to specify when you want a CDC operation to start. Specifying both values results in an error.

        The value can be in date, checkpoint, log sequence number (LSN), or system change number (SCN) format.

        Here is a date example: ``--cdc-start-position "2018-03-08T12:12:12"``

        Here is a checkpoint example: ``--cdc-start-position "checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93"``

        Here is an LSN example: ``--cdc-start-position “mysql-bin-changelog.000024:373”``
        .. epigraph::

           When you use this task setting with a source PostgreSQL database, a logical replication slot should already be created and associated with the source endpoint. You can verify this by setting the ``slotName`` extra connection attribute to the name of this logical replication slot. For more information, see `Extra Connection Attributes When Using PostgreSQL as a Source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.PostgreSQL.html#CHAP_Source.PostgreSQL.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-cdcstartposition
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cdcStartPosition"))

    @cdc_start_position.setter
    def cdc_start_position(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa82d6e089afb93ad70af3df19227faf2db3eb623c8f07fd1456bf56cbaff6d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdcStartPosition", value)

    @builtins.property
    @jsii.member(jsii_name="cdcStartTime")
    def cdc_start_time(self) -> typing.Optional[jsii.Number]:
        '''Indicates the start time for a change data capture (CDC) operation.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-cdcstarttime
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cdcStartTime"))

    @cdc_start_time.setter
    def cdc_start_time(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d92df919d84bc8b83971df67e68f533ccd204f4fe55e3fcc7aa95c9cce003482)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdcStartTime", value)

    @builtins.property
    @jsii.member(jsii_name="cdcStopPosition")
    def cdc_stop_position(self) -> typing.Optional[builtins.str]:
        '''Indicates when you want a change data capture (CDC) operation to stop.

        The value can be either server time or commit time.

        Here is a server time example: ``--cdc-stop-position "server_time:2018-02-09T12:12:12"``

        Here is a commit time example: ``--cdc-stop-position "commit_time: 2018-02-09T12:12:12"``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-cdcstopposition
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cdcStopPosition"))

    @cdc_stop_position.setter
    def cdc_stop_position(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65d50e4e15ed3bec1700147705e723139ced5f2a2c300c4e46341259d4ab1453)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdcStopPosition", value)

    @builtins.property
    @jsii.member(jsii_name="replicationTaskIdentifier")
    def replication_task_identifier(self) -> typing.Optional[builtins.str]:
        '''An identifier for the replication task.

        Constraints:

        - Must contain 1-255 alphanumeric characters or hyphens.
        - First character must be a letter.
        - Cannot end with a hyphen or contain two consecutive hyphens.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-replicationtaskidentifier
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replicationTaskIdentifier"))

    @replication_task_identifier.setter
    def replication_task_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e2fb0f771f11c9dee384348116c2dc68494b80be453e67f8e2a47b4f27aa4cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationTaskIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="replicationTaskSettings")
    def replication_task_settings(self) -> typing.Optional[builtins.str]:
        '''Overall settings for the task, in JSON format.

        For more information, see `Specifying Task Settings for AWS Database Migration Service Tasks <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.html>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-replicationtasksettings
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replicationTaskSettings"))

    @replication_task_settings.setter
    def replication_task_settings(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bad8bf37d0f1b7a5355cd09acd68ae696e327038c60d7493eb51e2c89a362eb7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationTaskSettings", value)

    @builtins.property
    @jsii.member(jsii_name="resourceIdentifier")
    def resource_identifier(self) -> typing.Optional[builtins.str]:
        '''A display name for the resource identifier at the end of the ``EndpointArn`` response parameter that is returned in the created ``Endpoint`` object.

        The value for this parameter can have up to 31 characters. It can contain only ASCII letters, digits, and hyphen ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter, such as ``Example-App-ARN1`` .

        For example, this value might result in the ``EndpointArn`` value ``arn:aws:dms:eu-west-1:012345678901:rep:Example-App-ARN1`` . If you don't specify a ``ResourceIdentifier`` value, AWS DMS generates a default identifier value for the end of ``EndpointArn`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-resourceidentifier
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceIdentifier"))

    @resource_identifier.setter
    def resource_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e8ecad3e2b72494baa1481deae03ba6815e8ad2aec0a7d1c81947b1b48f0e8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="taskData")
    def task_data(self) -> typing.Optional[builtins.str]:
        '''``AWS::DMS::ReplicationTask.TaskData``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-taskdata
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "taskData"))

    @task_data.setter
    def task_data(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef31ec51285cff017775c6429d28c963021adb82d45a9b4d8057cc5c03502f52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskData", value)


@jsii.data_type(
    jsii_type="monocdk.aws_dms.CfnReplicationTaskProps",
    jsii_struct_bases=[],
    name_mapping={
        "migration_type": "migrationType",
        "replication_instance_arn": "replicationInstanceArn",
        "source_endpoint_arn": "sourceEndpointArn",
        "table_mappings": "tableMappings",
        "target_endpoint_arn": "targetEndpointArn",
        "cdc_start_position": "cdcStartPosition",
        "cdc_start_time": "cdcStartTime",
        "cdc_stop_position": "cdcStopPosition",
        "replication_task_identifier": "replicationTaskIdentifier",
        "replication_task_settings": "replicationTaskSettings",
        "resource_identifier": "resourceIdentifier",
        "tags": "tags",
        "task_data": "taskData",
    },
)
class CfnReplicationTaskProps:
    def __init__(
        self,
        *,
        migration_type: builtins.str,
        replication_instance_arn: builtins.str,
        source_endpoint_arn: builtins.str,
        table_mappings: builtins.str,
        target_endpoint_arn: builtins.str,
        cdc_start_position: typing.Optional[builtins.str] = None,
        cdc_start_time: typing.Optional[jsii.Number] = None,
        cdc_stop_position: typing.Optional[builtins.str] = None,
        replication_task_identifier: typing.Optional[builtins.str] = None,
        replication_task_settings: typing.Optional[builtins.str] = None,
        resource_identifier: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
        task_data: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnReplicationTask``.

        :param migration_type: The migration type. Valid values: ``full-load`` | ``cdc`` | ``full-load-and-cdc``
        :param replication_instance_arn: The Amazon Resource Name (ARN) of a replication instance.
        :param source_endpoint_arn: An Amazon Resource Name (ARN) that uniquely identifies the source endpoint.
        :param table_mappings: The table mappings for the task, in JSON format. For more information, see `Using Table Mapping to Specify Task Settings <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.html>`_ in the *AWS Database Migration Service User Guide* .
        :param target_endpoint_arn: An Amazon Resource Name (ARN) that uniquely identifies the target endpoint.
        :param cdc_start_position: Indicates when you want a change data capture (CDC) operation to start. Use either ``CdcStartPosition`` or ``CdcStartTime`` to specify when you want a CDC operation to start. Specifying both values results in an error. The value can be in date, checkpoint, log sequence number (LSN), or system change number (SCN) format. Here is a date example: ``--cdc-start-position "2018-03-08T12:12:12"`` Here is a checkpoint example: ``--cdc-start-position "checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93"`` Here is an LSN example: ``--cdc-start-position “mysql-bin-changelog.000024:373”`` .. epigraph:: When you use this task setting with a source PostgreSQL database, a logical replication slot should already be created and associated with the source endpoint. You can verify this by setting the ``slotName`` extra connection attribute to the name of this logical replication slot. For more information, see `Extra Connection Attributes When Using PostgreSQL as a Source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.PostgreSQL.html#CHAP_Source.PostgreSQL.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .
        :param cdc_start_time: Indicates the start time for a change data capture (CDC) operation.
        :param cdc_stop_position: Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time. Here is a server time example: ``--cdc-stop-position "server_time:2018-02-09T12:12:12"`` Here is a commit time example: ``--cdc-stop-position "commit_time: 2018-02-09T12:12:12"``
        :param replication_task_identifier: An identifier for the replication task. Constraints: - Must contain 1-255 alphanumeric characters or hyphens. - First character must be a letter. - Cannot end with a hyphen or contain two consecutive hyphens.
        :param replication_task_settings: Overall settings for the task, in JSON format. For more information, see `Specifying Task Settings for AWS Database Migration Service Tasks <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.html>`_ in the *AWS Database Migration Service User Guide* .
        :param resource_identifier: A display name for the resource identifier at the end of the ``EndpointArn`` response parameter that is returned in the created ``Endpoint`` object. The value for this parameter can have up to 31 characters. It can contain only ASCII letters, digits, and hyphen ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter, such as ``Example-App-ARN1`` . For example, this value might result in the ``EndpointArn`` value ``arn:aws:dms:eu-west-1:012345678901:rep:Example-App-ARN1`` . If you don't specify a ``ResourceIdentifier`` value, AWS DMS generates a default identifier value for the end of ``EndpointArn`` .
        :param tags: One or more tags to be assigned to the replication task.
        :param task_data: ``AWS::DMS::ReplicationTask.TaskData``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_dms as dms
            
            cfn_replication_task_props = dms.CfnReplicationTaskProps(
                migration_type="migrationType",
                replication_instance_arn="replicationInstanceArn",
                source_endpoint_arn="sourceEndpointArn",
                table_mappings="tableMappings",
                target_endpoint_arn="targetEndpointArn",
            
                # the properties below are optional
                cdc_start_position="cdcStartPosition",
                cdc_start_time=123,
                cdc_stop_position="cdcStopPosition",
                replication_task_identifier="replicationTaskIdentifier",
                replication_task_settings="replicationTaskSettings",
                resource_identifier="resourceIdentifier",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                task_data="taskData"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ced164f0a1e318a05581e801b434d32986262bca8c5ea9fda179b2a4c97c9fca)
            check_type(argname="argument migration_type", value=migration_type, expected_type=type_hints["migration_type"])
            check_type(argname="argument replication_instance_arn", value=replication_instance_arn, expected_type=type_hints["replication_instance_arn"])
            check_type(argname="argument source_endpoint_arn", value=source_endpoint_arn, expected_type=type_hints["source_endpoint_arn"])
            check_type(argname="argument table_mappings", value=table_mappings, expected_type=type_hints["table_mappings"])
            check_type(argname="argument target_endpoint_arn", value=target_endpoint_arn, expected_type=type_hints["target_endpoint_arn"])
            check_type(argname="argument cdc_start_position", value=cdc_start_position, expected_type=type_hints["cdc_start_position"])
            check_type(argname="argument cdc_start_time", value=cdc_start_time, expected_type=type_hints["cdc_start_time"])
            check_type(argname="argument cdc_stop_position", value=cdc_stop_position, expected_type=type_hints["cdc_stop_position"])
            check_type(argname="argument replication_task_identifier", value=replication_task_identifier, expected_type=type_hints["replication_task_identifier"])
            check_type(argname="argument replication_task_settings", value=replication_task_settings, expected_type=type_hints["replication_task_settings"])
            check_type(argname="argument resource_identifier", value=resource_identifier, expected_type=type_hints["resource_identifier"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument task_data", value=task_data, expected_type=type_hints["task_data"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "migration_type": migration_type,
            "replication_instance_arn": replication_instance_arn,
            "source_endpoint_arn": source_endpoint_arn,
            "table_mappings": table_mappings,
            "target_endpoint_arn": target_endpoint_arn,
        }
        if cdc_start_position is not None:
            self._values["cdc_start_position"] = cdc_start_position
        if cdc_start_time is not None:
            self._values["cdc_start_time"] = cdc_start_time
        if cdc_stop_position is not None:
            self._values["cdc_stop_position"] = cdc_stop_position
        if replication_task_identifier is not None:
            self._values["replication_task_identifier"] = replication_task_identifier
        if replication_task_settings is not None:
            self._values["replication_task_settings"] = replication_task_settings
        if resource_identifier is not None:
            self._values["resource_identifier"] = resource_identifier
        if tags is not None:
            self._values["tags"] = tags
        if task_data is not None:
            self._values["task_data"] = task_data

    @builtins.property
    def migration_type(self) -> builtins.str:
        '''The migration type.

        Valid values: ``full-load`` | ``cdc`` | ``full-load-and-cdc``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-migrationtype
        '''
        result = self._values.get("migration_type")
        assert result is not None, "Required property 'migration_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def replication_instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of a replication instance.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-replicationinstancearn
        '''
        result = self._values.get("replication_instance_arn")
        assert result is not None, "Required property 'replication_instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_endpoint_arn(self) -> builtins.str:
        '''An Amazon Resource Name (ARN) that uniquely identifies the source endpoint.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-sourceendpointarn
        '''
        result = self._values.get("source_endpoint_arn")
        assert result is not None, "Required property 'source_endpoint_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_mappings(self) -> builtins.str:
        '''The table mappings for the task, in JSON format.

        For more information, see `Using Table Mapping to Specify Task Settings <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.html>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-tablemappings
        '''
        result = self._values.get("table_mappings")
        assert result is not None, "Required property 'table_mappings' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_endpoint_arn(self) -> builtins.str:
        '''An Amazon Resource Name (ARN) that uniquely identifies the target endpoint.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-targetendpointarn
        '''
        result = self._values.get("target_endpoint_arn")
        assert result is not None, "Required property 'target_endpoint_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cdc_start_position(self) -> typing.Optional[builtins.str]:
        '''Indicates when you want a change data capture (CDC) operation to start.

        Use either ``CdcStartPosition`` or ``CdcStartTime`` to specify when you want a CDC operation to start. Specifying both values results in an error.

        The value can be in date, checkpoint, log sequence number (LSN), or system change number (SCN) format.

        Here is a date example: ``--cdc-start-position "2018-03-08T12:12:12"``

        Here is a checkpoint example: ``--cdc-start-position "checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93"``

        Here is an LSN example: ``--cdc-start-position “mysql-bin-changelog.000024:373”``
        .. epigraph::

           When you use this task setting with a source PostgreSQL database, a logical replication slot should already be created and associated with the source endpoint. You can verify this by setting the ``slotName`` extra connection attribute to the name of this logical replication slot. For more information, see `Extra Connection Attributes When Using PostgreSQL as a Source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.PostgreSQL.html#CHAP_Source.PostgreSQL.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-cdcstartposition
        '''
        result = self._values.get("cdc_start_position")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cdc_start_time(self) -> typing.Optional[jsii.Number]:
        '''Indicates the start time for a change data capture (CDC) operation.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-cdcstarttime
        '''
        result = self._values.get("cdc_start_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cdc_stop_position(self) -> typing.Optional[builtins.str]:
        '''Indicates when you want a change data capture (CDC) operation to stop.

        The value can be either server time or commit time.

        Here is a server time example: ``--cdc-stop-position "server_time:2018-02-09T12:12:12"``

        Here is a commit time example: ``--cdc-stop-position "commit_time: 2018-02-09T12:12:12"``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-cdcstopposition
        '''
        result = self._values.get("cdc_stop_position")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def replication_task_identifier(self) -> typing.Optional[builtins.str]:
        '''An identifier for the replication task.

        Constraints:

        - Must contain 1-255 alphanumeric characters or hyphens.
        - First character must be a letter.
        - Cannot end with a hyphen or contain two consecutive hyphens.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-replicationtaskidentifier
        '''
        result = self._values.get("replication_task_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def replication_task_settings(self) -> typing.Optional[builtins.str]:
        '''Overall settings for the task, in JSON format.

        For more information, see `Specifying Task Settings for AWS Database Migration Service Tasks <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.html>`_ in the *AWS Database Migration Service User Guide* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-replicationtasksettings
        '''
        result = self._values.get("replication_task_settings")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_identifier(self) -> typing.Optional[builtins.str]:
        '''A display name for the resource identifier at the end of the ``EndpointArn`` response parameter that is returned in the created ``Endpoint`` object.

        The value for this parameter can have up to 31 characters. It can contain only ASCII letters, digits, and hyphen ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter, such as ``Example-App-ARN1`` .

        For example, this value might result in the ``EndpointArn`` value ``arn:aws:dms:eu-west-1:012345678901:rep:Example-App-ARN1`` . If you don't specify a ``ResourceIdentifier`` value, AWS DMS generates a default identifier value for the end of ``EndpointArn`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-resourceidentifier
        '''
        result = self._values.get("resource_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''One or more tags to be assigned to the replication task.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    @builtins.property
    def task_data(self) -> typing.Optional[builtins.str]:
        '''``AWS::DMS::ReplicationTask.TaskData``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-taskdata
        '''
        result = self._values.get("task_data")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnReplicationTaskProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCertificate",
    "CfnCertificateProps",
    "CfnEndpoint",
    "CfnEndpointProps",
    "CfnEventSubscription",
    "CfnEventSubscriptionProps",
    "CfnReplicationInstance",
    "CfnReplicationInstanceProps",
    "CfnReplicationSubnetGroup",
    "CfnReplicationSubnetGroupProps",
    "CfnReplicationTask",
    "CfnReplicationTaskProps",
]

publication.publish()

def _typecheckingstub__6d979b5faaef30b55f0baa438530b2b64189152fed38d623cd51c26acc3f6a6f(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    certificate_identifier: typing.Optional[builtins.str] = None,
    certificate_pem: typing.Optional[builtins.str] = None,
    certificate_wallet: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86a510a264dfa2e34b691e7a27244e66cf90815c0f30584cec7d7c9778fa5e9f(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fbdc78514f3756bf1e34650115adde8108c4ddf23c2cdf2c0596e969de6cf34(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99b2aefa35e0a8c9e52900fb49eddd2e702f971fb9dae833a50eab73e431f004(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__890d88ab2b7f7ccf0086b1a36ab18c8f209a2482233ce7cb521748ffd18dd92a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4067982d1e3936e4784a4ac328aa852dbadcf4bef5e14ee2d61d055147c9ea8b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01d018beae7bb80039522a75ca3d5437e2b052649fbbd020d98a2eff34641e38(
    *,
    certificate_identifier: typing.Optional[builtins.str] = None,
    certificate_pem: typing.Optional[builtins.str] = None,
    certificate_wallet: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b80cb01550182c42f97c84801688a4219f207ab936e9783f1e911db3806e295a(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    endpoint_type: builtins.str,
    engine_name: builtins.str,
    certificate_arn: typing.Optional[builtins.str] = None,
    database_name: typing.Optional[builtins.str] = None,
    doc_db_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.DocDbSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    dynamo_db_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.DynamoDbSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    elasticsearch_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.ElasticsearchSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    endpoint_identifier: typing.Optional[builtins.str] = None,
    extra_connection_attributes: typing.Optional[builtins.str] = None,
    gcp_my_sql_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.GcpMySQLSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    ibm_db2_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.IbmDb2SettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    kafka_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.KafkaSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    kinesis_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.KinesisSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    microsoft_sql_server_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.MicrosoftSqlServerSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    mongo_db_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.MongoDbSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    my_sql_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.MySqlSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    neptune_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.NeptuneSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    oracle_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.OracleSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    password: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    postgre_sql_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.PostgreSqlSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    redis_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.RedisSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    redshift_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.RedshiftSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    resource_identifier: typing.Optional[builtins.str] = None,
    s3_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.S3SettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    server_name: typing.Optional[builtins.str] = None,
    ssl_mode: typing.Optional[builtins.str] = None,
    sybase_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.SybaseSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2042813baa1c1096c0ac960beceffaf958fe9e9101f69d5ea2dd3f9ae221384(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fac39ac07c8358ab2389fcf1be93f2f7c07e208334af5c21ecdfc4f97604630(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b70e3048cb5084f9d84e4aa2c4e868cca681866dbe60d1b345df05989ead56e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36111ba9dee88e796f732bfe8f6fb7caae87359f0fbb10fffec894d6cb3f2baf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71b73a99af429b60f2650588b5d17e2d43ff0ff5cf1a84371a866e10e0212f03(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3d2f46c0259759c3f4bfd34159da2d8860b465dd17753b65f65a23a9222b8e6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1120b87703d042c0d113f94d99d58995a7dbb2d6bbfe4131fa13245992f7edc3(
    value: typing.Optional[typing.Union[CfnEndpoint.DocDbSettingsProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f5ae59f17daf8acc4379d9bb5fe7de5abeaf6694b06d0248dd0b07b7dd9ca38(
    value: typing.Optional[typing.Union[CfnEndpoint.DynamoDbSettingsProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3190e88c08339bcbabe7ab7335318fdefe45dfe697cf6d4e28cd5344ef67ac59(
    value: typing.Optional[typing.Union[CfnEndpoint.ElasticsearchSettingsProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b0dbaddc79e1f97c356c0aa921ef4dedf80cab928da7cf17b90c860f4636f3c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__471feade4152dc0e46bf911d1f434fbaa7677edb330b1ba73dc651c3fd5577a8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__676e92674b3a8b72cfa3018ece21734f3ba08bf12a853b3973abc95817a00c3b(
    value: typing.Optional[typing.Union[CfnEndpoint.GcpMySQLSettingsProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1e2595f5be5c8fa25c5ec8eb41077880b98d0d00b0d98d30464d0f57bfc4679(
    value: typing.Optional[typing.Union[CfnEndpoint.IbmDb2SettingsProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14678eb823011b903079a8ba375dd724cf9a8bca5d5ad96e7bd7ad9fcc2d4367(
    value: typing.Optional[typing.Union[CfnEndpoint.KafkaSettingsProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__418213c4c9ab68626c51ff6e44f646ed99d9fde2bcadb8ab392aed65074bb4fe(
    value: typing.Optional[typing.Union[CfnEndpoint.KinesisSettingsProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a34e72cc1fff2080b1994b47ea9da8148c1879d16020b37a2e32a62feb3c2915(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afbaa24445d4af14203f62cf7fa50694a4a51f03ae7f9fb9dde28842c0158158(
    value: typing.Optional[typing.Union[CfnEndpoint.MicrosoftSqlServerSettingsProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0a4d656104d0034cdf0ecf8db38f742b0a8bb1b764befd23b869ab961758c0d(
    value: typing.Optional[typing.Union[CfnEndpoint.MongoDbSettingsProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c32b50c347948e95a16708723f156974efaa51c6cb635142ee7ffe1a46f5c821(
    value: typing.Optional[typing.Union[CfnEndpoint.MySqlSettingsProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__031b01d60f73af53e6d4e6ce936c2427553caa8cc09263201fa907fc04de4570(
    value: typing.Optional[typing.Union[CfnEndpoint.NeptuneSettingsProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfccaff9a31133bfea110e6d6d860b621a431aa55db33fb3d2be007deed2a08c(
    value: typing.Optional[typing.Union[CfnEndpoint.OracleSettingsProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__245fdc73212922a23c7d84d6d92ebb70d4d1e8280e95bf17391d6f64ca42c204(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9690ad6532fe25316497e40dd439fa7ee253ac5f2f472f662bc46b970873c70(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc691848968c1d6d50e8b7d858474a94304bce094c79dae632b5e4220c62c208(
    value: typing.Optional[typing.Union[CfnEndpoint.PostgreSqlSettingsProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a369014e246456df9c5c756bfd7fc8a85b93ca632b01927f9c1ebb32ff2ddd1(
    value: typing.Optional[typing.Union[CfnEndpoint.RedisSettingsProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d774c13d229e8bab977cf9a990620508801d41760bd7299019de0c11cb8358c(
    value: typing.Optional[typing.Union[CfnEndpoint.RedshiftSettingsProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5a006892b9a525c811f210fc6e69d5f60e15b970e3320c59cc0d0b306167b5e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__398ce1cf49f22c04aa9c9ad875a6e9894d6c98d088034ac0601478e40c8ce596(
    value: typing.Optional[typing.Union[CfnEndpoint.S3SettingsProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2c8f32cfe4f822507c85fd661022611ecd212b975e9509e612be7b494cbeb38(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8c22accc018eead3b74efafeaf1a183065ee233dcd9a31ed8cff37078fe9eb3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b87c8e781a2d3285ddd8999e8c1f6157cf08f0573db90e15bdd0bbe00fa58d0(
    value: typing.Optional[typing.Union[CfnEndpoint.SybaseSettingsProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de6d2c3659f33d7556f3d0a49f7707551d65c11199e7e2f1fda7a3f4c4084475(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9bf8276635c85953ae5f0c4c3b0492f4aa31f1ed93aff08b1590f79fc9178cf(
    *,
    docs_to_investigate: typing.Optional[jsii.Number] = None,
    extract_doc_id: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    nesting_level: typing.Optional[builtins.str] = None,
    secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
    secrets_manager_secret_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41bc0e22e70470a9b4db3855416e7bfa0d12ffd2533dff28cae680ff337a0ffc(
    *,
    service_access_role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__682cf18e83c5c00fdb751700432cce646117b4a92d41af518f4663fa98814d2c(
    *,
    endpoint_uri: typing.Optional[builtins.str] = None,
    error_retry_duration: typing.Optional[jsii.Number] = None,
    full_load_error_percentage: typing.Optional[jsii.Number] = None,
    service_access_role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd1c0b06c8ceaf467d835d6ab2c746c73f943852b107b3ac3d8d83df2820914e(
    *,
    after_connect_script: typing.Optional[builtins.str] = None,
    clean_source_metadata_on_mismatch: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    database_name: typing.Optional[builtins.str] = None,
    events_poll_interval: typing.Optional[jsii.Number] = None,
    max_file_size: typing.Optional[jsii.Number] = None,
    parallel_load_threads: typing.Optional[jsii.Number] = None,
    password: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
    secrets_manager_secret_id: typing.Optional[builtins.str] = None,
    server_name: typing.Optional[builtins.str] = None,
    server_timezone: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0bb9685ace29805f69a4500ec1350518c53956efb1d676ffb3a67ee5b2170c7(
    *,
    current_lsn: typing.Optional[builtins.str] = None,
    max_k_bytes_per_read: typing.Optional[jsii.Number] = None,
    secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
    secrets_manager_secret_id: typing.Optional[builtins.str] = None,
    set_data_capture_changes: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b2bfaca6d665af7431f159590048ac8b759b878af0480fc254f2c8cf011d547(
    *,
    broker: typing.Optional[builtins.str] = None,
    include_control_details: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    include_null_and_empty: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    include_partition_value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    include_table_alter_operations: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    include_transaction_details: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    message_format: typing.Optional[builtins.str] = None,
    message_max_bytes: typing.Optional[jsii.Number] = None,
    no_hex_prefix: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    partition_include_schema_table: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    sasl_password: typing.Optional[builtins.str] = None,
    sasl_user_name: typing.Optional[builtins.str] = None,
    security_protocol: typing.Optional[builtins.str] = None,
    ssl_ca_certificate_arn: typing.Optional[builtins.str] = None,
    ssl_client_certificate_arn: typing.Optional[builtins.str] = None,
    ssl_client_key_arn: typing.Optional[builtins.str] = None,
    ssl_client_key_password: typing.Optional[builtins.str] = None,
    topic: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50ae30a854acf9cf5d2be7057f5211ed1623f13610e13f1ee2066cbe68d2bf26(
    *,
    include_control_details: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    include_null_and_empty: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    include_partition_value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    include_table_alter_operations: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    include_transaction_details: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    message_format: typing.Optional[builtins.str] = None,
    no_hex_prefix: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    partition_include_schema_table: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    service_access_role_arn: typing.Optional[builtins.str] = None,
    stream_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f7a6006215e1604c5eb4dbda619ce3e1479d08380de7614aded7df76594b7d8(
    *,
    bcp_packet_size: typing.Optional[jsii.Number] = None,
    control_tables_file_group: typing.Optional[builtins.str] = None,
    query_single_always_on_node: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    read_backup_only: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    safeguard_policy: typing.Optional[builtins.str] = None,
    secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
    secrets_manager_secret_id: typing.Optional[builtins.str] = None,
    use_bcp_full_load: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    use_third_party_backup_device: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a1be5105bbfbd03cd358a6d7a5d96718fb6e587c51f31f62e2103b312b45641(
    *,
    auth_mechanism: typing.Optional[builtins.str] = None,
    auth_source: typing.Optional[builtins.str] = None,
    auth_type: typing.Optional[builtins.str] = None,
    database_name: typing.Optional[builtins.str] = None,
    docs_to_investigate: typing.Optional[builtins.str] = None,
    extract_doc_id: typing.Optional[builtins.str] = None,
    nesting_level: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
    secrets_manager_secret_id: typing.Optional[builtins.str] = None,
    server_name: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be0b06e0664968b276ec30fd4245521fd3675357dfe12029f709bac30b468529(
    *,
    after_connect_script: typing.Optional[builtins.str] = None,
    clean_source_metadata_on_mismatch: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    events_poll_interval: typing.Optional[jsii.Number] = None,
    max_file_size: typing.Optional[jsii.Number] = None,
    parallel_load_threads: typing.Optional[jsii.Number] = None,
    secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
    secrets_manager_secret_id: typing.Optional[builtins.str] = None,
    server_timezone: typing.Optional[builtins.str] = None,
    target_db_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__434a69112509f8f99ce9dbb760f746ede02a0d869f4afa6869e7606ba3ce2409(
    *,
    error_retry_duration: typing.Optional[jsii.Number] = None,
    iam_auth_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    max_file_size: typing.Optional[jsii.Number] = None,
    max_retry_count: typing.Optional[jsii.Number] = None,
    s3_bucket_folder: typing.Optional[builtins.str] = None,
    s3_bucket_name: typing.Optional[builtins.str] = None,
    service_access_role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__464af41633f33a1ed9a8fe247f62c425817f547882c8631d54fe5ede395c9f20(
    *,
    access_alternate_directly: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    additional_archived_log_dest_id: typing.Optional[jsii.Number] = None,
    add_supplemental_logging: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    allow_select_nested_tables: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    archived_log_dest_id: typing.Optional[jsii.Number] = None,
    archived_logs_only: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    asm_password: typing.Optional[builtins.str] = None,
    asm_server: typing.Optional[builtins.str] = None,
    asm_user: typing.Optional[builtins.str] = None,
    char_length_semantics: typing.Optional[builtins.str] = None,
    direct_path_no_log: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    direct_path_parallel_load: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    enable_homogenous_tablespace: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    extra_archived_log_dest_ids: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[jsii.Number]]] = None,
    fail_tasks_on_lob_truncation: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    number_datatype_scale: typing.Optional[jsii.Number] = None,
    oracle_path_prefix: typing.Optional[builtins.str] = None,
    parallel_asm_read_threads: typing.Optional[jsii.Number] = None,
    read_ahead_blocks: typing.Optional[jsii.Number] = None,
    read_table_space_name: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    replace_path_prefix: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    retry_interval: typing.Optional[jsii.Number] = None,
    secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
    secrets_manager_oracle_asm_access_role_arn: typing.Optional[builtins.str] = None,
    secrets_manager_oracle_asm_secret_id: typing.Optional[builtins.str] = None,
    secrets_manager_secret_id: typing.Optional[builtins.str] = None,
    security_db_encryption: typing.Optional[builtins.str] = None,
    security_db_encryption_name: typing.Optional[builtins.str] = None,
    spatial_data_option_to_geo_json_function_name: typing.Optional[builtins.str] = None,
    standby_delay_time: typing.Optional[jsii.Number] = None,
    use_alternate_folder_for_online: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    use_b_file: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    use_direct_path_full_load: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    use_logminer_reader: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    use_path_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7718c9f321a7e3ac2ac907ba6716972aa25acd11ecf939790c5f30bbdf9f4f8(
    *,
    after_connect_script: typing.Optional[builtins.str] = None,
    capture_ddls: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    ddl_artifacts_schema: typing.Optional[builtins.str] = None,
    execute_timeout: typing.Optional[jsii.Number] = None,
    fail_tasks_on_lob_truncation: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    heartbeat_enable: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    heartbeat_frequency: typing.Optional[jsii.Number] = None,
    heartbeat_schema: typing.Optional[builtins.str] = None,
    max_file_size: typing.Optional[jsii.Number] = None,
    plugin_name: typing.Optional[builtins.str] = None,
    secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
    secrets_manager_secret_id: typing.Optional[builtins.str] = None,
    slot_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b554461776ac556361ecd0dd0196b43627b912f433b8c4b1117c65b9d0fcf9c2(
    *,
    auth_password: typing.Optional[builtins.str] = None,
    auth_type: typing.Optional[builtins.str] = None,
    auth_user_name: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    server_name: typing.Optional[builtins.str] = None,
    ssl_ca_certificate_arn: typing.Optional[builtins.str] = None,
    ssl_security_protocol: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__296834ac1ac0261ad3737a1bddc3d51ca428ac3e7f151aa7861afe37a343b544(
    *,
    accept_any_date: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    after_connect_script: typing.Optional[builtins.str] = None,
    bucket_folder: typing.Optional[builtins.str] = None,
    bucket_name: typing.Optional[builtins.str] = None,
    case_sensitive_names: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    comp_update: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    connection_timeout: typing.Optional[jsii.Number] = None,
    date_format: typing.Optional[builtins.str] = None,
    empty_as_null: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    encryption_mode: typing.Optional[builtins.str] = None,
    explicit_ids: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    file_transfer_upload_streams: typing.Optional[jsii.Number] = None,
    load_timeout: typing.Optional[jsii.Number] = None,
    max_file_size: typing.Optional[jsii.Number] = None,
    remove_quotes: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    replace_chars: typing.Optional[builtins.str] = None,
    replace_invalid_chars: typing.Optional[builtins.str] = None,
    secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
    secrets_manager_secret_id: typing.Optional[builtins.str] = None,
    server_side_encryption_kms_key_id: typing.Optional[builtins.str] = None,
    service_access_role_arn: typing.Optional[builtins.str] = None,
    time_format: typing.Optional[builtins.str] = None,
    trim_blanks: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    truncate_columns: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    write_buffer_size: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dce05f410d1325b0f2dfd514c502c320539e35971e8d2d9efc2220a7eb138441(
    *,
    add_column_name: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    bucket_folder: typing.Optional[builtins.str] = None,
    bucket_name: typing.Optional[builtins.str] = None,
    canned_acl_for_objects: typing.Optional[builtins.str] = None,
    cdc_inserts_and_updates: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    cdc_inserts_only: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    cdc_max_batch_interval: typing.Optional[jsii.Number] = None,
    cdc_min_file_size: typing.Optional[jsii.Number] = None,
    cdc_path: typing.Optional[builtins.str] = None,
    compression_type: typing.Optional[builtins.str] = None,
    csv_delimiter: typing.Optional[builtins.str] = None,
    csv_no_sup_value: typing.Optional[builtins.str] = None,
    csv_null_value: typing.Optional[builtins.str] = None,
    csv_row_delimiter: typing.Optional[builtins.str] = None,
    data_format: typing.Optional[builtins.str] = None,
    data_page_size: typing.Optional[jsii.Number] = None,
    date_partition_delimiter: typing.Optional[builtins.str] = None,
    date_partition_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    date_partition_sequence: typing.Optional[builtins.str] = None,
    date_partition_timezone: typing.Optional[builtins.str] = None,
    dict_page_size_limit: typing.Optional[jsii.Number] = None,
    enable_statistics: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    encoding_type: typing.Optional[builtins.str] = None,
    encryption_mode: typing.Optional[builtins.str] = None,
    external_table_definition: typing.Optional[builtins.str] = None,
    ignore_header_rows: typing.Optional[jsii.Number] = None,
    include_op_for_full_load: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    max_file_size: typing.Optional[jsii.Number] = None,
    parquet_timestamp_in_millisecond: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    parquet_version: typing.Optional[builtins.str] = None,
    preserve_transactions: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    rfc4180: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    row_group_length: typing.Optional[jsii.Number] = None,
    server_side_encryption_kms_key_id: typing.Optional[builtins.str] = None,
    service_access_role_arn: typing.Optional[builtins.str] = None,
    timestamp_column_name: typing.Optional[builtins.str] = None,
    use_csv_no_sup_value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    use_task_start_time_for_full_load_timestamp: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37f8ecccccfa862918c84ab832ab1b008e37457d1dd134f815173627c73c7baf(
    *,
    secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
    secrets_manager_secret_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3846aa4465700375d8cb01199b03bb11e111b3f12d9f6508c8b2c749d6f87d05(
    *,
    endpoint_type: builtins.str,
    engine_name: builtins.str,
    certificate_arn: typing.Optional[builtins.str] = None,
    database_name: typing.Optional[builtins.str] = None,
    doc_db_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.DocDbSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    dynamo_db_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.DynamoDbSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    elasticsearch_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.ElasticsearchSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    endpoint_identifier: typing.Optional[builtins.str] = None,
    extra_connection_attributes: typing.Optional[builtins.str] = None,
    gcp_my_sql_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.GcpMySQLSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    ibm_db2_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.IbmDb2SettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    kafka_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.KafkaSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    kinesis_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.KinesisSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    microsoft_sql_server_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.MicrosoftSqlServerSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    mongo_db_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.MongoDbSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    my_sql_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.MySqlSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    neptune_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.NeptuneSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    oracle_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.OracleSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    password: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    postgre_sql_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.PostgreSqlSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    redis_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.RedisSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    redshift_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.RedshiftSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    resource_identifier: typing.Optional[builtins.str] = None,
    s3_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.S3SettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    server_name: typing.Optional[builtins.str] = None,
    ssl_mode: typing.Optional[builtins.str] = None,
    sybase_settings: typing.Optional[typing.Union[typing.Union[CfnEndpoint.SybaseSettingsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed9a483887b88712ab19bee610dcc1a5ff39c64ec9fe87997156ac3d1ca216b9(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    sns_topic_arn: builtins.str,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    event_categories: typing.Optional[typing.Sequence[builtins.str]] = None,
    source_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    source_type: typing.Optional[builtins.str] = None,
    subscription_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f01a7158f4408996e13a84b3b49f3feb30f1e37b19d5050e4b011111575ce7fa(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fe006d58faba91c41d51b0ee2ecfa08d1c0e22755db43f0f5fde7e5b4aa9fa4(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c08a7c92b4af17042cf19ae9abcda4c43973a0a7ee94183999181f4cd9655dc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ad5bc447803eaea717199b040f0f67698408028c14ede5356de494be484fb16(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c43ce4d555948bf9ee822a2dd1de8218a83479a5b9759b64daf593372716ee90(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04a3aae04d2f640bec56df5901dcea54370c57f08a1e62c3a31ecc0a8accf0ae(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c808822a5e0035629732866ec86ed7a5f5b5153f5625bb27d64bd6c7b3f91fc9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d91c8f261cce5023aac6450efe2b21eb7cdcb1c3bc30e9287b17598f8cc83cae(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eac6da9bf7916943fcc6ef84e232a432ed6a28b7157007ad4fc22d5a4cbf436f(
    *,
    sns_topic_arn: builtins.str,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    event_categories: typing.Optional[typing.Sequence[builtins.str]] = None,
    source_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    source_type: typing.Optional[builtins.str] = None,
    subscription_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae453d536c4e8595e0abb4dc24ed93cbd3b8a113e9a2b8b51eaf575741838495(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    replication_instance_class: builtins.str,
    allocated_storage: typing.Optional[jsii.Number] = None,
    allow_major_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    availability_zone: typing.Optional[builtins.str] = None,
    engine_version: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    multi_az: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    preferred_maintenance_window: typing.Optional[builtins.str] = None,
    publicly_accessible: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    replication_instance_identifier: typing.Optional[builtins.str] = None,
    replication_subnet_group_identifier: typing.Optional[builtins.str] = None,
    resource_identifier: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__632cae8ff54d24b7437bda048de9a67a46ba6bcf027a39935e3662bfc00fff69(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9868685aad0720bb2ccfab61702851662ecebe6a8d4ca79c0d67a1e031b7e2dc(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f5a1c59b7279890ab539ff6e7d4f5ac30c040f813db3cabc40d980489eca971(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09d532711776e1ff5af2d32dcee888e22de3c4bc903dd890f2c716dfd29577ba(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fd1890b6eebf4f32727ed3092ce3d7d01afc4c77381eac8af9ba21b497464be(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cff2dd5ed975a5598743d11b78b425f45f92f58a53465abf89edf3703cd2428b(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afdaeb43ae281129316de8f496a57be65627595a9563c167841cba0ca27286ec(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a7ea0f656af005d9f13e3d242ea44643ea5484bf7a0d683ad5322c0dbf2519c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d39dc31bf0755b81f62a2a84e7be3832e18fb18d3ffa6259200f4cb45e6eca79(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ca8d5ccec5794109accb5cbd60c59f121fff0c1ded70038c3e4ca74123c585c(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c98146675fc31fd640b7732727ca2dacd831d410bcc40c227b04ce7cfa9d82e1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d58ccab74e1c937bf66a7ae37a2e09afd1d9015eec4bb6eec1d75cb99a88922(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99ac926e09a8e5e43bf2b3e3fa08f009caf6fe50eab7ced6e31e33ab3d8729f8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__045a7a1dbbde8107ef98ad5bf3d82acf91a6ae7585c5d9f41dc3864d67a20529(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae36fd884b6c8fe3f981a55ccfbfba6a10282d23a4e201299025a731346083d6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2cbda897f9a10b2ee4f1d9b42f33012bb8b9b34a93b503fc66a812b2b469d72(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2a6b5c4e5317ed21f76f6d4a59e7a60981666a61eebbadac007afa548eda3cc(
    *,
    replication_instance_class: builtins.str,
    allocated_storage: typing.Optional[jsii.Number] = None,
    allow_major_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    availability_zone: typing.Optional[builtins.str] = None,
    engine_version: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    multi_az: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    preferred_maintenance_window: typing.Optional[builtins.str] = None,
    publicly_accessible: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    replication_instance_identifier: typing.Optional[builtins.str] = None,
    replication_subnet_group_identifier: typing.Optional[builtins.str] = None,
    resource_identifier: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ee2ab3c4c6babb11533157420d742b259cdc90bdf9630bcdadc97829fe97e54(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    replication_subnet_group_description: builtins.str,
    subnet_ids: typing.Sequence[builtins.str],
    replication_subnet_group_identifier: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fbafc9aa2e578da41cca9e6efe630a8f7411c6b27e32043cf07cfffda3c38a8(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__451ba3e252d44ae9950f0913cc62216091d6498cb5bd7fc2b835b3822fdd1149(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7af0faaa13b2bd3840d178bf83e3cf5b44b8c4284e36eb921537a6d402dae7d8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb9770e1eb956a551dab01abf98da7dd9b457b477e6c9a8c7472e35668070ae4(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a76a1f2ea529ce0cad0fc9f60cbd373ab040b5468718c95b74cc8ed82e8466a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3569fc156ff19c9a6fc6e712b9e869dde2594772c31a77ab58f39891fc567c5(
    *,
    replication_subnet_group_description: builtins.str,
    subnet_ids: typing.Sequence[builtins.str],
    replication_subnet_group_identifier: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97cc37eb6af081c79d3af15c060ef72233337275ff6e28cc7acfee1ecdf5adb9(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    migration_type: builtins.str,
    replication_instance_arn: builtins.str,
    source_endpoint_arn: builtins.str,
    table_mappings: builtins.str,
    target_endpoint_arn: builtins.str,
    cdc_start_position: typing.Optional[builtins.str] = None,
    cdc_start_time: typing.Optional[jsii.Number] = None,
    cdc_stop_position: typing.Optional[builtins.str] = None,
    replication_task_identifier: typing.Optional[builtins.str] = None,
    replication_task_settings: typing.Optional[builtins.str] = None,
    resource_identifier: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    task_data: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79ca4a4a60747edd129fc1b059a94bc9471c748befc135eaedbe30fa51807026(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9a57bc05c04d125a890afbcd5fe93263cbdcaafe8ef6a54af80d6fee4e6d4cd(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c47b925de554f6357194e559fbe203b0eb360bb6f3497f5c18440e84bfbac210(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0041f1f0146349c8df11428bf6b5b91753f0498420b7b95d8f962c9ace7d6b7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adba1e1d3b5becf895fbce7a8994965b5db1691d736557409624d932f3c600f8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f11e429ee8ff9b1be059cd7f66aac0429bf11bf575deaedc4f52a8bd217cf8fa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f56b887dc0ac08cecc93bc76aa36b6326447eb10eaf36c127d4da0484fd03c0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa82d6e089afb93ad70af3df19227faf2db3eb623c8f07fd1456bf56cbaff6d5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d92df919d84bc8b83971df67e68f533ccd204f4fe55e3fcc7aa95c9cce003482(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65d50e4e15ed3bec1700147705e723139ced5f2a2c300c4e46341259d4ab1453(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e2fb0f771f11c9dee384348116c2dc68494b80be453e67f8e2a47b4f27aa4cc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bad8bf37d0f1b7a5355cd09acd68ae696e327038c60d7493eb51e2c89a362eb7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e8ecad3e2b72494baa1481deae03ba6815e8ad2aec0a7d1c81947b1b48f0e8d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef31ec51285cff017775c6429d28c963021adb82d45a9b4d8057cc5c03502f52(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ced164f0a1e318a05581e801b434d32986262bca8c5ea9fda179b2a4c97c9fca(
    *,
    migration_type: builtins.str,
    replication_instance_arn: builtins.str,
    source_endpoint_arn: builtins.str,
    table_mappings: builtins.str,
    target_endpoint_arn: builtins.str,
    cdc_start_position: typing.Optional[builtins.str] = None,
    cdc_start_time: typing.Optional[jsii.Number] = None,
    cdc_stop_position: typing.Optional[builtins.str] = None,
    replication_task_identifier: typing.Optional[builtins.str] = None,
    replication_task_settings: typing.Optional[builtins.str] = None,
    resource_identifier: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    task_data: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

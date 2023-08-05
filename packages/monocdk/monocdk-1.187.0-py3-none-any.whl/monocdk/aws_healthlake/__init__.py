'''
# AWS::HealthLake Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import monocdk as healthlake
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for HealthLake construct libraries](https://constructs.dev/search?q=healthlake)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::HealthLake resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_HealthLake.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::HealthLake](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_HealthLake.html).

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
class CfnFHIRDatastore(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_healthlake.CfnFHIRDatastore",
):
    '''A CloudFormation ``AWS::HealthLake::FHIRDatastore``.

    Creates a Data Store that can ingest and export FHIR formatted data.
    .. epigraph::

       Please note that when a user tries to do an Update operation via CloudFormation, changes to the Data Store name, Type Version, PreloadDataConfig, or SSEConfiguration will delete their existing Data Store for the stack and create a new one. This will lead to potential loss of data.

    :cloudformationResource: AWS::HealthLake::FHIRDatastore
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_healthlake as healthlake
        
        cfn_fHIRDatastore = healthlake.CfnFHIRDatastore(self, "MyCfnFHIRDatastore",
            datastore_type_version="datastoreTypeVersion",
        
            # the properties below are optional
            datastore_name="datastoreName",
            preload_data_config=healthlake.CfnFHIRDatastore.PreloadDataConfigProperty(
                preload_data_type="preloadDataType"
            ),
            sse_configuration=healthlake.CfnFHIRDatastore.SseConfigurationProperty(
                kms_encryption_config=healthlake.CfnFHIRDatastore.KmsEncryptionConfigProperty(
                    cmk_type="cmkType",
        
                    # the properties below are optional
                    kms_key_id="kmsKeyId"
                )
            ),
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
        datastore_type_version: builtins.str,
        datastore_name: typing.Optional[builtins.str] = None,
        preload_data_config: typing.Optional[typing.Union[typing.Union["CfnFHIRDatastore.PreloadDataConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        sse_configuration: typing.Optional[typing.Union[typing.Union["CfnFHIRDatastore.SseConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::HealthLake::FHIRDatastore``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param datastore_type_version: The FHIR version of the Data Store. The only supported version is R4.
        :param datastore_name: The user generated name for the Data Store.
        :param preload_data_config: The preloaded data configuration for the Data Store. Only data preloaded from Synthea is supported.
        :param sse_configuration: The server-side encryption key configuration for a customer provided encryption key specified for creating a Data Store.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ed946fd406aad2d2ef0dc31315b9021260e8654b17cec3b564ce004e56dd5ef)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFHIRDatastoreProps(
            datastore_type_version=datastore_type_version,
            datastore_name=datastore_name,
            preload_data_config=preload_data_config,
            sse_configuration=sse_configuration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83078627fd9ede8075f74cfdeb6b001ed3bd6b361f35b33e967b4a113824ab18)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7f5515fd07c10e77b898260ef3a4954b4e64ebf02e9856f0c36438192d4b0e11)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAtNanos")
    def attr_created_at_nanos(self) -> jsii.Number:
        '''
        :cloudformationAttribute: CreatedAt.Nanos
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrCreatedAtNanos"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAtSeconds")
    def attr_created_at_seconds(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreatedAt.Seconds
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAtSeconds"))

    @builtins.property
    @jsii.member(jsii_name="attrDatastoreArn")
    def attr_datastore_arn(self) -> builtins.str:
        '''The Data Store ARN is generated during the creation of the Data Store and can be found in the output from the initial Data Store creation request.

        :cloudformationAttribute: DatastoreArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDatastoreArn"))

    @builtins.property
    @jsii.member(jsii_name="attrDatastoreEndpoint")
    def attr_datastore_endpoint(self) -> builtins.str:
        '''The endpoint for the created Data Store.

        :cloudformationAttribute: DatastoreEndpoint
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDatastoreEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="attrDatastoreId")
    def attr_datastore_id(self) -> builtins.str:
        '''The Amazon generated Data Store id.

        This id is in the output from the initial Data Store creation call.

        :cloudformationAttribute: DatastoreId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDatastoreId"))

    @builtins.property
    @jsii.member(jsii_name="attrDatastoreStatus")
    def attr_datastore_status(self) -> builtins.str:
        '''The status of the FHIR Data Store.

        Possible statuses are ‘CREATING’, ‘ACTIVE’, ‘DELETING’, ‘DELETED’.

        :cloudformationAttribute: DatastoreStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDatastoreStatus"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html#cfn-healthlake-fhirdatastore-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="datastoreTypeVersion")
    def datastore_type_version(self) -> builtins.str:
        '''The FHIR version of the Data Store.

        The only supported version is R4.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html#cfn-healthlake-fhirdatastore-datastoretypeversion
        '''
        return typing.cast(builtins.str, jsii.get(self, "datastoreTypeVersion"))

    @datastore_type_version.setter
    def datastore_type_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b172e9fff3c5f13a1d7b0c2f836d2a5c200d04c7b8418c86f5e17433d5c48aaf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datastoreTypeVersion", value)

    @builtins.property
    @jsii.member(jsii_name="datastoreName")
    def datastore_name(self) -> typing.Optional[builtins.str]:
        '''The user generated name for the Data Store.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html#cfn-healthlake-fhirdatastore-datastorename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datastoreName"))

    @datastore_name.setter
    def datastore_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3aff9393d89e09b4cd8ead263c89dd18be37ab96cff602cc3f1fc035222c47fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datastoreName", value)

    @builtins.property
    @jsii.member(jsii_name="preloadDataConfig")
    def preload_data_config(
        self,
    ) -> typing.Optional[typing.Union["CfnFHIRDatastore.PreloadDataConfigProperty", _IResolvable_a771d0ef]]:
        '''The preloaded data configuration for the Data Store.

        Only data preloaded from Synthea is supported.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html#cfn-healthlake-fhirdatastore-preloaddataconfig
        '''
        return typing.cast(typing.Optional[typing.Union["CfnFHIRDatastore.PreloadDataConfigProperty", _IResolvable_a771d0ef]], jsii.get(self, "preloadDataConfig"))

    @preload_data_config.setter
    def preload_data_config(
        self,
        value: typing.Optional[typing.Union["CfnFHIRDatastore.PreloadDataConfigProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92b33cf2c0df3d5e09982f5c42a7d44ad3caa405247f751af8461b179f5e527f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preloadDataConfig", value)

    @builtins.property
    @jsii.member(jsii_name="sseConfiguration")
    def sse_configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnFHIRDatastore.SseConfigurationProperty", _IResolvable_a771d0ef]]:
        '''The server-side encryption key configuration for a customer provided encryption key specified for creating a Data Store.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html#cfn-healthlake-fhirdatastore-sseconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union["CfnFHIRDatastore.SseConfigurationProperty", _IResolvable_a771d0ef]], jsii.get(self, "sseConfiguration"))

    @sse_configuration.setter
    def sse_configuration(
        self,
        value: typing.Optional[typing.Union["CfnFHIRDatastore.SseConfigurationProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4fe44f3b3247041536ad17a6884a6c1ce4feba53fbb7c8480875d8e53a4fe3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sseConfiguration", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_healthlake.CfnFHIRDatastore.CreatedAtProperty",
        jsii_struct_bases=[],
        name_mapping={"nanos": "nanos", "seconds": "seconds"},
    )
    class CreatedAtProperty:
        def __init__(self, *, nanos: jsii.Number, seconds: builtins.str) -> None:
            '''
            :param nanos: ``CfnFHIRDatastore.CreatedAtProperty.Nanos``.
            :param seconds: ``CfnFHIRDatastore.CreatedAtProperty.Seconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-createdat.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_healthlake as healthlake
                
                created_at_property = healthlake.CfnFHIRDatastore.CreatedAtProperty(
                    nanos=123,
                    seconds="seconds"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7263b1bece1ee4a6e07cbdafc1aa267514e51d56748bb58bb193a5a445ba08ca)
                check_type(argname="argument nanos", value=nanos, expected_type=type_hints["nanos"])
                check_type(argname="argument seconds", value=seconds, expected_type=type_hints["seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "nanos": nanos,
                "seconds": seconds,
            }

        @builtins.property
        def nanos(self) -> jsii.Number:
            '''``CfnFHIRDatastore.CreatedAtProperty.Nanos``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-createdat.html#cfn-healthlake-fhirdatastore-createdat-nanos
            '''
            result = self._values.get("nanos")
            assert result is not None, "Required property 'nanos' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def seconds(self) -> builtins.str:
            '''``CfnFHIRDatastore.CreatedAtProperty.Seconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-createdat.html#cfn-healthlake-fhirdatastore-createdat-seconds
            '''
            result = self._values.get("seconds")
            assert result is not None, "Required property 'seconds' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CreatedAtProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_healthlake.CfnFHIRDatastore.KmsEncryptionConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"cmk_type": "cmkType", "kms_key_id": "kmsKeyId"},
    )
    class KmsEncryptionConfigProperty:
        def __init__(
            self,
            *,
            cmk_type: builtins.str,
            kms_key_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The customer-managed-key(CMK) used when creating a Data Store.

            If a customer owned key is not specified, an Amazon owned key will be used for encryption.

            :param cmk_type: The type of customer-managed-key(CMK) used for encryption. The two types of supported CMKs are customer owned CMKs and Amazon owned CMKs. For more information on CMK types, see `KmsEncryptionConfig <https://docs.aws.amazon.com/healthlake/latest/APIReference/API_KmsEncryptionConfig.html#HealthLake-Type-KmsEncryptionConfig-CmkType>`_ .
            :param kms_key_id: The KMS encryption key id/alias used to encrypt the Data Store contents at rest.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-kmsencryptionconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_healthlake as healthlake
                
                kms_encryption_config_property = healthlake.CfnFHIRDatastore.KmsEncryptionConfigProperty(
                    cmk_type="cmkType",
                
                    # the properties below are optional
                    kms_key_id="kmsKeyId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e10d20129aa73710fbd3322346464595fa9a3deb67e13b2c1461452ded91d4ee)
                check_type(argname="argument cmk_type", value=cmk_type, expected_type=type_hints["cmk_type"])
                check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cmk_type": cmk_type,
            }
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id

        @builtins.property
        def cmk_type(self) -> builtins.str:
            '''The type of customer-managed-key(CMK) used for encryption.

            The two types of supported CMKs are customer owned CMKs and Amazon owned CMKs. For more information on CMK types, see `KmsEncryptionConfig <https://docs.aws.amazon.com/healthlake/latest/APIReference/API_KmsEncryptionConfig.html#HealthLake-Type-KmsEncryptionConfig-CmkType>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-kmsencryptionconfig.html#cfn-healthlake-fhirdatastore-kmsencryptionconfig-cmktype
            '''
            result = self._values.get("cmk_type")
            assert result is not None, "Required property 'cmk_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''The KMS encryption key id/alias used to encrypt the Data Store contents at rest.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-kmsencryptionconfig.html#cfn-healthlake-fhirdatastore-kmsencryptionconfig-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KmsEncryptionConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_healthlake.CfnFHIRDatastore.PreloadDataConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"preload_data_type": "preloadDataType"},
    )
    class PreloadDataConfigProperty:
        def __init__(self, *, preload_data_type: builtins.str) -> None:
            '''Optional parameter to preload data upon creation of the Data Store.

            Currently, the only supported preloaded data is synthetic data generated from Synthea.

            :param preload_data_type: The type of preloaded data. Only Synthea preloaded data is supported.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-preloaddataconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_healthlake as healthlake
                
                preload_data_config_property = healthlake.CfnFHIRDatastore.PreloadDataConfigProperty(
                    preload_data_type="preloadDataType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2bb9c8be10826ce669ee01513333655f2a7aaaaaa4a1608ac402729187a897b9)
                check_type(argname="argument preload_data_type", value=preload_data_type, expected_type=type_hints["preload_data_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "preload_data_type": preload_data_type,
            }

        @builtins.property
        def preload_data_type(self) -> builtins.str:
            '''The type of preloaded data.

            Only Synthea preloaded data is supported.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-preloaddataconfig.html#cfn-healthlake-fhirdatastore-preloaddataconfig-preloaddatatype
            '''
            result = self._values.get("preload_data_type")
            assert result is not None, "Required property 'preload_data_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PreloadDataConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_healthlake.CfnFHIRDatastore.SseConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"kms_encryption_config": "kmsEncryptionConfig"},
    )
    class SseConfigurationProperty:
        def __init__(
            self,
            *,
            kms_encryption_config: typing.Union[typing.Union["CfnFHIRDatastore.KmsEncryptionConfigProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
        ) -> None:
            '''The server-side encryption key configuration for a customer provided encryption key.

            :param kms_encryption_config: The server-side encryption key configuration for a customer provided encryption key (CMK).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-sseconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_healthlake as healthlake
                
                sse_configuration_property = healthlake.CfnFHIRDatastore.SseConfigurationProperty(
                    kms_encryption_config=healthlake.CfnFHIRDatastore.KmsEncryptionConfigProperty(
                        cmk_type="cmkType",
                
                        # the properties below are optional
                        kms_key_id="kmsKeyId"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__08794ad7842aabd035a5da7f17a5333ae8e0790ed5bcae7b514805ea8594550c)
                check_type(argname="argument kms_encryption_config", value=kms_encryption_config, expected_type=type_hints["kms_encryption_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "kms_encryption_config": kms_encryption_config,
            }

        @builtins.property
        def kms_encryption_config(
            self,
        ) -> typing.Union["CfnFHIRDatastore.KmsEncryptionConfigProperty", _IResolvable_a771d0ef]:
            '''The server-side encryption key configuration for a customer provided encryption key (CMK).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-sseconfiguration.html#cfn-healthlake-fhirdatastore-sseconfiguration-kmsencryptionconfig
            '''
            result = self._values.get("kms_encryption_config")
            assert result is not None, "Required property 'kms_encryption_config' is missing"
            return typing.cast(typing.Union["CfnFHIRDatastore.KmsEncryptionConfigProperty", _IResolvable_a771d0ef], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SseConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_healthlake.CfnFHIRDatastoreProps",
    jsii_struct_bases=[],
    name_mapping={
        "datastore_type_version": "datastoreTypeVersion",
        "datastore_name": "datastoreName",
        "preload_data_config": "preloadDataConfig",
        "sse_configuration": "sseConfiguration",
        "tags": "tags",
    },
)
class CfnFHIRDatastoreProps:
    def __init__(
        self,
        *,
        datastore_type_version: builtins.str,
        datastore_name: typing.Optional[builtins.str] = None,
        preload_data_config: typing.Optional[typing.Union[typing.Union[CfnFHIRDatastore.PreloadDataConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        sse_configuration: typing.Optional[typing.Union[typing.Union[CfnFHIRDatastore.SseConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnFHIRDatastore``.

        :param datastore_type_version: The FHIR version of the Data Store. The only supported version is R4.
        :param datastore_name: The user generated name for the Data Store.
        :param preload_data_config: The preloaded data configuration for the Data Store. Only data preloaded from Synthea is supported.
        :param sse_configuration: The server-side encryption key configuration for a customer provided encryption key specified for creating a Data Store.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_healthlake as healthlake
            
            cfn_fHIRDatastore_props = healthlake.CfnFHIRDatastoreProps(
                datastore_type_version="datastoreTypeVersion",
            
                # the properties below are optional
                datastore_name="datastoreName",
                preload_data_config=healthlake.CfnFHIRDatastore.PreloadDataConfigProperty(
                    preload_data_type="preloadDataType"
                ),
                sse_configuration=healthlake.CfnFHIRDatastore.SseConfigurationProperty(
                    kms_encryption_config=healthlake.CfnFHIRDatastore.KmsEncryptionConfigProperty(
                        cmk_type="cmkType",
            
                        # the properties below are optional
                        kms_key_id="kmsKeyId"
                    )
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__759d60d8fa1d1726896a3a5877d1a33920a9fbe73bda5030ff8990ccf8be9408)
            check_type(argname="argument datastore_type_version", value=datastore_type_version, expected_type=type_hints["datastore_type_version"])
            check_type(argname="argument datastore_name", value=datastore_name, expected_type=type_hints["datastore_name"])
            check_type(argname="argument preload_data_config", value=preload_data_config, expected_type=type_hints["preload_data_config"])
            check_type(argname="argument sse_configuration", value=sse_configuration, expected_type=type_hints["sse_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "datastore_type_version": datastore_type_version,
        }
        if datastore_name is not None:
            self._values["datastore_name"] = datastore_name
        if preload_data_config is not None:
            self._values["preload_data_config"] = preload_data_config
        if sse_configuration is not None:
            self._values["sse_configuration"] = sse_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def datastore_type_version(self) -> builtins.str:
        '''The FHIR version of the Data Store.

        The only supported version is R4.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html#cfn-healthlake-fhirdatastore-datastoretypeversion
        '''
        result = self._values.get("datastore_type_version")
        assert result is not None, "Required property 'datastore_type_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def datastore_name(self) -> typing.Optional[builtins.str]:
        '''The user generated name for the Data Store.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html#cfn-healthlake-fhirdatastore-datastorename
        '''
        result = self._values.get("datastore_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preload_data_config(
        self,
    ) -> typing.Optional[typing.Union[CfnFHIRDatastore.PreloadDataConfigProperty, _IResolvable_a771d0ef]]:
        '''The preloaded data configuration for the Data Store.

        Only data preloaded from Synthea is supported.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html#cfn-healthlake-fhirdatastore-preloaddataconfig
        '''
        result = self._values.get("preload_data_config")
        return typing.cast(typing.Optional[typing.Union[CfnFHIRDatastore.PreloadDataConfigProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def sse_configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnFHIRDatastore.SseConfigurationProperty, _IResolvable_a771d0ef]]:
        '''The server-side encryption key configuration for a customer provided encryption key specified for creating a Data Store.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html#cfn-healthlake-fhirdatastore-sseconfiguration
        '''
        result = self._values.get("sse_configuration")
        return typing.cast(typing.Optional[typing.Union[CfnFHIRDatastore.SseConfigurationProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html#cfn-healthlake-fhirdatastore-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFHIRDatastoreProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnFHIRDatastore",
    "CfnFHIRDatastoreProps",
]

publication.publish()

def _typecheckingstub__3ed946fd406aad2d2ef0dc31315b9021260e8654b17cec3b564ce004e56dd5ef(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    datastore_type_version: builtins.str,
    datastore_name: typing.Optional[builtins.str] = None,
    preload_data_config: typing.Optional[typing.Union[typing.Union[CfnFHIRDatastore.PreloadDataConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    sse_configuration: typing.Optional[typing.Union[typing.Union[CfnFHIRDatastore.SseConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83078627fd9ede8075f74cfdeb6b001ed3bd6b361f35b33e967b4a113824ab18(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f5515fd07c10e77b898260ef3a4954b4e64ebf02e9856f0c36438192d4b0e11(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b172e9fff3c5f13a1d7b0c2f836d2a5c200d04c7b8418c86f5e17433d5c48aaf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3aff9393d89e09b4cd8ead263c89dd18be37ab96cff602cc3f1fc035222c47fe(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92b33cf2c0df3d5e09982f5c42a7d44ad3caa405247f751af8461b179f5e527f(
    value: typing.Optional[typing.Union[CfnFHIRDatastore.PreloadDataConfigProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4fe44f3b3247041536ad17a6884a6c1ce4feba53fbb7c8480875d8e53a4fe3f(
    value: typing.Optional[typing.Union[CfnFHIRDatastore.SseConfigurationProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7263b1bece1ee4a6e07cbdafc1aa267514e51d56748bb58bb193a5a445ba08ca(
    *,
    nanos: jsii.Number,
    seconds: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e10d20129aa73710fbd3322346464595fa9a3deb67e13b2c1461452ded91d4ee(
    *,
    cmk_type: builtins.str,
    kms_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bb9c8be10826ce669ee01513333655f2a7aaaaaa4a1608ac402729187a897b9(
    *,
    preload_data_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08794ad7842aabd035a5da7f17a5333ae8e0790ed5bcae7b514805ea8594550c(
    *,
    kms_encryption_config: typing.Union[typing.Union[CfnFHIRDatastore.KmsEncryptionConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__759d60d8fa1d1726896a3a5877d1a33920a9fbe73bda5030ff8990ccf8be9408(
    *,
    datastore_type_version: builtins.str,
    datastore_name: typing.Optional[builtins.str] = None,
    preload_data_config: typing.Optional[typing.Union[typing.Union[CfnFHIRDatastore.PreloadDataConfigProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    sse_configuration: typing.Optional[typing.Union[typing.Union[CfnFHIRDatastore.SseConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

'''
# Amazon Pinpoint Email Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import monocdk as pinpointemail
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for PinpointEmail construct libraries](https://constructs.dev/search?q=pinpointemail)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::PinpointEmail resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_PinpointEmail.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::PinpointEmail](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_PinpointEmail.html).

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
    TreeInspector as _TreeInspector_1cd1894e,
)


@jsii.implements(_IInspectable_82c04a63)
class CfnConfigurationSet(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_pinpointemail.CfnConfigurationSet",
):
    '''A CloudFormation ``AWS::PinpointEmail::ConfigurationSet``.

    Create a configuration set. *Configuration sets* are groups of rules that you can apply to the emails you send using Amazon Pinpoint. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.

    :cloudformationResource: AWS::PinpointEmail::ConfigurationSet
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_pinpointemail as pinpointemail
        
        cfn_configuration_set = pinpointemail.CfnConfigurationSet(self, "MyCfnConfigurationSet",
            name="name",
        
            # the properties below are optional
            delivery_options=pinpointemail.CfnConfigurationSet.DeliveryOptionsProperty(
                sending_pool_name="sendingPoolName"
            ),
            reputation_options=pinpointemail.CfnConfigurationSet.ReputationOptionsProperty(
                reputation_metrics_enabled=False
            ),
            sending_options=pinpointemail.CfnConfigurationSet.SendingOptionsProperty(
                sending_enabled=False
            ),
            tags=[pinpointemail.CfnConfigurationSet.TagsProperty(
                key="key",
                value="value"
            )],
            tracking_options=pinpointemail.CfnConfigurationSet.TrackingOptionsProperty(
                custom_redirect_domain="customRedirectDomain"
            )
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        name: builtins.str,
        delivery_options: typing.Optional[typing.Union[typing.Union["CfnConfigurationSet.DeliveryOptionsProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        reputation_options: typing.Optional[typing.Union[typing.Union["CfnConfigurationSet.ReputationOptionsProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        sending_options: typing.Optional[typing.Union[typing.Union["CfnConfigurationSet.SendingOptionsProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["CfnConfigurationSet.TagsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tracking_options: typing.Optional[typing.Union[typing.Union["CfnConfigurationSet.TrackingOptionsProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    ) -> None:
        '''Create a new ``AWS::PinpointEmail::ConfigurationSet``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: The name of the configuration set.
        :param delivery_options: An object that defines the dedicated IP pool that is used to send emails that you send using the configuration set.
        :param reputation_options: An object that defines whether or not Amazon Pinpoint collects reputation metrics for the emails that you send that use the configuration set.
        :param sending_options: An object that defines whether or not Amazon Pinpoint can send email that you send using the configuration set.
        :param tags: An object that defines the tags (keys and values) that you want to associate with the configuration set.
        :param tracking_options: An object that defines the open and click tracking options for emails that you send using the configuration set.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5883984ad1311cfaaf11ca8eab556aea2cf6417079aae0293b66006d89162f3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConfigurationSetProps(
            name=name,
            delivery_options=delivery_options,
            reputation_options=reputation_options,
            sending_options=sending_options,
            tags=tags,
            tracking_options=tracking_options,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__edbbea0488801ae94a320fe0688143e4a2f6f27d1cb3b41693f28179e1114d76)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d4d2595ff4a49482ec1bbc2cd37d1810924e89d89fddf0e1786b30a17659d7e6)
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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the configuration set.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46ae6e64a9112029d6104c7e2d44f99abd4f04b13e589b8b35b1bfb59a933516)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="deliveryOptions")
    def delivery_options(
        self,
    ) -> typing.Optional[typing.Union["CfnConfigurationSet.DeliveryOptionsProperty", _IResolvable_a771d0ef]]:
        '''An object that defines the dedicated IP pool that is used to send emails that you send using the configuration set.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-deliveryoptions
        '''
        return typing.cast(typing.Optional[typing.Union["CfnConfigurationSet.DeliveryOptionsProperty", _IResolvable_a771d0ef]], jsii.get(self, "deliveryOptions"))

    @delivery_options.setter
    def delivery_options(
        self,
        value: typing.Optional[typing.Union["CfnConfigurationSet.DeliveryOptionsProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3f8ae9976e159a1718067d389fbe3706f5026445e046740aa56237c5fdcf3d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deliveryOptions", value)

    @builtins.property
    @jsii.member(jsii_name="reputationOptions")
    def reputation_options(
        self,
    ) -> typing.Optional[typing.Union["CfnConfigurationSet.ReputationOptionsProperty", _IResolvable_a771d0ef]]:
        '''An object that defines whether or not Amazon Pinpoint collects reputation metrics for the emails that you send that use the configuration set.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-reputationoptions
        '''
        return typing.cast(typing.Optional[typing.Union["CfnConfigurationSet.ReputationOptionsProperty", _IResolvable_a771d0ef]], jsii.get(self, "reputationOptions"))

    @reputation_options.setter
    def reputation_options(
        self,
        value: typing.Optional[typing.Union["CfnConfigurationSet.ReputationOptionsProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58062a827573a7a7d37efc3419487bc882f5948ef28063ae422431568d46dfa9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reputationOptions", value)

    @builtins.property
    @jsii.member(jsii_name="sendingOptions")
    def sending_options(
        self,
    ) -> typing.Optional[typing.Union["CfnConfigurationSet.SendingOptionsProperty", _IResolvable_a771d0ef]]:
        '''An object that defines whether or not Amazon Pinpoint can send email that you send using the configuration set.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-sendingoptions
        '''
        return typing.cast(typing.Optional[typing.Union["CfnConfigurationSet.SendingOptionsProperty", _IResolvable_a771d0ef]], jsii.get(self, "sendingOptions"))

    @sending_options.setter
    def sending_options(
        self,
        value: typing.Optional[typing.Union["CfnConfigurationSet.SendingOptionsProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41313e55c12723a640d803f32b0530f5cf4e5504d33326f1c04888ea04ea8d41)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sendingOptions", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["CfnConfigurationSet.TagsProperty"]]:
        '''An object that defines the tags (keys and values) that you want to associate with the configuration set.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-tags
        '''
        return typing.cast(typing.Optional[typing.List["CfnConfigurationSet.TagsProperty"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["CfnConfigurationSet.TagsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf6015ba5151acadc0a23718a33a6426172e90a45fcd25cb6c48c055e9d5fd0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="trackingOptions")
    def tracking_options(
        self,
    ) -> typing.Optional[typing.Union["CfnConfigurationSet.TrackingOptionsProperty", _IResolvable_a771d0ef]]:
        '''An object that defines the open and click tracking options for emails that you send using the configuration set.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-trackingoptions
        '''
        return typing.cast(typing.Optional[typing.Union["CfnConfigurationSet.TrackingOptionsProperty", _IResolvable_a771d0ef]], jsii.get(self, "trackingOptions"))

    @tracking_options.setter
    def tracking_options(
        self,
        value: typing.Optional[typing.Union["CfnConfigurationSet.TrackingOptionsProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4185429bcdb088868cff68b4000b94487aa64d1d047ba1599d58c6384c8fa3d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trackingOptions", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_pinpointemail.CfnConfigurationSet.DeliveryOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"sending_pool_name": "sendingPoolName"},
    )
    class DeliveryOptionsProperty:
        def __init__(
            self,
            *,
            sending_pool_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Used to associate a configuration set with a dedicated IP pool.

            :param sending_pool_name: The name of the dedicated IP pool that you want to associate with the configuration set.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-deliveryoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_pinpointemail as pinpointemail
                
                delivery_options_property = pinpointemail.CfnConfigurationSet.DeliveryOptionsProperty(
                    sending_pool_name="sendingPoolName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__85368c0a3518fb63084683c62965c534cb6a7eb3579edb161fabf12a98f94138)
                check_type(argname="argument sending_pool_name", value=sending_pool_name, expected_type=type_hints["sending_pool_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if sending_pool_name is not None:
                self._values["sending_pool_name"] = sending_pool_name

        @builtins.property
        def sending_pool_name(self) -> typing.Optional[builtins.str]:
            '''The name of the dedicated IP pool that you want to associate with the configuration set.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-deliveryoptions.html#cfn-pinpointemail-configurationset-deliveryoptions-sendingpoolname
            '''
            result = self._values.get("sending_pool_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeliveryOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_pinpointemail.CfnConfigurationSet.ReputationOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"reputation_metrics_enabled": "reputationMetricsEnabled"},
    )
    class ReputationOptionsProperty:
        def __init__(
            self,
            *,
            reputation_metrics_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''Enable or disable collection of reputation metrics for emails that you send using this configuration set in the current AWS Region.

            :param reputation_metrics_enabled: If ``true`` , tracking of reputation metrics is enabled for the configuration set. If ``false`` , tracking of reputation metrics is disabled for the configuration set.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-reputationoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_pinpointemail as pinpointemail
                
                reputation_options_property = pinpointemail.CfnConfigurationSet.ReputationOptionsProperty(
                    reputation_metrics_enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f045ad54d73f019d4dfb939078b0858000c7555ff7d386313d49a3d546712d15)
                check_type(argname="argument reputation_metrics_enabled", value=reputation_metrics_enabled, expected_type=type_hints["reputation_metrics_enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if reputation_metrics_enabled is not None:
                self._values["reputation_metrics_enabled"] = reputation_metrics_enabled

        @builtins.property
        def reputation_metrics_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''If ``true`` , tracking of reputation metrics is enabled for the configuration set.

            If ``false`` , tracking of reputation metrics is disabled for the configuration set.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-reputationoptions.html#cfn-pinpointemail-configurationset-reputationoptions-reputationmetricsenabled
            '''
            result = self._values.get("reputation_metrics_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ReputationOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_pinpointemail.CfnConfigurationSet.SendingOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"sending_enabled": "sendingEnabled"},
    )
    class SendingOptionsProperty:
        def __init__(
            self,
            *,
            sending_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''Used to enable or disable email sending for messages that use this configuration set in the current AWS Region.

            :param sending_enabled: If ``true`` , email sending is enabled for the configuration set. If ``false`` , email sending is disabled for the configuration set.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-sendingoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_pinpointemail as pinpointemail
                
                sending_options_property = pinpointemail.CfnConfigurationSet.SendingOptionsProperty(
                    sending_enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6f170319e613e4a4463d75ba5083b6022a1910366e198e5db04e659f0f4519f2)
                check_type(argname="argument sending_enabled", value=sending_enabled, expected_type=type_hints["sending_enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if sending_enabled is not None:
                self._values["sending_enabled"] = sending_enabled

        @builtins.property
        def sending_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''If ``true`` , email sending is enabled for the configuration set.

            If ``false`` , email sending is disabled for the configuration set.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-sendingoptions.html#cfn-pinpointemail-configurationset-sendingoptions-sendingenabled
            '''
            result = self._values.get("sending_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SendingOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_pinpointemail.CfnConfigurationSet.TagsProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class TagsProperty:
        def __init__(
            self,
            *,
            key: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An object that defines the tags (keys and values) that you want to associate with the configuration set.

            :param key: One part of a key-value pair that defines a tag. The maximum length of a tag key is 128 characters. The minimum length is 1 character. If you specify tags for the configuration set, then this value is required.
            :param value: The optional part of a key-value pair that defines a tag. The maximum length of a tag value is 256 characters. The minimum length is 0 characters. If you don’t want a resource to have a specific tag value, don’t specify a value for this parameter. Amazon Pinpoint will set the value to an empty string.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-tags.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_pinpointemail as pinpointemail
                
                tags_property = pinpointemail.CfnConfigurationSet.TagsProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fb578541f03a4950372f080fb23ee50c1c40012f032c3205fbb9162f1ede11a5)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if key is not None:
                self._values["key"] = key
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''One part of a key-value pair that defines a tag.

            The maximum length of a tag key is 128 characters. The minimum length is 1 character.

            If you specify tags for the configuration set, then this value is required.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-tags.html#cfn-pinpointemail-configurationset-tags-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The optional part of a key-value pair that defines a tag.

            The maximum length of a tag value is 256 characters. The minimum length is 0 characters. If you don’t want a resource to have a specific tag value, don’t specify a value for this parameter. Amazon Pinpoint will set the value to an empty string.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-tags.html#cfn-pinpointemail-configurationset-tags-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TagsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_pinpointemail.CfnConfigurationSet.TrackingOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"custom_redirect_domain": "customRedirectDomain"},
    )
    class TrackingOptionsProperty:
        def __init__(
            self,
            *,
            custom_redirect_domain: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An object that defines the tracking options for a configuration set.

            When you use Amazon Pinpoint to send an email, it contains an invisible image that's used to track when recipients open your email. If your email contains links, those links are changed slightly in order to track when recipients click them.

            These images and links include references to a domain operated by AWS . You can optionally configure Amazon Pinpoint to use a domain that you operate for these images and links.

            :param custom_redirect_domain: The domain that you want to use for tracking open and click events.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-trackingoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_pinpointemail as pinpointemail
                
                tracking_options_property = pinpointemail.CfnConfigurationSet.TrackingOptionsProperty(
                    custom_redirect_domain="customRedirectDomain"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5b9bc02c2421fe8f95d3ee4d2d0d4e5a1f4115bd947559b88b2b2418af240d91)
                check_type(argname="argument custom_redirect_domain", value=custom_redirect_domain, expected_type=type_hints["custom_redirect_domain"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if custom_redirect_domain is not None:
                self._values["custom_redirect_domain"] = custom_redirect_domain

        @builtins.property
        def custom_redirect_domain(self) -> typing.Optional[builtins.str]:
            '''The domain that you want to use for tracking open and click events.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-trackingoptions.html#cfn-pinpointemail-configurationset-trackingoptions-customredirectdomain
            '''
            result = self._values.get("custom_redirect_domain")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TrackingOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_82c04a63)
class CfnConfigurationSetEventDestination(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_pinpointemail.CfnConfigurationSetEventDestination",
):
    '''A CloudFormation ``AWS::PinpointEmail::ConfigurationSetEventDestination``.

    Create an event destination. In Amazon Pinpoint, *events* include message sends, deliveries, opens, clicks, bounces, and complaints. *Event destinations* are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.

    A single configuration set can include more than one event destination.

    :cloudformationResource: AWS::PinpointEmail::ConfigurationSetEventDestination
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationseteventdestination.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_pinpointemail as pinpointemail
        
        cfn_configuration_set_event_destination = pinpointemail.CfnConfigurationSetEventDestination(self, "MyCfnConfigurationSetEventDestination",
            configuration_set_name="configurationSetName",
            event_destination_name="eventDestinationName",
        
            # the properties below are optional
            event_destination=pinpointemail.CfnConfigurationSetEventDestination.EventDestinationProperty(
                matching_event_types=["matchingEventTypes"],
        
                # the properties below are optional
                cloud_watch_destination=pinpointemail.CfnConfigurationSetEventDestination.CloudWatchDestinationProperty(
                    dimension_configurations=[pinpointemail.CfnConfigurationSetEventDestination.DimensionConfigurationProperty(
                        default_dimension_value="defaultDimensionValue",
                        dimension_name="dimensionName",
                        dimension_value_source="dimensionValueSource"
                    )]
                ),
                enabled=False,
                kinesis_firehose_destination=pinpointemail.CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty(
                    delivery_stream_arn="deliveryStreamArn",
                    iam_role_arn="iamRoleArn"
                ),
                pinpoint_destination=pinpointemail.CfnConfigurationSetEventDestination.PinpointDestinationProperty(
                    application_arn="applicationArn"
                ),
                sns_destination=pinpointemail.CfnConfigurationSetEventDestination.SnsDestinationProperty(
                    topic_arn="topicArn"
                )
            )
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        configuration_set_name: builtins.str,
        event_destination_name: builtins.str,
        event_destination: typing.Optional[typing.Union[typing.Union["CfnConfigurationSetEventDestination.EventDestinationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    ) -> None:
        '''Create a new ``AWS::PinpointEmail::ConfigurationSetEventDestination``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param configuration_set_name: The name of the configuration set that contains the event destination that you want to modify.
        :param event_destination_name: The name of the event destination that you want to modify.
        :param event_destination: An object that defines the event destination.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__668889263897a93ec423752b155e3dc053b532cb62492ee997b17012dbe50275)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConfigurationSetEventDestinationProps(
            configuration_set_name=configuration_set_name,
            event_destination_name=event_destination_name,
            event_destination=event_destination,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bb1fe42f16de7b64973f77328910cb24af889d1443b71edcd1eb17d816a0208)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8cbd7b5e8bb24c3eda55739763cb80a43801f81f59c3c79ff30643e6652278c0)
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
    @jsii.member(jsii_name="configurationSetName")
    def configuration_set_name(self) -> builtins.str:
        '''The name of the configuration set that contains the event destination that you want to modify.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationseteventdestination.html#cfn-pinpointemail-configurationseteventdestination-configurationsetname
        '''
        return typing.cast(builtins.str, jsii.get(self, "configurationSetName"))

    @configuration_set_name.setter
    def configuration_set_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1fa282673be7fa6e73bb208564d2f665ec36b0f05227c36f64a9e00f3bc8cb9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurationSetName", value)

    @builtins.property
    @jsii.member(jsii_name="eventDestinationName")
    def event_destination_name(self) -> builtins.str:
        '''The name of the event destination that you want to modify.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationseteventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestinationname
        '''
        return typing.cast(builtins.str, jsii.get(self, "eventDestinationName"))

    @event_destination_name.setter
    def event_destination_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__629c691eb16c379b2687b88ad1ec9fd3267b3a897da44e9622f58dd967f258d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventDestinationName", value)

    @builtins.property
    @jsii.member(jsii_name="eventDestination")
    def event_destination(
        self,
    ) -> typing.Optional[typing.Union["CfnConfigurationSetEventDestination.EventDestinationProperty", _IResolvable_a771d0ef]]:
        '''An object that defines the event destination.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationseteventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestination
        '''
        return typing.cast(typing.Optional[typing.Union["CfnConfigurationSetEventDestination.EventDestinationProperty", _IResolvable_a771d0ef]], jsii.get(self, "eventDestination"))

    @event_destination.setter
    def event_destination(
        self,
        value: typing.Optional[typing.Union["CfnConfigurationSetEventDestination.EventDestinationProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca5c8de21ccb88a79cae28aed8e98eee72a11c7f79eb758635ae7499a1541e0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventDestination", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_pinpointemail.CfnConfigurationSetEventDestination.CloudWatchDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"dimension_configurations": "dimensionConfigurations"},
    )
    class CloudWatchDestinationProperty:
        def __init__(
            self,
            *,
            dimension_configurations: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union["CfnConfigurationSetEventDestination.DimensionConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]]] = None,
        ) -> None:
            '''An object that defines an Amazon CloudWatch destination for email events.

            You can use Amazon CloudWatch to monitor and gain insights on your email sending metrics.

            :param dimension_configurations: An array of objects that define the dimensions to use when you send email events to Amazon CloudWatch.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-cloudwatchdestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_pinpointemail as pinpointemail
                
                cloud_watch_destination_property = pinpointemail.CfnConfigurationSetEventDestination.CloudWatchDestinationProperty(
                    dimension_configurations=[pinpointemail.CfnConfigurationSetEventDestination.DimensionConfigurationProperty(
                        default_dimension_value="defaultDimensionValue",
                        dimension_name="dimensionName",
                        dimension_value_source="dimensionValueSource"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__30f57a46a6936dd157c9116b7b0f38dfa216dc4838db5143b9c41378d0810e9e)
                check_type(argname="argument dimension_configurations", value=dimension_configurations, expected_type=type_hints["dimension_configurations"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if dimension_configurations is not None:
                self._values["dimension_configurations"] = dimension_configurations

        @builtins.property
        def dimension_configurations(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnConfigurationSetEventDestination.DimensionConfigurationProperty", _IResolvable_a771d0ef]]]]:
            '''An array of objects that define the dimensions to use when you send email events to Amazon CloudWatch.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-cloudwatchdestination.html#cfn-pinpointemail-configurationseteventdestination-cloudwatchdestination-dimensionconfigurations
            '''
            result = self._values.get("dimension_configurations")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnConfigurationSetEventDestination.DimensionConfigurationProperty", _IResolvable_a771d0ef]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_pinpointemail.CfnConfigurationSetEventDestination.DimensionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "default_dimension_value": "defaultDimensionValue",
            "dimension_name": "dimensionName",
            "dimension_value_source": "dimensionValueSource",
        },
    )
    class DimensionConfigurationProperty:
        def __init__(
            self,
            *,
            default_dimension_value: builtins.str,
            dimension_name: builtins.str,
            dimension_value_source: builtins.str,
        ) -> None:
            '''An array of objects that define the dimensions to use when you send email events to Amazon CloudWatch.

            :param default_dimension_value: The default value of the dimension that is published to Amazon CloudWatch if you don't provide the value of the dimension when you send an email. This value has to meet the following criteria: - It can only contain ASCII letters (a–z, A–Z), numbers (0–9), underscores (_), or dashes (-). - It can contain no more than 256 characters.
            :param dimension_name: The name of an Amazon CloudWatch dimension associated with an email sending metric. The name has to meet the following criteria: - It can only contain ASCII letters (a–z, A–Z), numbers (0–9), underscores (_), or dashes (-). - It can contain no more than 256 characters.
            :param dimension_value_source: The location where Amazon Pinpoint finds the value of a dimension to publish to Amazon CloudWatch. Acceptable values: ``MESSAGE_TAG`` , ``EMAIL_HEADER`` , and ``LINK_TAG`` . If you want Amazon Pinpoint to use the message tags that you specify using an ``X-SES-MESSAGE-TAGS`` header or a parameter to the ``SendEmail`` API, choose ``MESSAGE_TAG`` . If you want Amazon Pinpoint to use your own email headers, choose ``EMAIL_HEADER`` . If you want Amazon Pinpoint to use tags that are specified in your links, choose ``LINK_TAG`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-dimensionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_pinpointemail as pinpointemail
                
                dimension_configuration_property = pinpointemail.CfnConfigurationSetEventDestination.DimensionConfigurationProperty(
                    default_dimension_value="defaultDimensionValue",
                    dimension_name="dimensionName",
                    dimension_value_source="dimensionValueSource"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__55e140348608c6e3e976c689bd3233cea7d8a4e18deab1a65b454feee08562da)
                check_type(argname="argument default_dimension_value", value=default_dimension_value, expected_type=type_hints["default_dimension_value"])
                check_type(argname="argument dimension_name", value=dimension_name, expected_type=type_hints["dimension_name"])
                check_type(argname="argument dimension_value_source", value=dimension_value_source, expected_type=type_hints["dimension_value_source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "default_dimension_value": default_dimension_value,
                "dimension_name": dimension_name,
                "dimension_value_source": dimension_value_source,
            }

        @builtins.property
        def default_dimension_value(self) -> builtins.str:
            '''The default value of the dimension that is published to Amazon CloudWatch if you don't provide the value of the dimension when you send an email.

            This value has to meet the following criteria:

            - It can only contain ASCII letters (a–z, A–Z), numbers (0–9), underscores (_), or dashes (-).
            - It can contain no more than 256 characters.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-dimensionconfiguration.html#cfn-pinpointemail-configurationseteventdestination-dimensionconfiguration-defaultdimensionvalue
            '''
            result = self._values.get("default_dimension_value")
            assert result is not None, "Required property 'default_dimension_value' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def dimension_name(self) -> builtins.str:
            '''The name of an Amazon CloudWatch dimension associated with an email sending metric.

            The name has to meet the following criteria:

            - It can only contain ASCII letters (a–z, A–Z), numbers (0–9), underscores (_), or dashes (-).
            - It can contain no more than 256 characters.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-dimensionconfiguration.html#cfn-pinpointemail-configurationseteventdestination-dimensionconfiguration-dimensionname
            '''
            result = self._values.get("dimension_name")
            assert result is not None, "Required property 'dimension_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def dimension_value_source(self) -> builtins.str:
            '''The location where Amazon Pinpoint finds the value of a dimension to publish to Amazon CloudWatch.

            Acceptable values: ``MESSAGE_TAG`` , ``EMAIL_HEADER`` , and ``LINK_TAG`` .

            If you want Amazon Pinpoint to use the message tags that you specify using an ``X-SES-MESSAGE-TAGS`` header or a parameter to the ``SendEmail`` API, choose ``MESSAGE_TAG`` . If you want Amazon Pinpoint to use your own email headers, choose ``EMAIL_HEADER`` . If you want Amazon Pinpoint to use tags that are specified in your links, choose ``LINK_TAG`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-dimensionconfiguration.html#cfn-pinpointemail-configurationseteventdestination-dimensionconfiguration-dimensionvaluesource
            '''
            result = self._values.get("dimension_value_source")
            assert result is not None, "Required property 'dimension_value_source' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DimensionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_pinpointemail.CfnConfigurationSetEventDestination.EventDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "matching_event_types": "matchingEventTypes",
            "cloud_watch_destination": "cloudWatchDestination",
            "enabled": "enabled",
            "kinesis_firehose_destination": "kinesisFirehoseDestination",
            "pinpoint_destination": "pinpointDestination",
            "sns_destination": "snsDestination",
        },
    )
    class EventDestinationProperty:
        def __init__(
            self,
            *,
            matching_event_types: typing.Sequence[builtins.str],
            cloud_watch_destination: typing.Optional[typing.Union[typing.Union["CfnConfigurationSetEventDestination.CloudWatchDestinationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            kinesis_firehose_destination: typing.Optional[typing.Union[typing.Union["CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            pinpoint_destination: typing.Optional[typing.Union[typing.Union["CfnConfigurationSetEventDestination.PinpointDestinationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
            sns_destination: typing.Optional[typing.Union[typing.Union["CfnConfigurationSetEventDestination.SnsDestinationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        ) -> None:
            '''In Amazon Pinpoint, *events* include message sends, deliveries, opens, clicks, bounces, and complaints.

            *Event destinations* are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.

            :param matching_event_types: The types of events that Amazon Pinpoint sends to the specified event destinations. Acceptable values: ``SEND`` , ``REJECT`` , ``BOUNCE`` , ``COMPLAINT`` , ``DELIVERY`` , ``OPEN`` , ``CLICK`` , and ``RENDERING_FAILURE`` .
            :param cloud_watch_destination: An object that defines an Amazon CloudWatch destination for email events. You can use Amazon CloudWatch to monitor and gain insights on your email sending metrics.
            :param enabled: If ``true`` , the event destination is enabled. When the event destination is enabled, the specified event types are sent to the destinations in this ``EventDestinationDefinition`` . If ``false`` , the event destination is disabled. When the event destination is disabled, events aren't sent to the specified destinations.
            :param kinesis_firehose_destination: An object that defines an Amazon Kinesis Data Firehose destination for email events. You can use Amazon Kinesis Data Firehose to stream data to other services, such as Amazon S3 and Amazon Redshift.
            :param pinpoint_destination: An object that defines a Amazon Pinpoint destination for email events. You can use Amazon Pinpoint events to create attributes in Amazon Pinpoint projects. You can use these attributes to create segments for your campaigns.
            :param sns_destination: An object that defines an Amazon SNS destination for email events. You can use Amazon SNS to send notification when certain email events occur.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-eventdestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_pinpointemail as pinpointemail
                
                event_destination_property = pinpointemail.CfnConfigurationSetEventDestination.EventDestinationProperty(
                    matching_event_types=["matchingEventTypes"],
                
                    # the properties below are optional
                    cloud_watch_destination=pinpointemail.CfnConfigurationSetEventDestination.CloudWatchDestinationProperty(
                        dimension_configurations=[pinpointemail.CfnConfigurationSetEventDestination.DimensionConfigurationProperty(
                            default_dimension_value="defaultDimensionValue",
                            dimension_name="dimensionName",
                            dimension_value_source="dimensionValueSource"
                        )]
                    ),
                    enabled=False,
                    kinesis_firehose_destination=pinpointemail.CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty(
                        delivery_stream_arn="deliveryStreamArn",
                        iam_role_arn="iamRoleArn"
                    ),
                    pinpoint_destination=pinpointemail.CfnConfigurationSetEventDestination.PinpointDestinationProperty(
                        application_arn="applicationArn"
                    ),
                    sns_destination=pinpointemail.CfnConfigurationSetEventDestination.SnsDestinationProperty(
                        topic_arn="topicArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4a0737de3768b00466a794fed26a8edc22b104bac27eb101fd6ca045a92f6374)
                check_type(argname="argument matching_event_types", value=matching_event_types, expected_type=type_hints["matching_event_types"])
                check_type(argname="argument cloud_watch_destination", value=cloud_watch_destination, expected_type=type_hints["cloud_watch_destination"])
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument kinesis_firehose_destination", value=kinesis_firehose_destination, expected_type=type_hints["kinesis_firehose_destination"])
                check_type(argname="argument pinpoint_destination", value=pinpoint_destination, expected_type=type_hints["pinpoint_destination"])
                check_type(argname="argument sns_destination", value=sns_destination, expected_type=type_hints["sns_destination"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "matching_event_types": matching_event_types,
            }
            if cloud_watch_destination is not None:
                self._values["cloud_watch_destination"] = cloud_watch_destination
            if enabled is not None:
                self._values["enabled"] = enabled
            if kinesis_firehose_destination is not None:
                self._values["kinesis_firehose_destination"] = kinesis_firehose_destination
            if pinpoint_destination is not None:
                self._values["pinpoint_destination"] = pinpoint_destination
            if sns_destination is not None:
                self._values["sns_destination"] = sns_destination

        @builtins.property
        def matching_event_types(self) -> typing.List[builtins.str]:
            '''The types of events that Amazon Pinpoint sends to the specified event destinations.

            Acceptable values: ``SEND`` , ``REJECT`` , ``BOUNCE`` , ``COMPLAINT`` , ``DELIVERY`` , ``OPEN`` , ``CLICK`` , and ``RENDERING_FAILURE`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-eventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestination-matchingeventtypes
            '''
            result = self._values.get("matching_event_types")
            assert result is not None, "Required property 'matching_event_types' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def cloud_watch_destination(
            self,
        ) -> typing.Optional[typing.Union["CfnConfigurationSetEventDestination.CloudWatchDestinationProperty", _IResolvable_a771d0ef]]:
            '''An object that defines an Amazon CloudWatch destination for email events.

            You can use Amazon CloudWatch to monitor and gain insights on your email sending metrics.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-eventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestination-cloudwatchdestination
            '''
            result = self._values.get("cloud_watch_destination")
            return typing.cast(typing.Optional[typing.Union["CfnConfigurationSetEventDestination.CloudWatchDestinationProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            '''If ``true`` , the event destination is enabled.

            When the event destination is enabled, the specified event types are sent to the destinations in this ``EventDestinationDefinition`` .

            If ``false`` , the event destination is disabled. When the event destination is disabled, events aren't sent to the specified destinations.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-eventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestination-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

        @builtins.property
        def kinesis_firehose_destination(
            self,
        ) -> typing.Optional[typing.Union["CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty", _IResolvable_a771d0ef]]:
            '''An object that defines an Amazon Kinesis Data Firehose destination for email events.

            You can use Amazon Kinesis Data Firehose to stream data to other services, such as Amazon S3 and Amazon Redshift.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-eventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestination-kinesisfirehosedestination
            '''
            result = self._values.get("kinesis_firehose_destination")
            return typing.cast(typing.Optional[typing.Union["CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def pinpoint_destination(
            self,
        ) -> typing.Optional[typing.Union["CfnConfigurationSetEventDestination.PinpointDestinationProperty", _IResolvable_a771d0ef]]:
            '''An object that defines a Amazon Pinpoint destination for email events.

            You can use Amazon Pinpoint events to create attributes in Amazon Pinpoint projects. You can use these attributes to create segments for your campaigns.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-eventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestination-pinpointdestination
            '''
            result = self._values.get("pinpoint_destination")
            return typing.cast(typing.Optional[typing.Union["CfnConfigurationSetEventDestination.PinpointDestinationProperty", _IResolvable_a771d0ef]], result)

        @builtins.property
        def sns_destination(
            self,
        ) -> typing.Optional[typing.Union["CfnConfigurationSetEventDestination.SnsDestinationProperty", _IResolvable_a771d0ef]]:
            '''An object that defines an Amazon SNS destination for email events.

            You can use Amazon SNS to send notification when certain email events occur.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-eventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestination-snsdestination
            '''
            result = self._values.get("sns_destination")
            return typing.cast(typing.Optional[typing.Union["CfnConfigurationSetEventDestination.SnsDestinationProperty", _IResolvable_a771d0ef]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_pinpointemail.CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "delivery_stream_arn": "deliveryStreamArn",
            "iam_role_arn": "iamRoleArn",
        },
    )
    class KinesisFirehoseDestinationProperty:
        def __init__(
            self,
            *,
            delivery_stream_arn: builtins.str,
            iam_role_arn: builtins.str,
        ) -> None:
            '''An object that defines an Amazon Kinesis Data Firehose destination for email events.

            You can use Amazon Kinesis Data Firehose to stream data to other services, such as Amazon S3 and Amazon Redshift.

            :param delivery_stream_arn: The Amazon Resource Name (ARN) of the Amazon Kinesis Data Firehose stream that Amazon Pinpoint sends email events to.
            :param iam_role_arn: The Amazon Resource Name (ARN) of the IAM role that Amazon Pinpoint uses when sending email events to the Amazon Kinesis Data Firehose stream.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-kinesisfirehosedestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_pinpointemail as pinpointemail
                
                kinesis_firehose_destination_property = pinpointemail.CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty(
                    delivery_stream_arn="deliveryStreamArn",
                    iam_role_arn="iamRoleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2710a1086c0e2b3f9dca03f3cfa46cad723658e2541acea93b98a960f57844cf)
                check_type(argname="argument delivery_stream_arn", value=delivery_stream_arn, expected_type=type_hints["delivery_stream_arn"])
                check_type(argname="argument iam_role_arn", value=iam_role_arn, expected_type=type_hints["iam_role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "delivery_stream_arn": delivery_stream_arn,
                "iam_role_arn": iam_role_arn,
            }

        @builtins.property
        def delivery_stream_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the Amazon Kinesis Data Firehose stream that Amazon Pinpoint sends email events to.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-kinesisfirehosedestination.html#cfn-pinpointemail-configurationseteventdestination-kinesisfirehosedestination-deliverystreamarn
            '''
            result = self._values.get("delivery_stream_arn")
            assert result is not None, "Required property 'delivery_stream_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def iam_role_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the IAM role that Amazon Pinpoint uses when sending email events to the Amazon Kinesis Data Firehose stream.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-kinesisfirehosedestination.html#cfn-pinpointemail-configurationseteventdestination-kinesisfirehosedestination-iamrolearn
            '''
            result = self._values.get("iam_role_arn")
            assert result is not None, "Required property 'iam_role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisFirehoseDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_pinpointemail.CfnConfigurationSetEventDestination.PinpointDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"application_arn": "applicationArn"},
    )
    class PinpointDestinationProperty:
        def __init__(
            self,
            *,
            application_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An object that defines a Amazon Pinpoint destination for email events.

            You can use Amazon Pinpoint events to create attributes in Amazon Pinpoint projects. You can use these attributes to create segments for your campaigns.

            :param application_arn: The Amazon Resource Name (ARN) of the Amazon Pinpoint project that you want to send email events to.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-pinpointdestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_pinpointemail as pinpointemail
                
                pinpoint_destination_property = pinpointemail.CfnConfigurationSetEventDestination.PinpointDestinationProperty(
                    application_arn="applicationArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2345e2eaebb8eb55d49ab36422f7a0caa3f9f7981c8e74968b47fd2de08b2066)
                check_type(argname="argument application_arn", value=application_arn, expected_type=type_hints["application_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if application_arn is not None:
                self._values["application_arn"] = application_arn

        @builtins.property
        def application_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the Amazon Pinpoint project that you want to send email events to.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-pinpointdestination.html#cfn-pinpointemail-configurationseteventdestination-pinpointdestination-applicationarn
            '''
            result = self._values.get("application_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PinpointDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_pinpointemail.CfnConfigurationSetEventDestination.SnsDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"topic_arn": "topicArn"},
    )
    class SnsDestinationProperty:
        def __init__(self, *, topic_arn: builtins.str) -> None:
            '''An object that defines an Amazon SNS destination for email events.

            You can use Amazon SNS to send notification when certain email events occur.

            :param topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic that you want to publish email events to. For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-snsdestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_pinpointemail as pinpointemail
                
                sns_destination_property = pinpointemail.CfnConfigurationSetEventDestination.SnsDestinationProperty(
                    topic_arn="topicArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5632754cdbac357038bdbbf6fb698480bd30d39c8c5e730f1cf16508c1f3b2f8)
                check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "topic_arn": topic_arn,
            }

        @builtins.property
        def topic_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the Amazon SNS topic that you want to publish email events to.

            For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-snsdestination.html#cfn-pinpointemail-configurationseteventdestination-snsdestination-topicarn
            '''
            result = self._values.get("topic_arn")
            assert result is not None, "Required property 'topic_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SnsDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_pinpointemail.CfnConfigurationSetEventDestinationProps",
    jsii_struct_bases=[],
    name_mapping={
        "configuration_set_name": "configurationSetName",
        "event_destination_name": "eventDestinationName",
        "event_destination": "eventDestination",
    },
)
class CfnConfigurationSetEventDestinationProps:
    def __init__(
        self,
        *,
        configuration_set_name: builtins.str,
        event_destination_name: builtins.str,
        event_destination: typing.Optional[typing.Union[typing.Union[CfnConfigurationSetEventDestination.EventDestinationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    ) -> None:
        '''Properties for defining a ``CfnConfigurationSetEventDestination``.

        :param configuration_set_name: The name of the configuration set that contains the event destination that you want to modify.
        :param event_destination_name: The name of the event destination that you want to modify.
        :param event_destination: An object that defines the event destination.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationseteventdestination.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_pinpointemail as pinpointemail
            
            cfn_configuration_set_event_destination_props = pinpointemail.CfnConfigurationSetEventDestinationProps(
                configuration_set_name="configurationSetName",
                event_destination_name="eventDestinationName",
            
                # the properties below are optional
                event_destination=pinpointemail.CfnConfigurationSetEventDestination.EventDestinationProperty(
                    matching_event_types=["matchingEventTypes"],
            
                    # the properties below are optional
                    cloud_watch_destination=pinpointemail.CfnConfigurationSetEventDestination.CloudWatchDestinationProperty(
                        dimension_configurations=[pinpointemail.CfnConfigurationSetEventDestination.DimensionConfigurationProperty(
                            default_dimension_value="defaultDimensionValue",
                            dimension_name="dimensionName",
                            dimension_value_source="dimensionValueSource"
                        )]
                    ),
                    enabled=False,
                    kinesis_firehose_destination=pinpointemail.CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty(
                        delivery_stream_arn="deliveryStreamArn",
                        iam_role_arn="iamRoleArn"
                    ),
                    pinpoint_destination=pinpointemail.CfnConfigurationSetEventDestination.PinpointDestinationProperty(
                        application_arn="applicationArn"
                    ),
                    sns_destination=pinpointemail.CfnConfigurationSetEventDestination.SnsDestinationProperty(
                        topic_arn="topicArn"
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a0705cdfa79e0e24a08e95b787f33de17c5d8f215d3d8b7eabfea192e2b7295)
            check_type(argname="argument configuration_set_name", value=configuration_set_name, expected_type=type_hints["configuration_set_name"])
            check_type(argname="argument event_destination_name", value=event_destination_name, expected_type=type_hints["event_destination_name"])
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "configuration_set_name": configuration_set_name,
            "event_destination_name": event_destination_name,
        }
        if event_destination is not None:
            self._values["event_destination"] = event_destination

    @builtins.property
    def configuration_set_name(self) -> builtins.str:
        '''The name of the configuration set that contains the event destination that you want to modify.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationseteventdestination.html#cfn-pinpointemail-configurationseteventdestination-configurationsetname
        '''
        result = self._values.get("configuration_set_name")
        assert result is not None, "Required property 'configuration_set_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def event_destination_name(self) -> builtins.str:
        '''The name of the event destination that you want to modify.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationseteventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestinationname
        '''
        result = self._values.get("event_destination_name")
        assert result is not None, "Required property 'event_destination_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def event_destination(
        self,
    ) -> typing.Optional[typing.Union[CfnConfigurationSetEventDestination.EventDestinationProperty, _IResolvable_a771d0ef]]:
        '''An object that defines the event destination.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationseteventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestination
        '''
        result = self._values.get("event_destination")
        return typing.cast(typing.Optional[typing.Union[CfnConfigurationSetEventDestination.EventDestinationProperty, _IResolvable_a771d0ef]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConfigurationSetEventDestinationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_pinpointemail.CfnConfigurationSetProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "delivery_options": "deliveryOptions",
        "reputation_options": "reputationOptions",
        "sending_options": "sendingOptions",
        "tags": "tags",
        "tracking_options": "trackingOptions",
    },
)
class CfnConfigurationSetProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        delivery_options: typing.Optional[typing.Union[typing.Union[CfnConfigurationSet.DeliveryOptionsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        reputation_options: typing.Optional[typing.Union[typing.Union[CfnConfigurationSet.ReputationOptionsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        sending_options: typing.Optional[typing.Union[typing.Union[CfnConfigurationSet.SendingOptionsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[CfnConfigurationSet.TagsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tracking_options: typing.Optional[typing.Union[typing.Union[CfnConfigurationSet.TrackingOptionsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    ) -> None:
        '''Properties for defining a ``CfnConfigurationSet``.

        :param name: The name of the configuration set.
        :param delivery_options: An object that defines the dedicated IP pool that is used to send emails that you send using the configuration set.
        :param reputation_options: An object that defines whether or not Amazon Pinpoint collects reputation metrics for the emails that you send that use the configuration set.
        :param sending_options: An object that defines whether or not Amazon Pinpoint can send email that you send using the configuration set.
        :param tags: An object that defines the tags (keys and values) that you want to associate with the configuration set.
        :param tracking_options: An object that defines the open and click tracking options for emails that you send using the configuration set.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_pinpointemail as pinpointemail
            
            cfn_configuration_set_props = pinpointemail.CfnConfigurationSetProps(
                name="name",
            
                # the properties below are optional
                delivery_options=pinpointemail.CfnConfigurationSet.DeliveryOptionsProperty(
                    sending_pool_name="sendingPoolName"
                ),
                reputation_options=pinpointemail.CfnConfigurationSet.ReputationOptionsProperty(
                    reputation_metrics_enabled=False
                ),
                sending_options=pinpointemail.CfnConfigurationSet.SendingOptionsProperty(
                    sending_enabled=False
                ),
                tags=[pinpointemail.CfnConfigurationSet.TagsProperty(
                    key="key",
                    value="value"
                )],
                tracking_options=pinpointemail.CfnConfigurationSet.TrackingOptionsProperty(
                    custom_redirect_domain="customRedirectDomain"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2979be437f6a3f34cc7d08cd89a69b5f6fc664d8b5ebf6ecb681add9be5b49a9)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument delivery_options", value=delivery_options, expected_type=type_hints["delivery_options"])
            check_type(argname="argument reputation_options", value=reputation_options, expected_type=type_hints["reputation_options"])
            check_type(argname="argument sending_options", value=sending_options, expected_type=type_hints["sending_options"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tracking_options", value=tracking_options, expected_type=type_hints["tracking_options"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if delivery_options is not None:
            self._values["delivery_options"] = delivery_options
        if reputation_options is not None:
            self._values["reputation_options"] = reputation_options
        if sending_options is not None:
            self._values["sending_options"] = sending_options
        if tags is not None:
            self._values["tags"] = tags
        if tracking_options is not None:
            self._values["tracking_options"] = tracking_options

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the configuration set.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def delivery_options(
        self,
    ) -> typing.Optional[typing.Union[CfnConfigurationSet.DeliveryOptionsProperty, _IResolvable_a771d0ef]]:
        '''An object that defines the dedicated IP pool that is used to send emails that you send using the configuration set.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-deliveryoptions
        '''
        result = self._values.get("delivery_options")
        return typing.cast(typing.Optional[typing.Union[CfnConfigurationSet.DeliveryOptionsProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def reputation_options(
        self,
    ) -> typing.Optional[typing.Union[CfnConfigurationSet.ReputationOptionsProperty, _IResolvable_a771d0ef]]:
        '''An object that defines whether or not Amazon Pinpoint collects reputation metrics for the emails that you send that use the configuration set.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-reputationoptions
        '''
        result = self._values.get("reputation_options")
        return typing.cast(typing.Optional[typing.Union[CfnConfigurationSet.ReputationOptionsProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def sending_options(
        self,
    ) -> typing.Optional[typing.Union[CfnConfigurationSet.SendingOptionsProperty, _IResolvable_a771d0ef]]:
        '''An object that defines whether or not Amazon Pinpoint can send email that you send using the configuration set.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-sendingoptions
        '''
        result = self._values.get("sending_options")
        return typing.cast(typing.Optional[typing.Union[CfnConfigurationSet.SendingOptionsProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[CfnConfigurationSet.TagsProperty]]:
        '''An object that defines the tags (keys and values) that you want to associate with the configuration set.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[CfnConfigurationSet.TagsProperty]], result)

    @builtins.property
    def tracking_options(
        self,
    ) -> typing.Optional[typing.Union[CfnConfigurationSet.TrackingOptionsProperty, _IResolvable_a771d0ef]]:
        '''An object that defines the open and click tracking options for emails that you send using the configuration set.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-trackingoptions
        '''
        result = self._values.get("tracking_options")
        return typing.cast(typing.Optional[typing.Union[CfnConfigurationSet.TrackingOptionsProperty, _IResolvable_a771d0ef]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConfigurationSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnDedicatedIpPool(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_pinpointemail.CfnDedicatedIpPool",
):
    '''A CloudFormation ``AWS::PinpointEmail::DedicatedIpPool``.

    A request to create a new dedicated IP pool.

    :cloudformationResource: AWS::PinpointEmail::DedicatedIpPool
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-dedicatedippool.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_pinpointemail as pinpointemail
        
        cfn_dedicated_ip_pool = pinpointemail.CfnDedicatedIpPool(self, "MyCfnDedicatedIpPool",
            pool_name="poolName",
            tags=[pinpointemail.CfnDedicatedIpPool.TagsProperty(
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
        pool_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["CfnDedicatedIpPool.TagsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::PinpointEmail::DedicatedIpPool``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param pool_name: The name of the dedicated IP pool.
        :param tags: An object that defines the tags (keys and values) that you want to associate with the dedicated IP pool.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d60f161c94fa5de42006dc60385892ea9b90c47f2bcb1cc3a57fec3358ef256)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDedicatedIpPoolProps(pool_name=pool_name, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a144489f5464bf545348dc048831ff0579f2e5b4c1af98c2f57e72db07a8903)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d7bd0f34a623cfa66f763bfd319b5dd325e00c20d6973a4045f05021129bd7fd)
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
    @jsii.member(jsii_name="poolName")
    def pool_name(self) -> typing.Optional[builtins.str]:
        '''The name of the dedicated IP pool.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-dedicatedippool.html#cfn-pinpointemail-dedicatedippool-poolname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "poolName"))

    @pool_name.setter
    def pool_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__366593b1d05d2bc9faf94ff8c43b10d71eb2c891052835b9e99b28513a30cc25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "poolName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["CfnDedicatedIpPool.TagsProperty"]]:
        '''An object that defines the tags (keys and values) that you want to associate with the dedicated IP pool.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-dedicatedippool.html#cfn-pinpointemail-dedicatedippool-tags
        '''
        return typing.cast(typing.Optional[typing.List["CfnDedicatedIpPool.TagsProperty"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["CfnDedicatedIpPool.TagsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f95bbd0c2f78153af66d3387f7c074bd20195aca73c16e64c7fd36923124d4ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_pinpointemail.CfnDedicatedIpPool.TagsProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class TagsProperty:
        def __init__(
            self,
            *,
            key: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An object that defines the tags (keys and values) that you want to associate with the dedicated IP pool.

            :param key: One part of a key-value pair that defines a tag. The maximum length of a tag key is 128 characters. The minimum length is 1 character. If you specify tags for the dedicated IP pool, then this value is required.
            :param value: The optional part of a key-value pair that defines a tag. The maximum length of a tag value is 256 characters. The minimum length is 0 characters. If you don’t want a resource to have a specific tag value, don’t specify a value for this parameter. Amazon Pinpoint will set the value to an empty string.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-dedicatedippool-tags.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_pinpointemail as pinpointemail
                
                tags_property = pinpointemail.CfnDedicatedIpPool.TagsProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bdf1c4b13943e53b5c58216b38c2db293be0321eb60a52599ca79a1957e2c567)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if key is not None:
                self._values["key"] = key
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''One part of a key-value pair that defines a tag.

            The maximum length of a tag key is 128 characters. The minimum length is 1 character.

            If you specify tags for the dedicated IP pool, then this value is required.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-dedicatedippool-tags.html#cfn-pinpointemail-dedicatedippool-tags-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The optional part of a key-value pair that defines a tag.

            The maximum length of a tag value is 256 characters. The minimum length is 0 characters. If you don’t want a resource to have a specific tag value, don’t specify a value for this parameter. Amazon Pinpoint will set the value to an empty string.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-dedicatedippool-tags.html#cfn-pinpointemail-dedicatedippool-tags-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TagsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_pinpointemail.CfnDedicatedIpPoolProps",
    jsii_struct_bases=[],
    name_mapping={"pool_name": "poolName", "tags": "tags"},
)
class CfnDedicatedIpPoolProps:
    def __init__(
        self,
        *,
        pool_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[CfnDedicatedIpPool.TagsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDedicatedIpPool``.

        :param pool_name: The name of the dedicated IP pool.
        :param tags: An object that defines the tags (keys and values) that you want to associate with the dedicated IP pool.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-dedicatedippool.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_pinpointemail as pinpointemail
            
            cfn_dedicated_ip_pool_props = pinpointemail.CfnDedicatedIpPoolProps(
                pool_name="poolName",
                tags=[pinpointemail.CfnDedicatedIpPool.TagsProperty(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c7420f31323c8af7ecc585e3db3bc8272b2005dbdce0a883cbcdb8be66135c6)
            check_type(argname="argument pool_name", value=pool_name, expected_type=type_hints["pool_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if pool_name is not None:
            self._values["pool_name"] = pool_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def pool_name(self) -> typing.Optional[builtins.str]:
        '''The name of the dedicated IP pool.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-dedicatedippool.html#cfn-pinpointemail-dedicatedippool-poolname
        '''
        result = self._values.get("pool_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[CfnDedicatedIpPool.TagsProperty]]:
        '''An object that defines the tags (keys and values) that you want to associate with the dedicated IP pool.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-dedicatedippool.html#cfn-pinpointemail-dedicatedippool-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[CfnDedicatedIpPool.TagsProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDedicatedIpPoolProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnIdentity(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_pinpointemail.CfnIdentity",
):
    '''A CloudFormation ``AWS::PinpointEmail::Identity``.

    Specifies an identity to use for sending email through Amazon Pinpoint. In Amazon Pinpoint, an *identity* is an email address or domain that you use when you send email. Before you can use Amazon Pinpoint to send an email from an identity, you first have to verify it. By verifying an identity, you demonstrate that you're the owner of the address or domain, and that you've given Amazon Pinpoint permission to send email from that identity.

    When you verify an email address, Amazon Pinpoint sends an email to the address. Your email address is verified as soon as you follow the link in the verification email.

    When you verify a domain, this operation provides a set of DKIM tokens, which you can convert into CNAME tokens. You add these CNAME tokens to the DNS configuration for your domain. Your domain is verified when Amazon Pinpoint detects these records in the DNS configuration for your domain. It usually takes around 72 hours to complete the domain verification process.
    .. epigraph::

       When you use CloudFormation to specify an identity, CloudFormation might indicate that the identity was created successfully. However, you have to verify the identity before you can use it to send email.

    :cloudformationResource: AWS::PinpointEmail::Identity
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_pinpointemail as pinpointemail
        
        cfn_identity = pinpointemail.CfnIdentity(self, "MyCfnIdentity",
            name="name",
        
            # the properties below are optional
            dkim_signing_enabled=False,
            feedback_forwarding_enabled=False,
            mail_from_attributes=pinpointemail.CfnIdentity.MailFromAttributesProperty(
                behavior_on_mx_failure="behaviorOnMxFailure",
                mail_from_domain="mailFromDomain"
            ),
            tags=[pinpointemail.CfnIdentity.TagsProperty(
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
        name: builtins.str,
        dkim_signing_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        feedback_forwarding_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        mail_from_attributes: typing.Optional[typing.Union[typing.Union["CfnIdentity.MailFromAttributesProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["CfnIdentity.TagsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::PinpointEmail::Identity``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: The address or domain of the identity, such as *sender@example.com* or *example.co.uk* .
        :param dkim_signing_enabled: For domain identities, this attribute is used to enable or disable DomainKeys Identified Mail (DKIM) signing for the domain. If the value is ``true`` , then the messages that you send from the domain are signed using both the DKIM keys for your domain, as well as the keys for the ``amazonses.com`` domain. If the value is ``false`` , then the messages that you send are only signed using the DKIM keys for the ``amazonses.com`` domain.
        :param feedback_forwarding_enabled: Used to enable or disable feedback forwarding for an identity. This setting determines what happens when an identity is used to send an email that results in a bounce or complaint event. When you enable feedback forwarding, Amazon Pinpoint sends you email notifications when bounce or complaint events occur. Amazon Pinpoint sends this notification to the address that you specified in the Return-Path header of the original email. When you disable feedback forwarding, Amazon Pinpoint sends notifications through other mechanisms, such as by notifying an Amazon SNS topic. You're required to have a method of tracking bounces and complaints. If you haven't set up another mechanism for receiving bounce or complaint notifications, Amazon Pinpoint sends an email notification when these events occur (even if this setting is disabled).
        :param mail_from_attributes: Used to enable or disable the custom Mail-From domain configuration for an email identity.
        :param tags: An object that defines the tags (keys and values) that you want to associate with the email identity.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcee97837737ec359ea224aaeb1b6e00ea1fdfe89f307ac8fe71cdadb3f10769)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnIdentityProps(
            name=name,
            dkim_signing_enabled=dkim_signing_enabled,
            feedback_forwarding_enabled=feedback_forwarding_enabled,
            mail_from_attributes=mail_from_attributes,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b01441e7959e2141606cbe77ba12606b103aafcb23b3b879e403497d841125c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cdab7dc53d09b75933e0c4895e65054b4dae6b922bec258c0792adba66e63184)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrIdentityDnsRecordName1")
    def attr_identity_dns_record_name1(self) -> builtins.str:
        '''The host name for the first token that you have to add to the DNS configuration for your domain.

        For more information, see `Verifying a Domain <https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-manage-verify.html#channels-email-manage-verify-domain>`_ in the Amazon Pinpoint User Guide.

        :cloudformationAttribute: IdentityDNSRecordName1
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIdentityDnsRecordName1"))

    @builtins.property
    @jsii.member(jsii_name="attrIdentityDnsRecordName2")
    def attr_identity_dns_record_name2(self) -> builtins.str:
        '''The host name for the second token that you have to add to the DNS configuration for your domain.

        :cloudformationAttribute: IdentityDNSRecordName2
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIdentityDnsRecordName2"))

    @builtins.property
    @jsii.member(jsii_name="attrIdentityDnsRecordName3")
    def attr_identity_dns_record_name3(self) -> builtins.str:
        '''The host name for the third token that you have to add to the DNS configuration for your domain.

        :cloudformationAttribute: IdentityDNSRecordName3
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIdentityDnsRecordName3"))

    @builtins.property
    @jsii.member(jsii_name="attrIdentityDnsRecordValue1")
    def attr_identity_dns_record_value1(self) -> builtins.str:
        '''The record value for the first token that you have to add to the DNS configuration for your domain.

        :cloudformationAttribute: IdentityDNSRecordValue1
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIdentityDnsRecordValue1"))

    @builtins.property
    @jsii.member(jsii_name="attrIdentityDnsRecordValue2")
    def attr_identity_dns_record_value2(self) -> builtins.str:
        '''The record value for the second token that you have to add to the DNS configuration for your domain.

        :cloudformationAttribute: IdentityDNSRecordValue2
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIdentityDnsRecordValue2"))

    @builtins.property
    @jsii.member(jsii_name="attrIdentityDnsRecordValue3")
    def attr_identity_dns_record_value3(self) -> builtins.str:
        '''The record value for the third token that you have to add to the DNS configuration for your domain.

        :cloudformationAttribute: IdentityDNSRecordValue3
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIdentityDnsRecordValue3"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The address or domain of the identity, such as *sender@example.com* or *example.co.uk* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html#cfn-pinpointemail-identity-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56df6f03be25ae761fc4a4dcd51cfd70434f7696ac20c7fc6c5a2b00fc519912)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="dkimSigningEnabled")
    def dkim_signing_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''For domain identities, this attribute is used to enable or disable DomainKeys Identified Mail (DKIM) signing for the domain.

        If the value is ``true`` , then the messages that you send from the domain are signed using both the DKIM keys for your domain, as well as the keys for the ``amazonses.com`` domain. If the value is ``false`` , then the messages that you send are only signed using the DKIM keys for the ``amazonses.com`` domain.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html#cfn-pinpointemail-identity-dkimsigningenabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], jsii.get(self, "dkimSigningEnabled"))

    @dkim_signing_enabled.setter
    def dkim_signing_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b692e61288c0e1447afd16670aab8c08b7b3e517fa8a4459b27ad96d4b8a8793)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dkimSigningEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="feedbackForwardingEnabled")
    def feedback_forwarding_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''Used to enable or disable feedback forwarding for an identity.

        This setting determines what happens when an identity is used to send an email that results in a bounce or complaint event.

        When you enable feedback forwarding, Amazon Pinpoint sends you email notifications when bounce or complaint events occur. Amazon Pinpoint sends this notification to the address that you specified in the Return-Path header of the original email.

        When you disable feedback forwarding, Amazon Pinpoint sends notifications through other mechanisms, such as by notifying an Amazon SNS topic. You're required to have a method of tracking bounces and complaints. If you haven't set up another mechanism for receiving bounce or complaint notifications, Amazon Pinpoint sends an email notification when these events occur (even if this setting is disabled).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html#cfn-pinpointemail-identity-feedbackforwardingenabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], jsii.get(self, "feedbackForwardingEnabled"))

    @feedback_forwarding_enabled.setter
    def feedback_forwarding_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9938adf55a136450a5604478cb17889a1a65b6f6f69b472b2d9da98043ababe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "feedbackForwardingEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="mailFromAttributes")
    def mail_from_attributes(
        self,
    ) -> typing.Optional[typing.Union["CfnIdentity.MailFromAttributesProperty", _IResolvable_a771d0ef]]:
        '''Used to enable or disable the custom Mail-From domain configuration for an email identity.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html#cfn-pinpointemail-identity-mailfromattributes
        '''
        return typing.cast(typing.Optional[typing.Union["CfnIdentity.MailFromAttributesProperty", _IResolvable_a771d0ef]], jsii.get(self, "mailFromAttributes"))

    @mail_from_attributes.setter
    def mail_from_attributes(
        self,
        value: typing.Optional[typing.Union["CfnIdentity.MailFromAttributesProperty", _IResolvable_a771d0ef]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8330973f61006bd3d0be48810b97139bf534f4b2fe6f7a8434f17de3b9ca9e91)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mailFromAttributes", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["CfnIdentity.TagsProperty"]]:
        '''An object that defines the tags (keys and values) that you want to associate with the email identity.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html#cfn-pinpointemail-identity-tags
        '''
        return typing.cast(typing.Optional[typing.List["CfnIdentity.TagsProperty"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["CfnIdentity.TagsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0454f722b8ace5ee4630cfdedea311189ed61dd083bde5f55690494cea51259)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_pinpointemail.CfnIdentity.MailFromAttributesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "behavior_on_mx_failure": "behaviorOnMxFailure",
            "mail_from_domain": "mailFromDomain",
        },
    )
    class MailFromAttributesProperty:
        def __init__(
            self,
            *,
            behavior_on_mx_failure: typing.Optional[builtins.str] = None,
            mail_from_domain: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A list of attributes that are associated with a MAIL FROM domain.

            :param behavior_on_mx_failure: The action that Amazon Pinpoint to takes if it can't read the required MX record for a custom MAIL FROM domain. When you set this value to ``UseDefaultValue`` , Amazon Pinpoint uses *amazonses.com* as the MAIL FROM domain. When you set this value to ``RejectMessage`` , Amazon Pinpoint returns a ``MailFromDomainNotVerified`` error, and doesn't attempt to deliver the email. These behaviors are taken when the custom MAIL FROM domain configuration is in the ``Pending`` , ``Failed`` , and ``TemporaryFailure`` states.
            :param mail_from_domain: The name of a domain that an email identity uses as a custom MAIL FROM domain.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-identity-mailfromattributes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_pinpointemail as pinpointemail
                
                mail_from_attributes_property = pinpointemail.CfnIdentity.MailFromAttributesProperty(
                    behavior_on_mx_failure="behaviorOnMxFailure",
                    mail_from_domain="mailFromDomain"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0a1e1693d52ef06a29ee3050e2a91aa69309d44e40c8da869ae839ef538f4903)
                check_type(argname="argument behavior_on_mx_failure", value=behavior_on_mx_failure, expected_type=type_hints["behavior_on_mx_failure"])
                check_type(argname="argument mail_from_domain", value=mail_from_domain, expected_type=type_hints["mail_from_domain"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if behavior_on_mx_failure is not None:
                self._values["behavior_on_mx_failure"] = behavior_on_mx_failure
            if mail_from_domain is not None:
                self._values["mail_from_domain"] = mail_from_domain

        @builtins.property
        def behavior_on_mx_failure(self) -> typing.Optional[builtins.str]:
            '''The action that Amazon Pinpoint to takes if it can't read the required MX record for a custom MAIL FROM domain.

            When you set this value to ``UseDefaultValue`` , Amazon Pinpoint uses *amazonses.com* as the MAIL FROM domain. When you set this value to ``RejectMessage`` , Amazon Pinpoint returns a ``MailFromDomainNotVerified`` error, and doesn't attempt to deliver the email.

            These behaviors are taken when the custom MAIL FROM domain configuration is in the ``Pending`` , ``Failed`` , and ``TemporaryFailure`` states.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-identity-mailfromattributes.html#cfn-pinpointemail-identity-mailfromattributes-behavioronmxfailure
            '''
            result = self._values.get("behavior_on_mx_failure")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def mail_from_domain(self) -> typing.Optional[builtins.str]:
            '''The name of a domain that an email identity uses as a custom MAIL FROM domain.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-identity-mailfromattributes.html#cfn-pinpointemail-identity-mailfromattributes-mailfromdomain
            '''
            result = self._values.get("mail_from_domain")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MailFromAttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_pinpointemail.CfnIdentity.TagsProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class TagsProperty:
        def __init__(
            self,
            *,
            key: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An object that defines the tags (keys and values) that you want to associate with the identity.

            :param key: One part of a key-value pair that defines a tag. The maximum length of a tag key is 128 characters. The minimum length is 1 character. If you specify tags for the identity, then this value is required.
            :param value: The optional part of a key-value pair that defines a tag. The maximum length of a tag value is 256 characters. The minimum length is 0 characters. If you don’t want a resource to have a specific tag value, don’t specify a value for this parameter. Amazon Pinpoint will set the value to an empty string.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-identity-tags.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_pinpointemail as pinpointemail
                
                tags_property = pinpointemail.CfnIdentity.TagsProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__abf0e3d685840494b81a9c43d7a0af7f918fe5e2730162321aa1ab038f0c2856)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if key is not None:
                self._values["key"] = key
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''One part of a key-value pair that defines a tag.

            The maximum length of a tag key is 128 characters. The minimum length is 1 character.

            If you specify tags for the identity, then this value is required.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-identity-tags.html#cfn-pinpointemail-identity-tags-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The optional part of a key-value pair that defines a tag.

            The maximum length of a tag value is 256 characters. The minimum length is 0 characters. If you don’t want a resource to have a specific tag value, don’t specify a value for this parameter. Amazon Pinpoint will set the value to an empty string.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-identity-tags.html#cfn-pinpointemail-identity-tags-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TagsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_pinpointemail.CfnIdentityProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "dkim_signing_enabled": "dkimSigningEnabled",
        "feedback_forwarding_enabled": "feedbackForwardingEnabled",
        "mail_from_attributes": "mailFromAttributes",
        "tags": "tags",
    },
)
class CfnIdentityProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        dkim_signing_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        feedback_forwarding_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        mail_from_attributes: typing.Optional[typing.Union[typing.Union[CfnIdentity.MailFromAttributesProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[CfnIdentity.TagsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnIdentity``.

        :param name: The address or domain of the identity, such as *sender@example.com* or *example.co.uk* .
        :param dkim_signing_enabled: For domain identities, this attribute is used to enable or disable DomainKeys Identified Mail (DKIM) signing for the domain. If the value is ``true`` , then the messages that you send from the domain are signed using both the DKIM keys for your domain, as well as the keys for the ``amazonses.com`` domain. If the value is ``false`` , then the messages that you send are only signed using the DKIM keys for the ``amazonses.com`` domain.
        :param feedback_forwarding_enabled: Used to enable or disable feedback forwarding for an identity. This setting determines what happens when an identity is used to send an email that results in a bounce or complaint event. When you enable feedback forwarding, Amazon Pinpoint sends you email notifications when bounce or complaint events occur. Amazon Pinpoint sends this notification to the address that you specified in the Return-Path header of the original email. When you disable feedback forwarding, Amazon Pinpoint sends notifications through other mechanisms, such as by notifying an Amazon SNS topic. You're required to have a method of tracking bounces and complaints. If you haven't set up another mechanism for receiving bounce or complaint notifications, Amazon Pinpoint sends an email notification when these events occur (even if this setting is disabled).
        :param mail_from_attributes: Used to enable or disable the custom Mail-From domain configuration for an email identity.
        :param tags: An object that defines the tags (keys and values) that you want to associate with the email identity.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_pinpointemail as pinpointemail
            
            cfn_identity_props = pinpointemail.CfnIdentityProps(
                name="name",
            
                # the properties below are optional
                dkim_signing_enabled=False,
                feedback_forwarding_enabled=False,
                mail_from_attributes=pinpointemail.CfnIdentity.MailFromAttributesProperty(
                    behavior_on_mx_failure="behaviorOnMxFailure",
                    mail_from_domain="mailFromDomain"
                ),
                tags=[pinpointemail.CfnIdentity.TagsProperty(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ad40a3bb7f70638a62caa760433cc12144dcb3d8127fb853cab77c6d64ee0c0)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument dkim_signing_enabled", value=dkim_signing_enabled, expected_type=type_hints["dkim_signing_enabled"])
            check_type(argname="argument feedback_forwarding_enabled", value=feedback_forwarding_enabled, expected_type=type_hints["feedback_forwarding_enabled"])
            check_type(argname="argument mail_from_attributes", value=mail_from_attributes, expected_type=type_hints["mail_from_attributes"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if dkim_signing_enabled is not None:
            self._values["dkim_signing_enabled"] = dkim_signing_enabled
        if feedback_forwarding_enabled is not None:
            self._values["feedback_forwarding_enabled"] = feedback_forwarding_enabled
        if mail_from_attributes is not None:
            self._values["mail_from_attributes"] = mail_from_attributes
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The address or domain of the identity, such as *sender@example.com* or *example.co.uk* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html#cfn-pinpointemail-identity-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dkim_signing_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''For domain identities, this attribute is used to enable or disable DomainKeys Identified Mail (DKIM) signing for the domain.

        If the value is ``true`` , then the messages that you send from the domain are signed using both the DKIM keys for your domain, as well as the keys for the ``amazonses.com`` domain. If the value is ``false`` , then the messages that you send are only signed using the DKIM keys for the ``amazonses.com`` domain.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html#cfn-pinpointemail-identity-dkimsigningenabled
        '''
        result = self._values.get("dkim_signing_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

    @builtins.property
    def feedback_forwarding_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        '''Used to enable or disable feedback forwarding for an identity.

        This setting determines what happens when an identity is used to send an email that results in a bounce or complaint event.

        When you enable feedback forwarding, Amazon Pinpoint sends you email notifications when bounce or complaint events occur. Amazon Pinpoint sends this notification to the address that you specified in the Return-Path header of the original email.

        When you disable feedback forwarding, Amazon Pinpoint sends notifications through other mechanisms, such as by notifying an Amazon SNS topic. You're required to have a method of tracking bounces and complaints. If you haven't set up another mechanism for receiving bounce or complaint notifications, Amazon Pinpoint sends an email notification when these events occur (even if this setting is disabled).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html#cfn-pinpointemail-identity-feedbackforwardingenabled
        '''
        result = self._values.get("feedback_forwarding_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]], result)

    @builtins.property
    def mail_from_attributes(
        self,
    ) -> typing.Optional[typing.Union[CfnIdentity.MailFromAttributesProperty, _IResolvable_a771d0ef]]:
        '''Used to enable or disable the custom Mail-From domain configuration for an email identity.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html#cfn-pinpointemail-identity-mailfromattributes
        '''
        result = self._values.get("mail_from_attributes")
        return typing.cast(typing.Optional[typing.Union[CfnIdentity.MailFromAttributesProperty, _IResolvable_a771d0ef]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[CfnIdentity.TagsProperty]]:
        '''An object that defines the tags (keys and values) that you want to associate with the email identity.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html#cfn-pinpointemail-identity-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[CfnIdentity.TagsProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnIdentityProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnConfigurationSet",
    "CfnConfigurationSetEventDestination",
    "CfnConfigurationSetEventDestinationProps",
    "CfnConfigurationSetProps",
    "CfnDedicatedIpPool",
    "CfnDedicatedIpPoolProps",
    "CfnIdentity",
    "CfnIdentityProps",
]

publication.publish()

def _typecheckingstub__b5883984ad1311cfaaf11ca8eab556aea2cf6417079aae0293b66006d89162f3(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    name: builtins.str,
    delivery_options: typing.Optional[typing.Union[typing.Union[CfnConfigurationSet.DeliveryOptionsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    reputation_options: typing.Optional[typing.Union[typing.Union[CfnConfigurationSet.ReputationOptionsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    sending_options: typing.Optional[typing.Union[typing.Union[CfnConfigurationSet.SendingOptionsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnConfigurationSet.TagsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tracking_options: typing.Optional[typing.Union[typing.Union[CfnConfigurationSet.TrackingOptionsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edbbea0488801ae94a320fe0688143e4a2f6f27d1cb3b41693f28179e1114d76(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4d2595ff4a49482ec1bbc2cd37d1810924e89d89fddf0e1786b30a17659d7e6(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46ae6e64a9112029d6104c7e2d44f99abd4f04b13e589b8b35b1bfb59a933516(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3f8ae9976e159a1718067d389fbe3706f5026445e046740aa56237c5fdcf3d5(
    value: typing.Optional[typing.Union[CfnConfigurationSet.DeliveryOptionsProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58062a827573a7a7d37efc3419487bc882f5948ef28063ae422431568d46dfa9(
    value: typing.Optional[typing.Union[CfnConfigurationSet.ReputationOptionsProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41313e55c12723a640d803f32b0530f5cf4e5504d33326f1c04888ea04ea8d41(
    value: typing.Optional[typing.Union[CfnConfigurationSet.SendingOptionsProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf6015ba5151acadc0a23718a33a6426172e90a45fcd25cb6c48c055e9d5fd0c(
    value: typing.Optional[typing.List[CfnConfigurationSet.TagsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4185429bcdb088868cff68b4000b94487aa64d1d047ba1599d58c6384c8fa3d1(
    value: typing.Optional[typing.Union[CfnConfigurationSet.TrackingOptionsProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85368c0a3518fb63084683c62965c534cb6a7eb3579edb161fabf12a98f94138(
    *,
    sending_pool_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f045ad54d73f019d4dfb939078b0858000c7555ff7d386313d49a3d546712d15(
    *,
    reputation_metrics_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f170319e613e4a4463d75ba5083b6022a1910366e198e5db04e659f0f4519f2(
    *,
    sending_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb578541f03a4950372f080fb23ee50c1c40012f032c3205fbb9162f1ede11a5(
    *,
    key: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b9bc02c2421fe8f95d3ee4d2d0d4e5a1f4115bd947559b88b2b2418af240d91(
    *,
    custom_redirect_domain: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__668889263897a93ec423752b155e3dc053b532cb62492ee997b17012dbe50275(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    configuration_set_name: builtins.str,
    event_destination_name: builtins.str,
    event_destination: typing.Optional[typing.Union[typing.Union[CfnConfigurationSetEventDestination.EventDestinationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bb1fe42f16de7b64973f77328910cb24af889d1443b71edcd1eb17d816a0208(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cbd7b5e8bb24c3eda55739763cb80a43801f81f59c3c79ff30643e6652278c0(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1fa282673be7fa6e73bb208564d2f665ec36b0f05227c36f64a9e00f3bc8cb9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__629c691eb16c379b2687b88ad1ec9fd3267b3a897da44e9622f58dd967f258d1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca5c8de21ccb88a79cae28aed8e98eee72a11c7f79eb758635ae7499a1541e0c(
    value: typing.Optional[typing.Union[CfnConfigurationSetEventDestination.EventDestinationProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30f57a46a6936dd157c9116b7b0f38dfa216dc4838db5143b9c41378d0810e9e(
    *,
    dimension_configurations: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.Sequence[typing.Union[typing.Union[CfnConfigurationSetEventDestination.DimensionConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55e140348608c6e3e976c689bd3233cea7d8a4e18deab1a65b454feee08562da(
    *,
    default_dimension_value: builtins.str,
    dimension_name: builtins.str,
    dimension_value_source: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a0737de3768b00466a794fed26a8edc22b104bac27eb101fd6ca045a92f6374(
    *,
    matching_event_types: typing.Sequence[builtins.str],
    cloud_watch_destination: typing.Optional[typing.Union[typing.Union[CfnConfigurationSetEventDestination.CloudWatchDestinationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    kinesis_firehose_destination: typing.Optional[typing.Union[typing.Union[CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    pinpoint_destination: typing.Optional[typing.Union[typing.Union[CfnConfigurationSetEventDestination.PinpointDestinationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    sns_destination: typing.Optional[typing.Union[typing.Union[CfnConfigurationSetEventDestination.SnsDestinationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2710a1086c0e2b3f9dca03f3cfa46cad723658e2541acea93b98a960f57844cf(
    *,
    delivery_stream_arn: builtins.str,
    iam_role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2345e2eaebb8eb55d49ab36422f7a0caa3f9f7981c8e74968b47fd2de08b2066(
    *,
    application_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5632754cdbac357038bdbbf6fb698480bd30d39c8c5e730f1cf16508c1f3b2f8(
    *,
    topic_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a0705cdfa79e0e24a08e95b787f33de17c5d8f215d3d8b7eabfea192e2b7295(
    *,
    configuration_set_name: builtins.str,
    event_destination_name: builtins.str,
    event_destination: typing.Optional[typing.Union[typing.Union[CfnConfigurationSetEventDestination.EventDestinationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2979be437f6a3f34cc7d08cd89a69b5f6fc664d8b5ebf6ecb681add9be5b49a9(
    *,
    name: builtins.str,
    delivery_options: typing.Optional[typing.Union[typing.Union[CfnConfigurationSet.DeliveryOptionsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    reputation_options: typing.Optional[typing.Union[typing.Union[CfnConfigurationSet.ReputationOptionsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    sending_options: typing.Optional[typing.Union[typing.Union[CfnConfigurationSet.SendingOptionsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnConfigurationSet.TagsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tracking_options: typing.Optional[typing.Union[typing.Union[CfnConfigurationSet.TrackingOptionsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d60f161c94fa5de42006dc60385892ea9b90c47f2bcb1cc3a57fec3358ef256(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    pool_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnDedicatedIpPool.TagsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a144489f5464bf545348dc048831ff0579f2e5b4c1af98c2f57e72db07a8903(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7bd0f34a623cfa66f763bfd319b5dd325e00c20d6973a4045f05021129bd7fd(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__366593b1d05d2bc9faf94ff8c43b10d71eb2c891052835b9e99b28513a30cc25(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f95bbd0c2f78153af66d3387f7c074bd20195aca73c16e64c7fd36923124d4ee(
    value: typing.Optional[typing.List[CfnDedicatedIpPool.TagsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdf1c4b13943e53b5c58216b38c2db293be0321eb60a52599ca79a1957e2c567(
    *,
    key: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c7420f31323c8af7ecc585e3db3bc8272b2005dbdce0a883cbcdb8be66135c6(
    *,
    pool_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnDedicatedIpPool.TagsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcee97837737ec359ea224aaeb1b6e00ea1fdfe89f307ac8fe71cdadb3f10769(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    name: builtins.str,
    dkim_signing_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    feedback_forwarding_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    mail_from_attributes: typing.Optional[typing.Union[typing.Union[CfnIdentity.MailFromAttributesProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnIdentity.TagsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b01441e7959e2141606cbe77ba12606b103aafcb23b3b879e403497d841125c(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdab7dc53d09b75933e0c4895e65054b4dae6b922bec258c0792adba66e63184(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56df6f03be25ae761fc4a4dcd51cfd70434f7696ac20c7fc6c5a2b00fc519912(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b692e61288c0e1447afd16670aab8c08b7b3e517fa8a4459b27ad96d4b8a8793(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9938adf55a136450a5604478cb17889a1a65b6f6f69b472b2d9da98043ababe(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8330973f61006bd3d0be48810b97139bf534f4b2fe6f7a8434f17de3b9ca9e91(
    value: typing.Optional[typing.Union[CfnIdentity.MailFromAttributesProperty, _IResolvable_a771d0ef]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0454f722b8ace5ee4630cfdedea311189ed61dd083bde5f55690494cea51259(
    value: typing.Optional[typing.List[CfnIdentity.TagsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a1e1693d52ef06a29ee3050e2a91aa69309d44e40c8da869ae839ef538f4903(
    *,
    behavior_on_mx_failure: typing.Optional[builtins.str] = None,
    mail_from_domain: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abf0e3d685840494b81a9c43d7a0af7f918fe5e2730162321aa1ab038f0c2856(
    *,
    key: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ad40a3bb7f70638a62caa760433cc12144dcb3d8127fb853cab77c6d64ee0c0(
    *,
    name: builtins.str,
    dkim_signing_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    feedback_forwarding_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    mail_from_attributes: typing.Optional[typing.Union[typing.Union[CfnIdentity.MailFromAttributesProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnIdentity.TagsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

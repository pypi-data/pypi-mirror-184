'''
# AWS::EMRContainers Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import monocdk as emrcontainers
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for EMRContainers construct libraries](https://constructs.dev/search?q=emrcontainers)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::EMRContainers resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_EMRContainers.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::EMRContainers](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_EMRContainers.html).

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
class CfnVirtualCluster(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_emrcontainers.CfnVirtualCluster",
):
    '''A CloudFormation ``AWS::EMRContainers::VirtualCluster``.

    The ``AWS::EMRContainers::VirtualCluster`` resource specifies a virtual cluster. A virtual cluster is a managed entity on Amazon EMR on EKS. You can create, describe, list, and delete virtual clusters. They do not consume any additional resources in your system. A single virtual cluster maps to a single Kubernetes namespace. Given this relationship, you can model virtual clusters the same way you model Kubernetes namespaces to meet your requirements.

    :cloudformationResource: AWS::EMRContainers::VirtualCluster
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-virtualcluster.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_emrcontainers as emrcontainers
        
        cfn_virtual_cluster = emrcontainers.CfnVirtualCluster(self, "MyCfnVirtualCluster",
            container_provider=emrcontainers.CfnVirtualCluster.ContainerProviderProperty(
                id="id",
                info=emrcontainers.CfnVirtualCluster.ContainerInfoProperty(
                    eks_info=emrcontainers.CfnVirtualCluster.EksInfoProperty(
                        namespace="namespace"
                    )
                ),
                type="type"
            ),
            name="name",
        
            # the properties below are optional
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
        container_provider: typing.Union[typing.Union["CfnVirtualCluster.ContainerProviderProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
        name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::EMRContainers::VirtualCluster``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param container_provider: The container provider of the virtual cluster.
        :param name: The name of the virtual cluster.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f13d72ed68a5ff1dd81def6d6f8558013ec7f3b5bf2ed149b0169b642b3bf356)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnVirtualClusterProps(
            container_provider=container_provider, name=name, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdd0f249647501e7046dc138784af31b0bb09d60146468b55ceaaa198606338b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2cead680911adfc7563688861a84b658acbf1902869b2a80cc2b68cb451f8504)
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
        '''The Amazon Resource Name (ARN) of the project, such as ``arn:aws:emr-containers:us-east-1:123456789012:/virtualclusters/ab4rp1abcs8xz47n3x0example`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the virtual cluster, such as ``ab4rp1abcs8xz47n3x0example`` .

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

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-virtualcluster.html#cfn-emrcontainers-virtualcluster-tags
        '''
        return typing.cast(_TagManager_0b7ab120, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="containerProvider")
    def container_provider(
        self,
    ) -> typing.Union["CfnVirtualCluster.ContainerProviderProperty", _IResolvable_a771d0ef]:
        '''The container provider of the virtual cluster.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-virtualcluster.html#cfn-emrcontainers-virtualcluster-containerprovider
        '''
        return typing.cast(typing.Union["CfnVirtualCluster.ContainerProviderProperty", _IResolvable_a771d0ef], jsii.get(self, "containerProvider"))

    @container_provider.setter
    def container_provider(
        self,
        value: typing.Union["CfnVirtualCluster.ContainerProviderProperty", _IResolvable_a771d0ef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a365eadc5a810af552f749454e0b5f6beb083007f01b15704bf2dc45928ffb24)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerProvider", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the virtual cluster.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-virtualcluster.html#cfn-emrcontainers-virtualcluster-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e02f62947a75b2ba210d3a685ce7038699431f4e5a639055de5dd004efaaa20c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_emrcontainers.CfnVirtualCluster.ContainerInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"eks_info": "eksInfo"},
    )
    class ContainerInfoProperty:
        def __init__(
            self,
            *,
            eks_info: typing.Union[typing.Union["CfnVirtualCluster.EksInfoProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
        ) -> None:
            '''The information about the container used for a job run or a managed endpoint.

            :param eks_info: The information about the Amazon EKS cluster.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-containerinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_emrcontainers as emrcontainers
                
                container_info_property = emrcontainers.CfnVirtualCluster.ContainerInfoProperty(
                    eks_info=emrcontainers.CfnVirtualCluster.EksInfoProperty(
                        namespace="namespace"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6ef2ede6d21c18d25a23dc27c5d9b665381e84416aca72ad523b91f6f94d0f1f)
                check_type(argname="argument eks_info", value=eks_info, expected_type=type_hints["eks_info"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "eks_info": eks_info,
            }

        @builtins.property
        def eks_info(
            self,
        ) -> typing.Union["CfnVirtualCluster.EksInfoProperty", _IResolvable_a771d0ef]:
            '''The information about the Amazon EKS cluster.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-containerinfo.html#cfn-emrcontainers-virtualcluster-containerinfo-eksinfo
            '''
            result = self._values.get("eks_info")
            assert result is not None, "Required property 'eks_info' is missing"
            return typing.cast(typing.Union["CfnVirtualCluster.EksInfoProperty", _IResolvable_a771d0ef], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_emrcontainers.CfnVirtualCluster.ContainerProviderProperty",
        jsii_struct_bases=[],
        name_mapping={"id": "id", "info": "info", "type": "type"},
    )
    class ContainerProviderProperty:
        def __init__(
            self,
            *,
            id: builtins.str,
            info: typing.Union[typing.Union["CfnVirtualCluster.ContainerInfoProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
            type: builtins.str,
        ) -> None:
            '''The information about the container provider.

            :param id: The ID of the container cluster. *Minimum* : 1 *Maximum* : 100 *Pattern* : ``^[0-9A-Za-z][A-Za-z0-9\\-_]*``
            :param info: The information about the container cluster.
            :param type: The type of the container provider. Amazon EKS is the only supported type as of now.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-containerprovider.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_emrcontainers as emrcontainers
                
                container_provider_property = emrcontainers.CfnVirtualCluster.ContainerProviderProperty(
                    id="id",
                    info=emrcontainers.CfnVirtualCluster.ContainerInfoProperty(
                        eks_info=emrcontainers.CfnVirtualCluster.EksInfoProperty(
                            namespace="namespace"
                        )
                    ),
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__213150720f78774a76f6cbcf12a4fe8a3af7b7b61c6bc9f27f0040991d9bf40d)
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument info", value=info, expected_type=type_hints["info"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "id": id,
                "info": info,
                "type": type,
            }

        @builtins.property
        def id(self) -> builtins.str:
            '''The ID of the container cluster.

            *Minimum* : 1

            *Maximum* : 100

            *Pattern* : ``^[0-9A-Za-z][A-Za-z0-9\\-_]*``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-containerprovider.html#cfn-emrcontainers-virtualcluster-containerprovider-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def info(
            self,
        ) -> typing.Union["CfnVirtualCluster.ContainerInfoProperty", _IResolvable_a771d0ef]:
            '''The information about the container cluster.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-containerprovider.html#cfn-emrcontainers-virtualcluster-containerprovider-info
            '''
            result = self._values.get("info")
            assert result is not None, "Required property 'info' is missing"
            return typing.cast(typing.Union["CfnVirtualCluster.ContainerInfoProperty", _IResolvable_a771d0ef], result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of the container provider.

            Amazon EKS is the only supported type as of now.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-containerprovider.html#cfn-emrcontainers-virtualcluster-containerprovider-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerProviderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_emrcontainers.CfnVirtualCluster.EksInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"namespace": "namespace"},
    )
    class EksInfoProperty:
        def __init__(self, *, namespace: builtins.str) -> None:
            '''The information about the Amazon EKS cluster.

            :param namespace: The namespaces of the EKS cluster. *Minimum* : 1 *Maximum* : 63 *Pattern* : ``[a-z0-9]([-a-z0-9]*[a-z0-9])?``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-eksinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_emrcontainers as emrcontainers
                
                eks_info_property = emrcontainers.CfnVirtualCluster.EksInfoProperty(
                    namespace="namespace"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3b3f26cc1bdda7a215b4ba59105c897f6c55edeae6e6e50422dfe6f3bed44b85)
                check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "namespace": namespace,
            }

        @builtins.property
        def namespace(self) -> builtins.str:
            '''The namespaces of the EKS cluster.

            *Minimum* : 1

            *Maximum* : 63

            *Pattern* : ``[a-z0-9]([-a-z0-9]*[a-z0-9])?``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-eksinfo.html#cfn-emrcontainers-virtualcluster-eksinfo-namespace
            '''
            result = self._values.get("namespace")
            assert result is not None, "Required property 'namespace' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EksInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_emrcontainers.CfnVirtualClusterProps",
    jsii_struct_bases=[],
    name_mapping={
        "container_provider": "containerProvider",
        "name": "name",
        "tags": "tags",
    },
)
class CfnVirtualClusterProps:
    def __init__(
        self,
        *,
        container_provider: typing.Union[typing.Union[CfnVirtualCluster.ContainerProviderProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
        name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnVirtualCluster``.

        :param container_provider: The container provider of the virtual cluster.
        :param name: The name of the virtual cluster.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-virtualcluster.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_emrcontainers as emrcontainers
            
            cfn_virtual_cluster_props = emrcontainers.CfnVirtualClusterProps(
                container_provider=emrcontainers.CfnVirtualCluster.ContainerProviderProperty(
                    id="id",
                    info=emrcontainers.CfnVirtualCluster.ContainerInfoProperty(
                        eks_info=emrcontainers.CfnVirtualCluster.EksInfoProperty(
                            namespace="namespace"
                        )
                    ),
                    type="type"
                ),
                name="name",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03a25aa37e56597d2bb78ab5be9171fb3cc13b45825bfc910ddbaac1b881f844)
            check_type(argname="argument container_provider", value=container_provider, expected_type=type_hints["container_provider"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "container_provider": container_provider,
            "name": name,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def container_provider(
        self,
    ) -> typing.Union[CfnVirtualCluster.ContainerProviderProperty, _IResolvable_a771d0ef]:
        '''The container provider of the virtual cluster.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-virtualcluster.html#cfn-emrcontainers-virtualcluster-containerprovider
        '''
        result = self._values.get("container_provider")
        assert result is not None, "Required property 'container_provider' is missing"
        return typing.cast(typing.Union[CfnVirtualCluster.ContainerProviderProperty, _IResolvable_a771d0ef], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the virtual cluster.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-virtualcluster.html#cfn-emrcontainers-virtualcluster-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_95fbdc29]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-virtualcluster.html#cfn-emrcontainers-virtualcluster-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_95fbdc29]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVirtualClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnVirtualCluster",
    "CfnVirtualClusterProps",
]

publication.publish()

def _typecheckingstub__f13d72ed68a5ff1dd81def6d6f8558013ec7f3b5bf2ed149b0169b642b3bf356(
    scope: _Construct_e78e779f,
    id: builtins.str,
    *,
    container_provider: typing.Union[typing.Union[CfnVirtualCluster.ContainerProviderProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
    name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdd0f249647501e7046dc138784af31b0bb09d60146468b55ceaaa198606338b(
    inspector: _TreeInspector_1cd1894e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cead680911adfc7563688861a84b658acbf1902869b2a80cc2b68cb451f8504(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a365eadc5a810af552f749454e0b5f6beb083007f01b15704bf2dc45928ffb24(
    value: typing.Union[CfnVirtualCluster.ContainerProviderProperty, _IResolvable_a771d0ef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e02f62947a75b2ba210d3a685ce7038699431f4e5a639055de5dd004efaaa20c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ef2ede6d21c18d25a23dc27c5d9b665381e84416aca72ad523b91f6f94d0f1f(
    *,
    eks_info: typing.Union[typing.Union[CfnVirtualCluster.EksInfoProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__213150720f78774a76f6cbcf12a4fe8a3af7b7b61c6bc9f27f0040991d9bf40d(
    *,
    id: builtins.str,
    info: typing.Union[typing.Union[CfnVirtualCluster.ContainerInfoProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b3f26cc1bdda7a215b4ba59105c897f6c55edeae6e6e50422dfe6f3bed44b85(
    *,
    namespace: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03a25aa37e56597d2bb78ab5be9171fb3cc13b45825bfc910ddbaac1b881f844(
    *,
    container_provider: typing.Union[typing.Union[CfnVirtualCluster.ContainerProviderProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_a771d0ef],
    name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_95fbdc29, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

'''
# AWS::IoTFleetWise Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_iotfleetwise as iotfleetwise
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for IoTFleetWise construct libraries](https://constructs.dev/search?q=iotfleetwise)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::IoTFleetWise resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IoTFleetWise.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::IoTFleetWise](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IoTFleetWise.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/main/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

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

import constructs as _constructs_77d1e7e8
from .. import (
    CfnResource as _CfnResource_9df397a6,
    CfnTag as _CfnTag_f6864754,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnCampaign(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnCampaign",
):
    '''A CloudFormation ``AWS::IoTFleetWise::Campaign``.

    :cloudformationResource: AWS::IoTFleetWise::Campaign
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iotfleetwise as iotfleetwise
        
        cfn_campaign = iotfleetwise.CfnCampaign(self, "MyCfnCampaign",
            action="action",
            collection_scheme=iotfleetwise.CfnCampaign.CollectionSchemeProperty(
                condition_based_collection_scheme=iotfleetwise.CfnCampaign.ConditionBasedCollectionSchemeProperty(
                    expression="expression",
        
                    # the properties below are optional
                    condition_language_version=123,
                    minimum_trigger_interval_ms=123,
                    trigger_mode="triggerMode"
                ),
                time_based_collection_scheme=iotfleetwise.CfnCampaign.TimeBasedCollectionSchemeProperty(
                    period_ms=123
                )
            ),
            name="name",
            signal_catalog_arn="signalCatalogArn",
            target_arn="targetArn",
        
            # the properties below are optional
            compression="compression",
            data_extra_dimensions=["dataExtraDimensions"],
            description="description",
            diagnostics_mode="diagnosticsMode",
            expiry_time="expiryTime",
            post_trigger_collection_duration=123,
            priority=123,
            signals_to_collect=[iotfleetwise.CfnCampaign.SignalInformationProperty(
                name="name",
        
                # the properties below are optional
                max_sample_count=123,
                minimum_sampling_interval_ms=123
            )],
            spooling_mode="spoolingMode",
            start_time="startTime",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        action: builtins.str,
        collection_scheme: typing.Union[typing.Union["CfnCampaign.CollectionSchemeProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b],
        name: builtins.str,
        signal_catalog_arn: builtins.str,
        target_arn: builtins.str,
        compression: typing.Optional[builtins.str] = None,
        data_extra_dimensions: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        diagnostics_mode: typing.Optional[builtins.str] = None,
        expiry_time: typing.Optional[builtins.str] = None,
        post_trigger_collection_duration: typing.Optional[jsii.Number] = None,
        priority: typing.Optional[jsii.Number] = None,
        signals_to_collect: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnCampaign.SignalInformationProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        spooling_mode: typing.Optional[builtins.str] = None,
        start_time: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::IoTFleetWise::Campaign``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param action: ``AWS::IoTFleetWise::Campaign.Action``.
        :param collection_scheme: ``AWS::IoTFleetWise::Campaign.CollectionScheme``.
        :param name: ``AWS::IoTFleetWise::Campaign.Name``.
        :param signal_catalog_arn: ``AWS::IoTFleetWise::Campaign.SignalCatalogArn``.
        :param target_arn: ``AWS::IoTFleetWise::Campaign.TargetArn``.
        :param compression: ``AWS::IoTFleetWise::Campaign.Compression``.
        :param data_extra_dimensions: ``AWS::IoTFleetWise::Campaign.DataExtraDimensions``.
        :param description: ``AWS::IoTFleetWise::Campaign.Description``.
        :param diagnostics_mode: ``AWS::IoTFleetWise::Campaign.DiagnosticsMode``.
        :param expiry_time: ``AWS::IoTFleetWise::Campaign.ExpiryTime``.
        :param post_trigger_collection_duration: ``AWS::IoTFleetWise::Campaign.PostTriggerCollectionDuration``.
        :param priority: ``AWS::IoTFleetWise::Campaign.Priority``.
        :param signals_to_collect: ``AWS::IoTFleetWise::Campaign.SignalsToCollect``.
        :param spooling_mode: ``AWS::IoTFleetWise::Campaign.SpoolingMode``.
        :param start_time: ``AWS::IoTFleetWise::Campaign.StartTime``.
        :param tags: ``AWS::IoTFleetWise::Campaign.Tags``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7abc45d2046b48ec3bc5807ec2826a784930a5009b41b194dd6e4bed2413f8d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCampaignProps(
            action=action,
            collection_scheme=collection_scheme,
            name=name,
            signal_catalog_arn=signal_catalog_arn,
            target_arn=target_arn,
            compression=compression,
            data_extra_dimensions=data_extra_dimensions,
            description=description,
            diagnostics_mode=diagnostics_mode,
            expiry_time=expiry_time,
            post_trigger_collection_duration=post_trigger_collection_duration,
            priority=priority,
            signals_to_collect=signals_to_collect,
            spooling_mode=spooling_mode,
            start_time=start_time,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09fbf1d259fb24b3ffc81851949fdbc1abbaa3df7fef9d0031938dd5b723205f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__89d4f6e55fdf4b8418716e773b2a62dc1763b8a2553490a7567e2cfe6f27d77f)
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
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModificationTime")
    def attr_last_modification_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: LastModificationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastModificationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''``AWS::IoTFleetWise::Campaign.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        '''``AWS::IoTFleetWise::Campaign.Action``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-action
        '''
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66dafa89e69b8562346040c56213280b8861d04a6b73911f5471941f58e3d463)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="collectionScheme")
    def collection_scheme(
        self,
    ) -> typing.Union["CfnCampaign.CollectionSchemeProperty", _IResolvable_da3f097b]:
        '''``AWS::IoTFleetWise::Campaign.CollectionScheme``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-collectionscheme
        '''
        return typing.cast(typing.Union["CfnCampaign.CollectionSchemeProperty", _IResolvable_da3f097b], jsii.get(self, "collectionScheme"))

    @collection_scheme.setter
    def collection_scheme(
        self,
        value: typing.Union["CfnCampaign.CollectionSchemeProperty", _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__868a9ff35e32583e37d3c029fdca22ea031055a38c7dd0dcbfa1f30846ee551d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "collectionScheme", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::IoTFleetWise::Campaign.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61dfb8819034de21f19e0466ab15e542f6b7270be82092cfffb60970bbc9708b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="signalCatalogArn")
    def signal_catalog_arn(self) -> builtins.str:
        '''``AWS::IoTFleetWise::Campaign.SignalCatalogArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-signalcatalogarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "signalCatalogArn"))

    @signal_catalog_arn.setter
    def signal_catalog_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5a5ce376850a7a86f93938b2f133fca5cc48d27769ddbdcaf2291ab00d48bac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signalCatalogArn", value)

    @builtins.property
    @jsii.member(jsii_name="targetArn")
    def target_arn(self) -> builtins.str:
        '''``AWS::IoTFleetWise::Campaign.TargetArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-targetarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "targetArn"))

    @target_arn.setter
    def target_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6154b7ad20e73a4e23143d3707a09d050bbb1092b307bc8e0145589083575f5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetArn", value)

    @builtins.property
    @jsii.member(jsii_name="compression")
    def compression(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::Campaign.Compression``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-compression
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "compression"))

    @compression.setter
    def compression(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17ec1dfb29d11e0d55dc84fc23937babfb2d1e33fdf8192c23c4130716fa6a02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compression", value)

    @builtins.property
    @jsii.member(jsii_name="dataExtraDimensions")
    def data_extra_dimensions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::IoTFleetWise::Campaign.DataExtraDimensions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-dataextradimensions
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dataExtraDimensions"))

    @data_extra_dimensions.setter
    def data_extra_dimensions(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d948dada7b0177410b9932e42eb5ef3a76fe3c3274594fb0b3ffa49ded440324)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataExtraDimensions", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::Campaign.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24bd4808a24c1ef5c17e4550fe902693202fc86dca7d97ddddcd994c722276bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="diagnosticsMode")
    def diagnostics_mode(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::Campaign.DiagnosticsMode``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-diagnosticsmode
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "diagnosticsMode"))

    @diagnostics_mode.setter
    def diagnostics_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e28d99e6bd56db5b97b272b04aeb5c1af8103d1b8b0080fe05d1a5f2fb149e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diagnosticsMode", value)

    @builtins.property
    @jsii.member(jsii_name="expiryTime")
    def expiry_time(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::Campaign.ExpiryTime``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-expirytime
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expiryTime"))

    @expiry_time.setter
    def expiry_time(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11cce95e76c12143123da5bc8c755592e90256d2ed3e61b6cd5a6d839e9318e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expiryTime", value)

    @builtins.property
    @jsii.member(jsii_name="postTriggerCollectionDuration")
    def post_trigger_collection_duration(self) -> typing.Optional[jsii.Number]:
        '''``AWS::IoTFleetWise::Campaign.PostTriggerCollectionDuration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-posttriggercollectionduration
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "postTriggerCollectionDuration"))

    @post_trigger_collection_duration.setter
    def post_trigger_collection_duration(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__660bebd5ebd77dcec64e7fcb6fd086f3ce7252832c2b9967a58fbda5d5fe6bd2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "postTriggerCollectionDuration", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> typing.Optional[jsii.Number]:
        '''``AWS::IoTFleetWise::Campaign.Priority``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-priority
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7eceb1aaf4de04c54d69e423a5e6de547b2e207a605050b36deefed0ccc4c9b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="signalsToCollect")
    def signals_to_collect(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnCampaign.SignalInformationProperty", _IResolvable_da3f097b]]]]:
        '''``AWS::IoTFleetWise::Campaign.SignalsToCollect``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-signalstocollect
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnCampaign.SignalInformationProperty", _IResolvable_da3f097b]]]], jsii.get(self, "signalsToCollect"))

    @signals_to_collect.setter
    def signals_to_collect(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnCampaign.SignalInformationProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49e9a686748dfc74bfa8ee7c7e9c87ccd64dc236b6b72144f22cebb87065a3d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signalsToCollect", value)

    @builtins.property
    @jsii.member(jsii_name="spoolingMode")
    def spooling_mode(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::Campaign.SpoolingMode``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-spoolingmode
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "spoolingMode"))

    @spooling_mode.setter
    def spooling_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2470f955a4e2089dd25722e38734a0e9fffc60420def257c19a15c6db378b523)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spoolingMode", value)

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::Campaign.StartTime``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-starttime
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startTime"))

    @start_time.setter
    def start_time(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67bb9c23f09e7b35b9a93baa91bd26954a931e9dac0ecfa4b472a8de197849a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTime", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnCampaign.CollectionSchemeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "condition_based_collection_scheme": "conditionBasedCollectionScheme",
            "time_based_collection_scheme": "timeBasedCollectionScheme",
        },
    )
    class CollectionSchemeProperty:
        def __init__(
            self,
            *,
            condition_based_collection_scheme: typing.Optional[typing.Union[typing.Union["CfnCampaign.ConditionBasedCollectionSchemeProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
            time_based_collection_scheme: typing.Optional[typing.Union[typing.Union["CfnCampaign.TimeBasedCollectionSchemeProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param condition_based_collection_scheme: ``CfnCampaign.CollectionSchemeProperty.ConditionBasedCollectionScheme``.
            :param time_based_collection_scheme: ``CfnCampaign.CollectionSchemeProperty.TimeBasedCollectionScheme``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-collectionscheme.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotfleetwise as iotfleetwise
                
                collection_scheme_property = iotfleetwise.CfnCampaign.CollectionSchemeProperty(
                    condition_based_collection_scheme=iotfleetwise.CfnCampaign.ConditionBasedCollectionSchemeProperty(
                        expression="expression",
                
                        # the properties below are optional
                        condition_language_version=123,
                        minimum_trigger_interval_ms=123,
                        trigger_mode="triggerMode"
                    ),
                    time_based_collection_scheme=iotfleetwise.CfnCampaign.TimeBasedCollectionSchemeProperty(
                        period_ms=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1d2862e457404e83c11e21830d9ccb15c52f442305bb2db0a1ebf80b0de3877a)
                check_type(argname="argument condition_based_collection_scheme", value=condition_based_collection_scheme, expected_type=type_hints["condition_based_collection_scheme"])
                check_type(argname="argument time_based_collection_scheme", value=time_based_collection_scheme, expected_type=type_hints["time_based_collection_scheme"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if condition_based_collection_scheme is not None:
                self._values["condition_based_collection_scheme"] = condition_based_collection_scheme
            if time_based_collection_scheme is not None:
                self._values["time_based_collection_scheme"] = time_based_collection_scheme

        @builtins.property
        def condition_based_collection_scheme(
            self,
        ) -> typing.Optional[typing.Union["CfnCampaign.ConditionBasedCollectionSchemeProperty", _IResolvable_da3f097b]]:
            '''``CfnCampaign.CollectionSchemeProperty.ConditionBasedCollectionScheme``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-collectionscheme.html#cfn-iotfleetwise-campaign-collectionscheme-conditionbasedcollectionscheme
            '''
            result = self._values.get("condition_based_collection_scheme")
            return typing.cast(typing.Optional[typing.Union["CfnCampaign.ConditionBasedCollectionSchemeProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def time_based_collection_scheme(
            self,
        ) -> typing.Optional[typing.Union["CfnCampaign.TimeBasedCollectionSchemeProperty", _IResolvable_da3f097b]]:
            '''``CfnCampaign.CollectionSchemeProperty.TimeBasedCollectionScheme``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-collectionscheme.html#cfn-iotfleetwise-campaign-collectionscheme-timebasedcollectionscheme
            '''
            result = self._values.get("time_based_collection_scheme")
            return typing.cast(typing.Optional[typing.Union["CfnCampaign.TimeBasedCollectionSchemeProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CollectionSchemeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnCampaign.ConditionBasedCollectionSchemeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "expression": "expression",
            "condition_language_version": "conditionLanguageVersion",
            "minimum_trigger_interval_ms": "minimumTriggerIntervalMs",
            "trigger_mode": "triggerMode",
        },
    )
    class ConditionBasedCollectionSchemeProperty:
        def __init__(
            self,
            *,
            expression: builtins.str,
            condition_language_version: typing.Optional[jsii.Number] = None,
            minimum_trigger_interval_ms: typing.Optional[jsii.Number] = None,
            trigger_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param expression: ``CfnCampaign.ConditionBasedCollectionSchemeProperty.Expression``.
            :param condition_language_version: ``CfnCampaign.ConditionBasedCollectionSchemeProperty.ConditionLanguageVersion``.
            :param minimum_trigger_interval_ms: ``CfnCampaign.ConditionBasedCollectionSchemeProperty.MinimumTriggerIntervalMs``.
            :param trigger_mode: ``CfnCampaign.ConditionBasedCollectionSchemeProperty.TriggerMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-conditionbasedcollectionscheme.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotfleetwise as iotfleetwise
                
                condition_based_collection_scheme_property = iotfleetwise.CfnCampaign.ConditionBasedCollectionSchemeProperty(
                    expression="expression",
                
                    # the properties below are optional
                    condition_language_version=123,
                    minimum_trigger_interval_ms=123,
                    trigger_mode="triggerMode"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dd3351de9470a98f13f006dd95deedef6c30dbfc08cdfe7bde2b9d950d547615)
                check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
                check_type(argname="argument condition_language_version", value=condition_language_version, expected_type=type_hints["condition_language_version"])
                check_type(argname="argument minimum_trigger_interval_ms", value=minimum_trigger_interval_ms, expected_type=type_hints["minimum_trigger_interval_ms"])
                check_type(argname="argument trigger_mode", value=trigger_mode, expected_type=type_hints["trigger_mode"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "expression": expression,
            }
            if condition_language_version is not None:
                self._values["condition_language_version"] = condition_language_version
            if minimum_trigger_interval_ms is not None:
                self._values["minimum_trigger_interval_ms"] = minimum_trigger_interval_ms
            if trigger_mode is not None:
                self._values["trigger_mode"] = trigger_mode

        @builtins.property
        def expression(self) -> builtins.str:
            '''``CfnCampaign.ConditionBasedCollectionSchemeProperty.Expression``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-conditionbasedcollectionscheme.html#cfn-iotfleetwise-campaign-conditionbasedcollectionscheme-expression
            '''
            result = self._values.get("expression")
            assert result is not None, "Required property 'expression' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def condition_language_version(self) -> typing.Optional[jsii.Number]:
            '''``CfnCampaign.ConditionBasedCollectionSchemeProperty.ConditionLanguageVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-conditionbasedcollectionscheme.html#cfn-iotfleetwise-campaign-conditionbasedcollectionscheme-conditionlanguageversion
            '''
            result = self._values.get("condition_language_version")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def minimum_trigger_interval_ms(self) -> typing.Optional[jsii.Number]:
            '''``CfnCampaign.ConditionBasedCollectionSchemeProperty.MinimumTriggerIntervalMs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-conditionbasedcollectionscheme.html#cfn-iotfleetwise-campaign-conditionbasedcollectionscheme-minimumtriggerintervalms
            '''
            result = self._values.get("minimum_trigger_interval_ms")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def trigger_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnCampaign.ConditionBasedCollectionSchemeProperty.TriggerMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-conditionbasedcollectionscheme.html#cfn-iotfleetwise-campaign-conditionbasedcollectionscheme-triggermode
            '''
            result = self._values.get("trigger_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConditionBasedCollectionSchemeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnCampaign.SignalInformationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "max_sample_count": "maxSampleCount",
            "minimum_sampling_interval_ms": "minimumSamplingIntervalMs",
        },
    )
    class SignalInformationProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            max_sample_count: typing.Optional[jsii.Number] = None,
            minimum_sampling_interval_ms: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param name: ``CfnCampaign.SignalInformationProperty.Name``.
            :param max_sample_count: ``CfnCampaign.SignalInformationProperty.MaxSampleCount``.
            :param minimum_sampling_interval_ms: ``CfnCampaign.SignalInformationProperty.MinimumSamplingIntervalMs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-signalinformation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotfleetwise as iotfleetwise
                
                signal_information_property = iotfleetwise.CfnCampaign.SignalInformationProperty(
                    name="name",
                
                    # the properties below are optional
                    max_sample_count=123,
                    minimum_sampling_interval_ms=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__53d5027f8c4da8a26f3f9cf9e5ab42f41c46c70820c567f2c340ad26784c6997)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument max_sample_count", value=max_sample_count, expected_type=type_hints["max_sample_count"])
                check_type(argname="argument minimum_sampling_interval_ms", value=minimum_sampling_interval_ms, expected_type=type_hints["minimum_sampling_interval_ms"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }
            if max_sample_count is not None:
                self._values["max_sample_count"] = max_sample_count
            if minimum_sampling_interval_ms is not None:
                self._values["minimum_sampling_interval_ms"] = minimum_sampling_interval_ms

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnCampaign.SignalInformationProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-signalinformation.html#cfn-iotfleetwise-campaign-signalinformation-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def max_sample_count(self) -> typing.Optional[jsii.Number]:
            '''``CfnCampaign.SignalInformationProperty.MaxSampleCount``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-signalinformation.html#cfn-iotfleetwise-campaign-signalinformation-maxsamplecount
            '''
            result = self._values.get("max_sample_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def minimum_sampling_interval_ms(self) -> typing.Optional[jsii.Number]:
            '''``CfnCampaign.SignalInformationProperty.MinimumSamplingIntervalMs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-signalinformation.html#cfn-iotfleetwise-campaign-signalinformation-minimumsamplingintervalms
            '''
            result = self._values.get("minimum_sampling_interval_ms")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SignalInformationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnCampaign.TimeBasedCollectionSchemeProperty",
        jsii_struct_bases=[],
        name_mapping={"period_ms": "periodMs"},
    )
    class TimeBasedCollectionSchemeProperty:
        def __init__(self, *, period_ms: jsii.Number) -> None:
            '''
            :param period_ms: ``CfnCampaign.TimeBasedCollectionSchemeProperty.PeriodMs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-timebasedcollectionscheme.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotfleetwise as iotfleetwise
                
                time_based_collection_scheme_property = iotfleetwise.CfnCampaign.TimeBasedCollectionSchemeProperty(
                    period_ms=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7bffeabbd9e812e2b77c405369e410069d9bd5d47737b57d4b23d11433d93329)
                check_type(argname="argument period_ms", value=period_ms, expected_type=type_hints["period_ms"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "period_ms": period_ms,
            }

        @builtins.property
        def period_ms(self) -> jsii.Number:
            '''``CfnCampaign.TimeBasedCollectionSchemeProperty.PeriodMs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-timebasedcollectionscheme.html#cfn-iotfleetwise-campaign-timebasedcollectionscheme-periodms
            '''
            result = self._values.get("period_ms")
            assert result is not None, "Required property 'period_ms' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TimeBasedCollectionSchemeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnCampaignProps",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "collection_scheme": "collectionScheme",
        "name": "name",
        "signal_catalog_arn": "signalCatalogArn",
        "target_arn": "targetArn",
        "compression": "compression",
        "data_extra_dimensions": "dataExtraDimensions",
        "description": "description",
        "diagnostics_mode": "diagnosticsMode",
        "expiry_time": "expiryTime",
        "post_trigger_collection_duration": "postTriggerCollectionDuration",
        "priority": "priority",
        "signals_to_collect": "signalsToCollect",
        "spooling_mode": "spoolingMode",
        "start_time": "startTime",
        "tags": "tags",
    },
)
class CfnCampaignProps:
    def __init__(
        self,
        *,
        action: builtins.str,
        collection_scheme: typing.Union[typing.Union[CfnCampaign.CollectionSchemeProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b],
        name: builtins.str,
        signal_catalog_arn: builtins.str,
        target_arn: builtins.str,
        compression: typing.Optional[builtins.str] = None,
        data_extra_dimensions: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        diagnostics_mode: typing.Optional[builtins.str] = None,
        expiry_time: typing.Optional[builtins.str] = None,
        post_trigger_collection_duration: typing.Optional[jsii.Number] = None,
        priority: typing.Optional[jsii.Number] = None,
        signals_to_collect: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnCampaign.SignalInformationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        spooling_mode: typing.Optional[builtins.str] = None,
        start_time: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCampaign``.

        :param action: ``AWS::IoTFleetWise::Campaign.Action``.
        :param collection_scheme: ``AWS::IoTFleetWise::Campaign.CollectionScheme``.
        :param name: ``AWS::IoTFleetWise::Campaign.Name``.
        :param signal_catalog_arn: ``AWS::IoTFleetWise::Campaign.SignalCatalogArn``.
        :param target_arn: ``AWS::IoTFleetWise::Campaign.TargetArn``.
        :param compression: ``AWS::IoTFleetWise::Campaign.Compression``.
        :param data_extra_dimensions: ``AWS::IoTFleetWise::Campaign.DataExtraDimensions``.
        :param description: ``AWS::IoTFleetWise::Campaign.Description``.
        :param diagnostics_mode: ``AWS::IoTFleetWise::Campaign.DiagnosticsMode``.
        :param expiry_time: ``AWS::IoTFleetWise::Campaign.ExpiryTime``.
        :param post_trigger_collection_duration: ``AWS::IoTFleetWise::Campaign.PostTriggerCollectionDuration``.
        :param priority: ``AWS::IoTFleetWise::Campaign.Priority``.
        :param signals_to_collect: ``AWS::IoTFleetWise::Campaign.SignalsToCollect``.
        :param spooling_mode: ``AWS::IoTFleetWise::Campaign.SpoolingMode``.
        :param start_time: ``AWS::IoTFleetWise::Campaign.StartTime``.
        :param tags: ``AWS::IoTFleetWise::Campaign.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iotfleetwise as iotfleetwise
            
            cfn_campaign_props = iotfleetwise.CfnCampaignProps(
                action="action",
                collection_scheme=iotfleetwise.CfnCampaign.CollectionSchemeProperty(
                    condition_based_collection_scheme=iotfleetwise.CfnCampaign.ConditionBasedCollectionSchemeProperty(
                        expression="expression",
            
                        # the properties below are optional
                        condition_language_version=123,
                        minimum_trigger_interval_ms=123,
                        trigger_mode="triggerMode"
                    ),
                    time_based_collection_scheme=iotfleetwise.CfnCampaign.TimeBasedCollectionSchemeProperty(
                        period_ms=123
                    )
                ),
                name="name",
                signal_catalog_arn="signalCatalogArn",
                target_arn="targetArn",
            
                # the properties below are optional
                compression="compression",
                data_extra_dimensions=["dataExtraDimensions"],
                description="description",
                diagnostics_mode="diagnosticsMode",
                expiry_time="expiryTime",
                post_trigger_collection_duration=123,
                priority=123,
                signals_to_collect=[iotfleetwise.CfnCampaign.SignalInformationProperty(
                    name="name",
            
                    # the properties below are optional
                    max_sample_count=123,
                    minimum_sampling_interval_ms=123
                )],
                spooling_mode="spoolingMode",
                start_time="startTime",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54c45792d3f0c102d3358acf678401b9616a7fee4b70882083776c5f9635cf71)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument collection_scheme", value=collection_scheme, expected_type=type_hints["collection_scheme"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument signal_catalog_arn", value=signal_catalog_arn, expected_type=type_hints["signal_catalog_arn"])
            check_type(argname="argument target_arn", value=target_arn, expected_type=type_hints["target_arn"])
            check_type(argname="argument compression", value=compression, expected_type=type_hints["compression"])
            check_type(argname="argument data_extra_dimensions", value=data_extra_dimensions, expected_type=type_hints["data_extra_dimensions"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument diagnostics_mode", value=diagnostics_mode, expected_type=type_hints["diagnostics_mode"])
            check_type(argname="argument expiry_time", value=expiry_time, expected_type=type_hints["expiry_time"])
            check_type(argname="argument post_trigger_collection_duration", value=post_trigger_collection_duration, expected_type=type_hints["post_trigger_collection_duration"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument signals_to_collect", value=signals_to_collect, expected_type=type_hints["signals_to_collect"])
            check_type(argname="argument spooling_mode", value=spooling_mode, expected_type=type_hints["spooling_mode"])
            check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action": action,
            "collection_scheme": collection_scheme,
            "name": name,
            "signal_catalog_arn": signal_catalog_arn,
            "target_arn": target_arn,
        }
        if compression is not None:
            self._values["compression"] = compression
        if data_extra_dimensions is not None:
            self._values["data_extra_dimensions"] = data_extra_dimensions
        if description is not None:
            self._values["description"] = description
        if diagnostics_mode is not None:
            self._values["diagnostics_mode"] = diagnostics_mode
        if expiry_time is not None:
            self._values["expiry_time"] = expiry_time
        if post_trigger_collection_duration is not None:
            self._values["post_trigger_collection_duration"] = post_trigger_collection_duration
        if priority is not None:
            self._values["priority"] = priority
        if signals_to_collect is not None:
            self._values["signals_to_collect"] = signals_to_collect
        if spooling_mode is not None:
            self._values["spooling_mode"] = spooling_mode
        if start_time is not None:
            self._values["start_time"] = start_time
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def action(self) -> builtins.str:
        '''``AWS::IoTFleetWise::Campaign.Action``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-action
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def collection_scheme(
        self,
    ) -> typing.Union[CfnCampaign.CollectionSchemeProperty, _IResolvable_da3f097b]:
        '''``AWS::IoTFleetWise::Campaign.CollectionScheme``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-collectionscheme
        '''
        result = self._values.get("collection_scheme")
        assert result is not None, "Required property 'collection_scheme' is missing"
        return typing.cast(typing.Union[CfnCampaign.CollectionSchemeProperty, _IResolvable_da3f097b], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::IoTFleetWise::Campaign.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def signal_catalog_arn(self) -> builtins.str:
        '''``AWS::IoTFleetWise::Campaign.SignalCatalogArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-signalcatalogarn
        '''
        result = self._values.get("signal_catalog_arn")
        assert result is not None, "Required property 'signal_catalog_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_arn(self) -> builtins.str:
        '''``AWS::IoTFleetWise::Campaign.TargetArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-targetarn
        '''
        result = self._values.get("target_arn")
        assert result is not None, "Required property 'target_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def compression(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::Campaign.Compression``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-compression
        '''
        result = self._values.get("compression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_extra_dimensions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::IoTFleetWise::Campaign.DataExtraDimensions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-dataextradimensions
        '''
        result = self._values.get("data_extra_dimensions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::Campaign.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def diagnostics_mode(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::Campaign.DiagnosticsMode``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-diagnosticsmode
        '''
        result = self._values.get("diagnostics_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expiry_time(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::Campaign.ExpiryTime``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-expirytime
        '''
        result = self._values.get("expiry_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def post_trigger_collection_duration(self) -> typing.Optional[jsii.Number]:
        '''``AWS::IoTFleetWise::Campaign.PostTriggerCollectionDuration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-posttriggercollectionduration
        '''
        result = self._values.get("post_trigger_collection_duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''``AWS::IoTFleetWise::Campaign.Priority``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-priority
        '''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def signals_to_collect(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnCampaign.SignalInformationProperty, _IResolvable_da3f097b]]]]:
        '''``AWS::IoTFleetWise::Campaign.SignalsToCollect``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-signalstocollect
        '''
        result = self._values.get("signals_to_collect")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnCampaign.SignalInformationProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def spooling_mode(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::Campaign.SpoolingMode``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-spoolingmode
        '''
        result = self._values.get("spooling_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_time(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::Campaign.StartTime``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-starttime
        '''
        result = self._values.get("start_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''``AWS::IoTFleetWise::Campaign.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCampaignProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnDecoderManifest(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnDecoderManifest",
):
    '''A CloudFormation ``AWS::IoTFleetWise::DecoderManifest``.

    :cloudformationResource: AWS::IoTFleetWise::DecoderManifest
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iotfleetwise as iotfleetwise
        
        cfn_decoder_manifest = iotfleetwise.CfnDecoderManifest(self, "MyCfnDecoderManifest",
            model_manifest_arn="modelManifestArn",
            name="name",
        
            # the properties below are optional
            description="description",
            network_interfaces=[iotfleetwise.CfnDecoderManifest.NetworkInterfacesItemsProperty(
                interface_id="interfaceId",
                type="type",
        
                # the properties below are optional
                can_interface=iotfleetwise.CfnDecoderManifest.CanInterfaceProperty(
                    name="name",
        
                    # the properties below are optional
                    protocol_name="protocolName",
                    protocol_version="protocolVersion"
                ),
                obd_interface=iotfleetwise.CfnDecoderManifest.ObdInterfaceProperty(
                    name="name",
                    request_message_id="requestMessageId",
        
                    # the properties below are optional
                    dtc_request_interval_seconds="dtcRequestIntervalSeconds",
                    has_transmission_ecu="hasTransmissionEcu",
                    obd_standard="obdStandard",
                    pid_request_interval_seconds="pidRequestIntervalSeconds",
                    use_extended_ids="useExtendedIds"
                )
            )],
            signal_decoders=[iotfleetwise.CfnDecoderManifest.SignalDecodersItemsProperty(
                fully_qualified_name="fullyQualifiedName",
                interface_id="interfaceId",
                type="type",
        
                # the properties below are optional
                can_signal=iotfleetwise.CfnDecoderManifest.CanSignalProperty(
                    factor="factor",
                    is_big_endian="isBigEndian",
                    is_signed="isSigned",
                    length="length",
                    message_id="messageId",
                    offset="offset",
                    start_bit="startBit",
        
                    # the properties below are optional
                    name="name"
                ),
                obd_signal=iotfleetwise.CfnDecoderManifest.ObdSignalProperty(
                    byte_length="byteLength",
                    offset="offset",
                    pid="pid",
                    pid_response_length="pidResponseLength",
                    scaling="scaling",
                    service_mode="serviceMode",
                    start_byte="startByte",
        
                    # the properties below are optional
                    bit_mask_length="bitMaskLength",
                    bit_right_shift="bitRightShift"
                )
            )],
            status="status",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        model_manifest_arn: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        network_interfaces: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnDecoderManifest.NetworkInterfacesItemsProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        signal_decoders: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnDecoderManifest.SignalDecodersItemsProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::IoTFleetWise::DecoderManifest``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param model_manifest_arn: ``AWS::IoTFleetWise::DecoderManifest.ModelManifestArn``.
        :param name: ``AWS::IoTFleetWise::DecoderManifest.Name``.
        :param description: ``AWS::IoTFleetWise::DecoderManifest.Description``.
        :param network_interfaces: ``AWS::IoTFleetWise::DecoderManifest.NetworkInterfaces``.
        :param signal_decoders: ``AWS::IoTFleetWise::DecoderManifest.SignalDecoders``.
        :param status: ``AWS::IoTFleetWise::DecoderManifest.Status``.
        :param tags: ``AWS::IoTFleetWise::DecoderManifest.Tags``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd0d8efce6baca0fa606fb0cf95bebcdeda196fcde2fb7e18542334332eb8ba4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDecoderManifestProps(
            model_manifest_arn=model_manifest_arn,
            name=name,
            description=description,
            network_interfaces=network_interfaces,
            signal_decoders=signal_decoders,
            status=status,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7c1f4e3cc81a06a60eef4d178a3aaf54f7c99cca4a0481a51c50d560d76ba09)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d12e1e0a1684404c74ecc86ed4ae33ffdac8b3611db04d45a6a46ef55c87bbbe)
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
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModificationTime")
    def attr_last_modification_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: LastModificationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastModificationTime"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''``AWS::IoTFleetWise::DecoderManifest.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html#cfn-iotfleetwise-decodermanifest-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="modelManifestArn")
    def model_manifest_arn(self) -> builtins.str:
        '''``AWS::IoTFleetWise::DecoderManifest.ModelManifestArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html#cfn-iotfleetwise-decodermanifest-modelmanifestarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "modelManifestArn"))

    @model_manifest_arn.setter
    def model_manifest_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b8f77dd16bf3c88bd7f097b2327803bb360213ddb0b320722348c6a1b99afce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "modelManifestArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::IoTFleetWise::DecoderManifest.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html#cfn-iotfleetwise-decodermanifest-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a5a43cce0da85f8ef5934babccfc93088317c19ae303a38ae3adc573ad6c633)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::DecoderManifest.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html#cfn-iotfleetwise-decodermanifest-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1e4501ad7312a6dac9b29817aed239a25a724386677541e036223da190a2d9b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="networkInterfaces")
    def network_interfaces(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDecoderManifest.NetworkInterfacesItemsProperty", _IResolvable_da3f097b]]]]:
        '''``AWS::IoTFleetWise::DecoderManifest.NetworkInterfaces``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html#cfn-iotfleetwise-decodermanifest-networkinterfaces
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDecoderManifest.NetworkInterfacesItemsProperty", _IResolvable_da3f097b]]]], jsii.get(self, "networkInterfaces"))

    @network_interfaces.setter
    def network_interfaces(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDecoderManifest.NetworkInterfacesItemsProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4059f7868b58b43acd642cd2537b59a16c939681bb626ef560a6efbc8d7cda5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkInterfaces", value)

    @builtins.property
    @jsii.member(jsii_name="signalDecoders")
    def signal_decoders(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDecoderManifest.SignalDecodersItemsProperty", _IResolvable_da3f097b]]]]:
        '''``AWS::IoTFleetWise::DecoderManifest.SignalDecoders``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html#cfn-iotfleetwise-decodermanifest-signaldecoders
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDecoderManifest.SignalDecodersItemsProperty", _IResolvable_da3f097b]]]], jsii.get(self, "signalDecoders"))

    @signal_decoders.setter
    def signal_decoders(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnDecoderManifest.SignalDecodersItemsProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32a124503ae0a9be522e3691aef89b61eb023aea0d8b57342dcef4a708073af0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signalDecoders", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::DecoderManifest.Status``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html#cfn-iotfleetwise-decodermanifest-status
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8428ef9254e1885dc4fbe7c358202136e77b7b7c68b9e9b92c6016edfca9ad8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnDecoderManifest.CanInterfaceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "protocol_name": "protocolName",
            "protocol_version": "protocolVersion",
        },
    )
    class CanInterfaceProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            protocol_name: typing.Optional[builtins.str] = None,
            protocol_version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param name: ``CfnDecoderManifest.CanInterfaceProperty.Name``.
            :param protocol_name: ``CfnDecoderManifest.CanInterfaceProperty.ProtocolName``.
            :param protocol_version: ``CfnDecoderManifest.CanInterfaceProperty.ProtocolVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-caninterface.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotfleetwise as iotfleetwise
                
                can_interface_property = iotfleetwise.CfnDecoderManifest.CanInterfaceProperty(
                    name="name",
                
                    # the properties below are optional
                    protocol_name="protocolName",
                    protocol_version="protocolVersion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f41ef25a35e6c8526ccaa9ecc87becb68ccffe031fd1ae9c650719807164dc68)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument protocol_name", value=protocol_name, expected_type=type_hints["protocol_name"])
                check_type(argname="argument protocol_version", value=protocol_version, expected_type=type_hints["protocol_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }
            if protocol_name is not None:
                self._values["protocol_name"] = protocol_name
            if protocol_version is not None:
                self._values["protocol_version"] = protocol_version

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnDecoderManifest.CanInterfaceProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-caninterface.html#cfn-iotfleetwise-decodermanifest-caninterface-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def protocol_name(self) -> typing.Optional[builtins.str]:
            '''``CfnDecoderManifest.CanInterfaceProperty.ProtocolName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-caninterface.html#cfn-iotfleetwise-decodermanifest-caninterface-protocolname
            '''
            result = self._values.get("protocol_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def protocol_version(self) -> typing.Optional[builtins.str]:
            '''``CfnDecoderManifest.CanInterfaceProperty.ProtocolVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-caninterface.html#cfn-iotfleetwise-decodermanifest-caninterface-protocolversion
            '''
            result = self._values.get("protocol_version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CanInterfaceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnDecoderManifest.CanSignalProperty",
        jsii_struct_bases=[],
        name_mapping={
            "factor": "factor",
            "is_big_endian": "isBigEndian",
            "is_signed": "isSigned",
            "length": "length",
            "message_id": "messageId",
            "offset": "offset",
            "start_bit": "startBit",
            "name": "name",
        },
    )
    class CanSignalProperty:
        def __init__(
            self,
            *,
            factor: builtins.str,
            is_big_endian: builtins.str,
            is_signed: builtins.str,
            length: builtins.str,
            message_id: builtins.str,
            offset: builtins.str,
            start_bit: builtins.str,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param factor: ``CfnDecoderManifest.CanSignalProperty.Factor``.
            :param is_big_endian: ``CfnDecoderManifest.CanSignalProperty.IsBigEndian``.
            :param is_signed: ``CfnDecoderManifest.CanSignalProperty.IsSigned``.
            :param length: ``CfnDecoderManifest.CanSignalProperty.Length``.
            :param message_id: ``CfnDecoderManifest.CanSignalProperty.MessageId``.
            :param offset: ``CfnDecoderManifest.CanSignalProperty.Offset``.
            :param start_bit: ``CfnDecoderManifest.CanSignalProperty.StartBit``.
            :param name: ``CfnDecoderManifest.CanSignalProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignal.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotfleetwise as iotfleetwise
                
                can_signal_property = iotfleetwise.CfnDecoderManifest.CanSignalProperty(
                    factor="factor",
                    is_big_endian="isBigEndian",
                    is_signed="isSigned",
                    length="length",
                    message_id="messageId",
                    offset="offset",
                    start_bit="startBit",
                
                    # the properties below are optional
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d1fdd86137a92797754860d3b8da115496d862a2f95c8e39c08a70fdf76855c4)
                check_type(argname="argument factor", value=factor, expected_type=type_hints["factor"])
                check_type(argname="argument is_big_endian", value=is_big_endian, expected_type=type_hints["is_big_endian"])
                check_type(argname="argument is_signed", value=is_signed, expected_type=type_hints["is_signed"])
                check_type(argname="argument length", value=length, expected_type=type_hints["length"])
                check_type(argname="argument message_id", value=message_id, expected_type=type_hints["message_id"])
                check_type(argname="argument offset", value=offset, expected_type=type_hints["offset"])
                check_type(argname="argument start_bit", value=start_bit, expected_type=type_hints["start_bit"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "factor": factor,
                "is_big_endian": is_big_endian,
                "is_signed": is_signed,
                "length": length,
                "message_id": message_id,
                "offset": offset,
                "start_bit": start_bit,
            }
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def factor(self) -> builtins.str:
            '''``CfnDecoderManifest.CanSignalProperty.Factor``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignal.html#cfn-iotfleetwise-decodermanifest-cansignal-factor
            '''
            result = self._values.get("factor")
            assert result is not None, "Required property 'factor' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def is_big_endian(self) -> builtins.str:
            '''``CfnDecoderManifest.CanSignalProperty.IsBigEndian``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignal.html#cfn-iotfleetwise-decodermanifest-cansignal-isbigendian
            '''
            result = self._values.get("is_big_endian")
            assert result is not None, "Required property 'is_big_endian' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def is_signed(self) -> builtins.str:
            '''``CfnDecoderManifest.CanSignalProperty.IsSigned``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignal.html#cfn-iotfleetwise-decodermanifest-cansignal-issigned
            '''
            result = self._values.get("is_signed")
            assert result is not None, "Required property 'is_signed' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def length(self) -> builtins.str:
            '''``CfnDecoderManifest.CanSignalProperty.Length``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignal.html#cfn-iotfleetwise-decodermanifest-cansignal-length
            '''
            result = self._values.get("length")
            assert result is not None, "Required property 'length' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def message_id(self) -> builtins.str:
            '''``CfnDecoderManifest.CanSignalProperty.MessageId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignal.html#cfn-iotfleetwise-decodermanifest-cansignal-messageid
            '''
            result = self._values.get("message_id")
            assert result is not None, "Required property 'message_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def offset(self) -> builtins.str:
            '''``CfnDecoderManifest.CanSignalProperty.Offset``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignal.html#cfn-iotfleetwise-decodermanifest-cansignal-offset
            '''
            result = self._values.get("offset")
            assert result is not None, "Required property 'offset' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def start_bit(self) -> builtins.str:
            '''``CfnDecoderManifest.CanSignalProperty.StartBit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignal.html#cfn-iotfleetwise-decodermanifest-cansignal-startbit
            '''
            result = self._values.get("start_bit")
            assert result is not None, "Required property 'start_bit' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnDecoderManifest.CanSignalProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignal.html#cfn-iotfleetwise-decodermanifest-cansignal-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CanSignalProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnDecoderManifest.NetworkInterfacesItemsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "interface_id": "interfaceId",
            "type": "type",
            "can_interface": "canInterface",
            "obd_interface": "obdInterface",
        },
    )
    class NetworkInterfacesItemsProperty:
        def __init__(
            self,
            *,
            interface_id: builtins.str,
            type: builtins.str,
            can_interface: typing.Optional[typing.Union[typing.Union["CfnDecoderManifest.CanInterfaceProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
            obd_interface: typing.Optional[typing.Union[typing.Union["CfnDecoderManifest.ObdInterfaceProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param interface_id: ``CfnDecoderManifest.NetworkInterfacesItemsProperty.InterfaceId``.
            :param type: ``CfnDecoderManifest.NetworkInterfacesItemsProperty.Type``.
            :param can_interface: ``CfnDecoderManifest.NetworkInterfacesItemsProperty.CanInterface``.
            :param obd_interface: ``CfnDecoderManifest.NetworkInterfacesItemsProperty.ObdInterface``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-networkinterfacesitems.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotfleetwise as iotfleetwise
                
                network_interfaces_items_property = iotfleetwise.CfnDecoderManifest.NetworkInterfacesItemsProperty(
                    interface_id="interfaceId",
                    type="type",
                
                    # the properties below are optional
                    can_interface=iotfleetwise.CfnDecoderManifest.CanInterfaceProperty(
                        name="name",
                
                        # the properties below are optional
                        protocol_name="protocolName",
                        protocol_version="protocolVersion"
                    ),
                    obd_interface=iotfleetwise.CfnDecoderManifest.ObdInterfaceProperty(
                        name="name",
                        request_message_id="requestMessageId",
                
                        # the properties below are optional
                        dtc_request_interval_seconds="dtcRequestIntervalSeconds",
                        has_transmission_ecu="hasTransmissionEcu",
                        obd_standard="obdStandard",
                        pid_request_interval_seconds="pidRequestIntervalSeconds",
                        use_extended_ids="useExtendedIds"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__763a8a9c006b5f64d4a07d45a9f83b3a4b0be692630292c6e33fd7f6c09a4c07)
                check_type(argname="argument interface_id", value=interface_id, expected_type=type_hints["interface_id"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument can_interface", value=can_interface, expected_type=type_hints["can_interface"])
                check_type(argname="argument obd_interface", value=obd_interface, expected_type=type_hints["obd_interface"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "interface_id": interface_id,
                "type": type,
            }
            if can_interface is not None:
                self._values["can_interface"] = can_interface
            if obd_interface is not None:
                self._values["obd_interface"] = obd_interface

        @builtins.property
        def interface_id(self) -> builtins.str:
            '''``CfnDecoderManifest.NetworkInterfacesItemsProperty.InterfaceId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-networkinterfacesitems.html#cfn-iotfleetwise-decodermanifest-networkinterfacesitems-interfaceid
            '''
            result = self._values.get("interface_id")
            assert result is not None, "Required property 'interface_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''``CfnDecoderManifest.NetworkInterfacesItemsProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-networkinterfacesitems.html#cfn-iotfleetwise-decodermanifest-networkinterfacesitems-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def can_interface(
            self,
        ) -> typing.Optional[typing.Union["CfnDecoderManifest.CanInterfaceProperty", _IResolvable_da3f097b]]:
            '''``CfnDecoderManifest.NetworkInterfacesItemsProperty.CanInterface``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-networkinterfacesitems.html#cfn-iotfleetwise-decodermanifest-networkinterfacesitems-caninterface
            '''
            result = self._values.get("can_interface")
            return typing.cast(typing.Optional[typing.Union["CfnDecoderManifest.CanInterfaceProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def obd_interface(
            self,
        ) -> typing.Optional[typing.Union["CfnDecoderManifest.ObdInterfaceProperty", _IResolvable_da3f097b]]:
            '''``CfnDecoderManifest.NetworkInterfacesItemsProperty.ObdInterface``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-networkinterfacesitems.html#cfn-iotfleetwise-decodermanifest-networkinterfacesitems-obdinterface
            '''
            result = self._values.get("obd_interface")
            return typing.cast(typing.Optional[typing.Union["CfnDecoderManifest.ObdInterfaceProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkInterfacesItemsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnDecoderManifest.ObdInterfaceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "request_message_id": "requestMessageId",
            "dtc_request_interval_seconds": "dtcRequestIntervalSeconds",
            "has_transmission_ecu": "hasTransmissionEcu",
            "obd_standard": "obdStandard",
            "pid_request_interval_seconds": "pidRequestIntervalSeconds",
            "use_extended_ids": "useExtendedIds",
        },
    )
    class ObdInterfaceProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            request_message_id: builtins.str,
            dtc_request_interval_seconds: typing.Optional[builtins.str] = None,
            has_transmission_ecu: typing.Optional[builtins.str] = None,
            obd_standard: typing.Optional[builtins.str] = None,
            pid_request_interval_seconds: typing.Optional[builtins.str] = None,
            use_extended_ids: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param name: ``CfnDecoderManifest.ObdInterfaceProperty.Name``.
            :param request_message_id: ``CfnDecoderManifest.ObdInterfaceProperty.RequestMessageId``.
            :param dtc_request_interval_seconds: ``CfnDecoderManifest.ObdInterfaceProperty.DtcRequestIntervalSeconds``.
            :param has_transmission_ecu: ``CfnDecoderManifest.ObdInterfaceProperty.HasTransmissionEcu``.
            :param obd_standard: ``CfnDecoderManifest.ObdInterfaceProperty.ObdStandard``.
            :param pid_request_interval_seconds: ``CfnDecoderManifest.ObdInterfaceProperty.PidRequestIntervalSeconds``.
            :param use_extended_ids: ``CfnDecoderManifest.ObdInterfaceProperty.UseExtendedIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdinterface.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotfleetwise as iotfleetwise
                
                obd_interface_property = iotfleetwise.CfnDecoderManifest.ObdInterfaceProperty(
                    name="name",
                    request_message_id="requestMessageId",
                
                    # the properties below are optional
                    dtc_request_interval_seconds="dtcRequestIntervalSeconds",
                    has_transmission_ecu="hasTransmissionEcu",
                    obd_standard="obdStandard",
                    pid_request_interval_seconds="pidRequestIntervalSeconds",
                    use_extended_ids="useExtendedIds"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__619deb4a5a81c6ae8bcb58cd0d96a9beddd6b7ac867f4e945e1bd4668fc25b17)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument request_message_id", value=request_message_id, expected_type=type_hints["request_message_id"])
                check_type(argname="argument dtc_request_interval_seconds", value=dtc_request_interval_seconds, expected_type=type_hints["dtc_request_interval_seconds"])
                check_type(argname="argument has_transmission_ecu", value=has_transmission_ecu, expected_type=type_hints["has_transmission_ecu"])
                check_type(argname="argument obd_standard", value=obd_standard, expected_type=type_hints["obd_standard"])
                check_type(argname="argument pid_request_interval_seconds", value=pid_request_interval_seconds, expected_type=type_hints["pid_request_interval_seconds"])
                check_type(argname="argument use_extended_ids", value=use_extended_ids, expected_type=type_hints["use_extended_ids"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "request_message_id": request_message_id,
            }
            if dtc_request_interval_seconds is not None:
                self._values["dtc_request_interval_seconds"] = dtc_request_interval_seconds
            if has_transmission_ecu is not None:
                self._values["has_transmission_ecu"] = has_transmission_ecu
            if obd_standard is not None:
                self._values["obd_standard"] = obd_standard
            if pid_request_interval_seconds is not None:
                self._values["pid_request_interval_seconds"] = pid_request_interval_seconds
            if use_extended_ids is not None:
                self._values["use_extended_ids"] = use_extended_ids

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnDecoderManifest.ObdInterfaceProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdinterface.html#cfn-iotfleetwise-decodermanifest-obdinterface-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def request_message_id(self) -> builtins.str:
            '''``CfnDecoderManifest.ObdInterfaceProperty.RequestMessageId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdinterface.html#cfn-iotfleetwise-decodermanifest-obdinterface-requestmessageid
            '''
            result = self._values.get("request_message_id")
            assert result is not None, "Required property 'request_message_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def dtc_request_interval_seconds(self) -> typing.Optional[builtins.str]:
            '''``CfnDecoderManifest.ObdInterfaceProperty.DtcRequestIntervalSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdinterface.html#cfn-iotfleetwise-decodermanifest-obdinterface-dtcrequestintervalseconds
            '''
            result = self._values.get("dtc_request_interval_seconds")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def has_transmission_ecu(self) -> typing.Optional[builtins.str]:
            '''``CfnDecoderManifest.ObdInterfaceProperty.HasTransmissionEcu``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdinterface.html#cfn-iotfleetwise-decodermanifest-obdinterface-hastransmissionecu
            '''
            result = self._values.get("has_transmission_ecu")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def obd_standard(self) -> typing.Optional[builtins.str]:
            '''``CfnDecoderManifest.ObdInterfaceProperty.ObdStandard``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdinterface.html#cfn-iotfleetwise-decodermanifest-obdinterface-obdstandard
            '''
            result = self._values.get("obd_standard")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def pid_request_interval_seconds(self) -> typing.Optional[builtins.str]:
            '''``CfnDecoderManifest.ObdInterfaceProperty.PidRequestIntervalSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdinterface.html#cfn-iotfleetwise-decodermanifest-obdinterface-pidrequestintervalseconds
            '''
            result = self._values.get("pid_request_interval_seconds")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def use_extended_ids(self) -> typing.Optional[builtins.str]:
            '''``CfnDecoderManifest.ObdInterfaceProperty.UseExtendedIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdinterface.html#cfn-iotfleetwise-decodermanifest-obdinterface-useextendedids
            '''
            result = self._values.get("use_extended_ids")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ObdInterfaceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnDecoderManifest.ObdSignalProperty",
        jsii_struct_bases=[],
        name_mapping={
            "byte_length": "byteLength",
            "offset": "offset",
            "pid": "pid",
            "pid_response_length": "pidResponseLength",
            "scaling": "scaling",
            "service_mode": "serviceMode",
            "start_byte": "startByte",
            "bit_mask_length": "bitMaskLength",
            "bit_right_shift": "bitRightShift",
        },
    )
    class ObdSignalProperty:
        def __init__(
            self,
            *,
            byte_length: builtins.str,
            offset: builtins.str,
            pid: builtins.str,
            pid_response_length: builtins.str,
            scaling: builtins.str,
            service_mode: builtins.str,
            start_byte: builtins.str,
            bit_mask_length: typing.Optional[builtins.str] = None,
            bit_right_shift: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param byte_length: ``CfnDecoderManifest.ObdSignalProperty.ByteLength``.
            :param offset: ``CfnDecoderManifest.ObdSignalProperty.Offset``.
            :param pid: ``CfnDecoderManifest.ObdSignalProperty.Pid``.
            :param pid_response_length: ``CfnDecoderManifest.ObdSignalProperty.PidResponseLength``.
            :param scaling: ``CfnDecoderManifest.ObdSignalProperty.Scaling``.
            :param service_mode: ``CfnDecoderManifest.ObdSignalProperty.ServiceMode``.
            :param start_byte: ``CfnDecoderManifest.ObdSignalProperty.StartByte``.
            :param bit_mask_length: ``CfnDecoderManifest.ObdSignalProperty.BitMaskLength``.
            :param bit_right_shift: ``CfnDecoderManifest.ObdSignalProperty.BitRightShift``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignal.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotfleetwise as iotfleetwise
                
                obd_signal_property = iotfleetwise.CfnDecoderManifest.ObdSignalProperty(
                    byte_length="byteLength",
                    offset="offset",
                    pid="pid",
                    pid_response_length="pidResponseLength",
                    scaling="scaling",
                    service_mode="serviceMode",
                    start_byte="startByte",
                
                    # the properties below are optional
                    bit_mask_length="bitMaskLength",
                    bit_right_shift="bitRightShift"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ccb776ce607aa563ef4bc105956ab186267e45066ee492c162a4555709004e4b)
                check_type(argname="argument byte_length", value=byte_length, expected_type=type_hints["byte_length"])
                check_type(argname="argument offset", value=offset, expected_type=type_hints["offset"])
                check_type(argname="argument pid", value=pid, expected_type=type_hints["pid"])
                check_type(argname="argument pid_response_length", value=pid_response_length, expected_type=type_hints["pid_response_length"])
                check_type(argname="argument scaling", value=scaling, expected_type=type_hints["scaling"])
                check_type(argname="argument service_mode", value=service_mode, expected_type=type_hints["service_mode"])
                check_type(argname="argument start_byte", value=start_byte, expected_type=type_hints["start_byte"])
                check_type(argname="argument bit_mask_length", value=bit_mask_length, expected_type=type_hints["bit_mask_length"])
                check_type(argname="argument bit_right_shift", value=bit_right_shift, expected_type=type_hints["bit_right_shift"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "byte_length": byte_length,
                "offset": offset,
                "pid": pid,
                "pid_response_length": pid_response_length,
                "scaling": scaling,
                "service_mode": service_mode,
                "start_byte": start_byte,
            }
            if bit_mask_length is not None:
                self._values["bit_mask_length"] = bit_mask_length
            if bit_right_shift is not None:
                self._values["bit_right_shift"] = bit_right_shift

        @builtins.property
        def byte_length(self) -> builtins.str:
            '''``CfnDecoderManifest.ObdSignalProperty.ByteLength``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignal.html#cfn-iotfleetwise-decodermanifest-obdsignal-bytelength
            '''
            result = self._values.get("byte_length")
            assert result is not None, "Required property 'byte_length' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def offset(self) -> builtins.str:
            '''``CfnDecoderManifest.ObdSignalProperty.Offset``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignal.html#cfn-iotfleetwise-decodermanifest-obdsignal-offset
            '''
            result = self._values.get("offset")
            assert result is not None, "Required property 'offset' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def pid(self) -> builtins.str:
            '''``CfnDecoderManifest.ObdSignalProperty.Pid``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignal.html#cfn-iotfleetwise-decodermanifest-obdsignal-pid
            '''
            result = self._values.get("pid")
            assert result is not None, "Required property 'pid' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def pid_response_length(self) -> builtins.str:
            '''``CfnDecoderManifest.ObdSignalProperty.PidResponseLength``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignal.html#cfn-iotfleetwise-decodermanifest-obdsignal-pidresponselength
            '''
            result = self._values.get("pid_response_length")
            assert result is not None, "Required property 'pid_response_length' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def scaling(self) -> builtins.str:
            '''``CfnDecoderManifest.ObdSignalProperty.Scaling``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignal.html#cfn-iotfleetwise-decodermanifest-obdsignal-scaling
            '''
            result = self._values.get("scaling")
            assert result is not None, "Required property 'scaling' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def service_mode(self) -> builtins.str:
            '''``CfnDecoderManifest.ObdSignalProperty.ServiceMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignal.html#cfn-iotfleetwise-decodermanifest-obdsignal-servicemode
            '''
            result = self._values.get("service_mode")
            assert result is not None, "Required property 'service_mode' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def start_byte(self) -> builtins.str:
            '''``CfnDecoderManifest.ObdSignalProperty.StartByte``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignal.html#cfn-iotfleetwise-decodermanifest-obdsignal-startbyte
            '''
            result = self._values.get("start_byte")
            assert result is not None, "Required property 'start_byte' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def bit_mask_length(self) -> typing.Optional[builtins.str]:
            '''``CfnDecoderManifest.ObdSignalProperty.BitMaskLength``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignal.html#cfn-iotfleetwise-decodermanifest-obdsignal-bitmasklength
            '''
            result = self._values.get("bit_mask_length")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def bit_right_shift(self) -> typing.Optional[builtins.str]:
            '''``CfnDecoderManifest.ObdSignalProperty.BitRightShift``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignal.html#cfn-iotfleetwise-decodermanifest-obdsignal-bitrightshift
            '''
            result = self._values.get("bit_right_shift")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ObdSignalProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnDecoderManifest.SignalDecodersItemsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "fully_qualified_name": "fullyQualifiedName",
            "interface_id": "interfaceId",
            "type": "type",
            "can_signal": "canSignal",
            "obd_signal": "obdSignal",
        },
    )
    class SignalDecodersItemsProperty:
        def __init__(
            self,
            *,
            fully_qualified_name: builtins.str,
            interface_id: builtins.str,
            type: builtins.str,
            can_signal: typing.Optional[typing.Union[typing.Union["CfnDecoderManifest.CanSignalProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
            obd_signal: typing.Optional[typing.Union[typing.Union["CfnDecoderManifest.ObdSignalProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param fully_qualified_name: ``CfnDecoderManifest.SignalDecodersItemsProperty.FullyQualifiedName``.
            :param interface_id: ``CfnDecoderManifest.SignalDecodersItemsProperty.InterfaceId``.
            :param type: ``CfnDecoderManifest.SignalDecodersItemsProperty.Type``.
            :param can_signal: ``CfnDecoderManifest.SignalDecodersItemsProperty.CanSignal``.
            :param obd_signal: ``CfnDecoderManifest.SignalDecodersItemsProperty.ObdSignal``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-signaldecodersitems.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotfleetwise as iotfleetwise
                
                signal_decoders_items_property = iotfleetwise.CfnDecoderManifest.SignalDecodersItemsProperty(
                    fully_qualified_name="fullyQualifiedName",
                    interface_id="interfaceId",
                    type="type",
                
                    # the properties below are optional
                    can_signal=iotfleetwise.CfnDecoderManifest.CanSignalProperty(
                        factor="factor",
                        is_big_endian="isBigEndian",
                        is_signed="isSigned",
                        length="length",
                        message_id="messageId",
                        offset="offset",
                        start_bit="startBit",
                
                        # the properties below are optional
                        name="name"
                    ),
                    obd_signal=iotfleetwise.CfnDecoderManifest.ObdSignalProperty(
                        byte_length="byteLength",
                        offset="offset",
                        pid="pid",
                        pid_response_length="pidResponseLength",
                        scaling="scaling",
                        service_mode="serviceMode",
                        start_byte="startByte",
                
                        # the properties below are optional
                        bit_mask_length="bitMaskLength",
                        bit_right_shift="bitRightShift"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5832121c7c16050419993147c157e7f5739fca1dc1afba25d1f52da2d4bd75fb)
                check_type(argname="argument fully_qualified_name", value=fully_qualified_name, expected_type=type_hints["fully_qualified_name"])
                check_type(argname="argument interface_id", value=interface_id, expected_type=type_hints["interface_id"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument can_signal", value=can_signal, expected_type=type_hints["can_signal"])
                check_type(argname="argument obd_signal", value=obd_signal, expected_type=type_hints["obd_signal"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "fully_qualified_name": fully_qualified_name,
                "interface_id": interface_id,
                "type": type,
            }
            if can_signal is not None:
                self._values["can_signal"] = can_signal
            if obd_signal is not None:
                self._values["obd_signal"] = obd_signal

        @builtins.property
        def fully_qualified_name(self) -> builtins.str:
            '''``CfnDecoderManifest.SignalDecodersItemsProperty.FullyQualifiedName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-signaldecodersitems.html#cfn-iotfleetwise-decodermanifest-signaldecodersitems-fullyqualifiedname
            '''
            result = self._values.get("fully_qualified_name")
            assert result is not None, "Required property 'fully_qualified_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def interface_id(self) -> builtins.str:
            '''``CfnDecoderManifest.SignalDecodersItemsProperty.InterfaceId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-signaldecodersitems.html#cfn-iotfleetwise-decodermanifest-signaldecodersitems-interfaceid
            '''
            result = self._values.get("interface_id")
            assert result is not None, "Required property 'interface_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''``CfnDecoderManifest.SignalDecodersItemsProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-signaldecodersitems.html#cfn-iotfleetwise-decodermanifest-signaldecodersitems-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def can_signal(
            self,
        ) -> typing.Optional[typing.Union["CfnDecoderManifest.CanSignalProperty", _IResolvable_da3f097b]]:
            '''``CfnDecoderManifest.SignalDecodersItemsProperty.CanSignal``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-signaldecodersitems.html#cfn-iotfleetwise-decodermanifest-signaldecodersitems-cansignal
            '''
            result = self._values.get("can_signal")
            return typing.cast(typing.Optional[typing.Union["CfnDecoderManifest.CanSignalProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def obd_signal(
            self,
        ) -> typing.Optional[typing.Union["CfnDecoderManifest.ObdSignalProperty", _IResolvable_da3f097b]]:
            '''``CfnDecoderManifest.SignalDecodersItemsProperty.ObdSignal``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-signaldecodersitems.html#cfn-iotfleetwise-decodermanifest-signaldecodersitems-obdsignal
            '''
            result = self._values.get("obd_signal")
            return typing.cast(typing.Optional[typing.Union["CfnDecoderManifest.ObdSignalProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SignalDecodersItemsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnDecoderManifestProps",
    jsii_struct_bases=[],
    name_mapping={
        "model_manifest_arn": "modelManifestArn",
        "name": "name",
        "description": "description",
        "network_interfaces": "networkInterfaces",
        "signal_decoders": "signalDecoders",
        "status": "status",
        "tags": "tags",
    },
)
class CfnDecoderManifestProps:
    def __init__(
        self,
        *,
        model_manifest_arn: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        network_interfaces: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnDecoderManifest.NetworkInterfacesItemsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        signal_decoders: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnDecoderManifest.SignalDecodersItemsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDecoderManifest``.

        :param model_manifest_arn: ``AWS::IoTFleetWise::DecoderManifest.ModelManifestArn``.
        :param name: ``AWS::IoTFleetWise::DecoderManifest.Name``.
        :param description: ``AWS::IoTFleetWise::DecoderManifest.Description``.
        :param network_interfaces: ``AWS::IoTFleetWise::DecoderManifest.NetworkInterfaces``.
        :param signal_decoders: ``AWS::IoTFleetWise::DecoderManifest.SignalDecoders``.
        :param status: ``AWS::IoTFleetWise::DecoderManifest.Status``.
        :param tags: ``AWS::IoTFleetWise::DecoderManifest.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iotfleetwise as iotfleetwise
            
            cfn_decoder_manifest_props = iotfleetwise.CfnDecoderManifestProps(
                model_manifest_arn="modelManifestArn",
                name="name",
            
                # the properties below are optional
                description="description",
                network_interfaces=[iotfleetwise.CfnDecoderManifest.NetworkInterfacesItemsProperty(
                    interface_id="interfaceId",
                    type="type",
            
                    # the properties below are optional
                    can_interface=iotfleetwise.CfnDecoderManifest.CanInterfaceProperty(
                        name="name",
            
                        # the properties below are optional
                        protocol_name="protocolName",
                        protocol_version="protocolVersion"
                    ),
                    obd_interface=iotfleetwise.CfnDecoderManifest.ObdInterfaceProperty(
                        name="name",
                        request_message_id="requestMessageId",
            
                        # the properties below are optional
                        dtc_request_interval_seconds="dtcRequestIntervalSeconds",
                        has_transmission_ecu="hasTransmissionEcu",
                        obd_standard="obdStandard",
                        pid_request_interval_seconds="pidRequestIntervalSeconds",
                        use_extended_ids="useExtendedIds"
                    )
                )],
                signal_decoders=[iotfleetwise.CfnDecoderManifest.SignalDecodersItemsProperty(
                    fully_qualified_name="fullyQualifiedName",
                    interface_id="interfaceId",
                    type="type",
            
                    # the properties below are optional
                    can_signal=iotfleetwise.CfnDecoderManifest.CanSignalProperty(
                        factor="factor",
                        is_big_endian="isBigEndian",
                        is_signed="isSigned",
                        length="length",
                        message_id="messageId",
                        offset="offset",
                        start_bit="startBit",
            
                        # the properties below are optional
                        name="name"
                    ),
                    obd_signal=iotfleetwise.CfnDecoderManifest.ObdSignalProperty(
                        byte_length="byteLength",
                        offset="offset",
                        pid="pid",
                        pid_response_length="pidResponseLength",
                        scaling="scaling",
                        service_mode="serviceMode",
                        start_byte="startByte",
            
                        # the properties below are optional
                        bit_mask_length="bitMaskLength",
                        bit_right_shift="bitRightShift"
                    )
                )],
                status="status",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1be5cfb3ca0441a2fdb0856303c08c4449592f7472588f5c0659c42af4d89e2c)
            check_type(argname="argument model_manifest_arn", value=model_manifest_arn, expected_type=type_hints["model_manifest_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument network_interfaces", value=network_interfaces, expected_type=type_hints["network_interfaces"])
            check_type(argname="argument signal_decoders", value=signal_decoders, expected_type=type_hints["signal_decoders"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "model_manifest_arn": model_manifest_arn,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if network_interfaces is not None:
            self._values["network_interfaces"] = network_interfaces
        if signal_decoders is not None:
            self._values["signal_decoders"] = signal_decoders
        if status is not None:
            self._values["status"] = status
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def model_manifest_arn(self) -> builtins.str:
        '''``AWS::IoTFleetWise::DecoderManifest.ModelManifestArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html#cfn-iotfleetwise-decodermanifest-modelmanifestarn
        '''
        result = self._values.get("model_manifest_arn")
        assert result is not None, "Required property 'model_manifest_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::IoTFleetWise::DecoderManifest.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html#cfn-iotfleetwise-decodermanifest-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::DecoderManifest.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html#cfn-iotfleetwise-decodermanifest-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_interfaces(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnDecoderManifest.NetworkInterfacesItemsProperty, _IResolvable_da3f097b]]]]:
        '''``AWS::IoTFleetWise::DecoderManifest.NetworkInterfaces``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html#cfn-iotfleetwise-decodermanifest-networkinterfaces
        '''
        result = self._values.get("network_interfaces")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnDecoderManifest.NetworkInterfacesItemsProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def signal_decoders(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnDecoderManifest.SignalDecodersItemsProperty, _IResolvable_da3f097b]]]]:
        '''``AWS::IoTFleetWise::DecoderManifest.SignalDecoders``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html#cfn-iotfleetwise-decodermanifest-signaldecoders
        '''
        result = self._values.get("signal_decoders")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnDecoderManifest.SignalDecodersItemsProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::DecoderManifest.Status``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html#cfn-iotfleetwise-decodermanifest-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''``AWS::IoTFleetWise::DecoderManifest.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html#cfn-iotfleetwise-decodermanifest-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDecoderManifestProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnFleet(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnFleet",
):
    '''A CloudFormation ``AWS::IoTFleetWise::Fleet``.

    :cloudformationResource: AWS::IoTFleetWise::Fleet
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-fleet.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iotfleetwise as iotfleetwise
        
        cfn_fleet = iotfleetwise.CfnFleet(self, "MyCfnFleet",
            id="id",
            signal_catalog_arn="signalCatalogArn",
        
            # the properties below are optional
            description="description",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        id: builtins.str,
        signal_catalog_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::IoTFleetWise::Fleet``.

        :param scope: - scope in which this resource is defined.
        :param id_: - scoped id of the resource.
        :param id: ``AWS::IoTFleetWise::Fleet.Id``.
        :param signal_catalog_arn: ``AWS::IoTFleetWise::Fleet.SignalCatalogArn``.
        :param description: ``AWS::IoTFleetWise::Fleet.Description``.
        :param tags: ``AWS::IoTFleetWise::Fleet.Tags``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be2399a288ba3f0fe4eba6c31d42082d31eac165febede18736a759d92f2120d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        props = CfnFleetProps(
            id=id,
            signal_catalog_arn=signal_catalog_arn,
            description=description,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id_, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b66a25ffe3875464ec35ff63e6d6335f63f5bd966c356414cfa0ec840225eedd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__19ef6ad0585e294dae29b4c919f9fbf11b89c72deadd5a5cda8a56f1433235a8)
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
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModificationTime")
    def attr_last_modification_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: LastModificationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastModificationTime"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''``AWS::IoTFleetWise::Fleet.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-fleet.html#cfn-iotfleetwise-fleet-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        '''``AWS::IoTFleetWise::Fleet.Id``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-fleet.html#cfn-iotfleetwise-fleet-id
        '''
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__521c3cdc3b4991a92beb684d8c8af88ceab73dcbd34d08d120663c9c7f94d059)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="signalCatalogArn")
    def signal_catalog_arn(self) -> builtins.str:
        '''``AWS::IoTFleetWise::Fleet.SignalCatalogArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-fleet.html#cfn-iotfleetwise-fleet-signalcatalogarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "signalCatalogArn"))

    @signal_catalog_arn.setter
    def signal_catalog_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eec1aed040f26806fdbfee937ccf8c8b0ccb036bc460096cfbb5b04da65cccca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signalCatalogArn", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::Fleet.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-fleet.html#cfn-iotfleetwise-fleet-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47625bcd41335399a9f769fa64574c2375f2937ed4511d09a3984dbd0abef447)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnFleetProps",
    jsii_struct_bases=[],
    name_mapping={
        "id": "id",
        "signal_catalog_arn": "signalCatalogArn",
        "description": "description",
        "tags": "tags",
    },
)
class CfnFleetProps:
    def __init__(
        self,
        *,
        id: builtins.str,
        signal_catalog_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnFleet``.

        :param id: ``AWS::IoTFleetWise::Fleet.Id``.
        :param signal_catalog_arn: ``AWS::IoTFleetWise::Fleet.SignalCatalogArn``.
        :param description: ``AWS::IoTFleetWise::Fleet.Description``.
        :param tags: ``AWS::IoTFleetWise::Fleet.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-fleet.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iotfleetwise as iotfleetwise
            
            cfn_fleet_props = iotfleetwise.CfnFleetProps(
                id="id",
                signal_catalog_arn="signalCatalogArn",
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06c4343c5d692e914e7c2c900c5e4f0c5bed9b41e2c90ff1efc672ba0974c3d8)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument signal_catalog_arn", value=signal_catalog_arn, expected_type=type_hints["signal_catalog_arn"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "id": id,
            "signal_catalog_arn": signal_catalog_arn,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def id(self) -> builtins.str:
        '''``AWS::IoTFleetWise::Fleet.Id``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-fleet.html#cfn-iotfleetwise-fleet-id
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def signal_catalog_arn(self) -> builtins.str:
        '''``AWS::IoTFleetWise::Fleet.SignalCatalogArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-fleet.html#cfn-iotfleetwise-fleet-signalcatalogarn
        '''
        result = self._values.get("signal_catalog_arn")
        assert result is not None, "Required property 'signal_catalog_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::Fleet.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-fleet.html#cfn-iotfleetwise-fleet-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''``AWS::IoTFleetWise::Fleet.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-fleet.html#cfn-iotfleetwise-fleet-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFleetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnModelManifest(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnModelManifest",
):
    '''A CloudFormation ``AWS::IoTFleetWise::ModelManifest``.

    :cloudformationResource: AWS::IoTFleetWise::ModelManifest
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iotfleetwise as iotfleetwise
        
        cfn_model_manifest = iotfleetwise.CfnModelManifest(self, "MyCfnModelManifest",
            name="name",
            signal_catalog_arn="signalCatalogArn",
        
            # the properties below are optional
            description="description",
            nodes=["nodes"],
            status="status",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        signal_catalog_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        nodes: typing.Optional[typing.Sequence[builtins.str]] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::IoTFleetWise::ModelManifest``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::IoTFleetWise::ModelManifest.Name``.
        :param signal_catalog_arn: ``AWS::IoTFleetWise::ModelManifest.SignalCatalogArn``.
        :param description: ``AWS::IoTFleetWise::ModelManifest.Description``.
        :param nodes: ``AWS::IoTFleetWise::ModelManifest.Nodes``.
        :param status: ``AWS::IoTFleetWise::ModelManifest.Status``.
        :param tags: ``AWS::IoTFleetWise::ModelManifest.Tags``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f0e03fe14f53de97f2e7071c7f10132492e794782f840695921dc42cd286a81)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnModelManifestProps(
            name=name,
            signal_catalog_arn=signal_catalog_arn,
            description=description,
            nodes=nodes,
            status=status,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26ab7dc28e60a5682365801d22047c22eca01f42fd1ecbb3b9b379fa832ee14c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c6a3d382e4e768e4426411dff74ffd0bcaba33058efbe3e880fae9c7ace6d5d3)
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
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModificationTime")
    def attr_last_modification_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: LastModificationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastModificationTime"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''``AWS::IoTFleetWise::ModelManifest.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html#cfn-iotfleetwise-modelmanifest-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::IoTFleetWise::ModelManifest.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html#cfn-iotfleetwise-modelmanifest-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf56f12f94bd9c70533145a1dbb473b412b33dff8bc3791a2bcad34f29302b8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="signalCatalogArn")
    def signal_catalog_arn(self) -> builtins.str:
        '''``AWS::IoTFleetWise::ModelManifest.SignalCatalogArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html#cfn-iotfleetwise-modelmanifest-signalcatalogarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "signalCatalogArn"))

    @signal_catalog_arn.setter
    def signal_catalog_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9c26dfed7e5cc0b2e5105665abac1ffd59d367b056759c9e21642fa1214969e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signalCatalogArn", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::ModelManifest.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html#cfn-iotfleetwise-modelmanifest-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d266113c8b366f668b05115f1bddeefd3b243d1c8fd8eecc3c143d130167d11)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="nodes")
    def nodes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::IoTFleetWise::ModelManifest.Nodes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html#cfn-iotfleetwise-modelmanifest-nodes
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "nodes"))

    @nodes.setter
    def nodes(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f0af1e0b1687e8bdbdeec73691f1b3cac6582b744e41041b611118e281c9134)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodes", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::ModelManifest.Status``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html#cfn-iotfleetwise-modelmanifest-status
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f57f8c832da7ae938e0025bdef8ca3f24978b35cafd09be0c6bc21a8ee3329a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnModelManifestProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "signal_catalog_arn": "signalCatalogArn",
        "description": "description",
        "nodes": "nodes",
        "status": "status",
        "tags": "tags",
    },
)
class CfnModelManifestProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        signal_catalog_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        nodes: typing.Optional[typing.Sequence[builtins.str]] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnModelManifest``.

        :param name: ``AWS::IoTFleetWise::ModelManifest.Name``.
        :param signal_catalog_arn: ``AWS::IoTFleetWise::ModelManifest.SignalCatalogArn``.
        :param description: ``AWS::IoTFleetWise::ModelManifest.Description``.
        :param nodes: ``AWS::IoTFleetWise::ModelManifest.Nodes``.
        :param status: ``AWS::IoTFleetWise::ModelManifest.Status``.
        :param tags: ``AWS::IoTFleetWise::ModelManifest.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iotfleetwise as iotfleetwise
            
            cfn_model_manifest_props = iotfleetwise.CfnModelManifestProps(
                name="name",
                signal_catalog_arn="signalCatalogArn",
            
                # the properties below are optional
                description="description",
                nodes=["nodes"],
                status="status",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1235282929965217b607172340e97ee502a13c24469f00158a042c2a92786260)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument signal_catalog_arn", value=signal_catalog_arn, expected_type=type_hints["signal_catalog_arn"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument nodes", value=nodes, expected_type=type_hints["nodes"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "signal_catalog_arn": signal_catalog_arn,
        }
        if description is not None:
            self._values["description"] = description
        if nodes is not None:
            self._values["nodes"] = nodes
        if status is not None:
            self._values["status"] = status
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::IoTFleetWise::ModelManifest.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html#cfn-iotfleetwise-modelmanifest-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def signal_catalog_arn(self) -> builtins.str:
        '''``AWS::IoTFleetWise::ModelManifest.SignalCatalogArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html#cfn-iotfleetwise-modelmanifest-signalcatalogarn
        '''
        result = self._values.get("signal_catalog_arn")
        assert result is not None, "Required property 'signal_catalog_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::ModelManifest.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html#cfn-iotfleetwise-modelmanifest-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nodes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::IoTFleetWise::ModelManifest.Nodes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html#cfn-iotfleetwise-modelmanifest-nodes
        '''
        result = self._values.get("nodes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::ModelManifest.Status``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html#cfn-iotfleetwise-modelmanifest-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''``AWS::IoTFleetWise::ModelManifest.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html#cfn-iotfleetwise-modelmanifest-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModelManifestProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnSignalCatalog(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnSignalCatalog",
):
    '''A CloudFormation ``AWS::IoTFleetWise::SignalCatalog``.

    :cloudformationResource: AWS::IoTFleetWise::SignalCatalog
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-signalcatalog.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iotfleetwise as iotfleetwise
        
        cfn_signal_catalog = iotfleetwise.CfnSignalCatalog(self, "MyCfnSignalCatalog",
            description="description",
            name="name",
            node_counts=iotfleetwise.CfnSignalCatalog.NodeCountsProperty(
                total_actuators=123,
                total_attributes=123,
                total_branches=123,
                total_nodes=123,
                total_sensors=123
            ),
            nodes=[iotfleetwise.CfnSignalCatalog.NodeProperty(
                actuator=iotfleetwise.CfnSignalCatalog.ActuatorProperty(
                    data_type="dataType",
                    fully_qualified_name="fullyQualifiedName",
        
                    # the properties below are optional
                    allowed_values=["allowedValues"],
                    assigned_value="assignedValue",
                    description="description",
                    max=123,
                    min=123,
                    unit="unit"
                ),
                attribute=iotfleetwise.CfnSignalCatalog.AttributeProperty(
                    data_type="dataType",
                    fully_qualified_name="fullyQualifiedName",
        
                    # the properties below are optional
                    allowed_values=["allowedValues"],
                    assigned_value="assignedValue",
                    default_value="defaultValue",
                    description="description",
                    max=123,
                    min=123,
                    unit="unit"
                ),
                branch=iotfleetwise.CfnSignalCatalog.BranchProperty(
                    fully_qualified_name="fullyQualifiedName",
        
                    # the properties below are optional
                    description="description"
                ),
                sensor=iotfleetwise.CfnSignalCatalog.SensorProperty(
                    data_type="dataType",
                    fully_qualified_name="fullyQualifiedName",
        
                    # the properties below are optional
                    allowed_values=["allowedValues"],
                    description="description",
                    max=123,
                    min=123,
                    unit="unit"
                )
            )],
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        node_counts: typing.Optional[typing.Union[typing.Union["CfnSignalCatalog.NodeCountsProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        nodes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union["CfnSignalCatalog.NodeProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::IoTFleetWise::SignalCatalog``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param description: ``AWS::IoTFleetWise::SignalCatalog.Description``.
        :param name: ``AWS::IoTFleetWise::SignalCatalog.Name``.
        :param node_counts: ``AWS::IoTFleetWise::SignalCatalog.NodeCounts``.
        :param nodes: ``AWS::IoTFleetWise::SignalCatalog.Nodes``.
        :param tags: ``AWS::IoTFleetWise::SignalCatalog.Tags``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00a926b4b26fd9efc933b63c5d4e497e8bfeceb8f4fb16790d18152e0fd2e282)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSignalCatalogProps(
            description=description,
            name=name,
            node_counts=node_counts,
            nodes=nodes,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d1771c8f83cb9b124255f0cb877c396f7dc19033885dac73e197f274702fe58)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3c1bc0963e13c138e8b1a9d56f8dfaba2b1c3f856cd9d0bc996158b2c5b704bb)
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
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModificationTime")
    def attr_last_modification_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: LastModificationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastModificationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrNodeCountsTotalActuators")
    def attr_node_counts_total_actuators(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: NodeCounts.TotalActuators
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrNodeCountsTotalActuators"))

    @builtins.property
    @jsii.member(jsii_name="attrNodeCountsTotalAttributes")
    def attr_node_counts_total_attributes(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: NodeCounts.TotalAttributes
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrNodeCountsTotalAttributes"))

    @builtins.property
    @jsii.member(jsii_name="attrNodeCountsTotalBranches")
    def attr_node_counts_total_branches(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: NodeCounts.TotalBranches
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrNodeCountsTotalBranches"))

    @builtins.property
    @jsii.member(jsii_name="attrNodeCountsTotalNodes")
    def attr_node_counts_total_nodes(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: NodeCounts.TotalNodes
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrNodeCountsTotalNodes"))

    @builtins.property
    @jsii.member(jsii_name="attrNodeCountsTotalSensors")
    def attr_node_counts_total_sensors(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: NodeCounts.TotalSensors
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrNodeCountsTotalSensors"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''``AWS::IoTFleetWise::SignalCatalog.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-signalcatalog.html#cfn-iotfleetwise-signalcatalog-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::SignalCatalog.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-signalcatalog.html#cfn-iotfleetwise-signalcatalog-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f426284778d609b7de7cea520eccf5230e025cc40e766b3f3f0a9b3c536bfe4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::SignalCatalog.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-signalcatalog.html#cfn-iotfleetwise-signalcatalog-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1be488894dded62944d72e0b078393e92b8c846e12e5682732e5b292abdf03c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="nodeCounts")
    def node_counts(
        self,
    ) -> typing.Optional[typing.Union["CfnSignalCatalog.NodeCountsProperty", _IResolvable_da3f097b]]:
        '''``AWS::IoTFleetWise::SignalCatalog.NodeCounts``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-signalcatalog.html#cfn-iotfleetwise-signalcatalog-nodecounts
        '''
        return typing.cast(typing.Optional[typing.Union["CfnSignalCatalog.NodeCountsProperty", _IResolvable_da3f097b]], jsii.get(self, "nodeCounts"))

    @node_counts.setter
    def node_counts(
        self,
        value: typing.Optional[typing.Union["CfnSignalCatalog.NodeCountsProperty", _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f8c5daca018b1e857e68a1c38c2d8c8ad48c3e10d76e27f1b88db531cc7800d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeCounts", value)

    @builtins.property
    @jsii.member(jsii_name="nodes")
    def nodes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnSignalCatalog.NodeProperty", _IResolvable_da3f097b]]]]:
        '''``AWS::IoTFleetWise::SignalCatalog.Nodes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-signalcatalog.html#cfn-iotfleetwise-signalcatalog-nodes
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnSignalCatalog.NodeProperty", _IResolvable_da3f097b]]]], jsii.get(self, "nodes"))

    @nodes.setter
    def nodes(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union["CfnSignalCatalog.NodeProperty", _IResolvable_da3f097b]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__017bfa378203e76812e9cd13928c4c7498a8ed198568cb4d309d165dee01a3b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodes", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnSignalCatalog.ActuatorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_type": "dataType",
            "fully_qualified_name": "fullyQualifiedName",
            "allowed_values": "allowedValues",
            "assigned_value": "assignedValue",
            "description": "description",
            "max": "max",
            "min": "min",
            "unit": "unit",
        },
    )
    class ActuatorProperty:
        def __init__(
            self,
            *,
            data_type: builtins.str,
            fully_qualified_name: builtins.str,
            allowed_values: typing.Optional[typing.Sequence[builtins.str]] = None,
            assigned_value: typing.Optional[builtins.str] = None,
            description: typing.Optional[builtins.str] = None,
            max: typing.Optional[jsii.Number] = None,
            min: typing.Optional[jsii.Number] = None,
            unit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param data_type: ``CfnSignalCatalog.ActuatorProperty.DataType``.
            :param fully_qualified_name: ``CfnSignalCatalog.ActuatorProperty.FullyQualifiedName``.
            :param allowed_values: ``CfnSignalCatalog.ActuatorProperty.AllowedValues``.
            :param assigned_value: ``CfnSignalCatalog.ActuatorProperty.AssignedValue``.
            :param description: ``CfnSignalCatalog.ActuatorProperty.Description``.
            :param max: ``CfnSignalCatalog.ActuatorProperty.Max``.
            :param min: ``CfnSignalCatalog.ActuatorProperty.Min``.
            :param unit: ``CfnSignalCatalog.ActuatorProperty.Unit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-actuator.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotfleetwise as iotfleetwise
                
                actuator_property = iotfleetwise.CfnSignalCatalog.ActuatorProperty(
                    data_type="dataType",
                    fully_qualified_name="fullyQualifiedName",
                
                    # the properties below are optional
                    allowed_values=["allowedValues"],
                    assigned_value="assignedValue",
                    description="description",
                    max=123,
                    min=123,
                    unit="unit"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3692c9418e6188deb5e6f1b10c8f51484f74857c2b24c543b0730826f0e8014c)
                check_type(argname="argument data_type", value=data_type, expected_type=type_hints["data_type"])
                check_type(argname="argument fully_qualified_name", value=fully_qualified_name, expected_type=type_hints["fully_qualified_name"])
                check_type(argname="argument allowed_values", value=allowed_values, expected_type=type_hints["allowed_values"])
                check_type(argname="argument assigned_value", value=assigned_value, expected_type=type_hints["assigned_value"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument max", value=max, expected_type=type_hints["max"])
                check_type(argname="argument min", value=min, expected_type=type_hints["min"])
                check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "data_type": data_type,
                "fully_qualified_name": fully_qualified_name,
            }
            if allowed_values is not None:
                self._values["allowed_values"] = allowed_values
            if assigned_value is not None:
                self._values["assigned_value"] = assigned_value
            if description is not None:
                self._values["description"] = description
            if max is not None:
                self._values["max"] = max
            if min is not None:
                self._values["min"] = min
            if unit is not None:
                self._values["unit"] = unit

        @builtins.property
        def data_type(self) -> builtins.str:
            '''``CfnSignalCatalog.ActuatorProperty.DataType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-actuator.html#cfn-iotfleetwise-signalcatalog-actuator-datatype
            '''
            result = self._values.get("data_type")
            assert result is not None, "Required property 'data_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def fully_qualified_name(self) -> builtins.str:
            '''``CfnSignalCatalog.ActuatorProperty.FullyQualifiedName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-actuator.html#cfn-iotfleetwise-signalcatalog-actuator-fullyqualifiedname
            '''
            result = self._values.get("fully_qualified_name")
            assert result is not None, "Required property 'fully_qualified_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def allowed_values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnSignalCatalog.ActuatorProperty.AllowedValues``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-actuator.html#cfn-iotfleetwise-signalcatalog-actuator-allowedvalues
            '''
            result = self._values.get("allowed_values")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def assigned_value(self) -> typing.Optional[builtins.str]:
            '''``CfnSignalCatalog.ActuatorProperty.AssignedValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-actuator.html#cfn-iotfleetwise-signalcatalog-actuator-assignedvalue
            '''
            result = self._values.get("assigned_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''``CfnSignalCatalog.ActuatorProperty.Description``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-actuator.html#cfn-iotfleetwise-signalcatalog-actuator-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def max(self) -> typing.Optional[jsii.Number]:
            '''``CfnSignalCatalog.ActuatorProperty.Max``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-actuator.html#cfn-iotfleetwise-signalcatalog-actuator-max
            '''
            result = self._values.get("max")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def min(self) -> typing.Optional[jsii.Number]:
            '''``CfnSignalCatalog.ActuatorProperty.Min``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-actuator.html#cfn-iotfleetwise-signalcatalog-actuator-min
            '''
            result = self._values.get("min")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def unit(self) -> typing.Optional[builtins.str]:
            '''``CfnSignalCatalog.ActuatorProperty.Unit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-actuator.html#cfn-iotfleetwise-signalcatalog-actuator-unit
            '''
            result = self._values.get("unit")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActuatorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnSignalCatalog.AttributeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_type": "dataType",
            "fully_qualified_name": "fullyQualifiedName",
            "allowed_values": "allowedValues",
            "assigned_value": "assignedValue",
            "default_value": "defaultValue",
            "description": "description",
            "max": "max",
            "min": "min",
            "unit": "unit",
        },
    )
    class AttributeProperty:
        def __init__(
            self,
            *,
            data_type: builtins.str,
            fully_qualified_name: builtins.str,
            allowed_values: typing.Optional[typing.Sequence[builtins.str]] = None,
            assigned_value: typing.Optional[builtins.str] = None,
            default_value: typing.Optional[builtins.str] = None,
            description: typing.Optional[builtins.str] = None,
            max: typing.Optional[jsii.Number] = None,
            min: typing.Optional[jsii.Number] = None,
            unit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param data_type: ``CfnSignalCatalog.AttributeProperty.DataType``.
            :param fully_qualified_name: ``CfnSignalCatalog.AttributeProperty.FullyQualifiedName``.
            :param allowed_values: ``CfnSignalCatalog.AttributeProperty.AllowedValues``.
            :param assigned_value: ``CfnSignalCatalog.AttributeProperty.AssignedValue``.
            :param default_value: ``CfnSignalCatalog.AttributeProperty.DefaultValue``.
            :param description: ``CfnSignalCatalog.AttributeProperty.Description``.
            :param max: ``CfnSignalCatalog.AttributeProperty.Max``.
            :param min: ``CfnSignalCatalog.AttributeProperty.Min``.
            :param unit: ``CfnSignalCatalog.AttributeProperty.Unit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-attribute.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotfleetwise as iotfleetwise
                
                attribute_property = iotfleetwise.CfnSignalCatalog.AttributeProperty(
                    data_type="dataType",
                    fully_qualified_name="fullyQualifiedName",
                
                    # the properties below are optional
                    allowed_values=["allowedValues"],
                    assigned_value="assignedValue",
                    default_value="defaultValue",
                    description="description",
                    max=123,
                    min=123,
                    unit="unit"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__34812da89e0890988b83a21707bc72187e1251886f85c8d31c8bad4f51a5ad5d)
                check_type(argname="argument data_type", value=data_type, expected_type=type_hints["data_type"])
                check_type(argname="argument fully_qualified_name", value=fully_qualified_name, expected_type=type_hints["fully_qualified_name"])
                check_type(argname="argument allowed_values", value=allowed_values, expected_type=type_hints["allowed_values"])
                check_type(argname="argument assigned_value", value=assigned_value, expected_type=type_hints["assigned_value"])
                check_type(argname="argument default_value", value=default_value, expected_type=type_hints["default_value"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument max", value=max, expected_type=type_hints["max"])
                check_type(argname="argument min", value=min, expected_type=type_hints["min"])
                check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "data_type": data_type,
                "fully_qualified_name": fully_qualified_name,
            }
            if allowed_values is not None:
                self._values["allowed_values"] = allowed_values
            if assigned_value is not None:
                self._values["assigned_value"] = assigned_value
            if default_value is not None:
                self._values["default_value"] = default_value
            if description is not None:
                self._values["description"] = description
            if max is not None:
                self._values["max"] = max
            if min is not None:
                self._values["min"] = min
            if unit is not None:
                self._values["unit"] = unit

        @builtins.property
        def data_type(self) -> builtins.str:
            '''``CfnSignalCatalog.AttributeProperty.DataType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-attribute.html#cfn-iotfleetwise-signalcatalog-attribute-datatype
            '''
            result = self._values.get("data_type")
            assert result is not None, "Required property 'data_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def fully_qualified_name(self) -> builtins.str:
            '''``CfnSignalCatalog.AttributeProperty.FullyQualifiedName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-attribute.html#cfn-iotfleetwise-signalcatalog-attribute-fullyqualifiedname
            '''
            result = self._values.get("fully_qualified_name")
            assert result is not None, "Required property 'fully_qualified_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def allowed_values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnSignalCatalog.AttributeProperty.AllowedValues``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-attribute.html#cfn-iotfleetwise-signalcatalog-attribute-allowedvalues
            '''
            result = self._values.get("allowed_values")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def assigned_value(self) -> typing.Optional[builtins.str]:
            '''``CfnSignalCatalog.AttributeProperty.AssignedValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-attribute.html#cfn-iotfleetwise-signalcatalog-attribute-assignedvalue
            '''
            result = self._values.get("assigned_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def default_value(self) -> typing.Optional[builtins.str]:
            '''``CfnSignalCatalog.AttributeProperty.DefaultValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-attribute.html#cfn-iotfleetwise-signalcatalog-attribute-defaultvalue
            '''
            result = self._values.get("default_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''``CfnSignalCatalog.AttributeProperty.Description``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-attribute.html#cfn-iotfleetwise-signalcatalog-attribute-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def max(self) -> typing.Optional[jsii.Number]:
            '''``CfnSignalCatalog.AttributeProperty.Max``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-attribute.html#cfn-iotfleetwise-signalcatalog-attribute-max
            '''
            result = self._values.get("max")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def min(self) -> typing.Optional[jsii.Number]:
            '''``CfnSignalCatalog.AttributeProperty.Min``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-attribute.html#cfn-iotfleetwise-signalcatalog-attribute-min
            '''
            result = self._values.get("min")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def unit(self) -> typing.Optional[builtins.str]:
            '''``CfnSignalCatalog.AttributeProperty.Unit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-attribute.html#cfn-iotfleetwise-signalcatalog-attribute-unit
            '''
            result = self._values.get("unit")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AttributeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnSignalCatalog.BranchProperty",
        jsii_struct_bases=[],
        name_mapping={
            "fully_qualified_name": "fullyQualifiedName",
            "description": "description",
        },
    )
    class BranchProperty:
        def __init__(
            self,
            *,
            fully_qualified_name: builtins.str,
            description: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param fully_qualified_name: ``CfnSignalCatalog.BranchProperty.FullyQualifiedName``.
            :param description: ``CfnSignalCatalog.BranchProperty.Description``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-branch.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotfleetwise as iotfleetwise
                
                branch_property = iotfleetwise.CfnSignalCatalog.BranchProperty(
                    fully_qualified_name="fullyQualifiedName",
                
                    # the properties below are optional
                    description="description"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__10c551cff70ab7e9a7ade619807100cf531ce4f17b5ade4cfc711a7110032c76)
                check_type(argname="argument fully_qualified_name", value=fully_qualified_name, expected_type=type_hints["fully_qualified_name"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "fully_qualified_name": fully_qualified_name,
            }
            if description is not None:
                self._values["description"] = description

        @builtins.property
        def fully_qualified_name(self) -> builtins.str:
            '''``CfnSignalCatalog.BranchProperty.FullyQualifiedName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-branch.html#cfn-iotfleetwise-signalcatalog-branch-fullyqualifiedname
            '''
            result = self._values.get("fully_qualified_name")
            assert result is not None, "Required property 'fully_qualified_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''``CfnSignalCatalog.BranchProperty.Description``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-branch.html#cfn-iotfleetwise-signalcatalog-branch-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BranchProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnSignalCatalog.NodeCountsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "total_actuators": "totalActuators",
            "total_attributes": "totalAttributes",
            "total_branches": "totalBranches",
            "total_nodes": "totalNodes",
            "total_sensors": "totalSensors",
        },
    )
    class NodeCountsProperty:
        def __init__(
            self,
            *,
            total_actuators: typing.Optional[jsii.Number] = None,
            total_attributes: typing.Optional[jsii.Number] = None,
            total_branches: typing.Optional[jsii.Number] = None,
            total_nodes: typing.Optional[jsii.Number] = None,
            total_sensors: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param total_actuators: ``CfnSignalCatalog.NodeCountsProperty.TotalActuators``.
            :param total_attributes: ``CfnSignalCatalog.NodeCountsProperty.TotalAttributes``.
            :param total_branches: ``CfnSignalCatalog.NodeCountsProperty.TotalBranches``.
            :param total_nodes: ``CfnSignalCatalog.NodeCountsProperty.TotalNodes``.
            :param total_sensors: ``CfnSignalCatalog.NodeCountsProperty.TotalSensors``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-nodecounts.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotfleetwise as iotfleetwise
                
                node_counts_property = iotfleetwise.CfnSignalCatalog.NodeCountsProperty(
                    total_actuators=123,
                    total_attributes=123,
                    total_branches=123,
                    total_nodes=123,
                    total_sensors=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e0ecad1dc29fa151da6ab7009debe26c40391783260739fb2c93faa85a3ff88d)
                check_type(argname="argument total_actuators", value=total_actuators, expected_type=type_hints["total_actuators"])
                check_type(argname="argument total_attributes", value=total_attributes, expected_type=type_hints["total_attributes"])
                check_type(argname="argument total_branches", value=total_branches, expected_type=type_hints["total_branches"])
                check_type(argname="argument total_nodes", value=total_nodes, expected_type=type_hints["total_nodes"])
                check_type(argname="argument total_sensors", value=total_sensors, expected_type=type_hints["total_sensors"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if total_actuators is not None:
                self._values["total_actuators"] = total_actuators
            if total_attributes is not None:
                self._values["total_attributes"] = total_attributes
            if total_branches is not None:
                self._values["total_branches"] = total_branches
            if total_nodes is not None:
                self._values["total_nodes"] = total_nodes
            if total_sensors is not None:
                self._values["total_sensors"] = total_sensors

        @builtins.property
        def total_actuators(self) -> typing.Optional[jsii.Number]:
            '''``CfnSignalCatalog.NodeCountsProperty.TotalActuators``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-nodecounts.html#cfn-iotfleetwise-signalcatalog-nodecounts-totalactuators
            '''
            result = self._values.get("total_actuators")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def total_attributes(self) -> typing.Optional[jsii.Number]:
            '''``CfnSignalCatalog.NodeCountsProperty.TotalAttributes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-nodecounts.html#cfn-iotfleetwise-signalcatalog-nodecounts-totalattributes
            '''
            result = self._values.get("total_attributes")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def total_branches(self) -> typing.Optional[jsii.Number]:
            '''``CfnSignalCatalog.NodeCountsProperty.TotalBranches``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-nodecounts.html#cfn-iotfleetwise-signalcatalog-nodecounts-totalbranches
            '''
            result = self._values.get("total_branches")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def total_nodes(self) -> typing.Optional[jsii.Number]:
            '''``CfnSignalCatalog.NodeCountsProperty.TotalNodes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-nodecounts.html#cfn-iotfleetwise-signalcatalog-nodecounts-totalnodes
            '''
            result = self._values.get("total_nodes")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def total_sensors(self) -> typing.Optional[jsii.Number]:
            '''``CfnSignalCatalog.NodeCountsProperty.TotalSensors``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-nodecounts.html#cfn-iotfleetwise-signalcatalog-nodecounts-totalsensors
            '''
            result = self._values.get("total_sensors")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NodeCountsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnSignalCatalog.NodeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "actuator": "actuator",
            "attribute": "attribute",
            "branch": "branch",
            "sensor": "sensor",
        },
    )
    class NodeProperty:
        def __init__(
            self,
            *,
            actuator: typing.Optional[typing.Union[typing.Union["CfnSignalCatalog.ActuatorProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
            attribute: typing.Optional[typing.Union[typing.Union["CfnSignalCatalog.AttributeProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
            branch: typing.Optional[typing.Union[typing.Union["CfnSignalCatalog.BranchProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
            sensor: typing.Optional[typing.Union[typing.Union["CfnSignalCatalog.SensorProperty", typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param actuator: ``CfnSignalCatalog.NodeProperty.Actuator``.
            :param attribute: ``CfnSignalCatalog.NodeProperty.Attribute``.
            :param branch: ``CfnSignalCatalog.NodeProperty.Branch``.
            :param sensor: ``CfnSignalCatalog.NodeProperty.Sensor``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-node.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotfleetwise as iotfleetwise
                
                node_property = iotfleetwise.CfnSignalCatalog.NodeProperty(
                    actuator=iotfleetwise.CfnSignalCatalog.ActuatorProperty(
                        data_type="dataType",
                        fully_qualified_name="fullyQualifiedName",
                
                        # the properties below are optional
                        allowed_values=["allowedValues"],
                        assigned_value="assignedValue",
                        description="description",
                        max=123,
                        min=123,
                        unit="unit"
                    ),
                    attribute=iotfleetwise.CfnSignalCatalog.AttributeProperty(
                        data_type="dataType",
                        fully_qualified_name="fullyQualifiedName",
                
                        # the properties below are optional
                        allowed_values=["allowedValues"],
                        assigned_value="assignedValue",
                        default_value="defaultValue",
                        description="description",
                        max=123,
                        min=123,
                        unit="unit"
                    ),
                    branch=iotfleetwise.CfnSignalCatalog.BranchProperty(
                        fully_qualified_name="fullyQualifiedName",
                
                        # the properties below are optional
                        description="description"
                    ),
                    sensor=iotfleetwise.CfnSignalCatalog.SensorProperty(
                        data_type="dataType",
                        fully_qualified_name="fullyQualifiedName",
                
                        # the properties below are optional
                        allowed_values=["allowedValues"],
                        description="description",
                        max=123,
                        min=123,
                        unit="unit"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3f7b644285514f42793054887b78a595b6a6dc6b59e3a153fd29b94fb12c45e0)
                check_type(argname="argument actuator", value=actuator, expected_type=type_hints["actuator"])
                check_type(argname="argument attribute", value=attribute, expected_type=type_hints["attribute"])
                check_type(argname="argument branch", value=branch, expected_type=type_hints["branch"])
                check_type(argname="argument sensor", value=sensor, expected_type=type_hints["sensor"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if actuator is not None:
                self._values["actuator"] = actuator
            if attribute is not None:
                self._values["attribute"] = attribute
            if branch is not None:
                self._values["branch"] = branch
            if sensor is not None:
                self._values["sensor"] = sensor

        @builtins.property
        def actuator(
            self,
        ) -> typing.Optional[typing.Union["CfnSignalCatalog.ActuatorProperty", _IResolvable_da3f097b]]:
            '''``CfnSignalCatalog.NodeProperty.Actuator``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-node.html#cfn-iotfleetwise-signalcatalog-node-actuator
            '''
            result = self._values.get("actuator")
            return typing.cast(typing.Optional[typing.Union["CfnSignalCatalog.ActuatorProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def attribute(
            self,
        ) -> typing.Optional[typing.Union["CfnSignalCatalog.AttributeProperty", _IResolvable_da3f097b]]:
            '''``CfnSignalCatalog.NodeProperty.Attribute``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-node.html#cfn-iotfleetwise-signalcatalog-node-attribute
            '''
            result = self._values.get("attribute")
            return typing.cast(typing.Optional[typing.Union["CfnSignalCatalog.AttributeProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def branch(
            self,
        ) -> typing.Optional[typing.Union["CfnSignalCatalog.BranchProperty", _IResolvable_da3f097b]]:
            '''``CfnSignalCatalog.NodeProperty.Branch``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-node.html#cfn-iotfleetwise-signalcatalog-node-branch
            '''
            result = self._values.get("branch")
            return typing.cast(typing.Optional[typing.Union["CfnSignalCatalog.BranchProperty", _IResolvable_da3f097b]], result)

        @builtins.property
        def sensor(
            self,
        ) -> typing.Optional[typing.Union["CfnSignalCatalog.SensorProperty", _IResolvable_da3f097b]]:
            '''``CfnSignalCatalog.NodeProperty.Sensor``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-node.html#cfn-iotfleetwise-signalcatalog-node-sensor
            '''
            result = self._values.get("sensor")
            return typing.cast(typing.Optional[typing.Union["CfnSignalCatalog.SensorProperty", _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NodeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnSignalCatalog.SensorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_type": "dataType",
            "fully_qualified_name": "fullyQualifiedName",
            "allowed_values": "allowedValues",
            "description": "description",
            "max": "max",
            "min": "min",
            "unit": "unit",
        },
    )
    class SensorProperty:
        def __init__(
            self,
            *,
            data_type: builtins.str,
            fully_qualified_name: builtins.str,
            allowed_values: typing.Optional[typing.Sequence[builtins.str]] = None,
            description: typing.Optional[builtins.str] = None,
            max: typing.Optional[jsii.Number] = None,
            min: typing.Optional[jsii.Number] = None,
            unit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param data_type: ``CfnSignalCatalog.SensorProperty.DataType``.
            :param fully_qualified_name: ``CfnSignalCatalog.SensorProperty.FullyQualifiedName``.
            :param allowed_values: ``CfnSignalCatalog.SensorProperty.AllowedValues``.
            :param description: ``CfnSignalCatalog.SensorProperty.Description``.
            :param max: ``CfnSignalCatalog.SensorProperty.Max``.
            :param min: ``CfnSignalCatalog.SensorProperty.Min``.
            :param unit: ``CfnSignalCatalog.SensorProperty.Unit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-sensor.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotfleetwise as iotfleetwise
                
                sensor_property = iotfleetwise.CfnSignalCatalog.SensorProperty(
                    data_type="dataType",
                    fully_qualified_name="fullyQualifiedName",
                
                    # the properties below are optional
                    allowed_values=["allowedValues"],
                    description="description",
                    max=123,
                    min=123,
                    unit="unit"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__94596961b895ad256763fda2e339ce98264b2f53e8048d34957d691a584debcf)
                check_type(argname="argument data_type", value=data_type, expected_type=type_hints["data_type"])
                check_type(argname="argument fully_qualified_name", value=fully_qualified_name, expected_type=type_hints["fully_qualified_name"])
                check_type(argname="argument allowed_values", value=allowed_values, expected_type=type_hints["allowed_values"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument max", value=max, expected_type=type_hints["max"])
                check_type(argname="argument min", value=min, expected_type=type_hints["min"])
                check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "data_type": data_type,
                "fully_qualified_name": fully_qualified_name,
            }
            if allowed_values is not None:
                self._values["allowed_values"] = allowed_values
            if description is not None:
                self._values["description"] = description
            if max is not None:
                self._values["max"] = max
            if min is not None:
                self._values["min"] = min
            if unit is not None:
                self._values["unit"] = unit

        @builtins.property
        def data_type(self) -> builtins.str:
            '''``CfnSignalCatalog.SensorProperty.DataType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-sensor.html#cfn-iotfleetwise-signalcatalog-sensor-datatype
            '''
            result = self._values.get("data_type")
            assert result is not None, "Required property 'data_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def fully_qualified_name(self) -> builtins.str:
            '''``CfnSignalCatalog.SensorProperty.FullyQualifiedName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-sensor.html#cfn-iotfleetwise-signalcatalog-sensor-fullyqualifiedname
            '''
            result = self._values.get("fully_qualified_name")
            assert result is not None, "Required property 'fully_qualified_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def allowed_values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnSignalCatalog.SensorProperty.AllowedValues``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-sensor.html#cfn-iotfleetwise-signalcatalog-sensor-allowedvalues
            '''
            result = self._values.get("allowed_values")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''``CfnSignalCatalog.SensorProperty.Description``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-sensor.html#cfn-iotfleetwise-signalcatalog-sensor-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def max(self) -> typing.Optional[jsii.Number]:
            '''``CfnSignalCatalog.SensorProperty.Max``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-sensor.html#cfn-iotfleetwise-signalcatalog-sensor-max
            '''
            result = self._values.get("max")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def min(self) -> typing.Optional[jsii.Number]:
            '''``CfnSignalCatalog.SensorProperty.Min``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-sensor.html#cfn-iotfleetwise-signalcatalog-sensor-min
            '''
            result = self._values.get("min")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def unit(self) -> typing.Optional[builtins.str]:
            '''``CfnSignalCatalog.SensorProperty.Unit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-sensor.html#cfn-iotfleetwise-signalcatalog-sensor-unit
            '''
            result = self._values.get("unit")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SensorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnSignalCatalogProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "name": "name",
        "node_counts": "nodeCounts",
        "nodes": "nodes",
        "tags": "tags",
    },
)
class CfnSignalCatalogProps:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        node_counts: typing.Optional[typing.Union[typing.Union[CfnSignalCatalog.NodeCountsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
        nodes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnSignalCatalog.NodeProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSignalCatalog``.

        :param description: ``AWS::IoTFleetWise::SignalCatalog.Description``.
        :param name: ``AWS::IoTFleetWise::SignalCatalog.Name``.
        :param node_counts: ``AWS::IoTFleetWise::SignalCatalog.NodeCounts``.
        :param nodes: ``AWS::IoTFleetWise::SignalCatalog.Nodes``.
        :param tags: ``AWS::IoTFleetWise::SignalCatalog.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-signalcatalog.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iotfleetwise as iotfleetwise
            
            cfn_signal_catalog_props = iotfleetwise.CfnSignalCatalogProps(
                description="description",
                name="name",
                node_counts=iotfleetwise.CfnSignalCatalog.NodeCountsProperty(
                    total_actuators=123,
                    total_attributes=123,
                    total_branches=123,
                    total_nodes=123,
                    total_sensors=123
                ),
                nodes=[iotfleetwise.CfnSignalCatalog.NodeProperty(
                    actuator=iotfleetwise.CfnSignalCatalog.ActuatorProperty(
                        data_type="dataType",
                        fully_qualified_name="fullyQualifiedName",
            
                        # the properties below are optional
                        allowed_values=["allowedValues"],
                        assigned_value="assignedValue",
                        description="description",
                        max=123,
                        min=123,
                        unit="unit"
                    ),
                    attribute=iotfleetwise.CfnSignalCatalog.AttributeProperty(
                        data_type="dataType",
                        fully_qualified_name="fullyQualifiedName",
            
                        # the properties below are optional
                        allowed_values=["allowedValues"],
                        assigned_value="assignedValue",
                        default_value="defaultValue",
                        description="description",
                        max=123,
                        min=123,
                        unit="unit"
                    ),
                    branch=iotfleetwise.CfnSignalCatalog.BranchProperty(
                        fully_qualified_name="fullyQualifiedName",
            
                        # the properties below are optional
                        description="description"
                    ),
                    sensor=iotfleetwise.CfnSignalCatalog.SensorProperty(
                        data_type="dataType",
                        fully_qualified_name="fullyQualifiedName",
            
                        # the properties below are optional
                        allowed_values=["allowedValues"],
                        description="description",
                        max=123,
                        min=123,
                        unit="unit"
                    )
                )],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bd41091fa8f71325a3bfb8a9da99b2637a4ed068a31b5c7427bae2097ba03dd)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument node_counts", value=node_counts, expected_type=type_hints["node_counts"])
            check_type(argname="argument nodes", value=nodes, expected_type=type_hints["nodes"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if node_counts is not None:
            self._values["node_counts"] = node_counts
        if nodes is not None:
            self._values["nodes"] = nodes
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::SignalCatalog.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-signalcatalog.html#cfn-iotfleetwise-signalcatalog-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::SignalCatalog.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-signalcatalog.html#cfn-iotfleetwise-signalcatalog-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_counts(
        self,
    ) -> typing.Optional[typing.Union[CfnSignalCatalog.NodeCountsProperty, _IResolvable_da3f097b]]:
        '''``AWS::IoTFleetWise::SignalCatalog.NodeCounts``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-signalcatalog.html#cfn-iotfleetwise-signalcatalog-nodecounts
        '''
        result = self._values.get("node_counts")
        return typing.cast(typing.Optional[typing.Union[CfnSignalCatalog.NodeCountsProperty, _IResolvable_da3f097b]], result)

    @builtins.property
    def nodes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnSignalCatalog.NodeProperty, _IResolvable_da3f097b]]]]:
        '''``AWS::IoTFleetWise::SignalCatalog.Nodes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-signalcatalog.html#cfn-iotfleetwise-signalcatalog-nodes
        '''
        result = self._values.get("nodes")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnSignalCatalog.NodeProperty, _IResolvable_da3f097b]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''``AWS::IoTFleetWise::SignalCatalog.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-signalcatalog.html#cfn-iotfleetwise-signalcatalog-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSignalCatalogProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnVehicle(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnVehicle",
):
    '''A CloudFormation ``AWS::IoTFleetWise::Vehicle``.

    :cloudformationResource: AWS::IoTFleetWise::Vehicle
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iotfleetwise as iotfleetwise
        
        cfn_vehicle = iotfleetwise.CfnVehicle(self, "MyCfnVehicle",
            decoder_manifest_arn="decoderManifestArn",
            model_manifest_arn="modelManifestArn",
            name="name",
        
            # the properties below are optional
            association_behavior="associationBehavior",
            attributes={
                "attributes_key": "attributes"
            },
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        decoder_manifest_arn: builtins.str,
        model_manifest_arn: builtins.str,
        name: builtins.str,
        association_behavior: typing.Optional[builtins.str] = None,
        attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::IoTFleetWise::Vehicle``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param decoder_manifest_arn: ``AWS::IoTFleetWise::Vehicle.DecoderManifestArn``.
        :param model_manifest_arn: ``AWS::IoTFleetWise::Vehicle.ModelManifestArn``.
        :param name: ``AWS::IoTFleetWise::Vehicle.Name``.
        :param association_behavior: ``AWS::IoTFleetWise::Vehicle.AssociationBehavior``.
        :param attributes: ``AWS::IoTFleetWise::Vehicle.Attributes``.
        :param tags: ``AWS::IoTFleetWise::Vehicle.Tags``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7269c48709f71a558e1053c22bd1ef391024711944714eff09133981d39ff54)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnVehicleProps(
            decoder_manifest_arn=decoder_manifest_arn,
            model_manifest_arn=model_manifest_arn,
            name=name,
            association_behavior=association_behavior,
            attributes=attributes,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9b760c35be3bf4d0675af37ba807d0a1697ff44f4ca74c19616752539cb068e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__95af86f45386152805565188e4a1543fd1b5baf694bb584c01d1362547cffb8a)
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
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModificationTime")
    def attr_last_modification_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: LastModificationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastModificationTime"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''``AWS::IoTFleetWise::Vehicle.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html#cfn-iotfleetwise-vehicle-tags
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="decoderManifestArn")
    def decoder_manifest_arn(self) -> builtins.str:
        '''``AWS::IoTFleetWise::Vehicle.DecoderManifestArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html#cfn-iotfleetwise-vehicle-decodermanifestarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "decoderManifestArn"))

    @decoder_manifest_arn.setter
    def decoder_manifest_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07dfd0df1edc272a1b88da28d8fb52906df9f9da3594e4adc19e6bed64630a13)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "decoderManifestArn", value)

    @builtins.property
    @jsii.member(jsii_name="modelManifestArn")
    def model_manifest_arn(self) -> builtins.str:
        '''``AWS::IoTFleetWise::Vehicle.ModelManifestArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html#cfn-iotfleetwise-vehicle-modelmanifestarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "modelManifestArn"))

    @model_manifest_arn.setter
    def model_manifest_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44d29d9f9e6bcafa63b7a5a0e813e2a6bc9bf4dce13cba6bf0c8f3674cb8ab42)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "modelManifestArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::IoTFleetWise::Vehicle.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html#cfn-iotfleetwise-vehicle-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4505759fcded180f5aeb7d85f70fe4449363a0030d04d86046e82cc83a56ab92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="associationBehavior")
    def association_behavior(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::Vehicle.AssociationBehavior``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html#cfn-iotfleetwise-vehicle-associationbehavior
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "associationBehavior"))

    @association_behavior.setter
    def association_behavior(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58744563e98ef419016bcbd09088b8ed734d062980dbe0b3fa2e4ff0fe8f722d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "associationBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
        '''``AWS::IoTFleetWise::Vehicle.Attributes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html#cfn-iotfleetwise-vehicle-attributes
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "attributes"))

    @attributes.setter
    def attributes(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58c16f565864833e1b877bedd4f136bed80dfb02ea2ee4627d0b77770775cf1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributes", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnVehicleProps",
    jsii_struct_bases=[],
    name_mapping={
        "decoder_manifest_arn": "decoderManifestArn",
        "model_manifest_arn": "modelManifestArn",
        "name": "name",
        "association_behavior": "associationBehavior",
        "attributes": "attributes",
        "tags": "tags",
    },
)
class CfnVehicleProps:
    def __init__(
        self,
        *,
        decoder_manifest_arn: builtins.str,
        model_manifest_arn: builtins.str,
        name: builtins.str,
        association_behavior: typing.Optional[builtins.str] = None,
        attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnVehicle``.

        :param decoder_manifest_arn: ``AWS::IoTFleetWise::Vehicle.DecoderManifestArn``.
        :param model_manifest_arn: ``AWS::IoTFleetWise::Vehicle.ModelManifestArn``.
        :param name: ``AWS::IoTFleetWise::Vehicle.Name``.
        :param association_behavior: ``AWS::IoTFleetWise::Vehicle.AssociationBehavior``.
        :param attributes: ``AWS::IoTFleetWise::Vehicle.Attributes``.
        :param tags: ``AWS::IoTFleetWise::Vehicle.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iotfleetwise as iotfleetwise
            
            cfn_vehicle_props = iotfleetwise.CfnVehicleProps(
                decoder_manifest_arn="decoderManifestArn",
                model_manifest_arn="modelManifestArn",
                name="name",
            
                # the properties below are optional
                association_behavior="associationBehavior",
                attributes={
                    "attributes_key": "attributes"
                },
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24066091b85e61810110bf13ed6c1606f4b16a2637a0ea85ffb516d58b89a826)
            check_type(argname="argument decoder_manifest_arn", value=decoder_manifest_arn, expected_type=type_hints["decoder_manifest_arn"])
            check_type(argname="argument model_manifest_arn", value=model_manifest_arn, expected_type=type_hints["model_manifest_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument association_behavior", value=association_behavior, expected_type=type_hints["association_behavior"])
            check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "decoder_manifest_arn": decoder_manifest_arn,
            "model_manifest_arn": model_manifest_arn,
            "name": name,
        }
        if association_behavior is not None:
            self._values["association_behavior"] = association_behavior
        if attributes is not None:
            self._values["attributes"] = attributes
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def decoder_manifest_arn(self) -> builtins.str:
        '''``AWS::IoTFleetWise::Vehicle.DecoderManifestArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html#cfn-iotfleetwise-vehicle-decodermanifestarn
        '''
        result = self._values.get("decoder_manifest_arn")
        assert result is not None, "Required property 'decoder_manifest_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def model_manifest_arn(self) -> builtins.str:
        '''``AWS::IoTFleetWise::Vehicle.ModelManifestArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html#cfn-iotfleetwise-vehicle-modelmanifestarn
        '''
        result = self._values.get("model_manifest_arn")
        assert result is not None, "Required property 'model_manifest_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::IoTFleetWise::Vehicle.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html#cfn-iotfleetwise-vehicle-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def association_behavior(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTFleetWise::Vehicle.AssociationBehavior``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html#cfn-iotfleetwise-vehicle-associationbehavior
        '''
        result = self._values.get("association_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def attributes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
        '''``AWS::IoTFleetWise::Vehicle.Attributes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html#cfn-iotfleetwise-vehicle-attributes
        '''
        result = self._values.get("attributes")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''``AWS::IoTFleetWise::Vehicle.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html#cfn-iotfleetwise-vehicle-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVehicleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCampaign",
    "CfnCampaignProps",
    "CfnDecoderManifest",
    "CfnDecoderManifestProps",
    "CfnFleet",
    "CfnFleetProps",
    "CfnModelManifest",
    "CfnModelManifestProps",
    "CfnSignalCatalog",
    "CfnSignalCatalogProps",
    "CfnVehicle",
    "CfnVehicleProps",
]

publication.publish()

def _typecheckingstub__f7abc45d2046b48ec3bc5807ec2826a784930a5009b41b194dd6e4bed2413f8d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    action: builtins.str,
    collection_scheme: typing.Union[typing.Union[CfnCampaign.CollectionSchemeProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b],
    name: builtins.str,
    signal_catalog_arn: builtins.str,
    target_arn: builtins.str,
    compression: typing.Optional[builtins.str] = None,
    data_extra_dimensions: typing.Optional[typing.Sequence[builtins.str]] = None,
    description: typing.Optional[builtins.str] = None,
    diagnostics_mode: typing.Optional[builtins.str] = None,
    expiry_time: typing.Optional[builtins.str] = None,
    post_trigger_collection_duration: typing.Optional[jsii.Number] = None,
    priority: typing.Optional[jsii.Number] = None,
    signals_to_collect: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnCampaign.SignalInformationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
    spooling_mode: typing.Optional[builtins.str] = None,
    start_time: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09fbf1d259fb24b3ffc81851949fdbc1abbaa3df7fef9d0031938dd5b723205f(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89d4f6e55fdf4b8418716e773b2a62dc1763b8a2553490a7567e2cfe6f27d77f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66dafa89e69b8562346040c56213280b8861d04a6b73911f5471941f58e3d463(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__868a9ff35e32583e37d3c029fdca22ea031055a38c7dd0dcbfa1f30846ee551d(
    value: typing.Union[CfnCampaign.CollectionSchemeProperty, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61dfb8819034de21f19e0466ab15e542f6b7270be82092cfffb60970bbc9708b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5a5ce376850a7a86f93938b2f133fca5cc48d27769ddbdcaf2291ab00d48bac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6154b7ad20e73a4e23143d3707a09d050bbb1092b307bc8e0145589083575f5a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17ec1dfb29d11e0d55dc84fc23937babfb2d1e33fdf8192c23c4130716fa6a02(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d948dada7b0177410b9932e42eb5ef3a76fe3c3274594fb0b3ffa49ded440324(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24bd4808a24c1ef5c17e4550fe902693202fc86dca7d97ddddcd994c722276bf(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e28d99e6bd56db5b97b272b04aeb5c1af8103d1b8b0080fe05d1a5f2fb149e2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11cce95e76c12143123da5bc8c755592e90256d2ed3e61b6cd5a6d839e9318e9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__660bebd5ebd77dcec64e7fcb6fd086f3ce7252832c2b9967a58fbda5d5fe6bd2(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7eceb1aaf4de04c54d69e423a5e6de547b2e207a605050b36deefed0ccc4c9b8(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49e9a686748dfc74bfa8ee7c7e9c87ccd64dc236b6b72144f22cebb87065a3d7(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnCampaign.SignalInformationProperty, _IResolvable_da3f097b]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2470f955a4e2089dd25722e38734a0e9fffc60420def257c19a15c6db378b523(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67bb9c23f09e7b35b9a93baa91bd26954a931e9dac0ecfa4b472a8de197849a7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d2862e457404e83c11e21830d9ccb15c52f442305bb2db0a1ebf80b0de3877a(
    *,
    condition_based_collection_scheme: typing.Optional[typing.Union[typing.Union[CfnCampaign.ConditionBasedCollectionSchemeProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    time_based_collection_scheme: typing.Optional[typing.Union[typing.Union[CfnCampaign.TimeBasedCollectionSchemeProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd3351de9470a98f13f006dd95deedef6c30dbfc08cdfe7bde2b9d950d547615(
    *,
    expression: builtins.str,
    condition_language_version: typing.Optional[jsii.Number] = None,
    minimum_trigger_interval_ms: typing.Optional[jsii.Number] = None,
    trigger_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53d5027f8c4da8a26f3f9cf9e5ab42f41c46c70820c567f2c340ad26784c6997(
    *,
    name: builtins.str,
    max_sample_count: typing.Optional[jsii.Number] = None,
    minimum_sampling_interval_ms: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bffeabbd9e812e2b77c405369e410069d9bd5d47737b57d4b23d11433d93329(
    *,
    period_ms: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54c45792d3f0c102d3358acf678401b9616a7fee4b70882083776c5f9635cf71(
    *,
    action: builtins.str,
    collection_scheme: typing.Union[typing.Union[CfnCampaign.CollectionSchemeProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b],
    name: builtins.str,
    signal_catalog_arn: builtins.str,
    target_arn: builtins.str,
    compression: typing.Optional[builtins.str] = None,
    data_extra_dimensions: typing.Optional[typing.Sequence[builtins.str]] = None,
    description: typing.Optional[builtins.str] = None,
    diagnostics_mode: typing.Optional[builtins.str] = None,
    expiry_time: typing.Optional[builtins.str] = None,
    post_trigger_collection_duration: typing.Optional[jsii.Number] = None,
    priority: typing.Optional[jsii.Number] = None,
    signals_to_collect: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnCampaign.SignalInformationProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
    spooling_mode: typing.Optional[builtins.str] = None,
    start_time: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd0d8efce6baca0fa606fb0cf95bebcdeda196fcde2fb7e18542334332eb8ba4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    model_manifest_arn: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    network_interfaces: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnDecoderManifest.NetworkInterfacesItemsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
    signal_decoders: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnDecoderManifest.SignalDecodersItemsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
    status: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7c1f4e3cc81a06a60eef4d178a3aaf54f7c99cca4a0481a51c50d560d76ba09(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d12e1e0a1684404c74ecc86ed4ae33ffdac8b3611db04d45a6a46ef55c87bbbe(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b8f77dd16bf3c88bd7f097b2327803bb360213ddb0b320722348c6a1b99afce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a5a43cce0da85f8ef5934babccfc93088317c19ae303a38ae3adc573ad6c633(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1e4501ad7312a6dac9b29817aed239a25a724386677541e036223da190a2d9b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4059f7868b58b43acd642cd2537b59a16c939681bb626ef560a6efbc8d7cda5(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnDecoderManifest.NetworkInterfacesItemsProperty, _IResolvable_da3f097b]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32a124503ae0a9be522e3691aef89b61eb023aea0d8b57342dcef4a708073af0(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnDecoderManifest.SignalDecodersItemsProperty, _IResolvable_da3f097b]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8428ef9254e1885dc4fbe7c358202136e77b7b7c68b9e9b92c6016edfca9ad8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f41ef25a35e6c8526ccaa9ecc87becb68ccffe031fd1ae9c650719807164dc68(
    *,
    name: builtins.str,
    protocol_name: typing.Optional[builtins.str] = None,
    protocol_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1fdd86137a92797754860d3b8da115496d862a2f95c8e39c08a70fdf76855c4(
    *,
    factor: builtins.str,
    is_big_endian: builtins.str,
    is_signed: builtins.str,
    length: builtins.str,
    message_id: builtins.str,
    offset: builtins.str,
    start_bit: builtins.str,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__763a8a9c006b5f64d4a07d45a9f83b3a4b0be692630292c6e33fd7f6c09a4c07(
    *,
    interface_id: builtins.str,
    type: builtins.str,
    can_interface: typing.Optional[typing.Union[typing.Union[CfnDecoderManifest.CanInterfaceProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    obd_interface: typing.Optional[typing.Union[typing.Union[CfnDecoderManifest.ObdInterfaceProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__619deb4a5a81c6ae8bcb58cd0d96a9beddd6b7ac867f4e945e1bd4668fc25b17(
    *,
    name: builtins.str,
    request_message_id: builtins.str,
    dtc_request_interval_seconds: typing.Optional[builtins.str] = None,
    has_transmission_ecu: typing.Optional[builtins.str] = None,
    obd_standard: typing.Optional[builtins.str] = None,
    pid_request_interval_seconds: typing.Optional[builtins.str] = None,
    use_extended_ids: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccb776ce607aa563ef4bc105956ab186267e45066ee492c162a4555709004e4b(
    *,
    byte_length: builtins.str,
    offset: builtins.str,
    pid: builtins.str,
    pid_response_length: builtins.str,
    scaling: builtins.str,
    service_mode: builtins.str,
    start_byte: builtins.str,
    bit_mask_length: typing.Optional[builtins.str] = None,
    bit_right_shift: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5832121c7c16050419993147c157e7f5739fca1dc1afba25d1f52da2d4bd75fb(
    *,
    fully_qualified_name: builtins.str,
    interface_id: builtins.str,
    type: builtins.str,
    can_signal: typing.Optional[typing.Union[typing.Union[CfnDecoderManifest.CanSignalProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    obd_signal: typing.Optional[typing.Union[typing.Union[CfnDecoderManifest.ObdSignalProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1be5cfb3ca0441a2fdb0856303c08c4449592f7472588f5c0659c42af4d89e2c(
    *,
    model_manifest_arn: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    network_interfaces: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnDecoderManifest.NetworkInterfacesItemsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
    signal_decoders: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnDecoderManifest.SignalDecodersItemsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
    status: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be2399a288ba3f0fe4eba6c31d42082d31eac165febede18736a759d92f2120d(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    id: builtins.str,
    signal_catalog_arn: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b66a25ffe3875464ec35ff63e6d6335f63f5bd966c356414cfa0ec840225eedd(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19ef6ad0585e294dae29b4c919f9fbf11b89c72deadd5a5cda8a56f1433235a8(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__521c3cdc3b4991a92beb684d8c8af88ceab73dcbd34d08d120663c9c7f94d059(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eec1aed040f26806fdbfee937ccf8c8b0ccb036bc460096cfbb5b04da65cccca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47625bcd41335399a9f769fa64574c2375f2937ed4511d09a3984dbd0abef447(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06c4343c5d692e914e7c2c900c5e4f0c5bed9b41e2c90ff1efc672ba0974c3d8(
    *,
    id: builtins.str,
    signal_catalog_arn: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f0e03fe14f53de97f2e7071c7f10132492e794782f840695921dc42cd286a81(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    signal_catalog_arn: builtins.str,
    description: typing.Optional[builtins.str] = None,
    nodes: typing.Optional[typing.Sequence[builtins.str]] = None,
    status: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26ab7dc28e60a5682365801d22047c22eca01f42fd1ecbb3b9b379fa832ee14c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6a3d382e4e768e4426411dff74ffd0bcaba33058efbe3e880fae9c7ace6d5d3(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf56f12f94bd9c70533145a1dbb473b412b33dff8bc3791a2bcad34f29302b8d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9c26dfed7e5cc0b2e5105665abac1ffd59d367b056759c9e21642fa1214969e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d266113c8b366f668b05115f1bddeefd3b243d1c8fd8eecc3c143d130167d11(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f0af1e0b1687e8bdbdeec73691f1b3cac6582b744e41041b611118e281c9134(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f57f8c832da7ae938e0025bdef8ca3f24978b35cafd09be0c6bc21a8ee3329a9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1235282929965217b607172340e97ee502a13c24469f00158a042c2a92786260(
    *,
    name: builtins.str,
    signal_catalog_arn: builtins.str,
    description: typing.Optional[builtins.str] = None,
    nodes: typing.Optional[typing.Sequence[builtins.str]] = None,
    status: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00a926b4b26fd9efc933b63c5d4e497e8bfeceb8f4fb16790d18152e0fd2e282(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    node_counts: typing.Optional[typing.Union[typing.Union[CfnSignalCatalog.NodeCountsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    nodes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnSignalCatalog.NodeProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d1771c8f83cb9b124255f0cb877c396f7dc19033885dac73e197f274702fe58(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c1bc0963e13c138e8b1a9d56f8dfaba2b1c3f856cd9d0bc996158b2c5b704bb(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f426284778d609b7de7cea520eccf5230e025cc40e766b3f3f0a9b3c536bfe4a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1be488894dded62944d72e0b078393e92b8c846e12e5682732e5b292abdf03c1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f8c5daca018b1e857e68a1c38c2d8c8ad48c3e10d76e27f1b88db531cc7800d(
    value: typing.Optional[typing.Union[CfnSignalCatalog.NodeCountsProperty, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__017bfa378203e76812e9cd13928c4c7498a8ed198568cb4d309d165dee01a3b3(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[CfnSignalCatalog.NodeProperty, _IResolvable_da3f097b]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3692c9418e6188deb5e6f1b10c8f51484f74857c2b24c543b0730826f0e8014c(
    *,
    data_type: builtins.str,
    fully_qualified_name: builtins.str,
    allowed_values: typing.Optional[typing.Sequence[builtins.str]] = None,
    assigned_value: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    max: typing.Optional[jsii.Number] = None,
    min: typing.Optional[jsii.Number] = None,
    unit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34812da89e0890988b83a21707bc72187e1251886f85c8d31c8bad4f51a5ad5d(
    *,
    data_type: builtins.str,
    fully_qualified_name: builtins.str,
    allowed_values: typing.Optional[typing.Sequence[builtins.str]] = None,
    assigned_value: typing.Optional[builtins.str] = None,
    default_value: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    max: typing.Optional[jsii.Number] = None,
    min: typing.Optional[jsii.Number] = None,
    unit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10c551cff70ab7e9a7ade619807100cf531ce4f17b5ade4cfc711a7110032c76(
    *,
    fully_qualified_name: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0ecad1dc29fa151da6ab7009debe26c40391783260739fb2c93faa85a3ff88d(
    *,
    total_actuators: typing.Optional[jsii.Number] = None,
    total_attributes: typing.Optional[jsii.Number] = None,
    total_branches: typing.Optional[jsii.Number] = None,
    total_nodes: typing.Optional[jsii.Number] = None,
    total_sensors: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f7b644285514f42793054887b78a595b6a6dc6b59e3a153fd29b94fb12c45e0(
    *,
    actuator: typing.Optional[typing.Union[typing.Union[CfnSignalCatalog.ActuatorProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    attribute: typing.Optional[typing.Union[typing.Union[CfnSignalCatalog.AttributeProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    branch: typing.Optional[typing.Union[typing.Union[CfnSignalCatalog.BranchProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    sensor: typing.Optional[typing.Union[typing.Union[CfnSignalCatalog.SensorProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94596961b895ad256763fda2e339ce98264b2f53e8048d34957d691a584debcf(
    *,
    data_type: builtins.str,
    fully_qualified_name: builtins.str,
    allowed_values: typing.Optional[typing.Sequence[builtins.str]] = None,
    description: typing.Optional[builtins.str] = None,
    max: typing.Optional[jsii.Number] = None,
    min: typing.Optional[jsii.Number] = None,
    unit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bd41091fa8f71325a3bfb8a9da99b2637a4ed068a31b5c7427bae2097ba03dd(
    *,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    node_counts: typing.Optional[typing.Union[typing.Union[CfnSignalCatalog.NodeCountsProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]] = None,
    nodes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[typing.Union[CfnSignalCatalog.NodeProperty, typing.Dict[builtins.str, typing.Any]], _IResolvable_da3f097b]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7269c48709f71a558e1053c22bd1ef391024711944714eff09133981d39ff54(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    decoder_manifest_arn: builtins.str,
    model_manifest_arn: builtins.str,
    name: builtins.str,
    association_behavior: typing.Optional[builtins.str] = None,
    attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9b760c35be3bf4d0675af37ba807d0a1697ff44f4ca74c19616752539cb068e(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95af86f45386152805565188e4a1543fd1b5baf694bb584c01d1362547cffb8a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07dfd0df1edc272a1b88da28d8fb52906df9f9da3594e4adc19e6bed64630a13(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44d29d9f9e6bcafa63b7a5a0e813e2a6bc9bf4dce13cba6bf0c8f3674cb8ab42(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4505759fcded180f5aeb7d85f70fe4449363a0030d04d86046e82cc83a56ab92(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58744563e98ef419016bcbd09088b8ed734d062980dbe0b3fa2e4ff0fe8f722d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58c16f565864833e1b877bedd4f136bed80dfb02ea2ee4627d0b77770775cf1c(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24066091b85e61810110bf13ed6c1606f4b16a2637a0ea85ffb516d58b89a826(
    *,
    decoder_manifest_arn: builtins.str,
    model_manifest_arn: builtins.str,
    name: builtins.str,
    association_behavior: typing.Optional[builtins.str] = None,
    attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

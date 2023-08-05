'''
# Amazon Pinpoint Email Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_pinpointemail as pinpointemail
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

from ._jsii import *

import aws_cdk.core as _aws_cdk_core_f4b25747


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnConfigurationSet(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-pinpointemail.CfnConfigurationSet",
):
    '''A CloudFormation ``AWS::PinpointEmail::ConfigurationSet``.

    Create a configuration set. *Configuration sets* are groups of rules that you can apply to the emails you send using Amazon Pinpoint. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.

    :cloudformationResource: AWS::PinpointEmail::ConfigurationSet
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_pinpointemail as pinpointemail
        
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
        scope: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        delivery_options: typing.Optional[typing.Union[typing.Union["CfnConfigurationSet.DeliveryOptionsProperty", typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable]] = None,
        reputation_options: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnConfigurationSet.ReputationOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        sending_options: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnConfigurationSet.SendingOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["CfnConfigurationSet.TagsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tracking_options: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnConfigurationSet.TrackingOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
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
            type_hints = typing.get_type_hints(_typecheckingstub__79c94b7097d570913e6a201b16742195ba872eb77c6f30d31df80ff707a61cef)
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
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d878a70a9abcc05484d45875ba6fa820b448ef9cb6f6b7df2f49d4d8d8c8ac73)
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
            type_hints = typing.get_type_hints(_typecheckingstub__08fa61ea72e62043ee69f8c5d86b0884426774d5d728e888470db8e09d11b47e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__56d17b1c947a821bd0deae9a759b52b0aaf93bee51979a3738142934a3c01baa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="deliveryOptions")
    def delivery_options(
        self,
    ) -> typing.Optional[typing.Union["CfnConfigurationSet.DeliveryOptionsProperty", _aws_cdk_core_f4b25747.IResolvable]]:
        '''An object that defines the dedicated IP pool that is used to send emails that you send using the configuration set.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-deliveryoptions
        '''
        return typing.cast(typing.Optional[typing.Union["CfnConfigurationSet.DeliveryOptionsProperty", _aws_cdk_core_f4b25747.IResolvable]], jsii.get(self, "deliveryOptions"))

    @delivery_options.setter
    def delivery_options(
        self,
        value: typing.Optional[typing.Union["CfnConfigurationSet.DeliveryOptionsProperty", _aws_cdk_core_f4b25747.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__751d315454bfa515de0a354ee7d91822b64a2ac84ba746742c1761e3910c760e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deliveryOptions", value)

    @builtins.property
    @jsii.member(jsii_name="reputationOptions")
    def reputation_options(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnConfigurationSet.ReputationOptionsProperty"]]:
        '''An object that defines whether or not Amazon Pinpoint collects reputation metrics for the emails that you send that use the configuration set.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-reputationoptions
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnConfigurationSet.ReputationOptionsProperty"]], jsii.get(self, "reputationOptions"))

    @reputation_options.setter
    def reputation_options(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnConfigurationSet.ReputationOptionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56ea513e848ece3789871bac01fac32f40c9ed2cc13a7f43ac805e644df92e95)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reputationOptions", value)

    @builtins.property
    @jsii.member(jsii_name="sendingOptions")
    def sending_options(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnConfigurationSet.SendingOptionsProperty"]]:
        '''An object that defines whether or not Amazon Pinpoint can send email that you send using the configuration set.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-sendingoptions
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnConfigurationSet.SendingOptionsProperty"]], jsii.get(self, "sendingOptions"))

    @sending_options.setter
    def sending_options(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnConfigurationSet.SendingOptionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6016e4ab249cda5144333d432f68f798dd6d5b82c98bd958033e7b3fdd2df19d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9a0e0e4cde3fb60dcb4f3b8af87f5ca2e15f51961b8659a7e680bdd45f998c45)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="trackingOptions")
    def tracking_options(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnConfigurationSet.TrackingOptionsProperty"]]:
        '''An object that defines the open and click tracking options for emails that you send using the configuration set.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-trackingoptions
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnConfigurationSet.TrackingOptionsProperty"]], jsii.get(self, "trackingOptions"))

    @tracking_options.setter
    def tracking_options(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnConfigurationSet.TrackingOptionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1a5dceca245e615b9ca3b6029b58980958957028f9bd1f432c701a56b076821)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trackingOptions", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpointemail.CfnConfigurationSet.DeliveryOptionsProperty",
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
                import aws_cdk.aws_pinpointemail as pinpointemail
                
                delivery_options_property = pinpointemail.CfnConfigurationSet.DeliveryOptionsProperty(
                    sending_pool_name="sendingPoolName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b5bbfa12155f563a1c861522d0860321d3965f2750ac6961bfa363db9cd366a6)
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
        jsii_type="@aws-cdk/aws-pinpointemail.CfnConfigurationSet.ReputationOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"reputation_metrics_enabled": "reputationMetricsEnabled"},
    )
    class ReputationOptionsProperty:
        def __init__(
            self,
            *,
            reputation_metrics_enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
        ) -> None:
            '''Enable or disable collection of reputation metrics for emails that you send using this configuration set in the current AWS Region.

            :param reputation_metrics_enabled: If ``true`` , tracking of reputation metrics is enabled for the configuration set. If ``false`` , tracking of reputation metrics is disabled for the configuration set.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-reputationoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_pinpointemail as pinpointemail
                
                reputation_options_property = pinpointemail.CfnConfigurationSet.ReputationOptionsProperty(
                    reputation_metrics_enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__78c7de2f370c6c9cf08de8cfd651c4370d397e04f1542acdbcaf40bd37cfd514)
                check_type(argname="argument reputation_metrics_enabled", value=reputation_metrics_enabled, expected_type=type_hints["reputation_metrics_enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if reputation_metrics_enabled is not None:
                self._values["reputation_metrics_enabled"] = reputation_metrics_enabled

        @builtins.property
        def reputation_metrics_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''If ``true`` , tracking of reputation metrics is enabled for the configuration set.

            If ``false`` , tracking of reputation metrics is disabled for the configuration set.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-reputationoptions.html#cfn-pinpointemail-configurationset-reputationoptions-reputationmetricsenabled
            '''
            result = self._values.get("reputation_metrics_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ReputationOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpointemail.CfnConfigurationSet.SendingOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"sending_enabled": "sendingEnabled"},
    )
    class SendingOptionsProperty:
        def __init__(
            self,
            *,
            sending_enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
        ) -> None:
            '''Used to enable or disable email sending for messages that use this configuration set in the current AWS Region.

            :param sending_enabled: If ``true`` , email sending is enabled for the configuration set. If ``false`` , email sending is disabled for the configuration set.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-sendingoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_pinpointemail as pinpointemail
                
                sending_options_property = pinpointemail.CfnConfigurationSet.SendingOptionsProperty(
                    sending_enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d1afd5e8d830ec288b9ea9a1947ba73df2d53dd74f6f7aa8cceed6c989e49f2c)
                check_type(argname="argument sending_enabled", value=sending_enabled, expected_type=type_hints["sending_enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if sending_enabled is not None:
                self._values["sending_enabled"] = sending_enabled

        @builtins.property
        def sending_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''If ``true`` , email sending is enabled for the configuration set.

            If ``false`` , email sending is disabled for the configuration set.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationset-sendingoptions.html#cfn-pinpointemail-configurationset-sendingoptions-sendingenabled
            '''
            result = self._values.get("sending_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SendingOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpointemail.CfnConfigurationSet.TagsProperty",
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
                import aws_cdk.aws_pinpointemail as pinpointemail
                
                tags_property = pinpointemail.CfnConfigurationSet.TagsProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c777e74aa4c547e7e771f0fc07b792618fc2a7f1eb670dea1eca5ff8e212605d)
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
        jsii_type="@aws-cdk/aws-pinpointemail.CfnConfigurationSet.TrackingOptionsProperty",
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
                import aws_cdk.aws_pinpointemail as pinpointemail
                
                tracking_options_property = pinpointemail.CfnConfigurationSet.TrackingOptionsProperty(
                    custom_redirect_domain="customRedirectDomain"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2f3be60d81c1e75c6b4e7018c614f0e1df3d7fc504d2d81db89a10322813b9db)
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


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnConfigurationSetEventDestination(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-pinpointemail.CfnConfigurationSetEventDestination",
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
        import aws_cdk.aws_pinpointemail as pinpointemail
        
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
        scope: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        configuration_set_name: builtins.str,
        event_destination_name: builtins.str,
        event_destination: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnConfigurationSetEventDestination.EventDestinationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::PinpointEmail::ConfigurationSetEventDestination``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param configuration_set_name: The name of the configuration set that contains the event destination that you want to modify.
        :param event_destination_name: The name of the event destination that you want to modify.
        :param event_destination: An object that defines the event destination.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__571aa6db5d6903e39a0d354c8576b598395d23afbca33c0a7c933c062d070f13)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConfigurationSetEventDestinationProps(
            configuration_set_name=configuration_set_name,
            event_destination_name=event_destination_name,
            event_destination=event_destination,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6289bbe4d1ae11ec7870b9fcbb8873737f41a617487978eaf82afdd4bb6526c8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a2a1ae85bdb74c360def78020fd398d34b95d327146b3b36a24a812129e211a6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2bd15f0da6a34b43477fdba06f28323694db2d456e51332712efce08305e8d76)
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
            type_hints = typing.get_type_hints(_typecheckingstub__844bf86b5b3511c44c4b387fefa320977da6cbcbaecfedaaa06a390b9d5c4d96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventDestinationName", value)

    @builtins.property
    @jsii.member(jsii_name="eventDestination")
    def event_destination(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnConfigurationSetEventDestination.EventDestinationProperty"]]:
        '''An object that defines the event destination.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationseteventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestination
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnConfigurationSetEventDestination.EventDestinationProperty"]], jsii.get(self, "eventDestination"))

    @event_destination.setter
    def event_destination(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnConfigurationSetEventDestination.EventDestinationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fe1320e93d4c5127a8931b810a88f7adf31e084cdcdb23c5112877c496bd4cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventDestination", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpointemail.CfnConfigurationSetEventDestination.CloudWatchDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"dimension_configurations": "dimensionConfigurations"},
    )
    class CloudWatchDestinationProperty:
        def __init__(
            self,
            *,
            dimension_configurations: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnConfigurationSetEventDestination.DimensionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''An object that defines an Amazon CloudWatch destination for email events.

            You can use Amazon CloudWatch to monitor and gain insights on your email sending metrics.

            :param dimension_configurations: An array of objects that define the dimensions to use when you send email events to Amazon CloudWatch.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-cloudwatchdestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_pinpointemail as pinpointemail
                
                cloud_watch_destination_property = pinpointemail.CfnConfigurationSetEventDestination.CloudWatchDestinationProperty(
                    dimension_configurations=[pinpointemail.CfnConfigurationSetEventDestination.DimensionConfigurationProperty(
                        default_dimension_value="defaultDimensionValue",
                        dimension_name="dimensionName",
                        dimension_value_source="dimensionValueSource"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a6f5ee8448219389bf17a885586e478865bd6d58810dd01e79187f3039082a40)
                check_type(argname="argument dimension_configurations", value=dimension_configurations, expected_type=type_hints["dimension_configurations"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if dimension_configurations is not None:
                self._values["dimension_configurations"] = dimension_configurations

        @builtins.property
        def dimension_configurations(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnConfigurationSetEventDestination.DimensionConfigurationProperty"]]]]:
            '''An array of objects that define the dimensions to use when you send email events to Amazon CloudWatch.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-cloudwatchdestination.html#cfn-pinpointemail-configurationseteventdestination-cloudwatchdestination-dimensionconfigurations
            '''
            result = self._values.get("dimension_configurations")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnConfigurationSetEventDestination.DimensionConfigurationProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpointemail.CfnConfigurationSetEventDestination.DimensionConfigurationProperty",
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
                import aws_cdk.aws_pinpointemail as pinpointemail
                
                dimension_configuration_property = pinpointemail.CfnConfigurationSetEventDestination.DimensionConfigurationProperty(
                    default_dimension_value="defaultDimensionValue",
                    dimension_name="dimensionName",
                    dimension_value_source="dimensionValueSource"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__60e213f08de6688a76df4a372af3edd2a80383b65a7d41d7b3d7feaa99cc4e57)
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
        jsii_type="@aws-cdk/aws-pinpointemail.CfnConfigurationSetEventDestination.EventDestinationProperty",
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
            cloud_watch_destination: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnConfigurationSetEventDestination.CloudWatchDestinationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            kinesis_firehose_destination: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            pinpoint_destination: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnConfigurationSetEventDestination.PinpointDestinationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sns_destination: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnConfigurationSetEventDestination.SnsDestinationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
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
                import aws_cdk.aws_pinpointemail as pinpointemail
                
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
                type_hints = typing.get_type_hints(_typecheckingstub__4eeca540a4946d9d259112b13a21f31ff12160d9a5ecb81ffe343432508f960b)
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
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnConfigurationSetEventDestination.CloudWatchDestinationProperty"]]:
            '''An object that defines an Amazon CloudWatch destination for email events.

            You can use Amazon CloudWatch to monitor and gain insights on your email sending metrics.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-eventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestination-cloudwatchdestination
            '''
            result = self._values.get("cloud_watch_destination")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnConfigurationSetEventDestination.CloudWatchDestinationProperty"]], result)

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''If ``true`` , the event destination is enabled.

            When the event destination is enabled, the specified event types are sent to the destinations in this ``EventDestinationDefinition`` .

            If ``false`` , the event destination is disabled. When the event destination is disabled, events aren't sent to the specified destinations.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-eventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestination-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def kinesis_firehose_destination(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty"]]:
            '''An object that defines an Amazon Kinesis Data Firehose destination for email events.

            You can use Amazon Kinesis Data Firehose to stream data to other services, such as Amazon S3 and Amazon Redshift.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-eventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestination-kinesisfirehosedestination
            '''
            result = self._values.get("kinesis_firehose_destination")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty"]], result)

        @builtins.property
        def pinpoint_destination(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnConfigurationSetEventDestination.PinpointDestinationProperty"]]:
            '''An object that defines a Amazon Pinpoint destination for email events.

            You can use Amazon Pinpoint events to create attributes in Amazon Pinpoint projects. You can use these attributes to create segments for your campaigns.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-eventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestination-pinpointdestination
            '''
            result = self._values.get("pinpoint_destination")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnConfigurationSetEventDestination.PinpointDestinationProperty"]], result)

        @builtins.property
        def sns_destination(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnConfigurationSetEventDestination.SnsDestinationProperty"]]:
            '''An object that defines an Amazon SNS destination for email events.

            You can use Amazon SNS to send notification when certain email events occur.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpointemail-configurationseteventdestination-eventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestination-snsdestination
            '''
            result = self._values.get("sns_destination")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnConfigurationSetEventDestination.SnsDestinationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpointemail.CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty",
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
                import aws_cdk.aws_pinpointemail as pinpointemail
                
                kinesis_firehose_destination_property = pinpointemail.CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty(
                    delivery_stream_arn="deliveryStreamArn",
                    iam_role_arn="iamRoleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__253654f1867164e627b33da791dc07d7a058bf6598fa0dc6a5f6bb10621fdb96)
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
        jsii_type="@aws-cdk/aws-pinpointemail.CfnConfigurationSetEventDestination.PinpointDestinationProperty",
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
                import aws_cdk.aws_pinpointemail as pinpointemail
                
                pinpoint_destination_property = pinpointemail.CfnConfigurationSetEventDestination.PinpointDestinationProperty(
                    application_arn="applicationArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f349cc8501e51253fffafb0382e541bb6f653a88b1ecab4390488c1c22c586c2)
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
        jsii_type="@aws-cdk/aws-pinpointemail.CfnConfigurationSetEventDestination.SnsDestinationProperty",
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
                import aws_cdk.aws_pinpointemail as pinpointemail
                
                sns_destination_property = pinpointemail.CfnConfigurationSetEventDestination.SnsDestinationProperty(
                    topic_arn="topicArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e70b66abb7dba1a29243f60c80ef9b9d0935966ba049cbb973dd16b64398d16c)
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
    jsii_type="@aws-cdk/aws-pinpointemail.CfnConfigurationSetEventDestinationProps",
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
        event_destination: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnConfigurationSetEventDestination.EventDestinationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
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
            import aws_cdk.aws_pinpointemail as pinpointemail
            
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
            type_hints = typing.get_type_hints(_typecheckingstub__1e7de4d76acaf8d229ed0fb8017828fdcb02d0c8b4167164aa473c83581b9e1d)
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
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnConfigurationSetEventDestination.EventDestinationProperty]]:
        '''An object that defines the event destination.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationseteventdestination.html#cfn-pinpointemail-configurationseteventdestination-eventdestination
        '''
        result = self._values.get("event_destination")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnConfigurationSetEventDestination.EventDestinationProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConfigurationSetEventDestinationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-pinpointemail.CfnConfigurationSetProps",
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
        delivery_options: typing.Optional[typing.Union[typing.Union[CfnConfigurationSet.DeliveryOptionsProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable]] = None,
        reputation_options: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnConfigurationSet.ReputationOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        sending_options: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnConfigurationSet.SendingOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[CfnConfigurationSet.TagsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tracking_options: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnConfigurationSet.TrackingOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
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
            import aws_cdk.aws_pinpointemail as pinpointemail
            
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
            type_hints = typing.get_type_hints(_typecheckingstub__fc270122928b23b61ee26cc1d5480a105dd444ef06cf54765bf0b7fc012c5dbc)
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
    ) -> typing.Optional[typing.Union[CfnConfigurationSet.DeliveryOptionsProperty, _aws_cdk_core_f4b25747.IResolvable]]:
        '''An object that defines the dedicated IP pool that is used to send emails that you send using the configuration set.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-deliveryoptions
        '''
        result = self._values.get("delivery_options")
        return typing.cast(typing.Optional[typing.Union[CfnConfigurationSet.DeliveryOptionsProperty, _aws_cdk_core_f4b25747.IResolvable]], result)

    @builtins.property
    def reputation_options(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnConfigurationSet.ReputationOptionsProperty]]:
        '''An object that defines whether or not Amazon Pinpoint collects reputation metrics for the emails that you send that use the configuration set.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-reputationoptions
        '''
        result = self._values.get("reputation_options")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnConfigurationSet.ReputationOptionsProperty]], result)

    @builtins.property
    def sending_options(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnConfigurationSet.SendingOptionsProperty]]:
        '''An object that defines whether or not Amazon Pinpoint can send email that you send using the configuration set.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-sendingoptions
        '''
        result = self._values.get("sending_options")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnConfigurationSet.SendingOptionsProperty]], result)

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
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnConfigurationSet.TrackingOptionsProperty]]:
        '''An object that defines the open and click tracking options for emails that you send using the configuration set.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html#cfn-pinpointemail-configurationset-trackingoptions
        '''
        result = self._values.get("tracking_options")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnConfigurationSet.TrackingOptionsProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConfigurationSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnDedicatedIpPool(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-pinpointemail.CfnDedicatedIpPool",
):
    '''A CloudFormation ``AWS::PinpointEmail::DedicatedIpPool``.

    A request to create a new dedicated IP pool.

    :cloudformationResource: AWS::PinpointEmail::DedicatedIpPool
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-dedicatedippool.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_pinpointemail as pinpointemail
        
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
        scope: _aws_cdk_core_f4b25747.Construct,
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
            type_hints = typing.get_type_hints(_typecheckingstub__e32fe35963fd17cade5a2f645e7c19a1323c1492adf6feb26243a5e9e7662c3b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDedicatedIpPoolProps(pool_name=pool_name, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5f927ca48ddd041d4e0695fb549cebba5e598ce742e722993b8ac602a78e077)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e02354e13f66131596c1a805b06ff7ca3ec7781da17cd50e4b390e39c98739d5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__53fc1c6b841d49e922f0817b93835d298f3bd55bf2a5adb72a1506f0ccbb68d8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__807076abd404d7d7768ee17a024598e71fb38314a6a67e317ac3b921e7086bbb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpointemail.CfnDedicatedIpPool.TagsProperty",
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
                import aws_cdk.aws_pinpointemail as pinpointemail
                
                tags_property = pinpointemail.CfnDedicatedIpPool.TagsProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__646a4b9dec493a1b752cdc9a65aba8edf0ec4d212808534ed05ca66dbd998b38)
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
    jsii_type="@aws-cdk/aws-pinpointemail.CfnDedicatedIpPoolProps",
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
            import aws_cdk.aws_pinpointemail as pinpointemail
            
            cfn_dedicated_ip_pool_props = pinpointemail.CfnDedicatedIpPoolProps(
                pool_name="poolName",
                tags=[pinpointemail.CfnDedicatedIpPool.TagsProperty(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4dfb46bc91e3f91bf1e5da485d476b9333010547b1c7f60fe22125b5574a0aed)
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


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnIdentity(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-pinpointemail.CfnIdentity",
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
        import aws_cdk.aws_pinpointemail as pinpointemail
        
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
        scope: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        dkim_signing_enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
        feedback_forwarding_enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
        mail_from_attributes: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnIdentity.MailFromAttributesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
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
            type_hints = typing.get_type_hints(_typecheckingstub__aa19569180e64189d81b1d170f6cf2af518fbb81a2ed487104a2d4be92d95cc0)
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
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48d1fa694e0dee5ba07a7128add808292a82199b34d882e3c3978fa00b9bdca4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6826ea0d782b898b913863407b77931bd900e3ac75ea6756e71f25348ccdf6b2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bf3f7d60206cfa031c17c0243c2e281c7854118bea3beaae7b59f00f7d2b662e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="dkimSigningEnabled")
    def dkim_signing_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
        '''For domain identities, this attribute is used to enable or disable DomainKeys Identified Mail (DKIM) signing for the domain.

        If the value is ``true`` , then the messages that you send from the domain are signed using both the DKIM keys for your domain, as well as the keys for the ``amazonses.com`` domain. If the value is ``false`` , then the messages that you send are only signed using the DKIM keys for the ``amazonses.com`` domain.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html#cfn-pinpointemail-identity-dkimsigningenabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], jsii.get(self, "dkimSigningEnabled"))

    @dkim_signing_enabled.setter
    def dkim_signing_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c0c4f412675dd390107c4ae25e61c60ef1f7112476cc5b2ddf3dbdc7bad0013)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dkimSigningEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="feedbackForwardingEnabled")
    def feedback_forwarding_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
        '''Used to enable or disable feedback forwarding for an identity.

        This setting determines what happens when an identity is used to send an email that results in a bounce or complaint event.

        When you enable feedback forwarding, Amazon Pinpoint sends you email notifications when bounce or complaint events occur. Amazon Pinpoint sends this notification to the address that you specified in the Return-Path header of the original email.

        When you disable feedback forwarding, Amazon Pinpoint sends notifications through other mechanisms, such as by notifying an Amazon SNS topic. You're required to have a method of tracking bounces and complaints. If you haven't set up another mechanism for receiving bounce or complaint notifications, Amazon Pinpoint sends an email notification when these events occur (even if this setting is disabled).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html#cfn-pinpointemail-identity-feedbackforwardingenabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], jsii.get(self, "feedbackForwardingEnabled"))

    @feedback_forwarding_enabled.setter
    def feedback_forwarding_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f34b9b6288d4ae01040d8ee523f4b383d8ed5db3b6d5da51d90c3f0544312efd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "feedbackForwardingEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="mailFromAttributes")
    def mail_from_attributes(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnIdentity.MailFromAttributesProperty"]]:
        '''Used to enable or disable the custom Mail-From domain configuration for an email identity.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html#cfn-pinpointemail-identity-mailfromattributes
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnIdentity.MailFromAttributesProperty"]], jsii.get(self, "mailFromAttributes"))

    @mail_from_attributes.setter
    def mail_from_attributes(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnIdentity.MailFromAttributesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f73302b12df809dd942e0cf011b8fde32dd403a220057a6e5495ff49db368cc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__eb245cb47ec69ed4e12b8d543443a158defcbec013f43961e8c9be1ae33688c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpointemail.CfnIdentity.MailFromAttributesProperty",
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
                import aws_cdk.aws_pinpointemail as pinpointemail
                
                mail_from_attributes_property = pinpointemail.CfnIdentity.MailFromAttributesProperty(
                    behavior_on_mx_failure="behaviorOnMxFailure",
                    mail_from_domain="mailFromDomain"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__86140a65cefc0d75254fa2ffa01538e1e5de7ec7ca62783a42daa5ad769bd910)
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
        jsii_type="@aws-cdk/aws-pinpointemail.CfnIdentity.TagsProperty",
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
                import aws_cdk.aws_pinpointemail as pinpointemail
                
                tags_property = pinpointemail.CfnIdentity.TagsProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f37660850e578a36f3b42f05a85946b59d75a0e8f95f973cdc0ac0dc40a298d8)
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
    jsii_type="@aws-cdk/aws-pinpointemail.CfnIdentityProps",
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
        dkim_signing_enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
        feedback_forwarding_enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
        mail_from_attributes: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnIdentity.MailFromAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
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
            import aws_cdk.aws_pinpointemail as pinpointemail
            
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
            type_hints = typing.get_type_hints(_typecheckingstub__6b7cd2bb8f6c9d507b3332d438882f67ab7acfc7ec915315f7abfb73e15f5deb)
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
    ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
        '''For domain identities, this attribute is used to enable or disable DomainKeys Identified Mail (DKIM) signing for the domain.

        If the value is ``true`` , then the messages that you send from the domain are signed using both the DKIM keys for your domain, as well as the keys for the ``amazonses.com`` domain. If the value is ``false`` , then the messages that you send are only signed using the DKIM keys for the ``amazonses.com`` domain.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html#cfn-pinpointemail-identity-dkimsigningenabled
        '''
        result = self._values.get("dkim_signing_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

    @builtins.property
    def feedback_forwarding_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
        '''Used to enable or disable feedback forwarding for an identity.

        This setting determines what happens when an identity is used to send an email that results in a bounce or complaint event.

        When you enable feedback forwarding, Amazon Pinpoint sends you email notifications when bounce or complaint events occur. Amazon Pinpoint sends this notification to the address that you specified in the Return-Path header of the original email.

        When you disable feedback forwarding, Amazon Pinpoint sends notifications through other mechanisms, such as by notifying an Amazon SNS topic. You're required to have a method of tracking bounces and complaints. If you haven't set up another mechanism for receiving bounce or complaint notifications, Amazon Pinpoint sends an email notification when these events occur (even if this setting is disabled).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html#cfn-pinpointemail-identity-feedbackforwardingenabled
        '''
        result = self._values.get("feedback_forwarding_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

    @builtins.property
    def mail_from_attributes(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnIdentity.MailFromAttributesProperty]]:
        '''Used to enable or disable the custom Mail-From domain configuration for an email identity.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html#cfn-pinpointemail-identity-mailfromattributes
        '''
        result = self._values.get("mail_from_attributes")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnIdentity.MailFromAttributesProperty]], result)

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

def _typecheckingstub__79c94b7097d570913e6a201b16742195ba872eb77c6f30d31df80ff707a61cef(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    delivery_options: typing.Optional[typing.Union[typing.Union[CfnConfigurationSet.DeliveryOptionsProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable]] = None,
    reputation_options: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnConfigurationSet.ReputationOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sending_options: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnConfigurationSet.SendingOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnConfigurationSet.TagsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tracking_options: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnConfigurationSet.TrackingOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d878a70a9abcc05484d45875ba6fa820b448ef9cb6f6b7df2f49d4d8d8c8ac73(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08fa61ea72e62043ee69f8c5d86b0884426774d5d728e888470db8e09d11b47e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56d17b1c947a821bd0deae9a759b52b0aaf93bee51979a3738142934a3c01baa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__751d315454bfa515de0a354ee7d91822b64a2ac84ba746742c1761e3910c760e(
    value: typing.Optional[typing.Union[CfnConfigurationSet.DeliveryOptionsProperty, _aws_cdk_core_f4b25747.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56ea513e848ece3789871bac01fac32f40c9ed2cc13a7f43ac805e644df92e95(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnConfigurationSet.ReputationOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6016e4ab249cda5144333d432f68f798dd6d5b82c98bd958033e7b3fdd2df19d(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnConfigurationSet.SendingOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a0e0e4cde3fb60dcb4f3b8af87f5ca2e15f51961b8659a7e680bdd45f998c45(
    value: typing.Optional[typing.List[CfnConfigurationSet.TagsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1a5dceca245e615b9ca3b6029b58980958957028f9bd1f432c701a56b076821(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnConfigurationSet.TrackingOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5bbfa12155f563a1c861522d0860321d3965f2750ac6961bfa363db9cd366a6(
    *,
    sending_pool_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78c7de2f370c6c9cf08de8cfd651c4370d397e04f1542acdbcaf40bd37cfd514(
    *,
    reputation_metrics_enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1afd5e8d830ec288b9ea9a1947ba73df2d53dd74f6f7aa8cceed6c989e49f2c(
    *,
    sending_enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c777e74aa4c547e7e771f0fc07b792618fc2a7f1eb670dea1eca5ff8e212605d(
    *,
    key: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f3be60d81c1e75c6b4e7018c614f0e1df3d7fc504d2d81db89a10322813b9db(
    *,
    custom_redirect_domain: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__571aa6db5d6903e39a0d354c8576b598395d23afbca33c0a7c933c062d070f13(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    configuration_set_name: builtins.str,
    event_destination_name: builtins.str,
    event_destination: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnConfigurationSetEventDestination.EventDestinationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6289bbe4d1ae11ec7870b9fcbb8873737f41a617487978eaf82afdd4bb6526c8(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2a1ae85bdb74c360def78020fd398d34b95d327146b3b36a24a812129e211a6(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bd15f0da6a34b43477fdba06f28323694db2d456e51332712efce08305e8d76(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__844bf86b5b3511c44c4b387fefa320977da6cbcbaecfedaaa06a390b9d5c4d96(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fe1320e93d4c5127a8931b810a88f7adf31e084cdcdb23c5112877c496bd4cb(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnConfigurationSetEventDestination.EventDestinationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6f5ee8448219389bf17a885586e478865bd6d58810dd01e79187f3039082a40(
    *,
    dimension_configurations: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnConfigurationSetEventDestination.DimensionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60e213f08de6688a76df4a372af3edd2a80383b65a7d41d7b3d7feaa99cc4e57(
    *,
    default_dimension_value: builtins.str,
    dimension_name: builtins.str,
    dimension_value_source: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4eeca540a4946d9d259112b13a21f31ff12160d9a5ecb81ffe343432508f960b(
    *,
    matching_event_types: typing.Sequence[builtins.str],
    cloud_watch_destination: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnConfigurationSetEventDestination.CloudWatchDestinationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    kinesis_firehose_destination: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    pinpoint_destination: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnConfigurationSetEventDestination.PinpointDestinationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sns_destination: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnConfigurationSetEventDestination.SnsDestinationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__253654f1867164e627b33da791dc07d7a058bf6598fa0dc6a5f6bb10621fdb96(
    *,
    delivery_stream_arn: builtins.str,
    iam_role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f349cc8501e51253fffafb0382e541bb6f653a88b1ecab4390488c1c22c586c2(
    *,
    application_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e70b66abb7dba1a29243f60c80ef9b9d0935966ba049cbb973dd16b64398d16c(
    *,
    topic_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e7de4d76acaf8d229ed0fb8017828fdcb02d0c8b4167164aa473c83581b9e1d(
    *,
    configuration_set_name: builtins.str,
    event_destination_name: builtins.str,
    event_destination: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnConfigurationSetEventDestination.EventDestinationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc270122928b23b61ee26cc1d5480a105dd444ef06cf54765bf0b7fc012c5dbc(
    *,
    name: builtins.str,
    delivery_options: typing.Optional[typing.Union[typing.Union[CfnConfigurationSet.DeliveryOptionsProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable]] = None,
    reputation_options: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnConfigurationSet.ReputationOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sending_options: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnConfigurationSet.SendingOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnConfigurationSet.TagsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tracking_options: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnConfigurationSet.TrackingOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e32fe35963fd17cade5a2f645e7c19a1323c1492adf6feb26243a5e9e7662c3b(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    pool_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnDedicatedIpPool.TagsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5f927ca48ddd041d4e0695fb549cebba5e598ce742e722993b8ac602a78e077(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e02354e13f66131596c1a805b06ff7ca3ec7781da17cd50e4b390e39c98739d5(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53fc1c6b841d49e922f0817b93835d298f3bd55bf2a5adb72a1506f0ccbb68d8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__807076abd404d7d7768ee17a024598e71fb38314a6a67e317ac3b921e7086bbb(
    value: typing.Optional[typing.List[CfnDedicatedIpPool.TagsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__646a4b9dec493a1b752cdc9a65aba8edf0ec4d212808534ed05ca66dbd998b38(
    *,
    key: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4dfb46bc91e3f91bf1e5da485d476b9333010547b1c7f60fe22125b5574a0aed(
    *,
    pool_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnDedicatedIpPool.TagsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa19569180e64189d81b1d170f6cf2af518fbb81a2ed487104a2d4be92d95cc0(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    dkim_signing_enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    feedback_forwarding_enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    mail_from_attributes: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnIdentity.MailFromAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnIdentity.TagsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48d1fa694e0dee5ba07a7128add808292a82199b34d882e3c3978fa00b9bdca4(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6826ea0d782b898b913863407b77931bd900e3ac75ea6756e71f25348ccdf6b2(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf3f7d60206cfa031c17c0243c2e281c7854118bea3beaae7b59f00f7d2b662e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c0c4f412675dd390107c4ae25e61c60ef1f7112476cc5b2ddf3dbdc7bad0013(
    value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f34b9b6288d4ae01040d8ee523f4b383d8ed5db3b6d5da51d90c3f0544312efd(
    value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f73302b12df809dd942e0cf011b8fde32dd403a220057a6e5495ff49db368cc(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnIdentity.MailFromAttributesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb245cb47ec69ed4e12b8d543443a158defcbec013f43961e8c9be1ae33688c4(
    value: typing.Optional[typing.List[CfnIdentity.TagsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86140a65cefc0d75254fa2ffa01538e1e5de7ec7ca62783a42daa5ad769bd910(
    *,
    behavior_on_mx_failure: typing.Optional[builtins.str] = None,
    mail_from_domain: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f37660850e578a36f3b42f05a85946b59d75a0e8f95f973cdc0ac0dc40a298d8(
    *,
    key: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b7cd2bb8f6c9d507b3332d438882f67ab7acfc7ec915315f7abfb73e15f5deb(
    *,
    name: builtins.str,
    dkim_signing_enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    feedback_forwarding_enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    mail_from_attributes: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnIdentity.MailFromAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnIdentity.TagsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

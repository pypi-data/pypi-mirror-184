'''
# Alexa Skills Kit Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.alexa_ask as alexa_ask
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for ASK construct libraries](https://constructs.dev/search?q=ask)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation Alexa::ASK resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Alexa_ASK.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for Alexa::ASK](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Alexa_ASK.html).

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
class CfnSkill(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/alexa-ask.CfnSkill",
):
    '''A CloudFormation ``Alexa::ASK::Skill``.

    The ``Alexa::ASK::Skill`` resource creates an Alexa skill that enables customers to access new abilities. For more information about developing a skill, see the  .

    :cloudformationResource: Alexa::ASK::Skill
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ask-skill.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.alexa_ask as alexa_ask
        
        # manifest: Any
        
        cfn_skill = alexa_ask.CfnSkill(self, "MyCfnSkill",
            authentication_configuration=alexa_ask.CfnSkill.AuthenticationConfigurationProperty(
                client_id="clientId",
                client_secret="clientSecret",
                refresh_token="refreshToken"
            ),
            skill_package=alexa_ask.CfnSkill.SkillPackageProperty(
                s3_bucket="s3Bucket",
                s3_key="s3Key",
        
                # the properties below are optional
                overrides=alexa_ask.CfnSkill.OverridesProperty(
                    manifest=manifest
                ),
                s3_bucket_role="s3BucketRole",
                s3_object_version="s3ObjectVersion"
            ),
            vendor_id="vendorId"
        )
    '''

    def __init__(
        self,
        scope: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        authentication_configuration: typing.Union[typing.Union["CfnSkill.AuthenticationConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable],
        skill_package: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnSkill.SkillPackageProperty", typing.Dict[builtins.str, typing.Any]]],
        vendor_id: builtins.str,
    ) -> None:
        '''Create a new ``Alexa::ASK::Skill``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param authentication_configuration: Login with Amazon (LWA) configuration used to authenticate with the Alexa service. Only Login with Amazon clients created through the are supported. The client ID, client secret, and refresh token are required.
        :param skill_package: Configuration for the skill package that contains the components of the Alexa skill. Skill packages are retrieved from an Amazon S3 bucket and key and used to create and update the skill. For more information about the skill package format, see the .
        :param vendor_id: The vendor ID associated with the Amazon developer account that will host the skill. Details for retrieving the vendor ID are in . The provided LWA credentials must be linked to the developer account associated with this vendor ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc70d003b578b06f671c025c59316aabd73e48581733e392bb12ba13ca0b30a4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSkillProps(
            authentication_configuration=authentication_configuration,
            skill_package=skill_package,
            vendor_id=vendor_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d820f4d85d09e55f25d4f1e4e3c34dc6003b1f24509a95bcbbda19756b04061e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0855847b057c8c4899bee0b9dc756adee5932fb2adaba593cf4bae1090c139a9)
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
    @jsii.member(jsii_name="authenticationConfiguration")
    def authentication_configuration(
        self,
    ) -> typing.Union["CfnSkill.AuthenticationConfigurationProperty", _aws_cdk_core_f4b25747.IResolvable]:
        '''Login with Amazon (LWA) configuration used to authenticate with the Alexa service.

        Only Login with Amazon clients created through the  are supported. The client ID, client secret, and refresh token are required.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ask-skill.html#cfn-ask-skill-authenticationconfiguration
        '''
        return typing.cast(typing.Union["CfnSkill.AuthenticationConfigurationProperty", _aws_cdk_core_f4b25747.IResolvable], jsii.get(self, "authenticationConfiguration"))

    @authentication_configuration.setter
    def authentication_configuration(
        self,
        value: typing.Union["CfnSkill.AuthenticationConfigurationProperty", _aws_cdk_core_f4b25747.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84815d24bd7babe05a1474fe7eba4a8969fc0ab293a77a7f14a5ddd6e4856027)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authenticationConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="skillPackage")
    def skill_package(
        self,
    ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnSkill.SkillPackageProperty"]:
        '''Configuration for the skill package that contains the components of the Alexa skill.

        Skill packages are retrieved from an Amazon S3 bucket and key and used to create and update the skill. For more information about the skill package format, see the  .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ask-skill.html#cfn-ask-skill-skillpackage
        '''
        return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnSkill.SkillPackageProperty"], jsii.get(self, "skillPackage"))

    @skill_package.setter
    def skill_package(
        self,
        value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnSkill.SkillPackageProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af65bc3f913186b925dbc61c1c19bb42d4c16456cde26771d8d9c12abd7ac0b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skillPackage", value)

    @builtins.property
    @jsii.member(jsii_name="vendorId")
    def vendor_id(self) -> builtins.str:
        '''The vendor ID associated with the Amazon developer account that will host the skill.

        Details for retrieving the vendor ID are in  . The provided LWA credentials must be linked to the developer account associated with this vendor ID.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ask-skill.html#cfn-ask-skill-vendorid
        '''
        return typing.cast(builtins.str, jsii.get(self, "vendorId"))

    @vendor_id.setter
    def vendor_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f34b1235abf3f4b8d7a0dfa370c8ba2bcbc09302f839c1dbc899247769194d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vendorId", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/alexa-ask.CfnSkill.AuthenticationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "client_id": "clientId",
            "client_secret": "clientSecret",
            "refresh_token": "refreshToken",
        },
    )
    class AuthenticationConfigurationProperty:
        def __init__(
            self,
            *,
            client_id: builtins.str,
            client_secret: builtins.str,
            refresh_token: builtins.str,
        ) -> None:
            '''The ``AuthenticationConfiguration`` property type specifies the Login with Amazon (LWA) configuration used to authenticate with the Alexa service.

            Only Login with Amazon security profiles created through the  are supported for authentication. A client ID, client secret, and refresh token are required. You can generate a client ID and client secret by creating a new  on the Amazon Developer Portal or you can retrieve them from an existing profile. You can then retrieve the refresh token using the Alexa Skills Kit CLI. For instructions, see  in the  .

            ``AuthenticationConfiguration`` is a property of the ``Alexa::ASK::Skill`` resource.

            :param client_id: Client ID from Login with Amazon (LWA).
            :param client_secret: Client secret from Login with Amazon (LWA).
            :param refresh_token: Refresh token from Login with Amazon (LWA). This token is secret.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-authenticationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.alexa_ask as alexa_ask
                
                authentication_configuration_property = alexa_ask.CfnSkill.AuthenticationConfigurationProperty(
                    client_id="clientId",
                    client_secret="clientSecret",
                    refresh_token="refreshToken"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3ee2a2e52224de1498228029dddb21919e7fabd93d4d25337a447432af05cb29)
                check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
                check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
                check_type(argname="argument refresh_token", value=refresh_token, expected_type=type_hints["refresh_token"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "client_id": client_id,
                "client_secret": client_secret,
                "refresh_token": refresh_token,
            }

        @builtins.property
        def client_id(self) -> builtins.str:
            '''Client ID from Login with Amazon (LWA).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-authenticationconfiguration.html#cfn-ask-skill-authenticationconfiguration-clientid
            '''
            result = self._values.get("client_id")
            assert result is not None, "Required property 'client_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def client_secret(self) -> builtins.str:
            '''Client secret from Login with Amazon (LWA).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-authenticationconfiguration.html#cfn-ask-skill-authenticationconfiguration-clientsecret
            '''
            result = self._values.get("client_secret")
            assert result is not None, "Required property 'client_secret' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def refresh_token(self) -> builtins.str:
            '''Refresh token from Login with Amazon (LWA).

            This token is secret.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-authenticationconfiguration.html#cfn-ask-skill-authenticationconfiguration-refreshtoken
            '''
            result = self._values.get("refresh_token")
            assert result is not None, "Required property 'refresh_token' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthenticationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/alexa-ask.CfnSkill.OverridesProperty",
        jsii_struct_bases=[],
        name_mapping={"manifest": "manifest"},
    )
    class OverridesProperty:
        def __init__(self, *, manifest: typing.Any = None) -> None:
            '''The ``Overrides`` property type provides overrides to the skill package to apply when creating or updating the skill.

            Values provided here do not modify the contents of the original skill package. Currently, only overriding values inside of the skill manifest component of the package is supported.

            ``Overrides`` is a property of the ``Alexa::ASK::Skill SkillPackage`` property type.

            :param manifest: Overrides to apply to the skill manifest inside of the skill package. The skill manifest contains metadata about the skill. For more information, see .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-overrides.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.alexa_ask as alexa_ask
                
                # manifest: Any
                
                overrides_property = alexa_ask.CfnSkill.OverridesProperty(
                    manifest=manifest
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5820fd4897bcbf7bc0bbf525431880be10d10f85694a2843db400d89080a9170)
                check_type(argname="argument manifest", value=manifest, expected_type=type_hints["manifest"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if manifest is not None:
                self._values["manifest"] = manifest

        @builtins.property
        def manifest(self) -> typing.Any:
            '''Overrides to apply to the skill manifest inside of the skill package.

            The skill manifest contains metadata about the skill. For more information, see  .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-overrides.html#cfn-ask-skill-overrides-manifest
            '''
            result = self._values.get("manifest")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OverridesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/alexa-ask.CfnSkill.SkillPackageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "s3_bucket": "s3Bucket",
            "s3_key": "s3Key",
            "overrides": "overrides",
            "s3_bucket_role": "s3BucketRole",
            "s3_object_version": "s3ObjectVersion",
        },
    )
    class SkillPackageProperty:
        def __init__(
            self,
            *,
            s3_bucket: builtins.str,
            s3_key: builtins.str,
            overrides: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnSkill.OverridesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3_bucket_role: typing.Optional[builtins.str] = None,
            s3_object_version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``SkillPackage`` property type contains configuration details for the skill package that contains the components of the Alexa skill.

            Skill packages are retrieved from an Amazon S3 bucket and key and used to create and update the skill. More details about the skill package format are located in the  .

            ``SkillPackage`` is a property of the ``Alexa::ASK::Skill`` resource.

            :param s3_bucket: The name of the Amazon S3 bucket where the .zip file that contains the skill package is stored.
            :param s3_key: The location and name of the skill package .zip file.
            :param overrides: Overrides to the skill package to apply when creating or updating the skill. Values provided here do not modify the contents of the original skill package. Currently, only overriding values inside of the skill manifest component of the package is supported.
            :param s3_bucket_role: ARN of the IAM role that grants the Alexa service ( ``alexa-appkit.amazon.com`` ) permission to access the bucket and retrieve the skill package. This property is optional. If you do not provide it, the bucket must be publicly accessible or configured with a policy that allows this access. Otherwise, AWS CloudFormation cannot create the skill.
            :param s3_object_version: If you have S3 versioning enabled, the version ID of the skill package.zip file.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-skillpackage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.alexa_ask as alexa_ask
                
                # manifest: Any
                
                skill_package_property = alexa_ask.CfnSkill.SkillPackageProperty(
                    s3_bucket="s3Bucket",
                    s3_key="s3Key",
                
                    # the properties below are optional
                    overrides=alexa_ask.CfnSkill.OverridesProperty(
                        manifest=manifest
                    ),
                    s3_bucket_role="s3BucketRole",
                    s3_object_version="s3ObjectVersion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__41398c297b07e20bbb4984f38f37866e56e1d17733375858a8bcd8c8cd06a1f8)
                check_type(argname="argument s3_bucket", value=s3_bucket, expected_type=type_hints["s3_bucket"])
                check_type(argname="argument s3_key", value=s3_key, expected_type=type_hints["s3_key"])
                check_type(argname="argument overrides", value=overrides, expected_type=type_hints["overrides"])
                check_type(argname="argument s3_bucket_role", value=s3_bucket_role, expected_type=type_hints["s3_bucket_role"])
                check_type(argname="argument s3_object_version", value=s3_object_version, expected_type=type_hints["s3_object_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "s3_bucket": s3_bucket,
                "s3_key": s3_key,
            }
            if overrides is not None:
                self._values["overrides"] = overrides
            if s3_bucket_role is not None:
                self._values["s3_bucket_role"] = s3_bucket_role
            if s3_object_version is not None:
                self._values["s3_object_version"] = s3_object_version

        @builtins.property
        def s3_bucket(self) -> builtins.str:
            '''The name of the Amazon S3 bucket where the .zip file that contains the skill package is stored.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-skillpackage.html#cfn-ask-skill-skillpackage-s3bucket
            '''
            result = self._values.get("s3_bucket")
            assert result is not None, "Required property 's3_bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_key(self) -> builtins.str:
            '''The location and name of the skill package .zip file.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-skillpackage.html#cfn-ask-skill-skillpackage-s3key
            '''
            result = self._values.get("s3_key")
            assert result is not None, "Required property 's3_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def overrides(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnSkill.OverridesProperty"]]:
            '''Overrides to the skill package to apply when creating or updating the skill.

            Values provided here do not modify the contents of the original skill package. Currently, only overriding values inside of the skill manifest component of the package is supported.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-skillpackage.html#cfn-ask-skill-skillpackage-overrides
            '''
            result = self._values.get("overrides")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnSkill.OverridesProperty"]], result)

        @builtins.property
        def s3_bucket_role(self) -> typing.Optional[builtins.str]:
            '''ARN of the IAM role that grants the Alexa service ( ``alexa-appkit.amazon.com`` ) permission to access the bucket and retrieve the skill package. This property is optional. If you do not provide it, the bucket must be publicly accessible or configured with a policy that allows this access. Otherwise, AWS CloudFormation cannot create the skill.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-skillpackage.html#cfn-ask-skill-skillpackage-s3bucketrole
            '''
            result = self._values.get("s3_bucket_role")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_object_version(self) -> typing.Optional[builtins.str]:
            '''If you have S3 versioning enabled, the version ID of the skill package.zip file.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-skillpackage.html#cfn-ask-skill-skillpackage-s3objectversion
            '''
            result = self._values.get("s3_object_version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SkillPackageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/alexa-ask.CfnSkillProps",
    jsii_struct_bases=[],
    name_mapping={
        "authentication_configuration": "authenticationConfiguration",
        "skill_package": "skillPackage",
        "vendor_id": "vendorId",
    },
)
class CfnSkillProps:
    def __init__(
        self,
        *,
        authentication_configuration: typing.Union[typing.Union[CfnSkill.AuthenticationConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable],
        skill_package: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnSkill.SkillPackageProperty, typing.Dict[builtins.str, typing.Any]]],
        vendor_id: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnSkill``.

        :param authentication_configuration: Login with Amazon (LWA) configuration used to authenticate with the Alexa service. Only Login with Amazon clients created through the are supported. The client ID, client secret, and refresh token are required.
        :param skill_package: Configuration for the skill package that contains the components of the Alexa skill. Skill packages are retrieved from an Amazon S3 bucket and key and used to create and update the skill. For more information about the skill package format, see the .
        :param vendor_id: The vendor ID associated with the Amazon developer account that will host the skill. Details for retrieving the vendor ID are in . The provided LWA credentials must be linked to the developer account associated with this vendor ID.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ask-skill.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.alexa_ask as alexa_ask
            
            # manifest: Any
            
            cfn_skill_props = alexa_ask.CfnSkillProps(
                authentication_configuration=alexa_ask.CfnSkill.AuthenticationConfigurationProperty(
                    client_id="clientId",
                    client_secret="clientSecret",
                    refresh_token="refreshToken"
                ),
                skill_package=alexa_ask.CfnSkill.SkillPackageProperty(
                    s3_bucket="s3Bucket",
                    s3_key="s3Key",
            
                    # the properties below are optional
                    overrides=alexa_ask.CfnSkill.OverridesProperty(
                        manifest=manifest
                    ),
                    s3_bucket_role="s3BucketRole",
                    s3_object_version="s3ObjectVersion"
                ),
                vendor_id="vendorId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b072dbec48921d9742a8e72a7db1988271518d0992f8911add44a63e8d643549)
            check_type(argname="argument authentication_configuration", value=authentication_configuration, expected_type=type_hints["authentication_configuration"])
            check_type(argname="argument skill_package", value=skill_package, expected_type=type_hints["skill_package"])
            check_type(argname="argument vendor_id", value=vendor_id, expected_type=type_hints["vendor_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "authentication_configuration": authentication_configuration,
            "skill_package": skill_package,
            "vendor_id": vendor_id,
        }

    @builtins.property
    def authentication_configuration(
        self,
    ) -> typing.Union[CfnSkill.AuthenticationConfigurationProperty, _aws_cdk_core_f4b25747.IResolvable]:
        '''Login with Amazon (LWA) configuration used to authenticate with the Alexa service.

        Only Login with Amazon clients created through the  are supported. The client ID, client secret, and refresh token are required.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ask-skill.html#cfn-ask-skill-authenticationconfiguration
        '''
        result = self._values.get("authentication_configuration")
        assert result is not None, "Required property 'authentication_configuration' is missing"
        return typing.cast(typing.Union[CfnSkill.AuthenticationConfigurationProperty, _aws_cdk_core_f4b25747.IResolvable], result)

    @builtins.property
    def skill_package(
        self,
    ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnSkill.SkillPackageProperty]:
        '''Configuration for the skill package that contains the components of the Alexa skill.

        Skill packages are retrieved from an Amazon S3 bucket and key and used to create and update the skill. For more information about the skill package format, see the  .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ask-skill.html#cfn-ask-skill-skillpackage
        '''
        result = self._values.get("skill_package")
        assert result is not None, "Required property 'skill_package' is missing"
        return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnSkill.SkillPackageProperty], result)

    @builtins.property
    def vendor_id(self) -> builtins.str:
        '''The vendor ID associated with the Amazon developer account that will host the skill.

        Details for retrieving the vendor ID are in  . The provided LWA credentials must be linked to the developer account associated with this vendor ID.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ask-skill.html#cfn-ask-skill-vendorid
        '''
        result = self._values.get("vendor_id")
        assert result is not None, "Required property 'vendor_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSkillProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnSkill",
    "CfnSkillProps",
]

publication.publish()

def _typecheckingstub__bc70d003b578b06f671c025c59316aabd73e48581733e392bb12ba13ca0b30a4(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    authentication_configuration: typing.Union[typing.Union[CfnSkill.AuthenticationConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable],
    skill_package: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnSkill.SkillPackageProperty, typing.Dict[builtins.str, typing.Any]]],
    vendor_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d820f4d85d09e55f25d4f1e4e3c34dc6003b1f24509a95bcbbda19756b04061e(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0855847b057c8c4899bee0b9dc756adee5932fb2adaba593cf4bae1090c139a9(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84815d24bd7babe05a1474fe7eba4a8969fc0ab293a77a7f14a5ddd6e4856027(
    value: typing.Union[CfnSkill.AuthenticationConfigurationProperty, _aws_cdk_core_f4b25747.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af65bc3f913186b925dbc61c1c19bb42d4c16456cde26771d8d9c12abd7ac0b3(
    value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnSkill.SkillPackageProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f34b1235abf3f4b8d7a0dfa370c8ba2bcbc09302f839c1dbc899247769194d0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ee2a2e52224de1498228029dddb21919e7fabd93d4d25337a447432af05cb29(
    *,
    client_id: builtins.str,
    client_secret: builtins.str,
    refresh_token: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5820fd4897bcbf7bc0bbf525431880be10d10f85694a2843db400d89080a9170(
    *,
    manifest: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41398c297b07e20bbb4984f38f37866e56e1d17733375858a8bcd8c8cd06a1f8(
    *,
    s3_bucket: builtins.str,
    s3_key: builtins.str,
    overrides: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnSkill.OverridesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_bucket_role: typing.Optional[builtins.str] = None,
    s3_object_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b072dbec48921d9742a8e72a7db1988271518d0992f8911add44a63e8d643549(
    *,
    authentication_configuration: typing.Union[typing.Union[CfnSkill.AuthenticationConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable],
    skill_package: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnSkill.SkillPackageProperty, typing.Dict[builtins.str, typing.Any]]],
    vendor_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

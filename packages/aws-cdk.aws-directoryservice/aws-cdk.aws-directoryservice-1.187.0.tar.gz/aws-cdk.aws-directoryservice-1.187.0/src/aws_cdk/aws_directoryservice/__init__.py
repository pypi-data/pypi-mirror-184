'''
# AWS Directory Service Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_directoryservice as directoryservice
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for DirectoryService construct libraries](https://constructs.dev/search?q=directoryservice)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::DirectoryService resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DirectoryService.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::DirectoryService](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DirectoryService.html).

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
class CfnMicrosoftAD(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-directoryservice.CfnMicrosoftAD",
):
    '''A CloudFormation ``AWS::DirectoryService::MicrosoftAD``.

    The ``AWS::DirectoryService::MicrosoftAD`` resource specifies a Microsoft Active Directory in AWS so that your directory users and groups can access the AWS Management Console and AWS applications using their existing credentials. For more information, see `AWS Managed Microsoft AD <https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html>`_ in the *AWS Directory Service Admin Guide* .

    :cloudformationResource: AWS::DirectoryService::MicrosoftAD
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_directoryservice as directoryservice
        
        cfn_microsoft_aD = directoryservice.CfnMicrosoftAD(self, "MyCfnMicrosoftAD",
            name="name",
            password="password",
            vpc_settings=directoryservice.CfnMicrosoftAD.VpcSettingsProperty(
                subnet_ids=["subnetIds"],
                vpc_id="vpcId"
            ),
        
            # the properties below are optional
            create_alias=False,
            edition="edition",
            enable_sso=False,
            short_name="shortName"
        )
    '''

    def __init__(
        self,
        scope: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        password: builtins.str,
        vpc_settings: typing.Union[typing.Union["CfnMicrosoftAD.VpcSettingsProperty", typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable],
        create_alias: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
        edition: typing.Optional[builtins.str] = None,
        enable_sso: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
        short_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::DirectoryService::MicrosoftAD``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: The fully qualified domain name for the AWS Managed Microsoft AD directory, such as ``corp.example.com`` . This name will resolve inside your VPC only. It does not need to be publicly resolvable.
        :param password: The password for the default administrative user named ``Admin`` . If you need to change the password for the administrator account, see the `ResetUserPassword <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ResetUserPassword.html>`_ API call in the *AWS Directory Service API Reference* .
        :param vpc_settings: Specifies the VPC settings of the Microsoft AD directory server in AWS .
        :param create_alias: Specifies an alias for a directory and assigns the alias to the directory. The alias is used to construct the access URL for the directory, such as ``http://<alias>.awsapps.com`` . By default, AWS CloudFormation does not create an alias. .. epigraph:: After an alias has been created, it cannot be deleted or reused, so this operation should only be used when absolutely necessary.
        :param edition: AWS Managed Microsoft AD is available in two editions: ``Standard`` and ``Enterprise`` . ``Enterprise`` is the default.
        :param enable_sso: Whether to enable single sign-on for a Microsoft Active Directory in AWS . Single sign-on allows users in your directory to access certain AWS services from a computer joined to the directory without having to enter their credentials separately. If you don't specify a value, AWS CloudFormation disables single sign-on by default.
        :param short_name: The NetBIOS name for your domain, such as ``CORP`` . If you don't specify a NetBIOS name, it will default to the first part of your directory DNS. For example, ``CORP`` for the directory DNS ``corp.example.com`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3941813ded2bd7b528b2c263c13d48424aa047e76e91484cff219d8f757b95b8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMicrosoftADProps(
            name=name,
            password=password,
            vpc_settings=vpc_settings,
            create_alias=create_alias,
            edition=edition,
            enable_sso=enable_sso,
            short_name=short_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68b568d3166dec9ec4b675deb257676797fea4865e55483fe0a01a13e37a14cb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3335583b72747fa3aaf1f923d5c7b4939d465229e0fa7676d852f34c1bf42b1a)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAlias")
    def attr_alias(self) -> builtins.str:
        '''The alias for a directory.

        For example: ``d-12373a053a`` or ``alias4-mydirectory-12345abcgmzsk`` (if you have the ``CreateAlias`` property set to true).

        :cloudformationAttribute: Alias
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAlias"))

    @builtins.property
    @jsii.member(jsii_name="attrDnsIpAddresses")
    def attr_dns_ip_addresses(self) -> typing.List[builtins.str]:
        '''The IP addresses of the DNS servers for the directory, such as ``[ "192.0.2.1", "192.0.2.2" ]`` .

        :cloudformationAttribute: DnsIpAddresses
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrDnsIpAddresses"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The fully qualified domain name for the AWS Managed Microsoft AD directory, such as ``corp.example.com`` . This name will resolve inside your VPC only. It does not need to be publicly resolvable.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56bb46b36135a069321881902677f42f5ecbe9f42abab1211a2c9b4404f81b38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        '''The password for the default administrative user named ``Admin`` .

        If you need to change the password for the administrator account, see the `ResetUserPassword <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ResetUserPassword.html>`_ API call in the *AWS Directory Service API Reference* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-password
        '''
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58a78a8e58ff6b31762ce306e04d8411d273b3c14d28ff4dc90b91b6073a923b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="vpcSettings")
    def vpc_settings(
        self,
    ) -> typing.Union["CfnMicrosoftAD.VpcSettingsProperty", _aws_cdk_core_f4b25747.IResolvable]:
        '''Specifies the VPC settings of the Microsoft AD directory server in AWS .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-vpcsettings
        '''
        return typing.cast(typing.Union["CfnMicrosoftAD.VpcSettingsProperty", _aws_cdk_core_f4b25747.IResolvable], jsii.get(self, "vpcSettings"))

    @vpc_settings.setter
    def vpc_settings(
        self,
        value: typing.Union["CfnMicrosoftAD.VpcSettingsProperty", _aws_cdk_core_f4b25747.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ab9e5718b3f3ed3487ad6c247d2135e6ad1c29296fe26781c8beb627dd3621c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcSettings", value)

    @builtins.property
    @jsii.member(jsii_name="createAlias")
    def create_alias(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
        '''Specifies an alias for a directory and assigns the alias to the directory.

        The alias is used to construct the access URL for the directory, such as ``http://<alias>.awsapps.com`` . By default, AWS CloudFormation does not create an alias.
        .. epigraph::

           After an alias has been created, it cannot be deleted or reused, so this operation should only be used when absolutely necessary.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-createalias
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], jsii.get(self, "createAlias"))

    @create_alias.setter
    def create_alias(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cf396943ae4572d04ed1f357d3a41fcd8ed1569947b9ffb6233f7d90b6c6350)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createAlias", value)

    @builtins.property
    @jsii.member(jsii_name="edition")
    def edition(self) -> typing.Optional[builtins.str]:
        '''AWS Managed Microsoft AD is available in two editions: ``Standard`` and ``Enterprise`` .

        ``Enterprise`` is the default.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-edition
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "edition"))

    @edition.setter
    def edition(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1f803dd9738ed2c5e87aee5e22e689dca61a85d34c4e506e11368841b4adec2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "edition", value)

    @builtins.property
    @jsii.member(jsii_name="enableSso")
    def enable_sso(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
        '''Whether to enable single sign-on for a Microsoft Active Directory in AWS .

        Single sign-on allows users in your directory to access certain AWS services from a computer joined to the directory without having to enter their credentials separately. If you don't specify a value, AWS CloudFormation disables single sign-on by default.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-enablesso
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], jsii.get(self, "enableSso"))

    @enable_sso.setter
    def enable_sso(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0857b2bb71f6a8f0b48b7ca73a1cf677eca32186ef663edd9f745a184daae341)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableSso", value)

    @builtins.property
    @jsii.member(jsii_name="shortName")
    def short_name(self) -> typing.Optional[builtins.str]:
        '''The NetBIOS name for your domain, such as ``CORP`` .

        If you don't specify a NetBIOS name, it will default to the first part of your directory DNS. For example, ``CORP`` for the directory DNS ``corp.example.com`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-shortname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shortName"))

    @short_name.setter
    def short_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__734f1d0aef4307be9ad8bce48df347b8b354fe1030d7ad5dbe2022e0bdfbd61a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shortName", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-directoryservice.CfnMicrosoftAD.VpcSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"subnet_ids": "subnetIds", "vpc_id": "vpcId"},
    )
    class VpcSettingsProperty:
        def __init__(
            self,
            *,
            subnet_ids: typing.Sequence[builtins.str],
            vpc_id: builtins.str,
        ) -> None:
            '''Contains VPC information for the `CreateDirectory <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CreateDirectory.html>`_ or `CreateMicrosoftAD <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CreateMicrosoftAD.html>`_ operation.

            :param subnet_ids: The identifiers of the subnets for the directory servers. The two subnets must be in different Availability Zones. AWS Directory Service specifies a directory server and a DNS server in each of these subnets.
            :param vpc_id: The identifier of the VPC in which to create the directory.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-microsoftad-vpcsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_directoryservice as directoryservice
                
                vpc_settings_property = directoryservice.CfnMicrosoftAD.VpcSettingsProperty(
                    subnet_ids=["subnetIds"],
                    vpc_id="vpcId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__753d762ea6fe9e3b8643ccbf2c9cad670b078a481699b51dff5d6722006eb7d7)
                check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
                check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "subnet_ids": subnet_ids,
                "vpc_id": vpc_id,
            }

        @builtins.property
        def subnet_ids(self) -> typing.List[builtins.str]:
            '''The identifiers of the subnets for the directory servers.

            The two subnets must be in different Availability Zones. AWS Directory Service specifies a directory server and a DNS server in each of these subnets.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-microsoftad-vpcsettings.html#cfn-directoryservice-microsoftad-vpcsettings-subnetids
            '''
            result = self._values.get("subnet_ids")
            assert result is not None, "Required property 'subnet_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def vpc_id(self) -> builtins.str:
            '''The identifier of the VPC in which to create the directory.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-microsoftad-vpcsettings.html#cfn-directoryservice-microsoftad-vpcsettings-vpcid
            '''
            result = self._values.get("vpc_id")
            assert result is not None, "Required property 'vpc_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-directoryservice.CfnMicrosoftADProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "password": "password",
        "vpc_settings": "vpcSettings",
        "create_alias": "createAlias",
        "edition": "edition",
        "enable_sso": "enableSso",
        "short_name": "shortName",
    },
)
class CfnMicrosoftADProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        password: builtins.str,
        vpc_settings: typing.Union[typing.Union[CfnMicrosoftAD.VpcSettingsProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable],
        create_alias: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
        edition: typing.Optional[builtins.str] = None,
        enable_sso: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
        short_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnMicrosoftAD``.

        :param name: The fully qualified domain name for the AWS Managed Microsoft AD directory, such as ``corp.example.com`` . This name will resolve inside your VPC only. It does not need to be publicly resolvable.
        :param password: The password for the default administrative user named ``Admin`` . If you need to change the password for the administrator account, see the `ResetUserPassword <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ResetUserPassword.html>`_ API call in the *AWS Directory Service API Reference* .
        :param vpc_settings: Specifies the VPC settings of the Microsoft AD directory server in AWS .
        :param create_alias: Specifies an alias for a directory and assigns the alias to the directory. The alias is used to construct the access URL for the directory, such as ``http://<alias>.awsapps.com`` . By default, AWS CloudFormation does not create an alias. .. epigraph:: After an alias has been created, it cannot be deleted or reused, so this operation should only be used when absolutely necessary.
        :param edition: AWS Managed Microsoft AD is available in two editions: ``Standard`` and ``Enterprise`` . ``Enterprise`` is the default.
        :param enable_sso: Whether to enable single sign-on for a Microsoft Active Directory in AWS . Single sign-on allows users in your directory to access certain AWS services from a computer joined to the directory without having to enter their credentials separately. If you don't specify a value, AWS CloudFormation disables single sign-on by default.
        :param short_name: The NetBIOS name for your domain, such as ``CORP`` . If you don't specify a NetBIOS name, it will default to the first part of your directory DNS. For example, ``CORP`` for the directory DNS ``corp.example.com`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_directoryservice as directoryservice
            
            cfn_microsoft_aDProps = directoryservice.CfnMicrosoftADProps(
                name="name",
                password="password",
                vpc_settings=directoryservice.CfnMicrosoftAD.VpcSettingsProperty(
                    subnet_ids=["subnetIds"],
                    vpc_id="vpcId"
                ),
            
                # the properties below are optional
                create_alias=False,
                edition="edition",
                enable_sso=False,
                short_name="shortName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45e69c269ea8b6b7d89ff8a1804825055c30a6bff99807479b557ac1f5e622ee)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument vpc_settings", value=vpc_settings, expected_type=type_hints["vpc_settings"])
            check_type(argname="argument create_alias", value=create_alias, expected_type=type_hints["create_alias"])
            check_type(argname="argument edition", value=edition, expected_type=type_hints["edition"])
            check_type(argname="argument enable_sso", value=enable_sso, expected_type=type_hints["enable_sso"])
            check_type(argname="argument short_name", value=short_name, expected_type=type_hints["short_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "password": password,
            "vpc_settings": vpc_settings,
        }
        if create_alias is not None:
            self._values["create_alias"] = create_alias
        if edition is not None:
            self._values["edition"] = edition
        if enable_sso is not None:
            self._values["enable_sso"] = enable_sso
        if short_name is not None:
            self._values["short_name"] = short_name

    @builtins.property
    def name(self) -> builtins.str:
        '''The fully qualified domain name for the AWS Managed Microsoft AD directory, such as ``corp.example.com`` . This name will resolve inside your VPC only. It does not need to be publicly resolvable.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> builtins.str:
        '''The password for the default administrative user named ``Admin`` .

        If you need to change the password for the administrator account, see the `ResetUserPassword <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ResetUserPassword.html>`_ API call in the *AWS Directory Service API Reference* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-password
        '''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_settings(
        self,
    ) -> typing.Union[CfnMicrosoftAD.VpcSettingsProperty, _aws_cdk_core_f4b25747.IResolvable]:
        '''Specifies the VPC settings of the Microsoft AD directory server in AWS .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-vpcsettings
        '''
        result = self._values.get("vpc_settings")
        assert result is not None, "Required property 'vpc_settings' is missing"
        return typing.cast(typing.Union[CfnMicrosoftAD.VpcSettingsProperty, _aws_cdk_core_f4b25747.IResolvable], result)

    @builtins.property
    def create_alias(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
        '''Specifies an alias for a directory and assigns the alias to the directory.

        The alias is used to construct the access URL for the directory, such as ``http://<alias>.awsapps.com`` . By default, AWS CloudFormation does not create an alias.
        .. epigraph::

           After an alias has been created, it cannot be deleted or reused, so this operation should only be used when absolutely necessary.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-createalias
        '''
        result = self._values.get("create_alias")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

    @builtins.property
    def edition(self) -> typing.Optional[builtins.str]:
        '''AWS Managed Microsoft AD is available in two editions: ``Standard`` and ``Enterprise`` .

        ``Enterprise`` is the default.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-edition
        '''
        result = self._values.get("edition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_sso(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
        '''Whether to enable single sign-on for a Microsoft Active Directory in AWS .

        Single sign-on allows users in your directory to access certain AWS services from a computer joined to the directory without having to enter their credentials separately. If you don't specify a value, AWS CloudFormation disables single sign-on by default.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-enablesso
        '''
        result = self._values.get("enable_sso")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

    @builtins.property
    def short_name(self) -> typing.Optional[builtins.str]:
        '''The NetBIOS name for your domain, such as ``CORP`` .

        If you don't specify a NetBIOS name, it will default to the first part of your directory DNS. For example, ``CORP`` for the directory DNS ``corp.example.com`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-shortname
        '''
        result = self._values.get("short_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMicrosoftADProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnSimpleAD(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-directoryservice.CfnSimpleAD",
):
    '''A CloudFormation ``AWS::DirectoryService::SimpleAD``.

    The ``AWS::DirectoryService::SimpleAD`` resource specifies an AWS Directory Service Simple Active Directory ( Simple AD ) in AWS so that your directory users and groups can access the AWS Management Console and AWS applications using their existing credentials. Simple AD is a Microsoft Active Directory–compatible directory. For more information, see `Simple Active Directory <https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_simple_ad.html>`_ in the *AWS Directory Service Admin Guide* .

    :cloudformationResource: AWS::DirectoryService::SimpleAD
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_directoryservice as directoryservice
        
        cfn_simple_aD = directoryservice.CfnSimpleAD(self, "MyCfnSimpleAD",
            name="name",
            size="size",
            vpc_settings=directoryservice.CfnSimpleAD.VpcSettingsProperty(
                subnet_ids=["subnetIds"],
                vpc_id="vpcId"
            ),
        
            # the properties below are optional
            create_alias=False,
            description="description",
            enable_sso=False,
            password="password",
            short_name="shortName"
        )
    '''

    def __init__(
        self,
        scope: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        size: builtins.str,
        vpc_settings: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnSimpleAD.VpcSettingsProperty", typing.Dict[builtins.str, typing.Any]]],
        create_alias: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        enable_sso: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
        password: typing.Optional[builtins.str] = None,
        short_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::DirectoryService::SimpleAD``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: The fully qualified name for the directory, such as ``corp.example.com`` .
        :param size: The size of the directory. For valid values, see `CreateDirectory <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CreateDirectory.html>`_ in the *AWS Directory Service API Reference* .
        :param vpc_settings: A `DirectoryVpcSettings <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DirectoryVpcSettings.html>`_ object that contains additional information for the operation.
        :param create_alias: If set to ``true`` , specifies an alias for a directory and assigns the alias to the directory. The alias is used to construct the access URL for the directory, such as ``http://<alias>.awsapps.com`` . By default, this property is set to ``false`` . .. epigraph:: After an alias has been created, it cannot be deleted or reused, so this operation should only be used when absolutely necessary.
        :param description: A description for the directory.
        :param enable_sso: Whether to enable single sign-on for a directory. If you don't specify a value, AWS CloudFormation disables single sign-on by default.
        :param password: The password for the directory administrator. The directory creation process creates a directory administrator account with the user name ``Administrator`` and this password. If you need to change the password for the administrator account, see the `ResetUserPassword <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ResetUserPassword.html>`_ API call in the *AWS Directory Service API Reference* .
        :param short_name: The NetBIOS name of the directory, such as ``CORP`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e71a93669fec2134ab369e013e4fe65bafffa726a11070bd1db92172dc115bbb)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSimpleADProps(
            name=name,
            size=size,
            vpc_settings=vpc_settings,
            create_alias=create_alias,
            description=description,
            enable_sso=enable_sso,
            password=password,
            short_name=short_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2622e4990c16e404320de02eaba8d3133975173c48cc72b493621e3bc5abfb0e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d94c6ba68d254eb6c1fc920e8ce7e0f2a427cd13aa3ff63e61222d6aff430757)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAlias")
    def attr_alias(self) -> builtins.str:
        '''The alias for a directory.

        For example: ``d-12373a053a`` or ``alias4-mydirectory-12345abcgmzsk`` (if you have the ``CreateAlias`` property set to true).

        :cloudformationAttribute: Alias
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAlias"))

    @builtins.property
    @jsii.member(jsii_name="attrDirectoryId")
    def attr_directory_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: DirectoryId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDirectoryId"))

    @builtins.property
    @jsii.member(jsii_name="attrDnsIpAddresses")
    def attr_dns_ip_addresses(self) -> typing.List[builtins.str]:
        '''The IP addresses of the DNS servers for the directory, such as ``[ "172.31.3.154", "172.31.63.203" ]`` .

        :cloudformationAttribute: DnsIpAddresses
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrDnsIpAddresses"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The fully qualified name for the directory, such as ``corp.example.com`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__737f342c2c6ed6bc11bf4ae585f13bf303d8edd5faf7262d78b78aee28cce3a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> builtins.str:
        '''The size of the directory.

        For valid values, see `CreateDirectory <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CreateDirectory.html>`_ in the *AWS Directory Service API Reference* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-size
        '''
        return typing.cast(builtins.str, jsii.get(self, "size"))

    @size.setter
    def size(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87356e02d0f24eab8853fd6d08da50348d8d80157049d73d2e353180e9bb9054)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "size", value)

    @builtins.property
    @jsii.member(jsii_name="vpcSettings")
    def vpc_settings(
        self,
    ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnSimpleAD.VpcSettingsProperty"]:
        '''A `DirectoryVpcSettings <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DirectoryVpcSettings.html>`_ object that contains additional information for the operation.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-vpcsettings
        '''
        return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnSimpleAD.VpcSettingsProperty"], jsii.get(self, "vpcSettings"))

    @vpc_settings.setter
    def vpc_settings(
        self,
        value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnSimpleAD.VpcSettingsProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88a1637b63795845cfc61b1fbc200c66578084ce4a116ef023bdc9c4ff8e6770)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcSettings", value)

    @builtins.property
    @jsii.member(jsii_name="createAlias")
    def create_alias(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
        '''If set to ``true`` , specifies an alias for a directory and assigns the alias to the directory.

        The alias is used to construct the access URL for the directory, such as ``http://<alias>.awsapps.com`` . By default, this property is set to ``false`` .
        .. epigraph::

           After an alias has been created, it cannot be deleted or reused, so this operation should only be used when absolutely necessary.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-createalias
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], jsii.get(self, "createAlias"))

    @create_alias.setter
    def create_alias(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cec79f2cbcdc0659d8634b42c3f5646fb11afb7e62566fa6fe9dc7a886854d0f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createAlias", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the directory.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acb9133965aeaf44733c6df26299582897d4d6f6fce39aefb852084e94f61fbe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="enableSso")
    def enable_sso(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
        '''Whether to enable single sign-on for a directory.

        If you don't specify a value, AWS CloudFormation disables single sign-on by default.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-enablesso
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], jsii.get(self, "enableSso"))

    @enable_sso.setter
    def enable_sso(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fdf2b953e6d15007f0299a7cab82961621d87ca62697c8a4e1e7b54026f9b72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableSso", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> typing.Optional[builtins.str]:
        '''The password for the directory administrator.

        The directory creation process creates a directory administrator account with the user name ``Administrator`` and this password.

        If you need to change the password for the administrator account, see the `ResetUserPassword <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ResetUserPassword.html>`_ API call in the *AWS Directory Service API Reference* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-password
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "password"))

    @password.setter
    def password(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60ff907eb64c8afd6430994a53ae11ad174adadb9091cf234726a998caebc370)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="shortName")
    def short_name(self) -> typing.Optional[builtins.str]:
        '''The NetBIOS name of the directory, such as ``CORP`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-shortname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shortName"))

    @short_name.setter
    def short_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e3bbe09876640fa94a4d88d3301871f77f7e019aeba352842df81e7660b3490)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shortName", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-directoryservice.CfnSimpleAD.VpcSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"subnet_ids": "subnetIds", "vpc_id": "vpcId"},
    )
    class VpcSettingsProperty:
        def __init__(
            self,
            *,
            subnet_ids: typing.Sequence[builtins.str],
            vpc_id: builtins.str,
        ) -> None:
            '''Contains VPC information for the `CreateDirectory <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CreateDirectory.html>`_ or `CreateMicrosoftAD <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CreateMicrosoftAD.html>`_ operation.

            :param subnet_ids: The identifiers of the subnets for the directory servers. The two subnets must be in different Availability Zones. AWS Directory Service specifies a directory server and a DNS server in each of these subnets.
            :param vpc_id: The identifier of the VPC in which to create the directory.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-simplead-vpcsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_directoryservice as directoryservice
                
                vpc_settings_property = directoryservice.CfnSimpleAD.VpcSettingsProperty(
                    subnet_ids=["subnetIds"],
                    vpc_id="vpcId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__631034e5af15aa13c29aac2225c6f15b79215e5589a99d9322f6d784044662ea)
                check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
                check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "subnet_ids": subnet_ids,
                "vpc_id": vpc_id,
            }

        @builtins.property
        def subnet_ids(self) -> typing.List[builtins.str]:
            '''The identifiers of the subnets for the directory servers.

            The two subnets must be in different Availability Zones. AWS Directory Service specifies a directory server and a DNS server in each of these subnets.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-simplead-vpcsettings.html#cfn-directoryservice-simplead-vpcsettings-subnetids
            '''
            result = self._values.get("subnet_ids")
            assert result is not None, "Required property 'subnet_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def vpc_id(self) -> builtins.str:
            '''The identifier of the VPC in which to create the directory.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-simplead-vpcsettings.html#cfn-directoryservice-simplead-vpcsettings-vpcid
            '''
            result = self._values.get("vpc_id")
            assert result is not None, "Required property 'vpc_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-directoryservice.CfnSimpleADProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "size": "size",
        "vpc_settings": "vpcSettings",
        "create_alias": "createAlias",
        "description": "description",
        "enable_sso": "enableSso",
        "password": "password",
        "short_name": "shortName",
    },
)
class CfnSimpleADProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        size: builtins.str,
        vpc_settings: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnSimpleAD.VpcSettingsProperty, typing.Dict[builtins.str, typing.Any]]],
        create_alias: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        enable_sso: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
        password: typing.Optional[builtins.str] = None,
        short_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnSimpleAD``.

        :param name: The fully qualified name for the directory, such as ``corp.example.com`` .
        :param size: The size of the directory. For valid values, see `CreateDirectory <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CreateDirectory.html>`_ in the *AWS Directory Service API Reference* .
        :param vpc_settings: A `DirectoryVpcSettings <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DirectoryVpcSettings.html>`_ object that contains additional information for the operation.
        :param create_alias: If set to ``true`` , specifies an alias for a directory and assigns the alias to the directory. The alias is used to construct the access URL for the directory, such as ``http://<alias>.awsapps.com`` . By default, this property is set to ``false`` . .. epigraph:: After an alias has been created, it cannot be deleted or reused, so this operation should only be used when absolutely necessary.
        :param description: A description for the directory.
        :param enable_sso: Whether to enable single sign-on for a directory. If you don't specify a value, AWS CloudFormation disables single sign-on by default.
        :param password: The password for the directory administrator. The directory creation process creates a directory administrator account with the user name ``Administrator`` and this password. If you need to change the password for the administrator account, see the `ResetUserPassword <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ResetUserPassword.html>`_ API call in the *AWS Directory Service API Reference* .
        :param short_name: The NetBIOS name of the directory, such as ``CORP`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_directoryservice as directoryservice
            
            cfn_simple_aDProps = directoryservice.CfnSimpleADProps(
                name="name",
                size="size",
                vpc_settings=directoryservice.CfnSimpleAD.VpcSettingsProperty(
                    subnet_ids=["subnetIds"],
                    vpc_id="vpcId"
                ),
            
                # the properties below are optional
                create_alias=False,
                description="description",
                enable_sso=False,
                password="password",
                short_name="shortName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d5d11cd6738e8232ef64c1555ed3b70d1985286344d6f8126d6e53f55337291)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument size", value=size, expected_type=type_hints["size"])
            check_type(argname="argument vpc_settings", value=vpc_settings, expected_type=type_hints["vpc_settings"])
            check_type(argname="argument create_alias", value=create_alias, expected_type=type_hints["create_alias"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument enable_sso", value=enable_sso, expected_type=type_hints["enable_sso"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument short_name", value=short_name, expected_type=type_hints["short_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "size": size,
            "vpc_settings": vpc_settings,
        }
        if create_alias is not None:
            self._values["create_alias"] = create_alias
        if description is not None:
            self._values["description"] = description
        if enable_sso is not None:
            self._values["enable_sso"] = enable_sso
        if password is not None:
            self._values["password"] = password
        if short_name is not None:
            self._values["short_name"] = short_name

    @builtins.property
    def name(self) -> builtins.str:
        '''The fully qualified name for the directory, such as ``corp.example.com`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def size(self) -> builtins.str:
        '''The size of the directory.

        For valid values, see `CreateDirectory <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_CreateDirectory.html>`_ in the *AWS Directory Service API Reference* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-size
        '''
        result = self._values.get("size")
        assert result is not None, "Required property 'size' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_settings(
        self,
    ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnSimpleAD.VpcSettingsProperty]:
        '''A `DirectoryVpcSettings <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_DirectoryVpcSettings.html>`_ object that contains additional information for the operation.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-vpcsettings
        '''
        result = self._values.get("vpc_settings")
        assert result is not None, "Required property 'vpc_settings' is missing"
        return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnSimpleAD.VpcSettingsProperty], result)

    @builtins.property
    def create_alias(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
        '''If set to ``true`` , specifies an alias for a directory and assigns the alias to the directory.

        The alias is used to construct the access URL for the directory, such as ``http://<alias>.awsapps.com`` . By default, this property is set to ``false`` .
        .. epigraph::

           After an alias has been created, it cannot be deleted or reused, so this operation should only be used when absolutely necessary.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-createalias
        '''
        result = self._values.get("create_alias")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the directory.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_sso(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
        '''Whether to enable single sign-on for a directory.

        If you don't specify a value, AWS CloudFormation disables single sign-on by default.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-enablesso
        '''
        result = self._values.get("enable_sso")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The password for the directory administrator.

        The directory creation process creates a directory administrator account with the user name ``Administrator`` and this password.

        If you need to change the password for the administrator account, see the `ResetUserPassword <https://docs.aws.amazon.com/directoryservice/latest/devguide/API_ResetUserPassword.html>`_ API call in the *AWS Directory Service API Reference* .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-password
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def short_name(self) -> typing.Optional[builtins.str]:
        '''The NetBIOS name of the directory, such as ``CORP`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-shortname
        '''
        result = self._values.get("short_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSimpleADProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnMicrosoftAD",
    "CfnMicrosoftADProps",
    "CfnSimpleAD",
    "CfnSimpleADProps",
]

publication.publish()

def _typecheckingstub__3941813ded2bd7b528b2c263c13d48424aa047e76e91484cff219d8f757b95b8(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    password: builtins.str,
    vpc_settings: typing.Union[typing.Union[CfnMicrosoftAD.VpcSettingsProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable],
    create_alias: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    edition: typing.Optional[builtins.str] = None,
    enable_sso: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    short_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68b568d3166dec9ec4b675deb257676797fea4865e55483fe0a01a13e37a14cb(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3335583b72747fa3aaf1f923d5c7b4939d465229e0fa7676d852f34c1bf42b1a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56bb46b36135a069321881902677f42f5ecbe9f42abab1211a2c9b4404f81b38(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58a78a8e58ff6b31762ce306e04d8411d273b3c14d28ff4dc90b91b6073a923b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ab9e5718b3f3ed3487ad6c247d2135e6ad1c29296fe26781c8beb627dd3621c(
    value: typing.Union[CfnMicrosoftAD.VpcSettingsProperty, _aws_cdk_core_f4b25747.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cf396943ae4572d04ed1f357d3a41fcd8ed1569947b9ffb6233f7d90b6c6350(
    value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1f803dd9738ed2c5e87aee5e22e689dca61a85d34c4e506e11368841b4adec2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0857b2bb71f6a8f0b48b7ca73a1cf677eca32186ef663edd9f745a184daae341(
    value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__734f1d0aef4307be9ad8bce48df347b8b354fe1030d7ad5dbe2022e0bdfbd61a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__753d762ea6fe9e3b8643ccbf2c9cad670b078a481699b51dff5d6722006eb7d7(
    *,
    subnet_ids: typing.Sequence[builtins.str],
    vpc_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45e69c269ea8b6b7d89ff8a1804825055c30a6bff99807479b557ac1f5e622ee(
    *,
    name: builtins.str,
    password: builtins.str,
    vpc_settings: typing.Union[typing.Union[CfnMicrosoftAD.VpcSettingsProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable],
    create_alias: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    edition: typing.Optional[builtins.str] = None,
    enable_sso: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    short_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e71a93669fec2134ab369e013e4fe65bafffa726a11070bd1db92172dc115bbb(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    size: builtins.str,
    vpc_settings: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnSimpleAD.VpcSettingsProperty, typing.Dict[builtins.str, typing.Any]]],
    create_alias: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    description: typing.Optional[builtins.str] = None,
    enable_sso: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    password: typing.Optional[builtins.str] = None,
    short_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2622e4990c16e404320de02eaba8d3133975173c48cc72b493621e3bc5abfb0e(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d94c6ba68d254eb6c1fc920e8ce7e0f2a427cd13aa3ff63e61222d6aff430757(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__737f342c2c6ed6bc11bf4ae585f13bf303d8edd5faf7262d78b78aee28cce3a6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87356e02d0f24eab8853fd6d08da50348d8d80157049d73d2e353180e9bb9054(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88a1637b63795845cfc61b1fbc200c66578084ce4a116ef023bdc9c4ff8e6770(
    value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnSimpleAD.VpcSettingsProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cec79f2cbcdc0659d8634b42c3f5646fb11afb7e62566fa6fe9dc7a886854d0f(
    value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acb9133965aeaf44733c6df26299582897d4d6f6fce39aefb852084e94f61fbe(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fdf2b953e6d15007f0299a7cab82961621d87ca62697c8a4e1e7b54026f9b72(
    value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60ff907eb64c8afd6430994a53ae11ad174adadb9091cf234726a998caebc370(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e3bbe09876640fa94a4d88d3301871f77f7e019aeba352842df81e7660b3490(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__631034e5af15aa13c29aac2225c6f15b79215e5589a99d9322f6d784044662ea(
    *,
    subnet_ids: typing.Sequence[builtins.str],
    vpc_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d5d11cd6738e8232ef64c1555ed3b70d1985286344d6f8126d6e53f55337291(
    *,
    name: builtins.str,
    size: builtins.str,
    vpc_settings: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnSimpleAD.VpcSettingsProperty, typing.Dict[builtins.str, typing.Any]]],
    create_alias: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    description: typing.Optional[builtins.str] = None,
    enable_sso: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    password: typing.Optional[builtins.str] = None,
    short_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

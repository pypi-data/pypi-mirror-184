'''
# AWS::Kendra Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_kendra as kendra
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Kendra construct libraries](https://constructs.dev/search?q=kendra)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Kendra resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Kendra.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Kendra](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Kendra.html).

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
class CfnDataSource(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-kendra.CfnDataSource",
):
    '''A CloudFormation ``AWS::Kendra::DataSource``.

    Creates a data source connector that you want to use with an Amazon Kendra index.

    You specify a name, data source connector type and description for your data source. You also specify configuration information for the data source connector.

    :cloudformationResource: AWS::Kendra::DataSource
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_kendra as kendra
        
        cfn_data_source = kendra.CfnDataSource(self, "MyCfnDataSource",
            index_id="indexId",
            name="name",
            type="type",
        
            # the properties below are optional
            custom_document_enrichment_configuration=kendra.CfnDataSource.CustomDocumentEnrichmentConfigurationProperty(
                inline_configurations=[kendra.CfnDataSource.InlineCustomDocumentEnrichmentConfigurationProperty(
                    condition=kendra.CfnDataSource.DocumentAttributeConditionProperty(
                        condition_document_attribute_key="conditionDocumentAttributeKey",
                        operator="operator",
        
                        # the properties below are optional
                        condition_on_value=kendra.CfnDataSource.DocumentAttributeValueProperty(
                            date_value="dateValue",
                            long_value=123,
                            string_list_value=["stringListValue"],
                            string_value="stringValue"
                        )
                    ),
                    document_content_deletion=False,
                    target=kendra.CfnDataSource.DocumentAttributeTargetProperty(
                        target_document_attribute_key="targetDocumentAttributeKey",
        
                        # the properties below are optional
                        target_document_attribute_value=kendra.CfnDataSource.DocumentAttributeValueProperty(
                            date_value="dateValue",
                            long_value=123,
                            string_list_value=["stringListValue"],
                            string_value="stringValue"
                        ),
                        target_document_attribute_value_deletion=False
                    )
                )],
                post_extraction_hook_configuration=kendra.CfnDataSource.HookConfigurationProperty(
                    lambda_arn="lambdaArn",
                    s3_bucket="s3Bucket",
        
                    # the properties below are optional
                    invocation_condition=kendra.CfnDataSource.DocumentAttributeConditionProperty(
                        condition_document_attribute_key="conditionDocumentAttributeKey",
                        operator="operator",
        
                        # the properties below are optional
                        condition_on_value=kendra.CfnDataSource.DocumentAttributeValueProperty(
                            date_value="dateValue",
                            long_value=123,
                            string_list_value=["stringListValue"],
                            string_value="stringValue"
                        )
                    )
                ),
                pre_extraction_hook_configuration=kendra.CfnDataSource.HookConfigurationProperty(
                    lambda_arn="lambdaArn",
                    s3_bucket="s3Bucket",
        
                    # the properties below are optional
                    invocation_condition=kendra.CfnDataSource.DocumentAttributeConditionProperty(
                        condition_document_attribute_key="conditionDocumentAttributeKey",
                        operator="operator",
        
                        # the properties below are optional
                        condition_on_value=kendra.CfnDataSource.DocumentAttributeValueProperty(
                            date_value="dateValue",
                            long_value=123,
                            string_list_value=["stringListValue"],
                            string_value="stringValue"
                        )
                    )
                ),
                role_arn="roleArn"
            ),
            data_source_configuration=kendra.CfnDataSource.DataSourceConfigurationProperty(
                confluence_configuration=kendra.CfnDataSource.ConfluenceConfigurationProperty(
                    secret_arn="secretArn",
                    server_url="serverUrl",
                    version="version",
        
                    # the properties below are optional
                    attachment_configuration=kendra.CfnDataSource.ConfluenceAttachmentConfigurationProperty(
                        attachment_field_mappings=[kendra.CfnDataSource.ConfluenceAttachmentToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
        
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )],
                        crawl_attachments=False
                    ),
                    blog_configuration=kendra.CfnDataSource.ConfluenceBlogConfigurationProperty(
                        blog_field_mappings=[kendra.CfnDataSource.ConfluenceBlogToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
        
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )]
                    ),
                    exclusion_patterns=["exclusionPatterns"],
                    inclusion_patterns=["inclusionPatterns"],
                    page_configuration=kendra.CfnDataSource.ConfluencePageConfigurationProperty(
                        page_field_mappings=[kendra.CfnDataSource.ConfluencePageToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
        
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )]
                    ),
                    space_configuration=kendra.CfnDataSource.ConfluenceSpaceConfigurationProperty(
                        crawl_archived_spaces=False,
                        crawl_personal_spaces=False,
                        exclude_spaces=["excludeSpaces"],
                        include_spaces=["includeSpaces"],
                        space_field_mappings=[kendra.CfnDataSource.ConfluenceSpaceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
        
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )]
                    ),
                    vpc_configuration=kendra.CfnDataSource.DataSourceVpcConfigurationProperty(
                        security_group_ids=["securityGroupIds"],
                        subnet_ids=["subnetIds"]
                    )
                ),
                database_configuration=kendra.CfnDataSource.DatabaseConfigurationProperty(
                    column_configuration=kendra.CfnDataSource.ColumnConfigurationProperty(
                        change_detecting_columns=["changeDetectingColumns"],
                        document_data_column_name="documentDataColumnName",
                        document_id_column_name="documentIdColumnName",
        
                        # the properties below are optional
                        document_title_column_name="documentTitleColumnName",
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
        
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )]
                    ),
                    connection_configuration=kendra.CfnDataSource.ConnectionConfigurationProperty(
                        database_host="databaseHost",
                        database_name="databaseName",
                        database_port=123,
                        secret_arn="secretArn",
                        table_name="tableName"
                    ),
                    database_engine_type="databaseEngineType",
        
                    # the properties below are optional
                    acl_configuration=kendra.CfnDataSource.AclConfigurationProperty(
                        allowed_groups_column_name="allowedGroupsColumnName"
                    ),
                    sql_configuration=kendra.CfnDataSource.SqlConfigurationProperty(
                        query_identifiers_enclosing_option="queryIdentifiersEnclosingOption"
                    ),
                    vpc_configuration=kendra.CfnDataSource.DataSourceVpcConfigurationProperty(
                        security_group_ids=["securityGroupIds"],
                        subnet_ids=["subnetIds"]
                    )
                ),
                google_drive_configuration=kendra.CfnDataSource.GoogleDriveConfigurationProperty(
                    secret_arn="secretArn",
        
                    # the properties below are optional
                    exclude_mime_types=["excludeMimeTypes"],
                    exclude_shared_drives=["excludeSharedDrives"],
                    exclude_user_accounts=["excludeUserAccounts"],
                    exclusion_patterns=["exclusionPatterns"],
                    field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                        data_source_field_name="dataSourceFieldName",
                        index_field_name="indexFieldName",
        
                        # the properties below are optional
                        date_field_format="dateFieldFormat"
                    )],
                    inclusion_patterns=["inclusionPatterns"]
                ),
                one_drive_configuration=kendra.CfnDataSource.OneDriveConfigurationProperty(
                    one_drive_users=kendra.CfnDataSource.OneDriveUsersProperty(
                        one_drive_user_list=["oneDriveUserList"],
                        one_drive_user_s3_path=kendra.CfnDataSource.S3PathProperty(
                            bucket="bucket",
                            key="key"
                        )
                    ),
                    secret_arn="secretArn",
                    tenant_domain="tenantDomain",
        
                    # the properties below are optional
                    disable_local_groups=False,
                    exclusion_patterns=["exclusionPatterns"],
                    field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                        data_source_field_name="dataSourceFieldName",
                        index_field_name="indexFieldName",
        
                        # the properties below are optional
                        date_field_format="dateFieldFormat"
                    )],
                    inclusion_patterns=["inclusionPatterns"]
                ),
                s3_configuration=kendra.CfnDataSource.S3DataSourceConfigurationProperty(
                    bucket_name="bucketName",
        
                    # the properties below are optional
                    access_control_list_configuration=kendra.CfnDataSource.AccessControlListConfigurationProperty(
                        key_path="keyPath"
                    ),
                    documents_metadata_configuration=kendra.CfnDataSource.DocumentsMetadataConfigurationProperty(
                        s3_prefix="s3Prefix"
                    ),
                    exclusion_patterns=["exclusionPatterns"],
                    inclusion_patterns=["inclusionPatterns"],
                    inclusion_prefixes=["inclusionPrefixes"]
                ),
                salesforce_configuration=kendra.CfnDataSource.SalesforceConfigurationProperty(
                    secret_arn="secretArn",
                    server_url="serverUrl",
        
                    # the properties below are optional
                    chatter_feed_configuration=kendra.CfnDataSource.SalesforceChatterFeedConfigurationProperty(
                        document_data_field_name="documentDataFieldName",
        
                        # the properties below are optional
                        document_title_field_name="documentTitleFieldName",
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
        
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )],
                        include_filter_types=["includeFilterTypes"]
                    ),
                    crawl_attachments=False,
                    exclude_attachment_file_patterns=["excludeAttachmentFilePatterns"],
                    include_attachment_file_patterns=["includeAttachmentFilePatterns"],
                    knowledge_article_configuration=kendra.CfnDataSource.SalesforceKnowledgeArticleConfigurationProperty(
                        included_states=["includedStates"],
        
                        # the properties below are optional
                        custom_knowledge_article_type_configurations=[kendra.CfnDataSource.SalesforceCustomKnowledgeArticleTypeConfigurationProperty(
                            document_data_field_name="documentDataFieldName",
                            name="name",
        
                            # the properties below are optional
                            document_title_field_name="documentTitleFieldName",
                            field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
        
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )]
                        )],
                        standard_knowledge_article_type_configuration=kendra.CfnDataSource.SalesforceStandardKnowledgeArticleTypeConfigurationProperty(
                            document_data_field_name="documentDataFieldName",
        
                            # the properties below are optional
                            document_title_field_name="documentTitleFieldName",
                            field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
        
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )]
                        )
                    ),
                    standard_object_attachment_configuration=kendra.CfnDataSource.SalesforceStandardObjectAttachmentConfigurationProperty(
                        document_title_field_name="documentTitleFieldName",
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
        
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )]
                    ),
                    standard_object_configurations=[kendra.CfnDataSource.SalesforceStandardObjectConfigurationProperty(
                        document_data_field_name="documentDataFieldName",
                        name="name",
        
                        # the properties below are optional
                        document_title_field_name="documentTitleFieldName",
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
        
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )]
                    )]
                ),
                service_now_configuration=kendra.CfnDataSource.ServiceNowConfigurationProperty(
                    host_url="hostUrl",
                    secret_arn="secretArn",
                    service_now_build_version="serviceNowBuildVersion",
        
                    # the properties below are optional
                    authentication_type="authenticationType",
                    knowledge_article_configuration=kendra.CfnDataSource.ServiceNowKnowledgeArticleConfigurationProperty(
                        document_data_field_name="documentDataFieldName",
        
                        # the properties below are optional
                        crawl_attachments=False,
                        document_title_field_name="documentTitleFieldName",
                        exclude_attachment_file_patterns=["excludeAttachmentFilePatterns"],
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
        
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )],
                        filter_query="filterQuery",
                        include_attachment_file_patterns=["includeAttachmentFilePatterns"]
                    ),
                    service_catalog_configuration=kendra.CfnDataSource.ServiceNowServiceCatalogConfigurationProperty(
                        document_data_field_name="documentDataFieldName",
        
                        # the properties below are optional
                        crawl_attachments=False,
                        document_title_field_name="documentTitleFieldName",
                        exclude_attachment_file_patterns=["excludeAttachmentFilePatterns"],
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
        
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )],
                        include_attachment_file_patterns=["includeAttachmentFilePatterns"]
                    )
                ),
                share_point_configuration=kendra.CfnDataSource.SharePointConfigurationProperty(
                    secret_arn="secretArn",
                    share_point_version="sharePointVersion",
                    urls=["urls"],
        
                    # the properties below are optional
                    crawl_attachments=False,
                    disable_local_groups=False,
                    document_title_field_name="documentTitleFieldName",
                    exclusion_patterns=["exclusionPatterns"],
                    field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                        data_source_field_name="dataSourceFieldName",
                        index_field_name="indexFieldName",
        
                        # the properties below are optional
                        date_field_format="dateFieldFormat"
                    )],
                    inclusion_patterns=["inclusionPatterns"],
                    ssl_certificate_s3_path=kendra.CfnDataSource.S3PathProperty(
                        bucket="bucket",
                        key="key"
                    ),
                    use_change_log=False,
                    vpc_configuration=kendra.CfnDataSource.DataSourceVpcConfigurationProperty(
                        security_group_ids=["securityGroupIds"],
                        subnet_ids=["subnetIds"]
                    )
                ),
                web_crawler_configuration=kendra.CfnDataSource.WebCrawlerConfigurationProperty(
                    urls=kendra.CfnDataSource.WebCrawlerUrlsProperty(
                        seed_url_configuration=kendra.CfnDataSource.WebCrawlerSeedUrlConfigurationProperty(
                            seed_urls=["seedUrls"],
        
                            # the properties below are optional
                            web_crawler_mode="webCrawlerMode"
                        ),
                        site_maps_configuration=kendra.CfnDataSource.WebCrawlerSiteMapsConfigurationProperty(
                            site_maps=["siteMaps"]
                        )
                    ),
        
                    # the properties below are optional
                    authentication_configuration=kendra.CfnDataSource.WebCrawlerAuthenticationConfigurationProperty(
                        basic_authentication=[kendra.CfnDataSource.WebCrawlerBasicAuthenticationProperty(
                            credentials="credentials",
                            host="host",
                            port=123
                        )]
                    ),
                    crawl_depth=123,
                    max_content_size_per_page_in_mega_bytes=123,
                    max_links_per_page=123,
                    max_urls_per_minute_crawl_rate=123,
                    proxy_configuration=kendra.CfnDataSource.ProxyConfigurationProperty(
                        host="host",
                        port=123,
        
                        # the properties below are optional
                        credentials="credentials"
                    ),
                    url_exclusion_patterns=["urlExclusionPatterns"],
                    url_inclusion_patterns=["urlInclusionPatterns"]
                ),
                work_docs_configuration=kendra.CfnDataSource.WorkDocsConfigurationProperty(
                    organization_id="organizationId",
        
                    # the properties below are optional
                    crawl_comments=False,
                    exclusion_patterns=["exclusionPatterns"],
                    field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                        data_source_field_name="dataSourceFieldName",
                        index_field_name="indexFieldName",
        
                        # the properties below are optional
                        date_field_format="dateFieldFormat"
                    )],
                    inclusion_patterns=["inclusionPatterns"],
                    use_change_log=False
                )
            ),
            description="description",
            role_arn="roleArn",
            schedule="schedule",
            tags=[CfnTag(
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
        index_id: builtins.str,
        name: builtins.str,
        type: builtins.str,
        custom_document_enrichment_configuration: typing.Optional[typing.Union[typing.Union["CfnDataSource.CustomDocumentEnrichmentConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable]] = None,
        data_source_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.DataSourceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
        schedule: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Kendra::DataSource``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param index_id: The identifier of the index you want to use with the data source connector.
        :param name: The name of the data source.
        :param type: The type of the data source.
        :param custom_document_enrichment_configuration: Configuration information for altering document metadata and content during the document ingestion process.
        :param data_source_configuration: Configuration information for an Amazon Kendra data source. The contents of the configuration depend on the type of data source. You can only specify one type of data source in the configuration. You can't specify the ``Configuration`` parameter when the ``Type`` parameter is set to ``CUSTOM`` . The ``Configuration`` parameter is required for all other data sources.
        :param description: A description for the data source connector.
        :param role_arn: The Amazon Resource Name (ARN) of a role with permission to access the data source. You can't specify the ``RoleArn`` parameter when the ``Type`` parameter is set to ``CUSTOM`` . The ``RoleArn`` parameter is required for all other data sources.
        :param schedule: Sets the frequency that Amazon Kendra checks the documents in your data source and updates the index. If you don't set a schedule, Amazon Kendra doesn't periodically update the index.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__838c3775e79472827c639434b94d1cb415bc65f25d6d12e5896dab3e100005b1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDataSourceProps(
            index_id=index_id,
            name=name,
            type=type,
            custom_document_enrichment_configuration=custom_document_enrichment_configuration,
            data_source_configuration=data_source_configuration,
            description=description,
            role_arn=role_arn,
            schedule=schedule,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d5d31fa3e48e4f196ab3f69173009494a068d434fc7e6d1311d65ba7c502906)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0ab91ce8785e6a63b0d70715e363d1f50645e95d88006ea7fefc3b1e0a035f81)
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
        '''The Amazon Resource Name (ARN) of the data source. For example:.

        ``arn:aws:kendra:us-west-2:111122223333:index/335c3741-41df-46a6-b5d3-61f85b787884/data-source/b8cae438-6787-4091-8897-684a652bbb0a``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The identifier for the data source. For example:.

        ``b8cae438-6787-4091-8897-684a652bbb0a`` .

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _aws_cdk_core_f4b25747.TagManager:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-tags
        '''
        return typing.cast(_aws_cdk_core_f4b25747.TagManager, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="indexId")
    def index_id(self) -> builtins.str:
        '''The identifier of the index you want to use with the data source connector.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-indexid
        '''
        return typing.cast(builtins.str, jsii.get(self, "indexId"))

    @index_id.setter
    def index_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f054cc0e922eef2864cd379fb19130f2324a2373ba765ff284d0b0ea068bdca2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "indexId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the data source.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95512cd9daf4fe119adae42fb422a7783562418c0503d7e9cad9e1f5decb23c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type of the data source.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-type
        '''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6bcc0dd41454067a102f5153dd74d508c891b4416496138bc3d65b37ce383b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="customDocumentEnrichmentConfiguration")
    def custom_document_enrichment_configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnDataSource.CustomDocumentEnrichmentConfigurationProperty", _aws_cdk_core_f4b25747.IResolvable]]:
        '''Configuration information for altering document metadata and content during the document ingestion process.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-customdocumentenrichmentconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union["CfnDataSource.CustomDocumentEnrichmentConfigurationProperty", _aws_cdk_core_f4b25747.IResolvable]], jsii.get(self, "customDocumentEnrichmentConfiguration"))

    @custom_document_enrichment_configuration.setter
    def custom_document_enrichment_configuration(
        self,
        value: typing.Optional[typing.Union["CfnDataSource.CustomDocumentEnrichmentConfigurationProperty", _aws_cdk_core_f4b25747.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df8a4f8da541e2f4e257fee5554cb2dbff3c43e29904e686872395eba7a3f687)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customDocumentEnrichmentConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="dataSourceConfiguration")
    def data_source_configuration(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DataSourceConfigurationProperty"]]:
        '''Configuration information for an Amazon Kendra data source.

        The contents of the configuration depend on the type of data source. You can only specify one type of data source in the configuration.

        You can't specify the ``Configuration`` parameter when the ``Type`` parameter is set to ``CUSTOM`` .

        The ``Configuration`` parameter is required for all other data sources.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-datasourceconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DataSourceConfigurationProperty"]], jsii.get(self, "dataSourceConfiguration"))

    @data_source_configuration.setter
    def data_source_configuration(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DataSourceConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cf582e4e0d93058a5d69f75ea66337c4c20e3da032652df133859f9acf7662c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataSourceConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the data source connector.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1acaf915aee0950d33184ae0b090a90b862b5eb57845726c612b2b02b6cc6e60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of a role with permission to access the data source.

        You can't specify the ``RoleArn`` parameter when the ``Type`` parameter is set to ``CUSTOM`` .

        The ``RoleArn`` parameter is required for all other data sources.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-rolearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8a12b99c285b2e691b3b5c75162f4a09d7c74929bee4f696a31383855432bff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(self) -> typing.Optional[builtins.str]:
        '''Sets the frequency that Amazon Kendra checks the documents in your data source and updates the index.

        If you don't set a schedule, Amazon Kendra doesn't periodically update the index.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-schedule
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schedule"))

    @schedule.setter
    def schedule(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7ba1be93af2b0769a490dd83b4fbe931296c5ab24324d25facceec7775df474)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedule", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.AccessControlListConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"key_path": "keyPath"},
    )
    class AccessControlListConfigurationProperty:
        def __init__(self, *, key_path: typing.Optional[builtins.str] = None) -> None:
            '''Specifies access control list files for the documents in a data source.

            :param key_path: Path to the AWS S3 bucket that contains the access control list files.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-accesscontrollistconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                access_control_list_configuration_property = kendra.CfnDataSource.AccessControlListConfigurationProperty(
                    key_path="keyPath"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4a46122186a9433b6353533e6955e27217a2ce211d65c579ec8d34f7184bc3fa)
                check_type(argname="argument key_path", value=key_path, expected_type=type_hints["key_path"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if key_path is not None:
                self._values["key_path"] = key_path

        @builtins.property
        def key_path(self) -> typing.Optional[builtins.str]:
            '''Path to the AWS S3 bucket that contains the access control list files.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-accesscontrollistconfiguration.html#cfn-kendra-datasource-accesscontrollistconfiguration-keypath
            '''
            result = self._values.get("key_path")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AccessControlListConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.AclConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"allowed_groups_column_name": "allowedGroupsColumnName"},
    )
    class AclConfigurationProperty:
        def __init__(self, *, allowed_groups_column_name: builtins.str) -> None:
            '''Provides information about the column that should be used for filtering the query response by groups.

            :param allowed_groups_column_name: A list of groups, separated by semi-colons, that filters a query response based on user context. The document is only returned to users that are in one of the groups specified in the ``UserContext`` field of the `Query <https://docs.aws.amazon.com/kendra/latest/dg/API_Query.html>`_ operation.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-aclconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                acl_configuration_property = kendra.CfnDataSource.AclConfigurationProperty(
                    allowed_groups_column_name="allowedGroupsColumnName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cdc8384e21439c502e453c0e9f9e8ce3693e7db7a2956d088ec32ac22336d8d5)
                check_type(argname="argument allowed_groups_column_name", value=allowed_groups_column_name, expected_type=type_hints["allowed_groups_column_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "allowed_groups_column_name": allowed_groups_column_name,
            }

        @builtins.property
        def allowed_groups_column_name(self) -> builtins.str:
            '''A list of groups, separated by semi-colons, that filters a query response based on user context.

            The document is only returned to users that are in one of the groups specified in the ``UserContext`` field of the `Query <https://docs.aws.amazon.com/kendra/latest/dg/API_Query.html>`_ operation.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-aclconfiguration.html#cfn-kendra-datasource-aclconfiguration-allowedgroupscolumnname
            '''
            result = self._values.get("allowed_groups_column_name")
            assert result is not None, "Required property 'allowed_groups_column_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AclConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.ColumnConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "change_detecting_columns": "changeDetectingColumns",
            "document_data_column_name": "documentDataColumnName",
            "document_id_column_name": "documentIdColumnName",
            "document_title_column_name": "documentTitleColumnName",
            "field_mappings": "fieldMappings",
        },
    )
    class ColumnConfigurationProperty:
        def __init__(
            self,
            *,
            change_detecting_columns: typing.Sequence[builtins.str],
            document_data_column_name: builtins.str,
            document_id_column_name: builtins.str,
            document_title_column_name: typing.Optional[builtins.str] = None,
            field_mappings: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Provides information about how Amazon Kendra should use the columns of a database in an index.

            :param change_detecting_columns: One to five columns that indicate when a document in the database has changed.
            :param document_data_column_name: The column that contains the contents of the document.
            :param document_id_column_name: The column that provides the document's identifier.
            :param document_title_column_name: The column that contains the title of the document.
            :param field_mappings: An array of objects that map database column names to the corresponding fields in an index. You must first create the fields in the index using the `UpdateIndex <https://docs.aws.amazon.com/kendra/latest/dg/API_UpdateIndex.html>`_ operation.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-columnconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                column_configuration_property = kendra.CfnDataSource.ColumnConfigurationProperty(
                    change_detecting_columns=["changeDetectingColumns"],
                    document_data_column_name="documentDataColumnName",
                    document_id_column_name="documentIdColumnName",
                
                    # the properties below are optional
                    document_title_column_name="documentTitleColumnName",
                    field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                        data_source_field_name="dataSourceFieldName",
                        index_field_name="indexFieldName",
                
                        # the properties below are optional
                        date_field_format="dateFieldFormat"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__09effd1c50e617607c8bfcbdc57bb843bed98d278f24cdd3208a1415daba682d)
                check_type(argname="argument change_detecting_columns", value=change_detecting_columns, expected_type=type_hints["change_detecting_columns"])
                check_type(argname="argument document_data_column_name", value=document_data_column_name, expected_type=type_hints["document_data_column_name"])
                check_type(argname="argument document_id_column_name", value=document_id_column_name, expected_type=type_hints["document_id_column_name"])
                check_type(argname="argument document_title_column_name", value=document_title_column_name, expected_type=type_hints["document_title_column_name"])
                check_type(argname="argument field_mappings", value=field_mappings, expected_type=type_hints["field_mappings"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "change_detecting_columns": change_detecting_columns,
                "document_data_column_name": document_data_column_name,
                "document_id_column_name": document_id_column_name,
            }
            if document_title_column_name is not None:
                self._values["document_title_column_name"] = document_title_column_name
            if field_mappings is not None:
                self._values["field_mappings"] = field_mappings

        @builtins.property
        def change_detecting_columns(self) -> typing.List[builtins.str]:
            '''One to five columns that indicate when a document in the database has changed.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-columnconfiguration.html#cfn-kendra-datasource-columnconfiguration-changedetectingcolumns
            '''
            result = self._values.get("change_detecting_columns")
            assert result is not None, "Required property 'change_detecting_columns' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def document_data_column_name(self) -> builtins.str:
            '''The column that contains the contents of the document.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-columnconfiguration.html#cfn-kendra-datasource-columnconfiguration-documentdatacolumnname
            '''
            result = self._values.get("document_data_column_name")
            assert result is not None, "Required property 'document_data_column_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def document_id_column_name(self) -> builtins.str:
            '''The column that provides the document's identifier.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-columnconfiguration.html#cfn-kendra-datasource-columnconfiguration-documentidcolumnname
            '''
            result = self._values.get("document_id_column_name")
            assert result is not None, "Required property 'document_id_column_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def document_title_column_name(self) -> typing.Optional[builtins.str]:
            '''The column that contains the title of the document.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-columnconfiguration.html#cfn-kendra-datasource-columnconfiguration-documenttitlecolumnname
            '''
            result = self._values.get("document_title_column_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def field_mappings(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DataSourceToIndexFieldMappingProperty"]]]]:
            '''An array of objects that map database column names to the corresponding fields in an index.

            You must first create the fields in the index using the `UpdateIndex <https://docs.aws.amazon.com/kendra/latest/dg/API_UpdateIndex.html>`_ operation.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-columnconfiguration.html#cfn-kendra-datasource-columnconfiguration-fieldmappings
            '''
            result = self._values.get("field_mappings")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DataSourceToIndexFieldMappingProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ColumnConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.ConfluenceAttachmentConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "attachment_field_mappings": "attachmentFieldMappings",
            "crawl_attachments": "crawlAttachments",
        },
    )
    class ConfluenceAttachmentConfigurationProperty:
        def __init__(
            self,
            *,
            attachment_field_mappings: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.ConfluenceAttachmentToIndexFieldMappingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            crawl_attachments: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
        ) -> None:
            '''Configuration of attachment settings for the Confluence data source.

            Attachment settings are optional, if you don't specify settings attachments, Amazon Kendra won't index them.

            :param attachment_field_mappings: Maps attributes or field names of Confluence attachments to Amazon Kendra index field names. To create custom fields, use the ``UpdateIndex`` API before you map to Confluence fields. For more information, see `Mapping data source fields <https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html>`_ . The Confluence data source field names must exist in your Confluence custom metadata. If you specify the ``AttachentFieldMappings`` parameter, you must specify at least one field mapping.
            :param crawl_attachments: ``TRUE`` to index attachments of pages and blogs in Confluence.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceattachmentconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                confluence_attachment_configuration_property = kendra.CfnDataSource.ConfluenceAttachmentConfigurationProperty(
                    attachment_field_mappings=[kendra.CfnDataSource.ConfluenceAttachmentToIndexFieldMappingProperty(
                        data_source_field_name="dataSourceFieldName",
                        index_field_name="indexFieldName",
                
                        # the properties below are optional
                        date_field_format="dateFieldFormat"
                    )],
                    crawl_attachments=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__576b8ee36295a821c5bb667a8a07e11843fc9c1b04276e3f72b11c096b9d21f7)
                check_type(argname="argument attachment_field_mappings", value=attachment_field_mappings, expected_type=type_hints["attachment_field_mappings"])
                check_type(argname="argument crawl_attachments", value=crawl_attachments, expected_type=type_hints["crawl_attachments"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if attachment_field_mappings is not None:
                self._values["attachment_field_mappings"] = attachment_field_mappings
            if crawl_attachments is not None:
                self._values["crawl_attachments"] = crawl_attachments

        @builtins.property
        def attachment_field_mappings(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.ConfluenceAttachmentToIndexFieldMappingProperty"]]]]:
            '''Maps attributes or field names of Confluence attachments to Amazon Kendra index field names.

            To create custom fields, use the ``UpdateIndex`` API before you map to Confluence fields. For more information, see `Mapping data source fields <https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html>`_ . The Confluence data source field names must exist in your Confluence custom metadata.

            If you specify the ``AttachentFieldMappings`` parameter, you must specify at least one field mapping.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceattachmentconfiguration.html#cfn-kendra-datasource-confluenceattachmentconfiguration-attachmentfieldmappings
            '''
            result = self._values.get("attachment_field_mappings")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.ConfluenceAttachmentToIndexFieldMappingProperty"]]]], result)

        @builtins.property
        def crawl_attachments(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''``TRUE`` to index attachments of pages and blogs in Confluence.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceattachmentconfiguration.html#cfn-kendra-datasource-confluenceattachmentconfiguration-crawlattachments
            '''
            result = self._values.get("crawl_attachments")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfluenceAttachmentConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.ConfluenceAttachmentToIndexFieldMappingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_source_field_name": "dataSourceFieldName",
            "index_field_name": "indexFieldName",
            "date_field_format": "dateFieldFormat",
        },
    )
    class ConfluenceAttachmentToIndexFieldMappingProperty:
        def __init__(
            self,
            *,
            data_source_field_name: builtins.str,
            index_field_name: builtins.str,
            date_field_format: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Maps attributes or field names of Confluence attachments to Amazon Kendra index field names.

            To create custom fields, use the ``UpdateIndex`` API before you map to Confluence fields. For more information, see `Mapping data source fields <https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html>`_ . The Confuence data source field names must exist in your Confluence custom metadata.

            :param data_source_field_name: The name of the field in the data source. You must first create the index field using the ``UpdateIndex`` API.
            :param index_field_name: The name of the index field to map to the Confluence data source field. The index field type must match the Confluence field type.
            :param date_field_format: The format for date fields in the data source. If the field specified in ``DataSourceFieldName`` is a date field you must specify the date format. If the field is not a date field, an exception is thrown.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceattachmenttoindexfieldmapping.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                confluence_attachment_to_index_field_mapping_property = kendra.CfnDataSource.ConfluenceAttachmentToIndexFieldMappingProperty(
                    data_source_field_name="dataSourceFieldName",
                    index_field_name="indexFieldName",
                
                    # the properties below are optional
                    date_field_format="dateFieldFormat"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__924f1647295b2a1a10fde56627c68fad198d23c1d234f6f60c8ebbfaeb285e22)
                check_type(argname="argument data_source_field_name", value=data_source_field_name, expected_type=type_hints["data_source_field_name"])
                check_type(argname="argument index_field_name", value=index_field_name, expected_type=type_hints["index_field_name"])
                check_type(argname="argument date_field_format", value=date_field_format, expected_type=type_hints["date_field_format"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "data_source_field_name": data_source_field_name,
                "index_field_name": index_field_name,
            }
            if date_field_format is not None:
                self._values["date_field_format"] = date_field_format

        @builtins.property
        def data_source_field_name(self) -> builtins.str:
            '''The name of the field in the data source.

            You must first create the index field using the ``UpdateIndex`` API.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceattachmenttoindexfieldmapping.html#cfn-kendra-datasource-confluenceattachmenttoindexfieldmapping-datasourcefieldname
            '''
            result = self._values.get("data_source_field_name")
            assert result is not None, "Required property 'data_source_field_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def index_field_name(self) -> builtins.str:
            '''The name of the index field to map to the Confluence data source field.

            The index field type must match the Confluence field type.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceattachmenttoindexfieldmapping.html#cfn-kendra-datasource-confluenceattachmenttoindexfieldmapping-indexfieldname
            '''
            result = self._values.get("index_field_name")
            assert result is not None, "Required property 'index_field_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def date_field_format(self) -> typing.Optional[builtins.str]:
            '''The format for date fields in the data source.

            If the field specified in ``DataSourceFieldName`` is a date field you must specify the date format. If the field is not a date field, an exception is thrown.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceattachmenttoindexfieldmapping.html#cfn-kendra-datasource-confluenceattachmenttoindexfieldmapping-datefieldformat
            '''
            result = self._values.get("date_field_format")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfluenceAttachmentToIndexFieldMappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.ConfluenceBlogConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"blog_field_mappings": "blogFieldMappings"},
    )
    class ConfluenceBlogConfigurationProperty:
        def __init__(
            self,
            *,
            blog_field_mappings: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.ConfluenceBlogToIndexFieldMappingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Configuration of blog settings for the Confluence data source.

            Blogs are always indexed unless filtered from the index by the ``ExclusionPatterns`` or ``InclusionPatterns`` fields in the ``ConfluenceConfiguration`` object.

            :param blog_field_mappings: Maps attributes or field names of Confluence blogs to Amazon Kendra index field names. To create custom fields, use the ``UpdateIndex`` API before you map to Confluence fields. For more information, see `Mapping data source fields <https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html>`_ . The Confluence data source field names must exist in your Confluence custom metadata. If you specify the ``BlogFieldMappings`` parameter, you must specify at least one field mapping.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceblogconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                confluence_blog_configuration_property = kendra.CfnDataSource.ConfluenceBlogConfigurationProperty(
                    blog_field_mappings=[kendra.CfnDataSource.ConfluenceBlogToIndexFieldMappingProperty(
                        data_source_field_name="dataSourceFieldName",
                        index_field_name="indexFieldName",
                
                        # the properties below are optional
                        date_field_format="dateFieldFormat"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4e96f9bee1cf4ee733165b93e2b27bb37c131f402774b3276869e5167bfefbd7)
                check_type(argname="argument blog_field_mappings", value=blog_field_mappings, expected_type=type_hints["blog_field_mappings"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if blog_field_mappings is not None:
                self._values["blog_field_mappings"] = blog_field_mappings

        @builtins.property
        def blog_field_mappings(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.ConfluenceBlogToIndexFieldMappingProperty"]]]]:
            '''Maps attributes or field names of Confluence blogs to Amazon Kendra index field names.

            To create custom fields, use the ``UpdateIndex`` API before you map to Confluence fields. For more information, see `Mapping data source fields <https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html>`_ . The Confluence data source field names must exist in your Confluence custom metadata.

            If you specify the ``BlogFieldMappings`` parameter, you must specify at least one field mapping.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceblogconfiguration.html#cfn-kendra-datasource-confluenceblogconfiguration-blogfieldmappings
            '''
            result = self._values.get("blog_field_mappings")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.ConfluenceBlogToIndexFieldMappingProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfluenceBlogConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.ConfluenceBlogToIndexFieldMappingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_source_field_name": "dataSourceFieldName",
            "index_field_name": "indexFieldName",
            "date_field_format": "dateFieldFormat",
        },
    )
    class ConfluenceBlogToIndexFieldMappingProperty:
        def __init__(
            self,
            *,
            data_source_field_name: builtins.str,
            index_field_name: builtins.str,
            date_field_format: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Maps attributes or field names of Confluence blog to Amazon Kendra index field names.

            To create custom fields, use the ``UpdateIndex`` API before you map to Confluence fields. For more information, see `Mapping data source fields <https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html>`_ . The Confluence data source field names must exist in your Confluence custom metadata.

            :param data_source_field_name: The name of the field in the data source.
            :param index_field_name: The name of the index field to map to the Confluence data source field. The index field type must match the Confluence field type.
            :param date_field_format: The format for date fields in the data source. If the field specified in ``DataSourceFieldName`` is a date field you must specify the date format. If the field is not a date field, an exception is thrown.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceblogtoindexfieldmapping.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                confluence_blog_to_index_field_mapping_property = kendra.CfnDataSource.ConfluenceBlogToIndexFieldMappingProperty(
                    data_source_field_name="dataSourceFieldName",
                    index_field_name="indexFieldName",
                
                    # the properties below are optional
                    date_field_format="dateFieldFormat"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__83889ceeb258388b75d723227b3d33ab0585a0e337895a366822c883ec3d09f9)
                check_type(argname="argument data_source_field_name", value=data_source_field_name, expected_type=type_hints["data_source_field_name"])
                check_type(argname="argument index_field_name", value=index_field_name, expected_type=type_hints["index_field_name"])
                check_type(argname="argument date_field_format", value=date_field_format, expected_type=type_hints["date_field_format"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "data_source_field_name": data_source_field_name,
                "index_field_name": index_field_name,
            }
            if date_field_format is not None:
                self._values["date_field_format"] = date_field_format

        @builtins.property
        def data_source_field_name(self) -> builtins.str:
            '''The name of the field in the data source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceblogtoindexfieldmapping.html#cfn-kendra-datasource-confluenceblogtoindexfieldmapping-datasourcefieldname
            '''
            result = self._values.get("data_source_field_name")
            assert result is not None, "Required property 'data_source_field_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def index_field_name(self) -> builtins.str:
            '''The name of the index field to map to the Confluence data source field.

            The index field type must match the Confluence field type.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceblogtoindexfieldmapping.html#cfn-kendra-datasource-confluenceblogtoindexfieldmapping-indexfieldname
            '''
            result = self._values.get("index_field_name")
            assert result is not None, "Required property 'index_field_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def date_field_format(self) -> typing.Optional[builtins.str]:
            '''The format for date fields in the data source.

            If the field specified in ``DataSourceFieldName`` is a date field you must specify the date format. If the field is not a date field, an exception is thrown.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceblogtoindexfieldmapping.html#cfn-kendra-datasource-confluenceblogtoindexfieldmapping-datefieldformat
            '''
            result = self._values.get("date_field_format")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfluenceBlogToIndexFieldMappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.ConfluenceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "secret_arn": "secretArn",
            "server_url": "serverUrl",
            "version": "version",
            "attachment_configuration": "attachmentConfiguration",
            "blog_configuration": "blogConfiguration",
            "exclusion_patterns": "exclusionPatterns",
            "inclusion_patterns": "inclusionPatterns",
            "page_configuration": "pageConfiguration",
            "space_configuration": "spaceConfiguration",
            "vpc_configuration": "vpcConfiguration",
        },
    )
    class ConfluenceConfigurationProperty:
        def __init__(
            self,
            *,
            secret_arn: builtins.str,
            server_url: builtins.str,
            version: builtins.str,
            attachment_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.ConfluenceAttachmentConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            blog_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.ConfluenceBlogConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            exclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
            inclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
            page_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.ConfluencePageConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            space_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.ConfluenceSpaceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            vpc_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.DataSourceVpcConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Provides the configuration information to connect to Confluence as your data source.

            :param secret_arn: The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains the user name and password required to connect to the Confluence instance. If you use Confluence Cloud, you use a generated API token as the password. You can also provide authentication credentials in the form of a personal access token. For more information, see `Using a Confluence data source <https://docs.aws.amazon.com/kendra/latest/dg/data-source-confluence.html>`_ .
            :param server_url: The URL of your Confluence instance. Use the full URL of the server. For example, *https://server.example.com:port/* . You can also use an IP address, for example, *https://192.168.1.113/* .
            :param version: The version or the type of Confluence installation to connect to.
            :param attachment_configuration: Configuration information for indexing attachments to Confluence blogs and pages.
            :param blog_configuration: Configuration information for indexing Confluence blogs.
            :param exclusion_patterns: A list of regular expression patterns to exclude certain blog posts, pages, spaces, or attachments in your Confluence. Content that matches the patterns are excluded from the index. Content that doesn't match the patterns is included in the index. If content matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the content isn't included in the index.
            :param inclusion_patterns: A list of regular expression patterns to include certain blog posts, pages, spaces, or attachments in your Confluence. Content that matches the patterns are included in the index. Content that doesn't match the patterns is excluded from the index. If content matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the content isn't included in the index.
            :param page_configuration: Configuration information for indexing Confluence pages.
            :param space_configuration: Configuration information for indexing Confluence spaces.
            :param vpc_configuration: Configuration information for an Amazon Virtual Private Cloud to connect to your Confluence. For more information, see `Configuring a VPC <https://docs.aws.amazon.com/kendra/latest/dg/vpc-configuration.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                confluence_configuration_property = kendra.CfnDataSource.ConfluenceConfigurationProperty(
                    secret_arn="secretArn",
                    server_url="serverUrl",
                    version="version",
                
                    # the properties below are optional
                    attachment_configuration=kendra.CfnDataSource.ConfluenceAttachmentConfigurationProperty(
                        attachment_field_mappings=[kendra.CfnDataSource.ConfluenceAttachmentToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
                
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )],
                        crawl_attachments=False
                    ),
                    blog_configuration=kendra.CfnDataSource.ConfluenceBlogConfigurationProperty(
                        blog_field_mappings=[kendra.CfnDataSource.ConfluenceBlogToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
                
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )]
                    ),
                    exclusion_patterns=["exclusionPatterns"],
                    inclusion_patterns=["inclusionPatterns"],
                    page_configuration=kendra.CfnDataSource.ConfluencePageConfigurationProperty(
                        page_field_mappings=[kendra.CfnDataSource.ConfluencePageToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
                
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )]
                    ),
                    space_configuration=kendra.CfnDataSource.ConfluenceSpaceConfigurationProperty(
                        crawl_archived_spaces=False,
                        crawl_personal_spaces=False,
                        exclude_spaces=["excludeSpaces"],
                        include_spaces=["includeSpaces"],
                        space_field_mappings=[kendra.CfnDataSource.ConfluenceSpaceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
                
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )]
                    ),
                    vpc_configuration=kendra.CfnDataSource.DataSourceVpcConfigurationProperty(
                        security_group_ids=["securityGroupIds"],
                        subnet_ids=["subnetIds"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fca3cb4b2908265aa9bc6b4fe6f5b07c7676954bc521475def0ec3c71bb84571)
                check_type(argname="argument secret_arn", value=secret_arn, expected_type=type_hints["secret_arn"])
                check_type(argname="argument server_url", value=server_url, expected_type=type_hints["server_url"])
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
                check_type(argname="argument attachment_configuration", value=attachment_configuration, expected_type=type_hints["attachment_configuration"])
                check_type(argname="argument blog_configuration", value=blog_configuration, expected_type=type_hints["blog_configuration"])
                check_type(argname="argument exclusion_patterns", value=exclusion_patterns, expected_type=type_hints["exclusion_patterns"])
                check_type(argname="argument inclusion_patterns", value=inclusion_patterns, expected_type=type_hints["inclusion_patterns"])
                check_type(argname="argument page_configuration", value=page_configuration, expected_type=type_hints["page_configuration"])
                check_type(argname="argument space_configuration", value=space_configuration, expected_type=type_hints["space_configuration"])
                check_type(argname="argument vpc_configuration", value=vpc_configuration, expected_type=type_hints["vpc_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "secret_arn": secret_arn,
                "server_url": server_url,
                "version": version,
            }
            if attachment_configuration is not None:
                self._values["attachment_configuration"] = attachment_configuration
            if blog_configuration is not None:
                self._values["blog_configuration"] = blog_configuration
            if exclusion_patterns is not None:
                self._values["exclusion_patterns"] = exclusion_patterns
            if inclusion_patterns is not None:
                self._values["inclusion_patterns"] = inclusion_patterns
            if page_configuration is not None:
                self._values["page_configuration"] = page_configuration
            if space_configuration is not None:
                self._values["space_configuration"] = space_configuration
            if vpc_configuration is not None:
                self._values["vpc_configuration"] = vpc_configuration

        @builtins.property
        def secret_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains the user name and password required to connect to the Confluence instance.

            If you use Confluence Cloud, you use a generated API token as the password.

            You can also provide authentication credentials in the form of a personal access token. For more information, see `Using a Confluence data source <https://docs.aws.amazon.com/kendra/latest/dg/data-source-confluence.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceconfiguration.html#cfn-kendra-datasource-confluenceconfiguration-secretarn
            '''
            result = self._values.get("secret_arn")
            assert result is not None, "Required property 'secret_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def server_url(self) -> builtins.str:
            '''The URL of your Confluence instance.

            Use the full URL of the server. For example, *https://server.example.com:port/* . You can also use an IP address, for example, *https://192.168.1.113/* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceconfiguration.html#cfn-kendra-datasource-confluenceconfiguration-serverurl
            '''
            result = self._values.get("server_url")
            assert result is not None, "Required property 'server_url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def version(self) -> builtins.str:
            '''The version or the type of Confluence installation to connect to.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceconfiguration.html#cfn-kendra-datasource-confluenceconfiguration-version
            '''
            result = self._values.get("version")
            assert result is not None, "Required property 'version' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def attachment_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.ConfluenceAttachmentConfigurationProperty"]]:
            '''Configuration information for indexing attachments to Confluence blogs and pages.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceconfiguration.html#cfn-kendra-datasource-confluenceconfiguration-attachmentconfiguration
            '''
            result = self._values.get("attachment_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.ConfluenceAttachmentConfigurationProperty"]], result)

        @builtins.property
        def blog_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.ConfluenceBlogConfigurationProperty"]]:
            '''Configuration information for indexing Confluence blogs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceconfiguration.html#cfn-kendra-datasource-confluenceconfiguration-blogconfiguration
            '''
            result = self._values.get("blog_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.ConfluenceBlogConfigurationProperty"]], result)

        @builtins.property
        def exclusion_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of regular expression patterns to exclude certain blog posts, pages, spaces, or attachments in your Confluence.

            Content that matches the patterns are excluded from the index. Content that doesn't match the patterns is included in the index. If content matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the content isn't included in the index.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceconfiguration.html#cfn-kendra-datasource-confluenceconfiguration-exclusionpatterns
            '''
            result = self._values.get("exclusion_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def inclusion_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of regular expression patterns to include certain blog posts, pages, spaces, or attachments in your Confluence.

            Content that matches the patterns are included in the index. Content that doesn't match the patterns is excluded from the index. If content matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the content isn't included in the index.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceconfiguration.html#cfn-kendra-datasource-confluenceconfiguration-inclusionpatterns
            '''
            result = self._values.get("inclusion_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def page_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.ConfluencePageConfigurationProperty"]]:
            '''Configuration information for indexing Confluence pages.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceconfiguration.html#cfn-kendra-datasource-confluenceconfiguration-pageconfiguration
            '''
            result = self._values.get("page_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.ConfluencePageConfigurationProperty"]], result)

        @builtins.property
        def space_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.ConfluenceSpaceConfigurationProperty"]]:
            '''Configuration information for indexing Confluence spaces.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceconfiguration.html#cfn-kendra-datasource-confluenceconfiguration-spaceconfiguration
            '''
            result = self._values.get("space_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.ConfluenceSpaceConfigurationProperty"]], result)

        @builtins.property
        def vpc_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DataSourceVpcConfigurationProperty"]]:
            '''Configuration information for an Amazon Virtual Private Cloud to connect to your Confluence.

            For more information, see `Configuring a VPC <https://docs.aws.amazon.com/kendra/latest/dg/vpc-configuration.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluenceconfiguration.html#cfn-kendra-datasource-confluenceconfiguration-vpcconfiguration
            '''
            result = self._values.get("vpc_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DataSourceVpcConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfluenceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.ConfluencePageConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"page_field_mappings": "pageFieldMappings"},
    )
    class ConfluencePageConfigurationProperty:
        def __init__(
            self,
            *,
            page_field_mappings: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.ConfluencePageToIndexFieldMappingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Configuration of the page settings for the Confluence data source.

            :param page_field_mappings: Maps attributes or field names of Confluence pages to Amazon Kendra index field names. To create custom fields, use the ``UpdateIndex`` API before you map to Confluence fields. For more information, see `Mapping data source fields <https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html>`_ . The Confluence data source field names must exist in your Confluence custom metadata. If you specify the ``PageFieldMappings`` parameter, you must specify at least one field mapping.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencepageconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                confluence_page_configuration_property = kendra.CfnDataSource.ConfluencePageConfigurationProperty(
                    page_field_mappings=[kendra.CfnDataSource.ConfluencePageToIndexFieldMappingProperty(
                        data_source_field_name="dataSourceFieldName",
                        index_field_name="indexFieldName",
                
                        # the properties below are optional
                        date_field_format="dateFieldFormat"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f52527a9371fa1296e788de62cf40b198d363bee9da4c3419b813307b2cbf18a)
                check_type(argname="argument page_field_mappings", value=page_field_mappings, expected_type=type_hints["page_field_mappings"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if page_field_mappings is not None:
                self._values["page_field_mappings"] = page_field_mappings

        @builtins.property
        def page_field_mappings(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.ConfluencePageToIndexFieldMappingProperty"]]]]:
            '''Maps attributes or field names of Confluence pages to Amazon Kendra index field names.

            To create custom fields, use the ``UpdateIndex`` API before you map to Confluence fields. For more information, see `Mapping data source fields <https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html>`_ . The Confluence data source field names must exist in your Confluence custom metadata.

            If you specify the ``PageFieldMappings`` parameter, you must specify at least one field mapping.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencepageconfiguration.html#cfn-kendra-datasource-confluencepageconfiguration-pagefieldmappings
            '''
            result = self._values.get("page_field_mappings")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.ConfluencePageToIndexFieldMappingProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfluencePageConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.ConfluencePageToIndexFieldMappingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_source_field_name": "dataSourceFieldName",
            "index_field_name": "indexFieldName",
            "date_field_format": "dateFieldFormat",
        },
    )
    class ConfluencePageToIndexFieldMappingProperty:
        def __init__(
            self,
            *,
            data_source_field_name: builtins.str,
            index_field_name: builtins.str,
            date_field_format: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Maps attributes or field names of Confluence pages to Amazon Kendra index field names.

            To create custom fields, use the ``UpdateIndex`` API before you map to Confluence fields. For more information, see `Mapping data source fields <https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html>`_ . The Confluence data source field names must exist in your Confluence custom metadata.

            :param data_source_field_name: The name of the field in the data source.
            :param index_field_name: The name of the index field to map to the Confluence data source field. The index field type must match the Confluence field type.
            :param date_field_format: The format for date fields in the data source. If the field specified in ``DataSourceFieldName`` is a date field you must specify the date format. If the field is not a date field, an exception is thrown.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencepagetoindexfieldmapping.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                confluence_page_to_index_field_mapping_property = kendra.CfnDataSource.ConfluencePageToIndexFieldMappingProperty(
                    data_source_field_name="dataSourceFieldName",
                    index_field_name="indexFieldName",
                
                    # the properties below are optional
                    date_field_format="dateFieldFormat"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cefb7b06cc4104fdf1232f556342ec672704be92bc80771f6cd506c89eaba2c0)
                check_type(argname="argument data_source_field_name", value=data_source_field_name, expected_type=type_hints["data_source_field_name"])
                check_type(argname="argument index_field_name", value=index_field_name, expected_type=type_hints["index_field_name"])
                check_type(argname="argument date_field_format", value=date_field_format, expected_type=type_hints["date_field_format"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "data_source_field_name": data_source_field_name,
                "index_field_name": index_field_name,
            }
            if date_field_format is not None:
                self._values["date_field_format"] = date_field_format

        @builtins.property
        def data_source_field_name(self) -> builtins.str:
            '''The name of the field in the data source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencepagetoindexfieldmapping.html#cfn-kendra-datasource-confluencepagetoindexfieldmapping-datasourcefieldname
            '''
            result = self._values.get("data_source_field_name")
            assert result is not None, "Required property 'data_source_field_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def index_field_name(self) -> builtins.str:
            '''The name of the index field to map to the Confluence data source field.

            The index field type must match the Confluence field type.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencepagetoindexfieldmapping.html#cfn-kendra-datasource-confluencepagetoindexfieldmapping-indexfieldname
            '''
            result = self._values.get("index_field_name")
            assert result is not None, "Required property 'index_field_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def date_field_format(self) -> typing.Optional[builtins.str]:
            '''The format for date fields in the data source.

            If the field specified in ``DataSourceFieldName`` is a date field you must specify the date format. If the field is not a date field, an exception is thrown.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencepagetoindexfieldmapping.html#cfn-kendra-datasource-confluencepagetoindexfieldmapping-datefieldformat
            '''
            result = self._values.get("date_field_format")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfluencePageToIndexFieldMappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.ConfluenceSpaceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "crawl_archived_spaces": "crawlArchivedSpaces",
            "crawl_personal_spaces": "crawlPersonalSpaces",
            "exclude_spaces": "excludeSpaces",
            "include_spaces": "includeSpaces",
            "space_field_mappings": "spaceFieldMappings",
        },
    )
    class ConfluenceSpaceConfigurationProperty:
        def __init__(
            self,
            *,
            crawl_archived_spaces: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            crawl_personal_spaces: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            exclude_spaces: typing.Optional[typing.Sequence[builtins.str]] = None,
            include_spaces: typing.Optional[typing.Sequence[builtins.str]] = None,
            space_field_mappings: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.ConfluenceSpaceToIndexFieldMappingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Configuration information for indexing Confluence spaces.

            :param crawl_archived_spaces: ``TRUE`` to index archived spaces.
            :param crawl_personal_spaces: ``TRUE`` to index personal spaces. You can add restrictions to items in personal spaces. If personal spaces are indexed, queries without user context information may return restricted items from a personal space in their results. For more information, see `Filtering on user context <https://docs.aws.amazon.com/kendra/latest/dg/user-context-filter.html>`_ .
            :param exclude_spaces: A list of space keys of Confluence spaces. If you include a key, the blogs, documents, and attachments in the space are not indexed. If a space is in both the ``ExcludeSpaces`` and the ``IncludeSpaces`` list, the space is excluded.
            :param include_spaces: A list of space keys for Confluence spaces. If you include a key, the blogs, documents, and attachments in the space are indexed. Spaces that aren't in the list aren't indexed. A space in the list must exist. Otherwise, Amazon Kendra logs an error when the data source is synchronized. If a space is in both the ``IncludeSpaces`` and the ``ExcludeSpaces`` list, the space is excluded.
            :param space_field_mappings: Maps attributes or field names of Confluence spaces to Amazon Kendra index field names. To create custom fields, use the ``UpdateIndex`` API before you map to Confluence fields. For more information, see `Mapping data source fields <https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html>`_ . The Confluence data source field names must exist in your Confluence custom metadata. If you specify the ``SpaceFieldMappings`` parameter, you must specify at least one field mapping.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespaceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                confluence_space_configuration_property = kendra.CfnDataSource.ConfluenceSpaceConfigurationProperty(
                    crawl_archived_spaces=False,
                    crawl_personal_spaces=False,
                    exclude_spaces=["excludeSpaces"],
                    include_spaces=["includeSpaces"],
                    space_field_mappings=[kendra.CfnDataSource.ConfluenceSpaceToIndexFieldMappingProperty(
                        data_source_field_name="dataSourceFieldName",
                        index_field_name="indexFieldName",
                
                        # the properties below are optional
                        date_field_format="dateFieldFormat"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__edd6e444142fccf1e08d99868266ec9724c486c19845a128da9b7a4bf2c2ab01)
                check_type(argname="argument crawl_archived_spaces", value=crawl_archived_spaces, expected_type=type_hints["crawl_archived_spaces"])
                check_type(argname="argument crawl_personal_spaces", value=crawl_personal_spaces, expected_type=type_hints["crawl_personal_spaces"])
                check_type(argname="argument exclude_spaces", value=exclude_spaces, expected_type=type_hints["exclude_spaces"])
                check_type(argname="argument include_spaces", value=include_spaces, expected_type=type_hints["include_spaces"])
                check_type(argname="argument space_field_mappings", value=space_field_mappings, expected_type=type_hints["space_field_mappings"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if crawl_archived_spaces is not None:
                self._values["crawl_archived_spaces"] = crawl_archived_spaces
            if crawl_personal_spaces is not None:
                self._values["crawl_personal_spaces"] = crawl_personal_spaces
            if exclude_spaces is not None:
                self._values["exclude_spaces"] = exclude_spaces
            if include_spaces is not None:
                self._values["include_spaces"] = include_spaces
            if space_field_mappings is not None:
                self._values["space_field_mappings"] = space_field_mappings

        @builtins.property
        def crawl_archived_spaces(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''``TRUE`` to index archived spaces.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespaceconfiguration.html#cfn-kendra-datasource-confluencespaceconfiguration-crawlarchivedspaces
            '''
            result = self._values.get("crawl_archived_spaces")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def crawl_personal_spaces(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''``TRUE`` to index personal spaces.

            You can add restrictions to items in personal spaces. If personal spaces are indexed, queries without user context information may return restricted items from a personal space in their results. For more information, see `Filtering on user context <https://docs.aws.amazon.com/kendra/latest/dg/user-context-filter.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespaceconfiguration.html#cfn-kendra-datasource-confluencespaceconfiguration-crawlpersonalspaces
            '''
            result = self._values.get("crawl_personal_spaces")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def exclude_spaces(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of space keys of Confluence spaces.

            If you include a key, the blogs, documents, and attachments in the space are not indexed. If a space is in both the ``ExcludeSpaces`` and the ``IncludeSpaces`` list, the space is excluded.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespaceconfiguration.html#cfn-kendra-datasource-confluencespaceconfiguration-excludespaces
            '''
            result = self._values.get("exclude_spaces")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def include_spaces(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of space keys for Confluence spaces.

            If you include a key, the blogs, documents, and attachments in the space are indexed. Spaces that aren't in the list aren't indexed. A space in the list must exist. Otherwise, Amazon Kendra logs an error when the data source is synchronized. If a space is in both the ``IncludeSpaces`` and the ``ExcludeSpaces`` list, the space is excluded.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespaceconfiguration.html#cfn-kendra-datasource-confluencespaceconfiguration-includespaces
            '''
            result = self._values.get("include_spaces")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def space_field_mappings(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.ConfluenceSpaceToIndexFieldMappingProperty"]]]]:
            '''Maps attributes or field names of Confluence spaces to Amazon Kendra index field names.

            To create custom fields, use the ``UpdateIndex`` API before you map to Confluence fields. For more information, see `Mapping data source fields <https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html>`_ . The Confluence data source field names must exist in your Confluence custom metadata.

            If you specify the ``SpaceFieldMappings`` parameter, you must specify at least one field mapping.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespaceconfiguration.html#cfn-kendra-datasource-confluencespaceconfiguration-spacefieldmappings
            '''
            result = self._values.get("space_field_mappings")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.ConfluenceSpaceToIndexFieldMappingProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfluenceSpaceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.ConfluenceSpaceToIndexFieldMappingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_source_field_name": "dataSourceFieldName",
            "index_field_name": "indexFieldName",
            "date_field_format": "dateFieldFormat",
        },
    )
    class ConfluenceSpaceToIndexFieldMappingProperty:
        def __init__(
            self,
            *,
            data_source_field_name: builtins.str,
            index_field_name: builtins.str,
            date_field_format: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Maps attributes or field names of Confluence spaces to Amazon Kendra index field names.

            To create custom fields, use the ``UpdateIndex`` API before you map to Confluence fields. For more information, see `Mapping data source fields <https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html>`_ . The Confluence data source field names must exist in your Confluence custom metadata.

            :param data_source_field_name: The name of the field in the data source.
            :param index_field_name: The name of the index field to map to the Confluence data source field. The index field type must match the Confluence field type.
            :param date_field_format: The format for date fields in the data source. If the field specified in ``DataSourceFieldName`` is a date field you must specify the date format. If the field is not a date field, an exception is thrown.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespacetoindexfieldmapping.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                confluence_space_to_index_field_mapping_property = kendra.CfnDataSource.ConfluenceSpaceToIndexFieldMappingProperty(
                    data_source_field_name="dataSourceFieldName",
                    index_field_name="indexFieldName",
                
                    # the properties below are optional
                    date_field_format="dateFieldFormat"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4b38c3f2c7089b2621bd2e26fbd653f6703cb11453a622c5e9e8d151159ff3ba)
                check_type(argname="argument data_source_field_name", value=data_source_field_name, expected_type=type_hints["data_source_field_name"])
                check_type(argname="argument index_field_name", value=index_field_name, expected_type=type_hints["index_field_name"])
                check_type(argname="argument date_field_format", value=date_field_format, expected_type=type_hints["date_field_format"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "data_source_field_name": data_source_field_name,
                "index_field_name": index_field_name,
            }
            if date_field_format is not None:
                self._values["date_field_format"] = date_field_format

        @builtins.property
        def data_source_field_name(self) -> builtins.str:
            '''The name of the field in the data source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespacetoindexfieldmapping.html#cfn-kendra-datasource-confluencespacetoindexfieldmapping-datasourcefieldname
            '''
            result = self._values.get("data_source_field_name")
            assert result is not None, "Required property 'data_source_field_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def index_field_name(self) -> builtins.str:
            '''The name of the index field to map to the Confluence data source field.

            The index field type must match the Confluence field type.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespacetoindexfieldmapping.html#cfn-kendra-datasource-confluencespacetoindexfieldmapping-indexfieldname
            '''
            result = self._values.get("index_field_name")
            assert result is not None, "Required property 'index_field_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def date_field_format(self) -> typing.Optional[builtins.str]:
            '''The format for date fields in the data source.

            If the field specified in ``DataSourceFieldName`` is a date field you must specify the date format. If the field is not a date field, an exception is thrown.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-confluencespacetoindexfieldmapping.html#cfn-kendra-datasource-confluencespacetoindexfieldmapping-datefieldformat
            '''
            result = self._values.get("date_field_format")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfluenceSpaceToIndexFieldMappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.ConnectionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "database_host": "databaseHost",
            "database_name": "databaseName",
            "database_port": "databasePort",
            "secret_arn": "secretArn",
            "table_name": "tableName",
        },
    )
    class ConnectionConfigurationProperty:
        def __init__(
            self,
            *,
            database_host: builtins.str,
            database_name: builtins.str,
            database_port: jsii.Number,
            secret_arn: builtins.str,
            table_name: builtins.str,
        ) -> None:
            '''Provides the configuration information that's required to connect to a database.

            :param database_host: The name of the host for the database. Can be either a string (host.subdomain.domain.tld) or an IPv4 or IPv6 address.
            :param database_name: The name of the database containing the document data.
            :param database_port: The port that the database uses for connections.
            :param secret_arn: The Amazon Resource Name (ARN) of credentials stored in AWS Secrets Manager . The credentials should be a user/password pair. For more information, see `Using a Database Data Source <https://docs.aws.amazon.com/kendra/latest/dg/data-source-database.html>`_ . For more information about AWS Secrets Manager , see `What Is AWS Secrets Manager <https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html>`_ in the *AWS Secrets Manager* user guide.
            :param table_name: The name of the table that contains the document data.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-connectionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                connection_configuration_property = kendra.CfnDataSource.ConnectionConfigurationProperty(
                    database_host="databaseHost",
                    database_name="databaseName",
                    database_port=123,
                    secret_arn="secretArn",
                    table_name="tableName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__56480e4f803090fe216ded0da076620b1903a28234eddb142f3c8ea0edd716cb)
                check_type(argname="argument database_host", value=database_host, expected_type=type_hints["database_host"])
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument database_port", value=database_port, expected_type=type_hints["database_port"])
                check_type(argname="argument secret_arn", value=secret_arn, expected_type=type_hints["secret_arn"])
                check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "database_host": database_host,
                "database_name": database_name,
                "database_port": database_port,
                "secret_arn": secret_arn,
                "table_name": table_name,
            }

        @builtins.property
        def database_host(self) -> builtins.str:
            '''The name of the host for the database.

            Can be either a string (host.subdomain.domain.tld) or an IPv4 or IPv6 address.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-connectionconfiguration.html#cfn-kendra-datasource-connectionconfiguration-databasehost
            '''
            result = self._values.get("database_host")
            assert result is not None, "Required property 'database_host' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def database_name(self) -> builtins.str:
            '''The name of the database containing the document data.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-connectionconfiguration.html#cfn-kendra-datasource-connectionconfiguration-databasename
            '''
            result = self._values.get("database_name")
            assert result is not None, "Required property 'database_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def database_port(self) -> jsii.Number:
            '''The port that the database uses for connections.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-connectionconfiguration.html#cfn-kendra-datasource-connectionconfiguration-databaseport
            '''
            result = self._values.get("database_port")
            assert result is not None, "Required property 'database_port' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def secret_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of credentials stored in AWS Secrets Manager .

            The credentials should be a user/password pair. For more information, see `Using a Database Data Source <https://docs.aws.amazon.com/kendra/latest/dg/data-source-database.html>`_ . For more information about AWS Secrets Manager , see `What Is AWS Secrets Manager <https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html>`_ in the *AWS Secrets Manager* user guide.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-connectionconfiguration.html#cfn-kendra-datasource-connectionconfiguration-secretarn
            '''
            result = self._values.get("secret_arn")
            assert result is not None, "Required property 'secret_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def table_name(self) -> builtins.str:
            '''The name of the table that contains the document data.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-connectionconfiguration.html#cfn-kendra-datasource-connectionconfiguration-tablename
            '''
            result = self._values.get("table_name")
            assert result is not None, "Required property 'table_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConnectionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.CustomDocumentEnrichmentConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "inline_configurations": "inlineConfigurations",
            "post_extraction_hook_configuration": "postExtractionHookConfiguration",
            "pre_extraction_hook_configuration": "preExtractionHookConfiguration",
            "role_arn": "roleArn",
        },
    )
    class CustomDocumentEnrichmentConfigurationProperty:
        def __init__(
            self,
            *,
            inline_configurations: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.InlineCustomDocumentEnrichmentConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            post_extraction_hook_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.HookConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            pre_extraction_hook_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.HookConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            role_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides the configuration information for altering document metadata and content during the document ingestion process.

            For more information, see `Customizing document metadata during the ingestion process <https://docs.aws.amazon.com/kendra/latest/dg/custom-document-enrichment.html>`_ .

            :param inline_configurations: Configuration information to alter document attributes or metadata fields and content when ingesting documents into Amazon Kendra.
            :param post_extraction_hook_configuration: Configuration information for invoking a Lambda function in AWS Lambda on the structured documents with their metadata and text extracted. You can use a Lambda function to apply advanced logic for creating, modifying, or deleting document metadata and content. For more information, see `Advanced data manipulation <https://docs.aws.amazon.com/kendra/latest/dg/custom-document-enrichment.html#advanced-data-manipulation>`_ .
            :param pre_extraction_hook_configuration: Configuration information for invoking a Lambda function in AWS Lambda on the original or raw documents before extracting their metadata and text. You can use a Lambda function to apply advanced logic for creating, modifying, or deleting document metadata and content. For more information, see `Advanced data manipulation <https://docs.aws.amazon.com/kendra/latest/dg/custom-document-enrichment.html#advanced-data-manipulation>`_ .
            :param role_arn: The Amazon Resource Name (ARN) of a role with permission to run ``PreExtractionHookConfiguration`` and ``PostExtractionHookConfiguration`` for altering document metadata and content during the document ingestion process. For more information, see `IAM roles for Amazon Kendra <https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-customdocumentenrichmentconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                custom_document_enrichment_configuration_property = kendra.CfnDataSource.CustomDocumentEnrichmentConfigurationProperty(
                    inline_configurations=[kendra.CfnDataSource.InlineCustomDocumentEnrichmentConfigurationProperty(
                        condition=kendra.CfnDataSource.DocumentAttributeConditionProperty(
                            condition_document_attribute_key="conditionDocumentAttributeKey",
                            operator="operator",
                
                            # the properties below are optional
                            condition_on_value=kendra.CfnDataSource.DocumentAttributeValueProperty(
                                date_value="dateValue",
                                long_value=123,
                                string_list_value=["stringListValue"],
                                string_value="stringValue"
                            )
                        ),
                        document_content_deletion=False,
                        target=kendra.CfnDataSource.DocumentAttributeTargetProperty(
                            target_document_attribute_key="targetDocumentAttributeKey",
                
                            # the properties below are optional
                            target_document_attribute_value=kendra.CfnDataSource.DocumentAttributeValueProperty(
                                date_value="dateValue",
                                long_value=123,
                                string_list_value=["stringListValue"],
                                string_value="stringValue"
                            ),
                            target_document_attribute_value_deletion=False
                        )
                    )],
                    post_extraction_hook_configuration=kendra.CfnDataSource.HookConfigurationProperty(
                        lambda_arn="lambdaArn",
                        s3_bucket="s3Bucket",
                
                        # the properties below are optional
                        invocation_condition=kendra.CfnDataSource.DocumentAttributeConditionProperty(
                            condition_document_attribute_key="conditionDocumentAttributeKey",
                            operator="operator",
                
                            # the properties below are optional
                            condition_on_value=kendra.CfnDataSource.DocumentAttributeValueProperty(
                                date_value="dateValue",
                                long_value=123,
                                string_list_value=["stringListValue"],
                                string_value="stringValue"
                            )
                        )
                    ),
                    pre_extraction_hook_configuration=kendra.CfnDataSource.HookConfigurationProperty(
                        lambda_arn="lambdaArn",
                        s3_bucket="s3Bucket",
                
                        # the properties below are optional
                        invocation_condition=kendra.CfnDataSource.DocumentAttributeConditionProperty(
                            condition_document_attribute_key="conditionDocumentAttributeKey",
                            operator="operator",
                
                            # the properties below are optional
                            condition_on_value=kendra.CfnDataSource.DocumentAttributeValueProperty(
                                date_value="dateValue",
                                long_value=123,
                                string_list_value=["stringListValue"],
                                string_value="stringValue"
                            )
                        )
                    ),
                    role_arn="roleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1fcf90f5571479a5ff85f931922498d973d08d8feb15738ac9bcf68f032398ec)
                check_type(argname="argument inline_configurations", value=inline_configurations, expected_type=type_hints["inline_configurations"])
                check_type(argname="argument post_extraction_hook_configuration", value=post_extraction_hook_configuration, expected_type=type_hints["post_extraction_hook_configuration"])
                check_type(argname="argument pre_extraction_hook_configuration", value=pre_extraction_hook_configuration, expected_type=type_hints["pre_extraction_hook_configuration"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if inline_configurations is not None:
                self._values["inline_configurations"] = inline_configurations
            if post_extraction_hook_configuration is not None:
                self._values["post_extraction_hook_configuration"] = post_extraction_hook_configuration
            if pre_extraction_hook_configuration is not None:
                self._values["pre_extraction_hook_configuration"] = pre_extraction_hook_configuration
            if role_arn is not None:
                self._values["role_arn"] = role_arn

        @builtins.property
        def inline_configurations(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.InlineCustomDocumentEnrichmentConfigurationProperty"]]]]:
            '''Configuration information to alter document attributes or metadata fields and content when ingesting documents into Amazon Kendra.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-customdocumentenrichmentconfiguration.html#cfn-kendra-datasource-customdocumentenrichmentconfiguration-inlineconfigurations
            '''
            result = self._values.get("inline_configurations")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.InlineCustomDocumentEnrichmentConfigurationProperty"]]]], result)

        @builtins.property
        def post_extraction_hook_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.HookConfigurationProperty"]]:
            '''Configuration information for invoking a Lambda function in AWS Lambda on the structured documents with their metadata and text extracted.

            You can use a Lambda function to apply advanced logic for creating, modifying, or deleting document metadata and content. For more information, see `Advanced data manipulation <https://docs.aws.amazon.com/kendra/latest/dg/custom-document-enrichment.html#advanced-data-manipulation>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-customdocumentenrichmentconfiguration.html#cfn-kendra-datasource-customdocumentenrichmentconfiguration-postextractionhookconfiguration
            '''
            result = self._values.get("post_extraction_hook_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.HookConfigurationProperty"]], result)

        @builtins.property
        def pre_extraction_hook_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.HookConfigurationProperty"]]:
            '''Configuration information for invoking a Lambda function in AWS Lambda on the original or raw documents before extracting their metadata and text.

            You can use a Lambda function to apply advanced logic for creating, modifying, or deleting document metadata and content. For more information, see `Advanced data manipulation <https://docs.aws.amazon.com/kendra/latest/dg/custom-document-enrichment.html#advanced-data-manipulation>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-customdocumentenrichmentconfiguration.html#cfn-kendra-datasource-customdocumentenrichmentconfiguration-preextractionhookconfiguration
            '''
            result = self._values.get("pre_extraction_hook_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.HookConfigurationProperty"]], result)

        @builtins.property
        def role_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of a role with permission to run ``PreExtractionHookConfiguration`` and ``PostExtractionHookConfiguration`` for altering document metadata and content during the document ingestion process.

            For more information, see `IAM roles for Amazon Kendra <https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-customdocumentenrichmentconfiguration.html#cfn-kendra-datasource-customdocumentenrichmentconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomDocumentEnrichmentConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.DataSourceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "confluence_configuration": "confluenceConfiguration",
            "database_configuration": "databaseConfiguration",
            "google_drive_configuration": "googleDriveConfiguration",
            "one_drive_configuration": "oneDriveConfiguration",
            "s3_configuration": "s3Configuration",
            "salesforce_configuration": "salesforceConfiguration",
            "service_now_configuration": "serviceNowConfiguration",
            "share_point_configuration": "sharePointConfiguration",
            "web_crawler_configuration": "webCrawlerConfiguration",
            "work_docs_configuration": "workDocsConfiguration",
        },
    )
    class DataSourceConfigurationProperty:
        def __init__(
            self,
            *,
            confluence_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.ConfluenceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            database_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.DatabaseConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            google_drive_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.GoogleDriveConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            one_drive_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.OneDriveConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.S3DataSourceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            salesforce_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.SalesforceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            service_now_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.ServiceNowConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            share_point_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.SharePointConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            web_crawler_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.WebCrawlerConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            work_docs_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.WorkDocsConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Provides the configuration information for an Amazon Kendra data source.

            :param confluence_configuration: Provides the configuration information to connect to Confluence as your data source.
            :param database_configuration: Provides the configuration information to connect to a database as your data source.
            :param google_drive_configuration: Provides the configuration information to connect to Google Drive as your data source.
            :param one_drive_configuration: Provides the configuration information to connect to Microsoft OneDrive as your data source.
            :param s3_configuration: Provides the configuration information to connect to an Amazon S3 bucket as your data source.
            :param salesforce_configuration: Provides the configuration information to connect to Salesforce as your data source.
            :param service_now_configuration: Provides the configuration information to connect to ServiceNow as your data source.
            :param share_point_configuration: Provides the configuration information to connect to Microsoft SharePoint as your data source.
            :param web_crawler_configuration: Provides the configuration information required for Amazon Kendra Web Crawler.
            :param work_docs_configuration: Provides the configuration information to connect to Amazon WorkDocs as your data source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                data_source_configuration_property = kendra.CfnDataSource.DataSourceConfigurationProperty(
                    confluence_configuration=kendra.CfnDataSource.ConfluenceConfigurationProperty(
                        secret_arn="secretArn",
                        server_url="serverUrl",
                        version="version",
                
                        # the properties below are optional
                        attachment_configuration=kendra.CfnDataSource.ConfluenceAttachmentConfigurationProperty(
                            attachment_field_mappings=[kendra.CfnDataSource.ConfluenceAttachmentToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
                
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )],
                            crawl_attachments=False
                        ),
                        blog_configuration=kendra.CfnDataSource.ConfluenceBlogConfigurationProperty(
                            blog_field_mappings=[kendra.CfnDataSource.ConfluenceBlogToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
                
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )]
                        ),
                        exclusion_patterns=["exclusionPatterns"],
                        inclusion_patterns=["inclusionPatterns"],
                        page_configuration=kendra.CfnDataSource.ConfluencePageConfigurationProperty(
                            page_field_mappings=[kendra.CfnDataSource.ConfluencePageToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
                
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )]
                        ),
                        space_configuration=kendra.CfnDataSource.ConfluenceSpaceConfigurationProperty(
                            crawl_archived_spaces=False,
                            crawl_personal_spaces=False,
                            exclude_spaces=["excludeSpaces"],
                            include_spaces=["includeSpaces"],
                            space_field_mappings=[kendra.CfnDataSource.ConfluenceSpaceToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
                
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )]
                        ),
                        vpc_configuration=kendra.CfnDataSource.DataSourceVpcConfigurationProperty(
                            security_group_ids=["securityGroupIds"],
                            subnet_ids=["subnetIds"]
                        )
                    ),
                    database_configuration=kendra.CfnDataSource.DatabaseConfigurationProperty(
                        column_configuration=kendra.CfnDataSource.ColumnConfigurationProperty(
                            change_detecting_columns=["changeDetectingColumns"],
                            document_data_column_name="documentDataColumnName",
                            document_id_column_name="documentIdColumnName",
                
                            # the properties below are optional
                            document_title_column_name="documentTitleColumnName",
                            field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
                
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )]
                        ),
                        connection_configuration=kendra.CfnDataSource.ConnectionConfigurationProperty(
                            database_host="databaseHost",
                            database_name="databaseName",
                            database_port=123,
                            secret_arn="secretArn",
                            table_name="tableName"
                        ),
                        database_engine_type="databaseEngineType",
                
                        # the properties below are optional
                        acl_configuration=kendra.CfnDataSource.AclConfigurationProperty(
                            allowed_groups_column_name="allowedGroupsColumnName"
                        ),
                        sql_configuration=kendra.CfnDataSource.SqlConfigurationProperty(
                            query_identifiers_enclosing_option="queryIdentifiersEnclosingOption"
                        ),
                        vpc_configuration=kendra.CfnDataSource.DataSourceVpcConfigurationProperty(
                            security_group_ids=["securityGroupIds"],
                            subnet_ids=["subnetIds"]
                        )
                    ),
                    google_drive_configuration=kendra.CfnDataSource.GoogleDriveConfigurationProperty(
                        secret_arn="secretArn",
                
                        # the properties below are optional
                        exclude_mime_types=["excludeMimeTypes"],
                        exclude_shared_drives=["excludeSharedDrives"],
                        exclude_user_accounts=["excludeUserAccounts"],
                        exclusion_patterns=["exclusionPatterns"],
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
                
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )],
                        inclusion_patterns=["inclusionPatterns"]
                    ),
                    one_drive_configuration=kendra.CfnDataSource.OneDriveConfigurationProperty(
                        one_drive_users=kendra.CfnDataSource.OneDriveUsersProperty(
                            one_drive_user_list=["oneDriveUserList"],
                            one_drive_user_s3_path=kendra.CfnDataSource.S3PathProperty(
                                bucket="bucket",
                                key="key"
                            )
                        ),
                        secret_arn="secretArn",
                        tenant_domain="tenantDomain",
                
                        # the properties below are optional
                        disable_local_groups=False,
                        exclusion_patterns=["exclusionPatterns"],
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
                
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )],
                        inclusion_patterns=["inclusionPatterns"]
                    ),
                    s3_configuration=kendra.CfnDataSource.S3DataSourceConfigurationProperty(
                        bucket_name="bucketName",
                
                        # the properties below are optional
                        access_control_list_configuration=kendra.CfnDataSource.AccessControlListConfigurationProperty(
                            key_path="keyPath"
                        ),
                        documents_metadata_configuration=kendra.CfnDataSource.DocumentsMetadataConfigurationProperty(
                            s3_prefix="s3Prefix"
                        ),
                        exclusion_patterns=["exclusionPatterns"],
                        inclusion_patterns=["inclusionPatterns"],
                        inclusion_prefixes=["inclusionPrefixes"]
                    ),
                    salesforce_configuration=kendra.CfnDataSource.SalesforceConfigurationProperty(
                        secret_arn="secretArn",
                        server_url="serverUrl",
                
                        # the properties below are optional
                        chatter_feed_configuration=kendra.CfnDataSource.SalesforceChatterFeedConfigurationProperty(
                            document_data_field_name="documentDataFieldName",
                
                            # the properties below are optional
                            document_title_field_name="documentTitleFieldName",
                            field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
                
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )],
                            include_filter_types=["includeFilterTypes"]
                        ),
                        crawl_attachments=False,
                        exclude_attachment_file_patterns=["excludeAttachmentFilePatterns"],
                        include_attachment_file_patterns=["includeAttachmentFilePatterns"],
                        knowledge_article_configuration=kendra.CfnDataSource.SalesforceKnowledgeArticleConfigurationProperty(
                            included_states=["includedStates"],
                
                            # the properties below are optional
                            custom_knowledge_article_type_configurations=[kendra.CfnDataSource.SalesforceCustomKnowledgeArticleTypeConfigurationProperty(
                                document_data_field_name="documentDataFieldName",
                                name="name",
                
                                # the properties below are optional
                                document_title_field_name="documentTitleFieldName",
                                field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                                    data_source_field_name="dataSourceFieldName",
                                    index_field_name="indexFieldName",
                
                                    # the properties below are optional
                                    date_field_format="dateFieldFormat"
                                )]
                            )],
                            standard_knowledge_article_type_configuration=kendra.CfnDataSource.SalesforceStandardKnowledgeArticleTypeConfigurationProperty(
                                document_data_field_name="documentDataFieldName",
                
                                # the properties below are optional
                                document_title_field_name="documentTitleFieldName",
                                field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                                    data_source_field_name="dataSourceFieldName",
                                    index_field_name="indexFieldName",
                
                                    # the properties below are optional
                                    date_field_format="dateFieldFormat"
                                )]
                            )
                        ),
                        standard_object_attachment_configuration=kendra.CfnDataSource.SalesforceStandardObjectAttachmentConfigurationProperty(
                            document_title_field_name="documentTitleFieldName",
                            field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
                
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )]
                        ),
                        standard_object_configurations=[kendra.CfnDataSource.SalesforceStandardObjectConfigurationProperty(
                            document_data_field_name="documentDataFieldName",
                            name="name",
                
                            # the properties below are optional
                            document_title_field_name="documentTitleFieldName",
                            field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
                
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )]
                        )]
                    ),
                    service_now_configuration=kendra.CfnDataSource.ServiceNowConfigurationProperty(
                        host_url="hostUrl",
                        secret_arn="secretArn",
                        service_now_build_version="serviceNowBuildVersion",
                
                        # the properties below are optional
                        authentication_type="authenticationType",
                        knowledge_article_configuration=kendra.CfnDataSource.ServiceNowKnowledgeArticleConfigurationProperty(
                            document_data_field_name="documentDataFieldName",
                
                            # the properties below are optional
                            crawl_attachments=False,
                            document_title_field_name="documentTitleFieldName",
                            exclude_attachment_file_patterns=["excludeAttachmentFilePatterns"],
                            field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
                
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )],
                            filter_query="filterQuery",
                            include_attachment_file_patterns=["includeAttachmentFilePatterns"]
                        ),
                        service_catalog_configuration=kendra.CfnDataSource.ServiceNowServiceCatalogConfigurationProperty(
                            document_data_field_name="documentDataFieldName",
                
                            # the properties below are optional
                            crawl_attachments=False,
                            document_title_field_name="documentTitleFieldName",
                            exclude_attachment_file_patterns=["excludeAttachmentFilePatterns"],
                            field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
                
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )],
                            include_attachment_file_patterns=["includeAttachmentFilePatterns"]
                        )
                    ),
                    share_point_configuration=kendra.CfnDataSource.SharePointConfigurationProperty(
                        secret_arn="secretArn",
                        share_point_version="sharePointVersion",
                        urls=["urls"],
                
                        # the properties below are optional
                        crawl_attachments=False,
                        disable_local_groups=False,
                        document_title_field_name="documentTitleFieldName",
                        exclusion_patterns=["exclusionPatterns"],
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
                
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )],
                        inclusion_patterns=["inclusionPatterns"],
                        ssl_certificate_s3_path=kendra.CfnDataSource.S3PathProperty(
                            bucket="bucket",
                            key="key"
                        ),
                        use_change_log=False,
                        vpc_configuration=kendra.CfnDataSource.DataSourceVpcConfigurationProperty(
                            security_group_ids=["securityGroupIds"],
                            subnet_ids=["subnetIds"]
                        )
                    ),
                    web_crawler_configuration=kendra.CfnDataSource.WebCrawlerConfigurationProperty(
                        urls=kendra.CfnDataSource.WebCrawlerUrlsProperty(
                            seed_url_configuration=kendra.CfnDataSource.WebCrawlerSeedUrlConfigurationProperty(
                                seed_urls=["seedUrls"],
                
                                # the properties below are optional
                                web_crawler_mode="webCrawlerMode"
                            ),
                            site_maps_configuration=kendra.CfnDataSource.WebCrawlerSiteMapsConfigurationProperty(
                                site_maps=["siteMaps"]
                            )
                        ),
                
                        # the properties below are optional
                        authentication_configuration=kendra.CfnDataSource.WebCrawlerAuthenticationConfigurationProperty(
                            basic_authentication=[kendra.CfnDataSource.WebCrawlerBasicAuthenticationProperty(
                                credentials="credentials",
                                host="host",
                                port=123
                            )]
                        ),
                        crawl_depth=123,
                        max_content_size_per_page_in_mega_bytes=123,
                        max_links_per_page=123,
                        max_urls_per_minute_crawl_rate=123,
                        proxy_configuration=kendra.CfnDataSource.ProxyConfigurationProperty(
                            host="host",
                            port=123,
                
                            # the properties below are optional
                            credentials="credentials"
                        ),
                        url_exclusion_patterns=["urlExclusionPatterns"],
                        url_inclusion_patterns=["urlInclusionPatterns"]
                    ),
                    work_docs_configuration=kendra.CfnDataSource.WorkDocsConfigurationProperty(
                        organization_id="organizationId",
                
                        # the properties below are optional
                        crawl_comments=False,
                        exclusion_patterns=["exclusionPatterns"],
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
                
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )],
                        inclusion_patterns=["inclusionPatterns"],
                        use_change_log=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2cd8e584e6fbffd547c6f97fa7016cd6ac83b70f5d2bb3ef5b4740e4311dc129)
                check_type(argname="argument confluence_configuration", value=confluence_configuration, expected_type=type_hints["confluence_configuration"])
                check_type(argname="argument database_configuration", value=database_configuration, expected_type=type_hints["database_configuration"])
                check_type(argname="argument google_drive_configuration", value=google_drive_configuration, expected_type=type_hints["google_drive_configuration"])
                check_type(argname="argument one_drive_configuration", value=one_drive_configuration, expected_type=type_hints["one_drive_configuration"])
                check_type(argname="argument s3_configuration", value=s3_configuration, expected_type=type_hints["s3_configuration"])
                check_type(argname="argument salesforce_configuration", value=salesforce_configuration, expected_type=type_hints["salesforce_configuration"])
                check_type(argname="argument service_now_configuration", value=service_now_configuration, expected_type=type_hints["service_now_configuration"])
                check_type(argname="argument share_point_configuration", value=share_point_configuration, expected_type=type_hints["share_point_configuration"])
                check_type(argname="argument web_crawler_configuration", value=web_crawler_configuration, expected_type=type_hints["web_crawler_configuration"])
                check_type(argname="argument work_docs_configuration", value=work_docs_configuration, expected_type=type_hints["work_docs_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if confluence_configuration is not None:
                self._values["confluence_configuration"] = confluence_configuration
            if database_configuration is not None:
                self._values["database_configuration"] = database_configuration
            if google_drive_configuration is not None:
                self._values["google_drive_configuration"] = google_drive_configuration
            if one_drive_configuration is not None:
                self._values["one_drive_configuration"] = one_drive_configuration
            if s3_configuration is not None:
                self._values["s3_configuration"] = s3_configuration
            if salesforce_configuration is not None:
                self._values["salesforce_configuration"] = salesforce_configuration
            if service_now_configuration is not None:
                self._values["service_now_configuration"] = service_now_configuration
            if share_point_configuration is not None:
                self._values["share_point_configuration"] = share_point_configuration
            if web_crawler_configuration is not None:
                self._values["web_crawler_configuration"] = web_crawler_configuration
            if work_docs_configuration is not None:
                self._values["work_docs_configuration"] = work_docs_configuration

        @builtins.property
        def confluence_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.ConfluenceConfigurationProperty"]]:
            '''Provides the configuration information to connect to Confluence as your data source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourceconfiguration.html#cfn-kendra-datasource-datasourceconfiguration-confluenceconfiguration
            '''
            result = self._values.get("confluence_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.ConfluenceConfigurationProperty"]], result)

        @builtins.property
        def database_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DatabaseConfigurationProperty"]]:
            '''Provides the configuration information to connect to a database as your data source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourceconfiguration.html#cfn-kendra-datasource-datasourceconfiguration-databaseconfiguration
            '''
            result = self._values.get("database_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DatabaseConfigurationProperty"]], result)

        @builtins.property
        def google_drive_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.GoogleDriveConfigurationProperty"]]:
            '''Provides the configuration information to connect to Google Drive as your data source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourceconfiguration.html#cfn-kendra-datasource-datasourceconfiguration-googledriveconfiguration
            '''
            result = self._values.get("google_drive_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.GoogleDriveConfigurationProperty"]], result)

        @builtins.property
        def one_drive_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.OneDriveConfigurationProperty"]]:
            '''Provides the configuration information to connect to Microsoft OneDrive as your data source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourceconfiguration.html#cfn-kendra-datasource-datasourceconfiguration-onedriveconfiguration
            '''
            result = self._values.get("one_drive_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.OneDriveConfigurationProperty"]], result)

        @builtins.property
        def s3_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.S3DataSourceConfigurationProperty"]]:
            '''Provides the configuration information to connect to an Amazon S3 bucket as your data source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourceconfiguration.html#cfn-kendra-datasource-datasourceconfiguration-s3configuration
            '''
            result = self._values.get("s3_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.S3DataSourceConfigurationProperty"]], result)

        @builtins.property
        def salesforce_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.SalesforceConfigurationProperty"]]:
            '''Provides the configuration information to connect to Salesforce as your data source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourceconfiguration.html#cfn-kendra-datasource-datasourceconfiguration-salesforceconfiguration
            '''
            result = self._values.get("salesforce_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.SalesforceConfigurationProperty"]], result)

        @builtins.property
        def service_now_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.ServiceNowConfigurationProperty"]]:
            '''Provides the configuration information to connect to ServiceNow as your data source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourceconfiguration.html#cfn-kendra-datasource-datasourceconfiguration-servicenowconfiguration
            '''
            result = self._values.get("service_now_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.ServiceNowConfigurationProperty"]], result)

        @builtins.property
        def share_point_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.SharePointConfigurationProperty"]]:
            '''Provides the configuration information to connect to Microsoft SharePoint as your data source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourceconfiguration.html#cfn-kendra-datasource-datasourceconfiguration-sharepointconfiguration
            '''
            result = self._values.get("share_point_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.SharePointConfigurationProperty"]], result)

        @builtins.property
        def web_crawler_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.WebCrawlerConfigurationProperty"]]:
            '''Provides the configuration information required for Amazon Kendra Web Crawler.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourceconfiguration.html#cfn-kendra-datasource-datasourceconfiguration-webcrawlerconfiguration
            '''
            result = self._values.get("web_crawler_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.WebCrawlerConfigurationProperty"]], result)

        @builtins.property
        def work_docs_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.WorkDocsConfigurationProperty"]]:
            '''Provides the configuration information to connect to Amazon WorkDocs as your data source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourceconfiguration.html#cfn-kendra-datasource-datasourceconfiguration-workdocsconfiguration
            '''
            result = self._values.get("work_docs_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.WorkDocsConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataSourceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_source_field_name": "dataSourceFieldName",
            "index_field_name": "indexFieldName",
            "date_field_format": "dateFieldFormat",
        },
    )
    class DataSourceToIndexFieldMappingProperty:
        def __init__(
            self,
            *,
            data_source_field_name: builtins.str,
            index_field_name: builtins.str,
            date_field_format: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Maps a column or attribute in the data source to an index field.

            You must first create the fields in the index using the `UpdateIndex <https://docs.aws.amazon.com/kendra/latest/dg/API_UpdateIndex.html>`_ operation.

            :param data_source_field_name: The name of the column or attribute in the data source.
            :param index_field_name: The name of the field in the index.
            :param date_field_format: The type of data stored in the column or attribute.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourcetoindexfieldmapping.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                data_source_to_index_field_mapping_property = kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                    data_source_field_name="dataSourceFieldName",
                    index_field_name="indexFieldName",
                
                    # the properties below are optional
                    date_field_format="dateFieldFormat"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7d00484f9307c2cbde1ea7c3bffedbbc149e37389717b71abeb14bea3d444404)
                check_type(argname="argument data_source_field_name", value=data_source_field_name, expected_type=type_hints["data_source_field_name"])
                check_type(argname="argument index_field_name", value=index_field_name, expected_type=type_hints["index_field_name"])
                check_type(argname="argument date_field_format", value=date_field_format, expected_type=type_hints["date_field_format"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "data_source_field_name": data_source_field_name,
                "index_field_name": index_field_name,
            }
            if date_field_format is not None:
                self._values["date_field_format"] = date_field_format

        @builtins.property
        def data_source_field_name(self) -> builtins.str:
            '''The name of the column or attribute in the data source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourcetoindexfieldmapping.html#cfn-kendra-datasource-datasourcetoindexfieldmapping-datasourcefieldname
            '''
            result = self._values.get("data_source_field_name")
            assert result is not None, "Required property 'data_source_field_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def index_field_name(self) -> builtins.str:
            '''The name of the field in the index.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourcetoindexfieldmapping.html#cfn-kendra-datasource-datasourcetoindexfieldmapping-indexfieldname
            '''
            result = self._values.get("index_field_name")
            assert result is not None, "Required property 'index_field_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def date_field_format(self) -> typing.Optional[builtins.str]:
            '''The type of data stored in the column or attribute.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourcetoindexfieldmapping.html#cfn-kendra-datasource-datasourcetoindexfieldmapping-datefieldformat
            '''
            result = self._values.get("date_field_format")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataSourceToIndexFieldMappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.DataSourceVpcConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "security_group_ids": "securityGroupIds",
            "subnet_ids": "subnetIds",
        },
    )
    class DataSourceVpcConfigurationProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Sequence[builtins.str],
            subnet_ids: typing.Sequence[builtins.str],
        ) -> None:
            '''Provides the configuration information to connect to an Amazon VPC.

            :param security_group_ids: A list of identifiers of security groups within your Amazon VPC. The security groups should enable Amazon Kendra to connect to the data source.
            :param subnet_ids: A list of identifiers for subnets within your Amazon VPC. The subnets should be able to connect to each other in the VPC, and they should have outgoing access to the Internet through a NAT device.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourcevpcconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                data_source_vpc_configuration_property = kendra.CfnDataSource.DataSourceVpcConfigurationProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8523977b3861a731e172645f9e76e9004b8e82b143f46b2dfb1fac929d0a4001)
                check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
                check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "security_group_ids": security_group_ids,
                "subnet_ids": subnet_ids,
            }

        @builtins.property
        def security_group_ids(self) -> typing.List[builtins.str]:
            '''A list of identifiers of security groups within your Amazon VPC.

            The security groups should enable Amazon Kendra to connect to the data source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourcevpcconfiguration.html#cfn-kendra-datasource-datasourcevpcconfiguration-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            assert result is not None, "Required property 'security_group_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnet_ids(self) -> typing.List[builtins.str]:
            '''A list of identifiers for subnets within your Amazon VPC.

            The subnets should be able to connect to each other in the VPC, and they should have outgoing access to the Internet through a NAT device.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-datasourcevpcconfiguration.html#cfn-kendra-datasource-datasourcevpcconfiguration-subnetids
            '''
            result = self._values.get("subnet_ids")
            assert result is not None, "Required property 'subnet_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataSourceVpcConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.DatabaseConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "column_configuration": "columnConfiguration",
            "connection_configuration": "connectionConfiguration",
            "database_engine_type": "databaseEngineType",
            "acl_configuration": "aclConfiguration",
            "sql_configuration": "sqlConfiguration",
            "vpc_configuration": "vpcConfiguration",
        },
    )
    class DatabaseConfigurationProperty:
        def __init__(
            self,
            *,
            column_configuration: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.ColumnConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            connection_configuration: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.ConnectionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            database_engine_type: builtins.str,
            acl_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.AclConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sql_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.SqlConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            vpc_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.DataSourceVpcConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Provides the configuration information to connect to a index.

            :param column_configuration: Information about where the index should get the document information from the database.
            :param connection_configuration: Configuration information that's required to connect to a database.
            :param database_engine_type: The type of database engine that runs the database.
            :param acl_configuration: Information about the database column that provides information for user context filtering.
            :param sql_configuration: Provides information about how Amazon Kendra uses quote marks around SQL identifiers when querying a database data source.
            :param vpc_configuration: Provides information for connecting to an Amazon VPC.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-databaseconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                database_configuration_property = kendra.CfnDataSource.DatabaseConfigurationProperty(
                    column_configuration=kendra.CfnDataSource.ColumnConfigurationProperty(
                        change_detecting_columns=["changeDetectingColumns"],
                        document_data_column_name="documentDataColumnName",
                        document_id_column_name="documentIdColumnName",
                
                        # the properties below are optional
                        document_title_column_name="documentTitleColumnName",
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
                
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )]
                    ),
                    connection_configuration=kendra.CfnDataSource.ConnectionConfigurationProperty(
                        database_host="databaseHost",
                        database_name="databaseName",
                        database_port=123,
                        secret_arn="secretArn",
                        table_name="tableName"
                    ),
                    database_engine_type="databaseEngineType",
                
                    # the properties below are optional
                    acl_configuration=kendra.CfnDataSource.AclConfigurationProperty(
                        allowed_groups_column_name="allowedGroupsColumnName"
                    ),
                    sql_configuration=kendra.CfnDataSource.SqlConfigurationProperty(
                        query_identifiers_enclosing_option="queryIdentifiersEnclosingOption"
                    ),
                    vpc_configuration=kendra.CfnDataSource.DataSourceVpcConfigurationProperty(
                        security_group_ids=["securityGroupIds"],
                        subnet_ids=["subnetIds"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__625507bf30b92f47de71f7d7cf0d4eca2c026342a700972601ea6ba8bb2cdb4e)
                check_type(argname="argument column_configuration", value=column_configuration, expected_type=type_hints["column_configuration"])
                check_type(argname="argument connection_configuration", value=connection_configuration, expected_type=type_hints["connection_configuration"])
                check_type(argname="argument database_engine_type", value=database_engine_type, expected_type=type_hints["database_engine_type"])
                check_type(argname="argument acl_configuration", value=acl_configuration, expected_type=type_hints["acl_configuration"])
                check_type(argname="argument sql_configuration", value=sql_configuration, expected_type=type_hints["sql_configuration"])
                check_type(argname="argument vpc_configuration", value=vpc_configuration, expected_type=type_hints["vpc_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "column_configuration": column_configuration,
                "connection_configuration": connection_configuration,
                "database_engine_type": database_engine_type,
            }
            if acl_configuration is not None:
                self._values["acl_configuration"] = acl_configuration
            if sql_configuration is not None:
                self._values["sql_configuration"] = sql_configuration
            if vpc_configuration is not None:
                self._values["vpc_configuration"] = vpc_configuration

        @builtins.property
        def column_configuration(
            self,
        ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.ColumnConfigurationProperty"]:
            '''Information about where the index should get the document information from the database.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-databaseconfiguration.html#cfn-kendra-datasource-databaseconfiguration-columnconfiguration
            '''
            result = self._values.get("column_configuration")
            assert result is not None, "Required property 'column_configuration' is missing"
            return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.ColumnConfigurationProperty"], result)

        @builtins.property
        def connection_configuration(
            self,
        ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.ConnectionConfigurationProperty"]:
            '''Configuration information that's required to connect to a database.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-databaseconfiguration.html#cfn-kendra-datasource-databaseconfiguration-connectionconfiguration
            '''
            result = self._values.get("connection_configuration")
            assert result is not None, "Required property 'connection_configuration' is missing"
            return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.ConnectionConfigurationProperty"], result)

        @builtins.property
        def database_engine_type(self) -> builtins.str:
            '''The type of database engine that runs the database.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-databaseconfiguration.html#cfn-kendra-datasource-databaseconfiguration-databaseenginetype
            '''
            result = self._values.get("database_engine_type")
            assert result is not None, "Required property 'database_engine_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def acl_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.AclConfigurationProperty"]]:
            '''Information about the database column that provides information for user context filtering.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-databaseconfiguration.html#cfn-kendra-datasource-databaseconfiguration-aclconfiguration
            '''
            result = self._values.get("acl_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.AclConfigurationProperty"]], result)

        @builtins.property
        def sql_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.SqlConfigurationProperty"]]:
            '''Provides information about how Amazon Kendra uses quote marks around SQL identifiers when querying a database data source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-databaseconfiguration.html#cfn-kendra-datasource-databaseconfiguration-sqlconfiguration
            '''
            result = self._values.get("sql_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.SqlConfigurationProperty"]], result)

        @builtins.property
        def vpc_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DataSourceVpcConfigurationProperty"]]:
            '''Provides information for connecting to an Amazon VPC.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-databaseconfiguration.html#cfn-kendra-datasource-databaseconfiguration-vpcconfiguration
            '''
            result = self._values.get("vpc_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DataSourceVpcConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatabaseConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.DocumentAttributeConditionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "condition_document_attribute_key": "conditionDocumentAttributeKey",
            "operator": "operator",
            "condition_on_value": "conditionOnValue",
        },
    )
    class DocumentAttributeConditionProperty:
        def __init__(
            self,
            *,
            condition_document_attribute_key: builtins.str,
            operator: builtins.str,
            condition_on_value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.DocumentAttributeValueProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The condition used for the target document attribute or metadata field when ingesting documents into Amazon Kendra.

            You use this with `DocumentAttributeTarget to apply the condition <https://docs.aws.amazon.com/kendra/latest/dg/API_DocumentAttributeTarget.html>`_ .

            For example, you can create the 'Department' target field and have it prefill department names associated with the documents based on information in the 'Source_URI' field. Set the condition that if the 'Source_URI' field contains 'financial' in its URI value, then prefill the target field 'Department' with the target value 'Finance' for the document.

            Amazon Kendra cannot create a target field if it has not already been created as an index field. After you create your index field, you can create a document metadata field using ``DocumentAttributeTarget`` . Amazon Kendra then will map your newly created metadata field to your index field.

            :param condition_document_attribute_key: The identifier of the document attribute used for the condition. For example, 'Source_URI' could be an identifier for the attribute or metadata field that contains source URIs associated with the documents. Amazon Kendra currently does not support ``_document_body`` as an attribute key used for the condition.
            :param operator: The condition operator. For example, you can use 'Contains' to partially match a string.
            :param condition_on_value: The value used by the operator. For example, you can specify the value 'financial' for strings in the 'Source_URI' field that partially match or contain this value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentattributecondition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                document_attribute_condition_property = kendra.CfnDataSource.DocumentAttributeConditionProperty(
                    condition_document_attribute_key="conditionDocumentAttributeKey",
                    operator="operator",
                
                    # the properties below are optional
                    condition_on_value=kendra.CfnDataSource.DocumentAttributeValueProperty(
                        date_value="dateValue",
                        long_value=123,
                        string_list_value=["stringListValue"],
                        string_value="stringValue"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__69b7b73760f1787f973dfe93d47b85124d0d77fea803f935b79630e83121e400)
                check_type(argname="argument condition_document_attribute_key", value=condition_document_attribute_key, expected_type=type_hints["condition_document_attribute_key"])
                check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
                check_type(argname="argument condition_on_value", value=condition_on_value, expected_type=type_hints["condition_on_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "condition_document_attribute_key": condition_document_attribute_key,
                "operator": operator,
            }
            if condition_on_value is not None:
                self._values["condition_on_value"] = condition_on_value

        @builtins.property
        def condition_document_attribute_key(self) -> builtins.str:
            '''The identifier of the document attribute used for the condition.

            For example, 'Source_URI' could be an identifier for the attribute or metadata field that contains source URIs associated with the documents.

            Amazon Kendra currently does not support ``_document_body`` as an attribute key used for the condition.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentattributecondition.html#cfn-kendra-datasource-documentattributecondition-conditiondocumentattributekey
            '''
            result = self._values.get("condition_document_attribute_key")
            assert result is not None, "Required property 'condition_document_attribute_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def operator(self) -> builtins.str:
            '''The condition operator.

            For example, you can use 'Contains' to partially match a string.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentattributecondition.html#cfn-kendra-datasource-documentattributecondition-operator
            '''
            result = self._values.get("operator")
            assert result is not None, "Required property 'operator' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def condition_on_value(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DocumentAttributeValueProperty"]]:
            '''The value used by the operator.

            For example, you can specify the value 'financial' for strings in the 'Source_URI' field that partially match or contain this value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentattributecondition.html#cfn-kendra-datasource-documentattributecondition-conditiononvalue
            '''
            result = self._values.get("condition_on_value")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DocumentAttributeValueProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DocumentAttributeConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.DocumentAttributeTargetProperty",
        jsii_struct_bases=[],
        name_mapping={
            "target_document_attribute_key": "targetDocumentAttributeKey",
            "target_document_attribute_value": "targetDocumentAttributeValue",
            "target_document_attribute_value_deletion": "targetDocumentAttributeValueDeletion",
        },
    )
    class DocumentAttributeTargetProperty:
        def __init__(
            self,
            *,
            target_document_attribute_key: builtins.str,
            target_document_attribute_value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.DocumentAttributeValueProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            target_document_attribute_value_deletion: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
        ) -> None:
            '''The target document attribute or metadata field you want to alter when ingesting documents into Amazon Kendra.

            For example, you can delete customer identification numbers associated with the documents, stored in the document metadata field called 'Customer_ID'. You set the target key as 'Customer_ID' and the deletion flag to ``TRUE`` . This removes all customer ID values in the field 'Customer_ID'. This would scrub personally identifiable information from each document's metadata.

            Amazon Kendra cannot create a target field if it has not already been created as an index field. After you create your index field, you can create a document metadata field using ``DocumentAttributeTarget`` . Amazon Kendra then will map your newly created metadata field to your index field.

            You can also use this with `DocumentAttributeCondition <https://docs.aws.amazon.com/kendra/latest/dg/API_DocumentAttributeCondition.html>`_ .

            :param target_document_attribute_key: The identifier of the target document attribute or metadata field. For example, 'Department' could be an identifier for the target attribute or metadata field that includes the department names associated with the documents.
            :param target_document_attribute_value: The target value you want to create for the target attribute. For example, 'Finance' could be the target value for the target attribute key 'Department'.
            :param target_document_attribute_value_deletion: ``TRUE`` to delete the existing target value for your specified target attribute key. You cannot create a target value and set this to ``TRUE`` . To create a target value ( ``TargetDocumentAttributeValue`` ), set this to ``FALSE`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentattributetarget.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                document_attribute_target_property = kendra.CfnDataSource.DocumentAttributeTargetProperty(
                    target_document_attribute_key="targetDocumentAttributeKey",
                
                    # the properties below are optional
                    target_document_attribute_value=kendra.CfnDataSource.DocumentAttributeValueProperty(
                        date_value="dateValue",
                        long_value=123,
                        string_list_value=["stringListValue"],
                        string_value="stringValue"
                    ),
                    target_document_attribute_value_deletion=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__eaf296e383821da4fe186285591f4517cb6e84220ca53820c796e69864b1c7ff)
                check_type(argname="argument target_document_attribute_key", value=target_document_attribute_key, expected_type=type_hints["target_document_attribute_key"])
                check_type(argname="argument target_document_attribute_value", value=target_document_attribute_value, expected_type=type_hints["target_document_attribute_value"])
                check_type(argname="argument target_document_attribute_value_deletion", value=target_document_attribute_value_deletion, expected_type=type_hints["target_document_attribute_value_deletion"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "target_document_attribute_key": target_document_attribute_key,
            }
            if target_document_attribute_value is not None:
                self._values["target_document_attribute_value"] = target_document_attribute_value
            if target_document_attribute_value_deletion is not None:
                self._values["target_document_attribute_value_deletion"] = target_document_attribute_value_deletion

        @builtins.property
        def target_document_attribute_key(self) -> builtins.str:
            '''The identifier of the target document attribute or metadata field.

            For example, 'Department' could be an identifier for the target attribute or metadata field that includes the department names associated with the documents.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentattributetarget.html#cfn-kendra-datasource-documentattributetarget-targetdocumentattributekey
            '''
            result = self._values.get("target_document_attribute_key")
            assert result is not None, "Required property 'target_document_attribute_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def target_document_attribute_value(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DocumentAttributeValueProperty"]]:
            '''The target value you want to create for the target attribute.

            For example, 'Finance' could be the target value for the target attribute key 'Department'.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentattributetarget.html#cfn-kendra-datasource-documentattributetarget-targetdocumentattributevalue
            '''
            result = self._values.get("target_document_attribute_value")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DocumentAttributeValueProperty"]], result)

        @builtins.property
        def target_document_attribute_value_deletion(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''``TRUE`` to delete the existing target value for your specified target attribute key.

            You cannot create a target value and set this to ``TRUE`` . To create a target value ( ``TargetDocumentAttributeValue`` ), set this to ``FALSE`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentattributetarget.html#cfn-kendra-datasource-documentattributetarget-targetdocumentattributevaluedeletion
            '''
            result = self._values.get("target_document_attribute_value_deletion")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DocumentAttributeTargetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.DocumentAttributeValueProperty",
        jsii_struct_bases=[],
        name_mapping={
            "date_value": "dateValue",
            "long_value": "longValue",
            "string_list_value": "stringListValue",
            "string_value": "stringValue",
        },
    )
    class DocumentAttributeValueProperty:
        def __init__(
            self,
            *,
            date_value: typing.Optional[builtins.str] = None,
            long_value: typing.Optional[jsii.Number] = None,
            string_list_value: typing.Optional[typing.Sequence[builtins.str]] = None,
            string_value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The value of a document attribute.

            You can only provide one value for a document attribute.

            :param date_value: A date expressed as an ISO 8601 string. It is important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.
            :param long_value: A long integer value.
            :param string_list_value: A list of strings. The default maximum length or number of strings is 10.
            :param string_value: A string, such as "department".

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentattributevalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                document_attribute_value_property = kendra.CfnDataSource.DocumentAttributeValueProperty(
                    date_value="dateValue",
                    long_value=123,
                    string_list_value=["stringListValue"],
                    string_value="stringValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9bcaff04493a00bb4410de5a6af34399adc1f4f0cc4155e2cacc9d1d836e4423)
                check_type(argname="argument date_value", value=date_value, expected_type=type_hints["date_value"])
                check_type(argname="argument long_value", value=long_value, expected_type=type_hints["long_value"])
                check_type(argname="argument string_list_value", value=string_list_value, expected_type=type_hints["string_list_value"])
                check_type(argname="argument string_value", value=string_value, expected_type=type_hints["string_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if date_value is not None:
                self._values["date_value"] = date_value
            if long_value is not None:
                self._values["long_value"] = long_value
            if string_list_value is not None:
                self._values["string_list_value"] = string_list_value
            if string_value is not None:
                self._values["string_value"] = string_value

        @builtins.property
        def date_value(self) -> typing.Optional[builtins.str]:
            '''A date expressed as an ISO 8601 string.

            It is important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentattributevalue.html#cfn-kendra-datasource-documentattributevalue-datevalue
            '''
            result = self._values.get("date_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def long_value(self) -> typing.Optional[jsii.Number]:
            '''A long integer value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentattributevalue.html#cfn-kendra-datasource-documentattributevalue-longvalue
            '''
            result = self._values.get("long_value")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def string_list_value(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of strings.

            The default maximum length or number of strings is 10.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentattributevalue.html#cfn-kendra-datasource-documentattributevalue-stringlistvalue
            '''
            result = self._values.get("string_list_value")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def string_value(self) -> typing.Optional[builtins.str]:
            '''A string, such as "department".

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentattributevalue.html#cfn-kendra-datasource-documentattributevalue-stringvalue
            '''
            result = self._values.get("string_value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DocumentAttributeValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.DocumentsMetadataConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_prefix": "s3Prefix"},
    )
    class DocumentsMetadataConfigurationProperty:
        def __init__(self, *, s3_prefix: typing.Optional[builtins.str] = None) -> None:
            '''Document metadata files that contain information such as the document access control information, source URI, document author, and custom attributes.

            Each metadata file contains metadata about a single document.

            :param s3_prefix: A prefix used to filter metadata configuration files in the AWS S3 bucket. The S3 bucket might contain multiple metadata files. Use ``S3Prefix`` to include only the desired metadata files.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentsmetadataconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                documents_metadata_configuration_property = kendra.CfnDataSource.DocumentsMetadataConfigurationProperty(
                    s3_prefix="s3Prefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__aadc60e4754fe87872d1e909f86b0e2be2f500ba62bcddac35bc70a7f0f5cd65)
                check_type(argname="argument s3_prefix", value=s3_prefix, expected_type=type_hints["s3_prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if s3_prefix is not None:
                self._values["s3_prefix"] = s3_prefix

        @builtins.property
        def s3_prefix(self) -> typing.Optional[builtins.str]:
            '''A prefix used to filter metadata configuration files in the AWS S3 bucket.

            The S3 bucket might contain multiple metadata files. Use ``S3Prefix`` to include only the desired metadata files.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-documentsmetadataconfiguration.html#cfn-kendra-datasource-documentsmetadataconfiguration-s3prefix
            '''
            result = self._values.get("s3_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DocumentsMetadataConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.GoogleDriveConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "secret_arn": "secretArn",
            "exclude_mime_types": "excludeMimeTypes",
            "exclude_shared_drives": "excludeSharedDrives",
            "exclude_user_accounts": "excludeUserAccounts",
            "exclusion_patterns": "exclusionPatterns",
            "field_mappings": "fieldMappings",
            "inclusion_patterns": "inclusionPatterns",
        },
    )
    class GoogleDriveConfigurationProperty:
        def __init__(
            self,
            *,
            secret_arn: builtins.str,
            exclude_mime_types: typing.Optional[typing.Sequence[builtins.str]] = None,
            exclude_shared_drives: typing.Optional[typing.Sequence[builtins.str]] = None,
            exclude_user_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
            exclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
            field_mappings: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            inclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Provides the configuration information to connect to Google Drive as your data source.

            :param secret_arn: The Amazon Resource Name (ARN) of a AWS Secrets Manager secret that contains the credentials required to connect to Google Drive. For more information, see `Using a Google Workspace Drive data source <https://docs.aws.amazon.com/kendra/latest/dg/data-source-google-drive.html>`_ .
            :param exclude_mime_types: A list of MIME types to exclude from the index. All documents matching the specified MIME type are excluded. For a list of MIME types, see `Using a Google Workspace Drive data source <https://docs.aws.amazon.com/kendra/latest/dg/data-source-google-drive.html>`_ .
            :param exclude_shared_drives: A list of identifiers or shared drives to exclude from the index. All files and folders stored on the shared drive are excluded.
            :param exclude_user_accounts: A list of email addresses of the users. Documents owned by these users are excluded from the index. Documents shared with excluded users are indexed unless they are excluded in another way.
            :param exclusion_patterns: A list of regular expression patterns to exclude certain items in your Google Drive, including shared drives and users' My Drives. Items that match the patterns are excluded from the index. Items that don't match the patterns are included in the index. If an item matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the item isn't included in the index.
            :param field_mappings: Maps Google Drive data source attributes or field names to Amazon Kendra index field names. To create custom fields, use the ``UpdateIndex`` API before you map to Google Drive fields. For more information, see `Mapping data source fields <https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html>`_ . The Google Drive data source field names must exist in your Google Drive custom metadata.
            :param inclusion_patterns: A list of regular expression patterns to include certain items in your Google Drive, including shared drives and users' My Drives. Items that match the patterns are included in the index. Items that don't match the patterns are excluded from the index. If an item matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the item isn't included in the index.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-googledriveconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                google_drive_configuration_property = kendra.CfnDataSource.GoogleDriveConfigurationProperty(
                    secret_arn="secretArn",
                
                    # the properties below are optional
                    exclude_mime_types=["excludeMimeTypes"],
                    exclude_shared_drives=["excludeSharedDrives"],
                    exclude_user_accounts=["excludeUserAccounts"],
                    exclusion_patterns=["exclusionPatterns"],
                    field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                        data_source_field_name="dataSourceFieldName",
                        index_field_name="indexFieldName",
                
                        # the properties below are optional
                        date_field_format="dateFieldFormat"
                    )],
                    inclusion_patterns=["inclusionPatterns"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e8658af633ed7b37e5f45f8e2d3286bbe3ea33d5e931c8e79390eb7e91cd27b3)
                check_type(argname="argument secret_arn", value=secret_arn, expected_type=type_hints["secret_arn"])
                check_type(argname="argument exclude_mime_types", value=exclude_mime_types, expected_type=type_hints["exclude_mime_types"])
                check_type(argname="argument exclude_shared_drives", value=exclude_shared_drives, expected_type=type_hints["exclude_shared_drives"])
                check_type(argname="argument exclude_user_accounts", value=exclude_user_accounts, expected_type=type_hints["exclude_user_accounts"])
                check_type(argname="argument exclusion_patterns", value=exclusion_patterns, expected_type=type_hints["exclusion_patterns"])
                check_type(argname="argument field_mappings", value=field_mappings, expected_type=type_hints["field_mappings"])
                check_type(argname="argument inclusion_patterns", value=inclusion_patterns, expected_type=type_hints["inclusion_patterns"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "secret_arn": secret_arn,
            }
            if exclude_mime_types is not None:
                self._values["exclude_mime_types"] = exclude_mime_types
            if exclude_shared_drives is not None:
                self._values["exclude_shared_drives"] = exclude_shared_drives
            if exclude_user_accounts is not None:
                self._values["exclude_user_accounts"] = exclude_user_accounts
            if exclusion_patterns is not None:
                self._values["exclusion_patterns"] = exclusion_patterns
            if field_mappings is not None:
                self._values["field_mappings"] = field_mappings
            if inclusion_patterns is not None:
                self._values["inclusion_patterns"] = inclusion_patterns

        @builtins.property
        def secret_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of a AWS Secrets Manager secret that contains the credentials required to connect to Google Drive.

            For more information, see `Using a Google Workspace Drive data source <https://docs.aws.amazon.com/kendra/latest/dg/data-source-google-drive.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-googledriveconfiguration.html#cfn-kendra-datasource-googledriveconfiguration-secretarn
            '''
            result = self._values.get("secret_arn")
            assert result is not None, "Required property 'secret_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def exclude_mime_types(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of MIME types to exclude from the index. All documents matching the specified MIME type are excluded.

            For a list of MIME types, see `Using a Google Workspace Drive data source <https://docs.aws.amazon.com/kendra/latest/dg/data-source-google-drive.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-googledriveconfiguration.html#cfn-kendra-datasource-googledriveconfiguration-excludemimetypes
            '''
            result = self._values.get("exclude_mime_types")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def exclude_shared_drives(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of identifiers or shared drives to exclude from the index.

            All files and folders stored on the shared drive are excluded.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-googledriveconfiguration.html#cfn-kendra-datasource-googledriveconfiguration-excludeshareddrives
            '''
            result = self._values.get("exclude_shared_drives")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def exclude_user_accounts(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of email addresses of the users.

            Documents owned by these users are excluded from the index. Documents shared with excluded users are indexed unless they are excluded in another way.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-googledriveconfiguration.html#cfn-kendra-datasource-googledriveconfiguration-excludeuseraccounts
            '''
            result = self._values.get("exclude_user_accounts")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def exclusion_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of regular expression patterns to exclude certain items in your Google Drive, including shared drives and users' My Drives.

            Items that match the patterns are excluded from the index. Items that don't match the patterns are included in the index. If an item matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the item isn't included in the index.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-googledriveconfiguration.html#cfn-kendra-datasource-googledriveconfiguration-exclusionpatterns
            '''
            result = self._values.get("exclusion_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def field_mappings(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DataSourceToIndexFieldMappingProperty"]]]]:
            '''Maps Google Drive data source attributes or field names to Amazon Kendra index field names.

            To create custom fields, use the ``UpdateIndex`` API before you map to Google Drive fields. For more information, see `Mapping data source fields <https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html>`_ . The Google Drive data source field names must exist in your Google Drive custom metadata.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-googledriveconfiguration.html#cfn-kendra-datasource-googledriveconfiguration-fieldmappings
            '''
            result = self._values.get("field_mappings")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DataSourceToIndexFieldMappingProperty"]]]], result)

        @builtins.property
        def inclusion_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of regular expression patterns to include certain items in your Google Drive, including shared drives and users' My Drives.

            Items that match the patterns are included in the index. Items that don't match the patterns are excluded from the index. If an item matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the item isn't included in the index.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-googledriveconfiguration.html#cfn-kendra-datasource-googledriveconfiguration-inclusionpatterns
            '''
            result = self._values.get("inclusion_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GoogleDriveConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.HookConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "lambda_arn": "lambdaArn",
            "s3_bucket": "s3Bucket",
            "invocation_condition": "invocationCondition",
        },
    )
    class HookConfigurationProperty:
        def __init__(
            self,
            *,
            lambda_arn: builtins.str,
            s3_bucket: builtins.str,
            invocation_condition: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.DocumentAttributeConditionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Provides the configuration information for invoking a Lambda function in AWS Lambda to alter document metadata and content when ingesting documents into Amazon Kendra.

            You can configure your Lambda function using `PreExtractionHookConfiguration <https://docs.aws.amazon.com/kendra/latest/dg/API_CustomDocumentEnrichmentConfiguration.html>`_ if you want to apply advanced alterations on the original or raw documents. If you want to apply advanced alterations on the Amazon Kendra structured documents, you must configure your Lambda function using `PostExtractionHookConfiguration <https://docs.aws.amazon.com/kendra/latest/dg/API_CustomDocumentEnrichmentConfiguration.html>`_ . You can only invoke one Lambda function. However, this function can invoke other functions it requires.

            For more information, see `Customizing document metadata during the ingestion process <https://docs.aws.amazon.com/kendra/latest/dg/custom-document-enrichment.html>`_ .

            :param lambda_arn: The Amazon Resource Name (ARN) of a role with permission to run a Lambda function during ingestion. For more information, see `IAM roles for Amazon Kendra <https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html>`_ .
            :param s3_bucket: Stores the original, raw documents or the structured, parsed documents before and after altering them. For more information, see `Data contracts for Lambda functions <https://docs.aws.amazon.com/kendra/latest/dg/custom-document-enrichment.html#cde-data-contracts-lambda>`_ .
            :param invocation_condition: The condition used for when a Lambda function should be invoked. For example, you can specify a condition that if there are empty date-time values, then Amazon Kendra should invoke a function that inserts the current date-time.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-hookconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                hook_configuration_property = kendra.CfnDataSource.HookConfigurationProperty(
                    lambda_arn="lambdaArn",
                    s3_bucket="s3Bucket",
                
                    # the properties below are optional
                    invocation_condition=kendra.CfnDataSource.DocumentAttributeConditionProperty(
                        condition_document_attribute_key="conditionDocumentAttributeKey",
                        operator="operator",
                
                        # the properties below are optional
                        condition_on_value=kendra.CfnDataSource.DocumentAttributeValueProperty(
                            date_value="dateValue",
                            long_value=123,
                            string_list_value=["stringListValue"],
                            string_value="stringValue"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f88ce175d173734efc6721d6feeeb56e8658cb0561f11152633b1546afaf3467)
                check_type(argname="argument lambda_arn", value=lambda_arn, expected_type=type_hints["lambda_arn"])
                check_type(argname="argument s3_bucket", value=s3_bucket, expected_type=type_hints["s3_bucket"])
                check_type(argname="argument invocation_condition", value=invocation_condition, expected_type=type_hints["invocation_condition"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "lambda_arn": lambda_arn,
                "s3_bucket": s3_bucket,
            }
            if invocation_condition is not None:
                self._values["invocation_condition"] = invocation_condition

        @builtins.property
        def lambda_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of a role with permission to run a Lambda function during ingestion.

            For more information, see `IAM roles for Amazon Kendra <https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-hookconfiguration.html#cfn-kendra-datasource-hookconfiguration-lambdaarn
            '''
            result = self._values.get("lambda_arn")
            assert result is not None, "Required property 'lambda_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_bucket(self) -> builtins.str:
            '''Stores the original, raw documents or the structured, parsed documents before and after altering them.

            For more information, see `Data contracts for Lambda functions <https://docs.aws.amazon.com/kendra/latest/dg/custom-document-enrichment.html#cde-data-contracts-lambda>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-hookconfiguration.html#cfn-kendra-datasource-hookconfiguration-s3bucket
            '''
            result = self._values.get("s3_bucket")
            assert result is not None, "Required property 's3_bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def invocation_condition(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DocumentAttributeConditionProperty"]]:
            '''The condition used for when a Lambda function should be invoked.

            For example, you can specify a condition that if there are empty date-time values, then Amazon Kendra should invoke a function that inserts the current date-time.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-hookconfiguration.html#cfn-kendra-datasource-hookconfiguration-invocationcondition
            '''
            result = self._values.get("invocation_condition")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DocumentAttributeConditionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HookConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.InlineCustomDocumentEnrichmentConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "condition": "condition",
            "document_content_deletion": "documentContentDeletion",
            "target": "target",
        },
    )
    class InlineCustomDocumentEnrichmentConfigurationProperty:
        def __init__(
            self,
            *,
            condition: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.DocumentAttributeConditionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            document_content_deletion: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            target: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.DocumentAttributeTargetProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Provides the configuration information for applying basic logic to alter document metadata and content when ingesting documents into Amazon Kendra.

            To apply advanced logic, to go beyond what you can do with basic logic, see `HookConfiguration <https://docs.aws.amazon.com/kendra/latest/dg/API_HookConfiguration.html>`_ .

            For more information, see `Customizing document metadata during the ingestion process <https://docs.aws.amazon.com/kendra/latest/dg/custom-document-enrichment.html>`_ .

            :param condition: Configuration of the condition used for the target document attribute or metadata field when ingesting documents into Amazon Kendra.
            :param document_content_deletion: ``TRUE`` to delete content if the condition used for the target attribute is met.
            :param target: Configuration of the target document attribute or metadata field when ingesting documents into Amazon Kendra. You can also include a value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-inlinecustomdocumentenrichmentconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                inline_custom_document_enrichment_configuration_property = kendra.CfnDataSource.InlineCustomDocumentEnrichmentConfigurationProperty(
                    condition=kendra.CfnDataSource.DocumentAttributeConditionProperty(
                        condition_document_attribute_key="conditionDocumentAttributeKey",
                        operator="operator",
                
                        # the properties below are optional
                        condition_on_value=kendra.CfnDataSource.DocumentAttributeValueProperty(
                            date_value="dateValue",
                            long_value=123,
                            string_list_value=["stringListValue"],
                            string_value="stringValue"
                        )
                    ),
                    document_content_deletion=False,
                    target=kendra.CfnDataSource.DocumentAttributeTargetProperty(
                        target_document_attribute_key="targetDocumentAttributeKey",
                
                        # the properties below are optional
                        target_document_attribute_value=kendra.CfnDataSource.DocumentAttributeValueProperty(
                            date_value="dateValue",
                            long_value=123,
                            string_list_value=["stringListValue"],
                            string_value="stringValue"
                        ),
                        target_document_attribute_value_deletion=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__778dbd7cfd60bb1372e2f7438f3c056a9ea9a9161f3caa226477890bcd99cea3)
                check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
                check_type(argname="argument document_content_deletion", value=document_content_deletion, expected_type=type_hints["document_content_deletion"])
                check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if condition is not None:
                self._values["condition"] = condition
            if document_content_deletion is not None:
                self._values["document_content_deletion"] = document_content_deletion
            if target is not None:
                self._values["target"] = target

        @builtins.property
        def condition(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DocumentAttributeConditionProperty"]]:
            '''Configuration of the condition used for the target document attribute or metadata field when ingesting documents into Amazon Kendra.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-inlinecustomdocumentenrichmentconfiguration.html#cfn-kendra-datasource-inlinecustomdocumentenrichmentconfiguration-condition
            '''
            result = self._values.get("condition")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DocumentAttributeConditionProperty"]], result)

        @builtins.property
        def document_content_deletion(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''``TRUE`` to delete content if the condition used for the target attribute is met.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-inlinecustomdocumentenrichmentconfiguration.html#cfn-kendra-datasource-inlinecustomdocumentenrichmentconfiguration-documentcontentdeletion
            '''
            result = self._values.get("document_content_deletion")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def target(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DocumentAttributeTargetProperty"]]:
            '''Configuration of the target document attribute or metadata field when ingesting documents into Amazon Kendra.

            You can also include a value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-inlinecustomdocumentenrichmentconfiguration.html#cfn-kendra-datasource-inlinecustomdocumentenrichmentconfiguration-target
            '''
            result = self._values.get("target")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DocumentAttributeTargetProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InlineCustomDocumentEnrichmentConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.OneDriveConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "one_drive_users": "oneDriveUsers",
            "secret_arn": "secretArn",
            "tenant_domain": "tenantDomain",
            "disable_local_groups": "disableLocalGroups",
            "exclusion_patterns": "exclusionPatterns",
            "field_mappings": "fieldMappings",
            "inclusion_patterns": "inclusionPatterns",
        },
    )
    class OneDriveConfigurationProperty:
        def __init__(
            self,
            *,
            one_drive_users: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.OneDriveUsersProperty", typing.Dict[builtins.str, typing.Any]]],
            secret_arn: builtins.str,
            tenant_domain: builtins.str,
            disable_local_groups: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            exclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
            field_mappings: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            inclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Provides the configuration information to connect to OneDrive as your data source.

            :param one_drive_users: A list of user accounts whose documents should be indexed.
            :param secret_arn: The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains the user name and password to connect to OneDrive. The user name should be the application ID for the OneDrive application, and the password is the application key for the OneDrive application.
            :param tenant_domain: The Azure Active Directory domain of the organization.
            :param disable_local_groups: ``TRUE`` to disable local groups information.
            :param exclusion_patterns: A list of regular expression patterns to exclude certain documents in your OneDrive. Documents that match the patterns are excluded from the index. Documents that don't match the patterns are included in the index. If a document matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the document isn't included in the index. The pattern is applied to the file name.
            :param field_mappings: A list of ``DataSourceToIndexFieldMapping`` objects that map OneDrive data source attributes or field names to Amazon Kendra index field names. To create custom fields, use the ``UpdateIndex`` API before you map to OneDrive fields. For more information, see `Mapping data source fields <https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html>`_ . The OneDrive data source field names must exist in your OneDrive custom metadata.
            :param inclusion_patterns: A list of regular expression patterns to include certain documents in your OneDrive. Documents that match the patterns are included in the index. Documents that don't match the patterns are excluded from the index. If a document matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the document isn't included in the index. The pattern is applied to the file name.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                one_drive_configuration_property = kendra.CfnDataSource.OneDriveConfigurationProperty(
                    one_drive_users=kendra.CfnDataSource.OneDriveUsersProperty(
                        one_drive_user_list=["oneDriveUserList"],
                        one_drive_user_s3_path=kendra.CfnDataSource.S3PathProperty(
                            bucket="bucket",
                            key="key"
                        )
                    ),
                    secret_arn="secretArn",
                    tenant_domain="tenantDomain",
                
                    # the properties below are optional
                    disable_local_groups=False,
                    exclusion_patterns=["exclusionPatterns"],
                    field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                        data_source_field_name="dataSourceFieldName",
                        index_field_name="indexFieldName",
                
                        # the properties below are optional
                        date_field_format="dateFieldFormat"
                    )],
                    inclusion_patterns=["inclusionPatterns"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cf6e5efc7f0c997f06cf9f0d82afec4dfb97aaf99924cb7f954aa49cdb46aad6)
                check_type(argname="argument one_drive_users", value=one_drive_users, expected_type=type_hints["one_drive_users"])
                check_type(argname="argument secret_arn", value=secret_arn, expected_type=type_hints["secret_arn"])
                check_type(argname="argument tenant_domain", value=tenant_domain, expected_type=type_hints["tenant_domain"])
                check_type(argname="argument disable_local_groups", value=disable_local_groups, expected_type=type_hints["disable_local_groups"])
                check_type(argname="argument exclusion_patterns", value=exclusion_patterns, expected_type=type_hints["exclusion_patterns"])
                check_type(argname="argument field_mappings", value=field_mappings, expected_type=type_hints["field_mappings"])
                check_type(argname="argument inclusion_patterns", value=inclusion_patterns, expected_type=type_hints["inclusion_patterns"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "one_drive_users": one_drive_users,
                "secret_arn": secret_arn,
                "tenant_domain": tenant_domain,
            }
            if disable_local_groups is not None:
                self._values["disable_local_groups"] = disable_local_groups
            if exclusion_patterns is not None:
                self._values["exclusion_patterns"] = exclusion_patterns
            if field_mappings is not None:
                self._values["field_mappings"] = field_mappings
            if inclusion_patterns is not None:
                self._values["inclusion_patterns"] = inclusion_patterns

        @builtins.property
        def one_drive_users(
            self,
        ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.OneDriveUsersProperty"]:
            '''A list of user accounts whose documents should be indexed.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveconfiguration.html#cfn-kendra-datasource-onedriveconfiguration-onedriveusers
            '''
            result = self._values.get("one_drive_users")
            assert result is not None, "Required property 'one_drive_users' is missing"
            return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.OneDriveUsersProperty"], result)

        @builtins.property
        def secret_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains the user name and password to connect to OneDrive.

            The user name should be the application ID for the OneDrive application, and the password is the application key for the OneDrive application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveconfiguration.html#cfn-kendra-datasource-onedriveconfiguration-secretarn
            '''
            result = self._values.get("secret_arn")
            assert result is not None, "Required property 'secret_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def tenant_domain(self) -> builtins.str:
            '''The Azure Active Directory domain of the organization.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveconfiguration.html#cfn-kendra-datasource-onedriveconfiguration-tenantdomain
            '''
            result = self._values.get("tenant_domain")
            assert result is not None, "Required property 'tenant_domain' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def disable_local_groups(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''``TRUE`` to disable local groups information.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveconfiguration.html#cfn-kendra-datasource-onedriveconfiguration-disablelocalgroups
            '''
            result = self._values.get("disable_local_groups")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def exclusion_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of regular expression patterns to exclude certain documents in your OneDrive.

            Documents that match the patterns are excluded from the index. Documents that don't match the patterns are included in the index. If a document matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the document isn't included in the index.

            The pattern is applied to the file name.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveconfiguration.html#cfn-kendra-datasource-onedriveconfiguration-exclusionpatterns
            '''
            result = self._values.get("exclusion_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def field_mappings(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DataSourceToIndexFieldMappingProperty"]]]]:
            '''A list of ``DataSourceToIndexFieldMapping`` objects that map OneDrive data source attributes or field names to Amazon Kendra index field names.

            To create custom fields, use the ``UpdateIndex`` API before you map to OneDrive fields. For more information, see `Mapping data source fields <https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html>`_ . The OneDrive data source field names must exist in your OneDrive custom metadata.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveconfiguration.html#cfn-kendra-datasource-onedriveconfiguration-fieldmappings
            '''
            result = self._values.get("field_mappings")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DataSourceToIndexFieldMappingProperty"]]]], result)

        @builtins.property
        def inclusion_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of regular expression patterns to include certain documents in your OneDrive.

            Documents that match the patterns are included in the index. Documents that don't match the patterns are excluded from the index. If a document matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the document isn't included in the index.

            The pattern is applied to the file name.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveconfiguration.html#cfn-kendra-datasource-onedriveconfiguration-inclusionpatterns
            '''
            result = self._values.get("inclusion_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OneDriveConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.OneDriveUsersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "one_drive_user_list": "oneDriveUserList",
            "one_drive_user_s3_path": "oneDriveUserS3Path",
        },
    )
    class OneDriveUsersProperty:
        def __init__(
            self,
            *,
            one_drive_user_list: typing.Optional[typing.Sequence[builtins.str]] = None,
            one_drive_user_s3_path: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.S3PathProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''User accounts whose documents should be indexed.

            :param one_drive_user_list: A list of users whose documents should be indexed. Specify the user names in email format, for example, ``username@tenantdomain`` . If you need to index the documents of more than 100 users, use the ``OneDriveUserS3Path`` field to specify the location of a file containing a list of users.
            :param one_drive_user_s3_path: The S3 bucket location of a file containing a list of users whose documents should be indexed.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveusers.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                one_drive_users_property = kendra.CfnDataSource.OneDriveUsersProperty(
                    one_drive_user_list=["oneDriveUserList"],
                    one_drive_user_s3_path=kendra.CfnDataSource.S3PathProperty(
                        bucket="bucket",
                        key="key"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2b51f386d40b0bc8d28e76be7834b1e99ad4eb440721b408a31b6c03ea32fc94)
                check_type(argname="argument one_drive_user_list", value=one_drive_user_list, expected_type=type_hints["one_drive_user_list"])
                check_type(argname="argument one_drive_user_s3_path", value=one_drive_user_s3_path, expected_type=type_hints["one_drive_user_s3_path"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if one_drive_user_list is not None:
                self._values["one_drive_user_list"] = one_drive_user_list
            if one_drive_user_s3_path is not None:
                self._values["one_drive_user_s3_path"] = one_drive_user_s3_path

        @builtins.property
        def one_drive_user_list(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of users whose documents should be indexed.

            Specify the user names in email format, for example, ``username@tenantdomain`` . If you need to index the documents of more than 100 users, use the ``OneDriveUserS3Path`` field to specify the location of a file containing a list of users.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveusers.html#cfn-kendra-datasource-onedriveusers-onedriveuserlist
            '''
            result = self._values.get("one_drive_user_list")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def one_drive_user_s3_path(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.S3PathProperty"]]:
            '''The S3 bucket location of a file containing a list of users whose documents should be indexed.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-onedriveusers.html#cfn-kendra-datasource-onedriveusers-onedriveusers3path
            '''
            result = self._values.get("one_drive_user_s3_path")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.S3PathProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OneDriveUsersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.ProxyConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"host": "host", "port": "port", "credentials": "credentials"},
    )
    class ProxyConfigurationProperty:
        def __init__(
            self,
            *,
            host: builtins.str,
            port: jsii.Number,
            credentials: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides the configuration information for a web proxy to connect to website hosts.

            :param host: The name of the website host you want to connect to via a web proxy server. For example, the host name of https://a.example.com/page1.html is "a.example.com".
            :param port: The port number of the website host you want to connect to via a web proxy server. For example, the port for https://a.example.com/page1.html is 443, the standard port for HTTPS.
            :param credentials: Your secret ARN, which you can create in `AWS Secrets Manager <https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html>`_. The credentials are optional. You use a secret if web proxy credentials are required to connect to a website host. Amazon Kendra currently support basic authentication to connect to a web proxy server. The secret stores your credentials.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-proxyconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                proxy_configuration_property = kendra.CfnDataSource.ProxyConfigurationProperty(
                    host="host",
                    port=123,
                
                    # the properties below are optional
                    credentials="credentials"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7ee897455f83c68302294f702fdd1bef710bc383e0a7581050ba462dd652e299)
                check_type(argname="argument host", value=host, expected_type=type_hints["host"])
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
                check_type(argname="argument credentials", value=credentials, expected_type=type_hints["credentials"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "host": host,
                "port": port,
            }
            if credentials is not None:
                self._values["credentials"] = credentials

        @builtins.property
        def host(self) -> builtins.str:
            '''The name of the website host you want to connect to via a web proxy server.

            For example, the host name of https://a.example.com/page1.html is "a.example.com".

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-proxyconfiguration.html#cfn-kendra-datasource-proxyconfiguration-host
            '''
            result = self._values.get("host")
            assert result is not None, "Required property 'host' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def port(self) -> jsii.Number:
            '''The port number of the website host you want to connect to via a web proxy server.

            For example, the port for https://a.example.com/page1.html is 443, the standard port for HTTPS.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-proxyconfiguration.html#cfn-kendra-datasource-proxyconfiguration-port
            '''
            result = self._values.get("port")
            assert result is not None, "Required property 'port' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def credentials(self) -> typing.Optional[builtins.str]:
            '''Your secret ARN, which you can create in `AWS Secrets Manager <https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html>`_.

            The credentials are optional. You use a secret if web proxy credentials are required to connect to a website host. Amazon Kendra currently support basic authentication to connect to a web proxy server. The secret stores your credentials.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-proxyconfiguration.html#cfn-kendra-datasource-proxyconfiguration-credentials
            '''
            result = self._values.get("credentials")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProxyConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.S3DataSourceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket_name": "bucketName",
            "access_control_list_configuration": "accessControlListConfiguration",
            "documents_metadata_configuration": "documentsMetadataConfiguration",
            "exclusion_patterns": "exclusionPatterns",
            "inclusion_patterns": "inclusionPatterns",
            "inclusion_prefixes": "inclusionPrefixes",
        },
    )
    class S3DataSourceConfigurationProperty:
        def __init__(
            self,
            *,
            bucket_name: builtins.str,
            access_control_list_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.AccessControlListConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            documents_metadata_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.DocumentsMetadataConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            exclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
            inclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
            inclusion_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Provides the configuration information to connect to an Amazon S3 bucket.

            :param bucket_name: The name of the bucket that contains the documents.
            :param access_control_list_configuration: Provides the path to the S3 bucket that contains the user context filtering files for the data source. For the format of the file, see `Access control for S3 data sources <https://docs.aws.amazon.com/kendra/latest/dg/s3-acl.html>`_ .
            :param documents_metadata_configuration: Specifies document metadata files that contain information such as the document access control information, source URI, document author, and custom attributes. Each metadata file contains metadata about a single document.
            :param exclusion_patterns: A list of glob patterns for documents that should not be indexed. If a document that matches an inclusion prefix or inclusion pattern also matches an exclusion pattern, the document is not indexed. Some `examples <https://docs.aws.amazon.com/cli/latest/reference/s3/#use-of-exclude-and-include-filters>`_ are: - **.png , *.jpg* will exclude all PNG and JPEG image files in a directory (files with the extensions .png and .jpg). - **internal** will exclude all files in a directory that contain 'internal' in the file name, such as 'internal', 'internal_only', 'company_internal'. - *** /*internal** will exclude all internal-related files in a directory and its subdirectories.
            :param inclusion_patterns: A list of glob patterns for documents that should be indexed. If a document that matches an inclusion pattern also matches an exclusion pattern, the document is not indexed. Some `examples <https://docs.aws.amazon.com/cli/latest/reference/s3/#use-of-exclude-and-include-filters>`_ are: - **.txt* will include all text files in a directory (files with the extension .txt). - *** /*.txt* will include all text files in a directory and its subdirectories. - **tax** will include all files in a directory that contain 'tax' in the file name, such as 'tax', 'taxes', 'income_tax'.
            :param inclusion_prefixes: A list of S3 prefixes for the documents that should be included in the index.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-s3datasourceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                s3_data_source_configuration_property = kendra.CfnDataSource.S3DataSourceConfigurationProperty(
                    bucket_name="bucketName",
                
                    # the properties below are optional
                    access_control_list_configuration=kendra.CfnDataSource.AccessControlListConfigurationProperty(
                        key_path="keyPath"
                    ),
                    documents_metadata_configuration=kendra.CfnDataSource.DocumentsMetadataConfigurationProperty(
                        s3_prefix="s3Prefix"
                    ),
                    exclusion_patterns=["exclusionPatterns"],
                    inclusion_patterns=["inclusionPatterns"],
                    inclusion_prefixes=["inclusionPrefixes"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9e4ae625757091c33fab15f4b8e37c739fa7d7fed9de699223d5a680ac6aed34)
                check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
                check_type(argname="argument access_control_list_configuration", value=access_control_list_configuration, expected_type=type_hints["access_control_list_configuration"])
                check_type(argname="argument documents_metadata_configuration", value=documents_metadata_configuration, expected_type=type_hints["documents_metadata_configuration"])
                check_type(argname="argument exclusion_patterns", value=exclusion_patterns, expected_type=type_hints["exclusion_patterns"])
                check_type(argname="argument inclusion_patterns", value=inclusion_patterns, expected_type=type_hints["inclusion_patterns"])
                check_type(argname="argument inclusion_prefixes", value=inclusion_prefixes, expected_type=type_hints["inclusion_prefixes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket_name": bucket_name,
            }
            if access_control_list_configuration is not None:
                self._values["access_control_list_configuration"] = access_control_list_configuration
            if documents_metadata_configuration is not None:
                self._values["documents_metadata_configuration"] = documents_metadata_configuration
            if exclusion_patterns is not None:
                self._values["exclusion_patterns"] = exclusion_patterns
            if inclusion_patterns is not None:
                self._values["inclusion_patterns"] = inclusion_patterns
            if inclusion_prefixes is not None:
                self._values["inclusion_prefixes"] = inclusion_prefixes

        @builtins.property
        def bucket_name(self) -> builtins.str:
            '''The name of the bucket that contains the documents.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-s3datasourceconfiguration.html#cfn-kendra-datasource-s3datasourceconfiguration-bucketname
            '''
            result = self._values.get("bucket_name")
            assert result is not None, "Required property 'bucket_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def access_control_list_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.AccessControlListConfigurationProperty"]]:
            '''Provides the path to the S3 bucket that contains the user context filtering files for the data source.

            For the format of the file, see `Access control for S3 data sources <https://docs.aws.amazon.com/kendra/latest/dg/s3-acl.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-s3datasourceconfiguration.html#cfn-kendra-datasource-s3datasourceconfiguration-accesscontrollistconfiguration
            '''
            result = self._values.get("access_control_list_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.AccessControlListConfigurationProperty"]], result)

        @builtins.property
        def documents_metadata_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DocumentsMetadataConfigurationProperty"]]:
            '''Specifies document metadata files that contain information such as the document access control information, source URI, document author, and custom attributes.

            Each metadata file contains metadata about a single document.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-s3datasourceconfiguration.html#cfn-kendra-datasource-s3datasourceconfiguration-documentsmetadataconfiguration
            '''
            result = self._values.get("documents_metadata_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DocumentsMetadataConfigurationProperty"]], result)

        @builtins.property
        def exclusion_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of glob patterns for documents that should not be indexed.

            If a document that matches an inclusion prefix or inclusion pattern also matches an exclusion pattern, the document is not indexed.

            Some `examples <https://docs.aws.amazon.com/cli/latest/reference/s3/#use-of-exclude-and-include-filters>`_ are:

            - **.png , *.jpg* will exclude all PNG and JPEG image files in a directory (files with the extensions .png and .jpg).
            - **internal** will exclude all files in a directory that contain 'internal' in the file name, such as 'internal', 'internal_only', 'company_internal'.
            - *** /*internal** will exclude all internal-related files in a directory and its subdirectories.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-s3datasourceconfiguration.html#cfn-kendra-datasource-s3datasourceconfiguration-exclusionpatterns
            '''
            result = self._values.get("exclusion_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def inclusion_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of glob patterns for documents that should be indexed.

            If a document that matches an inclusion pattern also matches an exclusion pattern, the document is not indexed.

            Some `examples <https://docs.aws.amazon.com/cli/latest/reference/s3/#use-of-exclude-and-include-filters>`_ are:

            - **.txt* will include all text files in a directory (files with the extension .txt).
            - *** /*.txt* will include all text files in a directory and its subdirectories.
            - **tax** will include all files in a directory that contain 'tax' in the file name, such as 'tax', 'taxes', 'income_tax'.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-s3datasourceconfiguration.html#cfn-kendra-datasource-s3datasourceconfiguration-inclusionpatterns
            '''
            result = self._values.get("inclusion_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def inclusion_prefixes(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of S3 prefixes for the documents that should be included in the index.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-s3datasourceconfiguration.html#cfn-kendra-datasource-s3datasourceconfiguration-inclusionprefixes
            '''
            result = self._values.get("inclusion_prefixes")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3DataSourceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.S3PathProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket": "bucket", "key": "key"},
    )
    class S3PathProperty:
        def __init__(self, *, bucket: builtins.str, key: builtins.str) -> None:
            '''Information required to find a specific file in an Amazon S3 bucket.

            :param bucket: The name of the S3 bucket that contains the file.
            :param key: The name of the file.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-s3path.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                s3_path_property = kendra.CfnDataSource.S3PathProperty(
                    bucket="bucket",
                    key="key"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5c710214f188c5e4da6c2f781b8792ff32b6131c21a8e35e14587223cf96bd5a)
                check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket": bucket,
                "key": key,
            }

        @builtins.property
        def bucket(self) -> builtins.str:
            '''The name of the S3 bucket that contains the file.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-s3path.html#cfn-kendra-datasource-s3path-bucket
            '''
            result = self._values.get("bucket")
            assert result is not None, "Required property 'bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key(self) -> builtins.str:
            '''The name of the file.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-s3path.html#cfn-kendra-datasource-s3path-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3PathProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.SalesforceChatterFeedConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "document_data_field_name": "documentDataFieldName",
            "document_title_field_name": "documentTitleFieldName",
            "field_mappings": "fieldMappings",
            "include_filter_types": "includeFilterTypes",
        },
    )
    class SalesforceChatterFeedConfigurationProperty:
        def __init__(
            self,
            *,
            document_data_field_name: builtins.str,
            document_title_field_name: typing.Optional[builtins.str] = None,
            field_mappings: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            include_filter_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The configuration information for syncing a Salesforce chatter feed.

            The contents of the object comes from the Salesforce FeedItem table.

            :param document_data_field_name: The name of the column in the Salesforce FeedItem table that contains the content to index. Typically this is the ``Body`` column.
            :param document_title_field_name: The name of the column in the Salesforce FeedItem table that contains the title of the document. This is typically the ``Title`` column.
            :param field_mappings: Maps fields from a Salesforce chatter feed into Amazon Kendra index fields.
            :param include_filter_types: Filters the documents in the feed based on status of the user. When you specify ``ACTIVE_USERS`` only documents from users who have an active account are indexed. When you specify ``STANDARD_USER`` only documents for Salesforce standard users are documented. You can specify both.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcechatterfeedconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                salesforce_chatter_feed_configuration_property = kendra.CfnDataSource.SalesforceChatterFeedConfigurationProperty(
                    document_data_field_name="documentDataFieldName",
                
                    # the properties below are optional
                    document_title_field_name="documentTitleFieldName",
                    field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                        data_source_field_name="dataSourceFieldName",
                        index_field_name="indexFieldName",
                
                        # the properties below are optional
                        date_field_format="dateFieldFormat"
                    )],
                    include_filter_types=["includeFilterTypes"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a0f0b92db66314e44cb81d511b60249e849818e202786239e76913be72c16c62)
                check_type(argname="argument document_data_field_name", value=document_data_field_name, expected_type=type_hints["document_data_field_name"])
                check_type(argname="argument document_title_field_name", value=document_title_field_name, expected_type=type_hints["document_title_field_name"])
                check_type(argname="argument field_mappings", value=field_mappings, expected_type=type_hints["field_mappings"])
                check_type(argname="argument include_filter_types", value=include_filter_types, expected_type=type_hints["include_filter_types"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "document_data_field_name": document_data_field_name,
            }
            if document_title_field_name is not None:
                self._values["document_title_field_name"] = document_title_field_name
            if field_mappings is not None:
                self._values["field_mappings"] = field_mappings
            if include_filter_types is not None:
                self._values["include_filter_types"] = include_filter_types

        @builtins.property
        def document_data_field_name(self) -> builtins.str:
            '''The name of the column in the Salesforce FeedItem table that contains the content to index.

            Typically this is the ``Body`` column.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcechatterfeedconfiguration.html#cfn-kendra-datasource-salesforcechatterfeedconfiguration-documentdatafieldname
            '''
            result = self._values.get("document_data_field_name")
            assert result is not None, "Required property 'document_data_field_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def document_title_field_name(self) -> typing.Optional[builtins.str]:
            '''The name of the column in the Salesforce FeedItem table that contains the title of the document.

            This is typically the ``Title`` column.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcechatterfeedconfiguration.html#cfn-kendra-datasource-salesforcechatterfeedconfiguration-documenttitlefieldname
            '''
            result = self._values.get("document_title_field_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def field_mappings(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DataSourceToIndexFieldMappingProperty"]]]]:
            '''Maps fields from a Salesforce chatter feed into Amazon Kendra index fields.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcechatterfeedconfiguration.html#cfn-kendra-datasource-salesforcechatterfeedconfiguration-fieldmappings
            '''
            result = self._values.get("field_mappings")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DataSourceToIndexFieldMappingProperty"]]]], result)

        @builtins.property
        def include_filter_types(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Filters the documents in the feed based on status of the user.

            When you specify ``ACTIVE_USERS`` only documents from users who have an active account are indexed. When you specify ``STANDARD_USER`` only documents for Salesforce standard users are documented. You can specify both.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcechatterfeedconfiguration.html#cfn-kendra-datasource-salesforcechatterfeedconfiguration-includefiltertypes
            '''
            result = self._values.get("include_filter_types")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SalesforceChatterFeedConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.SalesforceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "secret_arn": "secretArn",
            "server_url": "serverUrl",
            "chatter_feed_configuration": "chatterFeedConfiguration",
            "crawl_attachments": "crawlAttachments",
            "exclude_attachment_file_patterns": "excludeAttachmentFilePatterns",
            "include_attachment_file_patterns": "includeAttachmentFilePatterns",
            "knowledge_article_configuration": "knowledgeArticleConfiguration",
            "standard_object_attachment_configuration": "standardObjectAttachmentConfiguration",
            "standard_object_configurations": "standardObjectConfigurations",
        },
    )
    class SalesforceConfigurationProperty:
        def __init__(
            self,
            *,
            secret_arn: builtins.str,
            server_url: builtins.str,
            chatter_feed_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.SalesforceChatterFeedConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            crawl_attachments: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            exclude_attachment_file_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
            include_attachment_file_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
            knowledge_article_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.SalesforceKnowledgeArticleConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            standard_object_attachment_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.SalesforceStandardObjectAttachmentConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            standard_object_configurations: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.SalesforceStandardObjectConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Provides the configuration information to connect to Salesforce as your data source.

            :param secret_arn: The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains the key/value pairs required to connect to your Salesforce instance. The secret must contain a JSON structure with the following keys: - authenticationUrl - The OAUTH endpoint that Amazon Kendra connects to get an OAUTH token. - consumerKey - The application public key generated when you created your Salesforce application. - consumerSecret - The application private key generated when you created your Salesforce application. - password - The password associated with the user logging in to the Salesforce instance. - securityToken - The token associated with the user account logging in to the Salesforce instance. - username - The user name of the user logging in to the Salesforce instance.
            :param server_url: The instance URL for the Salesforce site that you want to index.
            :param chatter_feed_configuration: Configuration information for Salesforce chatter feeds.
            :param crawl_attachments: Indicates whether Amazon Kendra should index attachments to Salesforce objects.
            :param exclude_attachment_file_patterns: A list of regular expression patterns to exclude certain documents in your Salesforce. Documents that match the patterns are excluded from the index. Documents that don't match the patterns are included in the index. If a document matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the document isn't included in the index. The pattern is applied to the name of the attached file.
            :param include_attachment_file_patterns: A list of regular expression patterns to include certain documents in your Salesforce. Documents that match the patterns are included in the index. Documents that don't match the patterns are excluded from the index. If a document matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the document isn't included in the index. The pattern is applied to the name of the attached file.
            :param knowledge_article_configuration: Configuration information for the knowledge article types that Amazon Kendra indexes. Amazon Kendra indexes standard knowledge articles and the standard fields of knowledge articles, or the custom fields of custom knowledge articles, but not both.
            :param standard_object_attachment_configuration: Configuration information for processing attachments to Salesforce standard objects.
            :param standard_object_configurations: Configuration of the Salesforce standard objects that Amazon Kendra indexes.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                salesforce_configuration_property = kendra.CfnDataSource.SalesforceConfigurationProperty(
                    secret_arn="secretArn",
                    server_url="serverUrl",
                
                    # the properties below are optional
                    chatter_feed_configuration=kendra.CfnDataSource.SalesforceChatterFeedConfigurationProperty(
                        document_data_field_name="documentDataFieldName",
                
                        # the properties below are optional
                        document_title_field_name="documentTitleFieldName",
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
                
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )],
                        include_filter_types=["includeFilterTypes"]
                    ),
                    crawl_attachments=False,
                    exclude_attachment_file_patterns=["excludeAttachmentFilePatterns"],
                    include_attachment_file_patterns=["includeAttachmentFilePatterns"],
                    knowledge_article_configuration=kendra.CfnDataSource.SalesforceKnowledgeArticleConfigurationProperty(
                        included_states=["includedStates"],
                
                        # the properties below are optional
                        custom_knowledge_article_type_configurations=[kendra.CfnDataSource.SalesforceCustomKnowledgeArticleTypeConfigurationProperty(
                            document_data_field_name="documentDataFieldName",
                            name="name",
                
                            # the properties below are optional
                            document_title_field_name="documentTitleFieldName",
                            field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
                
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )]
                        )],
                        standard_knowledge_article_type_configuration=kendra.CfnDataSource.SalesforceStandardKnowledgeArticleTypeConfigurationProperty(
                            document_data_field_name="documentDataFieldName",
                
                            # the properties below are optional
                            document_title_field_name="documentTitleFieldName",
                            field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
                
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )]
                        )
                    ),
                    standard_object_attachment_configuration=kendra.CfnDataSource.SalesforceStandardObjectAttachmentConfigurationProperty(
                        document_title_field_name="documentTitleFieldName",
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
                
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )]
                    ),
                    standard_object_configurations=[kendra.CfnDataSource.SalesforceStandardObjectConfigurationProperty(
                        document_data_field_name="documentDataFieldName",
                        name="name",
                
                        # the properties below are optional
                        document_title_field_name="documentTitleFieldName",
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
                
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )]
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fe5fa142481d3b326eba699ad4f51fca25323939f0e91d3b0a128446ac069732)
                check_type(argname="argument secret_arn", value=secret_arn, expected_type=type_hints["secret_arn"])
                check_type(argname="argument server_url", value=server_url, expected_type=type_hints["server_url"])
                check_type(argname="argument chatter_feed_configuration", value=chatter_feed_configuration, expected_type=type_hints["chatter_feed_configuration"])
                check_type(argname="argument crawl_attachments", value=crawl_attachments, expected_type=type_hints["crawl_attachments"])
                check_type(argname="argument exclude_attachment_file_patterns", value=exclude_attachment_file_patterns, expected_type=type_hints["exclude_attachment_file_patterns"])
                check_type(argname="argument include_attachment_file_patterns", value=include_attachment_file_patterns, expected_type=type_hints["include_attachment_file_patterns"])
                check_type(argname="argument knowledge_article_configuration", value=knowledge_article_configuration, expected_type=type_hints["knowledge_article_configuration"])
                check_type(argname="argument standard_object_attachment_configuration", value=standard_object_attachment_configuration, expected_type=type_hints["standard_object_attachment_configuration"])
                check_type(argname="argument standard_object_configurations", value=standard_object_configurations, expected_type=type_hints["standard_object_configurations"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "secret_arn": secret_arn,
                "server_url": server_url,
            }
            if chatter_feed_configuration is not None:
                self._values["chatter_feed_configuration"] = chatter_feed_configuration
            if crawl_attachments is not None:
                self._values["crawl_attachments"] = crawl_attachments
            if exclude_attachment_file_patterns is not None:
                self._values["exclude_attachment_file_patterns"] = exclude_attachment_file_patterns
            if include_attachment_file_patterns is not None:
                self._values["include_attachment_file_patterns"] = include_attachment_file_patterns
            if knowledge_article_configuration is not None:
                self._values["knowledge_article_configuration"] = knowledge_article_configuration
            if standard_object_attachment_configuration is not None:
                self._values["standard_object_attachment_configuration"] = standard_object_attachment_configuration
            if standard_object_configurations is not None:
                self._values["standard_object_configurations"] = standard_object_configurations

        @builtins.property
        def secret_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains the key/value pairs required to connect to your Salesforce instance.

            The secret must contain a JSON structure with the following keys:

            - authenticationUrl - The OAUTH endpoint that Amazon Kendra connects to get an OAUTH token.
            - consumerKey - The application public key generated when you created your Salesforce application.
            - consumerSecret - The application private key generated when you created your Salesforce application.
            - password - The password associated with the user logging in to the Salesforce instance.
            - securityToken - The token associated with the user account logging in to the Salesforce instance.
            - username - The user name of the user logging in to the Salesforce instance.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceconfiguration.html#cfn-kendra-datasource-salesforceconfiguration-secretarn
            '''
            result = self._values.get("secret_arn")
            assert result is not None, "Required property 'secret_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def server_url(self) -> builtins.str:
            '''The instance URL for the Salesforce site that you want to index.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceconfiguration.html#cfn-kendra-datasource-salesforceconfiguration-serverurl
            '''
            result = self._values.get("server_url")
            assert result is not None, "Required property 'server_url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def chatter_feed_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.SalesforceChatterFeedConfigurationProperty"]]:
            '''Configuration information for Salesforce chatter feeds.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceconfiguration.html#cfn-kendra-datasource-salesforceconfiguration-chatterfeedconfiguration
            '''
            result = self._values.get("chatter_feed_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.SalesforceChatterFeedConfigurationProperty"]], result)

        @builtins.property
        def crawl_attachments(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''Indicates whether Amazon Kendra should index attachments to Salesforce objects.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceconfiguration.html#cfn-kendra-datasource-salesforceconfiguration-crawlattachments
            '''
            result = self._values.get("crawl_attachments")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def exclude_attachment_file_patterns(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of regular expression patterns to exclude certain documents in your Salesforce.

            Documents that match the patterns are excluded from the index. Documents that don't match the patterns are included in the index. If a document matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the document isn't included in the index.

            The pattern is applied to the name of the attached file.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceconfiguration.html#cfn-kendra-datasource-salesforceconfiguration-excludeattachmentfilepatterns
            '''
            result = self._values.get("exclude_attachment_file_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def include_attachment_file_patterns(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of regular expression patterns to include certain documents in your Salesforce.

            Documents that match the patterns are included in the index. Documents that don't match the patterns are excluded from the index. If a document matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the document isn't included in the index.

            The pattern is applied to the name of the attached file.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceconfiguration.html#cfn-kendra-datasource-salesforceconfiguration-includeattachmentfilepatterns
            '''
            result = self._values.get("include_attachment_file_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def knowledge_article_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.SalesforceKnowledgeArticleConfigurationProperty"]]:
            '''Configuration information for the knowledge article types that Amazon Kendra indexes.

            Amazon Kendra indexes standard knowledge articles and the standard fields of knowledge articles, or the custom fields of custom knowledge articles, but not both.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceconfiguration.html#cfn-kendra-datasource-salesforceconfiguration-knowledgearticleconfiguration
            '''
            result = self._values.get("knowledge_article_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.SalesforceKnowledgeArticleConfigurationProperty"]], result)

        @builtins.property
        def standard_object_attachment_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.SalesforceStandardObjectAttachmentConfigurationProperty"]]:
            '''Configuration information for processing attachments to Salesforce standard objects.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceconfiguration.html#cfn-kendra-datasource-salesforceconfiguration-standardobjectattachmentconfiguration
            '''
            result = self._values.get("standard_object_attachment_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.SalesforceStandardObjectAttachmentConfigurationProperty"]], result)

        @builtins.property
        def standard_object_configurations(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.SalesforceStandardObjectConfigurationProperty"]]]]:
            '''Configuration of the Salesforce standard objects that Amazon Kendra indexes.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceconfiguration.html#cfn-kendra-datasource-salesforceconfiguration-standardobjectconfigurations
            '''
            result = self._values.get("standard_object_configurations")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.SalesforceStandardObjectConfigurationProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SalesforceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.SalesforceCustomKnowledgeArticleTypeConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "document_data_field_name": "documentDataFieldName",
            "name": "name",
            "document_title_field_name": "documentTitleFieldName",
            "field_mappings": "fieldMappings",
        },
    )
    class SalesforceCustomKnowledgeArticleTypeConfigurationProperty:
        def __init__(
            self,
            *,
            document_data_field_name: builtins.str,
            name: builtins.str,
            document_title_field_name: typing.Optional[builtins.str] = None,
            field_mappings: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Provides the configuration information for indexing Salesforce custom articles.

            :param document_data_field_name: The name of the field in the custom knowledge article that contains the document data to index.
            :param name: The name of the configuration.
            :param document_title_field_name: The name of the field in the custom knowledge article that contains the document title.
            :param field_mappings: Maps attributes or field names of the custom knowledge article to Amazon Kendra index field names. To create custom fields, use the ``UpdateIndex`` API before you map to Salesforce fields. For more information, see `Mapping data source fields <https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html>`_ . The Salesforce data source field names must exist in your Salesforce custom metadata.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcecustomknowledgearticletypeconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                salesforce_custom_knowledge_article_type_configuration_property = kendra.CfnDataSource.SalesforceCustomKnowledgeArticleTypeConfigurationProperty(
                    document_data_field_name="documentDataFieldName",
                    name="name",
                
                    # the properties below are optional
                    document_title_field_name="documentTitleFieldName",
                    field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                        data_source_field_name="dataSourceFieldName",
                        index_field_name="indexFieldName",
                
                        # the properties below are optional
                        date_field_format="dateFieldFormat"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__151fc85c68d6264787df14a6f7d121b0319c9cc77d7c0dd10c4f55f2b29acc37)
                check_type(argname="argument document_data_field_name", value=document_data_field_name, expected_type=type_hints["document_data_field_name"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument document_title_field_name", value=document_title_field_name, expected_type=type_hints["document_title_field_name"])
                check_type(argname="argument field_mappings", value=field_mappings, expected_type=type_hints["field_mappings"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "document_data_field_name": document_data_field_name,
                "name": name,
            }
            if document_title_field_name is not None:
                self._values["document_title_field_name"] = document_title_field_name
            if field_mappings is not None:
                self._values["field_mappings"] = field_mappings

        @builtins.property
        def document_data_field_name(self) -> builtins.str:
            '''The name of the field in the custom knowledge article that contains the document data to index.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcecustomknowledgearticletypeconfiguration.html#cfn-kendra-datasource-salesforcecustomknowledgearticletypeconfiguration-documentdatafieldname
            '''
            result = self._values.get("document_data_field_name")
            assert result is not None, "Required property 'document_data_field_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcecustomknowledgearticletypeconfiguration.html#cfn-kendra-datasource-salesforcecustomknowledgearticletypeconfiguration-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def document_title_field_name(self) -> typing.Optional[builtins.str]:
            '''The name of the field in the custom knowledge article that contains the document title.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcecustomknowledgearticletypeconfiguration.html#cfn-kendra-datasource-salesforcecustomknowledgearticletypeconfiguration-documenttitlefieldname
            '''
            result = self._values.get("document_title_field_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def field_mappings(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DataSourceToIndexFieldMappingProperty"]]]]:
            '''Maps attributes or field names of the custom knowledge article to Amazon Kendra index field names.

            To create custom fields, use the ``UpdateIndex`` API before you map to Salesforce fields. For more information, see `Mapping data source fields <https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html>`_ . The Salesforce data source field names must exist in your Salesforce custom metadata.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcecustomknowledgearticletypeconfiguration.html#cfn-kendra-datasource-salesforcecustomknowledgearticletypeconfiguration-fieldmappings
            '''
            result = self._values.get("field_mappings")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DataSourceToIndexFieldMappingProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SalesforceCustomKnowledgeArticleTypeConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.SalesforceKnowledgeArticleConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "included_states": "includedStates",
            "custom_knowledge_article_type_configurations": "customKnowledgeArticleTypeConfigurations",
            "standard_knowledge_article_type_configuration": "standardKnowledgeArticleTypeConfiguration",
        },
    )
    class SalesforceKnowledgeArticleConfigurationProperty:
        def __init__(
            self,
            *,
            included_states: typing.Sequence[builtins.str],
            custom_knowledge_article_type_configurations: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.SalesforceCustomKnowledgeArticleTypeConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            standard_knowledge_article_type_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.SalesforceStandardKnowledgeArticleTypeConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Provides the configuration information for the knowledge article types that Amazon Kendra indexes.

            Amazon Kendra indexes standard knowledge articles and the standard fields of knowledge articles, or the custom fields of custom knowledge articles, but not both

            :param included_states: Specifies the document states that should be included when Amazon Kendra indexes knowledge articles. You must specify at least one state.
            :param custom_knowledge_article_type_configurations: Configuration information for custom Salesforce knowledge articles.
            :param standard_knowledge_article_type_configuration: Configuration information for standard Salesforce knowledge articles.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceknowledgearticleconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                salesforce_knowledge_article_configuration_property = kendra.CfnDataSource.SalesforceKnowledgeArticleConfigurationProperty(
                    included_states=["includedStates"],
                
                    # the properties below are optional
                    custom_knowledge_article_type_configurations=[kendra.CfnDataSource.SalesforceCustomKnowledgeArticleTypeConfigurationProperty(
                        document_data_field_name="documentDataFieldName",
                        name="name",
                
                        # the properties below are optional
                        document_title_field_name="documentTitleFieldName",
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
                
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )]
                    )],
                    standard_knowledge_article_type_configuration=kendra.CfnDataSource.SalesforceStandardKnowledgeArticleTypeConfigurationProperty(
                        document_data_field_name="documentDataFieldName",
                
                        # the properties below are optional
                        document_title_field_name="documentTitleFieldName",
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
                
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7737539f92080202809fd1b873f3311d1ab257843845347f1b4edeae69779f83)
                check_type(argname="argument included_states", value=included_states, expected_type=type_hints["included_states"])
                check_type(argname="argument custom_knowledge_article_type_configurations", value=custom_knowledge_article_type_configurations, expected_type=type_hints["custom_knowledge_article_type_configurations"])
                check_type(argname="argument standard_knowledge_article_type_configuration", value=standard_knowledge_article_type_configuration, expected_type=type_hints["standard_knowledge_article_type_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "included_states": included_states,
            }
            if custom_knowledge_article_type_configurations is not None:
                self._values["custom_knowledge_article_type_configurations"] = custom_knowledge_article_type_configurations
            if standard_knowledge_article_type_configuration is not None:
                self._values["standard_knowledge_article_type_configuration"] = standard_knowledge_article_type_configuration

        @builtins.property
        def included_states(self) -> typing.List[builtins.str]:
            '''Specifies the document states that should be included when Amazon Kendra indexes knowledge articles.

            You must specify at least one state.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceknowledgearticleconfiguration.html#cfn-kendra-datasource-salesforceknowledgearticleconfiguration-includedstates
            '''
            result = self._values.get("included_states")
            assert result is not None, "Required property 'included_states' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def custom_knowledge_article_type_configurations(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.SalesforceCustomKnowledgeArticleTypeConfigurationProperty"]]]]:
            '''Configuration information for custom Salesforce knowledge articles.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceknowledgearticleconfiguration.html#cfn-kendra-datasource-salesforceknowledgearticleconfiguration-customknowledgearticletypeconfigurations
            '''
            result = self._values.get("custom_knowledge_article_type_configurations")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.SalesforceCustomKnowledgeArticleTypeConfigurationProperty"]]]], result)

        @builtins.property
        def standard_knowledge_article_type_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.SalesforceStandardKnowledgeArticleTypeConfigurationProperty"]]:
            '''Configuration information for standard Salesforce knowledge articles.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforceknowledgearticleconfiguration.html#cfn-kendra-datasource-salesforceknowledgearticleconfiguration-standardknowledgearticletypeconfiguration
            '''
            result = self._values.get("standard_knowledge_article_type_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.SalesforceStandardKnowledgeArticleTypeConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SalesforceKnowledgeArticleConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.SalesforceStandardKnowledgeArticleTypeConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "document_data_field_name": "documentDataFieldName",
            "document_title_field_name": "documentTitleFieldName",
            "field_mappings": "fieldMappings",
        },
    )
    class SalesforceStandardKnowledgeArticleTypeConfigurationProperty:
        def __init__(
            self,
            *,
            document_data_field_name: builtins.str,
            document_title_field_name: typing.Optional[builtins.str] = None,
            field_mappings: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Provides the configuration information for standard Salesforce knowledge articles.

            :param document_data_field_name: The name of the field that contains the document data to index.
            :param document_title_field_name: The name of the field that contains the document title.
            :param field_mappings: Maps attributes or field names of the knowledge article to Amazon Kendra index field names. To create custom fields, use the ``UpdateIndex`` API before you map to Salesforce fields. For more information, see `Mapping data source fields <https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html>`_ . The Salesforce data source field names must exist in your Salesforce custom metadata.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                salesforce_standard_knowledge_article_type_configuration_property = kendra.CfnDataSource.SalesforceStandardKnowledgeArticleTypeConfigurationProperty(
                    document_data_field_name="documentDataFieldName",
                
                    # the properties below are optional
                    document_title_field_name="documentTitleFieldName",
                    field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                        data_source_field_name="dataSourceFieldName",
                        index_field_name="indexFieldName",
                
                        # the properties below are optional
                        date_field_format="dateFieldFormat"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8e081a7372ad2646b3a525519e42d144c16f1b312003b128841e099c6b97ced8)
                check_type(argname="argument document_data_field_name", value=document_data_field_name, expected_type=type_hints["document_data_field_name"])
                check_type(argname="argument document_title_field_name", value=document_title_field_name, expected_type=type_hints["document_title_field_name"])
                check_type(argname="argument field_mappings", value=field_mappings, expected_type=type_hints["field_mappings"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "document_data_field_name": document_data_field_name,
            }
            if document_title_field_name is not None:
                self._values["document_title_field_name"] = document_title_field_name
            if field_mappings is not None:
                self._values["field_mappings"] = field_mappings

        @builtins.property
        def document_data_field_name(self) -> builtins.str:
            '''The name of the field that contains the document data to index.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration.html#cfn-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration-documentdatafieldname
            '''
            result = self._values.get("document_data_field_name")
            assert result is not None, "Required property 'document_data_field_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def document_title_field_name(self) -> typing.Optional[builtins.str]:
            '''The name of the field that contains the document title.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration.html#cfn-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration-documenttitlefieldname
            '''
            result = self._values.get("document_title_field_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def field_mappings(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DataSourceToIndexFieldMappingProperty"]]]]:
            '''Maps attributes or field names of the knowledge article to Amazon Kendra index field names.

            To create custom fields, use the ``UpdateIndex`` API before you map to Salesforce fields. For more information, see `Mapping data source fields <https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html>`_ . The Salesforce data source field names must exist in your Salesforce custom metadata.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration.html#cfn-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration-fieldmappings
            '''
            result = self._values.get("field_mappings")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DataSourceToIndexFieldMappingProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SalesforceStandardKnowledgeArticleTypeConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.SalesforceStandardObjectAttachmentConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "document_title_field_name": "documentTitleFieldName",
            "field_mappings": "fieldMappings",
        },
    )
    class SalesforceStandardObjectAttachmentConfigurationProperty:
        def __init__(
            self,
            *,
            document_title_field_name: typing.Optional[builtins.str] = None,
            field_mappings: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Provides the configuration information for processing attachments to Salesforce standard objects.

            :param document_title_field_name: The name of the field used for the document title.
            :param field_mappings: One or more objects that map fields in attachments to Amazon Kendra index fields.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardobjectattachmentconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                salesforce_standard_object_attachment_configuration_property = kendra.CfnDataSource.SalesforceStandardObjectAttachmentConfigurationProperty(
                    document_title_field_name="documentTitleFieldName",
                    field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                        data_source_field_name="dataSourceFieldName",
                        index_field_name="indexFieldName",
                
                        # the properties below are optional
                        date_field_format="dateFieldFormat"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__365ce3c088ddf254287d302b735b788c3446d5a1628bcaf7d2146a24cda32b33)
                check_type(argname="argument document_title_field_name", value=document_title_field_name, expected_type=type_hints["document_title_field_name"])
                check_type(argname="argument field_mappings", value=field_mappings, expected_type=type_hints["field_mappings"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if document_title_field_name is not None:
                self._values["document_title_field_name"] = document_title_field_name
            if field_mappings is not None:
                self._values["field_mappings"] = field_mappings

        @builtins.property
        def document_title_field_name(self) -> typing.Optional[builtins.str]:
            '''The name of the field used for the document title.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardobjectattachmentconfiguration.html#cfn-kendra-datasource-salesforcestandardobjectattachmentconfiguration-documenttitlefieldname
            '''
            result = self._values.get("document_title_field_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def field_mappings(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DataSourceToIndexFieldMappingProperty"]]]]:
            '''One or more objects that map fields in attachments to Amazon Kendra index fields.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardobjectattachmentconfiguration.html#cfn-kendra-datasource-salesforcestandardobjectattachmentconfiguration-fieldmappings
            '''
            result = self._values.get("field_mappings")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DataSourceToIndexFieldMappingProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SalesforceStandardObjectAttachmentConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.SalesforceStandardObjectConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "document_data_field_name": "documentDataFieldName",
            "name": "name",
            "document_title_field_name": "documentTitleFieldName",
            "field_mappings": "fieldMappings",
        },
    )
    class SalesforceStandardObjectConfigurationProperty:
        def __init__(
            self,
            *,
            document_data_field_name: builtins.str,
            name: builtins.str,
            document_title_field_name: typing.Optional[builtins.str] = None,
            field_mappings: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Specifies configuration information for indexing a single standard object.

            :param document_data_field_name: The name of the field in the standard object table that contains the document contents.
            :param name: The name of the standard object.
            :param document_title_field_name: The name of the field in the standard object table that contains the document title.
            :param field_mappings: Maps attributes or field names of the standard object to Amazon Kendra index field names. To create custom fields, use the ``UpdateIndex`` API before you map to Salesforce fields. For more information, see `Mapping data source fields <https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html>`_ . The Salesforce data source field names must exist in your Salesforce custom metadata.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardobjectconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                salesforce_standard_object_configuration_property = kendra.CfnDataSource.SalesforceStandardObjectConfigurationProperty(
                    document_data_field_name="documentDataFieldName",
                    name="name",
                
                    # the properties below are optional
                    document_title_field_name="documentTitleFieldName",
                    field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                        data_source_field_name="dataSourceFieldName",
                        index_field_name="indexFieldName",
                
                        # the properties below are optional
                        date_field_format="dateFieldFormat"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5b9be6fc3897a699183461bfe1b6666a951df81a01c40697ca1c9526c2e30909)
                check_type(argname="argument document_data_field_name", value=document_data_field_name, expected_type=type_hints["document_data_field_name"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument document_title_field_name", value=document_title_field_name, expected_type=type_hints["document_title_field_name"])
                check_type(argname="argument field_mappings", value=field_mappings, expected_type=type_hints["field_mappings"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "document_data_field_name": document_data_field_name,
                "name": name,
            }
            if document_title_field_name is not None:
                self._values["document_title_field_name"] = document_title_field_name
            if field_mappings is not None:
                self._values["field_mappings"] = field_mappings

        @builtins.property
        def document_data_field_name(self) -> builtins.str:
            '''The name of the field in the standard object table that contains the document contents.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardobjectconfiguration.html#cfn-kendra-datasource-salesforcestandardobjectconfiguration-documentdatafieldname
            '''
            result = self._values.get("document_data_field_name")
            assert result is not None, "Required property 'document_data_field_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the standard object.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardobjectconfiguration.html#cfn-kendra-datasource-salesforcestandardobjectconfiguration-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def document_title_field_name(self) -> typing.Optional[builtins.str]:
            '''The name of the field in the standard object table that contains the document title.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardobjectconfiguration.html#cfn-kendra-datasource-salesforcestandardobjectconfiguration-documenttitlefieldname
            '''
            result = self._values.get("document_title_field_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def field_mappings(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DataSourceToIndexFieldMappingProperty"]]]]:
            '''Maps attributes or field names of the standard object to Amazon Kendra index field names.

            To create custom fields, use the ``UpdateIndex`` API before you map to Salesforce fields. For more information, see `Mapping data source fields <https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html>`_ . The Salesforce data source field names must exist in your Salesforce custom metadata.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-salesforcestandardobjectconfiguration.html#cfn-kendra-datasource-salesforcestandardobjectconfiguration-fieldmappings
            '''
            result = self._values.get("field_mappings")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DataSourceToIndexFieldMappingProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SalesforceStandardObjectConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.ServiceNowConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "host_url": "hostUrl",
            "secret_arn": "secretArn",
            "service_now_build_version": "serviceNowBuildVersion",
            "authentication_type": "authenticationType",
            "knowledge_article_configuration": "knowledgeArticleConfiguration",
            "service_catalog_configuration": "serviceCatalogConfiguration",
        },
    )
    class ServiceNowConfigurationProperty:
        def __init__(
            self,
            *,
            host_url: builtins.str,
            secret_arn: builtins.str,
            service_now_build_version: builtins.str,
            authentication_type: typing.Optional[builtins.str] = None,
            knowledge_article_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.ServiceNowKnowledgeArticleConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            service_catalog_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.ServiceNowServiceCatalogConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Provides the configuration information to connect to ServiceNow as your data source.

            :param host_url: The ServiceNow instance that the data source connects to. The host endpoint should look like the following: *{instance}.service-now.com.*
            :param secret_arn: The Amazon Resource Name (ARN) of the AWS Secrets Manager secret that contains the user name and password required to connect to the ServiceNow instance. You can also provide OAuth authentication credentials of user name, password, client ID, and client secret. For more information, see `Using a ServiceNow data source <https://docs.aws.amazon.com/kendra/latest/dg/data-source-servicenow.html>`_ .
            :param service_now_build_version: The identifier of the release that the ServiceNow host is running. If the host is not running the ``LONDON`` release, use ``OTHERS`` .
            :param authentication_type: The type of authentication used to connect to the ServiceNow instance. If you choose ``HTTP_BASIC`` , Amazon Kendra is authenticated using the user name and password provided in the AWS Secrets Manager secret in the ``SecretArn`` field. If you choose ``OAUTH2`` , Amazon Kendra is authenticated using the credentials of client ID, client secret, user name and password. When you use ``OAUTH2`` authentication, you must generate a token and a client secret using the ServiceNow console. For more information, see `Using a ServiceNow data source <https://docs.aws.amazon.com/kendra/latest/dg/data-source-servicenow.html>`_ .
            :param knowledge_article_configuration: Configuration information for crawling knowledge articles in the ServiceNow site.
            :param service_catalog_configuration: Configuration information for crawling service catalogs in the ServiceNow site.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                service_now_configuration_property = kendra.CfnDataSource.ServiceNowConfigurationProperty(
                    host_url="hostUrl",
                    secret_arn="secretArn",
                    service_now_build_version="serviceNowBuildVersion",
                
                    # the properties below are optional
                    authentication_type="authenticationType",
                    knowledge_article_configuration=kendra.CfnDataSource.ServiceNowKnowledgeArticleConfigurationProperty(
                        document_data_field_name="documentDataFieldName",
                
                        # the properties below are optional
                        crawl_attachments=False,
                        document_title_field_name="documentTitleFieldName",
                        exclude_attachment_file_patterns=["excludeAttachmentFilePatterns"],
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
                
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )],
                        filter_query="filterQuery",
                        include_attachment_file_patterns=["includeAttachmentFilePatterns"]
                    ),
                    service_catalog_configuration=kendra.CfnDataSource.ServiceNowServiceCatalogConfigurationProperty(
                        document_data_field_name="documentDataFieldName",
                
                        # the properties below are optional
                        crawl_attachments=False,
                        document_title_field_name="documentTitleFieldName",
                        exclude_attachment_file_patterns=["excludeAttachmentFilePatterns"],
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
                
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )],
                        include_attachment_file_patterns=["includeAttachmentFilePatterns"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__eaa6596c8c308501e64f72312b61619122995461454ed8ae0fe053f0b8e029c0)
                check_type(argname="argument host_url", value=host_url, expected_type=type_hints["host_url"])
                check_type(argname="argument secret_arn", value=secret_arn, expected_type=type_hints["secret_arn"])
                check_type(argname="argument service_now_build_version", value=service_now_build_version, expected_type=type_hints["service_now_build_version"])
                check_type(argname="argument authentication_type", value=authentication_type, expected_type=type_hints["authentication_type"])
                check_type(argname="argument knowledge_article_configuration", value=knowledge_article_configuration, expected_type=type_hints["knowledge_article_configuration"])
                check_type(argname="argument service_catalog_configuration", value=service_catalog_configuration, expected_type=type_hints["service_catalog_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "host_url": host_url,
                "secret_arn": secret_arn,
                "service_now_build_version": service_now_build_version,
            }
            if authentication_type is not None:
                self._values["authentication_type"] = authentication_type
            if knowledge_article_configuration is not None:
                self._values["knowledge_article_configuration"] = knowledge_article_configuration
            if service_catalog_configuration is not None:
                self._values["service_catalog_configuration"] = service_catalog_configuration

        @builtins.property
        def host_url(self) -> builtins.str:
            '''The ServiceNow instance that the data source connects to.

            The host endpoint should look like the following: *{instance}.service-now.com.*

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowconfiguration.html#cfn-kendra-datasource-servicenowconfiguration-hosturl
            '''
            result = self._values.get("host_url")
            assert result is not None, "Required property 'host_url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def secret_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the AWS Secrets Manager secret that contains the user name and password required to connect to the ServiceNow instance.

            You can also provide OAuth authentication credentials of user name, password, client ID, and client secret. For more information, see `Using a ServiceNow data source <https://docs.aws.amazon.com/kendra/latest/dg/data-source-servicenow.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowconfiguration.html#cfn-kendra-datasource-servicenowconfiguration-secretarn
            '''
            result = self._values.get("secret_arn")
            assert result is not None, "Required property 'secret_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def service_now_build_version(self) -> builtins.str:
            '''The identifier of the release that the ServiceNow host is running.

            If the host is not running the ``LONDON`` release, use ``OTHERS`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowconfiguration.html#cfn-kendra-datasource-servicenowconfiguration-servicenowbuildversion
            '''
            result = self._values.get("service_now_build_version")
            assert result is not None, "Required property 'service_now_build_version' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def authentication_type(self) -> typing.Optional[builtins.str]:
            '''The type of authentication used to connect to the ServiceNow instance.

            If you choose ``HTTP_BASIC`` , Amazon Kendra is authenticated using the user name and password provided in the AWS Secrets Manager secret in the ``SecretArn`` field. If you choose ``OAUTH2`` , Amazon Kendra is authenticated using the credentials of client ID, client secret, user name and password.

            When you use ``OAUTH2`` authentication, you must generate a token and a client secret using the ServiceNow console. For more information, see `Using a ServiceNow data source <https://docs.aws.amazon.com/kendra/latest/dg/data-source-servicenow.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowconfiguration.html#cfn-kendra-datasource-servicenowconfiguration-authenticationtype
            '''
            result = self._values.get("authentication_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def knowledge_article_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.ServiceNowKnowledgeArticleConfigurationProperty"]]:
            '''Configuration information for crawling knowledge articles in the ServiceNow site.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowconfiguration.html#cfn-kendra-datasource-servicenowconfiguration-knowledgearticleconfiguration
            '''
            result = self._values.get("knowledge_article_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.ServiceNowKnowledgeArticleConfigurationProperty"]], result)

        @builtins.property
        def service_catalog_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.ServiceNowServiceCatalogConfigurationProperty"]]:
            '''Configuration information for crawling service catalogs in the ServiceNow site.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowconfiguration.html#cfn-kendra-datasource-servicenowconfiguration-servicecatalogconfiguration
            '''
            result = self._values.get("service_catalog_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.ServiceNowServiceCatalogConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServiceNowConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.ServiceNowKnowledgeArticleConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "document_data_field_name": "documentDataFieldName",
            "crawl_attachments": "crawlAttachments",
            "document_title_field_name": "documentTitleFieldName",
            "exclude_attachment_file_patterns": "excludeAttachmentFilePatterns",
            "field_mappings": "fieldMappings",
            "filter_query": "filterQuery",
            "include_attachment_file_patterns": "includeAttachmentFilePatterns",
        },
    )
    class ServiceNowKnowledgeArticleConfigurationProperty:
        def __init__(
            self,
            *,
            document_data_field_name: builtins.str,
            crawl_attachments: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            document_title_field_name: typing.Optional[builtins.str] = None,
            exclude_attachment_file_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
            field_mappings: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            filter_query: typing.Optional[builtins.str] = None,
            include_attachment_file_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Provides the configuration information for crawling knowledge articles in the ServiceNow site.

            :param document_data_field_name: The name of the ServiceNow field that is mapped to the index document contents field in the Amazon Kendra index.
            :param crawl_attachments: ``TRUE`` to index attachments to knowledge articles.
            :param document_title_field_name: The name of the ServiceNow field that is mapped to the index document title field.
            :param exclude_attachment_file_patterns: A list of regular expression patterns to exclude certain attachments of knowledge articles in your ServiceNow. Item that match the patterns are excluded from the index. Items that don't match the patterns are included in the index. If an item matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the item isn't included in the index. The regex is applied to the field specified in the ``PatternTargetField`` .
            :param field_mappings: Maps attributes or field names of knoweldge articles to Amazon Kendra index field names. To create custom fields, use the ``UpdateIndex`` API before you map to ServiceNow fields. For more information, see `Mapping data source fields <https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html>`_ . The ServiceNow data source field names must exist in your ServiceNow custom metadata.
            :param filter_query: A query that selects the knowledge articles to index. The query can return articles from multiple knowledge bases, and the knowledge bases can be public or private. The query string must be one generated by the ServiceNow console. For more information, see `Specifying documents to index with a query <https://docs.aws.amazon.com/kendra/latest/dg/servicenow-query.html>`_ .
            :param include_attachment_file_patterns: A list of regular expression patterns to include certain attachments of knowledge articles in your ServiceNow. Item that match the patterns are included in the index. Items that don't match the patterns are excluded from the index. If an item matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the item isn't included in the index. The regex is applied to the field specified in the ``PatternTargetField`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowknowledgearticleconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                service_now_knowledge_article_configuration_property = kendra.CfnDataSource.ServiceNowKnowledgeArticleConfigurationProperty(
                    document_data_field_name="documentDataFieldName",
                
                    # the properties below are optional
                    crawl_attachments=False,
                    document_title_field_name="documentTitleFieldName",
                    exclude_attachment_file_patterns=["excludeAttachmentFilePatterns"],
                    field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                        data_source_field_name="dataSourceFieldName",
                        index_field_name="indexFieldName",
                
                        # the properties below are optional
                        date_field_format="dateFieldFormat"
                    )],
                    filter_query="filterQuery",
                    include_attachment_file_patterns=["includeAttachmentFilePatterns"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d01a96040c4e7f6dfc7efc09a5b83b28f0019321a6f9a00ca365a421c7455a9a)
                check_type(argname="argument document_data_field_name", value=document_data_field_name, expected_type=type_hints["document_data_field_name"])
                check_type(argname="argument crawl_attachments", value=crawl_attachments, expected_type=type_hints["crawl_attachments"])
                check_type(argname="argument document_title_field_name", value=document_title_field_name, expected_type=type_hints["document_title_field_name"])
                check_type(argname="argument exclude_attachment_file_patterns", value=exclude_attachment_file_patterns, expected_type=type_hints["exclude_attachment_file_patterns"])
                check_type(argname="argument field_mappings", value=field_mappings, expected_type=type_hints["field_mappings"])
                check_type(argname="argument filter_query", value=filter_query, expected_type=type_hints["filter_query"])
                check_type(argname="argument include_attachment_file_patterns", value=include_attachment_file_patterns, expected_type=type_hints["include_attachment_file_patterns"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "document_data_field_name": document_data_field_name,
            }
            if crawl_attachments is not None:
                self._values["crawl_attachments"] = crawl_attachments
            if document_title_field_name is not None:
                self._values["document_title_field_name"] = document_title_field_name
            if exclude_attachment_file_patterns is not None:
                self._values["exclude_attachment_file_patterns"] = exclude_attachment_file_patterns
            if field_mappings is not None:
                self._values["field_mappings"] = field_mappings
            if filter_query is not None:
                self._values["filter_query"] = filter_query
            if include_attachment_file_patterns is not None:
                self._values["include_attachment_file_patterns"] = include_attachment_file_patterns

        @builtins.property
        def document_data_field_name(self) -> builtins.str:
            '''The name of the ServiceNow field that is mapped to the index document contents field in the Amazon Kendra index.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowknowledgearticleconfiguration.html#cfn-kendra-datasource-servicenowknowledgearticleconfiguration-documentdatafieldname
            '''
            result = self._values.get("document_data_field_name")
            assert result is not None, "Required property 'document_data_field_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def crawl_attachments(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''``TRUE`` to index attachments to knowledge articles.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowknowledgearticleconfiguration.html#cfn-kendra-datasource-servicenowknowledgearticleconfiguration-crawlattachments
            '''
            result = self._values.get("crawl_attachments")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def document_title_field_name(self) -> typing.Optional[builtins.str]:
            '''The name of the ServiceNow field that is mapped to the index document title field.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowknowledgearticleconfiguration.html#cfn-kendra-datasource-servicenowknowledgearticleconfiguration-documenttitlefieldname
            '''
            result = self._values.get("document_title_field_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def exclude_attachment_file_patterns(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of regular expression patterns to exclude certain attachments of knowledge articles in your ServiceNow.

            Item that match the patterns are excluded from the index. Items that don't match the patterns are included in the index. If an item matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the item isn't included in the index.

            The regex is applied to the field specified in the ``PatternTargetField`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowknowledgearticleconfiguration.html#cfn-kendra-datasource-servicenowknowledgearticleconfiguration-excludeattachmentfilepatterns
            '''
            result = self._values.get("exclude_attachment_file_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def field_mappings(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DataSourceToIndexFieldMappingProperty"]]]]:
            '''Maps attributes or field names of knoweldge articles to Amazon Kendra index field names.

            To create custom fields, use the ``UpdateIndex`` API before you map to ServiceNow fields. For more information, see `Mapping data source fields <https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html>`_ . The ServiceNow data source field names must exist in your ServiceNow custom metadata.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowknowledgearticleconfiguration.html#cfn-kendra-datasource-servicenowknowledgearticleconfiguration-fieldmappings
            '''
            result = self._values.get("field_mappings")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DataSourceToIndexFieldMappingProperty"]]]], result)

        @builtins.property
        def filter_query(self) -> typing.Optional[builtins.str]:
            '''A query that selects the knowledge articles to index.

            The query can return articles from multiple knowledge bases, and the knowledge bases can be public or private.

            The query string must be one generated by the ServiceNow console. For more information, see `Specifying documents to index with a query <https://docs.aws.amazon.com/kendra/latest/dg/servicenow-query.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowknowledgearticleconfiguration.html#cfn-kendra-datasource-servicenowknowledgearticleconfiguration-filterquery
            '''
            result = self._values.get("filter_query")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def include_attachment_file_patterns(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of regular expression patterns to include certain attachments of knowledge articles in your ServiceNow.

            Item that match the patterns are included in the index. Items that don't match the patterns are excluded from the index. If an item matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the item isn't included in the index.

            The regex is applied to the field specified in the ``PatternTargetField`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowknowledgearticleconfiguration.html#cfn-kendra-datasource-servicenowknowledgearticleconfiguration-includeattachmentfilepatterns
            '''
            result = self._values.get("include_attachment_file_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServiceNowKnowledgeArticleConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.ServiceNowServiceCatalogConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "document_data_field_name": "documentDataFieldName",
            "crawl_attachments": "crawlAttachments",
            "document_title_field_name": "documentTitleFieldName",
            "exclude_attachment_file_patterns": "excludeAttachmentFilePatterns",
            "field_mappings": "fieldMappings",
            "include_attachment_file_patterns": "includeAttachmentFilePatterns",
        },
    )
    class ServiceNowServiceCatalogConfigurationProperty:
        def __init__(
            self,
            *,
            document_data_field_name: builtins.str,
            crawl_attachments: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            document_title_field_name: typing.Optional[builtins.str] = None,
            exclude_attachment_file_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
            field_mappings: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            include_attachment_file_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Provides the configuration information for crawling service catalog items in the ServiceNow site.

            :param document_data_field_name: The name of the ServiceNow field that is mapped to the index document contents field in the Amazon Kendra index.
            :param crawl_attachments: ``TRUE`` to index attachments to service catalog items.
            :param document_title_field_name: The name of the ServiceNow field that is mapped to the index document title field.
            :param exclude_attachment_file_patterns: A list of regular expression patterns to exclude certain attachments of catalogs in your ServiceNow. Item that match the patterns are excluded from the index. Items that don't match the patterns are included in the index. If an item matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the item isn't included in the index. The regex is applied to the file name of the attachment.
            :param field_mappings: Maps attributes or field names of catalogs to Amazon Kendra index field names. To create custom fields, use the ``UpdateIndex`` API before you map to ServiceNow fields. For more information, see `Mapping data source fields <https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html>`_ . The ServiceNow data source field names must exist in your ServiceNow custom metadata.
            :param include_attachment_file_patterns: A list of regular expression patterns to include certain attachments of catalogs in your ServiceNow. Item that match the patterns are included in the index. Items that don't match the patterns are excluded from the index. If an item matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the item isn't included in the index. The regex is applied to the file name of the attachment.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowservicecatalogconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                service_now_service_catalog_configuration_property = kendra.CfnDataSource.ServiceNowServiceCatalogConfigurationProperty(
                    document_data_field_name="documentDataFieldName",
                
                    # the properties below are optional
                    crawl_attachments=False,
                    document_title_field_name="documentTitleFieldName",
                    exclude_attachment_file_patterns=["excludeAttachmentFilePatterns"],
                    field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                        data_source_field_name="dataSourceFieldName",
                        index_field_name="indexFieldName",
                
                        # the properties below are optional
                        date_field_format="dateFieldFormat"
                    )],
                    include_attachment_file_patterns=["includeAttachmentFilePatterns"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4afd6863fb6363d54df26260263b705ca1257cf3b112217ea98696c920433bdb)
                check_type(argname="argument document_data_field_name", value=document_data_field_name, expected_type=type_hints["document_data_field_name"])
                check_type(argname="argument crawl_attachments", value=crawl_attachments, expected_type=type_hints["crawl_attachments"])
                check_type(argname="argument document_title_field_name", value=document_title_field_name, expected_type=type_hints["document_title_field_name"])
                check_type(argname="argument exclude_attachment_file_patterns", value=exclude_attachment_file_patterns, expected_type=type_hints["exclude_attachment_file_patterns"])
                check_type(argname="argument field_mappings", value=field_mappings, expected_type=type_hints["field_mappings"])
                check_type(argname="argument include_attachment_file_patterns", value=include_attachment_file_patterns, expected_type=type_hints["include_attachment_file_patterns"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "document_data_field_name": document_data_field_name,
            }
            if crawl_attachments is not None:
                self._values["crawl_attachments"] = crawl_attachments
            if document_title_field_name is not None:
                self._values["document_title_field_name"] = document_title_field_name
            if exclude_attachment_file_patterns is not None:
                self._values["exclude_attachment_file_patterns"] = exclude_attachment_file_patterns
            if field_mappings is not None:
                self._values["field_mappings"] = field_mappings
            if include_attachment_file_patterns is not None:
                self._values["include_attachment_file_patterns"] = include_attachment_file_patterns

        @builtins.property
        def document_data_field_name(self) -> builtins.str:
            '''The name of the ServiceNow field that is mapped to the index document contents field in the Amazon Kendra index.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowservicecatalogconfiguration.html#cfn-kendra-datasource-servicenowservicecatalogconfiguration-documentdatafieldname
            '''
            result = self._values.get("document_data_field_name")
            assert result is not None, "Required property 'document_data_field_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def crawl_attachments(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''``TRUE`` to index attachments to service catalog items.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowservicecatalogconfiguration.html#cfn-kendra-datasource-servicenowservicecatalogconfiguration-crawlattachments
            '''
            result = self._values.get("crawl_attachments")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def document_title_field_name(self) -> typing.Optional[builtins.str]:
            '''The name of the ServiceNow field that is mapped to the index document title field.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowservicecatalogconfiguration.html#cfn-kendra-datasource-servicenowservicecatalogconfiguration-documenttitlefieldname
            '''
            result = self._values.get("document_title_field_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def exclude_attachment_file_patterns(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of regular expression patterns to exclude certain attachments of catalogs in your ServiceNow.

            Item that match the patterns are excluded from the index. Items that don't match the patterns are included in the index. If an item matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the item isn't included in the index.

            The regex is applied to the file name of the attachment.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowservicecatalogconfiguration.html#cfn-kendra-datasource-servicenowservicecatalogconfiguration-excludeattachmentfilepatterns
            '''
            result = self._values.get("exclude_attachment_file_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def field_mappings(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DataSourceToIndexFieldMappingProperty"]]]]:
            '''Maps attributes or field names of catalogs to Amazon Kendra index field names.

            To create custom fields, use the ``UpdateIndex`` API before you map to ServiceNow fields. For more information, see `Mapping data source fields <https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html>`_ . The ServiceNow data source field names must exist in your ServiceNow custom metadata.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowservicecatalogconfiguration.html#cfn-kendra-datasource-servicenowservicecatalogconfiguration-fieldmappings
            '''
            result = self._values.get("field_mappings")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DataSourceToIndexFieldMappingProperty"]]]], result)

        @builtins.property
        def include_attachment_file_patterns(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of regular expression patterns to include certain attachments of catalogs in your ServiceNow.

            Item that match the patterns are included in the index. Items that don't match the patterns are excluded from the index. If an item matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the item isn't included in the index.

            The regex is applied to the file name of the attachment.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-servicenowservicecatalogconfiguration.html#cfn-kendra-datasource-servicenowservicecatalogconfiguration-includeattachmentfilepatterns
            '''
            result = self._values.get("include_attachment_file_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServiceNowServiceCatalogConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.SharePointConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "secret_arn": "secretArn",
            "share_point_version": "sharePointVersion",
            "urls": "urls",
            "crawl_attachments": "crawlAttachments",
            "disable_local_groups": "disableLocalGroups",
            "document_title_field_name": "documentTitleFieldName",
            "exclusion_patterns": "exclusionPatterns",
            "field_mappings": "fieldMappings",
            "inclusion_patterns": "inclusionPatterns",
            "ssl_certificate_s3_path": "sslCertificateS3Path",
            "use_change_log": "useChangeLog",
            "vpc_configuration": "vpcConfiguration",
        },
    )
    class SharePointConfigurationProperty:
        def __init__(
            self,
            *,
            secret_arn: builtins.str,
            share_point_version: builtins.str,
            urls: typing.Sequence[builtins.str],
            crawl_attachments: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            disable_local_groups: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            document_title_field_name: typing.Optional[builtins.str] = None,
            exclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
            field_mappings: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            inclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
            ssl_certificate_s3_path: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.S3PathProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            use_change_log: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            vpc_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.DataSourceVpcConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Provides the configuration information to connect to Microsoft SharePoint as your data source.

            :param secret_arn: The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains the user name and password required to connect to the SharePoint instance. If you use SharePoint Server, you also need to provide the sever domain name as part of the credentials. For more information, see `Using a Microsoft SharePoint Data Source <https://docs.aws.amazon.com/kendra/latest/dg/data-source-sharepoint.html>`_ . You can also provide OAuth authentication credentials of user name, password, client ID, and client secret. For more information, see `Using a SharePoint data source <https://docs.aws.amazon.com/kendra/latest/dg/data-source-sharepoint.html>`_ .
            :param share_point_version: The version of Microsoft SharePoint that you use.
            :param urls: The Microsoft SharePoint site URLs for the documents you want to index.
            :param crawl_attachments: ``TRUE`` to index document attachments.
            :param disable_local_groups: ``TRUE`` to disable local groups information.
            :param document_title_field_name: The Microsoft SharePoint attribute field that contains the title of the document.
            :param exclusion_patterns: A list of regular expression patterns. Documents that match the patterns are excluded from the index. Documents that don't match the patterns are included in the index. If a document matches both an exclusion pattern and an inclusion pattern, the document is not included in the index. The regex is applied to the display URL of the SharePoint document.
            :param field_mappings: A list of ``DataSourceToIndexFieldMapping`` objects that map Microsoft SharePoint attributes or fields to Amazon Kendra index fields. You must first create the index fields using the `UpdateIndex <https://docs.aws.amazon.com/kendra/latest/dg/API_UpdateIndex.html>`_ operation before you map SharePoint attributes. For more information, see `Mapping Data Source Fields <https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html>`_ .
            :param inclusion_patterns: A list of regular expression patterns to include certain documents in your SharePoint. Documents that match the patterns are included in the index. Documents that don't match the patterns are excluded from the index. If a document matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the document isn't included in the index. The regex applies to the display URL of the SharePoint document.
            :param ssl_certificate_s3_path: Information required to find a specific file in an Amazon S3 bucket.
            :param use_change_log: ``TRUE`` to use the SharePoint change log to determine which documents require updating in the index. Depending on the change log's size, it may take longer for Amazon Kendra to use the change log than to scan all of your documents in SharePoint.
            :param vpc_configuration: Provides information for connecting to an Amazon VPC.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                share_point_configuration_property = kendra.CfnDataSource.SharePointConfigurationProperty(
                    secret_arn="secretArn",
                    share_point_version="sharePointVersion",
                    urls=["urls"],
                
                    # the properties below are optional
                    crawl_attachments=False,
                    disable_local_groups=False,
                    document_title_field_name="documentTitleFieldName",
                    exclusion_patterns=["exclusionPatterns"],
                    field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                        data_source_field_name="dataSourceFieldName",
                        index_field_name="indexFieldName",
                
                        # the properties below are optional
                        date_field_format="dateFieldFormat"
                    )],
                    inclusion_patterns=["inclusionPatterns"],
                    ssl_certificate_s3_path=kendra.CfnDataSource.S3PathProperty(
                        bucket="bucket",
                        key="key"
                    ),
                    use_change_log=False,
                    vpc_configuration=kendra.CfnDataSource.DataSourceVpcConfigurationProperty(
                        security_group_ids=["securityGroupIds"],
                        subnet_ids=["subnetIds"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__33b31cc3720195569251ffa27b4503a6c9e1d6ccae8db446cb20132abd4410c6)
                check_type(argname="argument secret_arn", value=secret_arn, expected_type=type_hints["secret_arn"])
                check_type(argname="argument share_point_version", value=share_point_version, expected_type=type_hints["share_point_version"])
                check_type(argname="argument urls", value=urls, expected_type=type_hints["urls"])
                check_type(argname="argument crawl_attachments", value=crawl_attachments, expected_type=type_hints["crawl_attachments"])
                check_type(argname="argument disable_local_groups", value=disable_local_groups, expected_type=type_hints["disable_local_groups"])
                check_type(argname="argument document_title_field_name", value=document_title_field_name, expected_type=type_hints["document_title_field_name"])
                check_type(argname="argument exclusion_patterns", value=exclusion_patterns, expected_type=type_hints["exclusion_patterns"])
                check_type(argname="argument field_mappings", value=field_mappings, expected_type=type_hints["field_mappings"])
                check_type(argname="argument inclusion_patterns", value=inclusion_patterns, expected_type=type_hints["inclusion_patterns"])
                check_type(argname="argument ssl_certificate_s3_path", value=ssl_certificate_s3_path, expected_type=type_hints["ssl_certificate_s3_path"])
                check_type(argname="argument use_change_log", value=use_change_log, expected_type=type_hints["use_change_log"])
                check_type(argname="argument vpc_configuration", value=vpc_configuration, expected_type=type_hints["vpc_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "secret_arn": secret_arn,
                "share_point_version": share_point_version,
                "urls": urls,
            }
            if crawl_attachments is not None:
                self._values["crawl_attachments"] = crawl_attachments
            if disable_local_groups is not None:
                self._values["disable_local_groups"] = disable_local_groups
            if document_title_field_name is not None:
                self._values["document_title_field_name"] = document_title_field_name
            if exclusion_patterns is not None:
                self._values["exclusion_patterns"] = exclusion_patterns
            if field_mappings is not None:
                self._values["field_mappings"] = field_mappings
            if inclusion_patterns is not None:
                self._values["inclusion_patterns"] = inclusion_patterns
            if ssl_certificate_s3_path is not None:
                self._values["ssl_certificate_s3_path"] = ssl_certificate_s3_path
            if use_change_log is not None:
                self._values["use_change_log"] = use_change_log
            if vpc_configuration is not None:
                self._values["vpc_configuration"] = vpc_configuration

        @builtins.property
        def secret_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that contains the user name and password required to connect to the SharePoint instance.

            If you use SharePoint Server, you also need to provide the sever domain name as part of the credentials. For more information, see `Using a Microsoft SharePoint Data Source <https://docs.aws.amazon.com/kendra/latest/dg/data-source-sharepoint.html>`_ .

            You can also provide OAuth authentication credentials of user name, password, client ID, and client secret. For more information, see `Using a SharePoint data source <https://docs.aws.amazon.com/kendra/latest/dg/data-source-sharepoint.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html#cfn-kendra-datasource-sharepointconfiguration-secretarn
            '''
            result = self._values.get("secret_arn")
            assert result is not None, "Required property 'secret_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def share_point_version(self) -> builtins.str:
            '''The version of Microsoft SharePoint that you use.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html#cfn-kendra-datasource-sharepointconfiguration-sharepointversion
            '''
            result = self._values.get("share_point_version")
            assert result is not None, "Required property 'share_point_version' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def urls(self) -> typing.List[builtins.str]:
            '''The Microsoft SharePoint site URLs for the documents you want to index.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html#cfn-kendra-datasource-sharepointconfiguration-urls
            '''
            result = self._values.get("urls")
            assert result is not None, "Required property 'urls' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def crawl_attachments(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''``TRUE`` to index document attachments.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html#cfn-kendra-datasource-sharepointconfiguration-crawlattachments
            '''
            result = self._values.get("crawl_attachments")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def disable_local_groups(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''``TRUE`` to disable local groups information.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html#cfn-kendra-datasource-sharepointconfiguration-disablelocalgroups
            '''
            result = self._values.get("disable_local_groups")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def document_title_field_name(self) -> typing.Optional[builtins.str]:
            '''The Microsoft SharePoint attribute field that contains the title of the document.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html#cfn-kendra-datasource-sharepointconfiguration-documenttitlefieldname
            '''
            result = self._values.get("document_title_field_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def exclusion_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of regular expression patterns.

            Documents that match the patterns are excluded from the index. Documents that don't match the patterns are included in the index. If a document matches both an exclusion pattern and an inclusion pattern, the document is not included in the index.

            The regex is applied to the display URL of the SharePoint document.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html#cfn-kendra-datasource-sharepointconfiguration-exclusionpatterns
            '''
            result = self._values.get("exclusion_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def field_mappings(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DataSourceToIndexFieldMappingProperty"]]]]:
            '''A list of ``DataSourceToIndexFieldMapping`` objects that map Microsoft SharePoint attributes or fields to Amazon Kendra index fields.

            You must first create the index fields using the `UpdateIndex <https://docs.aws.amazon.com/kendra/latest/dg/API_UpdateIndex.html>`_ operation before you map SharePoint attributes. For more information, see `Mapping Data Source Fields <https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html#cfn-kendra-datasource-sharepointconfiguration-fieldmappings
            '''
            result = self._values.get("field_mappings")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DataSourceToIndexFieldMappingProperty"]]]], result)

        @builtins.property
        def inclusion_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of regular expression patterns to include certain documents in your SharePoint.

            Documents that match the patterns are included in the index. Documents that don't match the patterns are excluded from the index. If a document matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the document isn't included in the index.

            The regex applies to the display URL of the SharePoint document.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html#cfn-kendra-datasource-sharepointconfiguration-inclusionpatterns
            '''
            result = self._values.get("inclusion_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def ssl_certificate_s3_path(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.S3PathProperty"]]:
            '''Information required to find a specific file in an Amazon S3 bucket.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html#cfn-kendra-datasource-sharepointconfiguration-sslcertificates3path
            '''
            result = self._values.get("ssl_certificate_s3_path")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.S3PathProperty"]], result)

        @builtins.property
        def use_change_log(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''``TRUE`` to use the SharePoint change log to determine which documents require updating in the index.

            Depending on the change log's size, it may take longer for Amazon Kendra to use the change log than to scan all of your documents in SharePoint.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html#cfn-kendra-datasource-sharepointconfiguration-usechangelog
            '''
            result = self._values.get("use_change_log")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def vpc_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DataSourceVpcConfigurationProperty"]]:
            '''Provides information for connecting to an Amazon VPC.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sharepointconfiguration.html#cfn-kendra-datasource-sharepointconfiguration-vpcconfiguration
            '''
            result = self._values.get("vpc_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DataSourceVpcConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SharePointConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.SqlConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "query_identifiers_enclosing_option": "queryIdentifiersEnclosingOption",
        },
    )
    class SqlConfigurationProperty:
        def __init__(
            self,
            *,
            query_identifiers_enclosing_option: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides information that configures Amazon Kendra to use a SQL database.

            :param query_identifiers_enclosing_option: Determines whether Amazon Kendra encloses SQL identifiers for tables and column names in double quotes (") when making a database query. You can set the value to ``DOUBLE_QUOTES`` or ``NONE`` . By default, Amazon Kendra passes SQL identifiers the way that they are entered into the data source configuration. It does not change the case of identifiers or enclose them in quotes. PostgreSQL internally converts uppercase characters to lower case characters in identifiers unless they are quoted. Choosing this option encloses identifiers in quotes so that PostgreSQL does not convert the character's case. For MySQL databases, you must enable the ansi_quotes option when you set this field to ``DOUBLE_QUOTES`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sqlconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                sql_configuration_property = kendra.CfnDataSource.SqlConfigurationProperty(
                    query_identifiers_enclosing_option="queryIdentifiersEnclosingOption"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fb1d3fe487d9060882af04e9daee5af8c6c483e8167066d025070c4b426f7de3)
                check_type(argname="argument query_identifiers_enclosing_option", value=query_identifiers_enclosing_option, expected_type=type_hints["query_identifiers_enclosing_option"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if query_identifiers_enclosing_option is not None:
                self._values["query_identifiers_enclosing_option"] = query_identifiers_enclosing_option

        @builtins.property
        def query_identifiers_enclosing_option(self) -> typing.Optional[builtins.str]:
            '''Determines whether Amazon Kendra encloses SQL identifiers for tables and column names in double quotes (") when making a database query.

            You can set the value to ``DOUBLE_QUOTES`` or ``NONE`` .

            By default, Amazon Kendra passes SQL identifiers the way that they are entered into the data source configuration. It does not change the case of identifiers or enclose them in quotes.

            PostgreSQL internally converts uppercase characters to lower case characters in identifiers unless they are quoted. Choosing this option encloses identifiers in quotes so that PostgreSQL does not convert the character's case.

            For MySQL databases, you must enable the ansi_quotes option when you set this field to ``DOUBLE_QUOTES`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-sqlconfiguration.html#cfn-kendra-datasource-sqlconfiguration-queryidentifiersenclosingoption
            '''
            result = self._values.get("query_identifiers_enclosing_option")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SqlConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.WebCrawlerAuthenticationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"basic_authentication": "basicAuthentication"},
    )
    class WebCrawlerAuthenticationConfigurationProperty:
        def __init__(
            self,
            *,
            basic_authentication: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.WebCrawlerBasicAuthenticationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Provides the configuration information to connect to websites that require user authentication.

            :param basic_authentication: The list of configuration information that's required to connect to and crawl a website host using basic authentication credentials. The list includes the name and port number of the website host.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerauthenticationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                web_crawler_authentication_configuration_property = kendra.CfnDataSource.WebCrawlerAuthenticationConfigurationProperty(
                    basic_authentication=[kendra.CfnDataSource.WebCrawlerBasicAuthenticationProperty(
                        credentials="credentials",
                        host="host",
                        port=123
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5bc0f5447a7fb82df9fef5eaf21c792414d86f01c91224795ced30c7b2f67c71)
                check_type(argname="argument basic_authentication", value=basic_authentication, expected_type=type_hints["basic_authentication"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if basic_authentication is not None:
                self._values["basic_authentication"] = basic_authentication

        @builtins.property
        def basic_authentication(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.WebCrawlerBasicAuthenticationProperty"]]]]:
            '''The list of configuration information that's required to connect to and crawl a website host using basic authentication credentials.

            The list includes the name and port number of the website host.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerauthenticationconfiguration.html#cfn-kendra-datasource-webcrawlerauthenticationconfiguration-basicauthentication
            '''
            result = self._values.get("basic_authentication")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.WebCrawlerBasicAuthenticationProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WebCrawlerAuthenticationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.WebCrawlerBasicAuthenticationProperty",
        jsii_struct_bases=[],
        name_mapping={"credentials": "credentials", "host": "host", "port": "port"},
    )
    class WebCrawlerBasicAuthenticationProperty:
        def __init__(
            self,
            *,
            credentials: builtins.str,
            host: builtins.str,
            port: jsii.Number,
        ) -> None:
            '''Provides the configuration information to connect to websites that require basic user authentication.

            :param credentials: Your secret ARN, which you can create in `AWS Secrets Manager <https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html>`_. You use a secret if basic authentication credentials are required to connect to a website. The secret stores your credentials of user name and password.
            :param host: The name of the website host you want to connect to using authentication credentials. For example, the host name of https://a.example.com/page1.html is "a.example.com".
            :param port: The port number of the website host you want to connect to using authentication credentials. For example, the port for https://a.example.com/page1.html is 443, the standard port for HTTPS.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerbasicauthentication.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                web_crawler_basic_authentication_property = kendra.CfnDataSource.WebCrawlerBasicAuthenticationProperty(
                    credentials="credentials",
                    host="host",
                    port=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a4fc4beda7b6d0eaae8fd147a36d7ac4d0b64b3d7190a4e2fd1288720dc58357)
                check_type(argname="argument credentials", value=credentials, expected_type=type_hints["credentials"])
                check_type(argname="argument host", value=host, expected_type=type_hints["host"])
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "credentials": credentials,
                "host": host,
                "port": port,
            }

        @builtins.property
        def credentials(self) -> builtins.str:
            '''Your secret ARN, which you can create in `AWS Secrets Manager <https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html>`_.

            You use a secret if basic authentication credentials are required to connect to a website. The secret stores your credentials of user name and password.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerbasicauthentication.html#cfn-kendra-datasource-webcrawlerbasicauthentication-credentials
            '''
            result = self._values.get("credentials")
            assert result is not None, "Required property 'credentials' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def host(self) -> builtins.str:
            '''The name of the website host you want to connect to using authentication credentials.

            For example, the host name of https://a.example.com/page1.html is "a.example.com".

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerbasicauthentication.html#cfn-kendra-datasource-webcrawlerbasicauthentication-host
            '''
            result = self._values.get("host")
            assert result is not None, "Required property 'host' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def port(self) -> jsii.Number:
            '''The port number of the website host you want to connect to using authentication credentials.

            For example, the port for https://a.example.com/page1.html is 443, the standard port for HTTPS.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerbasicauthentication.html#cfn-kendra-datasource-webcrawlerbasicauthentication-port
            '''
            result = self._values.get("port")
            assert result is not None, "Required property 'port' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WebCrawlerBasicAuthenticationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.WebCrawlerConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "urls": "urls",
            "authentication_configuration": "authenticationConfiguration",
            "crawl_depth": "crawlDepth",
            "max_content_size_per_page_in_mega_bytes": "maxContentSizePerPageInMegaBytes",
            "max_links_per_page": "maxLinksPerPage",
            "max_urls_per_minute_crawl_rate": "maxUrlsPerMinuteCrawlRate",
            "proxy_configuration": "proxyConfiguration",
            "url_exclusion_patterns": "urlExclusionPatterns",
            "url_inclusion_patterns": "urlInclusionPatterns",
        },
    )
    class WebCrawlerConfigurationProperty:
        def __init__(
            self,
            *,
            urls: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.WebCrawlerUrlsProperty", typing.Dict[builtins.str, typing.Any]]],
            authentication_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.WebCrawlerAuthenticationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            crawl_depth: typing.Optional[jsii.Number] = None,
            max_content_size_per_page_in_mega_bytes: typing.Optional[jsii.Number] = None,
            max_links_per_page: typing.Optional[jsii.Number] = None,
            max_urls_per_minute_crawl_rate: typing.Optional[jsii.Number] = None,
            proxy_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.ProxyConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            url_exclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
            url_inclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Provides the configuration information required for Amazon Kendra Web Crawler.

            :param urls: Specifies the seed or starting point URLs of the websites or the sitemap URLs of the websites you want to crawl. You can include website subdomains. You can list up to 100 seed URLs and up to three sitemap URLs. You can only crawl websites that use the secure communication protocol, Hypertext Transfer Protocol Secure (HTTPS). If you receive an error when crawling a website, it could be that the website is blocked from crawling. *When selecting websites to index, you must adhere to the `Amazon Acceptable Use Policy <https://docs.aws.amazon.com/aup/>`_ and all other Amazon terms. Remember that you must only use Amazon Kendra Web Crawler to index your own webpages, or webpages that you have authorization to index.*
            :param authentication_configuration: Configuration information required to connect to websites using authentication. You can connect to websites using basic authentication of user name and password. You use a secret in `AWS Secrets Manager <https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html>`_ to store your authentication credentials. You must provide the website host name and port number. For example, the host name of https://a.example.com/page1.html is "a.example.com" and the port is 443, the standard port for HTTPS.
            :param crawl_depth: Specifies the number of levels in a website that you want to crawl. The first level begins from the website seed or starting point URL. For example, if a website has 3 levels – index level (i.e. seed in this example), sections level, and subsections level – and you are only interested in crawling information up to the sections level (i.e. levels 0-1), you can set your depth to 1. The default crawl depth is set to 2.
            :param max_content_size_per_page_in_mega_bytes: The maximum size (in MB) of a webpage or attachment to crawl. Files larger than this size (in MB) are skipped/not crawled. The default maximum size of a webpage or attachment is set to 50 MB.
            :param max_links_per_page: The maximum number of URLs on a webpage to include when crawling a website. This number is per webpage. As a website’s webpages are crawled, any URLs the webpages link to are also crawled. URLs on a webpage are crawled in order of appearance. The default maximum links per page is 100.
            :param max_urls_per_minute_crawl_rate: The maximum number of URLs crawled per website host per minute. A minimum of one URL is required. The default maximum number of URLs crawled per website host per minute is 300.
            :param proxy_configuration: Configuration information required to connect to your internal websites via a web proxy. You must provide the website host name and port number. For example, the host name of https://a.example.com/page1.html is "a.example.com" and the port is 443, the standard port for HTTPS. Web proxy credentials are optional and you can use them to connect to a web proxy server that requires basic authentication. To store web proxy credentials, you use a secret in `AWS Secrets Manager <https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html>`_ .
            :param url_exclusion_patterns: A list of regular expression patterns to exclude certain URLs to crawl. URLs that match the patterns are excluded from the index. URLs that don't match the patterns are included in the index. If a URL matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the URL file isn't included in the index.
            :param url_inclusion_patterns: A list of regular expression patterns to include certain URLs to crawl. URLs that match the patterns are included in the index. URLs that don't match the patterns are excluded from the index. If a URL matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the URL file isn't included in the index.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                web_crawler_configuration_property = kendra.CfnDataSource.WebCrawlerConfigurationProperty(
                    urls=kendra.CfnDataSource.WebCrawlerUrlsProperty(
                        seed_url_configuration=kendra.CfnDataSource.WebCrawlerSeedUrlConfigurationProperty(
                            seed_urls=["seedUrls"],
                
                            # the properties below are optional
                            web_crawler_mode="webCrawlerMode"
                        ),
                        site_maps_configuration=kendra.CfnDataSource.WebCrawlerSiteMapsConfigurationProperty(
                            site_maps=["siteMaps"]
                        )
                    ),
                
                    # the properties below are optional
                    authentication_configuration=kendra.CfnDataSource.WebCrawlerAuthenticationConfigurationProperty(
                        basic_authentication=[kendra.CfnDataSource.WebCrawlerBasicAuthenticationProperty(
                            credentials="credentials",
                            host="host",
                            port=123
                        )]
                    ),
                    crawl_depth=123,
                    max_content_size_per_page_in_mega_bytes=123,
                    max_links_per_page=123,
                    max_urls_per_minute_crawl_rate=123,
                    proxy_configuration=kendra.CfnDataSource.ProxyConfigurationProperty(
                        host="host",
                        port=123,
                
                        # the properties below are optional
                        credentials="credentials"
                    ),
                    url_exclusion_patterns=["urlExclusionPatterns"],
                    url_inclusion_patterns=["urlInclusionPatterns"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__484bbf2bc0472073880a1659d98e973cfe8cfff7c2fc4583c323d9f4fc18a51c)
                check_type(argname="argument urls", value=urls, expected_type=type_hints["urls"])
                check_type(argname="argument authentication_configuration", value=authentication_configuration, expected_type=type_hints["authentication_configuration"])
                check_type(argname="argument crawl_depth", value=crawl_depth, expected_type=type_hints["crawl_depth"])
                check_type(argname="argument max_content_size_per_page_in_mega_bytes", value=max_content_size_per_page_in_mega_bytes, expected_type=type_hints["max_content_size_per_page_in_mega_bytes"])
                check_type(argname="argument max_links_per_page", value=max_links_per_page, expected_type=type_hints["max_links_per_page"])
                check_type(argname="argument max_urls_per_minute_crawl_rate", value=max_urls_per_minute_crawl_rate, expected_type=type_hints["max_urls_per_minute_crawl_rate"])
                check_type(argname="argument proxy_configuration", value=proxy_configuration, expected_type=type_hints["proxy_configuration"])
                check_type(argname="argument url_exclusion_patterns", value=url_exclusion_patterns, expected_type=type_hints["url_exclusion_patterns"])
                check_type(argname="argument url_inclusion_patterns", value=url_inclusion_patterns, expected_type=type_hints["url_inclusion_patterns"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "urls": urls,
            }
            if authentication_configuration is not None:
                self._values["authentication_configuration"] = authentication_configuration
            if crawl_depth is not None:
                self._values["crawl_depth"] = crawl_depth
            if max_content_size_per_page_in_mega_bytes is not None:
                self._values["max_content_size_per_page_in_mega_bytes"] = max_content_size_per_page_in_mega_bytes
            if max_links_per_page is not None:
                self._values["max_links_per_page"] = max_links_per_page
            if max_urls_per_minute_crawl_rate is not None:
                self._values["max_urls_per_minute_crawl_rate"] = max_urls_per_minute_crawl_rate
            if proxy_configuration is not None:
                self._values["proxy_configuration"] = proxy_configuration
            if url_exclusion_patterns is not None:
                self._values["url_exclusion_patterns"] = url_exclusion_patterns
            if url_inclusion_patterns is not None:
                self._values["url_inclusion_patterns"] = url_inclusion_patterns

        @builtins.property
        def urls(
            self,
        ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.WebCrawlerUrlsProperty"]:
            '''Specifies the seed or starting point URLs of the websites or the sitemap URLs of the websites you want to crawl.

            You can include website subdomains. You can list up to 100 seed URLs and up to three sitemap URLs.

            You can only crawl websites that use the secure communication protocol, Hypertext Transfer Protocol Secure (HTTPS). If you receive an error when crawling a website, it could be that the website is blocked from crawling.

            *When selecting websites to index, you must adhere to the `Amazon Acceptable Use Policy <https://docs.aws.amazon.com/aup/>`_ and all other Amazon terms. Remember that you must only use Amazon Kendra Web Crawler to index your own webpages, or webpages that you have authorization to index.*

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerconfiguration.html#cfn-kendra-datasource-webcrawlerconfiguration-urls
            '''
            result = self._values.get("urls")
            assert result is not None, "Required property 'urls' is missing"
            return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.WebCrawlerUrlsProperty"], result)

        @builtins.property
        def authentication_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.WebCrawlerAuthenticationConfigurationProperty"]]:
            '''Configuration information required to connect to websites using authentication.

            You can connect to websites using basic authentication of user name and password. You use a secret in `AWS Secrets Manager <https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html>`_ to store your authentication credentials.

            You must provide the website host name and port number. For example, the host name of https://a.example.com/page1.html is "a.example.com" and the port is 443, the standard port for HTTPS.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerconfiguration.html#cfn-kendra-datasource-webcrawlerconfiguration-authenticationconfiguration
            '''
            result = self._values.get("authentication_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.WebCrawlerAuthenticationConfigurationProperty"]], result)

        @builtins.property
        def crawl_depth(self) -> typing.Optional[jsii.Number]:
            '''Specifies the number of levels in a website that you want to crawl.

            The first level begins from the website seed or starting point URL. For example, if a website has 3 levels – index level (i.e. seed in this example), sections level, and subsections level – and you are only interested in crawling information up to the sections level (i.e. levels 0-1), you can set your depth to 1.

            The default crawl depth is set to 2.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerconfiguration.html#cfn-kendra-datasource-webcrawlerconfiguration-crawldepth
            '''
            result = self._values.get("crawl_depth")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_content_size_per_page_in_mega_bytes(
            self,
        ) -> typing.Optional[jsii.Number]:
            '''The maximum size (in MB) of a webpage or attachment to crawl.

            Files larger than this size (in MB) are skipped/not crawled.

            The default maximum size of a webpage or attachment is set to 50 MB.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerconfiguration.html#cfn-kendra-datasource-webcrawlerconfiguration-maxcontentsizeperpageinmegabytes
            '''
            result = self._values.get("max_content_size_per_page_in_mega_bytes")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_links_per_page(self) -> typing.Optional[jsii.Number]:
            '''The maximum number of URLs on a webpage to include when crawling a website. This number is per webpage.

            As a website’s webpages are crawled, any URLs the webpages link to are also crawled. URLs on a webpage are crawled in order of appearance.

            The default maximum links per page is 100.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerconfiguration.html#cfn-kendra-datasource-webcrawlerconfiguration-maxlinksperpage
            '''
            result = self._values.get("max_links_per_page")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_urls_per_minute_crawl_rate(self) -> typing.Optional[jsii.Number]:
            '''The maximum number of URLs crawled per website host per minute.

            A minimum of one URL is required.

            The default maximum number of URLs crawled per website host per minute is 300.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerconfiguration.html#cfn-kendra-datasource-webcrawlerconfiguration-maxurlsperminutecrawlrate
            '''
            result = self._values.get("max_urls_per_minute_crawl_rate")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def proxy_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.ProxyConfigurationProperty"]]:
            '''Configuration information required to connect to your internal websites via a web proxy.

            You must provide the website host name and port number. For example, the host name of https://a.example.com/page1.html is "a.example.com" and the port is 443, the standard port for HTTPS.

            Web proxy credentials are optional and you can use them to connect to a web proxy server that requires basic authentication. To store web proxy credentials, you use a secret in `AWS Secrets Manager <https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerconfiguration.html#cfn-kendra-datasource-webcrawlerconfiguration-proxyconfiguration
            '''
            result = self._values.get("proxy_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.ProxyConfigurationProperty"]], result)

        @builtins.property
        def url_exclusion_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of regular expression patterns to exclude certain URLs to crawl.

            URLs that match the patterns are excluded from the index. URLs that don't match the patterns are included in the index. If a URL matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the URL file isn't included in the index.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerconfiguration.html#cfn-kendra-datasource-webcrawlerconfiguration-urlexclusionpatterns
            '''
            result = self._values.get("url_exclusion_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def url_inclusion_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of regular expression patterns to include certain URLs to crawl.

            URLs that match the patterns are included in the index. URLs that don't match the patterns are excluded from the index. If a URL matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the URL file isn't included in the index.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerconfiguration.html#cfn-kendra-datasource-webcrawlerconfiguration-urlinclusionpatterns
            '''
            result = self._values.get("url_inclusion_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WebCrawlerConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.WebCrawlerSeedUrlConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"seed_urls": "seedUrls", "web_crawler_mode": "webCrawlerMode"},
    )
    class WebCrawlerSeedUrlConfigurationProperty:
        def __init__(
            self,
            *,
            seed_urls: typing.Sequence[builtins.str],
            web_crawler_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides the configuration information of the seed or starting point URLs to crawl.

            *When selecting websites to index, you must adhere to the `Amazon Acceptable Use Policy <https://docs.aws.amazon.com/aup/>`_ and all other Amazon terms. Remember that you must only use the Amazon Kendra web crawler to index your own webpages, or webpages that you have authorization to index.*

            :param seed_urls: The list of seed or starting point URLs of the websites you want to crawl. The list can include a maximum of 100 seed URLs.
            :param web_crawler_mode: You can choose one of the following modes:. - ``HOST_ONLY`` – crawl only the website host names. For example, if the seed URL is "abc.example.com", then only URLs with host name "abc.example.com" are crawled. - ``SUBDOMAINS`` – crawl the website host names with subdomains. For example, if the seed URL is "abc.example.com", then "a.abc.example.com" and "b.abc.example.com" are also crawled. - ``EVERYTHING`` – crawl the website host names with subdomains and other domains that the webpages link to. The default mode is set to ``HOST_ONLY`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerseedurlconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                web_crawler_seed_url_configuration_property = kendra.CfnDataSource.WebCrawlerSeedUrlConfigurationProperty(
                    seed_urls=["seedUrls"],
                
                    # the properties below are optional
                    web_crawler_mode="webCrawlerMode"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e3ec3ac8587d1bf68152a59168462774272ae571eeb6061c1178c797875c9144)
                check_type(argname="argument seed_urls", value=seed_urls, expected_type=type_hints["seed_urls"])
                check_type(argname="argument web_crawler_mode", value=web_crawler_mode, expected_type=type_hints["web_crawler_mode"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "seed_urls": seed_urls,
            }
            if web_crawler_mode is not None:
                self._values["web_crawler_mode"] = web_crawler_mode

        @builtins.property
        def seed_urls(self) -> typing.List[builtins.str]:
            '''The list of seed or starting point URLs of the websites you want to crawl.

            The list can include a maximum of 100 seed URLs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerseedurlconfiguration.html#cfn-kendra-datasource-webcrawlerseedurlconfiguration-seedurls
            '''
            result = self._values.get("seed_urls")
            assert result is not None, "Required property 'seed_urls' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def web_crawler_mode(self) -> typing.Optional[builtins.str]:
            '''You can choose one of the following modes:.

            - ``HOST_ONLY`` – crawl only the website host names. For example, if the seed URL is "abc.example.com", then only URLs with host name "abc.example.com" are crawled.
            - ``SUBDOMAINS`` – crawl the website host names with subdomains. For example, if the seed URL is "abc.example.com", then "a.abc.example.com" and "b.abc.example.com" are also crawled.
            - ``EVERYTHING`` – crawl the website host names with subdomains and other domains that the webpages link to.

            The default mode is set to ``HOST_ONLY`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerseedurlconfiguration.html#cfn-kendra-datasource-webcrawlerseedurlconfiguration-webcrawlermode
            '''
            result = self._values.get("web_crawler_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WebCrawlerSeedUrlConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.WebCrawlerSiteMapsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"site_maps": "siteMaps"},
    )
    class WebCrawlerSiteMapsConfigurationProperty:
        def __init__(self, *, site_maps: typing.Sequence[builtins.str]) -> None:
            '''Provides the configuration information of the sitemap URLs to crawl.

            *When selecting websites to index, you must adhere to the `Amazon Acceptable Use Policy <https://docs.aws.amazon.com/aup/>`_ and all other Amazon terms. Remember that you must only use the Amazon Kendra web crawler to index your own webpages, or webpages that you have authorization to index.*

            :param site_maps: The list of sitemap URLs of the websites you want to crawl. The list can include a maximum of three sitemap URLs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlersitemapsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                web_crawler_site_maps_configuration_property = kendra.CfnDataSource.WebCrawlerSiteMapsConfigurationProperty(
                    site_maps=["siteMaps"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__11a3e0a7b08717554425279e6a9adfda167dbef15c3515f094a9b133ee8cc9cc)
                check_type(argname="argument site_maps", value=site_maps, expected_type=type_hints["site_maps"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "site_maps": site_maps,
            }

        @builtins.property
        def site_maps(self) -> typing.List[builtins.str]:
            '''The list of sitemap URLs of the websites you want to crawl.

            The list can include a maximum of three sitemap URLs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlersitemapsconfiguration.html#cfn-kendra-datasource-webcrawlersitemapsconfiguration-sitemaps
            '''
            result = self._values.get("site_maps")
            assert result is not None, "Required property 'site_maps' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WebCrawlerSiteMapsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.WebCrawlerUrlsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "seed_url_configuration": "seedUrlConfiguration",
            "site_maps_configuration": "siteMapsConfiguration",
        },
    )
    class WebCrawlerUrlsProperty:
        def __init__(
            self,
            *,
            seed_url_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.WebCrawlerSeedUrlConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            site_maps_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.WebCrawlerSiteMapsConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies the seed or starting point URLs of the websites or the sitemap URLs of the websites you want to crawl.

            You can include website subdomains. You can list up to 100 seed URLs and up to three sitemap URLs.

            You can only crawl websites that use the secure communication protocol, Hypertext Transfer Protocol Secure (HTTPS). If you receive an error when crawling a website, it could be that the website is blocked from crawling.

            *When selecting websites to index, you must adhere to the `Amazon Acceptable Use Policy <https://docs.aws.amazon.com/aup/>`_ and all other Amazon terms. Remember that you must only use the Amazon Kendra web crawler to index your own webpages, or webpages that you have authorization to index.*

            :param seed_url_configuration: Configuration of the seed or starting point URLs of the websites you want to crawl. You can choose to crawl only the website host names, or the website host names with subdomains, or the website host names with subdomains and other domains that the webpages link to. You can list up to 100 seed URLs.
            :param site_maps_configuration: Configuration of the sitemap URLs of the websites you want to crawl. Only URLs belonging to the same website host names are crawled. You can list up to three sitemap URLs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerurls.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                web_crawler_urls_property = kendra.CfnDataSource.WebCrawlerUrlsProperty(
                    seed_url_configuration=kendra.CfnDataSource.WebCrawlerSeedUrlConfigurationProperty(
                        seed_urls=["seedUrls"],
                
                        # the properties below are optional
                        web_crawler_mode="webCrawlerMode"
                    ),
                    site_maps_configuration=kendra.CfnDataSource.WebCrawlerSiteMapsConfigurationProperty(
                        site_maps=["siteMaps"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__351a084f3e7d67658f1cf5efcab3016279b2b065c00b8ab5374f3f25925c7166)
                check_type(argname="argument seed_url_configuration", value=seed_url_configuration, expected_type=type_hints["seed_url_configuration"])
                check_type(argname="argument site_maps_configuration", value=site_maps_configuration, expected_type=type_hints["site_maps_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if seed_url_configuration is not None:
                self._values["seed_url_configuration"] = seed_url_configuration
            if site_maps_configuration is not None:
                self._values["site_maps_configuration"] = site_maps_configuration

        @builtins.property
        def seed_url_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.WebCrawlerSeedUrlConfigurationProperty"]]:
            '''Configuration of the seed or starting point URLs of the websites you want to crawl.

            You can choose to crawl only the website host names, or the website host names with subdomains, or the website host names with subdomains and other domains that the webpages link to.

            You can list up to 100 seed URLs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerurls.html#cfn-kendra-datasource-webcrawlerurls-seedurlconfiguration
            '''
            result = self._values.get("seed_url_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.WebCrawlerSeedUrlConfigurationProperty"]], result)

        @builtins.property
        def site_maps_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.WebCrawlerSiteMapsConfigurationProperty"]]:
            '''Configuration of the sitemap URLs of the websites you want to crawl.

            Only URLs belonging to the same website host names are crawled. You can list up to three sitemap URLs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-webcrawlerurls.html#cfn-kendra-datasource-webcrawlerurls-sitemapsconfiguration
            '''
            result = self._values.get("site_maps_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.WebCrawlerSiteMapsConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WebCrawlerUrlsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnDataSource.WorkDocsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "organization_id": "organizationId",
            "crawl_comments": "crawlComments",
            "exclusion_patterns": "exclusionPatterns",
            "field_mappings": "fieldMappings",
            "inclusion_patterns": "inclusionPatterns",
            "use_change_log": "useChangeLog",
        },
    )
    class WorkDocsConfigurationProperty:
        def __init__(
            self,
            *,
            organization_id: builtins.str,
            crawl_comments: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            exclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
            field_mappings: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnDataSource.DataSourceToIndexFieldMappingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            inclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
            use_change_log: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
        ) -> None:
            '''Provides the configuration information to connect to Amazon WorkDocs as your data source.

            Amazon WorkDocs connector is available in Oregon, North Virginia, Sydney, Singapore and Ireland regions.

            :param organization_id: The identifier of the directory corresponding to your Amazon WorkDocs site repository. You can find the organization ID in the `AWS Directory Service <https://docs.aws.amazon.com/directoryservicev2/>`_ by going to *Active Directory* , then *Directories* . Your Amazon WorkDocs site directory has an ID, which is the organization ID. You can also set up a new Amazon WorkDocs directory in the AWS Directory Service console and enable a Amazon WorkDocs site for the directory in the Amazon WorkDocs console.
            :param crawl_comments: ``TRUE`` to include comments on documents in your index. Including comments in your index means each comment is a document that can be searched on. The default is set to ``FALSE`` .
            :param exclusion_patterns: A list of regular expression patterns to exclude certain files in your Amazon WorkDocs site repository. Files that match the patterns are excluded from the index. Files that don’t match the patterns are included in the index. If a file matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the file isn't included in the index.
            :param field_mappings: A list of ``DataSourceToIndexFieldMapping`` objects that map Amazon WorkDocs data source attributes or field names to Amazon Kendra index field names. To create custom fields, use the ``UpdateIndex`` API before you map to Amazon WorkDocs fields. For more information, see `Mapping data source fields <https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html>`_ . The Amazon WorkDocs data source field names must exist in your Amazon WorkDocs custom metadata.
            :param inclusion_patterns: A list of regular expression patterns to include certain files in your Amazon WorkDocs site repository. Files that match the patterns are included in the index. Files that don't match the patterns are excluded from the index. If a file matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the file isn't included in the index.
            :param use_change_log: ``TRUE`` to use the Amazon WorkDocs change log to determine which documents require updating in the index. Depending on the change log's size, it may take longer for Amazon Kendra to use the change log than to scan all of your documents in Amazon WorkDocs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-workdocsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                work_docs_configuration_property = kendra.CfnDataSource.WorkDocsConfigurationProperty(
                    organization_id="organizationId",
                
                    # the properties below are optional
                    crawl_comments=False,
                    exclusion_patterns=["exclusionPatterns"],
                    field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                        data_source_field_name="dataSourceFieldName",
                        index_field_name="indexFieldName",
                
                        # the properties below are optional
                        date_field_format="dateFieldFormat"
                    )],
                    inclusion_patterns=["inclusionPatterns"],
                    use_change_log=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a5bb8e5b0cdb6d927137ed524008b228e11190475c7c75a26dbe62a80a633d13)
                check_type(argname="argument organization_id", value=organization_id, expected_type=type_hints["organization_id"])
                check_type(argname="argument crawl_comments", value=crawl_comments, expected_type=type_hints["crawl_comments"])
                check_type(argname="argument exclusion_patterns", value=exclusion_patterns, expected_type=type_hints["exclusion_patterns"])
                check_type(argname="argument field_mappings", value=field_mappings, expected_type=type_hints["field_mappings"])
                check_type(argname="argument inclusion_patterns", value=inclusion_patterns, expected_type=type_hints["inclusion_patterns"])
                check_type(argname="argument use_change_log", value=use_change_log, expected_type=type_hints["use_change_log"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "organization_id": organization_id,
            }
            if crawl_comments is not None:
                self._values["crawl_comments"] = crawl_comments
            if exclusion_patterns is not None:
                self._values["exclusion_patterns"] = exclusion_patterns
            if field_mappings is not None:
                self._values["field_mappings"] = field_mappings
            if inclusion_patterns is not None:
                self._values["inclusion_patterns"] = inclusion_patterns
            if use_change_log is not None:
                self._values["use_change_log"] = use_change_log

        @builtins.property
        def organization_id(self) -> builtins.str:
            '''The identifier of the directory corresponding to your Amazon WorkDocs site repository.

            You can find the organization ID in the `AWS Directory Service <https://docs.aws.amazon.com/directoryservicev2/>`_ by going to *Active Directory* , then *Directories* . Your Amazon WorkDocs site directory has an ID, which is the organization ID. You can also set up a new Amazon WorkDocs directory in the AWS Directory Service console and enable a Amazon WorkDocs site for the directory in the Amazon WorkDocs console.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-workdocsconfiguration.html#cfn-kendra-datasource-workdocsconfiguration-organizationid
            '''
            result = self._values.get("organization_id")
            assert result is not None, "Required property 'organization_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def crawl_comments(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''``TRUE`` to include comments on documents in your index.

            Including comments in your index means each comment is a document that can be searched on.

            The default is set to ``FALSE`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-workdocsconfiguration.html#cfn-kendra-datasource-workdocsconfiguration-crawlcomments
            '''
            result = self._values.get("crawl_comments")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def exclusion_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of regular expression patterns to exclude certain files in your Amazon WorkDocs site repository.

            Files that match the patterns are excluded from the index. Files that don’t match the patterns are included in the index. If a file matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the file isn't included in the index.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-workdocsconfiguration.html#cfn-kendra-datasource-workdocsconfiguration-exclusionpatterns
            '''
            result = self._values.get("exclusion_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def field_mappings(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DataSourceToIndexFieldMappingProperty"]]]]:
            '''A list of ``DataSourceToIndexFieldMapping`` objects that map Amazon WorkDocs data source attributes or field names to Amazon Kendra index field names.

            To create custom fields, use the ``UpdateIndex`` API before you map to Amazon WorkDocs fields. For more information, see `Mapping data source fields <https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html>`_ . The Amazon WorkDocs data source field names must exist in your Amazon WorkDocs custom metadata.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-workdocsconfiguration.html#cfn-kendra-datasource-workdocsconfiguration-fieldmappings
            '''
            result = self._values.get("field_mappings")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnDataSource.DataSourceToIndexFieldMappingProperty"]]]], result)

        @builtins.property
        def inclusion_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of regular expression patterns to include certain files in your Amazon WorkDocs site repository.

            Files that match the patterns are included in the index. Files that don't match the patterns are excluded from the index. If a file matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the file isn't included in the index.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-workdocsconfiguration.html#cfn-kendra-datasource-workdocsconfiguration-inclusionpatterns
            '''
            result = self._values.get("inclusion_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def use_change_log(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''``TRUE`` to use the Amazon WorkDocs change log to determine which documents require updating in the index.

            Depending on the change log's size, it may take longer for Amazon Kendra to use the change log than to scan all of your documents in Amazon WorkDocs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-datasource-workdocsconfiguration.html#cfn-kendra-datasource-workdocsconfiguration-usechangelog
            '''
            result = self._values.get("use_change_log")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkDocsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-kendra.CfnDataSourceProps",
    jsii_struct_bases=[],
    name_mapping={
        "index_id": "indexId",
        "name": "name",
        "type": "type",
        "custom_document_enrichment_configuration": "customDocumentEnrichmentConfiguration",
        "data_source_configuration": "dataSourceConfiguration",
        "description": "description",
        "role_arn": "roleArn",
        "schedule": "schedule",
        "tags": "tags",
    },
)
class CfnDataSourceProps:
    def __init__(
        self,
        *,
        index_id: builtins.str,
        name: builtins.str,
        type: builtins.str,
        custom_document_enrichment_configuration: typing.Optional[typing.Union[typing.Union[CfnDataSource.CustomDocumentEnrichmentConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable]] = None,
        data_source_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.DataSourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
        schedule: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDataSource``.

        :param index_id: The identifier of the index you want to use with the data source connector.
        :param name: The name of the data source.
        :param type: The type of the data source.
        :param custom_document_enrichment_configuration: Configuration information for altering document metadata and content during the document ingestion process.
        :param data_source_configuration: Configuration information for an Amazon Kendra data source. The contents of the configuration depend on the type of data source. You can only specify one type of data source in the configuration. You can't specify the ``Configuration`` parameter when the ``Type`` parameter is set to ``CUSTOM`` . The ``Configuration`` parameter is required for all other data sources.
        :param description: A description for the data source connector.
        :param role_arn: The Amazon Resource Name (ARN) of a role with permission to access the data source. You can't specify the ``RoleArn`` parameter when the ``Type`` parameter is set to ``CUSTOM`` . The ``RoleArn`` parameter is required for all other data sources.
        :param schedule: Sets the frequency that Amazon Kendra checks the documents in your data source and updates the index. If you don't set a schedule, Amazon Kendra doesn't periodically update the index.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_kendra as kendra
            
            cfn_data_source_props = kendra.CfnDataSourceProps(
                index_id="indexId",
                name="name",
                type="type",
            
                # the properties below are optional
                custom_document_enrichment_configuration=kendra.CfnDataSource.CustomDocumentEnrichmentConfigurationProperty(
                    inline_configurations=[kendra.CfnDataSource.InlineCustomDocumentEnrichmentConfigurationProperty(
                        condition=kendra.CfnDataSource.DocumentAttributeConditionProperty(
                            condition_document_attribute_key="conditionDocumentAttributeKey",
                            operator="operator",
            
                            # the properties below are optional
                            condition_on_value=kendra.CfnDataSource.DocumentAttributeValueProperty(
                                date_value="dateValue",
                                long_value=123,
                                string_list_value=["stringListValue"],
                                string_value="stringValue"
                            )
                        ),
                        document_content_deletion=False,
                        target=kendra.CfnDataSource.DocumentAttributeTargetProperty(
                            target_document_attribute_key="targetDocumentAttributeKey",
            
                            # the properties below are optional
                            target_document_attribute_value=kendra.CfnDataSource.DocumentAttributeValueProperty(
                                date_value="dateValue",
                                long_value=123,
                                string_list_value=["stringListValue"],
                                string_value="stringValue"
                            ),
                            target_document_attribute_value_deletion=False
                        )
                    )],
                    post_extraction_hook_configuration=kendra.CfnDataSource.HookConfigurationProperty(
                        lambda_arn="lambdaArn",
                        s3_bucket="s3Bucket",
            
                        # the properties below are optional
                        invocation_condition=kendra.CfnDataSource.DocumentAttributeConditionProperty(
                            condition_document_attribute_key="conditionDocumentAttributeKey",
                            operator="operator",
            
                            # the properties below are optional
                            condition_on_value=kendra.CfnDataSource.DocumentAttributeValueProperty(
                                date_value="dateValue",
                                long_value=123,
                                string_list_value=["stringListValue"],
                                string_value="stringValue"
                            )
                        )
                    ),
                    pre_extraction_hook_configuration=kendra.CfnDataSource.HookConfigurationProperty(
                        lambda_arn="lambdaArn",
                        s3_bucket="s3Bucket",
            
                        # the properties below are optional
                        invocation_condition=kendra.CfnDataSource.DocumentAttributeConditionProperty(
                            condition_document_attribute_key="conditionDocumentAttributeKey",
                            operator="operator",
            
                            # the properties below are optional
                            condition_on_value=kendra.CfnDataSource.DocumentAttributeValueProperty(
                                date_value="dateValue",
                                long_value=123,
                                string_list_value=["stringListValue"],
                                string_value="stringValue"
                            )
                        )
                    ),
                    role_arn="roleArn"
                ),
                data_source_configuration=kendra.CfnDataSource.DataSourceConfigurationProperty(
                    confluence_configuration=kendra.CfnDataSource.ConfluenceConfigurationProperty(
                        secret_arn="secretArn",
                        server_url="serverUrl",
                        version="version",
            
                        # the properties below are optional
                        attachment_configuration=kendra.CfnDataSource.ConfluenceAttachmentConfigurationProperty(
                            attachment_field_mappings=[kendra.CfnDataSource.ConfluenceAttachmentToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
            
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )],
                            crawl_attachments=False
                        ),
                        blog_configuration=kendra.CfnDataSource.ConfluenceBlogConfigurationProperty(
                            blog_field_mappings=[kendra.CfnDataSource.ConfluenceBlogToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
            
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )]
                        ),
                        exclusion_patterns=["exclusionPatterns"],
                        inclusion_patterns=["inclusionPatterns"],
                        page_configuration=kendra.CfnDataSource.ConfluencePageConfigurationProperty(
                            page_field_mappings=[kendra.CfnDataSource.ConfluencePageToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
            
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )]
                        ),
                        space_configuration=kendra.CfnDataSource.ConfluenceSpaceConfigurationProperty(
                            crawl_archived_spaces=False,
                            crawl_personal_spaces=False,
                            exclude_spaces=["excludeSpaces"],
                            include_spaces=["includeSpaces"],
                            space_field_mappings=[kendra.CfnDataSource.ConfluenceSpaceToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
            
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )]
                        ),
                        vpc_configuration=kendra.CfnDataSource.DataSourceVpcConfigurationProperty(
                            security_group_ids=["securityGroupIds"],
                            subnet_ids=["subnetIds"]
                        )
                    ),
                    database_configuration=kendra.CfnDataSource.DatabaseConfigurationProperty(
                        column_configuration=kendra.CfnDataSource.ColumnConfigurationProperty(
                            change_detecting_columns=["changeDetectingColumns"],
                            document_data_column_name="documentDataColumnName",
                            document_id_column_name="documentIdColumnName",
            
                            # the properties below are optional
                            document_title_column_name="documentTitleColumnName",
                            field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
            
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )]
                        ),
                        connection_configuration=kendra.CfnDataSource.ConnectionConfigurationProperty(
                            database_host="databaseHost",
                            database_name="databaseName",
                            database_port=123,
                            secret_arn="secretArn",
                            table_name="tableName"
                        ),
                        database_engine_type="databaseEngineType",
            
                        # the properties below are optional
                        acl_configuration=kendra.CfnDataSource.AclConfigurationProperty(
                            allowed_groups_column_name="allowedGroupsColumnName"
                        ),
                        sql_configuration=kendra.CfnDataSource.SqlConfigurationProperty(
                            query_identifiers_enclosing_option="queryIdentifiersEnclosingOption"
                        ),
                        vpc_configuration=kendra.CfnDataSource.DataSourceVpcConfigurationProperty(
                            security_group_ids=["securityGroupIds"],
                            subnet_ids=["subnetIds"]
                        )
                    ),
                    google_drive_configuration=kendra.CfnDataSource.GoogleDriveConfigurationProperty(
                        secret_arn="secretArn",
            
                        # the properties below are optional
                        exclude_mime_types=["excludeMimeTypes"],
                        exclude_shared_drives=["excludeSharedDrives"],
                        exclude_user_accounts=["excludeUserAccounts"],
                        exclusion_patterns=["exclusionPatterns"],
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
            
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )],
                        inclusion_patterns=["inclusionPatterns"]
                    ),
                    one_drive_configuration=kendra.CfnDataSource.OneDriveConfigurationProperty(
                        one_drive_users=kendra.CfnDataSource.OneDriveUsersProperty(
                            one_drive_user_list=["oneDriveUserList"],
                            one_drive_user_s3_path=kendra.CfnDataSource.S3PathProperty(
                                bucket="bucket",
                                key="key"
                            )
                        ),
                        secret_arn="secretArn",
                        tenant_domain="tenantDomain",
            
                        # the properties below are optional
                        disable_local_groups=False,
                        exclusion_patterns=["exclusionPatterns"],
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
            
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )],
                        inclusion_patterns=["inclusionPatterns"]
                    ),
                    s3_configuration=kendra.CfnDataSource.S3DataSourceConfigurationProperty(
                        bucket_name="bucketName",
            
                        # the properties below are optional
                        access_control_list_configuration=kendra.CfnDataSource.AccessControlListConfigurationProperty(
                            key_path="keyPath"
                        ),
                        documents_metadata_configuration=kendra.CfnDataSource.DocumentsMetadataConfigurationProperty(
                            s3_prefix="s3Prefix"
                        ),
                        exclusion_patterns=["exclusionPatterns"],
                        inclusion_patterns=["inclusionPatterns"],
                        inclusion_prefixes=["inclusionPrefixes"]
                    ),
                    salesforce_configuration=kendra.CfnDataSource.SalesforceConfigurationProperty(
                        secret_arn="secretArn",
                        server_url="serverUrl",
            
                        # the properties below are optional
                        chatter_feed_configuration=kendra.CfnDataSource.SalesforceChatterFeedConfigurationProperty(
                            document_data_field_name="documentDataFieldName",
            
                            # the properties below are optional
                            document_title_field_name="documentTitleFieldName",
                            field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
            
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )],
                            include_filter_types=["includeFilterTypes"]
                        ),
                        crawl_attachments=False,
                        exclude_attachment_file_patterns=["excludeAttachmentFilePatterns"],
                        include_attachment_file_patterns=["includeAttachmentFilePatterns"],
                        knowledge_article_configuration=kendra.CfnDataSource.SalesforceKnowledgeArticleConfigurationProperty(
                            included_states=["includedStates"],
            
                            # the properties below are optional
                            custom_knowledge_article_type_configurations=[kendra.CfnDataSource.SalesforceCustomKnowledgeArticleTypeConfigurationProperty(
                                document_data_field_name="documentDataFieldName",
                                name="name",
            
                                # the properties below are optional
                                document_title_field_name="documentTitleFieldName",
                                field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                                    data_source_field_name="dataSourceFieldName",
                                    index_field_name="indexFieldName",
            
                                    # the properties below are optional
                                    date_field_format="dateFieldFormat"
                                )]
                            )],
                            standard_knowledge_article_type_configuration=kendra.CfnDataSource.SalesforceStandardKnowledgeArticleTypeConfigurationProperty(
                                document_data_field_name="documentDataFieldName",
            
                                # the properties below are optional
                                document_title_field_name="documentTitleFieldName",
                                field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                                    data_source_field_name="dataSourceFieldName",
                                    index_field_name="indexFieldName",
            
                                    # the properties below are optional
                                    date_field_format="dateFieldFormat"
                                )]
                            )
                        ),
                        standard_object_attachment_configuration=kendra.CfnDataSource.SalesforceStandardObjectAttachmentConfigurationProperty(
                            document_title_field_name="documentTitleFieldName",
                            field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
            
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )]
                        ),
                        standard_object_configurations=[kendra.CfnDataSource.SalesforceStandardObjectConfigurationProperty(
                            document_data_field_name="documentDataFieldName",
                            name="name",
            
                            # the properties below are optional
                            document_title_field_name="documentTitleFieldName",
                            field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
            
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )]
                        )]
                    ),
                    service_now_configuration=kendra.CfnDataSource.ServiceNowConfigurationProperty(
                        host_url="hostUrl",
                        secret_arn="secretArn",
                        service_now_build_version="serviceNowBuildVersion",
            
                        # the properties below are optional
                        authentication_type="authenticationType",
                        knowledge_article_configuration=kendra.CfnDataSource.ServiceNowKnowledgeArticleConfigurationProperty(
                            document_data_field_name="documentDataFieldName",
            
                            # the properties below are optional
                            crawl_attachments=False,
                            document_title_field_name="documentTitleFieldName",
                            exclude_attachment_file_patterns=["excludeAttachmentFilePatterns"],
                            field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
            
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )],
                            filter_query="filterQuery",
                            include_attachment_file_patterns=["includeAttachmentFilePatterns"]
                        ),
                        service_catalog_configuration=kendra.CfnDataSource.ServiceNowServiceCatalogConfigurationProperty(
                            document_data_field_name="documentDataFieldName",
            
                            # the properties below are optional
                            crawl_attachments=False,
                            document_title_field_name="documentTitleFieldName",
                            exclude_attachment_file_patterns=["excludeAttachmentFilePatterns"],
                            field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                                data_source_field_name="dataSourceFieldName",
                                index_field_name="indexFieldName",
            
                                # the properties below are optional
                                date_field_format="dateFieldFormat"
                            )],
                            include_attachment_file_patterns=["includeAttachmentFilePatterns"]
                        )
                    ),
                    share_point_configuration=kendra.CfnDataSource.SharePointConfigurationProperty(
                        secret_arn="secretArn",
                        share_point_version="sharePointVersion",
                        urls=["urls"],
            
                        # the properties below are optional
                        crawl_attachments=False,
                        disable_local_groups=False,
                        document_title_field_name="documentTitleFieldName",
                        exclusion_patterns=["exclusionPatterns"],
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
            
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )],
                        inclusion_patterns=["inclusionPatterns"],
                        ssl_certificate_s3_path=kendra.CfnDataSource.S3PathProperty(
                            bucket="bucket",
                            key="key"
                        ),
                        use_change_log=False,
                        vpc_configuration=kendra.CfnDataSource.DataSourceVpcConfigurationProperty(
                            security_group_ids=["securityGroupIds"],
                            subnet_ids=["subnetIds"]
                        )
                    ),
                    web_crawler_configuration=kendra.CfnDataSource.WebCrawlerConfigurationProperty(
                        urls=kendra.CfnDataSource.WebCrawlerUrlsProperty(
                            seed_url_configuration=kendra.CfnDataSource.WebCrawlerSeedUrlConfigurationProperty(
                                seed_urls=["seedUrls"],
            
                                # the properties below are optional
                                web_crawler_mode="webCrawlerMode"
                            ),
                            site_maps_configuration=kendra.CfnDataSource.WebCrawlerSiteMapsConfigurationProperty(
                                site_maps=["siteMaps"]
                            )
                        ),
            
                        # the properties below are optional
                        authentication_configuration=kendra.CfnDataSource.WebCrawlerAuthenticationConfigurationProperty(
                            basic_authentication=[kendra.CfnDataSource.WebCrawlerBasicAuthenticationProperty(
                                credentials="credentials",
                                host="host",
                                port=123
                            )]
                        ),
                        crawl_depth=123,
                        max_content_size_per_page_in_mega_bytes=123,
                        max_links_per_page=123,
                        max_urls_per_minute_crawl_rate=123,
                        proxy_configuration=kendra.CfnDataSource.ProxyConfigurationProperty(
                            host="host",
                            port=123,
            
                            # the properties below are optional
                            credentials="credentials"
                        ),
                        url_exclusion_patterns=["urlExclusionPatterns"],
                        url_inclusion_patterns=["urlInclusionPatterns"]
                    ),
                    work_docs_configuration=kendra.CfnDataSource.WorkDocsConfigurationProperty(
                        organization_id="organizationId",
            
                        # the properties below are optional
                        crawl_comments=False,
                        exclusion_patterns=["exclusionPatterns"],
                        field_mappings=[kendra.CfnDataSource.DataSourceToIndexFieldMappingProperty(
                            data_source_field_name="dataSourceFieldName",
                            index_field_name="indexFieldName",
            
                            # the properties below are optional
                            date_field_format="dateFieldFormat"
                        )],
                        inclusion_patterns=["inclusionPatterns"],
                        use_change_log=False
                    )
                ),
                description="description",
                role_arn="roleArn",
                schedule="schedule",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1977d3785581586034c986c94543d103c44b06111b0826035b84d143f438cdd6)
            check_type(argname="argument index_id", value=index_id, expected_type=type_hints["index_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument custom_document_enrichment_configuration", value=custom_document_enrichment_configuration, expected_type=type_hints["custom_document_enrichment_configuration"])
            check_type(argname="argument data_source_configuration", value=data_source_configuration, expected_type=type_hints["data_source_configuration"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "index_id": index_id,
            "name": name,
            "type": type,
        }
        if custom_document_enrichment_configuration is not None:
            self._values["custom_document_enrichment_configuration"] = custom_document_enrichment_configuration
        if data_source_configuration is not None:
            self._values["data_source_configuration"] = data_source_configuration
        if description is not None:
            self._values["description"] = description
        if role_arn is not None:
            self._values["role_arn"] = role_arn
        if schedule is not None:
            self._values["schedule"] = schedule
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def index_id(self) -> builtins.str:
        '''The identifier of the index you want to use with the data source connector.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-indexid
        '''
        result = self._values.get("index_id")
        assert result is not None, "Required property 'index_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the data source.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of the data source.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_document_enrichment_configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnDataSource.CustomDocumentEnrichmentConfigurationProperty, _aws_cdk_core_f4b25747.IResolvable]]:
        '''Configuration information for altering document metadata and content during the document ingestion process.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-customdocumentenrichmentconfiguration
        '''
        result = self._values.get("custom_document_enrichment_configuration")
        return typing.cast(typing.Optional[typing.Union[CfnDataSource.CustomDocumentEnrichmentConfigurationProperty, _aws_cdk_core_f4b25747.IResolvable]], result)

    @builtins.property
    def data_source_configuration(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnDataSource.DataSourceConfigurationProperty]]:
        '''Configuration information for an Amazon Kendra data source.

        The contents of the configuration depend on the type of data source. You can only specify one type of data source in the configuration.

        You can't specify the ``Configuration`` parameter when the ``Type`` parameter is set to ``CUSTOM`` .

        The ``Configuration`` parameter is required for all other data sources.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-datasourceconfiguration
        '''
        result = self._values.get("data_source_configuration")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnDataSource.DataSourceConfigurationProperty]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the data source connector.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of a role with permission to access the data source.

        You can't specify the ``RoleArn`` parameter when the ``Type`` parameter is set to ``CUSTOM`` .

        The ``RoleArn`` parameter is required for all other data sources.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-rolearn
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schedule(self) -> typing.Optional[builtins.str]:
        '''Sets the frequency that Amazon Kendra checks the documents in your data source and updates the index.

        If you don't set a schedule, Amazon Kendra doesn't periodically update the index.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-schedule
        '''
        result = self._values.get("schedule")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-datasource.html#cfn-kendra-datasource-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnFaq(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-kendra.CfnFaq",
):
    '''A CloudFormation ``AWS::Kendra::Faq``.

    Creates an new set of frequently asked question (FAQ) questions and answers.

    :cloudformationResource: AWS::Kendra::Faq
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_kendra as kendra
        
        cfn_faq = kendra.CfnFaq(self, "MyCfnFaq",
            index_id="indexId",
            name="name",
            role_arn="roleArn",
            s3_path=kendra.CfnFaq.S3PathProperty(
                bucket="bucket",
                key="key"
            ),
        
            # the properties below are optional
            description="description",
            file_format="fileFormat",
            tags=[CfnTag(
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
        index_id: builtins.str,
        name: builtins.str,
        role_arn: builtins.str,
        s3_path: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnFaq.S3PathProperty", typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        file_format: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Kendra::Faq``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param index_id: The identifier of the index that contains the FAQ.
        :param name: The name that you assigned the FAQ when you created or updated the FAQ.
        :param role_arn: The Amazon Resource Name (ARN) of a role with permission to access the S3 bucket that contains the FAQ.
        :param s3_path: The Amazon Simple Storage Service (Amazon S3) location of the FAQ input data.
        :param description: A description for the FAQ.
        :param file_format: The format of the input file. You can choose between a basic CSV format, a CSV format that includes customs attributes in a header, and a JSON format that includes custom attributes. The format must match the format of the file stored in the S3 bucket identified in the S3Path parameter. Valid values are: - ``CSV`` - ``CSV_WITH_HEADER`` - ``JSON``
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab89b7a98ca53da545dcff17304c9c343f2b8a8199c1072a3399c000ce313227)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFaqProps(
            index_id=index_id,
            name=name,
            role_arn=role_arn,
            s3_path=s3_path,
            description=description,
            file_format=file_format,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e01629f08de46ef91bc4678b76ac86f611d13ddefbec5ac511265a13e2c8dc1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__67dcbe13e8527b98fdeff47eb96567738d5ef6db39feaded973a554b6710aaba)
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
        '''``arn:aws:kendra:us-west-2:111122223333:index/335c3741-41df-46a6-b5d3-61f85b787884/faq/f61995a6-cd5c-4e99-9cfc-58816d8bfaa7``.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The identifier for the FAQ. For example:.

        ``f61995a6-cd5c-4e99-9cfc-58816d8bfaa7``

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _aws_cdk_core_f4b25747.TagManager:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-tags
        '''
        return typing.cast(_aws_cdk_core_f4b25747.TagManager, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="indexId")
    def index_id(self) -> builtins.str:
        '''The identifier of the index that contains the FAQ.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-indexid
        '''
        return typing.cast(builtins.str, jsii.get(self, "indexId"))

    @index_id.setter
    def index_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2c2f3f3c80cec4b674a4a4692e7d56a5672eeddf0fedbf383f56ab3f6059d4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "indexId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name that you assigned the FAQ when you created or updated the FAQ.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03513ddd0ecb5609bc31c5c091acd9ea713910ed9b86a77f8d0b0dab1d74ca0b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of a role with permission to access the S3 bucket that contains the FAQ.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__211f9d785f9aa932390b4387a36468593141a00aad0fa66cfb3d57af0924d14d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="s3Path")
    def s3_path(
        self,
    ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnFaq.S3PathProperty"]:
        '''The Amazon Simple Storage Service (Amazon S3) location of the FAQ input data.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-s3path
        '''
        return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnFaq.S3PathProperty"], jsii.get(self, "s3Path"))

    @s3_path.setter
    def s3_path(
        self,
        value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnFaq.S3PathProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1953eff083f69f2a10a608c97b42ac6296d3325935b824dc461953b1918a833)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3Path", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the FAQ.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d433f4df733fa6a1fa7dc2230f5a7552d9b05a432e85192ee89856dfb12f747e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="fileFormat")
    def file_format(self) -> typing.Optional[builtins.str]:
        '''The format of the input file.

        You can choose between a basic CSV format, a CSV format that includes customs attributes in a header, and a JSON format that includes custom attributes.

        The format must match the format of the file stored in the S3 bucket identified in the S3Path parameter.

        Valid values are:

        - ``CSV``
        - ``CSV_WITH_HEADER``
        - ``JSON``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-fileformat
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileFormat"))

    @file_format.setter
    def file_format(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c37eea23978725a4ed038d3aba9ef50585677c733a7b2ff767c0f0381f51e6ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileFormat", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnFaq.S3PathProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket": "bucket", "key": "key"},
    )
    class S3PathProperty:
        def __init__(self, *, bucket: builtins.str, key: builtins.str) -> None:
            '''Information required to find a specific file in an Amazon S3 bucket.

            :param bucket: The name of the S3 bucket that contains the file.
            :param key: The name of the file.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-faq-s3path.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                s3_path_property = kendra.CfnFaq.S3PathProperty(
                    bucket="bucket",
                    key="key"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ce5c3602f1c0097d46c431e26f3ccb335cf40ac53cd2cd7dbbec06b27d14fbba)
                check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket": bucket,
                "key": key,
            }

        @builtins.property
        def bucket(self) -> builtins.str:
            '''The name of the S3 bucket that contains the file.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-faq-s3path.html#cfn-kendra-faq-s3path-bucket
            '''
            result = self._values.get("bucket")
            assert result is not None, "Required property 'bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key(self) -> builtins.str:
            '''The name of the file.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-faq-s3path.html#cfn-kendra-faq-s3path-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3PathProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-kendra.CfnFaqProps",
    jsii_struct_bases=[],
    name_mapping={
        "index_id": "indexId",
        "name": "name",
        "role_arn": "roleArn",
        "s3_path": "s3Path",
        "description": "description",
        "file_format": "fileFormat",
        "tags": "tags",
    },
)
class CfnFaqProps:
    def __init__(
        self,
        *,
        index_id: builtins.str,
        name: builtins.str,
        role_arn: builtins.str,
        s3_path: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnFaq.S3PathProperty, typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        file_format: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnFaq``.

        :param index_id: The identifier of the index that contains the FAQ.
        :param name: The name that you assigned the FAQ when you created or updated the FAQ.
        :param role_arn: The Amazon Resource Name (ARN) of a role with permission to access the S3 bucket that contains the FAQ.
        :param s3_path: The Amazon Simple Storage Service (Amazon S3) location of the FAQ input data.
        :param description: A description for the FAQ.
        :param file_format: The format of the input file. You can choose between a basic CSV format, a CSV format that includes customs attributes in a header, and a JSON format that includes custom attributes. The format must match the format of the file stored in the S3 bucket identified in the S3Path parameter. Valid values are: - ``CSV`` - ``CSV_WITH_HEADER`` - ``JSON``
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_kendra as kendra
            
            cfn_faq_props = kendra.CfnFaqProps(
                index_id="indexId",
                name="name",
                role_arn="roleArn",
                s3_path=kendra.CfnFaq.S3PathProperty(
                    bucket="bucket",
                    key="key"
                ),
            
                # the properties below are optional
                description="description",
                file_format="fileFormat",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6d3c7f7d6a70914370ad158a0f4367ddb09e670825d70ff465c1fa85f619bdc)
            check_type(argname="argument index_id", value=index_id, expected_type=type_hints["index_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument s3_path", value=s3_path, expected_type=type_hints["s3_path"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument file_format", value=file_format, expected_type=type_hints["file_format"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "index_id": index_id,
            "name": name,
            "role_arn": role_arn,
            "s3_path": s3_path,
        }
        if description is not None:
            self._values["description"] = description
        if file_format is not None:
            self._values["file_format"] = file_format
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def index_id(self) -> builtins.str:
        '''The identifier of the index that contains the FAQ.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-indexid
        '''
        result = self._values.get("index_id")
        assert result is not None, "Required property 'index_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name that you assigned the FAQ when you created or updated the FAQ.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of a role with permission to access the S3 bucket that contains the FAQ.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def s3_path(
        self,
    ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnFaq.S3PathProperty]:
        '''The Amazon Simple Storage Service (Amazon S3) location of the FAQ input data.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-s3path
        '''
        result = self._values.get("s3_path")
        assert result is not None, "Required property 's3_path' is missing"
        return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnFaq.S3PathProperty], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the FAQ.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file_format(self) -> typing.Optional[builtins.str]:
        '''The format of the input file.

        You can choose between a basic CSV format, a CSV format that includes customs attributes in a header, and a JSON format that includes custom attributes.

        The format must match the format of the file stored in the S3 bucket identified in the S3Path parameter.

        Valid values are:

        - ``CSV``
        - ``CSV_WITH_HEADER``
        - ``JSON``

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-fileformat
        '''
        result = self._values.get("file_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFaqProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnIndex(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-kendra.CfnIndex",
):
    '''A CloudFormation ``AWS::Kendra::Index``.

    Creates an Amazon Kendra index

    Once the index is active you can add documents to your index using the `BatchPutDocument <https://docs.aws.amazon.com/kendra/latest/dg/BatchPutDocument.html>`_ operation or using one of the supported data sources.

    :cloudformationResource: AWS::Kendra::Index
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_kendra as kendra
        
        cfn_index = kendra.CfnIndex(self, "MyCfnIndex",
            edition="edition",
            name="name",
            role_arn="roleArn",
        
            # the properties below are optional
            capacity_units=kendra.CfnIndex.CapacityUnitsConfigurationProperty(
                query_capacity_units=123,
                storage_capacity_units=123
            ),
            description="description",
            document_metadata_configurations=[kendra.CfnIndex.DocumentMetadataConfigurationProperty(
                name="name",
                type="type",
        
                # the properties below are optional
                relevance=kendra.CfnIndex.RelevanceProperty(
                    duration="duration",
                    freshness=False,
                    importance=123,
                    rank_order="rankOrder",
                    value_importance_items=[kendra.CfnIndex.ValueImportanceItemProperty(
                        key="key",
                        value=123
                    )]
                ),
                search=kendra.CfnIndex.SearchProperty(
                    displayable=False,
                    facetable=False,
                    searchable=False,
                    sortable=False
                )
            )],
            server_side_encryption_configuration=kendra.CfnIndex.ServerSideEncryptionConfigurationProperty(
                kms_key_id="kmsKeyId"
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            user_context_policy="userContextPolicy",
            user_token_configurations=[kendra.CfnIndex.UserTokenConfigurationProperty(
                json_token_type_configuration=kendra.CfnIndex.JsonTokenTypeConfigurationProperty(
                    group_attribute_field="groupAttributeField",
                    user_name_attribute_field="userNameAttributeField"
                ),
                jwt_token_type_configuration=kendra.CfnIndex.JwtTokenTypeConfigurationProperty(
                    key_location="keyLocation",
        
                    # the properties below are optional
                    claim_regex="claimRegex",
                    group_attribute_field="groupAttributeField",
                    issuer="issuer",
                    secret_manager_arn="secretManagerArn",
                    url="url",
                    user_name_attribute_field="userNameAttributeField"
                )
            )]
        )
    '''

    def __init__(
        self,
        scope: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        edition: builtins.str,
        name: builtins.str,
        role_arn: builtins.str,
        capacity_units: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnIndex.CapacityUnitsConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        document_metadata_configurations: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnIndex.DocumentMetadataConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        server_side_encryption_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnIndex.ServerSideEncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
        user_context_policy: typing.Optional[builtins.str] = None,
        user_token_configurations: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnIndex.UserTokenConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Kendra::Index``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param edition: Indicates whether the index is a Enterprise Edition index or a Developer Edition index. Valid values are ``DEVELOPER_EDITION`` and ``ENTERPRISE_EDITION`` .
        :param name: The name of the index.
        :param role_arn: An IAM role that gives Amazon Kendra permissions to access your Amazon CloudWatch logs and metrics. This is also the role used when you use the `BatchPutDocument <https://docs.aws.amazon.com/kendra/latest/dg/BatchPutDocument.html>`_ operation to index documents from an Amazon S3 bucket.
        :param capacity_units: ``AWS::Kendra::Index.CapacityUnits``.
        :param description: A description for the index.
        :param document_metadata_configurations: Specifies the properties of an index field. You can add either a custom or a built-in field. You can add and remove built-in fields at any time. When a built-in field is removed it's configuration reverts to the default for the field. Custom fields can't be removed from an index after they are added.
        :param server_side_encryption_configuration: The identifier of the AWS KMS customer managed key (CMK) to use to encrypt data indexed by Amazon Kendra. Amazon Kendra doesn't support asymmetric CMKs.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param user_context_policy: The user context policy. ATTRIBUTE_FILTER - All indexed content is searchable and displayable for all users. If you want to filter search results on user context, you can use the attribute filters of ``_user_id`` and ``_group_ids`` or you can provide user and group information in ``UserContext`` . USER_TOKEN - Enables token-based user access control to filter search results on user context. All documents with no access control and all documents accessible to the user will be searchable and displayable.
        :param user_token_configurations: Defines the type of user token used for the index.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f4962c86ecad8a21588a24f555167043116fa4bb101c3e374054a59f8552e87)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnIndexProps(
            edition=edition,
            name=name,
            role_arn=role_arn,
            capacity_units=capacity_units,
            description=description,
            document_metadata_configurations=document_metadata_configurations,
            server_side_encryption_configuration=server_side_encryption_configuration,
            tags=tags,
            user_context_policy=user_context_policy,
            user_token_configurations=user_token_configurations,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8307c178571fcb836fa428a0f18d2a11638105c4e43c75e89e75cbd5d1f3e31d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cdf89fa9fa5b0045e5254f7f6dbb50be440d1ca20e0e23b215bdad8d7d17e05a)
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
        '''The Amazon Resource Name (ARN) of the index.

        For example: ``arn:aws:kendra:us-west-2:111122223333:index/0123456789abcdef`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The identifier for the index.

        For example: ``f4aeaa10-8056-4b2c-a343-522ca0f41234`` .

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _aws_cdk_core_f4b25747.TagManager:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-tags
        '''
        return typing.cast(_aws_cdk_core_f4b25747.TagManager, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="edition")
    def edition(self) -> builtins.str:
        '''Indicates whether the index is a Enterprise Edition index or a Developer Edition index.

        Valid values are ``DEVELOPER_EDITION`` and ``ENTERPRISE_EDITION`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-edition
        '''
        return typing.cast(builtins.str, jsii.get(self, "edition"))

    @edition.setter
    def edition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13bb66f77820d14599141ade0c8ac1ed9cafeeab163afffe66a709e4df4550a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "edition", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the index.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2893d2822c0f680e3ae3f99d4c31afbce2d7274afaf4332248a4733750015144)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''An IAM role that gives Amazon Kendra permissions to access your Amazon CloudWatch logs and metrics.

        This is also the role used when you use the `BatchPutDocument <https://docs.aws.amazon.com/kendra/latest/dg/BatchPutDocument.html>`_ operation to index documents from an Amazon S3 bucket.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08297ad63e24b8901a60dd7d4cd79d46368e2be02b01c3e28c91e2c0e7a2e813)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="capacityUnits")
    def capacity_units(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnIndex.CapacityUnitsConfigurationProperty"]]:
        '''``AWS::Kendra::Index.CapacityUnits``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-capacityunits
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnIndex.CapacityUnitsConfigurationProperty"]], jsii.get(self, "capacityUnits"))

    @capacity_units.setter
    def capacity_units(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnIndex.CapacityUnitsConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e0fbf2786717286c0e825002d1faa0d35387f64116f65de75d2e2872ab387f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacityUnits", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the index.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea856d03293bc15138c4bbc924441cc7bb9ab65452b4d8fa8058b8f93b89de48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="documentMetadataConfigurations")
    def document_metadata_configurations(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnIndex.DocumentMetadataConfigurationProperty"]]]]:
        '''Specifies the properties of an index field.

        You can add either a custom or a built-in field. You can add and remove built-in fields at any time. When a built-in field is removed it's configuration reverts to the default for the field. Custom fields can't be removed from an index after they are added.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-documentmetadataconfigurations
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnIndex.DocumentMetadataConfigurationProperty"]]]], jsii.get(self, "documentMetadataConfigurations"))

    @document_metadata_configurations.setter
    def document_metadata_configurations(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnIndex.DocumentMetadataConfigurationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ddc766b6df5028f55eda513046f17b3f975c0c833b9e458fe16cad3de399dcf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "documentMetadataConfigurations", value)

    @builtins.property
    @jsii.member(jsii_name="serverSideEncryptionConfiguration")
    def server_side_encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnIndex.ServerSideEncryptionConfigurationProperty"]]:
        '''The identifier of the AWS KMS customer managed key (CMK) to use to encrypt data indexed by Amazon Kendra.

        Amazon Kendra doesn't support asymmetric CMKs.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-serversideencryptionconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnIndex.ServerSideEncryptionConfigurationProperty"]], jsii.get(self, "serverSideEncryptionConfiguration"))

    @server_side_encryption_configuration.setter
    def server_side_encryption_configuration(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnIndex.ServerSideEncryptionConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9ba173dd7347d90c8f598d8684ca1655ca953353c1e475c81356104764fad29)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverSideEncryptionConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="userContextPolicy")
    def user_context_policy(self) -> typing.Optional[builtins.str]:
        '''The user context policy.

        ATTRIBUTE_FILTER

        - All indexed content is searchable and displayable for all users. If you want to filter search results on user context, you can use the attribute filters of ``_user_id`` and ``_group_ids`` or you can provide user and group information in ``UserContext`` .

        USER_TOKEN

        - Enables token-based user access control to filter search results on user context. All documents with no access control and all documents accessible to the user will be searchable and displayable.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-usercontextpolicy
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userContextPolicy"))

    @user_context_policy.setter
    def user_context_policy(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fed85dd48f35ea19282b64a9770efe37cb91d1992560303b83600e4cff3e79f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userContextPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="userTokenConfigurations")
    def user_token_configurations(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnIndex.UserTokenConfigurationProperty"]]]]:
        '''Defines the type of user token used for the index.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-usertokenconfigurations
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnIndex.UserTokenConfigurationProperty"]]]], jsii.get(self, "userTokenConfigurations"))

    @user_token_configurations.setter
    def user_token_configurations(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnIndex.UserTokenConfigurationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef1f1011ab1e1a36293803fb70f47a05c4e46c1e09883ce65cd4796a49895f7e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userTokenConfigurations", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnIndex.CapacityUnitsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "query_capacity_units": "queryCapacityUnits",
            "storage_capacity_units": "storageCapacityUnits",
        },
    )
    class CapacityUnitsConfigurationProperty:
        def __init__(
            self,
            *,
            query_capacity_units: jsii.Number,
            storage_capacity_units: jsii.Number,
        ) -> None:
            '''Specifies additional capacity units configured for your Enterprise Edition index.

            You can add and remove capacity units to fit your usage requirements.

            :param query_capacity_units: The amount of extra query capacity for an index and `GetQuerySuggestions <https://docs.aws.amazon.com/kendra/latest/dg/API_GetQuerySuggestions.html>`_ capacity. A single extra capacity unit for an index provides 0.1 queries per second or approximately 8,000 queries per day. You can add up to 100 extra capacity units. ``GetQuerySuggestions`` capacity is five times the provisioned query capacity for an index, or the base capacity of 2.5 calls per second, whichever is higher. For example, the base capacity for an index is 0.1 queries per second, and ``GetQuerySuggestions`` capacity has a base of 2.5 calls per second. If you add another 0.1 queries per second to total 0.2 queries per second for an index, the ``GetQuerySuggestions`` capacity is 2.5 calls per second (higher than five times 0.2 queries per second).
            :param storage_capacity_units: The amount of extra storage capacity for an index. A single capacity unit provides 30 GB of storage space or 100,000 documents, whichever is reached first. You can add up to 100 extra capacity units.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-capacityunitsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                capacity_units_configuration_property = kendra.CfnIndex.CapacityUnitsConfigurationProperty(
                    query_capacity_units=123,
                    storage_capacity_units=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a03e13b957bf6ef2b230204c5639848e1bc7eb4b5d53880d439189d604c381f7)
                check_type(argname="argument query_capacity_units", value=query_capacity_units, expected_type=type_hints["query_capacity_units"])
                check_type(argname="argument storage_capacity_units", value=storage_capacity_units, expected_type=type_hints["storage_capacity_units"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "query_capacity_units": query_capacity_units,
                "storage_capacity_units": storage_capacity_units,
            }

        @builtins.property
        def query_capacity_units(self) -> jsii.Number:
            '''The amount of extra query capacity for an index and `GetQuerySuggestions <https://docs.aws.amazon.com/kendra/latest/dg/API_GetQuerySuggestions.html>`_ capacity.

            A single extra capacity unit for an index provides 0.1 queries per second or approximately 8,000 queries per day. You can add up to 100 extra capacity units.

            ``GetQuerySuggestions`` capacity is five times the provisioned query capacity for an index, or the base capacity of 2.5 calls per second, whichever is higher. For example, the base capacity for an index is 0.1 queries per second, and ``GetQuerySuggestions`` capacity has a base of 2.5 calls per second. If you add another 0.1 queries per second to total 0.2 queries per second for an index, the ``GetQuerySuggestions`` capacity is 2.5 calls per second (higher than five times 0.2 queries per second).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-capacityunitsconfiguration.html#cfn-kendra-index-capacityunitsconfiguration-querycapacityunits
            '''
            result = self._values.get("query_capacity_units")
            assert result is not None, "Required property 'query_capacity_units' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def storage_capacity_units(self) -> jsii.Number:
            '''The amount of extra storage capacity for an index.

            A single capacity unit provides 30 GB of storage space or 100,000 documents, whichever is reached first. You can add up to 100 extra capacity units.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-capacityunitsconfiguration.html#cfn-kendra-index-capacityunitsconfiguration-storagecapacityunits
            '''
            result = self._values.get("storage_capacity_units")
            assert result is not None, "Required property 'storage_capacity_units' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CapacityUnitsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnIndex.DocumentMetadataConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "type": "type",
            "relevance": "relevance",
            "search": "search",
        },
    )
    class DocumentMetadataConfigurationProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            type: builtins.str,
            relevance: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnIndex.RelevanceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            search: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnIndex.SearchProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies the properties, such as relevance tuning and searchability, of an index field.

            :param name: The name of the index field.
            :param type: The data type of the index field.
            :param relevance: Provides tuning parameters to determine how the field affects the search results.
            :param search: Provides information about how the field is used during a search.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-documentmetadataconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                document_metadata_configuration_property = kendra.CfnIndex.DocumentMetadataConfigurationProperty(
                    name="name",
                    type="type",
                
                    # the properties below are optional
                    relevance=kendra.CfnIndex.RelevanceProperty(
                        duration="duration",
                        freshness=False,
                        importance=123,
                        rank_order="rankOrder",
                        value_importance_items=[kendra.CfnIndex.ValueImportanceItemProperty(
                            key="key",
                            value=123
                        )]
                    ),
                    search=kendra.CfnIndex.SearchProperty(
                        displayable=False,
                        facetable=False,
                        searchable=False,
                        sortable=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__69f22718a5ee54e2b50c78012eaf2e3f5a886c02b96fdbe9e3dd731d895a48b2)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument relevance", value=relevance, expected_type=type_hints["relevance"])
                check_type(argname="argument search", value=search, expected_type=type_hints["search"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "type": type,
            }
            if relevance is not None:
                self._values["relevance"] = relevance
            if search is not None:
                self._values["search"] = search

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the index field.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-documentmetadataconfiguration.html#cfn-kendra-index-documentmetadataconfiguration-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The data type of the index field.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-documentmetadataconfiguration.html#cfn-kendra-index-documentmetadataconfiguration-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def relevance(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnIndex.RelevanceProperty"]]:
            '''Provides tuning parameters to determine how the field affects the search results.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-documentmetadataconfiguration.html#cfn-kendra-index-documentmetadataconfiguration-relevance
            '''
            result = self._values.get("relevance")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnIndex.RelevanceProperty"]], result)

        @builtins.property
        def search(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnIndex.SearchProperty"]]:
            '''Provides information about how the field is used during a search.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-documentmetadataconfiguration.html#cfn-kendra-index-documentmetadataconfiguration-search
            '''
            result = self._values.get("search")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnIndex.SearchProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DocumentMetadataConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnIndex.JsonTokenTypeConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "group_attribute_field": "groupAttributeField",
            "user_name_attribute_field": "userNameAttributeField",
        },
    )
    class JsonTokenTypeConfigurationProperty:
        def __init__(
            self,
            *,
            group_attribute_field: builtins.str,
            user_name_attribute_field: builtins.str,
        ) -> None:
            '''Provides the configuration information for the JSON token type.

            :param group_attribute_field: The group attribute field.
            :param user_name_attribute_field: The user name attribute field.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jsontokentypeconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                json_token_type_configuration_property = kendra.CfnIndex.JsonTokenTypeConfigurationProperty(
                    group_attribute_field="groupAttributeField",
                    user_name_attribute_field="userNameAttributeField"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ceaab6e00a0352a748cd403853e892d781af46e109a602808ca7a99324c5cec4)
                check_type(argname="argument group_attribute_field", value=group_attribute_field, expected_type=type_hints["group_attribute_field"])
                check_type(argname="argument user_name_attribute_field", value=user_name_attribute_field, expected_type=type_hints["user_name_attribute_field"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "group_attribute_field": group_attribute_field,
                "user_name_attribute_field": user_name_attribute_field,
            }

        @builtins.property
        def group_attribute_field(self) -> builtins.str:
            '''The group attribute field.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jsontokentypeconfiguration.html#cfn-kendra-index-jsontokentypeconfiguration-groupattributefield
            '''
            result = self._values.get("group_attribute_field")
            assert result is not None, "Required property 'group_attribute_field' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def user_name_attribute_field(self) -> builtins.str:
            '''The user name attribute field.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jsontokentypeconfiguration.html#cfn-kendra-index-jsontokentypeconfiguration-usernameattributefield
            '''
            result = self._values.get("user_name_attribute_field")
            assert result is not None, "Required property 'user_name_attribute_field' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JsonTokenTypeConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnIndex.JwtTokenTypeConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "key_location": "keyLocation",
            "claim_regex": "claimRegex",
            "group_attribute_field": "groupAttributeField",
            "issuer": "issuer",
            "secret_manager_arn": "secretManagerArn",
            "url": "url",
            "user_name_attribute_field": "userNameAttributeField",
        },
    )
    class JwtTokenTypeConfigurationProperty:
        def __init__(
            self,
            *,
            key_location: builtins.str,
            claim_regex: typing.Optional[builtins.str] = None,
            group_attribute_field: typing.Optional[builtins.str] = None,
            issuer: typing.Optional[builtins.str] = None,
            secret_manager_arn: typing.Optional[builtins.str] = None,
            url: typing.Optional[builtins.str] = None,
            user_name_attribute_field: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides the configuration information for the JWT token type.

            :param key_location: The location of the key.
            :param claim_regex: The regular expression that identifies the claim.
            :param group_attribute_field: The group attribute field.
            :param issuer: The issuer of the token.
            :param secret_manager_arn: The Amazon Resource Name (arn) of the secret.
            :param url: The signing key URL.
            :param user_name_attribute_field: The user name attribute field.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jwttokentypeconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                jwt_token_type_configuration_property = kendra.CfnIndex.JwtTokenTypeConfigurationProperty(
                    key_location="keyLocation",
                
                    # the properties below are optional
                    claim_regex="claimRegex",
                    group_attribute_field="groupAttributeField",
                    issuer="issuer",
                    secret_manager_arn="secretManagerArn",
                    url="url",
                    user_name_attribute_field="userNameAttributeField"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__462c201496ce236f051289ec80cdd046522a03f66a2c470cb4a101d73e492ced)
                check_type(argname="argument key_location", value=key_location, expected_type=type_hints["key_location"])
                check_type(argname="argument claim_regex", value=claim_regex, expected_type=type_hints["claim_regex"])
                check_type(argname="argument group_attribute_field", value=group_attribute_field, expected_type=type_hints["group_attribute_field"])
                check_type(argname="argument issuer", value=issuer, expected_type=type_hints["issuer"])
                check_type(argname="argument secret_manager_arn", value=secret_manager_arn, expected_type=type_hints["secret_manager_arn"])
                check_type(argname="argument url", value=url, expected_type=type_hints["url"])
                check_type(argname="argument user_name_attribute_field", value=user_name_attribute_field, expected_type=type_hints["user_name_attribute_field"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key_location": key_location,
            }
            if claim_regex is not None:
                self._values["claim_regex"] = claim_regex
            if group_attribute_field is not None:
                self._values["group_attribute_field"] = group_attribute_field
            if issuer is not None:
                self._values["issuer"] = issuer
            if secret_manager_arn is not None:
                self._values["secret_manager_arn"] = secret_manager_arn
            if url is not None:
                self._values["url"] = url
            if user_name_attribute_field is not None:
                self._values["user_name_attribute_field"] = user_name_attribute_field

        @builtins.property
        def key_location(self) -> builtins.str:
            '''The location of the key.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jwttokentypeconfiguration.html#cfn-kendra-index-jwttokentypeconfiguration-keylocation
            '''
            result = self._values.get("key_location")
            assert result is not None, "Required property 'key_location' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def claim_regex(self) -> typing.Optional[builtins.str]:
            '''The regular expression that identifies the claim.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jwttokentypeconfiguration.html#cfn-kendra-index-jwttokentypeconfiguration-claimregex
            '''
            result = self._values.get("claim_regex")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def group_attribute_field(self) -> typing.Optional[builtins.str]:
            '''The group attribute field.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jwttokentypeconfiguration.html#cfn-kendra-index-jwttokentypeconfiguration-groupattributefield
            '''
            result = self._values.get("group_attribute_field")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def issuer(self) -> typing.Optional[builtins.str]:
            '''The issuer of the token.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jwttokentypeconfiguration.html#cfn-kendra-index-jwttokentypeconfiguration-issuer
            '''
            result = self._values.get("issuer")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secret_manager_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (arn) of the secret.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jwttokentypeconfiguration.html#cfn-kendra-index-jwttokentypeconfiguration-secretmanagerarn
            '''
            result = self._values.get("secret_manager_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def url(self) -> typing.Optional[builtins.str]:
            '''The signing key URL.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jwttokentypeconfiguration.html#cfn-kendra-index-jwttokentypeconfiguration-url
            '''
            result = self._values.get("url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def user_name_attribute_field(self) -> typing.Optional[builtins.str]:
            '''The user name attribute field.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-jwttokentypeconfiguration.html#cfn-kendra-index-jwttokentypeconfiguration-usernameattributefield
            '''
            result = self._values.get("user_name_attribute_field")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JwtTokenTypeConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnIndex.RelevanceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "duration": "duration",
            "freshness": "freshness",
            "importance": "importance",
            "rank_order": "rankOrder",
            "value_importance_items": "valueImportanceItems",
        },
    )
    class RelevanceProperty:
        def __init__(
            self,
            *,
            duration: typing.Optional[builtins.str] = None,
            freshness: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            importance: typing.Optional[jsii.Number] = None,
            rank_order: typing.Optional[builtins.str] = None,
            value_importance_items: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnIndex.ValueImportanceItemProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Provides information for tuning the relevance of a field in a search.

            When a query includes terms that match the field, the results are given a boost in the response based on these tuning parameters.

            :param duration: Specifies the time period that the boost applies to. For example, to make the boost apply to documents with the field value within the last month, you would use "2628000s". Once the field value is beyond the specified range, the effect of the boost drops off. The higher the importance, the faster the effect drops off. If you don't specify a value, the default is 3 months. The value of the field is a numeric string followed by the character "s", for example "86400s" for one day, or "604800s" for one week. Only applies to ``DATE`` fields.
            :param freshness: Indicates that this field determines how "fresh" a document is. For example, if document 1 was created on November 5, and document 2 was created on October 31, document 1 is "fresher" than document 2. You can only set the ``Freshness`` field on one ``DATE`` type field. Only applies to ``DATE`` fields.
            :param importance: The relative importance of the field in the search. Larger numbers provide more of a boost than smaller numbers.
            :param rank_order: Determines how values should be interpreted. When the ``RankOrder`` field is ``ASCENDING`` , higher numbers are better. For example, a document with a rating score of 10 is higher ranking than a document with a rating score of 1. When the ``RankOrder`` field is ``DESCENDING`` , lower numbers are better. For example, in a task tracking application, a priority 1 task is more important than a priority 5 task. Only applies to ``LONG`` and ``DOUBLE`` fields.
            :param value_importance_items: An array of key-value pairs for different boosts when they appear in the search result list. For example, if you want to boost query terms that match the "department" field in the result, query terms that match this field are boosted in the result. You can add entries from the department field to boost documents with those values higher. For example, you can add entries to the map with names of departments. If you add "HR", 5 and "Legal",3 those departments are given special attention when they appear in the metadata of a document.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-relevance.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                relevance_property = kendra.CfnIndex.RelevanceProperty(
                    duration="duration",
                    freshness=False,
                    importance=123,
                    rank_order="rankOrder",
                    value_importance_items=[kendra.CfnIndex.ValueImportanceItemProperty(
                        key="key",
                        value=123
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__acec0091ac009b19879d61ea8e788654c5f97d5f6018ca72bc4d747a0365301f)
                check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
                check_type(argname="argument freshness", value=freshness, expected_type=type_hints["freshness"])
                check_type(argname="argument importance", value=importance, expected_type=type_hints["importance"])
                check_type(argname="argument rank_order", value=rank_order, expected_type=type_hints["rank_order"])
                check_type(argname="argument value_importance_items", value=value_importance_items, expected_type=type_hints["value_importance_items"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if duration is not None:
                self._values["duration"] = duration
            if freshness is not None:
                self._values["freshness"] = freshness
            if importance is not None:
                self._values["importance"] = importance
            if rank_order is not None:
                self._values["rank_order"] = rank_order
            if value_importance_items is not None:
                self._values["value_importance_items"] = value_importance_items

        @builtins.property
        def duration(self) -> typing.Optional[builtins.str]:
            '''Specifies the time period that the boost applies to.

            For example, to make the boost apply to documents with the field value within the last month, you would use "2628000s". Once the field value is beyond the specified range, the effect of the boost drops off. The higher the importance, the faster the effect drops off. If you don't specify a value, the default is 3 months. The value of the field is a numeric string followed by the character "s", for example "86400s" for one day, or "604800s" for one week.

            Only applies to ``DATE`` fields.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-relevance.html#cfn-kendra-index-relevance-duration
            '''
            result = self._values.get("duration")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def freshness(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''Indicates that this field determines how "fresh" a document is.

            For example, if document 1 was created on November 5, and document 2 was created on October 31, document 1 is "fresher" than document 2. You can only set the ``Freshness`` field on one ``DATE`` type field. Only applies to ``DATE`` fields.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-relevance.html#cfn-kendra-index-relevance-freshness
            '''
            result = self._values.get("freshness")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def importance(self) -> typing.Optional[jsii.Number]:
            '''The relative importance of the field in the search.

            Larger numbers provide more of a boost than smaller numbers.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-relevance.html#cfn-kendra-index-relevance-importance
            '''
            result = self._values.get("importance")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def rank_order(self) -> typing.Optional[builtins.str]:
            '''Determines how values should be interpreted.

            When the ``RankOrder`` field is ``ASCENDING`` , higher numbers are better. For example, a document with a rating score of 10 is higher ranking than a document with a rating score of 1.

            When the ``RankOrder`` field is ``DESCENDING`` , lower numbers are better. For example, in a task tracking application, a priority 1 task is more important than a priority 5 task.

            Only applies to ``LONG`` and ``DOUBLE`` fields.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-relevance.html#cfn-kendra-index-relevance-rankorder
            '''
            result = self._values.get("rank_order")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value_importance_items(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnIndex.ValueImportanceItemProperty"]]]]:
            '''An array of key-value pairs for different boosts when they appear in the search result list.

            For example, if you want to boost query terms that match the "department" field in the result, query terms that match this field are boosted in the result. You can add entries from the department field to boost documents with those values higher.

            For example, you can add entries to the map with names of departments. If you add "HR", 5 and "Legal",3 those departments are given special attention when they appear in the metadata of a document.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-relevance.html#cfn-kendra-index-relevance-valueimportanceitems
            '''
            result = self._values.get("value_importance_items")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnIndex.ValueImportanceItemProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RelevanceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnIndex.SearchProperty",
        jsii_struct_bases=[],
        name_mapping={
            "displayable": "displayable",
            "facetable": "facetable",
            "searchable": "searchable",
            "sortable": "sortable",
        },
    )
    class SearchProperty:
        def __init__(
            self,
            *,
            displayable: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            facetable: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            searchable: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            sortable: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
        ) -> None:
            '''Provides information about how a custom index field is used during a search.

            :param displayable: Determines whether the field is returned in the query response. The default is ``true`` .
            :param facetable: Indicates that the field can be used to create search facets, a count of results for each value in the field. The default is ``false`` .
            :param searchable: Determines whether the field is used in the search. If the ``Searchable`` field is ``true`` , you can use relevance tuning to manually tune how Amazon Kendra weights the field in the search. The default is ``true`` for string fields and ``false`` for number and date fields.
            :param sortable: Determines whether the field can be used to sort the results of a query. The default is ``false`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-search.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                search_property = kendra.CfnIndex.SearchProperty(
                    displayable=False,
                    facetable=False,
                    searchable=False,
                    sortable=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__883e6e9b7a8a239400069c1c9950b5dec0955c6fbb1e5947a3175f04cdbc97ed)
                check_type(argname="argument displayable", value=displayable, expected_type=type_hints["displayable"])
                check_type(argname="argument facetable", value=facetable, expected_type=type_hints["facetable"])
                check_type(argname="argument searchable", value=searchable, expected_type=type_hints["searchable"])
                check_type(argname="argument sortable", value=sortable, expected_type=type_hints["sortable"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if displayable is not None:
                self._values["displayable"] = displayable
            if facetable is not None:
                self._values["facetable"] = facetable
            if searchable is not None:
                self._values["searchable"] = searchable
            if sortable is not None:
                self._values["sortable"] = sortable

        @builtins.property
        def displayable(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''Determines whether the field is returned in the query response.

            The default is ``true`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-search.html#cfn-kendra-index-search-displayable
            '''
            result = self._values.get("displayable")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def facetable(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''Indicates that the field can be used to create search facets, a count of results for each value in the field.

            The default is ``false`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-search.html#cfn-kendra-index-search-facetable
            '''
            result = self._values.get("facetable")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def searchable(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''Determines whether the field is used in the search.

            If the ``Searchable`` field is ``true`` , you can use relevance tuning to manually tune how Amazon Kendra weights the field in the search. The default is ``true`` for string fields and ``false`` for number and date fields.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-search.html#cfn-kendra-index-search-searchable
            '''
            result = self._values.get("searchable")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def sortable(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''Determines whether the field can be used to sort the results of a query.

            The default is ``false`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-search.html#cfn-kendra-index-search-sortable
            '''
            result = self._values.get("sortable")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SearchProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnIndex.ServerSideEncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"kms_key_id": "kmsKeyId"},
    )
    class ServerSideEncryptionConfigurationProperty:
        def __init__(self, *, kms_key_id: typing.Optional[builtins.str] = None) -> None:
            '''Provides the identifier of the AWS KMS customer master key (CMK) used to encrypt data indexed by Amazon Kendra.

            We suggest that you use a CMK from your account to help secure your index. Amazon Kendra doesn't support asymmetric CMKs.

            :param kms_key_id: The identifier of the AWS KMS key . Amazon Kendra doesn't support asymmetric keys.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-serversideencryptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                server_side_encryption_configuration_property = kendra.CfnIndex.ServerSideEncryptionConfigurationProperty(
                    kms_key_id="kmsKeyId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9e5a98bd425157d628f45c27a930a0585c6f2dbed6bad09a3e7caf1f0c7e28d2)
                check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''The identifier of the AWS KMS key .

            Amazon Kendra doesn't support asymmetric keys.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-serversideencryptionconfiguration.html#cfn-kendra-index-serversideencryptionconfiguration-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServerSideEncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnIndex.UserTokenConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "json_token_type_configuration": "jsonTokenTypeConfiguration",
            "jwt_token_type_configuration": "jwtTokenTypeConfiguration",
        },
    )
    class UserTokenConfigurationProperty:
        def __init__(
            self,
            *,
            json_token_type_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnIndex.JsonTokenTypeConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            jwt_token_type_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnIndex.JwtTokenTypeConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Provides the configuration information for a token.

            :param json_token_type_configuration: Information about the JSON token type configuration.
            :param jwt_token_type_configuration: Information about the JWT token type configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-usertokenconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                user_token_configuration_property = kendra.CfnIndex.UserTokenConfigurationProperty(
                    json_token_type_configuration=kendra.CfnIndex.JsonTokenTypeConfigurationProperty(
                        group_attribute_field="groupAttributeField",
                        user_name_attribute_field="userNameAttributeField"
                    ),
                    jwt_token_type_configuration=kendra.CfnIndex.JwtTokenTypeConfigurationProperty(
                        key_location="keyLocation",
                
                        # the properties below are optional
                        claim_regex="claimRegex",
                        group_attribute_field="groupAttributeField",
                        issuer="issuer",
                        secret_manager_arn="secretManagerArn",
                        url="url",
                        user_name_attribute_field="userNameAttributeField"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__10e3c7d841fa5151ce3a475a71a03fb223fa658d35349028884c28a978779d82)
                check_type(argname="argument json_token_type_configuration", value=json_token_type_configuration, expected_type=type_hints["json_token_type_configuration"])
                check_type(argname="argument jwt_token_type_configuration", value=jwt_token_type_configuration, expected_type=type_hints["jwt_token_type_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if json_token_type_configuration is not None:
                self._values["json_token_type_configuration"] = json_token_type_configuration
            if jwt_token_type_configuration is not None:
                self._values["jwt_token_type_configuration"] = jwt_token_type_configuration

        @builtins.property
        def json_token_type_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnIndex.JsonTokenTypeConfigurationProperty"]]:
            '''Information about the JSON token type configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-usertokenconfiguration.html#cfn-kendra-index-usertokenconfiguration-jsontokentypeconfiguration
            '''
            result = self._values.get("json_token_type_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnIndex.JsonTokenTypeConfigurationProperty"]], result)

        @builtins.property
        def jwt_token_type_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnIndex.JwtTokenTypeConfigurationProperty"]]:
            '''Information about the JWT token type configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-usertokenconfiguration.html#cfn-kendra-index-usertokenconfiguration-jwttokentypeconfiguration
            '''
            result = self._values.get("jwt_token_type_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnIndex.JwtTokenTypeConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UserTokenConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kendra.CfnIndex.ValueImportanceItemProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class ValueImportanceItemProperty:
        def __init__(
            self,
            *,
            key: typing.Optional[builtins.str] = None,
            value: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Specifies a key-value pair of the search boost value for a document when the key is part of the metadata of a document.

            :param key: The document metadata value used for the search boost.
            :param value: The boost value for a document when the key is part of the metadata of a document.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-valueimportanceitem.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kendra as kendra
                
                value_importance_item_property = kendra.CfnIndex.ValueImportanceItemProperty(
                    key="key",
                    value=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d191222e08c46f38378cc54be628016d4d18f0f83980ab0cf91a693e97aa543f)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if key is not None:
                self._values["key"] = key
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''The document metadata value used for the search boost.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-valueimportanceitem.html#cfn-kendra-index-valueimportanceitem-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[jsii.Number]:
            '''The boost value for a document when the key is part of the metadata of a document.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-valueimportanceitem.html#cfn-kendra-index-valueimportanceitem-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ValueImportanceItemProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-kendra.CfnIndexProps",
    jsii_struct_bases=[],
    name_mapping={
        "edition": "edition",
        "name": "name",
        "role_arn": "roleArn",
        "capacity_units": "capacityUnits",
        "description": "description",
        "document_metadata_configurations": "documentMetadataConfigurations",
        "server_side_encryption_configuration": "serverSideEncryptionConfiguration",
        "tags": "tags",
        "user_context_policy": "userContextPolicy",
        "user_token_configurations": "userTokenConfigurations",
    },
)
class CfnIndexProps:
    def __init__(
        self,
        *,
        edition: builtins.str,
        name: builtins.str,
        role_arn: builtins.str,
        capacity_units: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnIndex.CapacityUnitsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        document_metadata_configurations: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnIndex.DocumentMetadataConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        server_side_encryption_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnIndex.ServerSideEncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
        user_context_policy: typing.Optional[builtins.str] = None,
        user_token_configurations: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnIndex.UserTokenConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnIndex``.

        :param edition: Indicates whether the index is a Enterprise Edition index or a Developer Edition index. Valid values are ``DEVELOPER_EDITION`` and ``ENTERPRISE_EDITION`` .
        :param name: The name of the index.
        :param role_arn: An IAM role that gives Amazon Kendra permissions to access your Amazon CloudWatch logs and metrics. This is also the role used when you use the `BatchPutDocument <https://docs.aws.amazon.com/kendra/latest/dg/BatchPutDocument.html>`_ operation to index documents from an Amazon S3 bucket.
        :param capacity_units: ``AWS::Kendra::Index.CapacityUnits``.
        :param description: A description for the index.
        :param document_metadata_configurations: Specifies the properties of an index field. You can add either a custom or a built-in field. You can add and remove built-in fields at any time. When a built-in field is removed it's configuration reverts to the default for the field. Custom fields can't be removed from an index after they are added.
        :param server_side_encryption_configuration: The identifier of the AWS KMS customer managed key (CMK) to use to encrypt data indexed by Amazon Kendra. Amazon Kendra doesn't support asymmetric CMKs.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param user_context_policy: The user context policy. ATTRIBUTE_FILTER - All indexed content is searchable and displayable for all users. If you want to filter search results on user context, you can use the attribute filters of ``_user_id`` and ``_group_ids`` or you can provide user and group information in ``UserContext`` . USER_TOKEN - Enables token-based user access control to filter search results on user context. All documents with no access control and all documents accessible to the user will be searchable and displayable.
        :param user_token_configurations: Defines the type of user token used for the index.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_kendra as kendra
            
            cfn_index_props = kendra.CfnIndexProps(
                edition="edition",
                name="name",
                role_arn="roleArn",
            
                # the properties below are optional
                capacity_units=kendra.CfnIndex.CapacityUnitsConfigurationProperty(
                    query_capacity_units=123,
                    storage_capacity_units=123
                ),
                description="description",
                document_metadata_configurations=[kendra.CfnIndex.DocumentMetadataConfigurationProperty(
                    name="name",
                    type="type",
            
                    # the properties below are optional
                    relevance=kendra.CfnIndex.RelevanceProperty(
                        duration="duration",
                        freshness=False,
                        importance=123,
                        rank_order="rankOrder",
                        value_importance_items=[kendra.CfnIndex.ValueImportanceItemProperty(
                            key="key",
                            value=123
                        )]
                    ),
                    search=kendra.CfnIndex.SearchProperty(
                        displayable=False,
                        facetable=False,
                        searchable=False,
                        sortable=False
                    )
                )],
                server_side_encryption_configuration=kendra.CfnIndex.ServerSideEncryptionConfigurationProperty(
                    kms_key_id="kmsKeyId"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                user_context_policy="userContextPolicy",
                user_token_configurations=[kendra.CfnIndex.UserTokenConfigurationProperty(
                    json_token_type_configuration=kendra.CfnIndex.JsonTokenTypeConfigurationProperty(
                        group_attribute_field="groupAttributeField",
                        user_name_attribute_field="userNameAttributeField"
                    ),
                    jwt_token_type_configuration=kendra.CfnIndex.JwtTokenTypeConfigurationProperty(
                        key_location="keyLocation",
            
                        # the properties below are optional
                        claim_regex="claimRegex",
                        group_attribute_field="groupAttributeField",
                        issuer="issuer",
                        secret_manager_arn="secretManagerArn",
                        url="url",
                        user_name_attribute_field="userNameAttributeField"
                    )
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0707733901472b304f7c64d21a4b0c7cbacffd0ac000c953baf3c1430ee877a0)
            check_type(argname="argument edition", value=edition, expected_type=type_hints["edition"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument capacity_units", value=capacity_units, expected_type=type_hints["capacity_units"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument document_metadata_configurations", value=document_metadata_configurations, expected_type=type_hints["document_metadata_configurations"])
            check_type(argname="argument server_side_encryption_configuration", value=server_side_encryption_configuration, expected_type=type_hints["server_side_encryption_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument user_context_policy", value=user_context_policy, expected_type=type_hints["user_context_policy"])
            check_type(argname="argument user_token_configurations", value=user_token_configurations, expected_type=type_hints["user_token_configurations"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "edition": edition,
            "name": name,
            "role_arn": role_arn,
        }
        if capacity_units is not None:
            self._values["capacity_units"] = capacity_units
        if description is not None:
            self._values["description"] = description
        if document_metadata_configurations is not None:
            self._values["document_metadata_configurations"] = document_metadata_configurations
        if server_side_encryption_configuration is not None:
            self._values["server_side_encryption_configuration"] = server_side_encryption_configuration
        if tags is not None:
            self._values["tags"] = tags
        if user_context_policy is not None:
            self._values["user_context_policy"] = user_context_policy
        if user_token_configurations is not None:
            self._values["user_token_configurations"] = user_token_configurations

    @builtins.property
    def edition(self) -> builtins.str:
        '''Indicates whether the index is a Enterprise Edition index or a Developer Edition index.

        Valid values are ``DEVELOPER_EDITION`` and ``ENTERPRISE_EDITION`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-edition
        '''
        result = self._values.get("edition")
        assert result is not None, "Required property 'edition' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the index.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''An IAM role that gives Amazon Kendra permissions to access your Amazon CloudWatch logs and metrics.

        This is also the role used when you use the `BatchPutDocument <https://docs.aws.amazon.com/kendra/latest/dg/BatchPutDocument.html>`_ operation to index documents from an Amazon S3 bucket.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def capacity_units(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnIndex.CapacityUnitsConfigurationProperty]]:
        '''``AWS::Kendra::Index.CapacityUnits``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-capacityunits
        '''
        result = self._values.get("capacity_units")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnIndex.CapacityUnitsConfigurationProperty]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the index.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def document_metadata_configurations(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnIndex.DocumentMetadataConfigurationProperty]]]]:
        '''Specifies the properties of an index field.

        You can add either a custom or a built-in field. You can add and remove built-in fields at any time. When a built-in field is removed it's configuration reverts to the default for the field. Custom fields can't be removed from an index after they are added.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-documentmetadataconfigurations
        '''
        result = self._values.get("document_metadata_configurations")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnIndex.DocumentMetadataConfigurationProperty]]]], result)

    @builtins.property
    def server_side_encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnIndex.ServerSideEncryptionConfigurationProperty]]:
        '''The identifier of the AWS KMS customer managed key (CMK) to use to encrypt data indexed by Amazon Kendra.

        Amazon Kendra doesn't support asymmetric CMKs.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-serversideencryptionconfiguration
        '''
        result = self._values.get("server_side_encryption_configuration")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnIndex.ServerSideEncryptionConfigurationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]], result)

    @builtins.property
    def user_context_policy(self) -> typing.Optional[builtins.str]:
        '''The user context policy.

        ATTRIBUTE_FILTER

        - All indexed content is searchable and displayable for all users. If you want to filter search results on user context, you can use the attribute filters of ``_user_id`` and ``_group_ids`` or you can provide user and group information in ``UserContext`` .

        USER_TOKEN

        - Enables token-based user access control to filter search results on user context. All documents with no access control and all documents accessible to the user will be searchable and displayable.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-usercontextpolicy
        '''
        result = self._values.get("user_context_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_token_configurations(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnIndex.UserTokenConfigurationProperty]]]]:
        '''Defines the type of user token used for the index.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html#cfn-kendra-index-usertokenconfigurations
        '''
        result = self._values.get("user_token_configurations")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnIndex.UserTokenConfigurationProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnIndexProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDataSource",
    "CfnDataSourceProps",
    "CfnFaq",
    "CfnFaqProps",
    "CfnIndex",
    "CfnIndexProps",
]

publication.publish()

def _typecheckingstub__838c3775e79472827c639434b94d1cb415bc65f25d6d12e5896dab3e100005b1(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    index_id: builtins.str,
    name: builtins.str,
    type: builtins.str,
    custom_document_enrichment_configuration: typing.Optional[typing.Union[typing.Union[CfnDataSource.CustomDocumentEnrichmentConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable]] = None,
    data_source_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.DataSourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    role_arn: typing.Optional[builtins.str] = None,
    schedule: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d5d31fa3e48e4f196ab3f69173009494a068d434fc7e6d1311d65ba7c502906(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ab91ce8785e6a63b0d70715e363d1f50645e95d88006ea7fefc3b1e0a035f81(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f054cc0e922eef2864cd379fb19130f2324a2373ba765ff284d0b0ea068bdca2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95512cd9daf4fe119adae42fb422a7783562418c0503d7e9cad9e1f5decb23c1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6bcc0dd41454067a102f5153dd74d508c891b4416496138bc3d65b37ce383b3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df8a4f8da541e2f4e257fee5554cb2dbff3c43e29904e686872395eba7a3f687(
    value: typing.Optional[typing.Union[CfnDataSource.CustomDocumentEnrichmentConfigurationProperty, _aws_cdk_core_f4b25747.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cf582e4e0d93058a5d69f75ea66337c4c20e3da032652df133859f9acf7662c(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnDataSource.DataSourceConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1acaf915aee0950d33184ae0b090a90b862b5eb57845726c612b2b02b6cc6e60(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8a12b99c285b2e691b3b5c75162f4a09d7c74929bee4f696a31383855432bff(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7ba1be93af2b0769a490dd83b4fbe931296c5ab24324d25facceec7775df474(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a46122186a9433b6353533e6955e27217a2ce211d65c579ec8d34f7184bc3fa(
    *,
    key_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdc8384e21439c502e453c0e9f9e8ce3693e7db7a2956d088ec32ac22336d8d5(
    *,
    allowed_groups_column_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09effd1c50e617607c8bfcbdc57bb843bed98d278f24cdd3208a1415daba682d(
    *,
    change_detecting_columns: typing.Sequence[builtins.str],
    document_data_column_name: builtins.str,
    document_id_column_name: builtins.str,
    document_title_column_name: typing.Optional[builtins.str] = None,
    field_mappings: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.DataSourceToIndexFieldMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__576b8ee36295a821c5bb667a8a07e11843fc9c1b04276e3f72b11c096b9d21f7(
    *,
    attachment_field_mappings: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.ConfluenceAttachmentToIndexFieldMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    crawl_attachments: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__924f1647295b2a1a10fde56627c68fad198d23c1d234f6f60c8ebbfaeb285e22(
    *,
    data_source_field_name: builtins.str,
    index_field_name: builtins.str,
    date_field_format: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e96f9bee1cf4ee733165b93e2b27bb37c131f402774b3276869e5167bfefbd7(
    *,
    blog_field_mappings: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.ConfluenceBlogToIndexFieldMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83889ceeb258388b75d723227b3d33ab0585a0e337895a366822c883ec3d09f9(
    *,
    data_source_field_name: builtins.str,
    index_field_name: builtins.str,
    date_field_format: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fca3cb4b2908265aa9bc6b4fe6f5b07c7676954bc521475def0ec3c71bb84571(
    *,
    secret_arn: builtins.str,
    server_url: builtins.str,
    version: builtins.str,
    attachment_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.ConfluenceAttachmentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    blog_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.ConfluenceBlogConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    exclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
    inclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
    page_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.ConfluencePageConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    space_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.ConfluenceSpaceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.DataSourceVpcConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f52527a9371fa1296e788de62cf40b198d363bee9da4c3419b813307b2cbf18a(
    *,
    page_field_mappings: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.ConfluencePageToIndexFieldMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cefb7b06cc4104fdf1232f556342ec672704be92bc80771f6cd506c89eaba2c0(
    *,
    data_source_field_name: builtins.str,
    index_field_name: builtins.str,
    date_field_format: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edd6e444142fccf1e08d99868266ec9724c486c19845a128da9b7a4bf2c2ab01(
    *,
    crawl_archived_spaces: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    crawl_personal_spaces: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    exclude_spaces: typing.Optional[typing.Sequence[builtins.str]] = None,
    include_spaces: typing.Optional[typing.Sequence[builtins.str]] = None,
    space_field_mappings: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.ConfluenceSpaceToIndexFieldMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b38c3f2c7089b2621bd2e26fbd653f6703cb11453a622c5e9e8d151159ff3ba(
    *,
    data_source_field_name: builtins.str,
    index_field_name: builtins.str,
    date_field_format: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56480e4f803090fe216ded0da076620b1903a28234eddb142f3c8ea0edd716cb(
    *,
    database_host: builtins.str,
    database_name: builtins.str,
    database_port: jsii.Number,
    secret_arn: builtins.str,
    table_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fcf90f5571479a5ff85f931922498d973d08d8feb15738ac9bcf68f032398ec(
    *,
    inline_configurations: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.InlineCustomDocumentEnrichmentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    post_extraction_hook_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.HookConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    pre_extraction_hook_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.HookConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cd8e584e6fbffd547c6f97fa7016cd6ac83b70f5d2bb3ef5b4740e4311dc129(
    *,
    confluence_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.ConfluenceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    database_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.DatabaseConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    google_drive_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.GoogleDriveConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    one_drive_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.OneDriveConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.S3DataSourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    salesforce_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.SalesforceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    service_now_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.ServiceNowConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    share_point_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.SharePointConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    web_crawler_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.WebCrawlerConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    work_docs_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.WorkDocsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d00484f9307c2cbde1ea7c3bffedbbc149e37389717b71abeb14bea3d444404(
    *,
    data_source_field_name: builtins.str,
    index_field_name: builtins.str,
    date_field_format: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8523977b3861a731e172645f9e76e9004b8e82b143f46b2dfb1fac929d0a4001(
    *,
    security_group_ids: typing.Sequence[builtins.str],
    subnet_ids: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__625507bf30b92f47de71f7d7cf0d4eca2c026342a700972601ea6ba8bb2cdb4e(
    *,
    column_configuration: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.ColumnConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    connection_configuration: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.ConnectionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    database_engine_type: builtins.str,
    acl_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.AclConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sql_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.SqlConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.DataSourceVpcConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69b7b73760f1787f973dfe93d47b85124d0d77fea803f935b79630e83121e400(
    *,
    condition_document_attribute_key: builtins.str,
    operator: builtins.str,
    condition_on_value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.DocumentAttributeValueProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eaf296e383821da4fe186285591f4517cb6e84220ca53820c796e69864b1c7ff(
    *,
    target_document_attribute_key: builtins.str,
    target_document_attribute_value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.DocumentAttributeValueProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    target_document_attribute_value_deletion: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bcaff04493a00bb4410de5a6af34399adc1f4f0cc4155e2cacc9d1d836e4423(
    *,
    date_value: typing.Optional[builtins.str] = None,
    long_value: typing.Optional[jsii.Number] = None,
    string_list_value: typing.Optional[typing.Sequence[builtins.str]] = None,
    string_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aadc60e4754fe87872d1e909f86b0e2be2f500ba62bcddac35bc70a7f0f5cd65(
    *,
    s3_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8658af633ed7b37e5f45f8e2d3286bbe3ea33d5e931c8e79390eb7e91cd27b3(
    *,
    secret_arn: builtins.str,
    exclude_mime_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    exclude_shared_drives: typing.Optional[typing.Sequence[builtins.str]] = None,
    exclude_user_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
    exclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
    field_mappings: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.DataSourceToIndexFieldMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    inclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f88ce175d173734efc6721d6feeeb56e8658cb0561f11152633b1546afaf3467(
    *,
    lambda_arn: builtins.str,
    s3_bucket: builtins.str,
    invocation_condition: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.DocumentAttributeConditionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__778dbd7cfd60bb1372e2f7438f3c056a9ea9a9161f3caa226477890bcd99cea3(
    *,
    condition: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.DocumentAttributeConditionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    document_content_deletion: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    target: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.DocumentAttributeTargetProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf6e5efc7f0c997f06cf9f0d82afec4dfb97aaf99924cb7f954aa49cdb46aad6(
    *,
    one_drive_users: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.OneDriveUsersProperty, typing.Dict[builtins.str, typing.Any]]],
    secret_arn: builtins.str,
    tenant_domain: builtins.str,
    disable_local_groups: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    exclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
    field_mappings: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.DataSourceToIndexFieldMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    inclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b51f386d40b0bc8d28e76be7834b1e99ad4eb440721b408a31b6c03ea32fc94(
    *,
    one_drive_user_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    one_drive_user_s3_path: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.S3PathProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ee897455f83c68302294f702fdd1bef710bc383e0a7581050ba462dd652e299(
    *,
    host: builtins.str,
    port: jsii.Number,
    credentials: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e4ae625757091c33fab15f4b8e37c739fa7d7fed9de699223d5a680ac6aed34(
    *,
    bucket_name: builtins.str,
    access_control_list_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.AccessControlListConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    documents_metadata_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.DocumentsMetadataConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    exclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
    inclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
    inclusion_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c710214f188c5e4da6c2f781b8792ff32b6131c21a8e35e14587223cf96bd5a(
    *,
    bucket: builtins.str,
    key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0f0b92db66314e44cb81d511b60249e849818e202786239e76913be72c16c62(
    *,
    document_data_field_name: builtins.str,
    document_title_field_name: typing.Optional[builtins.str] = None,
    field_mappings: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.DataSourceToIndexFieldMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    include_filter_types: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe5fa142481d3b326eba699ad4f51fca25323939f0e91d3b0a128446ac069732(
    *,
    secret_arn: builtins.str,
    server_url: builtins.str,
    chatter_feed_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.SalesforceChatterFeedConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    crawl_attachments: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    exclude_attachment_file_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
    include_attachment_file_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
    knowledge_article_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.SalesforceKnowledgeArticleConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    standard_object_attachment_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.SalesforceStandardObjectAttachmentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    standard_object_configurations: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.SalesforceStandardObjectConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__151fc85c68d6264787df14a6f7d121b0319c9cc77d7c0dd10c4f55f2b29acc37(
    *,
    document_data_field_name: builtins.str,
    name: builtins.str,
    document_title_field_name: typing.Optional[builtins.str] = None,
    field_mappings: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.DataSourceToIndexFieldMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7737539f92080202809fd1b873f3311d1ab257843845347f1b4edeae69779f83(
    *,
    included_states: typing.Sequence[builtins.str],
    custom_knowledge_article_type_configurations: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.SalesforceCustomKnowledgeArticleTypeConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    standard_knowledge_article_type_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.SalesforceStandardKnowledgeArticleTypeConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e081a7372ad2646b3a525519e42d144c16f1b312003b128841e099c6b97ced8(
    *,
    document_data_field_name: builtins.str,
    document_title_field_name: typing.Optional[builtins.str] = None,
    field_mappings: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.DataSourceToIndexFieldMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__365ce3c088ddf254287d302b735b788c3446d5a1628bcaf7d2146a24cda32b33(
    *,
    document_title_field_name: typing.Optional[builtins.str] = None,
    field_mappings: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.DataSourceToIndexFieldMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b9be6fc3897a699183461bfe1b6666a951df81a01c40697ca1c9526c2e30909(
    *,
    document_data_field_name: builtins.str,
    name: builtins.str,
    document_title_field_name: typing.Optional[builtins.str] = None,
    field_mappings: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.DataSourceToIndexFieldMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eaa6596c8c308501e64f72312b61619122995461454ed8ae0fe053f0b8e029c0(
    *,
    host_url: builtins.str,
    secret_arn: builtins.str,
    service_now_build_version: builtins.str,
    authentication_type: typing.Optional[builtins.str] = None,
    knowledge_article_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.ServiceNowKnowledgeArticleConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    service_catalog_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.ServiceNowServiceCatalogConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d01a96040c4e7f6dfc7efc09a5b83b28f0019321a6f9a00ca365a421c7455a9a(
    *,
    document_data_field_name: builtins.str,
    crawl_attachments: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    document_title_field_name: typing.Optional[builtins.str] = None,
    exclude_attachment_file_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
    field_mappings: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.DataSourceToIndexFieldMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    filter_query: typing.Optional[builtins.str] = None,
    include_attachment_file_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4afd6863fb6363d54df26260263b705ca1257cf3b112217ea98696c920433bdb(
    *,
    document_data_field_name: builtins.str,
    crawl_attachments: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    document_title_field_name: typing.Optional[builtins.str] = None,
    exclude_attachment_file_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
    field_mappings: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.DataSourceToIndexFieldMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    include_attachment_file_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33b31cc3720195569251ffa27b4503a6c9e1d6ccae8db446cb20132abd4410c6(
    *,
    secret_arn: builtins.str,
    share_point_version: builtins.str,
    urls: typing.Sequence[builtins.str],
    crawl_attachments: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    disable_local_groups: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    document_title_field_name: typing.Optional[builtins.str] = None,
    exclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
    field_mappings: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.DataSourceToIndexFieldMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    inclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ssl_certificate_s3_path: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.S3PathProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    use_change_log: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    vpc_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.DataSourceVpcConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb1d3fe487d9060882af04e9daee5af8c6c483e8167066d025070c4b426f7de3(
    *,
    query_identifiers_enclosing_option: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bc0f5447a7fb82df9fef5eaf21c792414d86f01c91224795ced30c7b2f67c71(
    *,
    basic_authentication: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.WebCrawlerBasicAuthenticationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4fc4beda7b6d0eaae8fd147a36d7ac4d0b64b3d7190a4e2fd1288720dc58357(
    *,
    credentials: builtins.str,
    host: builtins.str,
    port: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__484bbf2bc0472073880a1659d98e973cfe8cfff7c2fc4583c323d9f4fc18a51c(
    *,
    urls: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.WebCrawlerUrlsProperty, typing.Dict[builtins.str, typing.Any]]],
    authentication_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.WebCrawlerAuthenticationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    crawl_depth: typing.Optional[jsii.Number] = None,
    max_content_size_per_page_in_mega_bytes: typing.Optional[jsii.Number] = None,
    max_links_per_page: typing.Optional[jsii.Number] = None,
    max_urls_per_minute_crawl_rate: typing.Optional[jsii.Number] = None,
    proxy_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.ProxyConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    url_exclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
    url_inclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3ec3ac8587d1bf68152a59168462774272ae571eeb6061c1178c797875c9144(
    *,
    seed_urls: typing.Sequence[builtins.str],
    web_crawler_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11a3e0a7b08717554425279e6a9adfda167dbef15c3515f094a9b133ee8cc9cc(
    *,
    site_maps: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__351a084f3e7d67658f1cf5efcab3016279b2b065c00b8ab5374f3f25925c7166(
    *,
    seed_url_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.WebCrawlerSeedUrlConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    site_maps_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.WebCrawlerSiteMapsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5bb8e5b0cdb6d927137ed524008b228e11190475c7c75a26dbe62a80a633d13(
    *,
    organization_id: builtins.str,
    crawl_comments: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    exclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
    field_mappings: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.DataSourceToIndexFieldMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    inclusion_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
    use_change_log: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1977d3785581586034c986c94543d103c44b06111b0826035b84d143f438cdd6(
    *,
    index_id: builtins.str,
    name: builtins.str,
    type: builtins.str,
    custom_document_enrichment_configuration: typing.Optional[typing.Union[typing.Union[CfnDataSource.CustomDocumentEnrichmentConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable]] = None,
    data_source_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnDataSource.DataSourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    role_arn: typing.Optional[builtins.str] = None,
    schedule: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab89b7a98ca53da545dcff17304c9c343f2b8a8199c1072a3399c000ce313227(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    index_id: builtins.str,
    name: builtins.str,
    role_arn: builtins.str,
    s3_path: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnFaq.S3PathProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    file_format: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e01629f08de46ef91bc4678b76ac86f611d13ddefbec5ac511265a13e2c8dc1(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67dcbe13e8527b98fdeff47eb96567738d5ef6db39feaded973a554b6710aaba(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2c2f3f3c80cec4b674a4a4692e7d56a5672eeddf0fedbf383f56ab3f6059d4e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03513ddd0ecb5609bc31c5c091acd9ea713910ed9b86a77f8d0b0dab1d74ca0b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__211f9d785f9aa932390b4387a36468593141a00aad0fa66cfb3d57af0924d14d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1953eff083f69f2a10a608c97b42ac6296d3325935b824dc461953b1918a833(
    value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnFaq.S3PathProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d433f4df733fa6a1fa7dc2230f5a7552d9b05a432e85192ee89856dfb12f747e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c37eea23978725a4ed038d3aba9ef50585677c733a7b2ff767c0f0381f51e6ac(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce5c3602f1c0097d46c431e26f3ccb335cf40ac53cd2cd7dbbec06b27d14fbba(
    *,
    bucket: builtins.str,
    key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6d3c7f7d6a70914370ad158a0f4367ddb09e670825d70ff465c1fa85f619bdc(
    *,
    index_id: builtins.str,
    name: builtins.str,
    role_arn: builtins.str,
    s3_path: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnFaq.S3PathProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    file_format: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f4962c86ecad8a21588a24f555167043116fa4bb101c3e374054a59f8552e87(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    edition: builtins.str,
    name: builtins.str,
    role_arn: builtins.str,
    capacity_units: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnIndex.CapacityUnitsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    document_metadata_configurations: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnIndex.DocumentMetadataConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    server_side_encryption_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnIndex.ServerSideEncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    user_context_policy: typing.Optional[builtins.str] = None,
    user_token_configurations: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnIndex.UserTokenConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8307c178571fcb836fa428a0f18d2a11638105c4e43c75e89e75cbd5d1f3e31d(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdf89fa9fa5b0045e5254f7f6dbb50be440d1ca20e0e23b215bdad8d7d17e05a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13bb66f77820d14599141ade0c8ac1ed9cafeeab163afffe66a709e4df4550a2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2893d2822c0f680e3ae3f99d4c31afbce2d7274afaf4332248a4733750015144(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08297ad63e24b8901a60dd7d4cd79d46368e2be02b01c3e28c91e2c0e7a2e813(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e0fbf2786717286c0e825002d1faa0d35387f64116f65de75d2e2872ab387f3(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnIndex.CapacityUnitsConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea856d03293bc15138c4bbc924441cc7bb9ab65452b4d8fa8058b8f93b89de48(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ddc766b6df5028f55eda513046f17b3f975c0c833b9e458fe16cad3de399dcf(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnIndex.DocumentMetadataConfigurationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9ba173dd7347d90c8f598d8684ca1655ca953353c1e475c81356104764fad29(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnIndex.ServerSideEncryptionConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fed85dd48f35ea19282b64a9770efe37cb91d1992560303b83600e4cff3e79f2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef1f1011ab1e1a36293803fb70f47a05c4e46c1e09883ce65cd4796a49895f7e(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnIndex.UserTokenConfigurationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a03e13b957bf6ef2b230204c5639848e1bc7eb4b5d53880d439189d604c381f7(
    *,
    query_capacity_units: jsii.Number,
    storage_capacity_units: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69f22718a5ee54e2b50c78012eaf2e3f5a886c02b96fdbe9e3dd731d895a48b2(
    *,
    name: builtins.str,
    type: builtins.str,
    relevance: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnIndex.RelevanceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    search: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnIndex.SearchProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ceaab6e00a0352a748cd403853e892d781af46e109a602808ca7a99324c5cec4(
    *,
    group_attribute_field: builtins.str,
    user_name_attribute_field: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__462c201496ce236f051289ec80cdd046522a03f66a2c470cb4a101d73e492ced(
    *,
    key_location: builtins.str,
    claim_regex: typing.Optional[builtins.str] = None,
    group_attribute_field: typing.Optional[builtins.str] = None,
    issuer: typing.Optional[builtins.str] = None,
    secret_manager_arn: typing.Optional[builtins.str] = None,
    url: typing.Optional[builtins.str] = None,
    user_name_attribute_field: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acec0091ac009b19879d61ea8e788654c5f97d5f6018ca72bc4d747a0365301f(
    *,
    duration: typing.Optional[builtins.str] = None,
    freshness: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    importance: typing.Optional[jsii.Number] = None,
    rank_order: typing.Optional[builtins.str] = None,
    value_importance_items: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnIndex.ValueImportanceItemProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__883e6e9b7a8a239400069c1c9950b5dec0955c6fbb1e5947a3175f04cdbc97ed(
    *,
    displayable: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    facetable: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    searchable: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    sortable: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e5a98bd425157d628f45c27a930a0585c6f2dbed6bad09a3e7caf1f0c7e28d2(
    *,
    kms_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10e3c7d841fa5151ce3a475a71a03fb223fa658d35349028884c28a978779d82(
    *,
    json_token_type_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnIndex.JsonTokenTypeConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    jwt_token_type_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnIndex.JwtTokenTypeConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d191222e08c46f38378cc54be628016d4d18f0f83980ab0cf91a693e97aa543f(
    *,
    key: typing.Optional[builtins.str] = None,
    value: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0707733901472b304f7c64d21a4b0c7cbacffd0ac000c953baf3c1430ee877a0(
    *,
    edition: builtins.str,
    name: builtins.str,
    role_arn: builtins.str,
    capacity_units: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnIndex.CapacityUnitsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    document_metadata_configurations: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnIndex.DocumentMetadataConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    server_side_encryption_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnIndex.ServerSideEncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    user_context_policy: typing.Optional[builtins.str] = None,
    user_token_configurations: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnIndex.UserTokenConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

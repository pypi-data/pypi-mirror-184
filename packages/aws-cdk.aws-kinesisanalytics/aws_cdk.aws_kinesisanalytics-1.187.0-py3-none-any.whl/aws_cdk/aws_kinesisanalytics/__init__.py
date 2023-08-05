'''
# Amazon Kinesis Data Analytics Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_kinesisanalytics as kinesisanalytics
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for KinesisAnalytics construct libraries](https://constructs.dev/search?q=kinesisanalytics)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::KinesisAnalytics resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_KinesisAnalytics.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::KinesisAnalytics](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_KinesisAnalytics.html).

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
class CfnApplication(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplication",
):
    '''A CloudFormation ``AWS::KinesisAnalytics::Application``.

    The ``AWS::KinesisAnalytics::Application`` resource creates an Amazon Kinesis Data Analytics application. For more information, see the `Amazon Kinesis Data Analytics Developer Guide <https://docs.aws.amazon.com//kinesisanalytics/latest/dev/what-is.html>`_ .

    :cloudformationResource: AWS::KinesisAnalytics::Application
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-application.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_kinesisanalytics as kinesisanalytics
        
        cfn_application = kinesisanalytics.CfnApplication(self, "MyCfnApplication",
            inputs=[kinesisanalytics.CfnApplication.InputProperty(
                input_schema=kinesisanalytics.CfnApplication.InputSchemaProperty(
                    record_columns=[kinesisanalytics.CfnApplication.RecordColumnProperty(
                        name="name",
                        sql_type="sqlType",
        
                        # the properties below are optional
                        mapping="mapping"
                    )],
                    record_format=kinesisanalytics.CfnApplication.RecordFormatProperty(
                        record_format_type="recordFormatType",
        
                        # the properties below are optional
                        mapping_parameters=kinesisanalytics.CfnApplication.MappingParametersProperty(
                            csv_mapping_parameters=kinesisanalytics.CfnApplication.CSVMappingParametersProperty(
                                record_column_delimiter="recordColumnDelimiter",
                                record_row_delimiter="recordRowDelimiter"
                            ),
                            json_mapping_parameters=kinesisanalytics.CfnApplication.JSONMappingParametersProperty(
                                record_row_path="recordRowPath"
                            )
                        )
                    ),
        
                    # the properties below are optional
                    record_encoding="recordEncoding"
                ),
                name_prefix="namePrefix",
        
                # the properties below are optional
                input_parallelism=kinesisanalytics.CfnApplication.InputParallelismProperty(
                    count=123
                ),
                input_processing_configuration=kinesisanalytics.CfnApplication.InputProcessingConfigurationProperty(
                    input_lambda_processor=kinesisanalytics.CfnApplication.InputLambdaProcessorProperty(
                        resource_arn="resourceArn",
                        role_arn="roleArn"
                    )
                ),
                kinesis_firehose_input=kinesisanalytics.CfnApplication.KinesisFirehoseInputProperty(
                    resource_arn="resourceArn",
                    role_arn="roleArn"
                ),
                kinesis_streams_input=kinesisanalytics.CfnApplication.KinesisStreamsInputProperty(
                    resource_arn="resourceArn",
                    role_arn="roleArn"
                )
            )],
        
            # the properties below are optional
            application_code="applicationCode",
            application_description="applicationDescription",
            application_name="applicationName"
        )
    '''

    def __init__(
        self,
        scope: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        inputs: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[typing.Union["CfnApplication.InputProperty", typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable]]],
        application_code: typing.Optional[builtins.str] = None,
        application_description: typing.Optional[builtins.str] = None,
        application_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::KinesisAnalytics::Application``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param inputs: Use this parameter to configure the application input. You can configure your application to receive input from a single streaming source. In this configuration, you map this streaming source to an in-application stream that is created. Your application code can then query the in-application stream like a table (you can think of it as a constantly updating table). For the streaming source, you provide its Amazon Resource Name (ARN) and format of data on the stream (for example, JSON, CSV, etc.). You also must provide an IAM role that Amazon Kinesis Analytics can assume to read this stream on your behalf. To create the in-application stream, you need to specify a schema to transform your data into a schematized version used in SQL. In the schema, you provide the necessary mapping of the data elements in the streaming source to record columns in the in-app stream.
        :param application_code: One or more SQL statements that read input data, transform it, and generate output. For example, you can write a SQL statement that reads data from one in-application stream, generates a running average of the number of advertisement clicks by vendor, and insert resulting rows in another in-application stream using pumps. For more information about the typical pattern, see `Application Code <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-app-code.html>`_ . You can provide such series of SQL statements, where output of one statement can be used as the input for the next statement. You store intermediate results by creating in-application streams and pumps. Note that the application code must create the streams with names specified in the ``Outputs`` . For example, if your ``Outputs`` defines output streams named ``ExampleOutputStream1`` and ``ExampleOutputStream2`` , then your application code must create these streams.
        :param application_description: Summary description of the application.
        :param application_name: Name of your Amazon Kinesis Analytics application (for example, ``sample-app`` ).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32b2db479ff8f4ba54c3123098b7a543a37fe947f8f5f4b0b22c95d87a5a8740)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApplicationProps(
            inputs=inputs,
            application_code=application_code,
            application_description=application_description,
            application_name=application_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf74750202e5145822e6a4dca5cc71c2d6ef1b3f369c92b0efaba7f825ea508d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__629352554e0b4ad1cd72d357cee75145e61011fa4d3ba6f231cbd04963737c9c)
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
    @jsii.member(jsii_name="inputs")
    def inputs(
        self,
    ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union["CfnApplication.InputProperty", _aws_cdk_core_f4b25747.IResolvable]]]:
        '''Use this parameter to configure the application input.

        You can configure your application to receive input from a single streaming source. In this configuration, you map this streaming source to an in-application stream that is created. Your application code can then query the in-application stream like a table (you can think of it as a constantly updating table).

        For the streaming source, you provide its Amazon Resource Name (ARN) and format of data on the stream (for example, JSON, CSV, etc.). You also must provide an IAM role that Amazon Kinesis Analytics can assume to read this stream on your behalf.

        To create the in-application stream, you need to specify a schema to transform your data into a schematized version used in SQL. In the schema, you provide the necessary mapping of the data elements in the streaming source to record columns in the in-app stream.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-application.html#cfn-kinesisanalytics-application-inputs
        '''
        return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union["CfnApplication.InputProperty", _aws_cdk_core_f4b25747.IResolvable]]], jsii.get(self, "inputs"))

    @inputs.setter
    def inputs(
        self,
        value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union["CfnApplication.InputProperty", _aws_cdk_core_f4b25747.IResolvable]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d80027fd700f25d7baa2fbc8e741e19f97183215c89b5e1b89612e8dee4c296f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inputs", value)

    @builtins.property
    @jsii.member(jsii_name="applicationCode")
    def application_code(self) -> typing.Optional[builtins.str]:
        '''One or more SQL statements that read input data, transform it, and generate output.

        For example, you can write a SQL statement that reads data from one in-application stream, generates a running average of the number of advertisement clicks by vendor, and insert resulting rows in another in-application stream using pumps. For more information about the typical pattern, see `Application Code <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-app-code.html>`_ .

        You can provide such series of SQL statements, where output of one statement can be used as the input for the next statement. You store intermediate results by creating in-application streams and pumps.

        Note that the application code must create the streams with names specified in the ``Outputs`` . For example, if your ``Outputs`` defines output streams named ``ExampleOutputStream1`` and ``ExampleOutputStream2`` , then your application code must create these streams.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-application.html#cfn-kinesisanalytics-application-applicationcode
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationCode"))

    @application_code.setter
    def application_code(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a16a017ea1ebcc0c6a4c3bb5adfcaa90d0472f728a593cfdbecb8ef9c5bde14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationCode", value)

    @builtins.property
    @jsii.member(jsii_name="applicationDescription")
    def application_description(self) -> typing.Optional[builtins.str]:
        '''Summary description of the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-application.html#cfn-kinesisanalytics-application-applicationdescription
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationDescription"))

    @application_description.setter
    def application_description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50745cd224885ded2718f0e25dd767d80309310eb69d93f96547a714cda10954)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationDescription", value)

    @builtins.property
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> typing.Optional[builtins.str]:
        '''Name of your Amazon Kinesis Analytics application (for example, ``sample-app`` ).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-application.html#cfn-kinesisanalytics-application-applicationname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationName"))

    @application_name.setter
    def application_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea4f2ecb41cadbc4bf511976fe42ebff8c97e03842733b3ee5f19e72a70a5f5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationName", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplication.CSVMappingParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "record_column_delimiter": "recordColumnDelimiter",
            "record_row_delimiter": "recordRowDelimiter",
        },
    )
    class CSVMappingParametersProperty:
        def __init__(
            self,
            *,
            record_column_delimiter: builtins.str,
            record_row_delimiter: builtins.str,
        ) -> None:
            '''Provides additional mapping information when the record format uses delimiters, such as CSV.

            For example, the following sample records use CSV format, where the records use the *'\\n'* as the row delimiter and a comma (",") as the column delimiter:

            ``"name1", "address1"``

            ``"name2", "address2"``

            :param record_column_delimiter: Column delimiter. For example, in a CSV format, a comma (",") is the typical column delimiter.
            :param record_row_delimiter: Row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-csvmappingparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                c_sVMapping_parameters_property = kinesisanalytics.CfnApplication.CSVMappingParametersProperty(
                    record_column_delimiter="recordColumnDelimiter",
                    record_row_delimiter="recordRowDelimiter"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9d6e953229adebd993016e0224131ee9512a01531f068b0cecfbc8bf612c1be5)
                check_type(argname="argument record_column_delimiter", value=record_column_delimiter, expected_type=type_hints["record_column_delimiter"])
                check_type(argname="argument record_row_delimiter", value=record_row_delimiter, expected_type=type_hints["record_row_delimiter"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "record_column_delimiter": record_column_delimiter,
                "record_row_delimiter": record_row_delimiter,
            }

        @builtins.property
        def record_column_delimiter(self) -> builtins.str:
            '''Column delimiter.

            For example, in a CSV format, a comma (",") is the typical column delimiter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-csvmappingparameters.html#cfn-kinesisanalytics-application-csvmappingparameters-recordcolumndelimiter
            '''
            result = self._values.get("record_column_delimiter")
            assert result is not None, "Required property 'record_column_delimiter' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def record_row_delimiter(self) -> builtins.str:
            '''Row delimiter.

            For example, in a CSV format, *'\\n'* is the typical row delimiter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-csvmappingparameters.html#cfn-kinesisanalytics-application-csvmappingparameters-recordrowdelimiter
            '''
            result = self._values.get("record_row_delimiter")
            assert result is not None, "Required property 'record_row_delimiter' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CSVMappingParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplication.InputLambdaProcessorProperty",
        jsii_struct_bases=[],
        name_mapping={"resource_arn": "resourceArn", "role_arn": "roleArn"},
    )
    class InputLambdaProcessorProperty:
        def __init__(
            self,
            *,
            resource_arn: builtins.str,
            role_arn: builtins.str,
        ) -> None:
            '''An object that contains the Amazon Resource Name (ARN) of the `AWS Lambda <https://docs.aws.amazon.com/lambda/>`_ function that is used to preprocess records in the stream, and the ARN of the IAM role that is used to access the AWS Lambda function.

            :param resource_arn: The ARN of the `AWS Lambda <https://docs.aws.amazon.com/lambda/>`_ function that operates on records in the stream. .. epigraph:: To specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see `Example ARNs: AWS Lambda <https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`_
            :param role_arn: The ARN of the IAM role that is used to access the AWS Lambda function.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputlambdaprocessor.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                input_lambda_processor_property = kinesisanalytics.CfnApplication.InputLambdaProcessorProperty(
                    resource_arn="resourceArn",
                    role_arn="roleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c6ee71d0e66f57a3eded5ebba8cdd3807d5cbff01049d07b2658efa0d8729aca)
                check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "resource_arn": resource_arn,
                "role_arn": role_arn,
            }

        @builtins.property
        def resource_arn(self) -> builtins.str:
            '''The ARN of the `AWS Lambda <https://docs.aws.amazon.com/lambda/>`_ function that operates on records in the stream.

            .. epigraph::

               To specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see `Example ARNs: AWS Lambda <https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`_

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputlambdaprocessor.html#cfn-kinesisanalytics-application-inputlambdaprocessor-resourcearn
            '''
            result = self._values.get("resource_arn")
            assert result is not None, "Required property 'resource_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the IAM role that is used to access the AWS Lambda function.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputlambdaprocessor.html#cfn-kinesisanalytics-application-inputlambdaprocessor-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputLambdaProcessorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplication.InputParallelismProperty",
        jsii_struct_bases=[],
        name_mapping={"count": "count"},
    )
    class InputParallelismProperty:
        def __init__(self, *, count: typing.Optional[jsii.Number] = None) -> None:
            '''Describes the number of in-application streams to create for a given streaming source.

            For information about parallelism, see `Configuring Application Input <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html>`_ .

            :param count: Number of in-application streams to create. For more information, see `Limits <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/limits.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputparallelism.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                input_parallelism_property = kinesisanalytics.CfnApplication.InputParallelismProperty(
                    count=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6d541b02d706686f3932fc9d2500b71d2264b7fc437925e98aa63a0531db99e1)
                check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if count is not None:
                self._values["count"] = count

        @builtins.property
        def count(self) -> typing.Optional[jsii.Number]:
            '''Number of in-application streams to create.

            For more information, see `Limits <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/limits.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputparallelism.html#cfn-kinesisanalytics-application-inputparallelism-count
            '''
            result = self._values.get("count")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputParallelismProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplication.InputProcessingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"input_lambda_processor": "inputLambdaProcessor"},
    )
    class InputProcessingConfigurationProperty:
        def __init__(
            self,
            *,
            input_lambda_processor: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplication.InputLambdaProcessorProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Provides a description of a processor that is used to preprocess the records in the stream before being processed by your application code.

            Currently, the only input processor available is `AWS Lambda <https://docs.aws.amazon.com/lambda/>`_ .

            :param input_lambda_processor: The `InputLambdaProcessor <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputlambdaprocessor.html>`_ that is used to preprocess the records in the stream before being processed by your application code.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputprocessingconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                input_processing_configuration_property = kinesisanalytics.CfnApplication.InputProcessingConfigurationProperty(
                    input_lambda_processor=kinesisanalytics.CfnApplication.InputLambdaProcessorProperty(
                        resource_arn="resourceArn",
                        role_arn="roleArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0c3bad6a40a5c81cc6104f50ced259d580601f457ed84cb097df149c39efa61c)
                check_type(argname="argument input_lambda_processor", value=input_lambda_processor, expected_type=type_hints["input_lambda_processor"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if input_lambda_processor is not None:
                self._values["input_lambda_processor"] = input_lambda_processor

        @builtins.property
        def input_lambda_processor(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplication.InputLambdaProcessorProperty"]]:
            '''The `InputLambdaProcessor <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputlambdaprocessor.html>`_ that is used to preprocess the records in the stream before being processed by your application code.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputprocessingconfiguration.html#cfn-kinesisanalytics-application-inputprocessingconfiguration-inputlambdaprocessor
            '''
            result = self._values.get("input_lambda_processor")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplication.InputLambdaProcessorProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputProcessingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplication.InputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "input_schema": "inputSchema",
            "name_prefix": "namePrefix",
            "input_parallelism": "inputParallelism",
            "input_processing_configuration": "inputProcessingConfiguration",
            "kinesis_firehose_input": "kinesisFirehoseInput",
            "kinesis_streams_input": "kinesisStreamsInput",
        },
    )
    class InputProperty:
        def __init__(
            self,
            *,
            input_schema: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplication.InputSchemaProperty", typing.Dict[builtins.str, typing.Any]]],
            name_prefix: builtins.str,
            input_parallelism: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplication.InputParallelismProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            input_processing_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplication.InputProcessingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            kinesis_firehose_input: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplication.KinesisFirehoseInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            kinesis_streams_input: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplication.KinesisStreamsInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''When you configure the application input, you specify the streaming source, the in-application stream name that is created, and the mapping between the two.

            For more information, see `Configuring Application Input <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html>`_ .

            :param input_schema: Describes the format of the data in the streaming source, and how each data element maps to corresponding columns in the in-application stream that is being created. Also used to describe the format of the reference data source.
            :param name_prefix: Name prefix to use when creating an in-application stream. Suppose that you specify a prefix "MyInApplicationStream." Amazon Kinesis Analytics then creates one or more (as per the ``InputParallelism`` count you specified) in-application streams with names "MyInApplicationStream_001," "MyInApplicationStream_002," and so on.
            :param input_parallelism: Describes the number of in-application streams to create. Data from your source is routed to these in-application input streams. See `Configuring Application Input <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html>`_ .
            :param input_processing_configuration: The `InputProcessingConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputprocessingconfiguration.html>`_ for the input. An input processor transforms records as they are received from the stream, before the application's SQL code executes. Currently, the only input processing configuration available is `InputLambdaProcessor <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputlambdaprocessor.html>`_ .
            :param kinesis_firehose_input: If the streaming source is an Amazon Kinesis Firehose delivery stream, identifies the delivery stream's ARN and an IAM role that enables Amazon Kinesis Analytics to access the stream on your behalf. Note: Either ``KinesisStreamsInput`` or ``KinesisFirehoseInput`` is required.
            :param kinesis_streams_input: If the streaming source is an Amazon Kinesis stream, identifies the stream's Amazon Resource Name (ARN) and an IAM role that enables Amazon Kinesis Analytics to access the stream on your behalf. Note: Either ``KinesisStreamsInput`` or ``KinesisFirehoseInput`` is required.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-input.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                input_property = kinesisanalytics.CfnApplication.InputProperty(
                    input_schema=kinesisanalytics.CfnApplication.InputSchemaProperty(
                        record_columns=[kinesisanalytics.CfnApplication.RecordColumnProperty(
                            name="name",
                            sql_type="sqlType",
                
                            # the properties below are optional
                            mapping="mapping"
                        )],
                        record_format=kinesisanalytics.CfnApplication.RecordFormatProperty(
                            record_format_type="recordFormatType",
                
                            # the properties below are optional
                            mapping_parameters=kinesisanalytics.CfnApplication.MappingParametersProperty(
                                csv_mapping_parameters=kinesisanalytics.CfnApplication.CSVMappingParametersProperty(
                                    record_column_delimiter="recordColumnDelimiter",
                                    record_row_delimiter="recordRowDelimiter"
                                ),
                                json_mapping_parameters=kinesisanalytics.CfnApplication.JSONMappingParametersProperty(
                                    record_row_path="recordRowPath"
                                )
                            )
                        ),
                
                        # the properties below are optional
                        record_encoding="recordEncoding"
                    ),
                    name_prefix="namePrefix",
                
                    # the properties below are optional
                    input_parallelism=kinesisanalytics.CfnApplication.InputParallelismProperty(
                        count=123
                    ),
                    input_processing_configuration=kinesisanalytics.CfnApplication.InputProcessingConfigurationProperty(
                        input_lambda_processor=kinesisanalytics.CfnApplication.InputLambdaProcessorProperty(
                            resource_arn="resourceArn",
                            role_arn="roleArn"
                        )
                    ),
                    kinesis_firehose_input=kinesisanalytics.CfnApplication.KinesisFirehoseInputProperty(
                        resource_arn="resourceArn",
                        role_arn="roleArn"
                    ),
                    kinesis_streams_input=kinesisanalytics.CfnApplication.KinesisStreamsInputProperty(
                        resource_arn="resourceArn",
                        role_arn="roleArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bda17ed8f8889f8c5c6ec56853049a882846d7dcd4f388d5a61d76bb67a4062e)
                check_type(argname="argument input_schema", value=input_schema, expected_type=type_hints["input_schema"])
                check_type(argname="argument name_prefix", value=name_prefix, expected_type=type_hints["name_prefix"])
                check_type(argname="argument input_parallelism", value=input_parallelism, expected_type=type_hints["input_parallelism"])
                check_type(argname="argument input_processing_configuration", value=input_processing_configuration, expected_type=type_hints["input_processing_configuration"])
                check_type(argname="argument kinesis_firehose_input", value=kinesis_firehose_input, expected_type=type_hints["kinesis_firehose_input"])
                check_type(argname="argument kinesis_streams_input", value=kinesis_streams_input, expected_type=type_hints["kinesis_streams_input"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "input_schema": input_schema,
                "name_prefix": name_prefix,
            }
            if input_parallelism is not None:
                self._values["input_parallelism"] = input_parallelism
            if input_processing_configuration is not None:
                self._values["input_processing_configuration"] = input_processing_configuration
            if kinesis_firehose_input is not None:
                self._values["kinesis_firehose_input"] = kinesis_firehose_input
            if kinesis_streams_input is not None:
                self._values["kinesis_streams_input"] = kinesis_streams_input

        @builtins.property
        def input_schema(
            self,
        ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplication.InputSchemaProperty"]:
            '''Describes the format of the data in the streaming source, and how each data element maps to corresponding columns in the in-application stream that is being created.

            Also used to describe the format of the reference data source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-input.html#cfn-kinesisanalytics-application-input-inputschema
            '''
            result = self._values.get("input_schema")
            assert result is not None, "Required property 'input_schema' is missing"
            return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplication.InputSchemaProperty"], result)

        @builtins.property
        def name_prefix(self) -> builtins.str:
            '''Name prefix to use when creating an in-application stream.

            Suppose that you specify a prefix "MyInApplicationStream." Amazon Kinesis Analytics then creates one or more (as per the ``InputParallelism`` count you specified) in-application streams with names "MyInApplicationStream_001," "MyInApplicationStream_002," and so on.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-input.html#cfn-kinesisanalytics-application-input-nameprefix
            '''
            result = self._values.get("name_prefix")
            assert result is not None, "Required property 'name_prefix' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def input_parallelism(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplication.InputParallelismProperty"]]:
            '''Describes the number of in-application streams to create.

            Data from your source is routed to these in-application input streams.

            See `Configuring Application Input <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-input.html#cfn-kinesisanalytics-application-input-inputparallelism
            '''
            result = self._values.get("input_parallelism")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplication.InputParallelismProperty"]], result)

        @builtins.property
        def input_processing_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplication.InputProcessingConfigurationProperty"]]:
            '''The `InputProcessingConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputprocessingconfiguration.html>`_ for the input. An input processor transforms records as they are received from the stream, before the application's SQL code executes. Currently, the only input processing configuration available is `InputLambdaProcessor <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputlambdaprocessor.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-input.html#cfn-kinesisanalytics-application-input-inputprocessingconfiguration
            '''
            result = self._values.get("input_processing_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplication.InputProcessingConfigurationProperty"]], result)

        @builtins.property
        def kinesis_firehose_input(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplication.KinesisFirehoseInputProperty"]]:
            '''If the streaming source is an Amazon Kinesis Firehose delivery stream, identifies the delivery stream's ARN and an IAM role that enables Amazon Kinesis Analytics to access the stream on your behalf.

            Note: Either ``KinesisStreamsInput`` or ``KinesisFirehoseInput`` is required.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-input.html#cfn-kinesisanalytics-application-input-kinesisfirehoseinput
            '''
            result = self._values.get("kinesis_firehose_input")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplication.KinesisFirehoseInputProperty"]], result)

        @builtins.property
        def kinesis_streams_input(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplication.KinesisStreamsInputProperty"]]:
            '''If the streaming source is an Amazon Kinesis stream, identifies the stream's Amazon Resource Name (ARN) and an IAM role that enables Amazon Kinesis Analytics to access the stream on your behalf.

            Note: Either ``KinesisStreamsInput`` or ``KinesisFirehoseInput`` is required.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-input.html#cfn-kinesisanalytics-application-input-kinesisstreamsinput
            '''
            result = self._values.get("kinesis_streams_input")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplication.KinesisStreamsInputProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplication.InputSchemaProperty",
        jsii_struct_bases=[],
        name_mapping={
            "record_columns": "recordColumns",
            "record_format": "recordFormat",
            "record_encoding": "recordEncoding",
        },
    )
    class InputSchemaProperty:
        def __init__(
            self,
            *,
            record_columns: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplication.RecordColumnProperty", typing.Dict[builtins.str, typing.Any]]]]],
            record_format: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplication.RecordFormatProperty", typing.Dict[builtins.str, typing.Any]]],
            record_encoding: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes the format of the data in the streaming source, and how each data element maps to corresponding columns in the in-application stream that is being created.

            Also used to describe the format of the reference data source.

            :param record_columns: A list of ``RecordColumn`` objects.
            :param record_format: Specifies the format of the records on the streaming source.
            :param record_encoding: Specifies the encoding of the records in the streaming source. For example, UTF-8.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputschema.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                input_schema_property = kinesisanalytics.CfnApplication.InputSchemaProperty(
                    record_columns=[kinesisanalytics.CfnApplication.RecordColumnProperty(
                        name="name",
                        sql_type="sqlType",
                
                        # the properties below are optional
                        mapping="mapping"
                    )],
                    record_format=kinesisanalytics.CfnApplication.RecordFormatProperty(
                        record_format_type="recordFormatType",
                
                        # the properties below are optional
                        mapping_parameters=kinesisanalytics.CfnApplication.MappingParametersProperty(
                            csv_mapping_parameters=kinesisanalytics.CfnApplication.CSVMappingParametersProperty(
                                record_column_delimiter="recordColumnDelimiter",
                                record_row_delimiter="recordRowDelimiter"
                            ),
                            json_mapping_parameters=kinesisanalytics.CfnApplication.JSONMappingParametersProperty(
                                record_row_path="recordRowPath"
                            )
                        )
                    ),
                
                    # the properties below are optional
                    record_encoding="recordEncoding"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fd2da19040f32bac6b97add291b5e9aa3a4820f542f0ab1f762c126e1fee2a72)
                check_type(argname="argument record_columns", value=record_columns, expected_type=type_hints["record_columns"])
                check_type(argname="argument record_format", value=record_format, expected_type=type_hints["record_format"])
                check_type(argname="argument record_encoding", value=record_encoding, expected_type=type_hints["record_encoding"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "record_columns": record_columns,
                "record_format": record_format,
            }
            if record_encoding is not None:
                self._values["record_encoding"] = record_encoding

        @builtins.property
        def record_columns(
            self,
        ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplication.RecordColumnProperty"]]]:
            '''A list of ``RecordColumn`` objects.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputschema.html#cfn-kinesisanalytics-application-inputschema-recordcolumns
            '''
            result = self._values.get("record_columns")
            assert result is not None, "Required property 'record_columns' is missing"
            return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplication.RecordColumnProperty"]]], result)

        @builtins.property
        def record_format(
            self,
        ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplication.RecordFormatProperty"]:
            '''Specifies the format of the records on the streaming source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputschema.html#cfn-kinesisanalytics-application-inputschema-recordformat
            '''
            result = self._values.get("record_format")
            assert result is not None, "Required property 'record_format' is missing"
            return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplication.RecordFormatProperty"], result)

        @builtins.property
        def record_encoding(self) -> typing.Optional[builtins.str]:
            '''Specifies the encoding of the records in the streaming source.

            For example, UTF-8.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputschema.html#cfn-kinesisanalytics-application-inputschema-recordencoding
            '''
            result = self._values.get("record_encoding")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputSchemaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplication.JSONMappingParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"record_row_path": "recordRowPath"},
    )
    class JSONMappingParametersProperty:
        def __init__(self, *, record_row_path: builtins.str) -> None:
            '''Provides additional mapping information when JSON is the record format on the streaming source.

            :param record_row_path: Path to the top-level parent that contains the records.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-jsonmappingparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                j_sONMapping_parameters_property = kinesisanalytics.CfnApplication.JSONMappingParametersProperty(
                    record_row_path="recordRowPath"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d166bde9431c4d007eb62ac8076c3b29ac6c26bd12d100bc0664f16a07741770)
                check_type(argname="argument record_row_path", value=record_row_path, expected_type=type_hints["record_row_path"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "record_row_path": record_row_path,
            }

        @builtins.property
        def record_row_path(self) -> builtins.str:
            '''Path to the top-level parent that contains the records.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-jsonmappingparameters.html#cfn-kinesisanalytics-application-jsonmappingparameters-recordrowpath
            '''
            result = self._values.get("record_row_path")
            assert result is not None, "Required property 'record_row_path' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JSONMappingParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplication.KinesisFirehoseInputProperty",
        jsii_struct_bases=[],
        name_mapping={"resource_arn": "resourceArn", "role_arn": "roleArn"},
    )
    class KinesisFirehoseInputProperty:
        def __init__(
            self,
            *,
            resource_arn: builtins.str,
            role_arn: builtins.str,
        ) -> None:
            '''Identifies an Amazon Kinesis Firehose delivery stream as the streaming source.

            You provide the delivery stream's Amazon Resource Name (ARN) and an IAM role ARN that enables Amazon Kinesis Analytics to access the stream on your behalf.

            :param resource_arn: ARN of the input delivery stream.
            :param role_arn: ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your behalf. You need to make sure that the role has the necessary permissions to access the stream.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-kinesisfirehoseinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                kinesis_firehose_input_property = kinesisanalytics.CfnApplication.KinesisFirehoseInputProperty(
                    resource_arn="resourceArn",
                    role_arn="roleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d104bb127b0f03f200db1dbbaec46e3975c27787da6c5b5267a6827ce0b4171a)
                check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "resource_arn": resource_arn,
                "role_arn": role_arn,
            }

        @builtins.property
        def resource_arn(self) -> builtins.str:
            '''ARN of the input delivery stream.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-kinesisfirehoseinput.html#cfn-kinesisanalytics-application-kinesisfirehoseinput-resourcearn
            '''
            result = self._values.get("resource_arn")
            assert result is not None, "Required property 'resource_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your behalf.

            You need to make sure that the role has the necessary permissions to access the stream.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-kinesisfirehoseinput.html#cfn-kinesisanalytics-application-kinesisfirehoseinput-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisFirehoseInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplication.KinesisStreamsInputProperty",
        jsii_struct_bases=[],
        name_mapping={"resource_arn": "resourceArn", "role_arn": "roleArn"},
    )
    class KinesisStreamsInputProperty:
        def __init__(
            self,
            *,
            resource_arn: builtins.str,
            role_arn: builtins.str,
        ) -> None:
            '''Identifies an Amazon Kinesis stream as the streaming source.

            You provide the stream's Amazon Resource Name (ARN) and an IAM role ARN that enables Amazon Kinesis Analytics to access the stream on your behalf.

            :param resource_arn: ARN of the input Amazon Kinesis stream to read.
            :param role_arn: ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your behalf. You need to grant the necessary permissions to this role.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-kinesisstreamsinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                kinesis_streams_input_property = kinesisanalytics.CfnApplication.KinesisStreamsInputProperty(
                    resource_arn="resourceArn",
                    role_arn="roleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__36461ab81a12ff5e6237be1b93ce731867343ce8aa41246829064d95f4c4797d)
                check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "resource_arn": resource_arn,
                "role_arn": role_arn,
            }

        @builtins.property
        def resource_arn(self) -> builtins.str:
            '''ARN of the input Amazon Kinesis stream to read.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-kinesisstreamsinput.html#cfn-kinesisanalytics-application-kinesisstreamsinput-resourcearn
            '''
            result = self._values.get("resource_arn")
            assert result is not None, "Required property 'resource_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''ARN of the IAM role that Amazon Kinesis Analytics can assume to access the stream on your behalf.

            You need to grant the necessary permissions to this role.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-kinesisstreamsinput.html#cfn-kinesisanalytics-application-kinesisstreamsinput-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisStreamsInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplication.MappingParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "csv_mapping_parameters": "csvMappingParameters",
            "json_mapping_parameters": "jsonMappingParameters",
        },
    )
    class MappingParametersProperty:
        def __init__(
            self,
            *,
            csv_mapping_parameters: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplication.CSVMappingParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            json_mapping_parameters: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplication.JSONMappingParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''When configuring application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

            :param csv_mapping_parameters: Provides additional mapping information when the record format uses delimiters (for example, CSV).
            :param json_mapping_parameters: Provides additional mapping information when JSON is the record format on the streaming source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-mappingparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                mapping_parameters_property = kinesisanalytics.CfnApplication.MappingParametersProperty(
                    csv_mapping_parameters=kinesisanalytics.CfnApplication.CSVMappingParametersProperty(
                        record_column_delimiter="recordColumnDelimiter",
                        record_row_delimiter="recordRowDelimiter"
                    ),
                    json_mapping_parameters=kinesisanalytics.CfnApplication.JSONMappingParametersProperty(
                        record_row_path="recordRowPath"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__02778d83ebd86d283335f90e321ab7c8f68ab8ec791bddee47d1f30fcb001f2b)
                check_type(argname="argument csv_mapping_parameters", value=csv_mapping_parameters, expected_type=type_hints["csv_mapping_parameters"])
                check_type(argname="argument json_mapping_parameters", value=json_mapping_parameters, expected_type=type_hints["json_mapping_parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if csv_mapping_parameters is not None:
                self._values["csv_mapping_parameters"] = csv_mapping_parameters
            if json_mapping_parameters is not None:
                self._values["json_mapping_parameters"] = json_mapping_parameters

        @builtins.property
        def csv_mapping_parameters(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplication.CSVMappingParametersProperty"]]:
            '''Provides additional mapping information when the record format uses delimiters (for example, CSV).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-mappingparameters.html#cfn-kinesisanalytics-application-mappingparameters-csvmappingparameters
            '''
            result = self._values.get("csv_mapping_parameters")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplication.CSVMappingParametersProperty"]], result)

        @builtins.property
        def json_mapping_parameters(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplication.JSONMappingParametersProperty"]]:
            '''Provides additional mapping information when JSON is the record format on the streaming source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-mappingparameters.html#cfn-kinesisanalytics-application-mappingparameters-jsonmappingparameters
            '''
            result = self._values.get("json_mapping_parameters")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplication.JSONMappingParametersProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MappingParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplication.RecordColumnProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "sql_type": "sqlType", "mapping": "mapping"},
    )
    class RecordColumnProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            sql_type: builtins.str,
            mapping: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.

            Also used to describe the format of the reference data source.

            :param name: Name of the column created in the in-application input stream or reference table.
            :param sql_type: Type of column created in the in-application input stream or reference table.
            :param mapping: Reference to the data element in the streaming input or the reference data source. This element is required if the `RecordFormatType <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_RecordFormat.html#analytics-Type-RecordFormat-RecordFormatTypel>`_ is ``JSON`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-recordcolumn.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                record_column_property = kinesisanalytics.CfnApplication.RecordColumnProperty(
                    name="name",
                    sql_type="sqlType",
                
                    # the properties below are optional
                    mapping="mapping"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__48cc42f79151b8ca76858bf0a39020b67d9e0f090ca7a6cf17135183e7fa8b2e)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument sql_type", value=sql_type, expected_type=type_hints["sql_type"])
                check_type(argname="argument mapping", value=mapping, expected_type=type_hints["mapping"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "sql_type": sql_type,
            }
            if mapping is not None:
                self._values["mapping"] = mapping

        @builtins.property
        def name(self) -> builtins.str:
            '''Name of the column created in the in-application input stream or reference table.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-recordcolumn.html#cfn-kinesisanalytics-application-recordcolumn-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def sql_type(self) -> builtins.str:
            '''Type of column created in the in-application input stream or reference table.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-recordcolumn.html#cfn-kinesisanalytics-application-recordcolumn-sqltype
            '''
            result = self._values.get("sql_type")
            assert result is not None, "Required property 'sql_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def mapping(self) -> typing.Optional[builtins.str]:
            '''Reference to the data element in the streaming input or the reference data source.

            This element is required if the `RecordFormatType <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_RecordFormat.html#analytics-Type-RecordFormat-RecordFormatTypel>`_ is ``JSON`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-recordcolumn.html#cfn-kinesisanalytics-application-recordcolumn-mapping
            '''
            result = self._values.get("mapping")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RecordColumnProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplication.RecordFormatProperty",
        jsii_struct_bases=[],
        name_mapping={
            "record_format_type": "recordFormatType",
            "mapping_parameters": "mappingParameters",
        },
    )
    class RecordFormatProperty:
        def __init__(
            self,
            *,
            record_format_type: builtins.str,
            mapping_parameters: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplication.MappingParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Describes the record format and relevant mapping information that should be applied to schematize the records on the stream.

            :param record_format_type: The type of record format.
            :param mapping_parameters: When configuring application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-recordformat.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                record_format_property = kinesisanalytics.CfnApplication.RecordFormatProperty(
                    record_format_type="recordFormatType",
                
                    # the properties below are optional
                    mapping_parameters=kinesisanalytics.CfnApplication.MappingParametersProperty(
                        csv_mapping_parameters=kinesisanalytics.CfnApplication.CSVMappingParametersProperty(
                            record_column_delimiter="recordColumnDelimiter",
                            record_row_delimiter="recordRowDelimiter"
                        ),
                        json_mapping_parameters=kinesisanalytics.CfnApplication.JSONMappingParametersProperty(
                            record_row_path="recordRowPath"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__61bf56eaeaf82967d3cce8d5f6d80e5688d48dc2a0fa909072e76989592896c7)
                check_type(argname="argument record_format_type", value=record_format_type, expected_type=type_hints["record_format_type"])
                check_type(argname="argument mapping_parameters", value=mapping_parameters, expected_type=type_hints["mapping_parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "record_format_type": record_format_type,
            }
            if mapping_parameters is not None:
                self._values["mapping_parameters"] = mapping_parameters

        @builtins.property
        def record_format_type(self) -> builtins.str:
            '''The type of record format.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-recordformat.html#cfn-kinesisanalytics-application-recordformat-recordformattype
            '''
            result = self._values.get("record_format_type")
            assert result is not None, "Required property 'record_format_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def mapping_parameters(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplication.MappingParametersProperty"]]:
            '''When configuring application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-recordformat.html#cfn-kinesisanalytics-application-recordformat-mappingparameters
            '''
            result = self._values.get("mapping_parameters")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplication.MappingParametersProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RecordFormatProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnApplicationCloudWatchLoggingOptionV2(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationCloudWatchLoggingOptionV2",
):
    '''A CloudFormation ``AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption``.

    Adds an Amazon CloudWatch log stream to monitor application configuration errors.
    .. epigraph::

       Only one *ApplicationCloudWatchLoggingOption* resource can be attached per application.

    :cloudformationResource: AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationcloudwatchloggingoption.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_kinesisanalytics as kinesisanalytics
        
        cfn_application_cloud_watch_logging_option_v2 = kinesisanalytics.CfnApplicationCloudWatchLoggingOptionV2(self, "MyCfnApplicationCloudWatchLoggingOptionV2",
            application_name="applicationName",
            cloud_watch_logging_option=kinesisanalytics.CfnApplicationCloudWatchLoggingOptionV2.CloudWatchLoggingOptionProperty(
                log_stream_arn="logStreamArn"
            )
        )
    '''

    def __init__(
        self,
        scope: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        application_name: builtins.str,
        cloud_watch_logging_option: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationCloudWatchLoggingOptionV2.CloudWatchLoggingOptionProperty", typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Create a new ``AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param application_name: The name of the application.
        :param cloud_watch_logging_option: Provides a description of Amazon CloudWatch logging options, including the log stream Amazon Resource Name (ARN).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77e02c50565dc001014a01a3f112ec517d53d8932d42e6e7d59db3991a10752f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApplicationCloudWatchLoggingOptionV2Props(
            application_name=application_name,
            cloud_watch_logging_option=cloud_watch_logging_option,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42c7b0b917b4d2688ea2bca2a3ef8a6ba2a343bfb65c6e1f22c47dea3b1a496a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0eb6e277e62d9e3fd460706970d0ccfbd75ceac4b6aede3b21bb228ea61ebe2a)
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
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> builtins.str:
        '''The name of the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationcloudwatchloggingoption.html#cfn-kinesisanalyticsv2-applicationcloudwatchloggingoption-applicationname
        '''
        return typing.cast(builtins.str, jsii.get(self, "applicationName"))

    @application_name.setter
    def application_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4de55c4421a87d36217166859de1aeafa9380105be2ba8f307f523c5316c439e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationName", value)

    @builtins.property
    @jsii.member(jsii_name="cloudWatchLoggingOption")
    def cloud_watch_logging_option(
        self,
    ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationCloudWatchLoggingOptionV2.CloudWatchLoggingOptionProperty"]:
        '''Provides a description of Amazon CloudWatch logging options, including the log stream Amazon Resource Name (ARN).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationcloudwatchloggingoption.html#cfn-kinesisanalyticsv2-applicationcloudwatchloggingoption-cloudwatchloggingoption
        '''
        return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationCloudWatchLoggingOptionV2.CloudWatchLoggingOptionProperty"], jsii.get(self, "cloudWatchLoggingOption"))

    @cloud_watch_logging_option.setter
    def cloud_watch_logging_option(
        self,
        value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationCloudWatchLoggingOptionV2.CloudWatchLoggingOptionProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58439338ee062af482eac743ac4b486000ed403b365ffffbc8fc5b37f1015429)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudWatchLoggingOption", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationCloudWatchLoggingOptionV2.CloudWatchLoggingOptionProperty",
        jsii_struct_bases=[],
        name_mapping={"log_stream_arn": "logStreamArn"},
    )
    class CloudWatchLoggingOptionProperty:
        def __init__(self, *, log_stream_arn: builtins.str) -> None:
            '''Provides a description of Amazon CloudWatch logging options, including the log stream Amazon Resource Name (ARN).

            :param log_stream_arn: The ARN of the CloudWatch log to receive application messages.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationcloudwatchloggingoption-cloudwatchloggingoption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                cloud_watch_logging_option_property = kinesisanalytics.CfnApplicationCloudWatchLoggingOptionV2.CloudWatchLoggingOptionProperty(
                    log_stream_arn="logStreamArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a38f2053b120441c24bd925839205cb2f122e8ae54bab1ccd34a6d2a1735aa1f)
                check_type(argname="argument log_stream_arn", value=log_stream_arn, expected_type=type_hints["log_stream_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "log_stream_arn": log_stream_arn,
            }

        @builtins.property
        def log_stream_arn(self) -> builtins.str:
            '''The ARN of the CloudWatch log to receive application messages.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationcloudwatchloggingoption-cloudwatchloggingoption.html#cfn-kinesisanalyticsv2-applicationcloudwatchloggingoption-cloudwatchloggingoption-logstreamarn
            '''
            result = self._values.get("log_stream_arn")
            assert result is not None, "Required property 'log_stream_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchLoggingOptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationCloudWatchLoggingOptionV2Props",
    jsii_struct_bases=[],
    name_mapping={
        "application_name": "applicationName",
        "cloud_watch_logging_option": "cloudWatchLoggingOption",
    },
)
class CfnApplicationCloudWatchLoggingOptionV2Props:
    def __init__(
        self,
        *,
        application_name: builtins.str,
        cloud_watch_logging_option: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationCloudWatchLoggingOptionV2.CloudWatchLoggingOptionProperty, typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Properties for defining a ``CfnApplicationCloudWatchLoggingOptionV2``.

        :param application_name: The name of the application.
        :param cloud_watch_logging_option: Provides a description of Amazon CloudWatch logging options, including the log stream Amazon Resource Name (ARN).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationcloudwatchloggingoption.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_kinesisanalytics as kinesisanalytics
            
            cfn_application_cloud_watch_logging_option_v2_props = kinesisanalytics.CfnApplicationCloudWatchLoggingOptionV2Props(
                application_name="applicationName",
                cloud_watch_logging_option=kinesisanalytics.CfnApplicationCloudWatchLoggingOptionV2.CloudWatchLoggingOptionProperty(
                    log_stream_arn="logStreamArn"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bb49e7696e279c60519c21a5e9b20be4a6f8105cdaf64deb11e8490f4026329)
            check_type(argname="argument application_name", value=application_name, expected_type=type_hints["application_name"])
            check_type(argname="argument cloud_watch_logging_option", value=cloud_watch_logging_option, expected_type=type_hints["cloud_watch_logging_option"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_name": application_name,
            "cloud_watch_logging_option": cloud_watch_logging_option,
        }

    @builtins.property
    def application_name(self) -> builtins.str:
        '''The name of the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationcloudwatchloggingoption.html#cfn-kinesisanalyticsv2-applicationcloudwatchloggingoption-applicationname
        '''
        result = self._values.get("application_name")
        assert result is not None, "Required property 'application_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cloud_watch_logging_option(
        self,
    ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnApplicationCloudWatchLoggingOptionV2.CloudWatchLoggingOptionProperty]:
        '''Provides a description of Amazon CloudWatch logging options, including the log stream Amazon Resource Name (ARN).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationcloudwatchloggingoption.html#cfn-kinesisanalyticsv2-applicationcloudwatchloggingoption-cloudwatchloggingoption
        '''
        result = self._values.get("cloud_watch_logging_option")
        assert result is not None, "Required property 'cloud_watch_logging_option' is missing"
        return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnApplicationCloudWatchLoggingOptionV2.CloudWatchLoggingOptionProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationCloudWatchLoggingOptionV2Props(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnApplicationOutput(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationOutput",
):
    '''A CloudFormation ``AWS::KinesisAnalytics::ApplicationOutput``.

    Adds an external destination to your Amazon Kinesis Analytics application.

    If you want Amazon Kinesis Analytics to deliver data from an in-application stream within your application to an external destination (such as an Amazon Kinesis stream, an Amazon Kinesis Firehose delivery stream, or an Amazon Lambda function), you add the relevant configuration to your application using this operation. You can configure one or more outputs for your application. Each output configuration maps an in-application stream and an external destination.

    You can use one of the output configurations to deliver data from your in-application error stream to an external destination so that you can analyze the errors. For more information, see `Understanding Application Output (Destination) <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-output.html>`_ .

    Any configuration update, including adding a streaming source using this operation, results in a new version of the application. You can use the ``DescribeApplication`` operation to find the current application version.

    For the limits on the number of application inputs and outputs you can configure, see `Limits <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/limits.html>`_ .

    This operation requires permissions to perform the ``kinesisanalytics:AddApplicationOutput`` action.

    :cloudformationResource: AWS::KinesisAnalytics::ApplicationOutput
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationoutput.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_kinesisanalytics as kinesisanalytics
        
        cfn_application_output = kinesisanalytics.CfnApplicationOutput(self, "MyCfnApplicationOutput",
            application_name="applicationName",
            output=kinesisanalytics.CfnApplicationOutput.OutputProperty(
                destination_schema=kinesisanalytics.CfnApplicationOutput.DestinationSchemaProperty(
                    record_format_type="recordFormatType"
                ),
        
                # the properties below are optional
                kinesis_firehose_output=kinesisanalytics.CfnApplicationOutput.KinesisFirehoseOutputProperty(
                    resource_arn="resourceArn",
                    role_arn="roleArn"
                ),
                kinesis_streams_output=kinesisanalytics.CfnApplicationOutput.KinesisStreamsOutputProperty(
                    resource_arn="resourceArn",
                    role_arn="roleArn"
                ),
                lambda_output=kinesisanalytics.CfnApplicationOutput.LambdaOutputProperty(
                    resource_arn="resourceArn",
                    role_arn="roleArn"
                ),
                name="name"
            )
        )
    '''

    def __init__(
        self,
        scope: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        application_name: builtins.str,
        output: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationOutput.OutputProperty", typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Create a new ``AWS::KinesisAnalytics::ApplicationOutput``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param application_name: Name of the application to which you want to add the output configuration.
        :param output: An array of objects, each describing one output configuration. In the output configuration, you specify the name of an in-application stream, a destination (that is, an Amazon Kinesis stream, an Amazon Kinesis Firehose delivery stream, or an AWS Lambda function), and record the formation to use when writing to the destination.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5229b72c55c9ec1a70a752b7ea4f36bff192ae73ffa20446027922b504c3bd47)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApplicationOutputProps(
            application_name=application_name, output=output
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6025a5c38c69b4d29ab92a1915f1da8b80625f3badc9cf792b257c1dff86c8c7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9914019c427934fc10d9c5ef3dc89ef025341e280f5d497093181fe6701f3f3b)
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
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> builtins.str:
        '''Name of the application to which you want to add the output configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationoutput.html#cfn-kinesisanalytics-applicationoutput-applicationname
        '''
        return typing.cast(builtins.str, jsii.get(self, "applicationName"))

    @application_name.setter
    def application_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc3a048e176d5104ca1727f912df4d30999391d1231319db24eebd119c7eda2b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationName", value)

    @builtins.property
    @jsii.member(jsii_name="output")
    def output(
        self,
    ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationOutput.OutputProperty"]:
        '''An array of objects, each describing one output configuration.

        In the output configuration, you specify the name of an in-application stream, a destination (that is, an Amazon Kinesis stream, an Amazon Kinesis Firehose delivery stream, or an AWS Lambda function), and record the formation to use when writing to the destination.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationoutput.html#cfn-kinesisanalytics-applicationoutput-output
        '''
        return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationOutput.OutputProperty"], jsii.get(self, "output"))

    @output.setter
    def output(
        self,
        value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationOutput.OutputProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fe64ac80e7fe311d7dc21dff57e45546ccf0fe7d29e582548c2d160d32470b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "output", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationOutput.DestinationSchemaProperty",
        jsii_struct_bases=[],
        name_mapping={"record_format_type": "recordFormatType"},
    )
    class DestinationSchemaProperty:
        def __init__(
            self,
            *,
            record_format_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes the data format when records are written to the destination.

            For more information, see `Configuring Application Output <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-output.html>`_ .

            :param record_format_type: Specifies the format of the records on the output stream.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-destinationschema.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                destination_schema_property = kinesisanalytics.CfnApplicationOutput.DestinationSchemaProperty(
                    record_format_type="recordFormatType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__25a29ae8b211eff60f243f6354dfda6840bff9cf9146e43c2c19f43c0a84b583)
                check_type(argname="argument record_format_type", value=record_format_type, expected_type=type_hints["record_format_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if record_format_type is not None:
                self._values["record_format_type"] = record_format_type

        @builtins.property
        def record_format_type(self) -> typing.Optional[builtins.str]:
            '''Specifies the format of the records on the output stream.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-destinationschema.html#cfn-kinesisanalytics-applicationoutput-destinationschema-recordformattype
            '''
            result = self._values.get("record_format_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DestinationSchemaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationOutput.KinesisFirehoseOutputProperty",
        jsii_struct_bases=[],
        name_mapping={"resource_arn": "resourceArn", "role_arn": "roleArn"},
    )
    class KinesisFirehoseOutputProperty:
        def __init__(
            self,
            *,
            resource_arn: builtins.str,
            role_arn: builtins.str,
        ) -> None:
            '''When configuring application output, identifies an Amazon Kinesis Firehose delivery stream as the destination.

            You provide the stream Amazon Resource Name (ARN) and an IAM role that enables Amazon Kinesis Analytics to write to the stream on your behalf.

            :param resource_arn: ARN of the destination Amazon Kinesis Firehose delivery stream to write to.
            :param role_arn: ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination stream on your behalf. You need to grant the necessary permissions to this role.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-kinesisfirehoseoutput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                kinesis_firehose_output_property = kinesisanalytics.CfnApplicationOutput.KinesisFirehoseOutputProperty(
                    resource_arn="resourceArn",
                    role_arn="roleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__87d4d7c5ca82e97c714ea59e212dc136025c2a5396d44e0c070f877ee141982d)
                check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "resource_arn": resource_arn,
                "role_arn": role_arn,
            }

        @builtins.property
        def resource_arn(self) -> builtins.str:
            '''ARN of the destination Amazon Kinesis Firehose delivery stream to write to.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-kinesisfirehoseoutput.html#cfn-kinesisanalytics-applicationoutput-kinesisfirehoseoutput-resourcearn
            '''
            result = self._values.get("resource_arn")
            assert result is not None, "Required property 'resource_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination stream on your behalf.

            You need to grant the necessary permissions to this role.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-kinesisfirehoseoutput.html#cfn-kinesisanalytics-applicationoutput-kinesisfirehoseoutput-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisFirehoseOutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationOutput.KinesisStreamsOutputProperty",
        jsii_struct_bases=[],
        name_mapping={"resource_arn": "resourceArn", "role_arn": "roleArn"},
    )
    class KinesisStreamsOutputProperty:
        def __init__(
            self,
            *,
            resource_arn: builtins.str,
            role_arn: builtins.str,
        ) -> None:
            '''When configuring application output, identifies an Amazon Kinesis stream as the destination.

            You provide the stream Amazon Resource Name (ARN) and also an IAM role ARN that Amazon Kinesis Analytics can use to write to the stream on your behalf.

            :param resource_arn: ARN of the destination Amazon Kinesis stream to write to.
            :param role_arn: ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination stream on your behalf. You need to grant the necessary permissions to this role.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-kinesisstreamsoutput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                kinesis_streams_output_property = kinesisanalytics.CfnApplicationOutput.KinesisStreamsOutputProperty(
                    resource_arn="resourceArn",
                    role_arn="roleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__75428eda82ae3ebe39f533c57f88cc57a5be1ca60c456b4175aff4b5d1f7ca29)
                check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "resource_arn": resource_arn,
                "role_arn": role_arn,
            }

        @builtins.property
        def resource_arn(self) -> builtins.str:
            '''ARN of the destination Amazon Kinesis stream to write to.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-kinesisstreamsoutput.html#cfn-kinesisanalytics-applicationoutput-kinesisstreamsoutput-resourcearn
            '''
            result = self._values.get("resource_arn")
            assert result is not None, "Required property 'resource_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination stream on your behalf.

            You need to grant the necessary permissions to this role.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-kinesisstreamsoutput.html#cfn-kinesisanalytics-applicationoutput-kinesisstreamsoutput-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisStreamsOutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationOutput.LambdaOutputProperty",
        jsii_struct_bases=[],
        name_mapping={"resource_arn": "resourceArn", "role_arn": "roleArn"},
    )
    class LambdaOutputProperty:
        def __init__(
            self,
            *,
            resource_arn: builtins.str,
            role_arn: builtins.str,
        ) -> None:
            '''When configuring application output, identifies an AWS Lambda function as the destination.

            You provide the function Amazon Resource Name (ARN) and also an IAM role ARN that Amazon Kinesis Analytics can use to write to the function on your behalf.

            :param resource_arn: Amazon Resource Name (ARN) of the destination Lambda function to write to. .. epigraph:: To specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see `Example ARNs: AWS Lambda <https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`_
            :param role_arn: ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination function on your behalf. You need to grant the necessary permissions to this role.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-lambdaoutput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                lambda_output_property = kinesisanalytics.CfnApplicationOutput.LambdaOutputProperty(
                    resource_arn="resourceArn",
                    role_arn="roleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c1b283619392a3fa63d6c03e676b8a6a33528e0e32a43300e90cb3b0962ac688)
                check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "resource_arn": resource_arn,
                "role_arn": role_arn,
            }

        @builtins.property
        def resource_arn(self) -> builtins.str:
            '''Amazon Resource Name (ARN) of the destination Lambda function to write to.

            .. epigraph::

               To specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see `Example ARNs: AWS Lambda <https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`_

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-lambdaoutput.html#cfn-kinesisanalytics-applicationoutput-lambdaoutput-resourcearn
            '''
            result = self._values.get("resource_arn")
            assert result is not None, "Required property 'resource_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination function on your behalf.

            You need to grant the necessary permissions to this role.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-lambdaoutput.html#cfn-kinesisanalytics-applicationoutput-lambdaoutput-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaOutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationOutput.OutputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination_schema": "destinationSchema",
            "kinesis_firehose_output": "kinesisFirehoseOutput",
            "kinesis_streams_output": "kinesisStreamsOutput",
            "lambda_output": "lambdaOutput",
            "name": "name",
        },
    )
    class OutputProperty:
        def __init__(
            self,
            *,
            destination_schema: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationOutput.DestinationSchemaProperty", typing.Dict[builtins.str, typing.Any]]],
            kinesis_firehose_output: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationOutput.KinesisFirehoseOutputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            kinesis_streams_output: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationOutput.KinesisStreamsOutputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            lambda_output: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationOutput.LambdaOutputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes application output configuration in which you identify an in-application stream and a destination where you want the in-application stream data to be written.

            The destination can be an Amazon Kinesis stream or an Amazon Kinesis Firehose delivery stream.

            For limits on how many destinations an application can write and other limitations, see `Limits <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/limits.html>`_ .

            :param destination_schema: Describes the data format when records are written to the destination. For more information, see `Configuring Application Output <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-output.html>`_ .
            :param kinesis_firehose_output: Identifies an Amazon Kinesis Firehose delivery stream as the destination.
            :param kinesis_streams_output: Identifies an Amazon Kinesis stream as the destination.
            :param lambda_output: Identifies an AWS Lambda function as the destination.
            :param name: Name of the in-application stream.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-output.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                output_property = kinesisanalytics.CfnApplicationOutput.OutputProperty(
                    destination_schema=kinesisanalytics.CfnApplicationOutput.DestinationSchemaProperty(
                        record_format_type="recordFormatType"
                    ),
                
                    # the properties below are optional
                    kinesis_firehose_output=kinesisanalytics.CfnApplicationOutput.KinesisFirehoseOutputProperty(
                        resource_arn="resourceArn",
                        role_arn="roleArn"
                    ),
                    kinesis_streams_output=kinesisanalytics.CfnApplicationOutput.KinesisStreamsOutputProperty(
                        resource_arn="resourceArn",
                        role_arn="roleArn"
                    ),
                    lambda_output=kinesisanalytics.CfnApplicationOutput.LambdaOutputProperty(
                        resource_arn="resourceArn",
                        role_arn="roleArn"
                    ),
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e1110074cda4eca6c6baff3f4e75bd112bad6528b90687200b080e88991054fe)
                check_type(argname="argument destination_schema", value=destination_schema, expected_type=type_hints["destination_schema"])
                check_type(argname="argument kinesis_firehose_output", value=kinesis_firehose_output, expected_type=type_hints["kinesis_firehose_output"])
                check_type(argname="argument kinesis_streams_output", value=kinesis_streams_output, expected_type=type_hints["kinesis_streams_output"])
                check_type(argname="argument lambda_output", value=lambda_output, expected_type=type_hints["lambda_output"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "destination_schema": destination_schema,
            }
            if kinesis_firehose_output is not None:
                self._values["kinesis_firehose_output"] = kinesis_firehose_output
            if kinesis_streams_output is not None:
                self._values["kinesis_streams_output"] = kinesis_streams_output
            if lambda_output is not None:
                self._values["lambda_output"] = lambda_output
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def destination_schema(
            self,
        ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationOutput.DestinationSchemaProperty"]:
            '''Describes the data format when records are written to the destination.

            For more information, see `Configuring Application Output <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-output.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-output.html#cfn-kinesisanalytics-applicationoutput-output-destinationschema
            '''
            result = self._values.get("destination_schema")
            assert result is not None, "Required property 'destination_schema' is missing"
            return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationOutput.DestinationSchemaProperty"], result)

        @builtins.property
        def kinesis_firehose_output(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationOutput.KinesisFirehoseOutputProperty"]]:
            '''Identifies an Amazon Kinesis Firehose delivery stream as the destination.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-output.html#cfn-kinesisanalytics-applicationoutput-output-kinesisfirehoseoutput
            '''
            result = self._values.get("kinesis_firehose_output")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationOutput.KinesisFirehoseOutputProperty"]], result)

        @builtins.property
        def kinesis_streams_output(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationOutput.KinesisStreamsOutputProperty"]]:
            '''Identifies an Amazon Kinesis stream as the destination.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-output.html#cfn-kinesisanalytics-applicationoutput-output-kinesisstreamsoutput
            '''
            result = self._values.get("kinesis_streams_output")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationOutput.KinesisStreamsOutputProperty"]], result)

        @builtins.property
        def lambda_output(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationOutput.LambdaOutputProperty"]]:
            '''Identifies an AWS Lambda function as the destination.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-output.html#cfn-kinesisanalytics-applicationoutput-output-lambdaoutput
            '''
            result = self._values.get("lambda_output")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationOutput.LambdaOutputProperty"]], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''Name of the in-application stream.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-output.html#cfn-kinesisanalytics-applicationoutput-output-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationOutputProps",
    jsii_struct_bases=[],
    name_mapping={"application_name": "applicationName", "output": "output"},
)
class CfnApplicationOutputProps:
    def __init__(
        self,
        *,
        application_name: builtins.str,
        output: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationOutput.OutputProperty, typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Properties for defining a ``CfnApplicationOutput``.

        :param application_name: Name of the application to which you want to add the output configuration.
        :param output: An array of objects, each describing one output configuration. In the output configuration, you specify the name of an in-application stream, a destination (that is, an Amazon Kinesis stream, an Amazon Kinesis Firehose delivery stream, or an AWS Lambda function), and record the formation to use when writing to the destination.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationoutput.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_kinesisanalytics as kinesisanalytics
            
            cfn_application_output_props = kinesisanalytics.CfnApplicationOutputProps(
                application_name="applicationName",
                output=kinesisanalytics.CfnApplicationOutput.OutputProperty(
                    destination_schema=kinesisanalytics.CfnApplicationOutput.DestinationSchemaProperty(
                        record_format_type="recordFormatType"
                    ),
            
                    # the properties below are optional
                    kinesis_firehose_output=kinesisanalytics.CfnApplicationOutput.KinesisFirehoseOutputProperty(
                        resource_arn="resourceArn",
                        role_arn="roleArn"
                    ),
                    kinesis_streams_output=kinesisanalytics.CfnApplicationOutput.KinesisStreamsOutputProperty(
                        resource_arn="resourceArn",
                        role_arn="roleArn"
                    ),
                    lambda_output=kinesisanalytics.CfnApplicationOutput.LambdaOutputProperty(
                        resource_arn="resourceArn",
                        role_arn="roleArn"
                    ),
                    name="name"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbc34d8b567a52fbe3b9065874429ecc60b290de7e8b59020fe6e8e33ca74fb2)
            check_type(argname="argument application_name", value=application_name, expected_type=type_hints["application_name"])
            check_type(argname="argument output", value=output, expected_type=type_hints["output"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_name": application_name,
            "output": output,
        }

    @builtins.property
    def application_name(self) -> builtins.str:
        '''Name of the application to which you want to add the output configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationoutput.html#cfn-kinesisanalytics-applicationoutput-applicationname
        '''
        result = self._values.get("application_name")
        assert result is not None, "Required property 'application_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def output(
        self,
    ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnApplicationOutput.OutputProperty]:
        '''An array of objects, each describing one output configuration.

        In the output configuration, you specify the name of an in-application stream, a destination (that is, an Amazon Kinesis stream, an Amazon Kinesis Firehose delivery stream, or an AWS Lambda function), and record the formation to use when writing to the destination.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationoutput.html#cfn-kinesisanalytics-applicationoutput-output
        '''
        result = self._values.get("output")
        assert result is not None, "Required property 'output' is missing"
        return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnApplicationOutput.OutputProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationOutputProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnApplicationOutputV2(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationOutputV2",
):
    '''A CloudFormation ``AWS::KinesisAnalyticsV2::ApplicationOutput``.

    Adds an external destination to your SQL-based Amazon Kinesis Data Analytics application.

    If you want Kinesis Data Analytics to deliver data from an in-application stream within your application to an external destination (such as an Kinesis data stream, a Kinesis Data Firehose delivery stream, or an Amazon Lambda function), you add the relevant configuration to your application using this operation. You can configure one or more outputs for your application. Each output configuration maps an in-application stream and an external destination.

    You can use one of the output configurations to deliver data from your in-application error stream to an external destination so that you can analyze the errors.

    Any configuration update, including adding a streaming source using this operation, results in a new version of the application. You can use the `DescribeApplication <https://docs.aws.amazon.com/kinesisanalytics/latest/apiv2/API_DescribeApplication.html>`_ operation to find the current application version.
    .. epigraph::

       Creation of multiple outputs should be sequential (use of DependsOn) to avoid a problem with a stale application version ( *ConcurrentModificationException* ).

    :cloudformationResource: AWS::KinesisAnalyticsV2::ApplicationOutput
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationoutput.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_kinesisanalytics as kinesisanalytics
        
        cfn_application_output_v2 = kinesisanalytics.CfnApplicationOutputV2(self, "MyCfnApplicationOutputV2",
            application_name="applicationName",
            output=kinesisanalytics.CfnApplicationOutputV2.OutputProperty(
                destination_schema=kinesisanalytics.CfnApplicationOutputV2.DestinationSchemaProperty(
                    record_format_type="recordFormatType"
                ),
        
                # the properties below are optional
                kinesis_firehose_output=kinesisanalytics.CfnApplicationOutputV2.KinesisFirehoseOutputProperty(
                    resource_arn="resourceArn"
                ),
                kinesis_streams_output=kinesisanalytics.CfnApplicationOutputV2.KinesisStreamsOutputProperty(
                    resource_arn="resourceArn"
                ),
                lambda_output=kinesisanalytics.CfnApplicationOutputV2.LambdaOutputProperty(
                    resource_arn="resourceArn"
                ),
                name="name"
            )
        )
    '''

    def __init__(
        self,
        scope: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        application_name: builtins.str,
        output: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationOutputV2.OutputProperty", typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Create a new ``AWS::KinesisAnalyticsV2::ApplicationOutput``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param application_name: The name of the application.
        :param output: Describes a SQL-based Kinesis Data Analytics application's output configuration, in which you identify an in-application stream and a destination where you want the in-application stream data to be written. The destination can be a Kinesis data stream or a Kinesis Data Firehose delivery stream.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__867c8fd92db8504a1076451d89e6d22bbbaf5ed11d87c0a07e0d573683fedf41)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApplicationOutputV2Props(
            application_name=application_name, output=output
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e80fcd45e56a2891d9ba87acea691afe6f274873237a3bab86b8e828706e4935)
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
            type_hints = typing.get_type_hints(_typecheckingstub__14ed88b9d3086377681a2689a41a980abb24bc0d0113a6005c8ca74124c4836a)
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
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> builtins.str:
        '''The name of the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationoutput.html#cfn-kinesisanalyticsv2-applicationoutput-applicationname
        '''
        return typing.cast(builtins.str, jsii.get(self, "applicationName"))

    @application_name.setter
    def application_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b59fa77e2c0332f5a6cbb3d58a719518ae89fb2132666d64e0c775aee4b6cfde)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationName", value)

    @builtins.property
    @jsii.member(jsii_name="output")
    def output(
        self,
    ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationOutputV2.OutputProperty"]:
        '''Describes a SQL-based Kinesis Data Analytics application's output configuration, in which you identify an in-application stream and a destination where you want the in-application stream data to be written.

        The destination can be a Kinesis data stream or a Kinesis Data Firehose delivery stream.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationoutput.html#cfn-kinesisanalyticsv2-applicationoutput-output
        '''
        return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationOutputV2.OutputProperty"], jsii.get(self, "output"))

    @output.setter
    def output(
        self,
        value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationOutputV2.OutputProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5954b4a1d7646d8e17ffb1231cf43daab2dd42c678a2ad58a884b9c8a06359b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "output", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationOutputV2.DestinationSchemaProperty",
        jsii_struct_bases=[],
        name_mapping={"record_format_type": "recordFormatType"},
    )
    class DestinationSchemaProperty:
        def __init__(
            self,
            *,
            record_format_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes the data format when records are written to the destination in a SQL-based Kinesis Data Analytics application.

            :param record_format_type: Specifies the format of the records on the output stream.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-destinationschema.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                destination_schema_property = kinesisanalytics.CfnApplicationOutputV2.DestinationSchemaProperty(
                    record_format_type="recordFormatType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9385cd408d5be727dae9f859288dd0ca5006e0e95d58288866d52bf26e97f1c7)
                check_type(argname="argument record_format_type", value=record_format_type, expected_type=type_hints["record_format_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if record_format_type is not None:
                self._values["record_format_type"] = record_format_type

        @builtins.property
        def record_format_type(self) -> typing.Optional[builtins.str]:
            '''Specifies the format of the records on the output stream.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-destinationschema.html#cfn-kinesisanalyticsv2-applicationoutput-destinationschema-recordformattype
            '''
            result = self._values.get("record_format_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DestinationSchemaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationOutputV2.KinesisFirehoseOutputProperty",
        jsii_struct_bases=[],
        name_mapping={"resource_arn": "resourceArn"},
    )
    class KinesisFirehoseOutputProperty:
        def __init__(self, *, resource_arn: builtins.str) -> None:
            '''For a SQL-based Kinesis Data Analytics application, when configuring application output, identifies a Kinesis Data Firehose delivery stream as the destination.

            You provide the stream Amazon Resource Name (ARN) of the delivery stream.

            :param resource_arn: The ARN of the destination delivery stream to write to.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-kinesisfirehoseoutput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                kinesis_firehose_output_property = kinesisanalytics.CfnApplicationOutputV2.KinesisFirehoseOutputProperty(
                    resource_arn="resourceArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0c1487dfe1a7f9d117e17be7ff927e4d17fd2f8902372013007a62ba0bbd0f5e)
                check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "resource_arn": resource_arn,
            }

        @builtins.property
        def resource_arn(self) -> builtins.str:
            '''The ARN of the destination delivery stream to write to.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-kinesisfirehoseoutput.html#cfn-kinesisanalyticsv2-applicationoutput-kinesisfirehoseoutput-resourcearn
            '''
            result = self._values.get("resource_arn")
            assert result is not None, "Required property 'resource_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisFirehoseOutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationOutputV2.KinesisStreamsOutputProperty",
        jsii_struct_bases=[],
        name_mapping={"resource_arn": "resourceArn"},
    )
    class KinesisStreamsOutputProperty:
        def __init__(self, *, resource_arn: builtins.str) -> None:
            '''When you configure a SQL-based Kinesis Data Analytics application's output, identifies a Kinesis data stream as the destination.

            You provide the stream Amazon Resource Name (ARN).

            :param resource_arn: The ARN of the destination Kinesis data stream to write to.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-kinesisstreamsoutput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                kinesis_streams_output_property = kinesisanalytics.CfnApplicationOutputV2.KinesisStreamsOutputProperty(
                    resource_arn="resourceArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__75d789c62fcd2dca1e7d7416e99312388e2a2f09a47a3fe9556b55af7bd4bc87)
                check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "resource_arn": resource_arn,
            }

        @builtins.property
        def resource_arn(self) -> builtins.str:
            '''The ARN of the destination Kinesis data stream to write to.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-kinesisstreamsoutput.html#cfn-kinesisanalyticsv2-applicationoutput-kinesisstreamsoutput-resourcearn
            '''
            result = self._values.get("resource_arn")
            assert result is not None, "Required property 'resource_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisStreamsOutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationOutputV2.LambdaOutputProperty",
        jsii_struct_bases=[],
        name_mapping={"resource_arn": "resourceArn"},
    )
    class LambdaOutputProperty:
        def __init__(self, *, resource_arn: builtins.str) -> None:
            '''When you configure a SQL-based Kinesis Data Analytics application's output, identifies an Amazon Lambda function as the destination.

            You provide the function Amazon Resource Name (ARN) of the Lambda function.

            :param resource_arn: The Amazon Resource Name (ARN) of the destination Lambda function to write to. .. epigraph:: To specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see `Example ARNs: Amazon Lambda <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`_

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-lambdaoutput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                lambda_output_property = kinesisanalytics.CfnApplicationOutputV2.LambdaOutputProperty(
                    resource_arn="resourceArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f7cd31a34a9cc14f01936e576adc40a1a574f6b79520943e453ac7c47d96f256)
                check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "resource_arn": resource_arn,
            }

        @builtins.property
        def resource_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the destination Lambda function to write to.

            .. epigraph::

               To specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see `Example ARNs: Amazon Lambda <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`_

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-lambdaoutput.html#cfn-kinesisanalyticsv2-applicationoutput-lambdaoutput-resourcearn
            '''
            result = self._values.get("resource_arn")
            assert result is not None, "Required property 'resource_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaOutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationOutputV2.OutputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination_schema": "destinationSchema",
            "kinesis_firehose_output": "kinesisFirehoseOutput",
            "kinesis_streams_output": "kinesisStreamsOutput",
            "lambda_output": "lambdaOutput",
            "name": "name",
        },
    )
    class OutputProperty:
        def __init__(
            self,
            *,
            destination_schema: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationOutputV2.DestinationSchemaProperty", typing.Dict[builtins.str, typing.Any]]],
            kinesis_firehose_output: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationOutputV2.KinesisFirehoseOutputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            kinesis_streams_output: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationOutputV2.KinesisStreamsOutputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            lambda_output: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationOutputV2.LambdaOutputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes a SQL-based Kinesis Data Analytics application's output configuration, in which you identify an in-application stream and a destination where you want the in-application stream data to be written.

            The destination can be a Kinesis data stream or a Kinesis Data Firehose delivery stream.

            :param destination_schema: Describes the data format when records are written to the destination.
            :param kinesis_firehose_output: Identifies a Kinesis Data Firehose delivery stream as the destination.
            :param kinesis_streams_output: Identifies a Kinesis data stream as the destination.
            :param lambda_output: Identifies an Amazon Lambda function as the destination.
            :param name: The name of the in-application stream.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-output.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                output_property = kinesisanalytics.CfnApplicationOutputV2.OutputProperty(
                    destination_schema=kinesisanalytics.CfnApplicationOutputV2.DestinationSchemaProperty(
                        record_format_type="recordFormatType"
                    ),
                
                    # the properties below are optional
                    kinesis_firehose_output=kinesisanalytics.CfnApplicationOutputV2.KinesisFirehoseOutputProperty(
                        resource_arn="resourceArn"
                    ),
                    kinesis_streams_output=kinesisanalytics.CfnApplicationOutputV2.KinesisStreamsOutputProperty(
                        resource_arn="resourceArn"
                    ),
                    lambda_output=kinesisanalytics.CfnApplicationOutputV2.LambdaOutputProperty(
                        resource_arn="resourceArn"
                    ),
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__63140470e878b081e70d74561d7050821df2fc723b52bd9d1e8d4fbb7c921d19)
                check_type(argname="argument destination_schema", value=destination_schema, expected_type=type_hints["destination_schema"])
                check_type(argname="argument kinesis_firehose_output", value=kinesis_firehose_output, expected_type=type_hints["kinesis_firehose_output"])
                check_type(argname="argument kinesis_streams_output", value=kinesis_streams_output, expected_type=type_hints["kinesis_streams_output"])
                check_type(argname="argument lambda_output", value=lambda_output, expected_type=type_hints["lambda_output"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "destination_schema": destination_schema,
            }
            if kinesis_firehose_output is not None:
                self._values["kinesis_firehose_output"] = kinesis_firehose_output
            if kinesis_streams_output is not None:
                self._values["kinesis_streams_output"] = kinesis_streams_output
            if lambda_output is not None:
                self._values["lambda_output"] = lambda_output
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def destination_schema(
            self,
        ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationOutputV2.DestinationSchemaProperty"]:
            '''Describes the data format when records are written to the destination.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-output.html#cfn-kinesisanalyticsv2-applicationoutput-output-destinationschema
            '''
            result = self._values.get("destination_schema")
            assert result is not None, "Required property 'destination_schema' is missing"
            return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationOutputV2.DestinationSchemaProperty"], result)

        @builtins.property
        def kinesis_firehose_output(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationOutputV2.KinesisFirehoseOutputProperty"]]:
            '''Identifies a Kinesis Data Firehose delivery stream as the destination.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-output.html#cfn-kinesisanalyticsv2-applicationoutput-output-kinesisfirehoseoutput
            '''
            result = self._values.get("kinesis_firehose_output")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationOutputV2.KinesisFirehoseOutputProperty"]], result)

        @builtins.property
        def kinesis_streams_output(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationOutputV2.KinesisStreamsOutputProperty"]]:
            '''Identifies a Kinesis data stream as the destination.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-output.html#cfn-kinesisanalyticsv2-applicationoutput-output-kinesisstreamsoutput
            '''
            result = self._values.get("kinesis_streams_output")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationOutputV2.KinesisStreamsOutputProperty"]], result)

        @builtins.property
        def lambda_output(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationOutputV2.LambdaOutputProperty"]]:
            '''Identifies an Amazon Lambda function as the destination.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-output.html#cfn-kinesisanalyticsv2-applicationoutput-output-lambdaoutput
            '''
            result = self._values.get("lambda_output")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationOutputV2.LambdaOutputProperty"]], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the in-application stream.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-output.html#cfn-kinesisanalyticsv2-applicationoutput-output-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationOutputV2Props",
    jsii_struct_bases=[],
    name_mapping={"application_name": "applicationName", "output": "output"},
)
class CfnApplicationOutputV2Props:
    def __init__(
        self,
        *,
        application_name: builtins.str,
        output: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationOutputV2.OutputProperty, typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Properties for defining a ``CfnApplicationOutputV2``.

        :param application_name: The name of the application.
        :param output: Describes a SQL-based Kinesis Data Analytics application's output configuration, in which you identify an in-application stream and a destination where you want the in-application stream data to be written. The destination can be a Kinesis data stream or a Kinesis Data Firehose delivery stream.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationoutput.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_kinesisanalytics as kinesisanalytics
            
            cfn_application_output_v2_props = kinesisanalytics.CfnApplicationOutputV2Props(
                application_name="applicationName",
                output=kinesisanalytics.CfnApplicationOutputV2.OutputProperty(
                    destination_schema=kinesisanalytics.CfnApplicationOutputV2.DestinationSchemaProperty(
                        record_format_type="recordFormatType"
                    ),
            
                    # the properties below are optional
                    kinesis_firehose_output=kinesisanalytics.CfnApplicationOutputV2.KinesisFirehoseOutputProperty(
                        resource_arn="resourceArn"
                    ),
                    kinesis_streams_output=kinesisanalytics.CfnApplicationOutputV2.KinesisStreamsOutputProperty(
                        resource_arn="resourceArn"
                    ),
                    lambda_output=kinesisanalytics.CfnApplicationOutputV2.LambdaOutputProperty(
                        resource_arn="resourceArn"
                    ),
                    name="name"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc1d3254af5c8202efccb3d570a7c2d03927d2a7c1eeca6cb1763bb1aeeac46d)
            check_type(argname="argument application_name", value=application_name, expected_type=type_hints["application_name"])
            check_type(argname="argument output", value=output, expected_type=type_hints["output"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_name": application_name,
            "output": output,
        }

    @builtins.property
    def application_name(self) -> builtins.str:
        '''The name of the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationoutput.html#cfn-kinesisanalyticsv2-applicationoutput-applicationname
        '''
        result = self._values.get("application_name")
        assert result is not None, "Required property 'application_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def output(
        self,
    ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnApplicationOutputV2.OutputProperty]:
        '''Describes a SQL-based Kinesis Data Analytics application's output configuration, in which you identify an in-application stream and a destination where you want the in-application stream data to be written.

        The destination can be a Kinesis data stream or a Kinesis Data Firehose delivery stream.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationoutput.html#cfn-kinesisanalyticsv2-applicationoutput-output
        '''
        result = self._values.get("output")
        assert result is not None, "Required property 'output' is missing"
        return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnApplicationOutputV2.OutputProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationOutputV2Props(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationProps",
    jsii_struct_bases=[],
    name_mapping={
        "inputs": "inputs",
        "application_code": "applicationCode",
        "application_description": "applicationDescription",
        "application_name": "applicationName",
    },
)
class CfnApplicationProps:
    def __init__(
        self,
        *,
        inputs: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[typing.Union[CfnApplication.InputProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable]]],
        application_code: typing.Optional[builtins.str] = None,
        application_description: typing.Optional[builtins.str] = None,
        application_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnApplication``.

        :param inputs: Use this parameter to configure the application input. You can configure your application to receive input from a single streaming source. In this configuration, you map this streaming source to an in-application stream that is created. Your application code can then query the in-application stream like a table (you can think of it as a constantly updating table). For the streaming source, you provide its Amazon Resource Name (ARN) and format of data on the stream (for example, JSON, CSV, etc.). You also must provide an IAM role that Amazon Kinesis Analytics can assume to read this stream on your behalf. To create the in-application stream, you need to specify a schema to transform your data into a schematized version used in SQL. In the schema, you provide the necessary mapping of the data elements in the streaming source to record columns in the in-app stream.
        :param application_code: One or more SQL statements that read input data, transform it, and generate output. For example, you can write a SQL statement that reads data from one in-application stream, generates a running average of the number of advertisement clicks by vendor, and insert resulting rows in another in-application stream using pumps. For more information about the typical pattern, see `Application Code <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-app-code.html>`_ . You can provide such series of SQL statements, where output of one statement can be used as the input for the next statement. You store intermediate results by creating in-application streams and pumps. Note that the application code must create the streams with names specified in the ``Outputs`` . For example, if your ``Outputs`` defines output streams named ``ExampleOutputStream1`` and ``ExampleOutputStream2`` , then your application code must create these streams.
        :param application_description: Summary description of the application.
        :param application_name: Name of your Amazon Kinesis Analytics application (for example, ``sample-app`` ).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-application.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_kinesisanalytics as kinesisanalytics
            
            cfn_application_props = kinesisanalytics.CfnApplicationProps(
                inputs=[kinesisanalytics.CfnApplication.InputProperty(
                    input_schema=kinesisanalytics.CfnApplication.InputSchemaProperty(
                        record_columns=[kinesisanalytics.CfnApplication.RecordColumnProperty(
                            name="name",
                            sql_type="sqlType",
            
                            # the properties below are optional
                            mapping="mapping"
                        )],
                        record_format=kinesisanalytics.CfnApplication.RecordFormatProperty(
                            record_format_type="recordFormatType",
            
                            # the properties below are optional
                            mapping_parameters=kinesisanalytics.CfnApplication.MappingParametersProperty(
                                csv_mapping_parameters=kinesisanalytics.CfnApplication.CSVMappingParametersProperty(
                                    record_column_delimiter="recordColumnDelimiter",
                                    record_row_delimiter="recordRowDelimiter"
                                ),
                                json_mapping_parameters=kinesisanalytics.CfnApplication.JSONMappingParametersProperty(
                                    record_row_path="recordRowPath"
                                )
                            )
                        ),
            
                        # the properties below are optional
                        record_encoding="recordEncoding"
                    ),
                    name_prefix="namePrefix",
            
                    # the properties below are optional
                    input_parallelism=kinesisanalytics.CfnApplication.InputParallelismProperty(
                        count=123
                    ),
                    input_processing_configuration=kinesisanalytics.CfnApplication.InputProcessingConfigurationProperty(
                        input_lambda_processor=kinesisanalytics.CfnApplication.InputLambdaProcessorProperty(
                            resource_arn="resourceArn",
                            role_arn="roleArn"
                        )
                    ),
                    kinesis_firehose_input=kinesisanalytics.CfnApplication.KinesisFirehoseInputProperty(
                        resource_arn="resourceArn",
                        role_arn="roleArn"
                    ),
                    kinesis_streams_input=kinesisanalytics.CfnApplication.KinesisStreamsInputProperty(
                        resource_arn="resourceArn",
                        role_arn="roleArn"
                    )
                )],
            
                # the properties below are optional
                application_code="applicationCode",
                application_description="applicationDescription",
                application_name="applicationName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fb160a2e8a7875ab724e2eb7e0fba236734e0241ad51f9a6725060acdc87383)
            check_type(argname="argument inputs", value=inputs, expected_type=type_hints["inputs"])
            check_type(argname="argument application_code", value=application_code, expected_type=type_hints["application_code"])
            check_type(argname="argument application_description", value=application_description, expected_type=type_hints["application_description"])
            check_type(argname="argument application_name", value=application_name, expected_type=type_hints["application_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "inputs": inputs,
        }
        if application_code is not None:
            self._values["application_code"] = application_code
        if application_description is not None:
            self._values["application_description"] = application_description
        if application_name is not None:
            self._values["application_name"] = application_name

    @builtins.property
    def inputs(
        self,
    ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[CfnApplication.InputProperty, _aws_cdk_core_f4b25747.IResolvable]]]:
        '''Use this parameter to configure the application input.

        You can configure your application to receive input from a single streaming source. In this configuration, you map this streaming source to an in-application stream that is created. Your application code can then query the in-application stream like a table (you can think of it as a constantly updating table).

        For the streaming source, you provide its Amazon Resource Name (ARN) and format of data on the stream (for example, JSON, CSV, etc.). You also must provide an IAM role that Amazon Kinesis Analytics can assume to read this stream on your behalf.

        To create the in-application stream, you need to specify a schema to transform your data into a schematized version used in SQL. In the schema, you provide the necessary mapping of the data elements in the streaming source to record columns in the in-app stream.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-application.html#cfn-kinesisanalytics-application-inputs
        '''
        result = self._values.get("inputs")
        assert result is not None, "Required property 'inputs' is missing"
        return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[CfnApplication.InputProperty, _aws_cdk_core_f4b25747.IResolvable]]], result)

    @builtins.property
    def application_code(self) -> typing.Optional[builtins.str]:
        '''One or more SQL statements that read input data, transform it, and generate output.

        For example, you can write a SQL statement that reads data from one in-application stream, generates a running average of the number of advertisement clicks by vendor, and insert resulting rows in another in-application stream using pumps. For more information about the typical pattern, see `Application Code <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-app-code.html>`_ .

        You can provide such series of SQL statements, where output of one statement can be used as the input for the next statement. You store intermediate results by creating in-application streams and pumps.

        Note that the application code must create the streams with names specified in the ``Outputs`` . For example, if your ``Outputs`` defines output streams named ``ExampleOutputStream1`` and ``ExampleOutputStream2`` , then your application code must create these streams.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-application.html#cfn-kinesisanalytics-application-applicationcode
        '''
        result = self._values.get("application_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def application_description(self) -> typing.Optional[builtins.str]:
        '''Summary description of the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-application.html#cfn-kinesisanalytics-application-applicationdescription
        '''
        result = self._values.get("application_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def application_name(self) -> typing.Optional[builtins.str]:
        '''Name of your Amazon Kinesis Analytics application (for example, ``sample-app`` ).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-application.html#cfn-kinesisanalytics-application-applicationname
        '''
        result = self._values.get("application_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnApplicationReferenceDataSource(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationReferenceDataSource",
):
    '''A CloudFormation ``AWS::KinesisAnalytics::ApplicationReferenceDataSource``.

    Adds a reference data source to an existing application.

    Amazon Kinesis Analytics reads reference data (that is, an Amazon S3 object) and creates an in-application table within your application. In the request, you provide the source (S3 bucket name and object key name), name of the in-application table to create, and the necessary mapping information that describes how data in Amazon S3 object maps to columns in the resulting in-application table.

    For conceptual information, see `Configuring Application Input <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html>`_ . For the limits on data sources you can add to your application, see `Limits <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/limits.html>`_ .

    This operation requires permissions to perform the ``kinesisanalytics:AddApplicationOutput`` action.

    :cloudformationResource: AWS::KinesisAnalytics::ApplicationReferenceDataSource
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationreferencedatasource.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_kinesisanalytics as kinesisanalytics
        
        cfn_application_reference_data_source = kinesisanalytics.CfnApplicationReferenceDataSource(self, "MyCfnApplicationReferenceDataSource",
            application_name="applicationName",
            reference_data_source=kinesisanalytics.CfnApplicationReferenceDataSource.ReferenceDataSourceProperty(
                reference_schema=kinesisanalytics.CfnApplicationReferenceDataSource.ReferenceSchemaProperty(
                    record_columns=[kinesisanalytics.CfnApplicationReferenceDataSource.RecordColumnProperty(
                        name="name",
                        sql_type="sqlType",
        
                        # the properties below are optional
                        mapping="mapping"
                    )],
                    record_format=kinesisanalytics.CfnApplicationReferenceDataSource.RecordFormatProperty(
                        record_format_type="recordFormatType",
        
                        # the properties below are optional
                        mapping_parameters=kinesisanalytics.CfnApplicationReferenceDataSource.MappingParametersProperty(
                            csv_mapping_parameters=kinesisanalytics.CfnApplicationReferenceDataSource.CSVMappingParametersProperty(
                                record_column_delimiter="recordColumnDelimiter",
                                record_row_delimiter="recordRowDelimiter"
                            ),
                            json_mapping_parameters=kinesisanalytics.CfnApplicationReferenceDataSource.JSONMappingParametersProperty(
                                record_row_path="recordRowPath"
                            )
                        )
                    ),
        
                    # the properties below are optional
                    record_encoding="recordEncoding"
                ),
        
                # the properties below are optional
                s3_reference_data_source=kinesisanalytics.CfnApplicationReferenceDataSource.S3ReferenceDataSourceProperty(
                    bucket_arn="bucketArn",
                    file_key="fileKey",
                    reference_role_arn="referenceRoleArn"
                ),
                table_name="tableName"
            )
        )
    '''

    def __init__(
        self,
        scope: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        application_name: builtins.str,
        reference_data_source: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationReferenceDataSource.ReferenceDataSourceProperty", typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Create a new ``AWS::KinesisAnalytics::ApplicationReferenceDataSource``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param application_name: Name of an existing application.
        :param reference_data_source: The reference data source can be an object in your Amazon S3 bucket. Amazon Kinesis Analytics reads the object and copies the data into the in-application table that is created. You provide an S3 bucket, object key name, and the resulting in-application table that is created. You must also provide an IAM role with the necessary permissions that Amazon Kinesis Analytics can assume to read the object from your S3 bucket on your behalf.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44b7524227e355ee536eb12a4b2fa4be32bf8b6d39fd1ba2268193cbff72f7d7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApplicationReferenceDataSourceProps(
            application_name=application_name,
            reference_data_source=reference_data_source,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb5bcff94728a48081af5ba06227e50f77f164c6a0e40f2424ce920feb46e253)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9ce761cff42aac9adf870e048443c1c4c76f8a78aedf21c2eb27dcb5ffd9e5ce)
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
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> builtins.str:
        '''Name of an existing application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationreferencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-applicationname
        '''
        return typing.cast(builtins.str, jsii.get(self, "applicationName"))

    @application_name.setter
    def application_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1851c29bf9c1785247cc3f20b8fe0ccda26baefcaf14697e79f376052bc40353)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationName", value)

    @builtins.property
    @jsii.member(jsii_name="referenceDataSource")
    def reference_data_source(
        self,
    ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationReferenceDataSource.ReferenceDataSourceProperty"]:
        '''The reference data source can be an object in your Amazon S3 bucket.

        Amazon Kinesis Analytics reads the object and copies the data into the in-application table that is created. You provide an S3 bucket, object key name, and the resulting in-application table that is created. You must also provide an IAM role with the necessary permissions that Amazon Kinesis Analytics can assume to read the object from your S3 bucket on your behalf.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationreferencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-referencedatasource
        '''
        return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationReferenceDataSource.ReferenceDataSourceProperty"], jsii.get(self, "referenceDataSource"))

    @reference_data_source.setter
    def reference_data_source(
        self,
        value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationReferenceDataSource.ReferenceDataSourceProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1151c61e8c048ee068553784f70c8ebd82a4c1564930da1972aa958c604d10a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "referenceDataSource", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationReferenceDataSource.CSVMappingParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "record_column_delimiter": "recordColumnDelimiter",
            "record_row_delimiter": "recordRowDelimiter",
        },
    )
    class CSVMappingParametersProperty:
        def __init__(
            self,
            *,
            record_column_delimiter: builtins.str,
            record_row_delimiter: builtins.str,
        ) -> None:
            '''Provides additional mapping information when the record format uses delimiters, such as CSV.

            For example, the following sample records use CSV format, where the records use the *'\\n'* as the row delimiter and a comma (",") as the column delimiter:

            ``"name1", "address1"``

            ``"name2", "address2"``

            :param record_column_delimiter: Column delimiter. For example, in a CSV format, a comma (",") is the typical column delimiter.
            :param record_row_delimiter: Row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-csvmappingparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                c_sVMapping_parameters_property = kinesisanalytics.CfnApplicationReferenceDataSource.CSVMappingParametersProperty(
                    record_column_delimiter="recordColumnDelimiter",
                    record_row_delimiter="recordRowDelimiter"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0c33dcc6cd16de9112b4380ce2ab5204cdeb7a783975c66da00cb15702e1642d)
                check_type(argname="argument record_column_delimiter", value=record_column_delimiter, expected_type=type_hints["record_column_delimiter"])
                check_type(argname="argument record_row_delimiter", value=record_row_delimiter, expected_type=type_hints["record_row_delimiter"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "record_column_delimiter": record_column_delimiter,
                "record_row_delimiter": record_row_delimiter,
            }

        @builtins.property
        def record_column_delimiter(self) -> builtins.str:
            '''Column delimiter.

            For example, in a CSV format, a comma (",") is the typical column delimiter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-csvmappingparameters.html#cfn-kinesisanalytics-applicationreferencedatasource-csvmappingparameters-recordcolumndelimiter
            '''
            result = self._values.get("record_column_delimiter")
            assert result is not None, "Required property 'record_column_delimiter' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def record_row_delimiter(self) -> builtins.str:
            '''Row delimiter.

            For example, in a CSV format, *'\\n'* is the typical row delimiter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-csvmappingparameters.html#cfn-kinesisanalytics-applicationreferencedatasource-csvmappingparameters-recordrowdelimiter
            '''
            result = self._values.get("record_row_delimiter")
            assert result is not None, "Required property 'record_row_delimiter' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CSVMappingParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationReferenceDataSource.JSONMappingParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"record_row_path": "recordRowPath"},
    )
    class JSONMappingParametersProperty:
        def __init__(self, *, record_row_path: builtins.str) -> None:
            '''Provides additional mapping information when JSON is the record format on the streaming source.

            :param record_row_path: Path to the top-level parent that contains the records.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-jsonmappingparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                j_sONMapping_parameters_property = kinesisanalytics.CfnApplicationReferenceDataSource.JSONMappingParametersProperty(
                    record_row_path="recordRowPath"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__24b04b499ed866076d6ce95ccc747c7667940b9bff6a2e8109c0744ff90310ba)
                check_type(argname="argument record_row_path", value=record_row_path, expected_type=type_hints["record_row_path"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "record_row_path": record_row_path,
            }

        @builtins.property
        def record_row_path(self) -> builtins.str:
            '''Path to the top-level parent that contains the records.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-jsonmappingparameters.html#cfn-kinesisanalytics-applicationreferencedatasource-jsonmappingparameters-recordrowpath
            '''
            result = self._values.get("record_row_path")
            assert result is not None, "Required property 'record_row_path' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JSONMappingParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationReferenceDataSource.MappingParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "csv_mapping_parameters": "csvMappingParameters",
            "json_mapping_parameters": "jsonMappingParameters",
        },
    )
    class MappingParametersProperty:
        def __init__(
            self,
            *,
            csv_mapping_parameters: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationReferenceDataSource.CSVMappingParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            json_mapping_parameters: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationReferenceDataSource.JSONMappingParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''When configuring application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

            :param csv_mapping_parameters: Provides additional mapping information when the record format uses delimiters (for example, CSV).
            :param json_mapping_parameters: Provides additional mapping information when JSON is the record format on the streaming source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-mappingparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                mapping_parameters_property = kinesisanalytics.CfnApplicationReferenceDataSource.MappingParametersProperty(
                    csv_mapping_parameters=kinesisanalytics.CfnApplicationReferenceDataSource.CSVMappingParametersProperty(
                        record_column_delimiter="recordColumnDelimiter",
                        record_row_delimiter="recordRowDelimiter"
                    ),
                    json_mapping_parameters=kinesisanalytics.CfnApplicationReferenceDataSource.JSONMappingParametersProperty(
                        record_row_path="recordRowPath"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__96af8c039b9c6385ba901e70d0aea360c88d50b0d6adba0a02eb254e568d13d8)
                check_type(argname="argument csv_mapping_parameters", value=csv_mapping_parameters, expected_type=type_hints["csv_mapping_parameters"])
                check_type(argname="argument json_mapping_parameters", value=json_mapping_parameters, expected_type=type_hints["json_mapping_parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if csv_mapping_parameters is not None:
                self._values["csv_mapping_parameters"] = csv_mapping_parameters
            if json_mapping_parameters is not None:
                self._values["json_mapping_parameters"] = json_mapping_parameters

        @builtins.property
        def csv_mapping_parameters(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationReferenceDataSource.CSVMappingParametersProperty"]]:
            '''Provides additional mapping information when the record format uses delimiters (for example, CSV).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-mappingparameters.html#cfn-kinesisanalytics-applicationreferencedatasource-mappingparameters-csvmappingparameters
            '''
            result = self._values.get("csv_mapping_parameters")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationReferenceDataSource.CSVMappingParametersProperty"]], result)

        @builtins.property
        def json_mapping_parameters(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationReferenceDataSource.JSONMappingParametersProperty"]]:
            '''Provides additional mapping information when JSON is the record format on the streaming source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-mappingparameters.html#cfn-kinesisanalytics-applicationreferencedatasource-mappingparameters-jsonmappingparameters
            '''
            result = self._values.get("json_mapping_parameters")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationReferenceDataSource.JSONMappingParametersProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MappingParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationReferenceDataSource.RecordColumnProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "sql_type": "sqlType", "mapping": "mapping"},
    )
    class RecordColumnProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            sql_type: builtins.str,
            mapping: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.

            Also used to describe the format of the reference data source.

            :param name: Name of the column created in the in-application input stream or reference table.
            :param sql_type: Type of column created in the in-application input stream or reference table.
            :param mapping: Reference to the data element in the streaming input or the reference data source. This element is required if the `RecordFormatType <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_RecordFormat.html#analytics-Type-RecordFormat-RecordFormatTypel>`_ is ``JSON`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-recordcolumn.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                record_column_property = kinesisanalytics.CfnApplicationReferenceDataSource.RecordColumnProperty(
                    name="name",
                    sql_type="sqlType",
                
                    # the properties below are optional
                    mapping="mapping"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e5aa4a67ad65a86ce398eef47607af181e7f0fdea5ee51cfbede2fd6d9f1c274)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument sql_type", value=sql_type, expected_type=type_hints["sql_type"])
                check_type(argname="argument mapping", value=mapping, expected_type=type_hints["mapping"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "sql_type": sql_type,
            }
            if mapping is not None:
                self._values["mapping"] = mapping

        @builtins.property
        def name(self) -> builtins.str:
            '''Name of the column created in the in-application input stream or reference table.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-recordcolumn.html#cfn-kinesisanalytics-applicationreferencedatasource-recordcolumn-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def sql_type(self) -> builtins.str:
            '''Type of column created in the in-application input stream or reference table.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-recordcolumn.html#cfn-kinesisanalytics-applicationreferencedatasource-recordcolumn-sqltype
            '''
            result = self._values.get("sql_type")
            assert result is not None, "Required property 'sql_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def mapping(self) -> typing.Optional[builtins.str]:
            '''Reference to the data element in the streaming input or the reference data source.

            This element is required if the `RecordFormatType <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_RecordFormat.html#analytics-Type-RecordFormat-RecordFormatTypel>`_ is ``JSON`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-recordcolumn.html#cfn-kinesisanalytics-applicationreferencedatasource-recordcolumn-mapping
            '''
            result = self._values.get("mapping")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RecordColumnProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationReferenceDataSource.RecordFormatProperty",
        jsii_struct_bases=[],
        name_mapping={
            "record_format_type": "recordFormatType",
            "mapping_parameters": "mappingParameters",
        },
    )
    class RecordFormatProperty:
        def __init__(
            self,
            *,
            record_format_type: builtins.str,
            mapping_parameters: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationReferenceDataSource.MappingParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Describes the record format and relevant mapping information that should be applied to schematize the records on the stream.

            :param record_format_type: The type of record format.
            :param mapping_parameters: When configuring application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-recordformat.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                record_format_property = kinesisanalytics.CfnApplicationReferenceDataSource.RecordFormatProperty(
                    record_format_type="recordFormatType",
                
                    # the properties below are optional
                    mapping_parameters=kinesisanalytics.CfnApplicationReferenceDataSource.MappingParametersProperty(
                        csv_mapping_parameters=kinesisanalytics.CfnApplicationReferenceDataSource.CSVMappingParametersProperty(
                            record_column_delimiter="recordColumnDelimiter",
                            record_row_delimiter="recordRowDelimiter"
                        ),
                        json_mapping_parameters=kinesisanalytics.CfnApplicationReferenceDataSource.JSONMappingParametersProperty(
                            record_row_path="recordRowPath"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cd14c1b93e0f993cc2c3576391f0e9fa3c5ba4e10c6deed7c679c30122afd5dd)
                check_type(argname="argument record_format_type", value=record_format_type, expected_type=type_hints["record_format_type"])
                check_type(argname="argument mapping_parameters", value=mapping_parameters, expected_type=type_hints["mapping_parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "record_format_type": record_format_type,
            }
            if mapping_parameters is not None:
                self._values["mapping_parameters"] = mapping_parameters

        @builtins.property
        def record_format_type(self) -> builtins.str:
            '''The type of record format.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-recordformat.html#cfn-kinesisanalytics-applicationreferencedatasource-recordformat-recordformattype
            '''
            result = self._values.get("record_format_type")
            assert result is not None, "Required property 'record_format_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def mapping_parameters(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationReferenceDataSource.MappingParametersProperty"]]:
            '''When configuring application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-recordformat.html#cfn-kinesisanalytics-applicationreferencedatasource-recordformat-mappingparameters
            '''
            result = self._values.get("mapping_parameters")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationReferenceDataSource.MappingParametersProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RecordFormatProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationReferenceDataSource.ReferenceDataSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "reference_schema": "referenceSchema",
            "s3_reference_data_source": "s3ReferenceDataSource",
            "table_name": "tableName",
        },
    )
    class ReferenceDataSourceProperty:
        def __init__(
            self,
            *,
            reference_schema: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationReferenceDataSource.ReferenceSchemaProperty", typing.Dict[builtins.str, typing.Any]]],
            s3_reference_data_source: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationReferenceDataSource.S3ReferenceDataSourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            table_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes the reference data source by providing the source information (S3 bucket name and object key name), the resulting in-application table name that is created, and the necessary schema to map the data elements in the Amazon S3 object to the in-application table.

            :param reference_schema: Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.
            :param s3_reference_data_source: Identifies the S3 bucket and object that contains the reference data. Also identifies the IAM role Amazon Kinesis Analytics can assume to read this object on your behalf. An Amazon Kinesis Analytics application loads reference data only once. If the data changes, you call the ``UpdateApplication`` operation to trigger reloading of data into your application.
            :param table_name: Name of the in-application table to create.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referencedatasource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                reference_data_source_property = kinesisanalytics.CfnApplicationReferenceDataSource.ReferenceDataSourceProperty(
                    reference_schema=kinesisanalytics.CfnApplicationReferenceDataSource.ReferenceSchemaProperty(
                        record_columns=[kinesisanalytics.CfnApplicationReferenceDataSource.RecordColumnProperty(
                            name="name",
                            sql_type="sqlType",
                
                            # the properties below are optional
                            mapping="mapping"
                        )],
                        record_format=kinesisanalytics.CfnApplicationReferenceDataSource.RecordFormatProperty(
                            record_format_type="recordFormatType",
                
                            # the properties below are optional
                            mapping_parameters=kinesisanalytics.CfnApplicationReferenceDataSource.MappingParametersProperty(
                                csv_mapping_parameters=kinesisanalytics.CfnApplicationReferenceDataSource.CSVMappingParametersProperty(
                                    record_column_delimiter="recordColumnDelimiter",
                                    record_row_delimiter="recordRowDelimiter"
                                ),
                                json_mapping_parameters=kinesisanalytics.CfnApplicationReferenceDataSource.JSONMappingParametersProperty(
                                    record_row_path="recordRowPath"
                                )
                            )
                        ),
                
                        # the properties below are optional
                        record_encoding="recordEncoding"
                    ),
                
                    # the properties below are optional
                    s3_reference_data_source=kinesisanalytics.CfnApplicationReferenceDataSource.S3ReferenceDataSourceProperty(
                        bucket_arn="bucketArn",
                        file_key="fileKey",
                        reference_role_arn="referenceRoleArn"
                    ),
                    table_name="tableName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f77b3888c90d63141853bf991c0930bcc10902696a82fd88fe5dec4452cdd85e)
                check_type(argname="argument reference_schema", value=reference_schema, expected_type=type_hints["reference_schema"])
                check_type(argname="argument s3_reference_data_source", value=s3_reference_data_source, expected_type=type_hints["s3_reference_data_source"])
                check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "reference_schema": reference_schema,
            }
            if s3_reference_data_source is not None:
                self._values["s3_reference_data_source"] = s3_reference_data_source
            if table_name is not None:
                self._values["table_name"] = table_name

        @builtins.property
        def reference_schema(
            self,
        ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationReferenceDataSource.ReferenceSchemaProperty"]:
            '''Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-referencedatasource-referenceschema
            '''
            result = self._values.get("reference_schema")
            assert result is not None, "Required property 'reference_schema' is missing"
            return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationReferenceDataSource.ReferenceSchemaProperty"], result)

        @builtins.property
        def s3_reference_data_source(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationReferenceDataSource.S3ReferenceDataSourceProperty"]]:
            '''Identifies the S3 bucket and object that contains the reference data.

            Also identifies the IAM role Amazon Kinesis Analytics can assume to read this object on your behalf. An Amazon Kinesis Analytics application loads reference data only once. If the data changes, you call the ``UpdateApplication`` operation to trigger reloading of data into your application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-referencedatasource-s3referencedatasource
            '''
            result = self._values.get("s3_reference_data_source")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationReferenceDataSource.S3ReferenceDataSourceProperty"]], result)

        @builtins.property
        def table_name(self) -> typing.Optional[builtins.str]:
            '''Name of the in-application table to create.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-referencedatasource-tablename
            '''
            result = self._values.get("table_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ReferenceDataSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationReferenceDataSource.ReferenceSchemaProperty",
        jsii_struct_bases=[],
        name_mapping={
            "record_columns": "recordColumns",
            "record_format": "recordFormat",
            "record_encoding": "recordEncoding",
        },
    )
    class ReferenceSchemaProperty:
        def __init__(
            self,
            *,
            record_columns: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationReferenceDataSource.RecordColumnProperty", typing.Dict[builtins.str, typing.Any]]]]],
            record_format: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationReferenceDataSource.RecordFormatProperty", typing.Dict[builtins.str, typing.Any]]],
            record_encoding: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ReferenceSchema property type specifies the format of the data in the reference source for a SQL-based Amazon Kinesis Data Analytics application.

            :param record_columns: A list of RecordColumn objects.
            :param record_format: Specifies the format of the records on the reference source.
            :param record_encoding: Specifies the encoding of the records in the reference source. For example, UTF-8.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referenceschema.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                reference_schema_property = kinesisanalytics.CfnApplicationReferenceDataSource.ReferenceSchemaProperty(
                    record_columns=[kinesisanalytics.CfnApplicationReferenceDataSource.RecordColumnProperty(
                        name="name",
                        sql_type="sqlType",
                
                        # the properties below are optional
                        mapping="mapping"
                    )],
                    record_format=kinesisanalytics.CfnApplicationReferenceDataSource.RecordFormatProperty(
                        record_format_type="recordFormatType",
                
                        # the properties below are optional
                        mapping_parameters=kinesisanalytics.CfnApplicationReferenceDataSource.MappingParametersProperty(
                            csv_mapping_parameters=kinesisanalytics.CfnApplicationReferenceDataSource.CSVMappingParametersProperty(
                                record_column_delimiter="recordColumnDelimiter",
                                record_row_delimiter="recordRowDelimiter"
                            ),
                            json_mapping_parameters=kinesisanalytics.CfnApplicationReferenceDataSource.JSONMappingParametersProperty(
                                record_row_path="recordRowPath"
                            )
                        )
                    ),
                
                    # the properties below are optional
                    record_encoding="recordEncoding"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0284401ad93061471f850b937fd451f07a4368ec180aab1819e549c069cce9c5)
                check_type(argname="argument record_columns", value=record_columns, expected_type=type_hints["record_columns"])
                check_type(argname="argument record_format", value=record_format, expected_type=type_hints["record_format"])
                check_type(argname="argument record_encoding", value=record_encoding, expected_type=type_hints["record_encoding"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "record_columns": record_columns,
                "record_format": record_format,
            }
            if record_encoding is not None:
                self._values["record_encoding"] = record_encoding

        @builtins.property
        def record_columns(
            self,
        ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationReferenceDataSource.RecordColumnProperty"]]]:
            '''A list of RecordColumn objects.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referenceschema.html#cfn-kinesisanalytics-applicationreferencedatasource-referenceschema-recordcolumns
            '''
            result = self._values.get("record_columns")
            assert result is not None, "Required property 'record_columns' is missing"
            return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationReferenceDataSource.RecordColumnProperty"]]], result)

        @builtins.property
        def record_format(
            self,
        ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationReferenceDataSource.RecordFormatProperty"]:
            '''Specifies the format of the records on the reference source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referenceschema.html#cfn-kinesisanalytics-applicationreferencedatasource-referenceschema-recordformat
            '''
            result = self._values.get("record_format")
            assert result is not None, "Required property 'record_format' is missing"
            return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationReferenceDataSource.RecordFormatProperty"], result)

        @builtins.property
        def record_encoding(self) -> typing.Optional[builtins.str]:
            '''Specifies the encoding of the records in the reference source.

            For example, UTF-8.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referenceschema.html#cfn-kinesisanalytics-applicationreferencedatasource-referenceschema-recordencoding
            '''
            result = self._values.get("record_encoding")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ReferenceSchemaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationReferenceDataSource.S3ReferenceDataSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket_arn": "bucketArn",
            "file_key": "fileKey",
            "reference_role_arn": "referenceRoleArn",
        },
    )
    class S3ReferenceDataSourceProperty:
        def __init__(
            self,
            *,
            bucket_arn: builtins.str,
            file_key: builtins.str,
            reference_role_arn: builtins.str,
        ) -> None:
            '''Identifies the S3 bucket and object that contains the reference data.

            Also identifies the IAM role Amazon Kinesis Analytics can assume to read this object on your behalf.

            An Amazon Kinesis Analytics application loads reference data only once. If the data changes, you call the `UpdateApplication <https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_UpdateApplication.html>`_ operation to trigger reloading of data into your application.

            :param bucket_arn: Amazon Resource Name (ARN) of the S3 bucket.
            :param file_key: Object key name containing reference data.
            :param reference_role_arn: ARN of the IAM role that the service can assume to read data on your behalf. This role must have permission for the ``s3:GetObject`` action on the object and trust policy that allows Amazon Kinesis Analytics service principal to assume this role.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-s3referencedatasource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                s3_reference_data_source_property = kinesisanalytics.CfnApplicationReferenceDataSource.S3ReferenceDataSourceProperty(
                    bucket_arn="bucketArn",
                    file_key="fileKey",
                    reference_role_arn="referenceRoleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3f6f75dbfa630f90e100fa5681be0776acb38c9a1b7bda1533304ff3a7ff2aa2)
                check_type(argname="argument bucket_arn", value=bucket_arn, expected_type=type_hints["bucket_arn"])
                check_type(argname="argument file_key", value=file_key, expected_type=type_hints["file_key"])
                check_type(argname="argument reference_role_arn", value=reference_role_arn, expected_type=type_hints["reference_role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket_arn": bucket_arn,
                "file_key": file_key,
                "reference_role_arn": reference_role_arn,
            }

        @builtins.property
        def bucket_arn(self) -> builtins.str:
            '''Amazon Resource Name (ARN) of the S3 bucket.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-s3referencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-s3referencedatasource-bucketarn
            '''
            result = self._values.get("bucket_arn")
            assert result is not None, "Required property 'bucket_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def file_key(self) -> builtins.str:
            '''Object key name containing reference data.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-s3referencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-s3referencedatasource-filekey
            '''
            result = self._values.get("file_key")
            assert result is not None, "Required property 'file_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def reference_role_arn(self) -> builtins.str:
            '''ARN of the IAM role that the service can assume to read data on your behalf.

            This role must have permission for the ``s3:GetObject`` action on the object and trust policy that allows Amazon Kinesis Analytics service principal to assume this role.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-s3referencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-s3referencedatasource-referencerolearn
            '''
            result = self._values.get("reference_role_arn")
            assert result is not None, "Required property 'reference_role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3ReferenceDataSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationReferenceDataSourceProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_name": "applicationName",
        "reference_data_source": "referenceDataSource",
    },
)
class CfnApplicationReferenceDataSourceProps:
    def __init__(
        self,
        *,
        application_name: builtins.str,
        reference_data_source: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationReferenceDataSource.ReferenceDataSourceProperty, typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Properties for defining a ``CfnApplicationReferenceDataSource``.

        :param application_name: Name of an existing application.
        :param reference_data_source: The reference data source can be an object in your Amazon S3 bucket. Amazon Kinesis Analytics reads the object and copies the data into the in-application table that is created. You provide an S3 bucket, object key name, and the resulting in-application table that is created. You must also provide an IAM role with the necessary permissions that Amazon Kinesis Analytics can assume to read the object from your S3 bucket on your behalf.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationreferencedatasource.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_kinesisanalytics as kinesisanalytics
            
            cfn_application_reference_data_source_props = kinesisanalytics.CfnApplicationReferenceDataSourceProps(
                application_name="applicationName",
                reference_data_source=kinesisanalytics.CfnApplicationReferenceDataSource.ReferenceDataSourceProperty(
                    reference_schema=kinesisanalytics.CfnApplicationReferenceDataSource.ReferenceSchemaProperty(
                        record_columns=[kinesisanalytics.CfnApplicationReferenceDataSource.RecordColumnProperty(
                            name="name",
                            sql_type="sqlType",
            
                            # the properties below are optional
                            mapping="mapping"
                        )],
                        record_format=kinesisanalytics.CfnApplicationReferenceDataSource.RecordFormatProperty(
                            record_format_type="recordFormatType",
            
                            # the properties below are optional
                            mapping_parameters=kinesisanalytics.CfnApplicationReferenceDataSource.MappingParametersProperty(
                                csv_mapping_parameters=kinesisanalytics.CfnApplicationReferenceDataSource.CSVMappingParametersProperty(
                                    record_column_delimiter="recordColumnDelimiter",
                                    record_row_delimiter="recordRowDelimiter"
                                ),
                                json_mapping_parameters=kinesisanalytics.CfnApplicationReferenceDataSource.JSONMappingParametersProperty(
                                    record_row_path="recordRowPath"
                                )
                            )
                        ),
            
                        # the properties below are optional
                        record_encoding="recordEncoding"
                    ),
            
                    # the properties below are optional
                    s3_reference_data_source=kinesisanalytics.CfnApplicationReferenceDataSource.S3ReferenceDataSourceProperty(
                        bucket_arn="bucketArn",
                        file_key="fileKey",
                        reference_role_arn="referenceRoleArn"
                    ),
                    table_name="tableName"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92a8527f2427122a8173207c8e9888711aec44d7da2255b630415cd609b8c6b6)
            check_type(argname="argument application_name", value=application_name, expected_type=type_hints["application_name"])
            check_type(argname="argument reference_data_source", value=reference_data_source, expected_type=type_hints["reference_data_source"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_name": application_name,
            "reference_data_source": reference_data_source,
        }

    @builtins.property
    def application_name(self) -> builtins.str:
        '''Name of an existing application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationreferencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-applicationname
        '''
        result = self._values.get("application_name")
        assert result is not None, "Required property 'application_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def reference_data_source(
        self,
    ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnApplicationReferenceDataSource.ReferenceDataSourceProperty]:
        '''The reference data source can be an object in your Amazon S3 bucket.

        Amazon Kinesis Analytics reads the object and copies the data into the in-application table that is created. You provide an S3 bucket, object key name, and the resulting in-application table that is created. You must also provide an IAM role with the necessary permissions that Amazon Kinesis Analytics can assume to read the object from your S3 bucket on your behalf.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationreferencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-referencedatasource
        '''
        result = self._values.get("reference_data_source")
        assert result is not None, "Required property 'reference_data_source' is missing"
        return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnApplicationReferenceDataSource.ReferenceDataSourceProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationReferenceDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnApplicationReferenceDataSourceV2(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationReferenceDataSourceV2",
):
    '''A CloudFormation ``AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource``.

    Adds a reference data source to an existing SQL-based Kinesis Data Analytics application.

    Kinesis Data Analytics reads reference data (that is, an Amazon S3 object) and creates an in-application table within your application. In the request, you provide the source (S3 bucket name and object key name), name of the in-application table to create, and the necessary mapping information that describes how data in an Amazon S3 object maps to columns in the resulting in-application table.

    :cloudformationResource: AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationreferencedatasource.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_kinesisanalytics as kinesisanalytics
        
        cfn_application_reference_data_source_v2 = kinesisanalytics.CfnApplicationReferenceDataSourceV2(self, "MyCfnApplicationReferenceDataSourceV2",
            application_name="applicationName",
            reference_data_source=kinesisanalytics.CfnApplicationReferenceDataSourceV2.ReferenceDataSourceProperty(
                reference_schema=kinesisanalytics.CfnApplicationReferenceDataSourceV2.ReferenceSchemaProperty(
                    record_columns=[kinesisanalytics.CfnApplicationReferenceDataSourceV2.RecordColumnProperty(
                        name="name",
                        sql_type="sqlType",
        
                        # the properties below are optional
                        mapping="mapping"
                    )],
                    record_format=kinesisanalytics.CfnApplicationReferenceDataSourceV2.RecordFormatProperty(
                        record_format_type="recordFormatType",
        
                        # the properties below are optional
                        mapping_parameters=kinesisanalytics.CfnApplicationReferenceDataSourceV2.MappingParametersProperty(
                            csv_mapping_parameters=kinesisanalytics.CfnApplicationReferenceDataSourceV2.CSVMappingParametersProperty(
                                record_column_delimiter="recordColumnDelimiter",
                                record_row_delimiter="recordRowDelimiter"
                            ),
                            json_mapping_parameters=kinesisanalytics.CfnApplicationReferenceDataSourceV2.JSONMappingParametersProperty(
                                record_row_path="recordRowPath"
                            )
                        )
                    ),
        
                    # the properties below are optional
                    record_encoding="recordEncoding"
                ),
        
                # the properties below are optional
                s3_reference_data_source=kinesisanalytics.CfnApplicationReferenceDataSourceV2.S3ReferenceDataSourceProperty(
                    bucket_arn="bucketArn",
                    file_key="fileKey"
                ),
                table_name="tableName"
            )
        )
    '''

    def __init__(
        self,
        scope: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        application_name: builtins.str,
        reference_data_source: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationReferenceDataSourceV2.ReferenceDataSourceProperty", typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Create a new ``AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param application_name: The name of the application.
        :param reference_data_source: For a SQL-based Kinesis Data Analytics application, describes the reference data source by providing the source information (Amazon S3 bucket name and object key name), the resulting in-application table name that is created, and the necessary schema to map the data elements in the Amazon S3 object to the in-application table.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24bc9def8c3de881e5cf426f42df5cf0bd4fa4aec91c12f7d97b7f67feb820be)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApplicationReferenceDataSourceV2Props(
            application_name=application_name,
            reference_data_source=reference_data_source,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20be1b39b2c9885d7b363da733146e5f4d406da6505570f00a3ef6c536ca3b00)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4af076368f1ce80003383d92ba56cc8d6e1a7371daff88bc595eb4c668e2c1fb)
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
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> builtins.str:
        '''The name of the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationreferencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-applicationname
        '''
        return typing.cast(builtins.str, jsii.get(self, "applicationName"))

    @application_name.setter
    def application_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__426041050bbd9563ce605756c50b2a58518fe882f0643cd6a9d9668c01610286)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationName", value)

    @builtins.property
    @jsii.member(jsii_name="referenceDataSource")
    def reference_data_source(
        self,
    ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationReferenceDataSourceV2.ReferenceDataSourceProperty"]:
        '''For a SQL-based Kinesis Data Analytics application, describes the reference data source by providing the source information (Amazon S3 bucket name and object key name), the resulting in-application table name that is created, and the necessary schema to map the data elements in the Amazon S3 object to the in-application table.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationreferencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource
        '''
        return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationReferenceDataSourceV2.ReferenceDataSourceProperty"], jsii.get(self, "referenceDataSource"))

    @reference_data_source.setter
    def reference_data_source(
        self,
        value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationReferenceDataSourceV2.ReferenceDataSourceProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05a8e39fad9c7cf863fabb2e166b301cbd52e0fb17de9403fca4ffccfd2c1863)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "referenceDataSource", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationReferenceDataSourceV2.CSVMappingParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "record_column_delimiter": "recordColumnDelimiter",
            "record_row_delimiter": "recordRowDelimiter",
        },
    )
    class CSVMappingParametersProperty:
        def __init__(
            self,
            *,
            record_column_delimiter: builtins.str,
            record_row_delimiter: builtins.str,
        ) -> None:
            '''For a SQL-based Kinesis Data Analytics application, provides additional mapping information when the record format uses delimiters, such as CSV.

            For example, the following sample records use CSV format, where the records use the *'\\n'* as the row delimiter and a comma (",") as the column delimiter:

            ``"name1", "address1"``

            ``"name2", "address2"``

            :param record_column_delimiter: The column delimiter. For example, in a CSV format, a comma (",") is the typical column delimiter.
            :param record_row_delimiter: The row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-csvmappingparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                c_sVMapping_parameters_property = kinesisanalytics.CfnApplicationReferenceDataSourceV2.CSVMappingParametersProperty(
                    record_column_delimiter="recordColumnDelimiter",
                    record_row_delimiter="recordRowDelimiter"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4646d32b18f2793a3efd4056b74bc1abb82850fe640ec2088423e5b9e355535b)
                check_type(argname="argument record_column_delimiter", value=record_column_delimiter, expected_type=type_hints["record_column_delimiter"])
                check_type(argname="argument record_row_delimiter", value=record_row_delimiter, expected_type=type_hints["record_row_delimiter"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "record_column_delimiter": record_column_delimiter,
                "record_row_delimiter": record_row_delimiter,
            }

        @builtins.property
        def record_column_delimiter(self) -> builtins.str:
            '''The column delimiter.

            For example, in a CSV format, a comma (",") is the typical column delimiter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-csvmappingparameters.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-csvmappingparameters-recordcolumndelimiter
            '''
            result = self._values.get("record_column_delimiter")
            assert result is not None, "Required property 'record_column_delimiter' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def record_row_delimiter(self) -> builtins.str:
            '''The row delimiter.

            For example, in a CSV format, *'\\n'* is the typical row delimiter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-csvmappingparameters.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-csvmappingparameters-recordrowdelimiter
            '''
            result = self._values.get("record_row_delimiter")
            assert result is not None, "Required property 'record_row_delimiter' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CSVMappingParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationReferenceDataSourceV2.JSONMappingParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"record_row_path": "recordRowPath"},
    )
    class JSONMappingParametersProperty:
        def __init__(self, *, record_row_path: builtins.str) -> None:
            '''For a SQL-based Kinesis Data Analytics application, provides additional mapping information when JSON is the record format on the streaming source.

            :param record_row_path: The path to the top-level parent that contains the records.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-jsonmappingparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                j_sONMapping_parameters_property = kinesisanalytics.CfnApplicationReferenceDataSourceV2.JSONMappingParametersProperty(
                    record_row_path="recordRowPath"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e8cd316cebf5f1bbe2f0206dcdb7cf88b9884704079071b0f6001f1106a0bc23)
                check_type(argname="argument record_row_path", value=record_row_path, expected_type=type_hints["record_row_path"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "record_row_path": record_row_path,
            }

        @builtins.property
        def record_row_path(self) -> builtins.str:
            '''The path to the top-level parent that contains the records.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-jsonmappingparameters.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-jsonmappingparameters-recordrowpath
            '''
            result = self._values.get("record_row_path")
            assert result is not None, "Required property 'record_row_path' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JSONMappingParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationReferenceDataSourceV2.MappingParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "csv_mapping_parameters": "csvMappingParameters",
            "json_mapping_parameters": "jsonMappingParameters",
        },
    )
    class MappingParametersProperty:
        def __init__(
            self,
            *,
            csv_mapping_parameters: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationReferenceDataSourceV2.CSVMappingParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            json_mapping_parameters: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationReferenceDataSourceV2.JSONMappingParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''When you configure a SQL-based Kinesis Data Analytics application's input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

            :param csv_mapping_parameters: Provides additional mapping information when the record format uses delimiters (for example, CSV).
            :param json_mapping_parameters: Provides additional mapping information when JSON is the record format on the streaming source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-mappingparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                mapping_parameters_property = kinesisanalytics.CfnApplicationReferenceDataSourceV2.MappingParametersProperty(
                    csv_mapping_parameters=kinesisanalytics.CfnApplicationReferenceDataSourceV2.CSVMappingParametersProperty(
                        record_column_delimiter="recordColumnDelimiter",
                        record_row_delimiter="recordRowDelimiter"
                    ),
                    json_mapping_parameters=kinesisanalytics.CfnApplicationReferenceDataSourceV2.JSONMappingParametersProperty(
                        record_row_path="recordRowPath"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f6289c96578bc463c638bff60a3e3c713e3200113b6b491684214db8ea85bad4)
                check_type(argname="argument csv_mapping_parameters", value=csv_mapping_parameters, expected_type=type_hints["csv_mapping_parameters"])
                check_type(argname="argument json_mapping_parameters", value=json_mapping_parameters, expected_type=type_hints["json_mapping_parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if csv_mapping_parameters is not None:
                self._values["csv_mapping_parameters"] = csv_mapping_parameters
            if json_mapping_parameters is not None:
                self._values["json_mapping_parameters"] = json_mapping_parameters

        @builtins.property
        def csv_mapping_parameters(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationReferenceDataSourceV2.CSVMappingParametersProperty"]]:
            '''Provides additional mapping information when the record format uses delimiters (for example, CSV).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-mappingparameters.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-mappingparameters-csvmappingparameters
            '''
            result = self._values.get("csv_mapping_parameters")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationReferenceDataSourceV2.CSVMappingParametersProperty"]], result)

        @builtins.property
        def json_mapping_parameters(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationReferenceDataSourceV2.JSONMappingParametersProperty"]]:
            '''Provides additional mapping information when JSON is the record format on the streaming source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-mappingparameters.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-mappingparameters-jsonmappingparameters
            '''
            result = self._values.get("json_mapping_parameters")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationReferenceDataSourceV2.JSONMappingParametersProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MappingParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationReferenceDataSourceV2.RecordColumnProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "sql_type": "sqlType", "mapping": "mapping"},
    )
    class RecordColumnProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            sql_type: builtins.str,
            mapping: typing.Optional[builtins.str] = None,
        ) -> None:
            '''For a SQL-based Kinesis Data Analytics application, describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.

            Also used to describe the format of the reference data source.

            :param name: The name of the column that is created in the in-application input stream or reference table.
            :param sql_type: The type of column created in the in-application input stream or reference table.
            :param mapping: A reference to the data element in the streaming input or the reference data source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                record_column_property = kinesisanalytics.CfnApplicationReferenceDataSourceV2.RecordColumnProperty(
                    name="name",
                    sql_type="sqlType",
                
                    # the properties below are optional
                    mapping="mapping"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__235f04e21304f85ec348f9a1c6ab176c37acba60aa0aaf642a6747595fa3406d)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument sql_type", value=sql_type, expected_type=type_hints["sql_type"])
                check_type(argname="argument mapping", value=mapping, expected_type=type_hints["mapping"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "sql_type": sql_type,
            }
            if mapping is not None:
                self._values["mapping"] = mapping

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the column that is created in the in-application input stream or reference table.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def sql_type(self) -> builtins.str:
            '''The type of column created in the in-application input stream or reference table.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn-sqltype
            '''
            result = self._values.get("sql_type")
            assert result is not None, "Required property 'sql_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def mapping(self) -> typing.Optional[builtins.str]:
            '''A reference to the data element in the streaming input or the reference data source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn-mapping
            '''
            result = self._values.get("mapping")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RecordColumnProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationReferenceDataSourceV2.RecordFormatProperty",
        jsii_struct_bases=[],
        name_mapping={
            "record_format_type": "recordFormatType",
            "mapping_parameters": "mappingParameters",
        },
    )
    class RecordFormatProperty:
        def __init__(
            self,
            *,
            record_format_type: builtins.str,
            mapping_parameters: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationReferenceDataSourceV2.MappingParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''For a SQL-based Kinesis Data Analytics application, describes the record format and relevant mapping information that should be applied to schematize the records on the stream.

            :param record_format_type: The type of record format.
            :param mapping_parameters: When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordformat.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                record_format_property = kinesisanalytics.CfnApplicationReferenceDataSourceV2.RecordFormatProperty(
                    record_format_type="recordFormatType",
                
                    # the properties below are optional
                    mapping_parameters=kinesisanalytics.CfnApplicationReferenceDataSourceV2.MappingParametersProperty(
                        csv_mapping_parameters=kinesisanalytics.CfnApplicationReferenceDataSourceV2.CSVMappingParametersProperty(
                            record_column_delimiter="recordColumnDelimiter",
                            record_row_delimiter="recordRowDelimiter"
                        ),
                        json_mapping_parameters=kinesisanalytics.CfnApplicationReferenceDataSourceV2.JSONMappingParametersProperty(
                            record_row_path="recordRowPath"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d9c7e6f72c9d25dfb44c69c3636f4abcf5c4e4e457977af92a0b800d19e85133)
                check_type(argname="argument record_format_type", value=record_format_type, expected_type=type_hints["record_format_type"])
                check_type(argname="argument mapping_parameters", value=mapping_parameters, expected_type=type_hints["mapping_parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "record_format_type": record_format_type,
            }
            if mapping_parameters is not None:
                self._values["mapping_parameters"] = mapping_parameters

        @builtins.property
        def record_format_type(self) -> builtins.str:
            '''The type of record format.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordformat.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-recordformat-recordformattype
            '''
            result = self._values.get("record_format_type")
            assert result is not None, "Required property 'record_format_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def mapping_parameters(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationReferenceDataSourceV2.MappingParametersProperty"]]:
            '''When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordformat.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-recordformat-mappingparameters
            '''
            result = self._values.get("mapping_parameters")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationReferenceDataSourceV2.MappingParametersProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RecordFormatProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationReferenceDataSourceV2.ReferenceDataSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "reference_schema": "referenceSchema",
            "s3_reference_data_source": "s3ReferenceDataSource",
            "table_name": "tableName",
        },
    )
    class ReferenceDataSourceProperty:
        def __init__(
            self,
            *,
            reference_schema: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationReferenceDataSourceV2.ReferenceSchemaProperty", typing.Dict[builtins.str, typing.Any]]],
            s3_reference_data_source: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationReferenceDataSourceV2.S3ReferenceDataSourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            table_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''For a SQL-based Kinesis Data Analytics application, describes the reference data source by providing the source information (Amazon S3 bucket name and object key name), the resulting in-application table name that is created, and the necessary schema to map the data elements in the Amazon S3 object to the in-application table.

            :param reference_schema: Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.
            :param s3_reference_data_source: Identifies the S3 bucket and object that contains the reference data. A Kinesis Data Analytics application loads reference data only once. If the data changes, you call the `UpdateApplication <https://docs.aws.amazon.com/kinesisanalytics/latest/apiv2/API_UpdateApplication.html>`_ operation to trigger reloading of data into your application.
            :param table_name: The name of the in-application table to create.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                reference_data_source_property = kinesisanalytics.CfnApplicationReferenceDataSourceV2.ReferenceDataSourceProperty(
                    reference_schema=kinesisanalytics.CfnApplicationReferenceDataSourceV2.ReferenceSchemaProperty(
                        record_columns=[kinesisanalytics.CfnApplicationReferenceDataSourceV2.RecordColumnProperty(
                            name="name",
                            sql_type="sqlType",
                
                            # the properties below are optional
                            mapping="mapping"
                        )],
                        record_format=kinesisanalytics.CfnApplicationReferenceDataSourceV2.RecordFormatProperty(
                            record_format_type="recordFormatType",
                
                            # the properties below are optional
                            mapping_parameters=kinesisanalytics.CfnApplicationReferenceDataSourceV2.MappingParametersProperty(
                                csv_mapping_parameters=kinesisanalytics.CfnApplicationReferenceDataSourceV2.CSVMappingParametersProperty(
                                    record_column_delimiter="recordColumnDelimiter",
                                    record_row_delimiter="recordRowDelimiter"
                                ),
                                json_mapping_parameters=kinesisanalytics.CfnApplicationReferenceDataSourceV2.JSONMappingParametersProperty(
                                    record_row_path="recordRowPath"
                                )
                            )
                        ),
                
                        # the properties below are optional
                        record_encoding="recordEncoding"
                    ),
                
                    # the properties below are optional
                    s3_reference_data_source=kinesisanalytics.CfnApplicationReferenceDataSourceV2.S3ReferenceDataSourceProperty(
                        bucket_arn="bucketArn",
                        file_key="fileKey"
                    ),
                    table_name="tableName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e7f4fd7833a40d2525cb8872830d87dac80ef1f875c1037e5557053a8d113dff)
                check_type(argname="argument reference_schema", value=reference_schema, expected_type=type_hints["reference_schema"])
                check_type(argname="argument s3_reference_data_source", value=s3_reference_data_source, expected_type=type_hints["s3_reference_data_source"])
                check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "reference_schema": reference_schema,
            }
            if s3_reference_data_source is not None:
                self._values["s3_reference_data_source"] = s3_reference_data_source
            if table_name is not None:
                self._values["table_name"] = table_name

        @builtins.property
        def reference_schema(
            self,
        ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationReferenceDataSourceV2.ReferenceSchemaProperty"]:
            '''Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource-referenceschema
            '''
            result = self._values.get("reference_schema")
            assert result is not None, "Required property 'reference_schema' is missing"
            return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationReferenceDataSourceV2.ReferenceSchemaProperty"], result)

        @builtins.property
        def s3_reference_data_source(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationReferenceDataSourceV2.S3ReferenceDataSourceProperty"]]:
            '''Identifies the S3 bucket and object that contains the reference data.

            A Kinesis Data Analytics application loads reference data only once. If the data changes, you call the `UpdateApplication <https://docs.aws.amazon.com/kinesisanalytics/latest/apiv2/API_UpdateApplication.html>`_ operation to trigger reloading of data into your application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource-s3referencedatasource
            '''
            result = self._values.get("s3_reference_data_source")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationReferenceDataSourceV2.S3ReferenceDataSourceProperty"]], result)

        @builtins.property
        def table_name(self) -> typing.Optional[builtins.str]:
            '''The name of the in-application table to create.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource-tablename
            '''
            result = self._values.get("table_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ReferenceDataSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationReferenceDataSourceV2.ReferenceSchemaProperty",
        jsii_struct_bases=[],
        name_mapping={
            "record_columns": "recordColumns",
            "record_format": "recordFormat",
            "record_encoding": "recordEncoding",
        },
    )
    class ReferenceSchemaProperty:
        def __init__(
            self,
            *,
            record_columns: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationReferenceDataSourceV2.RecordColumnProperty", typing.Dict[builtins.str, typing.Any]]]]],
            record_format: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationReferenceDataSourceV2.RecordFormatProperty", typing.Dict[builtins.str, typing.Any]]],
            record_encoding: typing.Optional[builtins.str] = None,
        ) -> None:
            '''For a SQL-based Kinesis Data Analytics application, describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.

            :param record_columns: A list of ``RecordColumn`` objects.
            :param record_format: Specifies the format of the records on the streaming source.
            :param record_encoding: Specifies the encoding of the records in the streaming source. For example, UTF-8.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referenceschema.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                reference_schema_property = kinesisanalytics.CfnApplicationReferenceDataSourceV2.ReferenceSchemaProperty(
                    record_columns=[kinesisanalytics.CfnApplicationReferenceDataSourceV2.RecordColumnProperty(
                        name="name",
                        sql_type="sqlType",
                
                        # the properties below are optional
                        mapping="mapping"
                    )],
                    record_format=kinesisanalytics.CfnApplicationReferenceDataSourceV2.RecordFormatProperty(
                        record_format_type="recordFormatType",
                
                        # the properties below are optional
                        mapping_parameters=kinesisanalytics.CfnApplicationReferenceDataSourceV2.MappingParametersProperty(
                            csv_mapping_parameters=kinesisanalytics.CfnApplicationReferenceDataSourceV2.CSVMappingParametersProperty(
                                record_column_delimiter="recordColumnDelimiter",
                                record_row_delimiter="recordRowDelimiter"
                            ),
                            json_mapping_parameters=kinesisanalytics.CfnApplicationReferenceDataSourceV2.JSONMappingParametersProperty(
                                record_row_path="recordRowPath"
                            )
                        )
                    ),
                
                    # the properties below are optional
                    record_encoding="recordEncoding"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__71a577f7cef0135eb9474b3547ec0e2a1b3769689b87e57b2b177a9566dbff6a)
                check_type(argname="argument record_columns", value=record_columns, expected_type=type_hints["record_columns"])
                check_type(argname="argument record_format", value=record_format, expected_type=type_hints["record_format"])
                check_type(argname="argument record_encoding", value=record_encoding, expected_type=type_hints["record_encoding"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "record_columns": record_columns,
                "record_format": record_format,
            }
            if record_encoding is not None:
                self._values["record_encoding"] = record_encoding

        @builtins.property
        def record_columns(
            self,
        ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationReferenceDataSourceV2.RecordColumnProperty"]]]:
            '''A list of ``RecordColumn`` objects.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referenceschema.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referenceschema-recordcolumns
            '''
            result = self._values.get("record_columns")
            assert result is not None, "Required property 'record_columns' is missing"
            return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationReferenceDataSourceV2.RecordColumnProperty"]]], result)

        @builtins.property
        def record_format(
            self,
        ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationReferenceDataSourceV2.RecordFormatProperty"]:
            '''Specifies the format of the records on the streaming source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referenceschema.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referenceschema-recordformat
            '''
            result = self._values.get("record_format")
            assert result is not None, "Required property 'record_format' is missing"
            return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationReferenceDataSourceV2.RecordFormatProperty"], result)

        @builtins.property
        def record_encoding(self) -> typing.Optional[builtins.str]:
            '''Specifies the encoding of the records in the streaming source.

            For example, UTF-8.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referenceschema.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referenceschema-recordencoding
            '''
            result = self._values.get("record_encoding")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ReferenceSchemaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationReferenceDataSourceV2.S3ReferenceDataSourceProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket_arn": "bucketArn", "file_key": "fileKey"},
    )
    class S3ReferenceDataSourceProperty:
        def __init__(self, *, bucket_arn: builtins.str, file_key: builtins.str) -> None:
            '''For an SQL-based Amazon Kinesis Data Analytics application, identifies the Amazon S3 bucket and object that contains the reference data.

            A Kinesis Data Analytics application loads reference data only once. If the data changes, you call the `UpdateApplication <https://docs.aws.amazon.com/kinesisanalytics/latest/apiv2/API_UpdateApplication.html>`_ operation to trigger reloading of data into your application.

            :param bucket_arn: The Amazon Resource Name (ARN) of the S3 bucket.
            :param file_key: The object key name containing the reference data.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                s3_reference_data_source_property = kinesisanalytics.CfnApplicationReferenceDataSourceV2.S3ReferenceDataSourceProperty(
                    bucket_arn="bucketArn",
                    file_key="fileKey"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__709b4b4610557c20d1721e1ccc642548825b5f541a00b361c6cfa760095a2266)
                check_type(argname="argument bucket_arn", value=bucket_arn, expected_type=type_hints["bucket_arn"])
                check_type(argname="argument file_key", value=file_key, expected_type=type_hints["file_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket_arn": bucket_arn,
                "file_key": file_key,
            }

        @builtins.property
        def bucket_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the S3 bucket.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource-bucketarn
            '''
            result = self._values.get("bucket_arn")
            assert result is not None, "Required property 'bucket_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def file_key(self) -> builtins.str:
            '''The object key name containing the reference data.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource-filekey
            '''
            result = self._values.get("file_key")
            assert result is not None, "Required property 'file_key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3ReferenceDataSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationReferenceDataSourceV2Props",
    jsii_struct_bases=[],
    name_mapping={
        "application_name": "applicationName",
        "reference_data_source": "referenceDataSource",
    },
)
class CfnApplicationReferenceDataSourceV2Props:
    def __init__(
        self,
        *,
        application_name: builtins.str,
        reference_data_source: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationReferenceDataSourceV2.ReferenceDataSourceProperty, typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Properties for defining a ``CfnApplicationReferenceDataSourceV2``.

        :param application_name: The name of the application.
        :param reference_data_source: For a SQL-based Kinesis Data Analytics application, describes the reference data source by providing the source information (Amazon S3 bucket name and object key name), the resulting in-application table name that is created, and the necessary schema to map the data elements in the Amazon S3 object to the in-application table.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationreferencedatasource.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_kinesisanalytics as kinesisanalytics
            
            cfn_application_reference_data_source_v2_props = kinesisanalytics.CfnApplicationReferenceDataSourceV2Props(
                application_name="applicationName",
                reference_data_source=kinesisanalytics.CfnApplicationReferenceDataSourceV2.ReferenceDataSourceProperty(
                    reference_schema=kinesisanalytics.CfnApplicationReferenceDataSourceV2.ReferenceSchemaProperty(
                        record_columns=[kinesisanalytics.CfnApplicationReferenceDataSourceV2.RecordColumnProperty(
                            name="name",
                            sql_type="sqlType",
            
                            # the properties below are optional
                            mapping="mapping"
                        )],
                        record_format=kinesisanalytics.CfnApplicationReferenceDataSourceV2.RecordFormatProperty(
                            record_format_type="recordFormatType",
            
                            # the properties below are optional
                            mapping_parameters=kinesisanalytics.CfnApplicationReferenceDataSourceV2.MappingParametersProperty(
                                csv_mapping_parameters=kinesisanalytics.CfnApplicationReferenceDataSourceV2.CSVMappingParametersProperty(
                                    record_column_delimiter="recordColumnDelimiter",
                                    record_row_delimiter="recordRowDelimiter"
                                ),
                                json_mapping_parameters=kinesisanalytics.CfnApplicationReferenceDataSourceV2.JSONMappingParametersProperty(
                                    record_row_path="recordRowPath"
                                )
                            )
                        ),
            
                        # the properties below are optional
                        record_encoding="recordEncoding"
                    ),
            
                    # the properties below are optional
                    s3_reference_data_source=kinesisanalytics.CfnApplicationReferenceDataSourceV2.S3ReferenceDataSourceProperty(
                        bucket_arn="bucketArn",
                        file_key="fileKey"
                    ),
                    table_name="tableName"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8abaabd6b0697ff27dcddbc4444c86abc5ce7a20c68c88d8cc56a7749dde3c1d)
            check_type(argname="argument application_name", value=application_name, expected_type=type_hints["application_name"])
            check_type(argname="argument reference_data_source", value=reference_data_source, expected_type=type_hints["reference_data_source"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_name": application_name,
            "reference_data_source": reference_data_source,
        }

    @builtins.property
    def application_name(self) -> builtins.str:
        '''The name of the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationreferencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-applicationname
        '''
        result = self._values.get("application_name")
        assert result is not None, "Required property 'application_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def reference_data_source(
        self,
    ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnApplicationReferenceDataSourceV2.ReferenceDataSourceProperty]:
        '''For a SQL-based Kinesis Data Analytics application, describes the reference data source by providing the source information (Amazon S3 bucket name and object key name), the resulting in-application table name that is created, and the necessary schema to map the data elements in the Amazon S3 object to the in-application table.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationreferencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource
        '''
        result = self._values.get("reference_data_source")
        assert result is not None, "Required property 'reference_data_source' is missing"
        return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnApplicationReferenceDataSourceV2.ReferenceDataSourceProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationReferenceDataSourceV2Props(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnApplicationV2(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2",
):
    '''A CloudFormation ``AWS::KinesisAnalyticsV2::Application``.

    Creates an Amazon Kinesis Data Analytics application. For information about creating a Kinesis Data Analytics application, see `Creating an Application <https://docs.aws.amazon.com/kinesisanalytics/latest/java/getting-started.html>`_ .

    :cloudformationResource: AWS::KinesisAnalyticsV2::Application
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_kinesisanalytics as kinesisanalytics
        
        cfn_application_v2 = kinesisanalytics.CfnApplicationV2(self, "MyCfnApplicationV2",
            runtime_environment="runtimeEnvironment",
            service_execution_role="serviceExecutionRole",
        
            # the properties below are optional
            application_configuration=kinesisanalytics.CfnApplicationV2.ApplicationConfigurationProperty(
                application_code_configuration=kinesisanalytics.CfnApplicationV2.ApplicationCodeConfigurationProperty(
                    code_content=kinesisanalytics.CfnApplicationV2.CodeContentProperty(
                        s3_content_location=kinesisanalytics.CfnApplicationV2.S3ContentLocationProperty(
                            bucket_arn="bucketArn",
                            file_key="fileKey",
        
                            # the properties below are optional
                            object_version="objectVersion"
                        ),
                        text_content="textContent",
                        zip_file_content="zipFileContent"
                    ),
                    code_content_type="codeContentType"
                ),
                application_snapshot_configuration=kinesisanalytics.CfnApplicationV2.ApplicationSnapshotConfigurationProperty(
                    snapshots_enabled=False
                ),
                environment_properties=kinesisanalytics.CfnApplicationV2.EnvironmentPropertiesProperty(
                    property_groups=[kinesisanalytics.CfnApplicationV2.PropertyGroupProperty(
                        property_group_id="propertyGroupId",
                        property_map={
                            "property_map_key": "propertyMap"
                        }
                    )]
                ),
                flink_application_configuration=kinesisanalytics.CfnApplicationV2.FlinkApplicationConfigurationProperty(
                    checkpoint_configuration=kinesisanalytics.CfnApplicationV2.CheckpointConfigurationProperty(
                        configuration_type="configurationType",
        
                        # the properties below are optional
                        checkpointing_enabled=False,
                        checkpoint_interval=123,
                        min_pause_between_checkpoints=123
                    ),
                    monitoring_configuration=kinesisanalytics.CfnApplicationV2.MonitoringConfigurationProperty(
                        configuration_type="configurationType",
        
                        # the properties below are optional
                        log_level="logLevel",
                        metrics_level="metricsLevel"
                    ),
                    parallelism_configuration=kinesisanalytics.CfnApplicationV2.ParallelismConfigurationProperty(
                        configuration_type="configurationType",
        
                        # the properties below are optional
                        auto_scaling_enabled=False,
                        parallelism=123,
                        parallelism_per_kpu=123
                    )
                ),
                sql_application_configuration=kinesisanalytics.CfnApplicationV2.SqlApplicationConfigurationProperty(
                    inputs=[kinesisanalytics.CfnApplicationV2.InputProperty(
                        input_schema=kinesisanalytics.CfnApplicationV2.InputSchemaProperty(
                            record_columns=[kinesisanalytics.CfnApplicationV2.RecordColumnProperty(
                                name="name",
                                sql_type="sqlType",
        
                                # the properties below are optional
                                mapping="mapping"
                            )],
                            record_format=kinesisanalytics.CfnApplicationV2.RecordFormatProperty(
                                record_format_type="recordFormatType",
        
                                # the properties below are optional
                                mapping_parameters=kinesisanalytics.CfnApplicationV2.MappingParametersProperty(
                                    csv_mapping_parameters=kinesisanalytics.CfnApplicationV2.CSVMappingParametersProperty(
                                        record_column_delimiter="recordColumnDelimiter",
                                        record_row_delimiter="recordRowDelimiter"
                                    ),
                                    json_mapping_parameters=kinesisanalytics.CfnApplicationV2.JSONMappingParametersProperty(
                                        record_row_path="recordRowPath"
                                    )
                                )
                            ),
        
                            # the properties below are optional
                            record_encoding="recordEncoding"
                        ),
                        name_prefix="namePrefix",
        
                        # the properties below are optional
                        input_parallelism=kinesisanalytics.CfnApplicationV2.InputParallelismProperty(
                            count=123
                        ),
                        input_processing_configuration=kinesisanalytics.CfnApplicationV2.InputProcessingConfigurationProperty(
                            input_lambda_processor=kinesisanalytics.CfnApplicationV2.InputLambdaProcessorProperty(
                                resource_arn="resourceArn"
                            )
                        ),
                        kinesis_firehose_input=kinesisanalytics.CfnApplicationV2.KinesisFirehoseInputProperty(
                            resource_arn="resourceArn"
                        ),
                        kinesis_streams_input=kinesisanalytics.CfnApplicationV2.KinesisStreamsInputProperty(
                            resource_arn="resourceArn"
                        )
                    )]
                ),
                vpc_configurations=[kinesisanalytics.CfnApplicationV2.VpcConfigurationProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                )],
                zeppelin_application_configuration=kinesisanalytics.CfnApplicationV2.ZeppelinApplicationConfigurationProperty(
                    catalog_configuration=kinesisanalytics.CfnApplicationV2.CatalogConfigurationProperty(
                        glue_data_catalog_configuration=kinesisanalytics.CfnApplicationV2.GlueDataCatalogConfigurationProperty(
                            database_arn="databaseArn"
                        )
                    ),
                    custom_artifacts_configuration=[kinesisanalytics.CfnApplicationV2.CustomArtifactConfigurationProperty(
                        artifact_type="artifactType",
        
                        # the properties below are optional
                        maven_reference=kinesisanalytics.CfnApplicationV2.MavenReferenceProperty(
                            artifact_id="artifactId",
                            group_id="groupId",
                            version="version"
                        ),
                        s3_content_location=kinesisanalytics.CfnApplicationV2.S3ContentLocationProperty(
                            bucket_arn="bucketArn",
                            file_key="fileKey",
        
                            # the properties below are optional
                            object_version="objectVersion"
                        )
                    )],
                    deploy_as_application_configuration=kinesisanalytics.CfnApplicationV2.DeployAsApplicationConfigurationProperty(
                        s3_content_location=kinesisanalytics.CfnApplicationV2.S3ContentBaseLocationProperty(
                            bucket_arn="bucketArn",
        
                            # the properties below are optional
                            base_path="basePath"
                        )
                    ),
                    monitoring_configuration=kinesisanalytics.CfnApplicationV2.ZeppelinMonitoringConfigurationProperty(
                        log_level="logLevel"
                    )
                )
            ),
            application_description="applicationDescription",
            application_maintenance_configuration=kinesisanalytics.CfnApplicationV2.ApplicationMaintenanceConfigurationProperty(
                application_maintenance_window_start_time="applicationMaintenanceWindowStartTime"
            ),
            application_mode="applicationMode",
            application_name="applicationName",
            run_configuration=kinesisanalytics.CfnApplicationV2.RunConfigurationProperty(
                application_restore_configuration=kinesisanalytics.CfnApplicationV2.ApplicationRestoreConfigurationProperty(
                    application_restore_type="applicationRestoreType",
        
                    # the properties below are optional
                    snapshot_name="snapshotName"
                ),
                flink_run_configuration=kinesisanalytics.CfnApplicationV2.FlinkRunConfigurationProperty(
                    allow_non_restored_state=False
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
        scope: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        runtime_environment: builtins.str,
        service_execution_role: builtins.str,
        application_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationV2.ApplicationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        application_description: typing.Optional[builtins.str] = None,
        application_maintenance_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationV2.ApplicationMaintenanceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        application_mode: typing.Optional[builtins.str] = None,
        application_name: typing.Optional[builtins.str] = None,
        run_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationV2.RunConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::KinesisAnalyticsV2::Application``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param runtime_environment: The runtime environment for the application.
        :param service_execution_role: Specifies the IAM role that the application uses to access external resources.
        :param application_configuration: Use this parameter to configure the application.
        :param application_description: The description of the application.
        :param application_maintenance_configuration: ``AWS::KinesisAnalyticsV2::Application.ApplicationMaintenanceConfiguration``.
        :param application_mode: To create a Kinesis Data Analytics Studio notebook, you must set the mode to ``INTERACTIVE`` . However, for a Kinesis Data Analytics for Apache Flink application, the mode is optional.
        :param application_name: The name of the application.
        :param run_configuration: ``AWS::KinesisAnalyticsV2::Application.RunConfiguration``.
        :param tags: A list of one or more tags to assign to the application. A tag is a key-value pair that identifies an application. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9eeabf2dab4475e291f514ae569b69c819c023305785983786a6b8f885c5cd5c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApplicationV2Props(
            runtime_environment=runtime_environment,
            service_execution_role=service_execution_role,
            application_configuration=application_configuration,
            application_description=application_description,
            application_maintenance_configuration=application_maintenance_configuration,
            application_mode=application_mode,
            application_name=application_name,
            run_configuration=run_configuration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ab979335d272b54385ec51a33e6197a1f1bbd114270a16401a86b7ed4fd0729)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5b1296e63ca5206494404f96c01aa8ac377b8c08b77ff4a0a1f5547e4a213f6b)
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
    def tags(self) -> _aws_cdk_core_f4b25747.TagManager:
        '''A list of one or more tags to assign to the application.

        A tag is a key-value pair that identifies an application. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-tags
        '''
        return typing.cast(_aws_cdk_core_f4b25747.TagManager, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="runtimeEnvironment")
    def runtime_environment(self) -> builtins.str:
        '''The runtime environment for the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-runtimeenvironment
        '''
        return typing.cast(builtins.str, jsii.get(self, "runtimeEnvironment"))

    @runtime_environment.setter
    def runtime_environment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea26b50ff4a0040f3d5ca977a91aafa1b52156384f8c8ee00c424e80cfade2e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runtimeEnvironment", value)

    @builtins.property
    @jsii.member(jsii_name="serviceExecutionRole")
    def service_execution_role(self) -> builtins.str:
        '''Specifies the IAM role that the application uses to access external resources.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-serviceexecutionrole
        '''
        return typing.cast(builtins.str, jsii.get(self, "serviceExecutionRole"))

    @service_execution_role.setter
    def service_execution_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1ec6f17b3e294209e152984b223657f15e2bfd642e38670ca405d5129b95ff8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceExecutionRole", value)

    @builtins.property
    @jsii.member(jsii_name="applicationConfiguration")
    def application_configuration(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.ApplicationConfigurationProperty"]]:
        '''Use this parameter to configure the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-applicationconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.ApplicationConfigurationProperty"]], jsii.get(self, "applicationConfiguration"))

    @application_configuration.setter
    def application_configuration(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.ApplicationConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f45255dc18cbc9d974e34c13cbacbcc8a7a597259ee5d9451cce0ff5afb32532)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="applicationDescription")
    def application_description(self) -> typing.Optional[builtins.str]:
        '''The description of the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-applicationdescription
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationDescription"))

    @application_description.setter
    def application_description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7cfac072ac577168ac4b3d35ff60fd0a75316c20bf8230a1e2dc26232a9c2e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationDescription", value)

    @builtins.property
    @jsii.member(jsii_name="applicationMaintenanceConfiguration")
    def application_maintenance_configuration(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.ApplicationMaintenanceConfigurationProperty"]]:
        '''``AWS::KinesisAnalyticsV2::Application.ApplicationMaintenanceConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-applicationmaintenanceconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.ApplicationMaintenanceConfigurationProperty"]], jsii.get(self, "applicationMaintenanceConfiguration"))

    @application_maintenance_configuration.setter
    def application_maintenance_configuration(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.ApplicationMaintenanceConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3ee22eb2d4826420231b97a72fb473adb0e577696c6d65cab483f2acda96133)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationMaintenanceConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="applicationMode")
    def application_mode(self) -> typing.Optional[builtins.str]:
        '''To create a Kinesis Data Analytics Studio notebook, you must set the mode to ``INTERACTIVE`` .

        However, for a Kinesis Data Analytics for Apache Flink application, the mode is optional.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-applicationmode
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationMode"))

    @application_mode.setter
    def application_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e9c83316fa80583cbdf8d5ae302580cbf7665e32af5f7b0ec0852312a99b3f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationMode", value)

    @builtins.property
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> typing.Optional[builtins.str]:
        '''The name of the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-applicationname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationName"))

    @application_name.setter
    def application_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f65f06ae39bb2bd68667c0fd563eae860cf18ed760d3b518cae3b1686d5e7bfb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationName", value)

    @builtins.property
    @jsii.member(jsii_name="runConfiguration")
    def run_configuration(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.RunConfigurationProperty"]]:
        '''``AWS::KinesisAnalyticsV2::Application.RunConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-runconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.RunConfigurationProperty"]], jsii.get(self, "runConfiguration"))

    @run_configuration.setter
    def run_configuration(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.RunConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a79ae96564492d92901cea5681dd2b874223e880d54b7603d9de65a79609ddcd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runConfiguration", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.ApplicationCodeConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "code_content": "codeContent",
            "code_content_type": "codeContentType",
        },
    )
    class ApplicationCodeConfigurationProperty:
        def __init__(
            self,
            *,
            code_content: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationV2.CodeContentProperty", typing.Dict[builtins.str, typing.Any]]],
            code_content_type: builtins.str,
        ) -> None:
            '''Describes code configuration for an application.

            :param code_content: The location and type of the application code.
            :param code_content_type: Specifies whether the code content is in text or zip format.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationcodeconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                application_code_configuration_property = kinesisanalytics.CfnApplicationV2.ApplicationCodeConfigurationProperty(
                    code_content=kinesisanalytics.CfnApplicationV2.CodeContentProperty(
                        s3_content_location=kinesisanalytics.CfnApplicationV2.S3ContentLocationProperty(
                            bucket_arn="bucketArn",
                            file_key="fileKey",
                
                            # the properties below are optional
                            object_version="objectVersion"
                        ),
                        text_content="textContent",
                        zip_file_content="zipFileContent"
                    ),
                    code_content_type="codeContentType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__11ced858fb4a6403eac2fb0ea73af504643aac4a21b74455dd7c22487b69faab)
                check_type(argname="argument code_content", value=code_content, expected_type=type_hints["code_content"])
                check_type(argname="argument code_content_type", value=code_content_type, expected_type=type_hints["code_content_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "code_content": code_content,
                "code_content_type": code_content_type,
            }

        @builtins.property
        def code_content(
            self,
        ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.CodeContentProperty"]:
            '''The location and type of the application code.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationcodeconfiguration.html#cfn-kinesisanalyticsv2-application-applicationcodeconfiguration-codecontent
            '''
            result = self._values.get("code_content")
            assert result is not None, "Required property 'code_content' is missing"
            return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.CodeContentProperty"], result)

        @builtins.property
        def code_content_type(self) -> builtins.str:
            '''Specifies whether the code content is in text or zip format.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationcodeconfiguration.html#cfn-kinesisanalyticsv2-application-applicationcodeconfiguration-codecontenttype
            '''
            result = self._values.get("code_content_type")
            assert result is not None, "Required property 'code_content_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApplicationCodeConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.ApplicationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "application_code_configuration": "applicationCodeConfiguration",
            "application_snapshot_configuration": "applicationSnapshotConfiguration",
            "environment_properties": "environmentProperties",
            "flink_application_configuration": "flinkApplicationConfiguration",
            "sql_application_configuration": "sqlApplicationConfiguration",
            "vpc_configurations": "vpcConfigurations",
            "zeppelin_application_configuration": "zeppelinApplicationConfiguration",
        },
    )
    class ApplicationConfigurationProperty:
        def __init__(
            self,
            *,
            application_code_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationV2.ApplicationCodeConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            application_snapshot_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationV2.ApplicationSnapshotConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            environment_properties: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationV2.EnvironmentPropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            flink_application_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationV2.FlinkApplicationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sql_application_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationV2.SqlApplicationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            vpc_configurations: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationV2.VpcConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            zeppelin_application_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationV2.ZeppelinApplicationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies the creation parameters for a Kinesis Data Analytics application.

            :param application_code_configuration: The code location and type parameters for a Flink-based Kinesis Data Analytics application.
            :param application_snapshot_configuration: Describes whether snapshots are enabled for a Flink-based Kinesis Data Analytics application.
            :param environment_properties: Describes execution properties for a Flink-based Kinesis Data Analytics application.
            :param flink_application_configuration: The creation and update parameters for a Flink-based Kinesis Data Analytics application.
            :param sql_application_configuration: The creation and update parameters for a SQL-based Kinesis Data Analytics application.
            :param vpc_configurations: The array of descriptions of VPC configurations available to the application.
            :param zeppelin_application_configuration: The configuration parameters for a Kinesis Data Analytics Studio notebook.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                application_configuration_property = kinesisanalytics.CfnApplicationV2.ApplicationConfigurationProperty(
                    application_code_configuration=kinesisanalytics.CfnApplicationV2.ApplicationCodeConfigurationProperty(
                        code_content=kinesisanalytics.CfnApplicationV2.CodeContentProperty(
                            s3_content_location=kinesisanalytics.CfnApplicationV2.S3ContentLocationProperty(
                                bucket_arn="bucketArn",
                                file_key="fileKey",
                
                                # the properties below are optional
                                object_version="objectVersion"
                            ),
                            text_content="textContent",
                            zip_file_content="zipFileContent"
                        ),
                        code_content_type="codeContentType"
                    ),
                    application_snapshot_configuration=kinesisanalytics.CfnApplicationV2.ApplicationSnapshotConfigurationProperty(
                        snapshots_enabled=False
                    ),
                    environment_properties=kinesisanalytics.CfnApplicationV2.EnvironmentPropertiesProperty(
                        property_groups=[kinesisanalytics.CfnApplicationV2.PropertyGroupProperty(
                            property_group_id="propertyGroupId",
                            property_map={
                                "property_map_key": "propertyMap"
                            }
                        )]
                    ),
                    flink_application_configuration=kinesisanalytics.CfnApplicationV2.FlinkApplicationConfigurationProperty(
                        checkpoint_configuration=kinesisanalytics.CfnApplicationV2.CheckpointConfigurationProperty(
                            configuration_type="configurationType",
                
                            # the properties below are optional
                            checkpointing_enabled=False,
                            checkpoint_interval=123,
                            min_pause_between_checkpoints=123
                        ),
                        monitoring_configuration=kinesisanalytics.CfnApplicationV2.MonitoringConfigurationProperty(
                            configuration_type="configurationType",
                
                            # the properties below are optional
                            log_level="logLevel",
                            metrics_level="metricsLevel"
                        ),
                        parallelism_configuration=kinesisanalytics.CfnApplicationV2.ParallelismConfigurationProperty(
                            configuration_type="configurationType",
                
                            # the properties below are optional
                            auto_scaling_enabled=False,
                            parallelism=123,
                            parallelism_per_kpu=123
                        )
                    ),
                    sql_application_configuration=kinesisanalytics.CfnApplicationV2.SqlApplicationConfigurationProperty(
                        inputs=[kinesisanalytics.CfnApplicationV2.InputProperty(
                            input_schema=kinesisanalytics.CfnApplicationV2.InputSchemaProperty(
                                record_columns=[kinesisanalytics.CfnApplicationV2.RecordColumnProperty(
                                    name="name",
                                    sql_type="sqlType",
                
                                    # the properties below are optional
                                    mapping="mapping"
                                )],
                                record_format=kinesisanalytics.CfnApplicationV2.RecordFormatProperty(
                                    record_format_type="recordFormatType",
                
                                    # the properties below are optional
                                    mapping_parameters=kinesisanalytics.CfnApplicationV2.MappingParametersProperty(
                                        csv_mapping_parameters=kinesisanalytics.CfnApplicationV2.CSVMappingParametersProperty(
                                            record_column_delimiter="recordColumnDelimiter",
                                            record_row_delimiter="recordRowDelimiter"
                                        ),
                                        json_mapping_parameters=kinesisanalytics.CfnApplicationV2.JSONMappingParametersProperty(
                                            record_row_path="recordRowPath"
                                        )
                                    )
                                ),
                
                                # the properties below are optional
                                record_encoding="recordEncoding"
                            ),
                            name_prefix="namePrefix",
                
                            # the properties below are optional
                            input_parallelism=kinesisanalytics.CfnApplicationV2.InputParallelismProperty(
                                count=123
                            ),
                            input_processing_configuration=kinesisanalytics.CfnApplicationV2.InputProcessingConfigurationProperty(
                                input_lambda_processor=kinesisanalytics.CfnApplicationV2.InputLambdaProcessorProperty(
                                    resource_arn="resourceArn"
                                )
                            ),
                            kinesis_firehose_input=kinesisanalytics.CfnApplicationV2.KinesisFirehoseInputProperty(
                                resource_arn="resourceArn"
                            ),
                            kinesis_streams_input=kinesisanalytics.CfnApplicationV2.KinesisStreamsInputProperty(
                                resource_arn="resourceArn"
                            )
                        )]
                    ),
                    vpc_configurations=[kinesisanalytics.CfnApplicationV2.VpcConfigurationProperty(
                        security_group_ids=["securityGroupIds"],
                        subnet_ids=["subnetIds"]
                    )],
                    zeppelin_application_configuration=kinesisanalytics.CfnApplicationV2.ZeppelinApplicationConfigurationProperty(
                        catalog_configuration=kinesisanalytics.CfnApplicationV2.CatalogConfigurationProperty(
                            glue_data_catalog_configuration=kinesisanalytics.CfnApplicationV2.GlueDataCatalogConfigurationProperty(
                                database_arn="databaseArn"
                            )
                        ),
                        custom_artifacts_configuration=[kinesisanalytics.CfnApplicationV2.CustomArtifactConfigurationProperty(
                            artifact_type="artifactType",
                
                            # the properties below are optional
                            maven_reference=kinesisanalytics.CfnApplicationV2.MavenReferenceProperty(
                                artifact_id="artifactId",
                                group_id="groupId",
                                version="version"
                            ),
                            s3_content_location=kinesisanalytics.CfnApplicationV2.S3ContentLocationProperty(
                                bucket_arn="bucketArn",
                                file_key="fileKey",
                
                                # the properties below are optional
                                object_version="objectVersion"
                            )
                        )],
                        deploy_as_application_configuration=kinesisanalytics.CfnApplicationV2.DeployAsApplicationConfigurationProperty(
                            s3_content_location=kinesisanalytics.CfnApplicationV2.S3ContentBaseLocationProperty(
                                bucket_arn="bucketArn",
                
                                # the properties below are optional
                                base_path="basePath"
                            )
                        ),
                        monitoring_configuration=kinesisanalytics.CfnApplicationV2.ZeppelinMonitoringConfigurationProperty(
                            log_level="logLevel"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__adedae0450360ea031c7f12fdc58fe9e38249fbd2e5f6df2b66cb768492efe40)
                check_type(argname="argument application_code_configuration", value=application_code_configuration, expected_type=type_hints["application_code_configuration"])
                check_type(argname="argument application_snapshot_configuration", value=application_snapshot_configuration, expected_type=type_hints["application_snapshot_configuration"])
                check_type(argname="argument environment_properties", value=environment_properties, expected_type=type_hints["environment_properties"])
                check_type(argname="argument flink_application_configuration", value=flink_application_configuration, expected_type=type_hints["flink_application_configuration"])
                check_type(argname="argument sql_application_configuration", value=sql_application_configuration, expected_type=type_hints["sql_application_configuration"])
                check_type(argname="argument vpc_configurations", value=vpc_configurations, expected_type=type_hints["vpc_configurations"])
                check_type(argname="argument zeppelin_application_configuration", value=zeppelin_application_configuration, expected_type=type_hints["zeppelin_application_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if application_code_configuration is not None:
                self._values["application_code_configuration"] = application_code_configuration
            if application_snapshot_configuration is not None:
                self._values["application_snapshot_configuration"] = application_snapshot_configuration
            if environment_properties is not None:
                self._values["environment_properties"] = environment_properties
            if flink_application_configuration is not None:
                self._values["flink_application_configuration"] = flink_application_configuration
            if sql_application_configuration is not None:
                self._values["sql_application_configuration"] = sql_application_configuration
            if vpc_configurations is not None:
                self._values["vpc_configurations"] = vpc_configurations
            if zeppelin_application_configuration is not None:
                self._values["zeppelin_application_configuration"] = zeppelin_application_configuration

        @builtins.property
        def application_code_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.ApplicationCodeConfigurationProperty"]]:
            '''The code location and type parameters for a Flink-based Kinesis Data Analytics application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-applicationcodeconfiguration
            '''
            result = self._values.get("application_code_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.ApplicationCodeConfigurationProperty"]], result)

        @builtins.property
        def application_snapshot_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.ApplicationSnapshotConfigurationProperty"]]:
            '''Describes whether snapshots are enabled for a Flink-based Kinesis Data Analytics application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-applicationsnapshotconfiguration
            '''
            result = self._values.get("application_snapshot_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.ApplicationSnapshotConfigurationProperty"]], result)

        @builtins.property
        def environment_properties(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.EnvironmentPropertiesProperty"]]:
            '''Describes execution properties for a Flink-based Kinesis Data Analytics application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-environmentproperties
            '''
            result = self._values.get("environment_properties")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.EnvironmentPropertiesProperty"]], result)

        @builtins.property
        def flink_application_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.FlinkApplicationConfigurationProperty"]]:
            '''The creation and update parameters for a Flink-based Kinesis Data Analytics application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-flinkapplicationconfiguration
            '''
            result = self._values.get("flink_application_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.FlinkApplicationConfigurationProperty"]], result)

        @builtins.property
        def sql_application_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.SqlApplicationConfigurationProperty"]]:
            '''The creation and update parameters for a SQL-based Kinesis Data Analytics application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-sqlapplicationconfiguration
            '''
            result = self._values.get("sql_application_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.SqlApplicationConfigurationProperty"]], result)

        @builtins.property
        def vpc_configurations(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.VpcConfigurationProperty"]]]]:
            '''The array of descriptions of VPC configurations available to the application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-vpcconfigurations
            '''
            result = self._values.get("vpc_configurations")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.VpcConfigurationProperty"]]]], result)

        @builtins.property
        def zeppelin_application_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.ZeppelinApplicationConfigurationProperty"]]:
            '''The configuration parameters for a Kinesis Data Analytics Studio notebook.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-zeppelinapplicationconfiguration
            '''
            result = self._values.get("zeppelin_application_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.ZeppelinApplicationConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApplicationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.ApplicationMaintenanceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "application_maintenance_window_start_time": "applicationMaintenanceWindowStartTime",
        },
    )
    class ApplicationMaintenanceConfigurationProperty:
        def __init__(
            self,
            *,
            application_maintenance_window_start_time: builtins.str,
        ) -> None:
            '''Specifies the maintence window parameters for a Kinesis Data Analytics application.

            :param application_maintenance_window_start_time: Specifies the start time of the maintence window.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationmaintenanceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                application_maintenance_configuration_property = kinesisanalytics.CfnApplicationV2.ApplicationMaintenanceConfigurationProperty(
                    application_maintenance_window_start_time="applicationMaintenanceWindowStartTime"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b3c28af81947372a5b9ec54172565fe2a7196cf424a8824350888549754d91e3)
                check_type(argname="argument application_maintenance_window_start_time", value=application_maintenance_window_start_time, expected_type=type_hints["application_maintenance_window_start_time"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "application_maintenance_window_start_time": application_maintenance_window_start_time,
            }

        @builtins.property
        def application_maintenance_window_start_time(self) -> builtins.str:
            '''Specifies the start time of the maintence window.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationmaintenanceconfiguration.html#cfn-kinesisanalyticsv2-application-applicationmaintenanceconfiguration-applicationmaintenancewindowstarttime
            '''
            result = self._values.get("application_maintenance_window_start_time")
            assert result is not None, "Required property 'application_maintenance_window_start_time' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApplicationMaintenanceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.ApplicationRestoreConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "application_restore_type": "applicationRestoreType",
            "snapshot_name": "snapshotName",
        },
    )
    class ApplicationRestoreConfigurationProperty:
        def __init__(
            self,
            *,
            application_restore_type: builtins.str,
            snapshot_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the method and snapshot to use when restarting an application using previously saved application state.

            :param application_restore_type: Specifies how the application should be restored.
            :param snapshot_name: The identifier of an existing snapshot of application state to use to restart an application. The application uses this value if ``RESTORE_FROM_CUSTOM_SNAPSHOT`` is specified for the ``ApplicationRestoreType`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationrestoreconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                application_restore_configuration_property = kinesisanalytics.CfnApplicationV2.ApplicationRestoreConfigurationProperty(
                    application_restore_type="applicationRestoreType",
                
                    # the properties below are optional
                    snapshot_name="snapshotName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__73181ab44c96124057c7e1f462e3a35e99fd6cb83742d4ce705475de1d4ee7df)
                check_type(argname="argument application_restore_type", value=application_restore_type, expected_type=type_hints["application_restore_type"])
                check_type(argname="argument snapshot_name", value=snapshot_name, expected_type=type_hints["snapshot_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "application_restore_type": application_restore_type,
            }
            if snapshot_name is not None:
                self._values["snapshot_name"] = snapshot_name

        @builtins.property
        def application_restore_type(self) -> builtins.str:
            '''Specifies how the application should be restored.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationrestoreconfiguration.html#cfn-kinesisanalyticsv2-application-applicationrestoreconfiguration-applicationrestoretype
            '''
            result = self._values.get("application_restore_type")
            assert result is not None, "Required property 'application_restore_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def snapshot_name(self) -> typing.Optional[builtins.str]:
            '''The identifier of an existing snapshot of application state to use to restart an application.

            The application uses this value if ``RESTORE_FROM_CUSTOM_SNAPSHOT`` is specified for the ``ApplicationRestoreType`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationrestoreconfiguration.html#cfn-kinesisanalyticsv2-application-applicationrestoreconfiguration-snapshotname
            '''
            result = self._values.get("snapshot_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApplicationRestoreConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.ApplicationSnapshotConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"snapshots_enabled": "snapshotsEnabled"},
    )
    class ApplicationSnapshotConfigurationProperty:
        def __init__(
            self,
            *,
            snapshots_enabled: typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable],
        ) -> None:
            '''Describes whether snapshots are enabled for a Flink-based Kinesis Data Analytics application.

            :param snapshots_enabled: Describes whether snapshots are enabled for a Flink-based Kinesis Data Analytics application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationsnapshotconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                application_snapshot_configuration_property = kinesisanalytics.CfnApplicationV2.ApplicationSnapshotConfigurationProperty(
                    snapshots_enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__62be34267931fb3ca9733964f24fde6338a92296b98b866fa5261551661b9921)
                check_type(argname="argument snapshots_enabled", value=snapshots_enabled, expected_type=type_hints["snapshots_enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "snapshots_enabled": snapshots_enabled,
            }

        @builtins.property
        def snapshots_enabled(
            self,
        ) -> typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]:
            '''Describes whether snapshots are enabled for a Flink-based Kinesis Data Analytics application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationsnapshotconfiguration.html#cfn-kinesisanalyticsv2-application-applicationsnapshotconfiguration-snapshotsenabled
            '''
            result = self._values.get("snapshots_enabled")
            assert result is not None, "Required property 'snapshots_enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApplicationSnapshotConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.CSVMappingParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "record_column_delimiter": "recordColumnDelimiter",
            "record_row_delimiter": "recordRowDelimiter",
        },
    )
    class CSVMappingParametersProperty:
        def __init__(
            self,
            *,
            record_column_delimiter: builtins.str,
            record_row_delimiter: builtins.str,
        ) -> None:
            '''For a SQL-based Kinesis Data Analytics application, provides additional mapping information when the record format uses delimiters, such as CSV.

            For example, the following sample records use CSV format, where the records use the *'\\n'* as the row delimiter and a comma (",") as the column delimiter:

            ``"name1", "address1"``

            ``"name2", "address2"``

            :param record_column_delimiter: The column delimiter. For example, in a CSV format, a comma (",") is the typical column delimiter.
            :param record_row_delimiter: The row delimiter. For example, in a CSV format, *'\\n'* is the typical row delimiter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-csvmappingparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                c_sVMapping_parameters_property = kinesisanalytics.CfnApplicationV2.CSVMappingParametersProperty(
                    record_column_delimiter="recordColumnDelimiter",
                    record_row_delimiter="recordRowDelimiter"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ac7b5879ac1fa92709822d232d2377fb551c35b93fc222aa4a14ec01413b718b)
                check_type(argname="argument record_column_delimiter", value=record_column_delimiter, expected_type=type_hints["record_column_delimiter"])
                check_type(argname="argument record_row_delimiter", value=record_row_delimiter, expected_type=type_hints["record_row_delimiter"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "record_column_delimiter": record_column_delimiter,
                "record_row_delimiter": record_row_delimiter,
            }

        @builtins.property
        def record_column_delimiter(self) -> builtins.str:
            '''The column delimiter.

            For example, in a CSV format, a comma (",") is the typical column delimiter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-csvmappingparameters.html#cfn-kinesisanalyticsv2-application-csvmappingparameters-recordcolumndelimiter
            '''
            result = self._values.get("record_column_delimiter")
            assert result is not None, "Required property 'record_column_delimiter' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def record_row_delimiter(self) -> builtins.str:
            '''The row delimiter.

            For example, in a CSV format, *'\\n'* is the typical row delimiter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-csvmappingparameters.html#cfn-kinesisanalyticsv2-application-csvmappingparameters-recordrowdelimiter
            '''
            result = self._values.get("record_row_delimiter")
            assert result is not None, "Required property 'record_row_delimiter' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CSVMappingParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.CatalogConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "glue_data_catalog_configuration": "glueDataCatalogConfiguration",
        },
    )
    class CatalogConfigurationProperty:
        def __init__(
            self,
            *,
            glue_data_catalog_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationV2.GlueDataCatalogConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The configuration parameters for the default Amazon Glue database.

            You use this database for SQL queries that you write in a Kinesis Data Analytics Studio notebook.

            :param glue_data_catalog_configuration: The configuration parameters for the default Amazon Glue database. You use this database for Apache Flink SQL queries and table API transforms that you write in a Kinesis Data Analytics Studio notebook.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-catalogconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                catalog_configuration_property = kinesisanalytics.CfnApplicationV2.CatalogConfigurationProperty(
                    glue_data_catalog_configuration=kinesisanalytics.CfnApplicationV2.GlueDataCatalogConfigurationProperty(
                        database_arn="databaseArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d72c420dd8e064238e27f38cc265738d549b5317a046487fe41e328345920689)
                check_type(argname="argument glue_data_catalog_configuration", value=glue_data_catalog_configuration, expected_type=type_hints["glue_data_catalog_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if glue_data_catalog_configuration is not None:
                self._values["glue_data_catalog_configuration"] = glue_data_catalog_configuration

        @builtins.property
        def glue_data_catalog_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.GlueDataCatalogConfigurationProperty"]]:
            '''The configuration parameters for the default Amazon Glue database.

            You use this database for Apache Flink SQL queries and table API transforms that you write in a Kinesis Data Analytics Studio notebook.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-catalogconfiguration.html#cfn-kinesisanalyticsv2-application-catalogconfiguration-gluedatacatalogconfiguration
            '''
            result = self._values.get("glue_data_catalog_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.GlueDataCatalogConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CatalogConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.CheckpointConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "configuration_type": "configurationType",
            "checkpointing_enabled": "checkpointingEnabled",
            "checkpoint_interval": "checkpointInterval",
            "min_pause_between_checkpoints": "minPauseBetweenCheckpoints",
        },
    )
    class CheckpointConfigurationProperty:
        def __init__(
            self,
            *,
            configuration_type: builtins.str,
            checkpointing_enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            checkpoint_interval: typing.Optional[jsii.Number] = None,
            min_pause_between_checkpoints: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Describes an application's checkpointing configuration.

            Checkpointing is the process of persisting application state for fault tolerance. For more information, see `Checkpoints for Fault Tolerance <https://docs.aws.amazon.com/https://ci.apache.org/projects/flink/flink-docs-release-1.8/concepts/programming-model.html#checkpoints-for-fault-tolerance>`_ in the `Apache Flink Documentation <https://docs.aws.amazon.com/https://ci.apache.org/projects/flink/flink-docs-release-1.8/>`_ .

            :param configuration_type: Describes whether the application uses Kinesis Data Analytics' default checkpointing behavior. You must set this property to ``CUSTOM`` in order to set the ``CheckpointingEnabled`` , ``CheckpointInterval`` , or ``MinPauseBetweenCheckpoints`` parameters. .. epigraph:: If this value is set to ``DEFAULT`` , the application will use the following values, even if they are set to other values using APIs or application code: - *CheckpointingEnabled:* true - *CheckpointInterval:* 60000 - *MinPauseBetweenCheckpoints:* 5000
            :param checkpointing_enabled: Describes whether checkpointing is enabled for a Flink-based Kinesis Data Analytics application. .. epigraph:: If ``CheckpointConfiguration.ConfigurationType`` is ``DEFAULT`` , the application will use a ``CheckpointingEnabled`` value of ``true`` , even if this value is set to another value using this API or in application code.
            :param checkpoint_interval: Describes the interval in milliseconds between checkpoint operations. .. epigraph:: If ``CheckpointConfiguration.ConfigurationType`` is ``DEFAULT`` , the application will use a ``CheckpointInterval`` value of 60000, even if this value is set to another value using this API or in application code.
            :param min_pause_between_checkpoints: Describes the minimum time in milliseconds after a checkpoint operation completes that a new checkpoint operation can start. If a checkpoint operation takes longer than the ``CheckpointInterval`` , the application otherwise performs continual checkpoint operations. For more information, see `Tuning Checkpointing <https://docs.aws.amazon.com/https://ci.apache.org/projects/flink/flink-docs-release-1.8/ops/state/large_state_tuning.html#tuning-checkpointing>`_ in the `Apache Flink Documentation <https://docs.aws.amazon.com/https://ci.apache.org/projects/flink/flink-docs-release-1.8/>`_ . .. epigraph:: If ``CheckpointConfiguration.ConfigurationType`` is ``DEFAULT`` , the application will use a ``MinPauseBetweenCheckpoints`` value of 5000, even if this value is set using this API or in application code.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-checkpointconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                checkpoint_configuration_property = kinesisanalytics.CfnApplicationV2.CheckpointConfigurationProperty(
                    configuration_type="configurationType",
                
                    # the properties below are optional
                    checkpointing_enabled=False,
                    checkpoint_interval=123,
                    min_pause_between_checkpoints=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d5f4a16d58b13b2fa9788f9baea212a8de26108bc477abcbd6fb176bb9b18a88)
                check_type(argname="argument configuration_type", value=configuration_type, expected_type=type_hints["configuration_type"])
                check_type(argname="argument checkpointing_enabled", value=checkpointing_enabled, expected_type=type_hints["checkpointing_enabled"])
                check_type(argname="argument checkpoint_interval", value=checkpoint_interval, expected_type=type_hints["checkpoint_interval"])
                check_type(argname="argument min_pause_between_checkpoints", value=min_pause_between_checkpoints, expected_type=type_hints["min_pause_between_checkpoints"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "configuration_type": configuration_type,
            }
            if checkpointing_enabled is not None:
                self._values["checkpointing_enabled"] = checkpointing_enabled
            if checkpoint_interval is not None:
                self._values["checkpoint_interval"] = checkpoint_interval
            if min_pause_between_checkpoints is not None:
                self._values["min_pause_between_checkpoints"] = min_pause_between_checkpoints

        @builtins.property
        def configuration_type(self) -> builtins.str:
            '''Describes whether the application uses Kinesis Data Analytics' default checkpointing behavior.

            You must set this property to ``CUSTOM`` in order to set the ``CheckpointingEnabled`` , ``CheckpointInterval`` , or ``MinPauseBetweenCheckpoints`` parameters.
            .. epigraph::

               If this value is set to ``DEFAULT`` , the application will use the following values, even if they are set to other values using APIs or application code:

               - *CheckpointingEnabled:* true
               - *CheckpointInterval:* 60000
               - *MinPauseBetweenCheckpoints:* 5000

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-checkpointconfiguration.html#cfn-kinesisanalyticsv2-application-checkpointconfiguration-configurationtype
            '''
            result = self._values.get("configuration_type")
            assert result is not None, "Required property 'configuration_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def checkpointing_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''Describes whether checkpointing is enabled for a Flink-based Kinesis Data Analytics application.

            .. epigraph::

               If ``CheckpointConfiguration.ConfigurationType`` is ``DEFAULT`` , the application will use a ``CheckpointingEnabled`` value of ``true`` , even if this value is set to another value using this API or in application code.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-checkpointconfiguration.html#cfn-kinesisanalyticsv2-application-checkpointconfiguration-checkpointingenabled
            '''
            result = self._values.get("checkpointing_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def checkpoint_interval(self) -> typing.Optional[jsii.Number]:
            '''Describes the interval in milliseconds between checkpoint operations.

            .. epigraph::

               If ``CheckpointConfiguration.ConfigurationType`` is ``DEFAULT`` , the application will use a ``CheckpointInterval`` value of 60000, even if this value is set to another value using this API or in application code.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-checkpointconfiguration.html#cfn-kinesisanalyticsv2-application-checkpointconfiguration-checkpointinterval
            '''
            result = self._values.get("checkpoint_interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def min_pause_between_checkpoints(self) -> typing.Optional[jsii.Number]:
            '''Describes the minimum time in milliseconds after a checkpoint operation completes that a new checkpoint operation can start.

            If a checkpoint operation takes longer than the ``CheckpointInterval`` , the application otherwise performs continual checkpoint operations. For more information, see `Tuning Checkpointing <https://docs.aws.amazon.com/https://ci.apache.org/projects/flink/flink-docs-release-1.8/ops/state/large_state_tuning.html#tuning-checkpointing>`_ in the `Apache Flink Documentation <https://docs.aws.amazon.com/https://ci.apache.org/projects/flink/flink-docs-release-1.8/>`_ .
            .. epigraph::

               If ``CheckpointConfiguration.ConfigurationType`` is ``DEFAULT`` , the application will use a ``MinPauseBetweenCheckpoints`` value of 5000, even if this value is set using this API or in application code.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-checkpointconfiguration.html#cfn-kinesisanalyticsv2-application-checkpointconfiguration-minpausebetweencheckpoints
            '''
            result = self._values.get("min_pause_between_checkpoints")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CheckpointConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.CodeContentProperty",
        jsii_struct_bases=[],
        name_mapping={
            "s3_content_location": "s3ContentLocation",
            "text_content": "textContent",
            "zip_file_content": "zipFileContent",
        },
    )
    class CodeContentProperty:
        def __init__(
            self,
            *,
            s3_content_location: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationV2.S3ContentLocationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            text_content: typing.Optional[builtins.str] = None,
            zip_file_content: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies either the application code, or the location of the application code, for a Flink-based Kinesis Data Analytics application.

            :param s3_content_location: Information about the Amazon S3 bucket that contains the application code.
            :param text_content: The text-format code for a Flink-based Kinesis Data Analytics application.
            :param zip_file_content: The zip-format code for a Flink-based Kinesis Data Analytics application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-codecontent.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                code_content_property = kinesisanalytics.CfnApplicationV2.CodeContentProperty(
                    s3_content_location=kinesisanalytics.CfnApplicationV2.S3ContentLocationProperty(
                        bucket_arn="bucketArn",
                        file_key="fileKey",
                
                        # the properties below are optional
                        object_version="objectVersion"
                    ),
                    text_content="textContent",
                    zip_file_content="zipFileContent"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5018e8540b0cb5ef200be9fec4c45b5f4a1bd73f35c9a85cb3275a5c29cfa251)
                check_type(argname="argument s3_content_location", value=s3_content_location, expected_type=type_hints["s3_content_location"])
                check_type(argname="argument text_content", value=text_content, expected_type=type_hints["text_content"])
                check_type(argname="argument zip_file_content", value=zip_file_content, expected_type=type_hints["zip_file_content"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if s3_content_location is not None:
                self._values["s3_content_location"] = s3_content_location
            if text_content is not None:
                self._values["text_content"] = text_content
            if zip_file_content is not None:
                self._values["zip_file_content"] = zip_file_content

        @builtins.property
        def s3_content_location(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.S3ContentLocationProperty"]]:
            '''Information about the Amazon S3 bucket that contains the application code.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-codecontent.html#cfn-kinesisanalyticsv2-application-codecontent-s3contentlocation
            '''
            result = self._values.get("s3_content_location")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.S3ContentLocationProperty"]], result)

        @builtins.property
        def text_content(self) -> typing.Optional[builtins.str]:
            '''The text-format code for a Flink-based Kinesis Data Analytics application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-codecontent.html#cfn-kinesisanalyticsv2-application-codecontent-textcontent
            '''
            result = self._values.get("text_content")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def zip_file_content(self) -> typing.Optional[builtins.str]:
            '''The zip-format code for a Flink-based Kinesis Data Analytics application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-codecontent.html#cfn-kinesisanalyticsv2-application-codecontent-zipfilecontent
            '''
            result = self._values.get("zip_file_content")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CodeContentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.CustomArtifactConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "artifact_type": "artifactType",
            "maven_reference": "mavenReference",
            "s3_content_location": "s3ContentLocation",
        },
    )
    class CustomArtifactConfigurationProperty:
        def __init__(
            self,
            *,
            artifact_type: builtins.str,
            maven_reference: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationV2.MavenReferenceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3_content_location: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationV2.S3ContentLocationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The configuration of connectors and user-defined functions.

            :param artifact_type: Set this to either ``UDF`` or ``DEPENDENCY_JAR`` . ``UDF`` stands for user-defined functions. This type of artifact must be in an S3 bucket. A ``DEPENDENCY_JAR`` can be in either Maven or an S3 bucket.
            :param maven_reference: The parameters required to fully specify a Maven reference.
            :param s3_content_location: The location of the custom artifacts.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-customartifactconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                custom_artifact_configuration_property = kinesisanalytics.CfnApplicationV2.CustomArtifactConfigurationProperty(
                    artifact_type="artifactType",
                
                    # the properties below are optional
                    maven_reference=kinesisanalytics.CfnApplicationV2.MavenReferenceProperty(
                        artifact_id="artifactId",
                        group_id="groupId",
                        version="version"
                    ),
                    s3_content_location=kinesisanalytics.CfnApplicationV2.S3ContentLocationProperty(
                        bucket_arn="bucketArn",
                        file_key="fileKey",
                
                        # the properties below are optional
                        object_version="objectVersion"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6e74e1834c61c6fad636d7bd2378b8af5b15fa7ca997b4fc18f6b3b23fc5b0ef)
                check_type(argname="argument artifact_type", value=artifact_type, expected_type=type_hints["artifact_type"])
                check_type(argname="argument maven_reference", value=maven_reference, expected_type=type_hints["maven_reference"])
                check_type(argname="argument s3_content_location", value=s3_content_location, expected_type=type_hints["s3_content_location"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "artifact_type": artifact_type,
            }
            if maven_reference is not None:
                self._values["maven_reference"] = maven_reference
            if s3_content_location is not None:
                self._values["s3_content_location"] = s3_content_location

        @builtins.property
        def artifact_type(self) -> builtins.str:
            '''Set this to either ``UDF`` or ``DEPENDENCY_JAR`` .

            ``UDF`` stands for user-defined functions. This type of artifact must be in an S3 bucket. A ``DEPENDENCY_JAR`` can be in either Maven or an S3 bucket.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-customartifactconfiguration.html#cfn-kinesisanalyticsv2-application-customartifactconfiguration-artifacttype
            '''
            result = self._values.get("artifact_type")
            assert result is not None, "Required property 'artifact_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def maven_reference(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.MavenReferenceProperty"]]:
            '''The parameters required to fully specify a Maven reference.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-customartifactconfiguration.html#cfn-kinesisanalyticsv2-application-customartifactconfiguration-mavenreference
            '''
            result = self._values.get("maven_reference")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.MavenReferenceProperty"]], result)

        @builtins.property
        def s3_content_location(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.S3ContentLocationProperty"]]:
            '''The location of the custom artifacts.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-customartifactconfiguration.html#cfn-kinesisanalyticsv2-application-customartifactconfiguration-s3contentlocation
            '''
            result = self._values.get("s3_content_location")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.S3ContentLocationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomArtifactConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.DeployAsApplicationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_content_location": "s3ContentLocation"},
    )
    class DeployAsApplicationConfigurationProperty:
        def __init__(
            self,
            *,
            s3_content_location: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationV2.S3ContentBaseLocationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The information required to deploy a Kinesis Data Analytics Studio notebook as an application with durable state.

            :param s3_content_location: The description of an Amazon S3 object that contains the Amazon Data Analytics application, including the Amazon Resource Name (ARN) of the S3 bucket, the name of the Amazon S3 object that contains the data, and the version number of the Amazon S3 object that contains the data.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-deployasapplicationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                deploy_as_application_configuration_property = kinesisanalytics.CfnApplicationV2.DeployAsApplicationConfigurationProperty(
                    s3_content_location=kinesisanalytics.CfnApplicationV2.S3ContentBaseLocationProperty(
                        bucket_arn="bucketArn",
                
                        # the properties below are optional
                        base_path="basePath"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__622030896182211331c57ed4befc845ea6ec88fcbca0ff17a24f7e9226eeab77)
                check_type(argname="argument s3_content_location", value=s3_content_location, expected_type=type_hints["s3_content_location"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "s3_content_location": s3_content_location,
            }

        @builtins.property
        def s3_content_location(
            self,
        ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.S3ContentBaseLocationProperty"]:
            '''The description of an Amazon S3 object that contains the Amazon Data Analytics application, including the Amazon Resource Name (ARN) of the S3 bucket, the name of the Amazon S3 object that contains the data, and the version number of the Amazon S3 object that contains the data.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-deployasapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-deployasapplicationconfiguration-s3contentlocation
            '''
            result = self._values.get("s3_content_location")
            assert result is not None, "Required property 's3_content_location' is missing"
            return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.S3ContentBaseLocationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeployAsApplicationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.EnvironmentPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"property_groups": "propertyGroups"},
    )
    class EnvironmentPropertiesProperty:
        def __init__(
            self,
            *,
            property_groups: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationV2.PropertyGroupProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Describes execution properties for a Flink-based Kinesis Data Analytics application.

            :param property_groups: Describes the execution property groups.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-environmentproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                environment_properties_property = kinesisanalytics.CfnApplicationV2.EnvironmentPropertiesProperty(
                    property_groups=[kinesisanalytics.CfnApplicationV2.PropertyGroupProperty(
                        property_group_id="propertyGroupId",
                        property_map={
                            "property_map_key": "propertyMap"
                        }
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a474487a1bb62dcf5a29014595714218319769466da8d8f9f253c9a9bd9c7c46)
                check_type(argname="argument property_groups", value=property_groups, expected_type=type_hints["property_groups"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if property_groups is not None:
                self._values["property_groups"] = property_groups

        @builtins.property
        def property_groups(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.PropertyGroupProperty"]]]]:
            '''Describes the execution property groups.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-environmentproperties.html#cfn-kinesisanalyticsv2-application-environmentproperties-propertygroups
            '''
            result = self._values.get("property_groups")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.PropertyGroupProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EnvironmentPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.FlinkApplicationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "checkpoint_configuration": "checkpointConfiguration",
            "monitoring_configuration": "monitoringConfiguration",
            "parallelism_configuration": "parallelismConfiguration",
        },
    )
    class FlinkApplicationConfigurationProperty:
        def __init__(
            self,
            *,
            checkpoint_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationV2.CheckpointConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            monitoring_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationV2.MonitoringConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            parallelism_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationV2.ParallelismConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Describes configuration parameters for a Flink-based Kinesis Data Analytics application or a Studio notebook.

            :param checkpoint_configuration: Describes an application's checkpointing configuration. Checkpointing is the process of persisting application state for fault tolerance. For more information, see `Checkpoints for Fault Tolerance <https://docs.aws.amazon.com/https://ci.apache.org/projects/flink/flink-docs-release-1.8/concepts/programming-model.html#checkpoints-for-fault-tolerance>`_ in the `Apache Flink Documentation <https://docs.aws.amazon.com/https://ci.apache.org/projects/flink/flink-docs-release-1.8/>`_ .
            :param monitoring_configuration: Describes configuration parameters for Amazon CloudWatch logging for an application.
            :param parallelism_configuration: Describes parameters for how an application executes multiple tasks simultaneously.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-flinkapplicationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                flink_application_configuration_property = kinesisanalytics.CfnApplicationV2.FlinkApplicationConfigurationProperty(
                    checkpoint_configuration=kinesisanalytics.CfnApplicationV2.CheckpointConfigurationProperty(
                        configuration_type="configurationType",
                
                        # the properties below are optional
                        checkpointing_enabled=False,
                        checkpoint_interval=123,
                        min_pause_between_checkpoints=123
                    ),
                    monitoring_configuration=kinesisanalytics.CfnApplicationV2.MonitoringConfigurationProperty(
                        configuration_type="configurationType",
                
                        # the properties below are optional
                        log_level="logLevel",
                        metrics_level="metricsLevel"
                    ),
                    parallelism_configuration=kinesisanalytics.CfnApplicationV2.ParallelismConfigurationProperty(
                        configuration_type="configurationType",
                
                        # the properties below are optional
                        auto_scaling_enabled=False,
                        parallelism=123,
                        parallelism_per_kpu=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__78b1dc8237ecce6a4ce1074e1dba92279736f8f4a110394b64036cebb1fdb612)
                check_type(argname="argument checkpoint_configuration", value=checkpoint_configuration, expected_type=type_hints["checkpoint_configuration"])
                check_type(argname="argument monitoring_configuration", value=monitoring_configuration, expected_type=type_hints["monitoring_configuration"])
                check_type(argname="argument parallelism_configuration", value=parallelism_configuration, expected_type=type_hints["parallelism_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if checkpoint_configuration is not None:
                self._values["checkpoint_configuration"] = checkpoint_configuration
            if monitoring_configuration is not None:
                self._values["monitoring_configuration"] = monitoring_configuration
            if parallelism_configuration is not None:
                self._values["parallelism_configuration"] = parallelism_configuration

        @builtins.property
        def checkpoint_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.CheckpointConfigurationProperty"]]:
            '''Describes an application's checkpointing configuration.

            Checkpointing is the process of persisting application state for fault tolerance. For more information, see `Checkpoints for Fault Tolerance <https://docs.aws.amazon.com/https://ci.apache.org/projects/flink/flink-docs-release-1.8/concepts/programming-model.html#checkpoints-for-fault-tolerance>`_ in the `Apache Flink Documentation <https://docs.aws.amazon.com/https://ci.apache.org/projects/flink/flink-docs-release-1.8/>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-flinkapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-flinkapplicationconfiguration-checkpointconfiguration
            '''
            result = self._values.get("checkpoint_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.CheckpointConfigurationProperty"]], result)

        @builtins.property
        def monitoring_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.MonitoringConfigurationProperty"]]:
            '''Describes configuration parameters for Amazon CloudWatch logging for an application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-flinkapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-flinkapplicationconfiguration-monitoringconfiguration
            '''
            result = self._values.get("monitoring_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.MonitoringConfigurationProperty"]], result)

        @builtins.property
        def parallelism_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.ParallelismConfigurationProperty"]]:
            '''Describes parameters for how an application executes multiple tasks simultaneously.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-flinkapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-flinkapplicationconfiguration-parallelismconfiguration
            '''
            result = self._values.get("parallelism_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.ParallelismConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FlinkApplicationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.FlinkRunConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"allow_non_restored_state": "allowNonRestoredState"},
    )
    class FlinkRunConfigurationProperty:
        def __init__(
            self,
            *,
            allow_non_restored_state: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
        ) -> None:
            '''Describes the starting parameters for a Flink-based Kinesis Data Analytics application.

            :param allow_non_restored_state: When restoring from a snapshot, specifies whether the runtime is allowed to skip a state that cannot be mapped to the new program. This will happen if the program is updated between snapshots to remove stateful parameters, and state data in the snapshot no longer corresponds to valid application data. For more information, see `Allowing Non-Restored State <https://docs.aws.amazon.com/https://ci.apache.org/projects/flink/flink-docs-release-1.8/ops/state/savepoints.html#allowing-non-restored-state>`_ in the `Apache Flink documentation <https://docs.aws.amazon.com/https://ci.apache.org/projects/flink/flink-docs-release-1.8/>`_ . .. epigraph:: This value defaults to ``false`` . If you update your application without specifying this parameter, ``AllowNonRestoredState`` will be set to ``false`` , even if it was previously set to ``true`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-flinkrunconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                flink_run_configuration_property = kinesisanalytics.CfnApplicationV2.FlinkRunConfigurationProperty(
                    allow_non_restored_state=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__eec6ce9ab9327e4bc0c12b507ac90007f268452f96cd144be25df0bd4f38093c)
                check_type(argname="argument allow_non_restored_state", value=allow_non_restored_state, expected_type=type_hints["allow_non_restored_state"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if allow_non_restored_state is not None:
                self._values["allow_non_restored_state"] = allow_non_restored_state

        @builtins.property
        def allow_non_restored_state(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''When restoring from a snapshot, specifies whether the runtime is allowed to skip a state that cannot be mapped to the new program.

            This will happen if the program is updated between snapshots to remove stateful parameters, and state data in the snapshot no longer corresponds to valid application data. For more information, see `Allowing Non-Restored State <https://docs.aws.amazon.com/https://ci.apache.org/projects/flink/flink-docs-release-1.8/ops/state/savepoints.html#allowing-non-restored-state>`_ in the `Apache Flink documentation <https://docs.aws.amazon.com/https://ci.apache.org/projects/flink/flink-docs-release-1.8/>`_ .
            .. epigraph::

               This value defaults to ``false`` . If you update your application without specifying this parameter, ``AllowNonRestoredState`` will be set to ``false`` , even if it was previously set to ``true`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-flinkrunconfiguration.html#cfn-kinesisanalyticsv2-application-flinkrunconfiguration-allownonrestoredstate
            '''
            result = self._values.get("allow_non_restored_state")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FlinkRunConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.GlueDataCatalogConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"database_arn": "databaseArn"},
    )
    class GlueDataCatalogConfigurationProperty:
        def __init__(
            self,
            *,
            database_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration of the Glue Data Catalog that you use for Apache Flink SQL queries and table API transforms that you write in an application.

            :param database_arn: The Amazon Resource Name (ARN) of the database.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-gluedatacatalogconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                glue_data_catalog_configuration_property = kinesisanalytics.CfnApplicationV2.GlueDataCatalogConfigurationProperty(
                    database_arn="databaseArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a5503d59073c796705474cba47c5d34a05c6dfeef56c91ea80aaf52212ae89bc)
                check_type(argname="argument database_arn", value=database_arn, expected_type=type_hints["database_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if database_arn is not None:
                self._values["database_arn"] = database_arn

        @builtins.property
        def database_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the database.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-gluedatacatalogconfiguration.html#cfn-kinesisanalyticsv2-application-gluedatacatalogconfiguration-databasearn
            '''
            result = self._values.get("database_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GlueDataCatalogConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.InputLambdaProcessorProperty",
        jsii_struct_bases=[],
        name_mapping={"resource_arn": "resourceArn"},
    )
    class InputLambdaProcessorProperty:
        def __init__(self, *, resource_arn: builtins.str) -> None:
            '''An object that contains the Amazon Resource Name (ARN) of the Amazon Lambda function that is used to preprocess records in the stream in a SQL-based Kinesis Data Analytics application.

            :param resource_arn: The ARN of the Amazon Lambda function that operates on records in the stream. .. epigraph:: To specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see `Example ARNs: Amazon Lambda <https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`_

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputlambdaprocessor.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                input_lambda_processor_property = kinesisanalytics.CfnApplicationV2.InputLambdaProcessorProperty(
                    resource_arn="resourceArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__abcc74675d58c2e25b0f95b0c1fe1a9a9c8824cfbd4c68e80e7d43b664035296)
                check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "resource_arn": resource_arn,
            }

        @builtins.property
        def resource_arn(self) -> builtins.str:
            '''The ARN of the Amazon Lambda function that operates on records in the stream.

            .. epigraph::

               To specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see `Example ARNs: Amazon Lambda <https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda>`_

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputlambdaprocessor.html#cfn-kinesisanalyticsv2-application-inputlambdaprocessor-resourcearn
            '''
            result = self._values.get("resource_arn")
            assert result is not None, "Required property 'resource_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputLambdaProcessorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.InputParallelismProperty",
        jsii_struct_bases=[],
        name_mapping={"count": "count"},
    )
    class InputParallelismProperty:
        def __init__(self, *, count: typing.Optional[jsii.Number] = None) -> None:
            '''For a SQL-based Kinesis Data Analytics application, describes the number of in-application streams to create for a given streaming source.

            :param count: The number of in-application streams to create.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputparallelism.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                input_parallelism_property = kinesisanalytics.CfnApplicationV2.InputParallelismProperty(
                    count=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f93451a6b3dc8951b0c68151cdd08fb947b19d0a8bb863c504bc0475d167314f)
                check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if count is not None:
                self._values["count"] = count

        @builtins.property
        def count(self) -> typing.Optional[jsii.Number]:
            '''The number of in-application streams to create.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputparallelism.html#cfn-kinesisanalyticsv2-application-inputparallelism-count
            '''
            result = self._values.get("count")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputParallelismProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.InputProcessingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"input_lambda_processor": "inputLambdaProcessor"},
    )
    class InputProcessingConfigurationProperty:
        def __init__(
            self,
            *,
            input_lambda_processor: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationV2.InputLambdaProcessorProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''For an SQL-based Amazon Kinesis Data Analytics application, describes a processor that is used to preprocess the records in the stream before being processed by your application code.

            Currently, the only input processor available is `Amazon Lambda <https://docs.aws.amazon.com/lambda/>`_ .

            :param input_lambda_processor: The `InputLambdaProcessor <https://docs.aws.amazon.com/kinesisanalytics/latest/apiv2/API_InputLambdaProcessor.html>`_ that is used to preprocess the records in the stream before being processed by your application code.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputprocessingconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                input_processing_configuration_property = kinesisanalytics.CfnApplicationV2.InputProcessingConfigurationProperty(
                    input_lambda_processor=kinesisanalytics.CfnApplicationV2.InputLambdaProcessorProperty(
                        resource_arn="resourceArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__debb904bbac4fd9fb35adf75ce4af3770860e7d3cba866fd3b2004b007cbfbe9)
                check_type(argname="argument input_lambda_processor", value=input_lambda_processor, expected_type=type_hints["input_lambda_processor"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if input_lambda_processor is not None:
                self._values["input_lambda_processor"] = input_lambda_processor

        @builtins.property
        def input_lambda_processor(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.InputLambdaProcessorProperty"]]:
            '''The `InputLambdaProcessor <https://docs.aws.amazon.com/kinesisanalytics/latest/apiv2/API_InputLambdaProcessor.html>`_ that is used to preprocess the records in the stream before being processed by your application code.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputprocessingconfiguration.html#cfn-kinesisanalyticsv2-application-inputprocessingconfiguration-inputlambdaprocessor
            '''
            result = self._values.get("input_lambda_processor")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.InputLambdaProcessorProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputProcessingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.InputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "input_schema": "inputSchema",
            "name_prefix": "namePrefix",
            "input_parallelism": "inputParallelism",
            "input_processing_configuration": "inputProcessingConfiguration",
            "kinesis_firehose_input": "kinesisFirehoseInput",
            "kinesis_streams_input": "kinesisStreamsInput",
        },
    )
    class InputProperty:
        def __init__(
            self,
            *,
            input_schema: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationV2.InputSchemaProperty", typing.Dict[builtins.str, typing.Any]]],
            name_prefix: builtins.str,
            input_parallelism: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationV2.InputParallelismProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            input_processing_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationV2.InputProcessingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            kinesis_firehose_input: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationV2.KinesisFirehoseInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            kinesis_streams_input: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationV2.KinesisStreamsInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''When you configure the application input for a SQL-based Kinesis Data Analytics application, you specify the streaming source, the in-application stream name that is created, and the mapping between the two.

            :param input_schema: Describes the format of the data in the streaming source, and how each data element maps to corresponding columns in the in-application stream that is being created. Also used to describe the format of the reference data source.
            :param name_prefix: The name prefix to use when creating an in-application stream. Suppose that you specify a prefix " ``MyInApplicationStream`` ." Kinesis Data Analytics then creates one or more (as per the ``InputParallelism`` count you specified) in-application streams with the names " ``MyInApplicationStream_001`` ," " ``MyInApplicationStream_002`` ," and so on.
            :param input_parallelism: Describes the number of in-application streams to create.
            :param input_processing_configuration: The `InputProcessingConfiguration <https://docs.aws.amazon.com/kinesisanalytics/latest/apiv2/API_InputProcessingConfiguration.html>`_ for the input. An input processor transforms records as they are received from the stream, before the application's SQL code executes. Currently, the only input processing configuration available is `InputLambdaProcessor <https://docs.aws.amazon.com/kinesisanalytics/latest/apiv2/API_InputLambdaProcessor.html>`_ .
            :param kinesis_firehose_input: If the streaming source is an Amazon Kinesis Data Firehose delivery stream, identifies the delivery stream's ARN.
            :param kinesis_streams_input: If the streaming source is an Amazon Kinesis data stream, identifies the stream's Amazon Resource Name (ARN).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                input_property = kinesisanalytics.CfnApplicationV2.InputProperty(
                    input_schema=kinesisanalytics.CfnApplicationV2.InputSchemaProperty(
                        record_columns=[kinesisanalytics.CfnApplicationV2.RecordColumnProperty(
                            name="name",
                            sql_type="sqlType",
                
                            # the properties below are optional
                            mapping="mapping"
                        )],
                        record_format=kinesisanalytics.CfnApplicationV2.RecordFormatProperty(
                            record_format_type="recordFormatType",
                
                            # the properties below are optional
                            mapping_parameters=kinesisanalytics.CfnApplicationV2.MappingParametersProperty(
                                csv_mapping_parameters=kinesisanalytics.CfnApplicationV2.CSVMappingParametersProperty(
                                    record_column_delimiter="recordColumnDelimiter",
                                    record_row_delimiter="recordRowDelimiter"
                                ),
                                json_mapping_parameters=kinesisanalytics.CfnApplicationV2.JSONMappingParametersProperty(
                                    record_row_path="recordRowPath"
                                )
                            )
                        ),
                
                        # the properties below are optional
                        record_encoding="recordEncoding"
                    ),
                    name_prefix="namePrefix",
                
                    # the properties below are optional
                    input_parallelism=kinesisanalytics.CfnApplicationV2.InputParallelismProperty(
                        count=123
                    ),
                    input_processing_configuration=kinesisanalytics.CfnApplicationV2.InputProcessingConfigurationProperty(
                        input_lambda_processor=kinesisanalytics.CfnApplicationV2.InputLambdaProcessorProperty(
                            resource_arn="resourceArn"
                        )
                    ),
                    kinesis_firehose_input=kinesisanalytics.CfnApplicationV2.KinesisFirehoseInputProperty(
                        resource_arn="resourceArn"
                    ),
                    kinesis_streams_input=kinesisanalytics.CfnApplicationV2.KinesisStreamsInputProperty(
                        resource_arn="resourceArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5814f166b40de77db8a8dd3b125b6020e018bf7424e479d37df575b412ea5047)
                check_type(argname="argument input_schema", value=input_schema, expected_type=type_hints["input_schema"])
                check_type(argname="argument name_prefix", value=name_prefix, expected_type=type_hints["name_prefix"])
                check_type(argname="argument input_parallelism", value=input_parallelism, expected_type=type_hints["input_parallelism"])
                check_type(argname="argument input_processing_configuration", value=input_processing_configuration, expected_type=type_hints["input_processing_configuration"])
                check_type(argname="argument kinesis_firehose_input", value=kinesis_firehose_input, expected_type=type_hints["kinesis_firehose_input"])
                check_type(argname="argument kinesis_streams_input", value=kinesis_streams_input, expected_type=type_hints["kinesis_streams_input"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "input_schema": input_schema,
                "name_prefix": name_prefix,
            }
            if input_parallelism is not None:
                self._values["input_parallelism"] = input_parallelism
            if input_processing_configuration is not None:
                self._values["input_processing_configuration"] = input_processing_configuration
            if kinesis_firehose_input is not None:
                self._values["kinesis_firehose_input"] = kinesis_firehose_input
            if kinesis_streams_input is not None:
                self._values["kinesis_streams_input"] = kinesis_streams_input

        @builtins.property
        def input_schema(
            self,
        ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.InputSchemaProperty"]:
            '''Describes the format of the data in the streaming source, and how each data element maps to corresponding columns in the in-application stream that is being created.

            Also used to describe the format of the reference data source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html#cfn-kinesisanalyticsv2-application-input-inputschema
            '''
            result = self._values.get("input_schema")
            assert result is not None, "Required property 'input_schema' is missing"
            return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.InputSchemaProperty"], result)

        @builtins.property
        def name_prefix(self) -> builtins.str:
            '''The name prefix to use when creating an in-application stream.

            Suppose that you specify a prefix " ``MyInApplicationStream`` ." Kinesis Data Analytics then creates one or more (as per the ``InputParallelism`` count you specified) in-application streams with the names " ``MyInApplicationStream_001`` ," " ``MyInApplicationStream_002`` ," and so on.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html#cfn-kinesisanalyticsv2-application-input-nameprefix
            '''
            result = self._values.get("name_prefix")
            assert result is not None, "Required property 'name_prefix' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def input_parallelism(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.InputParallelismProperty"]]:
            '''Describes the number of in-application streams to create.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html#cfn-kinesisanalyticsv2-application-input-inputparallelism
            '''
            result = self._values.get("input_parallelism")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.InputParallelismProperty"]], result)

        @builtins.property
        def input_processing_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.InputProcessingConfigurationProperty"]]:
            '''The `InputProcessingConfiguration <https://docs.aws.amazon.com/kinesisanalytics/latest/apiv2/API_InputProcessingConfiguration.html>`_ for the input. An input processor transforms records as they are received from the stream, before the application's SQL code executes. Currently, the only input processing configuration available is `InputLambdaProcessor <https://docs.aws.amazon.com/kinesisanalytics/latest/apiv2/API_InputLambdaProcessor.html>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html#cfn-kinesisanalyticsv2-application-input-inputprocessingconfiguration
            '''
            result = self._values.get("input_processing_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.InputProcessingConfigurationProperty"]], result)

        @builtins.property
        def kinesis_firehose_input(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.KinesisFirehoseInputProperty"]]:
            '''If the streaming source is an Amazon Kinesis Data Firehose delivery stream, identifies the delivery stream's ARN.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html#cfn-kinesisanalyticsv2-application-input-kinesisfirehoseinput
            '''
            result = self._values.get("kinesis_firehose_input")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.KinesisFirehoseInputProperty"]], result)

        @builtins.property
        def kinesis_streams_input(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.KinesisStreamsInputProperty"]]:
            '''If the streaming source is an Amazon Kinesis data stream, identifies the stream's Amazon Resource Name (ARN).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html#cfn-kinesisanalyticsv2-application-input-kinesisstreamsinput
            '''
            result = self._values.get("kinesis_streams_input")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.KinesisStreamsInputProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.InputSchemaProperty",
        jsii_struct_bases=[],
        name_mapping={
            "record_columns": "recordColumns",
            "record_format": "recordFormat",
            "record_encoding": "recordEncoding",
        },
    )
    class InputSchemaProperty:
        def __init__(
            self,
            *,
            record_columns: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationV2.RecordColumnProperty", typing.Dict[builtins.str, typing.Any]]]]],
            record_format: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationV2.RecordFormatProperty", typing.Dict[builtins.str, typing.Any]]],
            record_encoding: typing.Optional[builtins.str] = None,
        ) -> None:
            '''For a SQL-based Kinesis Data Analytics application, describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.

            :param record_columns: A list of ``RecordColumn`` objects.
            :param record_format: Specifies the format of the records on the streaming source.
            :param record_encoding: Specifies the encoding of the records in the streaming source. For example, UTF-8.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputschema.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                input_schema_property = kinesisanalytics.CfnApplicationV2.InputSchemaProperty(
                    record_columns=[kinesisanalytics.CfnApplicationV2.RecordColumnProperty(
                        name="name",
                        sql_type="sqlType",
                
                        # the properties below are optional
                        mapping="mapping"
                    )],
                    record_format=kinesisanalytics.CfnApplicationV2.RecordFormatProperty(
                        record_format_type="recordFormatType",
                
                        # the properties below are optional
                        mapping_parameters=kinesisanalytics.CfnApplicationV2.MappingParametersProperty(
                            csv_mapping_parameters=kinesisanalytics.CfnApplicationV2.CSVMappingParametersProperty(
                                record_column_delimiter="recordColumnDelimiter",
                                record_row_delimiter="recordRowDelimiter"
                            ),
                            json_mapping_parameters=kinesisanalytics.CfnApplicationV2.JSONMappingParametersProperty(
                                record_row_path="recordRowPath"
                            )
                        )
                    ),
                
                    # the properties below are optional
                    record_encoding="recordEncoding"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__48f3d8de8a9cbcfdacd9ccef8190e96847bd560d9134cd44ba92c8856fd850fb)
                check_type(argname="argument record_columns", value=record_columns, expected_type=type_hints["record_columns"])
                check_type(argname="argument record_format", value=record_format, expected_type=type_hints["record_format"])
                check_type(argname="argument record_encoding", value=record_encoding, expected_type=type_hints["record_encoding"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "record_columns": record_columns,
                "record_format": record_format,
            }
            if record_encoding is not None:
                self._values["record_encoding"] = record_encoding

        @builtins.property
        def record_columns(
            self,
        ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.RecordColumnProperty"]]]:
            '''A list of ``RecordColumn`` objects.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputschema.html#cfn-kinesisanalyticsv2-application-inputschema-recordcolumns
            '''
            result = self._values.get("record_columns")
            assert result is not None, "Required property 'record_columns' is missing"
            return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.RecordColumnProperty"]]], result)

        @builtins.property
        def record_format(
            self,
        ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.RecordFormatProperty"]:
            '''Specifies the format of the records on the streaming source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputschema.html#cfn-kinesisanalyticsv2-application-inputschema-recordformat
            '''
            result = self._values.get("record_format")
            assert result is not None, "Required property 'record_format' is missing"
            return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.RecordFormatProperty"], result)

        @builtins.property
        def record_encoding(self) -> typing.Optional[builtins.str]:
            '''Specifies the encoding of the records in the streaming source.

            For example, UTF-8.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputschema.html#cfn-kinesisanalyticsv2-application-inputschema-recordencoding
            '''
            result = self._values.get("record_encoding")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputSchemaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.JSONMappingParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"record_row_path": "recordRowPath"},
    )
    class JSONMappingParametersProperty:
        def __init__(self, *, record_row_path: builtins.str) -> None:
            '''For a SQL-based Kinesis Data Analytics application, provides additional mapping information when JSON is the record format on the streaming source.

            :param record_row_path: The path to the top-level parent that contains the records.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-jsonmappingparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                j_sONMapping_parameters_property = kinesisanalytics.CfnApplicationV2.JSONMappingParametersProperty(
                    record_row_path="recordRowPath"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d7a570e5bc762b99c19eda34dec838cee12d497461e3abead2ca41f3f1ed405b)
                check_type(argname="argument record_row_path", value=record_row_path, expected_type=type_hints["record_row_path"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "record_row_path": record_row_path,
            }

        @builtins.property
        def record_row_path(self) -> builtins.str:
            '''The path to the top-level parent that contains the records.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-jsonmappingparameters.html#cfn-kinesisanalyticsv2-application-jsonmappingparameters-recordrowpath
            '''
            result = self._values.get("record_row_path")
            assert result is not None, "Required property 'record_row_path' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JSONMappingParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.KinesisFirehoseInputProperty",
        jsii_struct_bases=[],
        name_mapping={"resource_arn": "resourceArn"},
    )
    class KinesisFirehoseInputProperty:
        def __init__(self, *, resource_arn: builtins.str) -> None:
            '''For a SQL-based Kinesis Data Analytics application, identifies a Kinesis Data Firehose delivery stream as the streaming source.

            You provide the delivery stream's Amazon Resource Name (ARN).

            :param resource_arn: The Amazon Resource Name (ARN) of the delivery stream.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-kinesisfirehoseinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                kinesis_firehose_input_property = kinesisanalytics.CfnApplicationV2.KinesisFirehoseInputProperty(
                    resource_arn="resourceArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f4593a749409eee1c4a15c54afd161d1dfcd6583d445152df2c78a1f4578ad77)
                check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "resource_arn": resource_arn,
            }

        @builtins.property
        def resource_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the delivery stream.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-kinesisfirehoseinput.html#cfn-kinesisanalyticsv2-application-kinesisfirehoseinput-resourcearn
            '''
            result = self._values.get("resource_arn")
            assert result is not None, "Required property 'resource_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisFirehoseInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.KinesisStreamsInputProperty",
        jsii_struct_bases=[],
        name_mapping={"resource_arn": "resourceArn"},
    )
    class KinesisStreamsInputProperty:
        def __init__(self, *, resource_arn: builtins.str) -> None:
            '''Identifies a Kinesis data stream as the streaming source.

            You provide the stream's Amazon Resource Name (ARN).

            :param resource_arn: The ARN of the input Kinesis data stream to read.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-kinesisstreamsinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                kinesis_streams_input_property = kinesisanalytics.CfnApplicationV2.KinesisStreamsInputProperty(
                    resource_arn="resourceArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__048ff7e43924503c1aa6b4dc5f4c93b0de7cb29e431592ebfc0d2f72132f2f8e)
                check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "resource_arn": resource_arn,
            }

        @builtins.property
        def resource_arn(self) -> builtins.str:
            '''The ARN of the input Kinesis data stream to read.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-kinesisstreamsinput.html#cfn-kinesisanalyticsv2-application-kinesisstreamsinput-resourcearn
            '''
            result = self._values.get("resource_arn")
            assert result is not None, "Required property 'resource_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisStreamsInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.MappingParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "csv_mapping_parameters": "csvMappingParameters",
            "json_mapping_parameters": "jsonMappingParameters",
        },
    )
    class MappingParametersProperty:
        def __init__(
            self,
            *,
            csv_mapping_parameters: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationV2.CSVMappingParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            json_mapping_parameters: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationV2.JSONMappingParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''When you configure a SQL-based Kinesis Data Analytics application's input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

            :param csv_mapping_parameters: Provides additional mapping information when the record format uses delimiters (for example, CSV).
            :param json_mapping_parameters: Provides additional mapping information when JSON is the record format on the streaming source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mappingparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                mapping_parameters_property = kinesisanalytics.CfnApplicationV2.MappingParametersProperty(
                    csv_mapping_parameters=kinesisanalytics.CfnApplicationV2.CSVMappingParametersProperty(
                        record_column_delimiter="recordColumnDelimiter",
                        record_row_delimiter="recordRowDelimiter"
                    ),
                    json_mapping_parameters=kinesisanalytics.CfnApplicationV2.JSONMappingParametersProperty(
                        record_row_path="recordRowPath"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8085a7ac9a94f2612d27fbf2dde753cb1330f65d099d09b6190a18c320484f26)
                check_type(argname="argument csv_mapping_parameters", value=csv_mapping_parameters, expected_type=type_hints["csv_mapping_parameters"])
                check_type(argname="argument json_mapping_parameters", value=json_mapping_parameters, expected_type=type_hints["json_mapping_parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if csv_mapping_parameters is not None:
                self._values["csv_mapping_parameters"] = csv_mapping_parameters
            if json_mapping_parameters is not None:
                self._values["json_mapping_parameters"] = json_mapping_parameters

        @builtins.property
        def csv_mapping_parameters(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.CSVMappingParametersProperty"]]:
            '''Provides additional mapping information when the record format uses delimiters (for example, CSV).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mappingparameters.html#cfn-kinesisanalyticsv2-application-mappingparameters-csvmappingparameters
            '''
            result = self._values.get("csv_mapping_parameters")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.CSVMappingParametersProperty"]], result)

        @builtins.property
        def json_mapping_parameters(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.JSONMappingParametersProperty"]]:
            '''Provides additional mapping information when JSON is the record format on the streaming source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mappingparameters.html#cfn-kinesisanalyticsv2-application-mappingparameters-jsonmappingparameters
            '''
            result = self._values.get("json_mapping_parameters")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.JSONMappingParametersProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MappingParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.MavenReferenceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "artifact_id": "artifactId",
            "group_id": "groupId",
            "version": "version",
        },
    )
    class MavenReferenceProperty:
        def __init__(
            self,
            *,
            artifact_id: builtins.str,
            group_id: builtins.str,
            version: builtins.str,
        ) -> None:
            '''The information required to specify a Maven reference.

            You can use Maven references to specify dependency JAR files.

            :param artifact_id: The artifact ID of the Maven reference.
            :param group_id: The group ID of the Maven reference.
            :param version: The version of the Maven reference.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mavenreference.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                maven_reference_property = kinesisanalytics.CfnApplicationV2.MavenReferenceProperty(
                    artifact_id="artifactId",
                    group_id="groupId",
                    version="version"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__47b603f3420d63acfee6059d061e11eed67a5b676b09c9301e04db0cbc0c8a86)
                check_type(argname="argument artifact_id", value=artifact_id, expected_type=type_hints["artifact_id"])
                check_type(argname="argument group_id", value=group_id, expected_type=type_hints["group_id"])
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "artifact_id": artifact_id,
                "group_id": group_id,
                "version": version,
            }

        @builtins.property
        def artifact_id(self) -> builtins.str:
            '''The artifact ID of the Maven reference.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mavenreference.html#cfn-kinesisanalyticsv2-application-mavenreference-artifactid
            '''
            result = self._values.get("artifact_id")
            assert result is not None, "Required property 'artifact_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def group_id(self) -> builtins.str:
            '''The group ID of the Maven reference.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mavenreference.html#cfn-kinesisanalyticsv2-application-mavenreference-groupid
            '''
            result = self._values.get("group_id")
            assert result is not None, "Required property 'group_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def version(self) -> builtins.str:
            '''The version of the Maven reference.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mavenreference.html#cfn-kinesisanalyticsv2-application-mavenreference-version
            '''
            result = self._values.get("version")
            assert result is not None, "Required property 'version' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MavenReferenceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.MonitoringConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "configuration_type": "configurationType",
            "log_level": "logLevel",
            "metrics_level": "metricsLevel",
        },
    )
    class MonitoringConfigurationProperty:
        def __init__(
            self,
            *,
            configuration_type: builtins.str,
            log_level: typing.Optional[builtins.str] = None,
            metrics_level: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes configuration parameters for Amazon CloudWatch logging for a Java-based Kinesis Data Analytics application.

            For more information about CloudWatch logging, see `Monitoring <https://docs.aws.amazon.com/kinesisanalytics/latest/java/monitoring-overview>`_ .

            :param configuration_type: Describes whether to use the default CloudWatch logging configuration for an application. You must set this property to ``CUSTOM`` in order to set the ``LogLevel`` or ``MetricsLevel`` parameters.
            :param log_level: Describes the verbosity of the CloudWatch Logs for an application.
            :param metrics_level: Describes the granularity of the CloudWatch Logs for an application. The ``Parallelism`` level is not recommended for applications with a Parallelism over 64 due to excessive costs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-monitoringconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                monitoring_configuration_property = kinesisanalytics.CfnApplicationV2.MonitoringConfigurationProperty(
                    configuration_type="configurationType",
                
                    # the properties below are optional
                    log_level="logLevel",
                    metrics_level="metricsLevel"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3211cef7ba767894311acff6375edbc5d8f4622c91dce61e3f8a2b53f48806d3)
                check_type(argname="argument configuration_type", value=configuration_type, expected_type=type_hints["configuration_type"])
                check_type(argname="argument log_level", value=log_level, expected_type=type_hints["log_level"])
                check_type(argname="argument metrics_level", value=metrics_level, expected_type=type_hints["metrics_level"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "configuration_type": configuration_type,
            }
            if log_level is not None:
                self._values["log_level"] = log_level
            if metrics_level is not None:
                self._values["metrics_level"] = metrics_level

        @builtins.property
        def configuration_type(self) -> builtins.str:
            '''Describes whether to use the default CloudWatch logging configuration for an application.

            You must set this property to ``CUSTOM`` in order to set the ``LogLevel`` or ``MetricsLevel`` parameters.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-monitoringconfiguration.html#cfn-kinesisanalyticsv2-application-monitoringconfiguration-configurationtype
            '''
            result = self._values.get("configuration_type")
            assert result is not None, "Required property 'configuration_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def log_level(self) -> typing.Optional[builtins.str]:
            '''Describes the verbosity of the CloudWatch Logs for an application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-monitoringconfiguration.html#cfn-kinesisanalyticsv2-application-monitoringconfiguration-loglevel
            '''
            result = self._values.get("log_level")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def metrics_level(self) -> typing.Optional[builtins.str]:
            '''Describes the granularity of the CloudWatch Logs for an application.

            The ``Parallelism`` level is not recommended for applications with a Parallelism over 64 due to excessive costs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-monitoringconfiguration.html#cfn-kinesisanalyticsv2-application-monitoringconfiguration-metricslevel
            '''
            result = self._values.get("metrics_level")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.ParallelismConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "configuration_type": "configurationType",
            "auto_scaling_enabled": "autoScalingEnabled",
            "parallelism": "parallelism",
            "parallelism_per_kpu": "parallelismPerKpu",
        },
    )
    class ParallelismConfigurationProperty:
        def __init__(
            self,
            *,
            configuration_type: builtins.str,
            auto_scaling_enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            parallelism: typing.Optional[jsii.Number] = None,
            parallelism_per_kpu: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Describes parameters for how a Flink-based Kinesis Data Analytics application executes multiple tasks simultaneously.

            For more information about parallelism, see `Parallel Execution <https://docs.aws.amazon.com/https://ci.apache.org/projects/flink/flink-docs-release-1.8/dev/parallel.html>`_ in the `Apache Flink Documentation <https://docs.aws.amazon.com/https://ci.apache.org/projects/flink/flink-docs-release-1.8/>`_ .

            :param configuration_type: Describes whether the application uses the default parallelism for the Kinesis Data Analytics service. You must set this property to ``CUSTOM`` in order to change your application's ``AutoScalingEnabled`` , ``Parallelism`` , or ``ParallelismPerKPU`` properties.
            :param auto_scaling_enabled: Describes whether the Kinesis Data Analytics service can increase the parallelism of the application in response to increased throughput.
            :param parallelism: Describes the initial number of parallel tasks that a Java-based Kinesis Data Analytics application can perform. The Kinesis Data Analytics service can increase this number automatically if `ParallelismConfiguration:AutoScalingEnabled <https://docs.aws.amazon.com/kinesisanalytics/latest/apiv2/API_ParallelismConfiguration.html#kinesisanalytics-Type-ParallelismConfiguration-AutoScalingEnabled.html>`_ is set to ``true`` .
            :param parallelism_per_kpu: Describes the number of parallel tasks that a Java-based Kinesis Data Analytics application can perform per Kinesis Processing Unit (KPU) used by the application. For more information about KPUs, see `Amazon Kinesis Data Analytics Pricing <https://docs.aws.amazon.com/kinesis/data-analytics/pricing/>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-parallelismconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                parallelism_configuration_property = kinesisanalytics.CfnApplicationV2.ParallelismConfigurationProperty(
                    configuration_type="configurationType",
                
                    # the properties below are optional
                    auto_scaling_enabled=False,
                    parallelism=123,
                    parallelism_per_kpu=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7ab5347c1eedc4da87f0ba76ac3c4b8a6c23f0100696749aa69c2c33f8d040b3)
                check_type(argname="argument configuration_type", value=configuration_type, expected_type=type_hints["configuration_type"])
                check_type(argname="argument auto_scaling_enabled", value=auto_scaling_enabled, expected_type=type_hints["auto_scaling_enabled"])
                check_type(argname="argument parallelism", value=parallelism, expected_type=type_hints["parallelism"])
                check_type(argname="argument parallelism_per_kpu", value=parallelism_per_kpu, expected_type=type_hints["parallelism_per_kpu"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "configuration_type": configuration_type,
            }
            if auto_scaling_enabled is not None:
                self._values["auto_scaling_enabled"] = auto_scaling_enabled
            if parallelism is not None:
                self._values["parallelism"] = parallelism
            if parallelism_per_kpu is not None:
                self._values["parallelism_per_kpu"] = parallelism_per_kpu

        @builtins.property
        def configuration_type(self) -> builtins.str:
            '''Describes whether the application uses the default parallelism for the Kinesis Data Analytics service.

            You must set this property to ``CUSTOM`` in order to change your application's ``AutoScalingEnabled`` , ``Parallelism`` , or ``ParallelismPerKPU`` properties.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-parallelismconfiguration.html#cfn-kinesisanalyticsv2-application-parallelismconfiguration-configurationtype
            '''
            result = self._values.get("configuration_type")
            assert result is not None, "Required property 'configuration_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def auto_scaling_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''Describes whether the Kinesis Data Analytics service can increase the parallelism of the application in response to increased throughput.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-parallelismconfiguration.html#cfn-kinesisanalyticsv2-application-parallelismconfiguration-autoscalingenabled
            '''
            result = self._values.get("auto_scaling_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def parallelism(self) -> typing.Optional[jsii.Number]:
            '''Describes the initial number of parallel tasks that a Java-based Kinesis Data Analytics application can perform.

            The Kinesis Data Analytics service can increase this number automatically if `ParallelismConfiguration:AutoScalingEnabled <https://docs.aws.amazon.com/kinesisanalytics/latest/apiv2/API_ParallelismConfiguration.html#kinesisanalytics-Type-ParallelismConfiguration-AutoScalingEnabled.html>`_ is set to ``true`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-parallelismconfiguration.html#cfn-kinesisanalyticsv2-application-parallelismconfiguration-parallelism
            '''
            result = self._values.get("parallelism")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def parallelism_per_kpu(self) -> typing.Optional[jsii.Number]:
            '''Describes the number of parallel tasks that a Java-based Kinesis Data Analytics application can perform per Kinesis Processing Unit (KPU) used by the application.

            For more information about KPUs, see `Amazon Kinesis Data Analytics Pricing <https://docs.aws.amazon.com/kinesis/data-analytics/pricing/>`_ .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-parallelismconfiguration.html#cfn-kinesisanalyticsv2-application-parallelismconfiguration-parallelismperkpu
            '''
            result = self._values.get("parallelism_per_kpu")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParallelismConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.PropertyGroupProperty",
        jsii_struct_bases=[],
        name_mapping={
            "property_group_id": "propertyGroupId",
            "property_map": "propertyMap",
        },
    )
    class PropertyGroupProperty:
        def __init__(
            self,
            *,
            property_group_id: typing.Optional[builtins.str] = None,
            property_map: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
        ) -> None:
            '''Property key-value pairs passed into an application.

            :param property_group_id: Describes the key of an application execution property key-value pair.
            :param property_map: Describes the value of an application execution property key-value pair.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-propertygroup.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                property_group_property = kinesisanalytics.CfnApplicationV2.PropertyGroupProperty(
                    property_group_id="propertyGroupId",
                    property_map={
                        "property_map_key": "propertyMap"
                    }
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__099a7b4afd271a44811681d03d9b38f608cfc1262b7e05cb615232f3284d1635)
                check_type(argname="argument property_group_id", value=property_group_id, expected_type=type_hints["property_group_id"])
                check_type(argname="argument property_map", value=property_map, expected_type=type_hints["property_map"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if property_group_id is not None:
                self._values["property_group_id"] = property_group_id
            if property_map is not None:
                self._values["property_map"] = property_map

        @builtins.property
        def property_group_id(self) -> typing.Optional[builtins.str]:
            '''Describes the key of an application execution property key-value pair.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-propertygroup.html#cfn-kinesisanalyticsv2-application-propertygroup-propertygroupid
            '''
            result = self._values.get("property_group_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def property_map(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
            '''Describes the value of an application execution property key-value pair.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-propertygroup.html#cfn-kinesisanalyticsv2-application-propertygroup-propertymap
            '''
            result = self._values.get("property_map")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PropertyGroupProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.RecordColumnProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "sql_type": "sqlType", "mapping": "mapping"},
    )
    class RecordColumnProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            sql_type: builtins.str,
            mapping: typing.Optional[builtins.str] = None,
        ) -> None:
            '''For a SQL-based Kinesis Data Analytics application, describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.

            Also used to describe the format of the reference data source.

            :param name: The name of the column that is created in the in-application input stream or reference table.
            :param sql_type: The type of column created in the in-application input stream or reference table.
            :param mapping: A reference to the data element in the streaming input or the reference data source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordcolumn.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                record_column_property = kinesisanalytics.CfnApplicationV2.RecordColumnProperty(
                    name="name",
                    sql_type="sqlType",
                
                    # the properties below are optional
                    mapping="mapping"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2e57c255a4355974df7e23bb9e32e3f6fe0123fd84b8f76526ba4fac1ba0717c)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument sql_type", value=sql_type, expected_type=type_hints["sql_type"])
                check_type(argname="argument mapping", value=mapping, expected_type=type_hints["mapping"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "sql_type": sql_type,
            }
            if mapping is not None:
                self._values["mapping"] = mapping

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the column that is created in the in-application input stream or reference table.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordcolumn.html#cfn-kinesisanalyticsv2-application-recordcolumn-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def sql_type(self) -> builtins.str:
            '''The type of column created in the in-application input stream or reference table.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordcolumn.html#cfn-kinesisanalyticsv2-application-recordcolumn-sqltype
            '''
            result = self._values.get("sql_type")
            assert result is not None, "Required property 'sql_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def mapping(self) -> typing.Optional[builtins.str]:
            '''A reference to the data element in the streaming input or the reference data source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordcolumn.html#cfn-kinesisanalyticsv2-application-recordcolumn-mapping
            '''
            result = self._values.get("mapping")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RecordColumnProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.RecordFormatProperty",
        jsii_struct_bases=[],
        name_mapping={
            "record_format_type": "recordFormatType",
            "mapping_parameters": "mappingParameters",
        },
    )
    class RecordFormatProperty:
        def __init__(
            self,
            *,
            record_format_type: builtins.str,
            mapping_parameters: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationV2.MappingParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''For a SQL-based Kinesis Data Analytics application, describes the record format and relevant mapping information that should be applied to schematize the records on the stream.

            :param record_format_type: The type of record format.
            :param mapping_parameters: When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordformat.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                record_format_property = kinesisanalytics.CfnApplicationV2.RecordFormatProperty(
                    record_format_type="recordFormatType",
                
                    # the properties below are optional
                    mapping_parameters=kinesisanalytics.CfnApplicationV2.MappingParametersProperty(
                        csv_mapping_parameters=kinesisanalytics.CfnApplicationV2.CSVMappingParametersProperty(
                            record_column_delimiter="recordColumnDelimiter",
                            record_row_delimiter="recordRowDelimiter"
                        ),
                        json_mapping_parameters=kinesisanalytics.CfnApplicationV2.JSONMappingParametersProperty(
                            record_row_path="recordRowPath"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__93d7f021f37b7b8e87adbb316c311484e7d3016e44192e70991e362f963613e1)
                check_type(argname="argument record_format_type", value=record_format_type, expected_type=type_hints["record_format_type"])
                check_type(argname="argument mapping_parameters", value=mapping_parameters, expected_type=type_hints["mapping_parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "record_format_type": record_format_type,
            }
            if mapping_parameters is not None:
                self._values["mapping_parameters"] = mapping_parameters

        @builtins.property
        def record_format_type(self) -> builtins.str:
            '''The type of record format.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordformat.html#cfn-kinesisanalyticsv2-application-recordformat-recordformattype
            '''
            result = self._values.get("record_format_type")
            assert result is not None, "Required property 'record_format_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def mapping_parameters(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.MappingParametersProperty"]]:
            '''When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordformat.html#cfn-kinesisanalyticsv2-application-recordformat-mappingparameters
            '''
            result = self._values.get("mapping_parameters")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.MappingParametersProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RecordFormatProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.RunConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "application_restore_configuration": "applicationRestoreConfiguration",
            "flink_run_configuration": "flinkRunConfiguration",
        },
    )
    class RunConfigurationProperty:
        def __init__(
            self,
            *,
            application_restore_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationV2.ApplicationRestoreConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            flink_run_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationV2.FlinkRunConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Describes the starting parameters for an Kinesis Data Analytics application.

            :param application_restore_configuration: Describes the restore behavior of a restarting application.
            :param flink_run_configuration: Describes the starting parameters for a Flink-based Kinesis Data Analytics application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-runconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                run_configuration_property = kinesisanalytics.CfnApplicationV2.RunConfigurationProperty(
                    application_restore_configuration=kinesisanalytics.CfnApplicationV2.ApplicationRestoreConfigurationProperty(
                        application_restore_type="applicationRestoreType",
                
                        # the properties below are optional
                        snapshot_name="snapshotName"
                    ),
                    flink_run_configuration=kinesisanalytics.CfnApplicationV2.FlinkRunConfigurationProperty(
                        allow_non_restored_state=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__74639cb20e6f9d9d15a507ae174fb1314525a03965aad815820e2c7a887a3b40)
                check_type(argname="argument application_restore_configuration", value=application_restore_configuration, expected_type=type_hints["application_restore_configuration"])
                check_type(argname="argument flink_run_configuration", value=flink_run_configuration, expected_type=type_hints["flink_run_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if application_restore_configuration is not None:
                self._values["application_restore_configuration"] = application_restore_configuration
            if flink_run_configuration is not None:
                self._values["flink_run_configuration"] = flink_run_configuration

        @builtins.property
        def application_restore_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.ApplicationRestoreConfigurationProperty"]]:
            '''Describes the restore behavior of a restarting application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-runconfiguration.html#cfn-kinesisanalyticsv2-application-runconfiguration-applicationrestoreconfiguration
            '''
            result = self._values.get("application_restore_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.ApplicationRestoreConfigurationProperty"]], result)

        @builtins.property
        def flink_run_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.FlinkRunConfigurationProperty"]]:
            '''Describes the starting parameters for a Flink-based Kinesis Data Analytics application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-runconfiguration.html#cfn-kinesisanalyticsv2-application-runconfiguration-flinkrunconfiguration
            '''
            result = self._values.get("flink_run_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.FlinkRunConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RunConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.S3ContentBaseLocationProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket_arn": "bucketArn", "base_path": "basePath"},
    )
    class S3ContentBaseLocationProperty:
        def __init__(
            self,
            *,
            bucket_arn: builtins.str,
            base_path: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The base location of the Amazon Data Analytics application.

            :param bucket_arn: The Amazon Resource Name (ARN) of the S3 bucket.
            :param base_path: The base path for the S3 bucket.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentbaselocation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                s3_content_base_location_property = kinesisanalytics.CfnApplicationV2.S3ContentBaseLocationProperty(
                    bucket_arn="bucketArn",
                
                    # the properties below are optional
                    base_path="basePath"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7167b363d560bcfe46dbd2d63496f185be4afca4b0a3c36f59045ced8dda06f6)
                check_type(argname="argument bucket_arn", value=bucket_arn, expected_type=type_hints["bucket_arn"])
                check_type(argname="argument base_path", value=base_path, expected_type=type_hints["base_path"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket_arn": bucket_arn,
            }
            if base_path is not None:
                self._values["base_path"] = base_path

        @builtins.property
        def bucket_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the S3 bucket.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentbaselocation.html#cfn-kinesisanalyticsv2-application-s3contentbaselocation-bucketarn
            '''
            result = self._values.get("bucket_arn")
            assert result is not None, "Required property 'bucket_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def base_path(self) -> typing.Optional[builtins.str]:
            '''The base path for the S3 bucket.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentbaselocation.html#cfn-kinesisanalyticsv2-application-s3contentbaselocation-basepath
            '''
            result = self._values.get("base_path")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3ContentBaseLocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.S3ContentLocationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket_arn": "bucketArn",
            "file_key": "fileKey",
            "object_version": "objectVersion",
        },
    )
    class S3ContentLocationProperty:
        def __init__(
            self,
            *,
            bucket_arn: builtins.str,
            file_key: builtins.str,
            object_version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The location of an application or a custom artifact.

            :param bucket_arn: The Amazon Resource Name (ARN) for the S3 bucket containing the application code.
            :param file_key: The file key for the object containing the application code.
            :param object_version: The version of the object containing the application code.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentlocation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                s3_content_location_property = kinesisanalytics.CfnApplicationV2.S3ContentLocationProperty(
                    bucket_arn="bucketArn",
                    file_key="fileKey",
                
                    # the properties below are optional
                    object_version="objectVersion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4b1da8f64d557313805c24a5815c1840cc27784f5fcf5b620d5bbad81a9fb779)
                check_type(argname="argument bucket_arn", value=bucket_arn, expected_type=type_hints["bucket_arn"])
                check_type(argname="argument file_key", value=file_key, expected_type=type_hints["file_key"])
                check_type(argname="argument object_version", value=object_version, expected_type=type_hints["object_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket_arn": bucket_arn,
                "file_key": file_key,
            }
            if object_version is not None:
                self._values["object_version"] = object_version

        @builtins.property
        def bucket_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) for the S3 bucket containing the application code.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentlocation.html#cfn-kinesisanalyticsv2-application-s3contentlocation-bucketarn
            '''
            result = self._values.get("bucket_arn")
            assert result is not None, "Required property 'bucket_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def file_key(self) -> builtins.str:
            '''The file key for the object containing the application code.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentlocation.html#cfn-kinesisanalyticsv2-application-s3contentlocation-filekey
            '''
            result = self._values.get("file_key")
            assert result is not None, "Required property 'file_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def object_version(self) -> typing.Optional[builtins.str]:
            '''The version of the object containing the application code.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentlocation.html#cfn-kinesisanalyticsv2-application-s3contentlocation-objectversion
            '''
            result = self._values.get("object_version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3ContentLocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.SqlApplicationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"inputs": "inputs"},
    )
    class SqlApplicationConfigurationProperty:
        def __init__(
            self,
            *,
            inputs: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationV2.InputProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Describes the inputs, outputs, and reference data sources for a SQL-based Kinesis Data Analytics application.

            :param inputs: The array of `Input <https://docs.aws.amazon.com/kinesisanalytics/latest/apiv2/API_Input.html>`_ objects describing the input streams used by the application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-sqlapplicationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                sql_application_configuration_property = kinesisanalytics.CfnApplicationV2.SqlApplicationConfigurationProperty(
                    inputs=[kinesisanalytics.CfnApplicationV2.InputProperty(
                        input_schema=kinesisanalytics.CfnApplicationV2.InputSchemaProperty(
                            record_columns=[kinesisanalytics.CfnApplicationV2.RecordColumnProperty(
                                name="name",
                                sql_type="sqlType",
                
                                # the properties below are optional
                                mapping="mapping"
                            )],
                            record_format=kinesisanalytics.CfnApplicationV2.RecordFormatProperty(
                                record_format_type="recordFormatType",
                
                                # the properties below are optional
                                mapping_parameters=kinesisanalytics.CfnApplicationV2.MappingParametersProperty(
                                    csv_mapping_parameters=kinesisanalytics.CfnApplicationV2.CSVMappingParametersProperty(
                                        record_column_delimiter="recordColumnDelimiter",
                                        record_row_delimiter="recordRowDelimiter"
                                    ),
                                    json_mapping_parameters=kinesisanalytics.CfnApplicationV2.JSONMappingParametersProperty(
                                        record_row_path="recordRowPath"
                                    )
                                )
                            ),
                
                            # the properties below are optional
                            record_encoding="recordEncoding"
                        ),
                        name_prefix="namePrefix",
                
                        # the properties below are optional
                        input_parallelism=kinesisanalytics.CfnApplicationV2.InputParallelismProperty(
                            count=123
                        ),
                        input_processing_configuration=kinesisanalytics.CfnApplicationV2.InputProcessingConfigurationProperty(
                            input_lambda_processor=kinesisanalytics.CfnApplicationV2.InputLambdaProcessorProperty(
                                resource_arn="resourceArn"
                            )
                        ),
                        kinesis_firehose_input=kinesisanalytics.CfnApplicationV2.KinesisFirehoseInputProperty(
                            resource_arn="resourceArn"
                        ),
                        kinesis_streams_input=kinesisanalytics.CfnApplicationV2.KinesisStreamsInputProperty(
                            resource_arn="resourceArn"
                        )
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3ba6abf1ac5b4329c6f3e661e65c682bc3755088f0c7e2b18279c84e78027ee9)
                check_type(argname="argument inputs", value=inputs, expected_type=type_hints["inputs"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if inputs is not None:
                self._values["inputs"] = inputs

        @builtins.property
        def inputs(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.InputProperty"]]]]:
            '''The array of `Input <https://docs.aws.amazon.com/kinesisanalytics/latest/apiv2/API_Input.html>`_ objects describing the input streams used by the application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-sqlapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-sqlapplicationconfiguration-inputs
            '''
            result = self._values.get("inputs")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.InputProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SqlApplicationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.VpcConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "security_group_ids": "securityGroupIds",
            "subnet_ids": "subnetIds",
        },
    )
    class VpcConfigurationProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Sequence[builtins.str],
            subnet_ids: typing.Sequence[builtins.str],
        ) -> None:
            '''Describes the parameters of a VPC used by the application.

            :param security_group_ids: The array of `SecurityGroup <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SecurityGroup.html>`_ IDs used by the VPC configuration.
            :param subnet_ids: The array of `Subnet <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Subnet.html>`_ IDs used by the VPC configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-vpcconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                vpc_configuration_property = kinesisanalytics.CfnApplicationV2.VpcConfigurationProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__327357f6841ab960621386fdfd3e5a10084879071611b1e8550b74e6eb46abbc)
                check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
                check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "security_group_ids": security_group_ids,
                "subnet_ids": subnet_ids,
            }

        @builtins.property
        def security_group_ids(self) -> typing.List[builtins.str]:
            '''The array of `SecurityGroup <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SecurityGroup.html>`_ IDs used by the VPC configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-vpcconfiguration.html#cfn-kinesisanalyticsv2-application-vpcconfiguration-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            assert result is not None, "Required property 'security_group_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnet_ids(self) -> typing.List[builtins.str]:
            '''The array of `Subnet <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Subnet.html>`_ IDs used by the VPC configuration.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-vpcconfiguration.html#cfn-kinesisanalyticsv2-application-vpcconfiguration-subnetids
            '''
            result = self._values.get("subnet_ids")
            assert result is not None, "Required property 'subnet_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.ZeppelinApplicationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog_configuration": "catalogConfiguration",
            "custom_artifacts_configuration": "customArtifactsConfiguration",
            "deploy_as_application_configuration": "deployAsApplicationConfiguration",
            "monitoring_configuration": "monitoringConfiguration",
        },
    )
    class ZeppelinApplicationConfigurationProperty:
        def __init__(
            self,
            *,
            catalog_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationV2.CatalogConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            custom_artifacts_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationV2.CustomArtifactConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            deploy_as_application_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationV2.DeployAsApplicationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            monitoring_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnApplicationV2.ZeppelinMonitoringConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The configuration of a Kinesis Data Analytics Studio notebook.

            :param catalog_configuration: The Amazon Glue Data Catalog that you use in queries in a Kinesis Data Analytics Studio notebook.
            :param custom_artifacts_configuration: A list of ``CustomArtifactConfiguration`` objects.
            :param deploy_as_application_configuration: The information required to deploy a Kinesis Data Analytics Studio notebook as an application with durable state.
            :param monitoring_configuration: The monitoring configuration of a Kinesis Data Analytics Studio notebook.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinapplicationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                zeppelin_application_configuration_property = kinesisanalytics.CfnApplicationV2.ZeppelinApplicationConfigurationProperty(
                    catalog_configuration=kinesisanalytics.CfnApplicationV2.CatalogConfigurationProperty(
                        glue_data_catalog_configuration=kinesisanalytics.CfnApplicationV2.GlueDataCatalogConfigurationProperty(
                            database_arn="databaseArn"
                        )
                    ),
                    custom_artifacts_configuration=[kinesisanalytics.CfnApplicationV2.CustomArtifactConfigurationProperty(
                        artifact_type="artifactType",
                
                        # the properties below are optional
                        maven_reference=kinesisanalytics.CfnApplicationV2.MavenReferenceProperty(
                            artifact_id="artifactId",
                            group_id="groupId",
                            version="version"
                        ),
                        s3_content_location=kinesisanalytics.CfnApplicationV2.S3ContentLocationProperty(
                            bucket_arn="bucketArn",
                            file_key="fileKey",
                
                            # the properties below are optional
                            object_version="objectVersion"
                        )
                    )],
                    deploy_as_application_configuration=kinesisanalytics.CfnApplicationV2.DeployAsApplicationConfigurationProperty(
                        s3_content_location=kinesisanalytics.CfnApplicationV2.S3ContentBaseLocationProperty(
                            bucket_arn="bucketArn",
                
                            # the properties below are optional
                            base_path="basePath"
                        )
                    ),
                    monitoring_configuration=kinesisanalytics.CfnApplicationV2.ZeppelinMonitoringConfigurationProperty(
                        log_level="logLevel"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__743da7b5de18410d73e8ac40fdef66769edc9ded035c253ed7e10cc343eaa8cd)
                check_type(argname="argument catalog_configuration", value=catalog_configuration, expected_type=type_hints["catalog_configuration"])
                check_type(argname="argument custom_artifacts_configuration", value=custom_artifacts_configuration, expected_type=type_hints["custom_artifacts_configuration"])
                check_type(argname="argument deploy_as_application_configuration", value=deploy_as_application_configuration, expected_type=type_hints["deploy_as_application_configuration"])
                check_type(argname="argument monitoring_configuration", value=monitoring_configuration, expected_type=type_hints["monitoring_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if catalog_configuration is not None:
                self._values["catalog_configuration"] = catalog_configuration
            if custom_artifacts_configuration is not None:
                self._values["custom_artifacts_configuration"] = custom_artifacts_configuration
            if deploy_as_application_configuration is not None:
                self._values["deploy_as_application_configuration"] = deploy_as_application_configuration
            if monitoring_configuration is not None:
                self._values["monitoring_configuration"] = monitoring_configuration

        @builtins.property
        def catalog_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.CatalogConfigurationProperty"]]:
            '''The Amazon Glue Data Catalog that you use in queries in a Kinesis Data Analytics Studio notebook.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-zeppelinapplicationconfiguration-catalogconfiguration
            '''
            result = self._values.get("catalog_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.CatalogConfigurationProperty"]], result)

        @builtins.property
        def custom_artifacts_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.CustomArtifactConfigurationProperty"]]]]:
            '''A list of ``CustomArtifactConfiguration`` objects.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-zeppelinapplicationconfiguration-customartifactsconfiguration
            '''
            result = self._values.get("custom_artifacts_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.CustomArtifactConfigurationProperty"]]]], result)

        @builtins.property
        def deploy_as_application_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.DeployAsApplicationConfigurationProperty"]]:
            '''The information required to deploy a Kinesis Data Analytics Studio notebook as an application with durable state.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-zeppelinapplicationconfiguration-deployasapplicationconfiguration
            '''
            result = self._values.get("deploy_as_application_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.DeployAsApplicationConfigurationProperty"]], result)

        @builtins.property
        def monitoring_configuration(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.ZeppelinMonitoringConfigurationProperty"]]:
            '''The monitoring configuration of a Kinesis Data Analytics Studio notebook.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-zeppelinapplicationconfiguration-monitoringconfiguration
            '''
            result = self._values.get("monitoring_configuration")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnApplicationV2.ZeppelinMonitoringConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ZeppelinApplicationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.ZeppelinMonitoringConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"log_level": "logLevel"},
    )
    class ZeppelinMonitoringConfigurationProperty:
        def __init__(self, *, log_level: typing.Optional[builtins.str] = None) -> None:
            '''Describes configuration parameters for Amazon CloudWatch logging for a Kinesis Data Analytics Studio notebook.

            For more information about CloudWatch logging, see `Monitoring <https://docs.aws.amazon.com/kinesisanalytics/latest/java/monitoring-overview.html>`_ .

            :param log_level: The verbosity of the CloudWatch Logs for an application. You can set it to ``INFO`` , ``WARN`` , ``ERROR`` , or ``DEBUG`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinmonitoringconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_kinesisanalytics as kinesisanalytics
                
                zeppelin_monitoring_configuration_property = kinesisanalytics.CfnApplicationV2.ZeppelinMonitoringConfigurationProperty(
                    log_level="logLevel"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e112e9d2fda05ec52aae23ada0044cbfac5b0a160e8453ed853c9c18ebaf2ebe)
                check_type(argname="argument log_level", value=log_level, expected_type=type_hints["log_level"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if log_level is not None:
                self._values["log_level"] = log_level

        @builtins.property
        def log_level(self) -> typing.Optional[builtins.str]:
            '''The verbosity of the CloudWatch Logs for an application.

            You can set it to ``INFO`` , ``WARN`` , ``ERROR`` , or ``DEBUG`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-zeppelinmonitoringconfiguration.html#cfn-kinesisanalyticsv2-application-zeppelinmonitoringconfiguration-loglevel
            '''
            result = self._values.get("log_level")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ZeppelinMonitoringConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2Props",
    jsii_struct_bases=[],
    name_mapping={
        "runtime_environment": "runtimeEnvironment",
        "service_execution_role": "serviceExecutionRole",
        "application_configuration": "applicationConfiguration",
        "application_description": "applicationDescription",
        "application_maintenance_configuration": "applicationMaintenanceConfiguration",
        "application_mode": "applicationMode",
        "application_name": "applicationName",
        "run_configuration": "runConfiguration",
        "tags": "tags",
    },
)
class CfnApplicationV2Props:
    def __init__(
        self,
        *,
        runtime_environment: builtins.str,
        service_execution_role: builtins.str,
        application_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.ApplicationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        application_description: typing.Optional[builtins.str] = None,
        application_maintenance_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.ApplicationMaintenanceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        application_mode: typing.Optional[builtins.str] = None,
        application_name: typing.Optional[builtins.str] = None,
        run_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.RunConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnApplicationV2``.

        :param runtime_environment: The runtime environment for the application.
        :param service_execution_role: Specifies the IAM role that the application uses to access external resources.
        :param application_configuration: Use this parameter to configure the application.
        :param application_description: The description of the application.
        :param application_maintenance_configuration: ``AWS::KinesisAnalyticsV2::Application.ApplicationMaintenanceConfiguration``.
        :param application_mode: To create a Kinesis Data Analytics Studio notebook, you must set the mode to ``INTERACTIVE`` . However, for a Kinesis Data Analytics for Apache Flink application, the mode is optional.
        :param application_name: The name of the application.
        :param run_configuration: ``AWS::KinesisAnalyticsV2::Application.RunConfiguration``.
        :param tags: A list of one or more tags to assign to the application. A tag is a key-value pair that identifies an application. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_kinesisanalytics as kinesisanalytics
            
            cfn_application_v2_props = kinesisanalytics.CfnApplicationV2Props(
                runtime_environment="runtimeEnvironment",
                service_execution_role="serviceExecutionRole",
            
                # the properties below are optional
                application_configuration=kinesisanalytics.CfnApplicationV2.ApplicationConfigurationProperty(
                    application_code_configuration=kinesisanalytics.CfnApplicationV2.ApplicationCodeConfigurationProperty(
                        code_content=kinesisanalytics.CfnApplicationV2.CodeContentProperty(
                            s3_content_location=kinesisanalytics.CfnApplicationV2.S3ContentLocationProperty(
                                bucket_arn="bucketArn",
                                file_key="fileKey",
            
                                # the properties below are optional
                                object_version="objectVersion"
                            ),
                            text_content="textContent",
                            zip_file_content="zipFileContent"
                        ),
                        code_content_type="codeContentType"
                    ),
                    application_snapshot_configuration=kinesisanalytics.CfnApplicationV2.ApplicationSnapshotConfigurationProperty(
                        snapshots_enabled=False
                    ),
                    environment_properties=kinesisanalytics.CfnApplicationV2.EnvironmentPropertiesProperty(
                        property_groups=[kinesisanalytics.CfnApplicationV2.PropertyGroupProperty(
                            property_group_id="propertyGroupId",
                            property_map={
                                "property_map_key": "propertyMap"
                            }
                        )]
                    ),
                    flink_application_configuration=kinesisanalytics.CfnApplicationV2.FlinkApplicationConfigurationProperty(
                        checkpoint_configuration=kinesisanalytics.CfnApplicationV2.CheckpointConfigurationProperty(
                            configuration_type="configurationType",
            
                            # the properties below are optional
                            checkpointing_enabled=False,
                            checkpoint_interval=123,
                            min_pause_between_checkpoints=123
                        ),
                        monitoring_configuration=kinesisanalytics.CfnApplicationV2.MonitoringConfigurationProperty(
                            configuration_type="configurationType",
            
                            # the properties below are optional
                            log_level="logLevel",
                            metrics_level="metricsLevel"
                        ),
                        parallelism_configuration=kinesisanalytics.CfnApplicationV2.ParallelismConfigurationProperty(
                            configuration_type="configurationType",
            
                            # the properties below are optional
                            auto_scaling_enabled=False,
                            parallelism=123,
                            parallelism_per_kpu=123
                        )
                    ),
                    sql_application_configuration=kinesisanalytics.CfnApplicationV2.SqlApplicationConfigurationProperty(
                        inputs=[kinesisanalytics.CfnApplicationV2.InputProperty(
                            input_schema=kinesisanalytics.CfnApplicationV2.InputSchemaProperty(
                                record_columns=[kinesisanalytics.CfnApplicationV2.RecordColumnProperty(
                                    name="name",
                                    sql_type="sqlType",
            
                                    # the properties below are optional
                                    mapping="mapping"
                                )],
                                record_format=kinesisanalytics.CfnApplicationV2.RecordFormatProperty(
                                    record_format_type="recordFormatType",
            
                                    # the properties below are optional
                                    mapping_parameters=kinesisanalytics.CfnApplicationV2.MappingParametersProperty(
                                        csv_mapping_parameters=kinesisanalytics.CfnApplicationV2.CSVMappingParametersProperty(
                                            record_column_delimiter="recordColumnDelimiter",
                                            record_row_delimiter="recordRowDelimiter"
                                        ),
                                        json_mapping_parameters=kinesisanalytics.CfnApplicationV2.JSONMappingParametersProperty(
                                            record_row_path="recordRowPath"
                                        )
                                    )
                                ),
            
                                # the properties below are optional
                                record_encoding="recordEncoding"
                            ),
                            name_prefix="namePrefix",
            
                            # the properties below are optional
                            input_parallelism=kinesisanalytics.CfnApplicationV2.InputParallelismProperty(
                                count=123
                            ),
                            input_processing_configuration=kinesisanalytics.CfnApplicationV2.InputProcessingConfigurationProperty(
                                input_lambda_processor=kinesisanalytics.CfnApplicationV2.InputLambdaProcessorProperty(
                                    resource_arn="resourceArn"
                                )
                            ),
                            kinesis_firehose_input=kinesisanalytics.CfnApplicationV2.KinesisFirehoseInputProperty(
                                resource_arn="resourceArn"
                            ),
                            kinesis_streams_input=kinesisanalytics.CfnApplicationV2.KinesisStreamsInputProperty(
                                resource_arn="resourceArn"
                            )
                        )]
                    ),
                    vpc_configurations=[kinesisanalytics.CfnApplicationV2.VpcConfigurationProperty(
                        security_group_ids=["securityGroupIds"],
                        subnet_ids=["subnetIds"]
                    )],
                    zeppelin_application_configuration=kinesisanalytics.CfnApplicationV2.ZeppelinApplicationConfigurationProperty(
                        catalog_configuration=kinesisanalytics.CfnApplicationV2.CatalogConfigurationProperty(
                            glue_data_catalog_configuration=kinesisanalytics.CfnApplicationV2.GlueDataCatalogConfigurationProperty(
                                database_arn="databaseArn"
                            )
                        ),
                        custom_artifacts_configuration=[kinesisanalytics.CfnApplicationV2.CustomArtifactConfigurationProperty(
                            artifact_type="artifactType",
            
                            # the properties below are optional
                            maven_reference=kinesisanalytics.CfnApplicationV2.MavenReferenceProperty(
                                artifact_id="artifactId",
                                group_id="groupId",
                                version="version"
                            ),
                            s3_content_location=kinesisanalytics.CfnApplicationV2.S3ContentLocationProperty(
                                bucket_arn="bucketArn",
                                file_key="fileKey",
            
                                # the properties below are optional
                                object_version="objectVersion"
                            )
                        )],
                        deploy_as_application_configuration=kinesisanalytics.CfnApplicationV2.DeployAsApplicationConfigurationProperty(
                            s3_content_location=kinesisanalytics.CfnApplicationV2.S3ContentBaseLocationProperty(
                                bucket_arn="bucketArn",
            
                                # the properties below are optional
                                base_path="basePath"
                            )
                        ),
                        monitoring_configuration=kinesisanalytics.CfnApplicationV2.ZeppelinMonitoringConfigurationProperty(
                            log_level="logLevel"
                        )
                    )
                ),
                application_description="applicationDescription",
                application_maintenance_configuration=kinesisanalytics.CfnApplicationV2.ApplicationMaintenanceConfigurationProperty(
                    application_maintenance_window_start_time="applicationMaintenanceWindowStartTime"
                ),
                application_mode="applicationMode",
                application_name="applicationName",
                run_configuration=kinesisanalytics.CfnApplicationV2.RunConfigurationProperty(
                    application_restore_configuration=kinesisanalytics.CfnApplicationV2.ApplicationRestoreConfigurationProperty(
                        application_restore_type="applicationRestoreType",
            
                        # the properties below are optional
                        snapshot_name="snapshotName"
                    ),
                    flink_run_configuration=kinesisanalytics.CfnApplicationV2.FlinkRunConfigurationProperty(
                        allow_non_restored_state=False
                    )
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__154e6fc7679982e744d86ce87daeaf267e11d389ca8a5533eae5f42e7278a344)
            check_type(argname="argument runtime_environment", value=runtime_environment, expected_type=type_hints["runtime_environment"])
            check_type(argname="argument service_execution_role", value=service_execution_role, expected_type=type_hints["service_execution_role"])
            check_type(argname="argument application_configuration", value=application_configuration, expected_type=type_hints["application_configuration"])
            check_type(argname="argument application_description", value=application_description, expected_type=type_hints["application_description"])
            check_type(argname="argument application_maintenance_configuration", value=application_maintenance_configuration, expected_type=type_hints["application_maintenance_configuration"])
            check_type(argname="argument application_mode", value=application_mode, expected_type=type_hints["application_mode"])
            check_type(argname="argument application_name", value=application_name, expected_type=type_hints["application_name"])
            check_type(argname="argument run_configuration", value=run_configuration, expected_type=type_hints["run_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "runtime_environment": runtime_environment,
            "service_execution_role": service_execution_role,
        }
        if application_configuration is not None:
            self._values["application_configuration"] = application_configuration
        if application_description is not None:
            self._values["application_description"] = application_description
        if application_maintenance_configuration is not None:
            self._values["application_maintenance_configuration"] = application_maintenance_configuration
        if application_mode is not None:
            self._values["application_mode"] = application_mode
        if application_name is not None:
            self._values["application_name"] = application_name
        if run_configuration is not None:
            self._values["run_configuration"] = run_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def runtime_environment(self) -> builtins.str:
        '''The runtime environment for the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-runtimeenvironment
        '''
        result = self._values.get("runtime_environment")
        assert result is not None, "Required property 'runtime_environment' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_execution_role(self) -> builtins.str:
        '''Specifies the IAM role that the application uses to access external resources.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-serviceexecutionrole
        '''
        result = self._values.get("service_execution_role")
        assert result is not None, "Required property 'service_execution_role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def application_configuration(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnApplicationV2.ApplicationConfigurationProperty]]:
        '''Use this parameter to configure the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-applicationconfiguration
        '''
        result = self._values.get("application_configuration")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnApplicationV2.ApplicationConfigurationProperty]], result)

    @builtins.property
    def application_description(self) -> typing.Optional[builtins.str]:
        '''The description of the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-applicationdescription
        '''
        result = self._values.get("application_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def application_maintenance_configuration(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnApplicationV2.ApplicationMaintenanceConfigurationProperty]]:
        '''``AWS::KinesisAnalyticsV2::Application.ApplicationMaintenanceConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-applicationmaintenanceconfiguration
        '''
        result = self._values.get("application_maintenance_configuration")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnApplicationV2.ApplicationMaintenanceConfigurationProperty]], result)

    @builtins.property
    def application_mode(self) -> typing.Optional[builtins.str]:
        '''To create a Kinesis Data Analytics Studio notebook, you must set the mode to ``INTERACTIVE`` .

        However, for a Kinesis Data Analytics for Apache Flink application, the mode is optional.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-applicationmode
        '''
        result = self._values.get("application_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def application_name(self) -> typing.Optional[builtins.str]:
        '''The name of the application.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-applicationname
        '''
        result = self._values.get("application_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def run_configuration(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnApplicationV2.RunConfigurationProperty]]:
        '''``AWS::KinesisAnalyticsV2::Application.RunConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-runconfiguration
        '''
        result = self._values.get("run_configuration")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnApplicationV2.RunConfigurationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]]:
        '''A list of one or more tags to assign to the application.

        A tag is a key-value pair that identifies an application. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationV2Props(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnApplication",
    "CfnApplicationCloudWatchLoggingOptionV2",
    "CfnApplicationCloudWatchLoggingOptionV2Props",
    "CfnApplicationOutput",
    "CfnApplicationOutputProps",
    "CfnApplicationOutputV2",
    "CfnApplicationOutputV2Props",
    "CfnApplicationProps",
    "CfnApplicationReferenceDataSource",
    "CfnApplicationReferenceDataSourceProps",
    "CfnApplicationReferenceDataSourceV2",
    "CfnApplicationReferenceDataSourceV2Props",
    "CfnApplicationV2",
    "CfnApplicationV2Props",
]

publication.publish()

def _typecheckingstub__32b2db479ff8f4ba54c3123098b7a543a37fe947f8f5f4b0b22c95d87a5a8740(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    inputs: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[typing.Union[CfnApplication.InputProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable]]],
    application_code: typing.Optional[builtins.str] = None,
    application_description: typing.Optional[builtins.str] = None,
    application_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf74750202e5145822e6a4dca5cc71c2d6ef1b3f369c92b0efaba7f825ea508d(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__629352554e0b4ad1cd72d357cee75145e61011fa4d3ba6f231cbd04963737c9c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d80027fd700f25d7baa2fbc8e741e19f97183215c89b5e1b89612e8dee4c296f(
    value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[CfnApplication.InputProperty, _aws_cdk_core_f4b25747.IResolvable]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a16a017ea1ebcc0c6a4c3bb5adfcaa90d0472f728a593cfdbecb8ef9c5bde14(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50745cd224885ded2718f0e25dd767d80309310eb69d93f96547a714cda10954(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea4f2ecb41cadbc4bf511976fe42ebff8c97e03842733b3ee5f19e72a70a5f5b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d6e953229adebd993016e0224131ee9512a01531f068b0cecfbc8bf612c1be5(
    *,
    record_column_delimiter: builtins.str,
    record_row_delimiter: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6ee71d0e66f57a3eded5ebba8cdd3807d5cbff01049d07b2658efa0d8729aca(
    *,
    resource_arn: builtins.str,
    role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d541b02d706686f3932fc9d2500b71d2264b7fc437925e98aa63a0531db99e1(
    *,
    count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c3bad6a40a5c81cc6104f50ced259d580601f457ed84cb097df149c39efa61c(
    *,
    input_lambda_processor: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplication.InputLambdaProcessorProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bda17ed8f8889f8c5c6ec56853049a882846d7dcd4f388d5a61d76bb67a4062e(
    *,
    input_schema: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplication.InputSchemaProperty, typing.Dict[builtins.str, typing.Any]]],
    name_prefix: builtins.str,
    input_parallelism: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplication.InputParallelismProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    input_processing_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplication.InputProcessingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kinesis_firehose_input: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplication.KinesisFirehoseInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kinesis_streams_input: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplication.KinesisStreamsInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd2da19040f32bac6b97add291b5e9aa3a4820f542f0ab1f762c126e1fee2a72(
    *,
    record_columns: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplication.RecordColumnProperty, typing.Dict[builtins.str, typing.Any]]]]],
    record_format: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplication.RecordFormatProperty, typing.Dict[builtins.str, typing.Any]]],
    record_encoding: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d166bde9431c4d007eb62ac8076c3b29ac6c26bd12d100bc0664f16a07741770(
    *,
    record_row_path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d104bb127b0f03f200db1dbbaec46e3975c27787da6c5b5267a6827ce0b4171a(
    *,
    resource_arn: builtins.str,
    role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36461ab81a12ff5e6237be1b93ce731867343ce8aa41246829064d95f4c4797d(
    *,
    resource_arn: builtins.str,
    role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02778d83ebd86d283335f90e321ab7c8f68ab8ec791bddee47d1f30fcb001f2b(
    *,
    csv_mapping_parameters: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplication.CSVMappingParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    json_mapping_parameters: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplication.JSONMappingParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48cc42f79151b8ca76858bf0a39020b67d9e0f090ca7a6cf17135183e7fa8b2e(
    *,
    name: builtins.str,
    sql_type: builtins.str,
    mapping: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61bf56eaeaf82967d3cce8d5f6d80e5688d48dc2a0fa909072e76989592896c7(
    *,
    record_format_type: builtins.str,
    mapping_parameters: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplication.MappingParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77e02c50565dc001014a01a3f112ec517d53d8932d42e6e7d59db3991a10752f(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    application_name: builtins.str,
    cloud_watch_logging_option: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationCloudWatchLoggingOptionV2.CloudWatchLoggingOptionProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42c7b0b917b4d2688ea2bca2a3ef8a6ba2a343bfb65c6e1f22c47dea3b1a496a(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0eb6e277e62d9e3fd460706970d0ccfbd75ceac4b6aede3b21bb228ea61ebe2a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4de55c4421a87d36217166859de1aeafa9380105be2ba8f307f523c5316c439e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58439338ee062af482eac743ac4b486000ed403b365ffffbc8fc5b37f1015429(
    value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnApplicationCloudWatchLoggingOptionV2.CloudWatchLoggingOptionProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a38f2053b120441c24bd925839205cb2f122e8ae54bab1ccd34a6d2a1735aa1f(
    *,
    log_stream_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bb49e7696e279c60519c21a5e9b20be4a6f8105cdaf64deb11e8490f4026329(
    *,
    application_name: builtins.str,
    cloud_watch_logging_option: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationCloudWatchLoggingOptionV2.CloudWatchLoggingOptionProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5229b72c55c9ec1a70a752b7ea4f36bff192ae73ffa20446027922b504c3bd47(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    application_name: builtins.str,
    output: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationOutput.OutputProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6025a5c38c69b4d29ab92a1915f1da8b80625f3badc9cf792b257c1dff86c8c7(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9914019c427934fc10d9c5ef3dc89ef025341e280f5d497093181fe6701f3f3b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc3a048e176d5104ca1727f912df4d30999391d1231319db24eebd119c7eda2b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fe64ac80e7fe311d7dc21dff57e45546ccf0fe7d29e582548c2d160d32470b8(
    value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnApplicationOutput.OutputProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25a29ae8b211eff60f243f6354dfda6840bff9cf9146e43c2c19f43c0a84b583(
    *,
    record_format_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87d4d7c5ca82e97c714ea59e212dc136025c2a5396d44e0c070f877ee141982d(
    *,
    resource_arn: builtins.str,
    role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75428eda82ae3ebe39f533c57f88cc57a5be1ca60c456b4175aff4b5d1f7ca29(
    *,
    resource_arn: builtins.str,
    role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1b283619392a3fa63d6c03e676b8a6a33528e0e32a43300e90cb3b0962ac688(
    *,
    resource_arn: builtins.str,
    role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1110074cda4eca6c6baff3f4e75bd112bad6528b90687200b080e88991054fe(
    *,
    destination_schema: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationOutput.DestinationSchemaProperty, typing.Dict[builtins.str, typing.Any]]],
    kinesis_firehose_output: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationOutput.KinesisFirehoseOutputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kinesis_streams_output: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationOutput.KinesisStreamsOutputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    lambda_output: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationOutput.LambdaOutputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbc34d8b567a52fbe3b9065874429ecc60b290de7e8b59020fe6e8e33ca74fb2(
    *,
    application_name: builtins.str,
    output: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationOutput.OutputProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__867c8fd92db8504a1076451d89e6d22bbbaf5ed11d87c0a07e0d573683fedf41(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    application_name: builtins.str,
    output: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationOutputV2.OutputProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e80fcd45e56a2891d9ba87acea691afe6f274873237a3bab86b8e828706e4935(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14ed88b9d3086377681a2689a41a980abb24bc0d0113a6005c8ca74124c4836a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b59fa77e2c0332f5a6cbb3d58a719518ae89fb2132666d64e0c775aee4b6cfde(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5954b4a1d7646d8e17ffb1231cf43daab2dd42c678a2ad58a884b9c8a06359b(
    value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnApplicationOutputV2.OutputProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9385cd408d5be727dae9f859288dd0ca5006e0e95d58288866d52bf26e97f1c7(
    *,
    record_format_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c1487dfe1a7f9d117e17be7ff927e4d17fd2f8902372013007a62ba0bbd0f5e(
    *,
    resource_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75d789c62fcd2dca1e7d7416e99312388e2a2f09a47a3fe9556b55af7bd4bc87(
    *,
    resource_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7cd31a34a9cc14f01936e576adc40a1a574f6b79520943e453ac7c47d96f256(
    *,
    resource_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63140470e878b081e70d74561d7050821df2fc723b52bd9d1e8d4fbb7c921d19(
    *,
    destination_schema: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationOutputV2.DestinationSchemaProperty, typing.Dict[builtins.str, typing.Any]]],
    kinesis_firehose_output: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationOutputV2.KinesisFirehoseOutputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kinesis_streams_output: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationOutputV2.KinesisStreamsOutputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    lambda_output: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationOutputV2.LambdaOutputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc1d3254af5c8202efccb3d570a7c2d03927d2a7c1eeca6cb1763bb1aeeac46d(
    *,
    application_name: builtins.str,
    output: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationOutputV2.OutputProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fb160a2e8a7875ab724e2eb7e0fba236734e0241ad51f9a6725060acdc87383(
    *,
    inputs: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[typing.Union[CfnApplication.InputProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable]]],
    application_code: typing.Optional[builtins.str] = None,
    application_description: typing.Optional[builtins.str] = None,
    application_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44b7524227e355ee536eb12a4b2fa4be32bf8b6d39fd1ba2268193cbff72f7d7(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    application_name: builtins.str,
    reference_data_source: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationReferenceDataSource.ReferenceDataSourceProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb5bcff94728a48081af5ba06227e50f77f164c6a0e40f2424ce920feb46e253(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ce761cff42aac9adf870e048443c1c4c76f8a78aedf21c2eb27dcb5ffd9e5ce(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1851c29bf9c1785247cc3f20b8fe0ccda26baefcaf14697e79f376052bc40353(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1151c61e8c048ee068553784f70c8ebd82a4c1564930da1972aa958c604d10a(
    value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnApplicationReferenceDataSource.ReferenceDataSourceProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c33dcc6cd16de9112b4380ce2ab5204cdeb7a783975c66da00cb15702e1642d(
    *,
    record_column_delimiter: builtins.str,
    record_row_delimiter: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24b04b499ed866076d6ce95ccc747c7667940b9bff6a2e8109c0744ff90310ba(
    *,
    record_row_path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96af8c039b9c6385ba901e70d0aea360c88d50b0d6adba0a02eb254e568d13d8(
    *,
    csv_mapping_parameters: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationReferenceDataSource.CSVMappingParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    json_mapping_parameters: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationReferenceDataSource.JSONMappingParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5aa4a67ad65a86ce398eef47607af181e7f0fdea5ee51cfbede2fd6d9f1c274(
    *,
    name: builtins.str,
    sql_type: builtins.str,
    mapping: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd14c1b93e0f993cc2c3576391f0e9fa3c5ba4e10c6deed7c679c30122afd5dd(
    *,
    record_format_type: builtins.str,
    mapping_parameters: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationReferenceDataSource.MappingParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f77b3888c90d63141853bf991c0930bcc10902696a82fd88fe5dec4452cdd85e(
    *,
    reference_schema: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationReferenceDataSource.ReferenceSchemaProperty, typing.Dict[builtins.str, typing.Any]]],
    s3_reference_data_source: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationReferenceDataSource.S3ReferenceDataSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    table_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0284401ad93061471f850b937fd451f07a4368ec180aab1819e549c069cce9c5(
    *,
    record_columns: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationReferenceDataSource.RecordColumnProperty, typing.Dict[builtins.str, typing.Any]]]]],
    record_format: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationReferenceDataSource.RecordFormatProperty, typing.Dict[builtins.str, typing.Any]]],
    record_encoding: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f6f75dbfa630f90e100fa5681be0776acb38c9a1b7bda1533304ff3a7ff2aa2(
    *,
    bucket_arn: builtins.str,
    file_key: builtins.str,
    reference_role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92a8527f2427122a8173207c8e9888711aec44d7da2255b630415cd609b8c6b6(
    *,
    application_name: builtins.str,
    reference_data_source: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationReferenceDataSource.ReferenceDataSourceProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24bc9def8c3de881e5cf426f42df5cf0bd4fa4aec91c12f7d97b7f67feb820be(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    application_name: builtins.str,
    reference_data_source: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationReferenceDataSourceV2.ReferenceDataSourceProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20be1b39b2c9885d7b363da733146e5f4d406da6505570f00a3ef6c536ca3b00(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4af076368f1ce80003383d92ba56cc8d6e1a7371daff88bc595eb4c668e2c1fb(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__426041050bbd9563ce605756c50b2a58518fe882f0643cd6a9d9668c01610286(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05a8e39fad9c7cf863fabb2e166b301cbd52e0fb17de9403fca4ffccfd2c1863(
    value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnApplicationReferenceDataSourceV2.ReferenceDataSourceProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4646d32b18f2793a3efd4056b74bc1abb82850fe640ec2088423e5b9e355535b(
    *,
    record_column_delimiter: builtins.str,
    record_row_delimiter: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8cd316cebf5f1bbe2f0206dcdb7cf88b9884704079071b0f6001f1106a0bc23(
    *,
    record_row_path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6289c96578bc463c638bff60a3e3c713e3200113b6b491684214db8ea85bad4(
    *,
    csv_mapping_parameters: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationReferenceDataSourceV2.CSVMappingParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    json_mapping_parameters: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationReferenceDataSourceV2.JSONMappingParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__235f04e21304f85ec348f9a1c6ab176c37acba60aa0aaf642a6747595fa3406d(
    *,
    name: builtins.str,
    sql_type: builtins.str,
    mapping: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9c7e6f72c9d25dfb44c69c3636f4abcf5c4e4e457977af92a0b800d19e85133(
    *,
    record_format_type: builtins.str,
    mapping_parameters: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationReferenceDataSourceV2.MappingParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7f4fd7833a40d2525cb8872830d87dac80ef1f875c1037e5557053a8d113dff(
    *,
    reference_schema: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationReferenceDataSourceV2.ReferenceSchemaProperty, typing.Dict[builtins.str, typing.Any]]],
    s3_reference_data_source: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationReferenceDataSourceV2.S3ReferenceDataSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    table_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71a577f7cef0135eb9474b3547ec0e2a1b3769689b87e57b2b177a9566dbff6a(
    *,
    record_columns: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationReferenceDataSourceV2.RecordColumnProperty, typing.Dict[builtins.str, typing.Any]]]]],
    record_format: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationReferenceDataSourceV2.RecordFormatProperty, typing.Dict[builtins.str, typing.Any]]],
    record_encoding: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__709b4b4610557c20d1721e1ccc642548825b5f541a00b361c6cfa760095a2266(
    *,
    bucket_arn: builtins.str,
    file_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8abaabd6b0697ff27dcddbc4444c86abc5ce7a20c68c88d8cc56a7749dde3c1d(
    *,
    application_name: builtins.str,
    reference_data_source: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationReferenceDataSourceV2.ReferenceDataSourceProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9eeabf2dab4475e291f514ae569b69c819c023305785983786a6b8f885c5cd5c(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    runtime_environment: builtins.str,
    service_execution_role: builtins.str,
    application_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.ApplicationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    application_description: typing.Optional[builtins.str] = None,
    application_maintenance_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.ApplicationMaintenanceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    application_mode: typing.Optional[builtins.str] = None,
    application_name: typing.Optional[builtins.str] = None,
    run_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.RunConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ab979335d272b54385ec51a33e6197a1f1bbd114270a16401a86b7ed4fd0729(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b1296e63ca5206494404f96c01aa8ac377b8c08b77ff4a0a1f5547e4a213f6b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea26b50ff4a0040f3d5ca977a91aafa1b52156384f8c8ee00c424e80cfade2e1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1ec6f17b3e294209e152984b223657f15e2bfd642e38670ca405d5129b95ff8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f45255dc18cbc9d974e34c13cbacbcc8a7a597259ee5d9451cce0ff5afb32532(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnApplicationV2.ApplicationConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7cfac072ac577168ac4b3d35ff60fd0a75316c20bf8230a1e2dc26232a9c2e6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3ee22eb2d4826420231b97a72fb473adb0e577696c6d65cab483f2acda96133(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnApplicationV2.ApplicationMaintenanceConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e9c83316fa80583cbdf8d5ae302580cbf7665e32af5f7b0ec0852312a99b3f5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f65f06ae39bb2bd68667c0fd563eae860cf18ed760d3b518cae3b1686d5e7bfb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a79ae96564492d92901cea5681dd2b874223e880d54b7603d9de65a79609ddcd(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnApplicationV2.RunConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11ced858fb4a6403eac2fb0ea73af504643aac4a21b74455dd7c22487b69faab(
    *,
    code_content: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.CodeContentProperty, typing.Dict[builtins.str, typing.Any]]],
    code_content_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adedae0450360ea031c7f12fdc58fe9e38249fbd2e5f6df2b66cb768492efe40(
    *,
    application_code_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.ApplicationCodeConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    application_snapshot_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.ApplicationSnapshotConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    environment_properties: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.EnvironmentPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    flink_application_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.FlinkApplicationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sql_application_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.SqlApplicationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_configurations: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.VpcConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    zeppelin_application_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.ZeppelinApplicationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3c28af81947372a5b9ec54172565fe2a7196cf424a8824350888549754d91e3(
    *,
    application_maintenance_window_start_time: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73181ab44c96124057c7e1f462e3a35e99fd6cb83742d4ce705475de1d4ee7df(
    *,
    application_restore_type: builtins.str,
    snapshot_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62be34267931fb3ca9733964f24fde6338a92296b98b866fa5261551661b9921(
    *,
    snapshots_enabled: typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac7b5879ac1fa92709822d232d2377fb551c35b93fc222aa4a14ec01413b718b(
    *,
    record_column_delimiter: builtins.str,
    record_row_delimiter: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d72c420dd8e064238e27f38cc265738d549b5317a046487fe41e328345920689(
    *,
    glue_data_catalog_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.GlueDataCatalogConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5f4a16d58b13b2fa9788f9baea212a8de26108bc477abcbd6fb176bb9b18a88(
    *,
    configuration_type: builtins.str,
    checkpointing_enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    checkpoint_interval: typing.Optional[jsii.Number] = None,
    min_pause_between_checkpoints: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5018e8540b0cb5ef200be9fec4c45b5f4a1bd73f35c9a85cb3275a5c29cfa251(
    *,
    s3_content_location: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.S3ContentLocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    text_content: typing.Optional[builtins.str] = None,
    zip_file_content: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e74e1834c61c6fad636d7bd2378b8af5b15fa7ca997b4fc18f6b3b23fc5b0ef(
    *,
    artifact_type: builtins.str,
    maven_reference: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.MavenReferenceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_content_location: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.S3ContentLocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__622030896182211331c57ed4befc845ea6ec88fcbca0ff17a24f7e9226eeab77(
    *,
    s3_content_location: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.S3ContentBaseLocationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a474487a1bb62dcf5a29014595714218319769466da8d8f9f253c9a9bd9c7c46(
    *,
    property_groups: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.PropertyGroupProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78b1dc8237ecce6a4ce1074e1dba92279736f8f4a110394b64036cebb1fdb612(
    *,
    checkpoint_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.CheckpointConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    monitoring_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.MonitoringConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    parallelism_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.ParallelismConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eec6ce9ab9327e4bc0c12b507ac90007f268452f96cd144be25df0bd4f38093c(
    *,
    allow_non_restored_state: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5503d59073c796705474cba47c5d34a05c6dfeef56c91ea80aaf52212ae89bc(
    *,
    database_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abcc74675d58c2e25b0f95b0c1fe1a9a9c8824cfbd4c68e80e7d43b664035296(
    *,
    resource_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f93451a6b3dc8951b0c68151cdd08fb947b19d0a8bb863c504bc0475d167314f(
    *,
    count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__debb904bbac4fd9fb35adf75ce4af3770860e7d3cba866fd3b2004b007cbfbe9(
    *,
    input_lambda_processor: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.InputLambdaProcessorProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5814f166b40de77db8a8dd3b125b6020e018bf7424e479d37df575b412ea5047(
    *,
    input_schema: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.InputSchemaProperty, typing.Dict[builtins.str, typing.Any]]],
    name_prefix: builtins.str,
    input_parallelism: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.InputParallelismProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    input_processing_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.InputProcessingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kinesis_firehose_input: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.KinesisFirehoseInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kinesis_streams_input: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.KinesisStreamsInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48f3d8de8a9cbcfdacd9ccef8190e96847bd560d9134cd44ba92c8856fd850fb(
    *,
    record_columns: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.RecordColumnProperty, typing.Dict[builtins.str, typing.Any]]]]],
    record_format: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.RecordFormatProperty, typing.Dict[builtins.str, typing.Any]]],
    record_encoding: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7a570e5bc762b99c19eda34dec838cee12d497461e3abead2ca41f3f1ed405b(
    *,
    record_row_path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4593a749409eee1c4a15c54afd161d1dfcd6583d445152df2c78a1f4578ad77(
    *,
    resource_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__048ff7e43924503c1aa6b4dc5f4c93b0de7cb29e431592ebfc0d2f72132f2f8e(
    *,
    resource_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8085a7ac9a94f2612d27fbf2dde753cb1330f65d099d09b6190a18c320484f26(
    *,
    csv_mapping_parameters: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.CSVMappingParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    json_mapping_parameters: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.JSONMappingParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47b603f3420d63acfee6059d061e11eed67a5b676b09c9301e04db0cbc0c8a86(
    *,
    artifact_id: builtins.str,
    group_id: builtins.str,
    version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3211cef7ba767894311acff6375edbc5d8f4622c91dce61e3f8a2b53f48806d3(
    *,
    configuration_type: builtins.str,
    log_level: typing.Optional[builtins.str] = None,
    metrics_level: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ab5347c1eedc4da87f0ba76ac3c4b8a6c23f0100696749aa69c2c33f8d040b3(
    *,
    configuration_type: builtins.str,
    auto_scaling_enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    parallelism: typing.Optional[jsii.Number] = None,
    parallelism_per_kpu: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__099a7b4afd271a44811681d03d9b38f608cfc1262b7e05cb615232f3284d1635(
    *,
    property_group_id: typing.Optional[builtins.str] = None,
    property_map: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e57c255a4355974df7e23bb9e32e3f6fe0123fd84b8f76526ba4fac1ba0717c(
    *,
    name: builtins.str,
    sql_type: builtins.str,
    mapping: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93d7f021f37b7b8e87adbb316c311484e7d3016e44192e70991e362f963613e1(
    *,
    record_format_type: builtins.str,
    mapping_parameters: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.MappingParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74639cb20e6f9d9d15a507ae174fb1314525a03965aad815820e2c7a887a3b40(
    *,
    application_restore_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.ApplicationRestoreConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    flink_run_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.FlinkRunConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7167b363d560bcfe46dbd2d63496f185be4afca4b0a3c36f59045ced8dda06f6(
    *,
    bucket_arn: builtins.str,
    base_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b1da8f64d557313805c24a5815c1840cc27784f5fcf5b620d5bbad81a9fb779(
    *,
    bucket_arn: builtins.str,
    file_key: builtins.str,
    object_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ba6abf1ac5b4329c6f3e661e65c682bc3755088f0c7e2b18279c84e78027ee9(
    *,
    inputs: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.InputProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__327357f6841ab960621386fdfd3e5a10084879071611b1e8550b74e6eb46abbc(
    *,
    security_group_ids: typing.Sequence[builtins.str],
    subnet_ids: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__743da7b5de18410d73e8ac40fdef66769edc9ded035c253ed7e10cc343eaa8cd(
    *,
    catalog_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.CatalogConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    custom_artifacts_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.CustomArtifactConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    deploy_as_application_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.DeployAsApplicationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    monitoring_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.ZeppelinMonitoringConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e112e9d2fda05ec52aae23ada0044cbfac5b0a160e8453ed853c9c18ebaf2ebe(
    *,
    log_level: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__154e6fc7679982e744d86ce87daeaf267e11d389ca8a5533eae5f42e7278a344(
    *,
    runtime_environment: builtins.str,
    service_execution_role: builtins.str,
    application_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.ApplicationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    application_description: typing.Optional[builtins.str] = None,
    application_maintenance_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.ApplicationMaintenanceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    application_mode: typing.Optional[builtins.str] = None,
    application_name: typing.Optional[builtins.str] = None,
    run_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnApplicationV2.RunConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

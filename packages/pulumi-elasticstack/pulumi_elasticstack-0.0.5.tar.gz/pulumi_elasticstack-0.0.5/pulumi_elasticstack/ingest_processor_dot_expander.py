# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'IngestProcessorDotExpanderResult',
    'AwaitableIngestProcessorDotExpanderResult',
    'ingest_processor_dot_expander',
    'ingest_processor_dot_expander_output',
]

@pulumi.output_type
class IngestProcessorDotExpanderResult:
    """
    A collection of values returned by IngestProcessorDotExpander.
    """
    def __init__(__self__, description=None, field=None, id=None, if_=None, ignore_failure=None, json=None, on_failures=None, override=None, path=None, tag=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if field and not isinstance(field, str):
            raise TypeError("Expected argument 'field' to be a str")
        pulumi.set(__self__, "field", field)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if if_ and not isinstance(if_, str):
            raise TypeError("Expected argument 'if_' to be a str")
        pulumi.set(__self__, "if_", if_)
        if ignore_failure and not isinstance(ignore_failure, bool):
            raise TypeError("Expected argument 'ignore_failure' to be a bool")
        pulumi.set(__self__, "ignore_failure", ignore_failure)
        if json and not isinstance(json, str):
            raise TypeError("Expected argument 'json' to be a str")
        pulumi.set(__self__, "json", json)
        if on_failures and not isinstance(on_failures, list):
            raise TypeError("Expected argument 'on_failures' to be a list")
        pulumi.set(__self__, "on_failures", on_failures)
        if override and not isinstance(override, bool):
            raise TypeError("Expected argument 'override' to be a bool")
        pulumi.set(__self__, "override", override)
        if path and not isinstance(path, str):
            raise TypeError("Expected argument 'path' to be a str")
        pulumi.set(__self__, "path", path)
        if tag and not isinstance(tag, str):
            raise TypeError("Expected argument 'tag' to be a str")
        pulumi.set(__self__, "tag", tag)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Description of the processor.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def field(self) -> str:
        """
        The field to expand into an object field. If set to *, all top-level fields will be expanded.
        """
        return pulumi.get(self, "field")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Internal identifier of the resource
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="if")
    def if_(self) -> Optional[str]:
        """
        Conditionally execute the processor
        """
        return pulumi.get(self, "if_")

    @property
    @pulumi.getter(name="ignoreFailure")
    def ignore_failure(self) -> Optional[bool]:
        """
        Ignore failures for the processor.
        """
        return pulumi.get(self, "ignore_failure")

    @property
    @pulumi.getter
    def json(self) -> str:
        """
        JSON representation of this data source.
        """
        return pulumi.get(self, "json")

    @property
    @pulumi.getter(name="onFailures")
    def on_failures(self) -> Optional[Sequence[str]]:
        """
        Handle failures for the processor.
        """
        return pulumi.get(self, "on_failures")

    @property
    @pulumi.getter
    def override(self) -> Optional[bool]:
        """
        Controls the behavior when there is already an existing nested object that conflicts with the expanded field.
        """
        return pulumi.get(self, "override")

    @property
    @pulumi.getter
    def path(self) -> Optional[str]:
        """
        The field that contains the field to expand.
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter
    def tag(self) -> Optional[str]:
        """
        Identifier for the processor.
        """
        return pulumi.get(self, "tag")


class AwaitableIngestProcessorDotExpanderResult(IngestProcessorDotExpanderResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return IngestProcessorDotExpanderResult(
            description=self.description,
            field=self.field,
            id=self.id,
            if_=self.if_,
            ignore_failure=self.ignore_failure,
            json=self.json,
            on_failures=self.on_failures,
            override=self.override,
            path=self.path,
            tag=self.tag)


def ingest_processor_dot_expander(description: Optional[str] = None,
                                  field: Optional[str] = None,
                                  if_: Optional[str] = None,
                                  ignore_failure: Optional[bool] = None,
                                  on_failures: Optional[Sequence[str]] = None,
                                  override: Optional[bool] = None,
                                  path: Optional[str] = None,
                                  tag: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableIngestProcessorDotExpanderResult:
    """
    Expands a field with dots into an object field. This processor allows fields with dots in the name to be accessible by other processors in the pipeline. Otherwise these fields can’t be accessed by any processor.

    See: elastic.co/guide/en/elasticsearch/reference/current/dot-expand-processor.html

    ## Example Usage

    ```python
    import pulumi
    import pulumi_elasticstack as elasticstack

    dot_expander = elasticstack.ingest_processor_dot_expander(field="foo.bar")
    my_ingest_pipeline = elasticstack.IngestPipeline("myIngestPipeline", processors=[dot_expander.json])
    ```


    :param str description: Description of the processor.
    :param str field: The field to expand into an object field. If set to *, all top-level fields will be expanded.
    :param str if_: Conditionally execute the processor
    :param bool ignore_failure: Ignore failures for the processor.
    :param Sequence[str] on_failures: Handle failures for the processor.
    :param bool override: Controls the behavior when there is already an existing nested object that conflicts with the expanded field.
    :param str path: The field that contains the field to expand.
    :param str tag: Identifier for the processor.
    """
    __args__ = dict()
    __args__['description'] = description
    __args__['field'] = field
    __args__['if'] = if_
    __args__['ignoreFailure'] = ignore_failure
    __args__['onFailures'] = on_failures
    __args__['override'] = override
    __args__['path'] = path
    __args__['tag'] = tag
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('elasticstack:index/ingestProcessorDotExpander:IngestProcessorDotExpander', __args__, opts=opts, typ=IngestProcessorDotExpanderResult).value

    return AwaitableIngestProcessorDotExpanderResult(
        description=__ret__.description,
        field=__ret__.field,
        id=__ret__.id,
        if_=__ret__.if_,
        ignore_failure=__ret__.ignore_failure,
        json=__ret__.json,
        on_failures=__ret__.on_failures,
        override=__ret__.override,
        path=__ret__.path,
        tag=__ret__.tag)


@_utilities.lift_output_func(ingest_processor_dot_expander)
def ingest_processor_dot_expander_output(description: Optional[pulumi.Input[Optional[str]]] = None,
                                         field: Optional[pulumi.Input[str]] = None,
                                         if_: Optional[pulumi.Input[Optional[str]]] = None,
                                         ignore_failure: Optional[pulumi.Input[Optional[bool]]] = None,
                                         on_failures: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                         override: Optional[pulumi.Input[Optional[bool]]] = None,
                                         path: Optional[pulumi.Input[Optional[str]]] = None,
                                         tag: Optional[pulumi.Input[Optional[str]]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[IngestProcessorDotExpanderResult]:
    """
    Expands a field with dots into an object field. This processor allows fields with dots in the name to be accessible by other processors in the pipeline. Otherwise these fields can’t be accessed by any processor.

    See: elastic.co/guide/en/elasticsearch/reference/current/dot-expand-processor.html

    ## Example Usage

    ```python
    import pulumi
    import pulumi_elasticstack as elasticstack

    dot_expander = elasticstack.ingest_processor_dot_expander(field="foo.bar")
    my_ingest_pipeline = elasticstack.IngestPipeline("myIngestPipeline", processors=[dot_expander.json])
    ```


    :param str description: Description of the processor.
    :param str field: The field to expand into an object field. If set to *, all top-level fields will be expanded.
    :param str if_: Conditionally execute the processor
    :param bool ignore_failure: Ignore failures for the processor.
    :param Sequence[str] on_failures: Handle failures for the processor.
    :param bool override: Controls the behavior when there is already an existing nested object that conflicts with the expanded field.
    :param str path: The field that contains the field to expand.
    :param str tag: Identifier for the processor.
    """
    ...
